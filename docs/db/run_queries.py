import queries
import sqlite3
import sys

AVAILABLE = list(sorted(q for q in dir(queries) if q.startswith('Q_')))
USAGE = f'Usage: run_queries.py db_path [{" | ".join(AVAILABLE)}]'

def dict_factory(connection, row):
    fields = [column[0] for column in connection.description]
    return {key: value for key, value in zip(fields, row)}

if (len(sys.argv) != 3) or (sys.argv[2] not in AVAILABLE):
    print(USAGE, file=sys.stderr)
    sys.exit(1)

sql = getattr(queries, sys.argv[2])
connection = sqlite3.connect(sys.argv[1])
connection.row_factory = dict_factory
for row in connection.execute(sql):
    print(row)
