from test_queries import small_db


Q_SELECT_SINGLE_STAFF_EXP = """
select experiment.sample_id, experiment.kind, experiment.start, experiment.end
from staff inner join performed inner join experiment
on
  (staff.staff_id = performed.staff_id)
  and
  (performed.sample_id = experiment.sample_id)
where staff.staff_id = ?
"""


def test_select_single_staff_experiments(small_db):
    actual = small_db.execute(Q_SELECT_SINGLE_STAFF_EXP, (5,)).fetchall()
    assert actual == [
        {'sample_id': 2, 'kind': 'ELISA', 'start': '2024-06-12', 'end': '2024-06-14'},
        {'sample_id': 4, 'kind': 'JESS', 'start': '2024-06-13', 'end': '2024-06-13'}
    ]
