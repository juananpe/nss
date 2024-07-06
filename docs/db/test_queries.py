from collections import namedtuple
import pytest
import queries
import sqlite3


def dict_factory(connection, row):
    fields = [column[0] for column in connection.description]
    return {key: value for key, value in zip(fields, row)}


CREATE = '''
CREATE TABLE staff (
	staff_id BIGINT, 
	personal TEXT, 
	family TEXT
);
CREATE TABLE experiment (
	sample_id BIGINT, 
	kind TEXT, 
	start TEXT, 
	"end" TEXT
);
CREATE TABLE performed (
	staff_id BIGINT, 
	sample_id BIGINT
);
'''
STAFF = (
    (5, 'Al', 'Pha'),
    (7, 'Be', 'Ta'),
)
EXPERIMENTS = (
    (2, 'ELISA', '2024-06-12', '2024-06-14'),
    (3, 'ELISA', '2024-06-12', None),
    (4, 'JESS', '2024-06-13', '2024-06-13'),
)
PERFORMED = (
    (5, 2),
    (7, 3),
    (5, 4),
    (7, 4),
)


@pytest.fixture
def small_db():
    connection = sqlite3.connect(':memory:')
    connection.row_factory = dict_factory
    connection.executescript(CREATE)
    connection.executemany('insert into staff values(?, ?, ?)', STAFF)
    connection.executemany('insert into experiment values(?, ?, ?, ?)', EXPERIMENTS)
    connection.executemany('insert into performed values(?, ?)', PERFORMED)
    return connection


def test_all_staff_alpha(small_db):
    actual = small_db.execute(queries.Q_ALL_STAFF_ALPHA).fetchall()
    assert actual == [
        {'name': 'Al Pha'},
        {'name': 'Be Ta'},
    ]


def test_count_exp_by_staff(small_db):
    actual = small_db.execute(queries.Q_COUNT_EXP_BY_STAFF).fetchall()
    assert actual == [
        {'staff_id': 5, 'num_experiments': 2},
        {'staff_id': 7, 'num_experiments': 2}
    ]
