COLUMNS=72
DB=data/lab.db
PY:=$(wildcard *.py)
SQL:=$(wildcard *.sql)
OUT:=$(patsubst %.py,%.out,${PY}) $(patsubst %.sql,%.out,${SQL})

all: ${OUT}

run_queries.out: run_queries.sh run_queries.py queries.py ${DB}
	bash $< > $@

test_queries.out: test_queries.py queries.py
	COLUMNS=${COLUMNS} pytest $< > $@

%.out: %.py ${DB}
	python $< ${DB} > $@

%.out: %.sql ${DB}
	sqlite3 ${DB} < $< > $@
