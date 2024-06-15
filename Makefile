include lib/mccole/mccole.mk

## datasets: make all datasets
.PHONY: datasets
datasets: data/lab.db data/designs/.touch data/readings/.touch data/grids/.touch data/map.png

## map: generate map
.PHONY: map
map: data/map.png

data/map.png: bin/map.py data/samples.csv
	python $< \
	--outfile $@ \
	--samples data/samples.csv

## db: generate database
.PHONY: db
db: data/lab.db

data/lab.db: bin/db.py data/assays.json data/samples.csv data/genomes.json
	@mkdir -p data
	python $< \
	--dbfile $@ \
	--assays data/assays.json \
	--samples data/samples.csv \
	--sites params/sites.csv \
	--surveys params/surveys.csv

## plates: generate plate files
.PHONY: plates
plates: data/designs/.touch data/readings/.touch

data/designs/.touch data/readings/.touch: bin/plates.py params/assays.json data/assays.json
	@rm -rf data/designs data/readings
	@mkdir -p data/designs data/readings
	python $< \
	--assays data/assays.json \
	--designs data/designs \
	--params params/assays.json \
	--readings data/readings
	touch data/designs/.touch data/readings/.touch

## assays: generate assay files
.PHONY: assays
assays: data/assays.json

data/assays.json: bin/assays.py params/assays.json data/genomes.json data/samples.csv
	@mkdir -p data
	python $< \
	--genomes data/genomes.json \
	--outfile $@ \
	--params params/assays.json \
	--samples data/samples.csv

## samples: sample snails from survey sites
.PHONY: samples
samples: data/samples.csv

data/samples.csv: bin/samples.py data/genomes.json params/samples.json params/sites.csv params/surveys.csv data/grids/.touch
	@mkdir -p data
	python $< \
	--genomes data/genomes.json \
	--grids data/grids \
	--outfile $@ \
	--params params/samples.json \
	--sites params/sites.csv \
	--surveys params/surveys.csv

## genomes: synthesize genomes
.PHONY: genomes
genomes: data/genomes.json

data/genomes.json: bin/genomes.py params/genomes.json
	@mkdir -p data
	python $< \
	--outfile $@ \
	--params params/genomes.json

## grids: synthesize pollution grids
.PHONY: grids
grids: data/grids/.touch

data/grids/.touch: bin/grid.py params/grids.json params/sites.csv
	@rm -rf data/grids
	@mkdir -p data/grids
	python $< \
	--grids params/grids.json \
	--outdir data/grids \
	--sites params/sites.csv
	touch data/grids/.touch

.PHONY: _clean
_clean:
	@rm -rf data
