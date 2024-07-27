from test_queries import small_db


Q_DELETE_EXP = [
    ('delete from performed where sample_id = ?', 2),
    ('delete from experiment where sample_id = ?', 1),
]


def test_delete_experiment(small_db):
    params = (4,)
    cursor = small_db.cursor()
    for (stmt, count) in Q_DELETE_EXP:
        cursor.execute(stmt, params)
        assert cursor.rowcount == count
