COLUMNS=72
DB_SRC=../../data/lab.db
DB=lab.db
PY:=$(wildcard *.py)
SQL:=$(wildcard *.sql)
OUT:=$(patsubst %.py,%.out,${PY}) $(patsubst %.sql,%.out,${SQL})

all: ${OUT}

run_queries.out: run_queries.sh run_queries.py queries.py
	@cp ${DB_SRC} ${DB}
	bash $< > $@

test_%.out: test_%.py queries.py
	COLUMNS=${COLUMNS} pytest $< > $@

%.out: %.py
	@cp ${DB_SRC} ${DB}
	python $< ${DB} > $@

%.out: %.sql
	@cp ${DB_SRC} ${DB}
	sqlite3 ${DB} < $< > $@
