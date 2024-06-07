# snailz

A set of synthetic data generators for teaching data science.

## Overview

These data generators model genomic analysis of snails in the Pacific Northwest
that are growing to unusual size as a result of exposure to pollution.
The workflow shown in in the diagram below simulates the following:

-   One or more *surveys* are conducted at one or more *sites*.
-   Each survey collects *genomes* and *sizes* of snails.
-   A *grid* at each site is marked out to show the presence or absence of pollution.
-   *Laboratory staff* perform *assays* of the snails' genetic material.
-   Each assay plate has a *design* showing the material applied and *readings* showing the measured response.
-   Plates may be *invalidated* after the fact if a staff member believes it is contaminated.

![workflow][workflow.svg]

## Usage

1.  Create a fresh Python environment: `mamba create -y -n snailz python=3.12`
2.  Activate that environment: `mamba activate snailz`
3.  Install required packages: `pip install -r requirements.txt`
4.  View available commands: `make` or `make commands`
5.  Synthesize datasets: `make datasets`

## Parameters

`./params` contains the parameter files used to control data generation.

-   Sites: `sites.csv`
    -   `site_id`: unique label for site (text)
    -   `lon`: longitude of site reference marker (deg)
    -   `lat`: latitude of site reference marker (deg)
-   Surveys: `surveys.csv`
    -   `survey_id`: unique label for survey (text)
    -   `site_id`: ID of site where survey was conducted (text)
    -   `date`: date that survey was conducted (date, YYYY-MM-DD)
    -   `spacing`: spacing of measurement point (float, meters)
-   Genomes: `genomes.json`
    -   `length`: number of base pairs in sequences (int > 0)
    -   `num_genomes`: how many individuals to generate (int > 0)
    -   `num_snp`: number of single nucleotide polymorphisms (int > 0)
    -   `prob_other`: probability of non-significant mutations (float in 0..1)
    -   `seed`: RNG seed (int > 0)
    -   `snp_probs`: probability of selecting various bases (list of 4 float summing to 1.0)
-   Grids: `grids.json`
    -   `depth`: range of random values per cell (int > 0)
    -   `height`: number of cells on Y axis (int > 0)
    -   `seed`: RNG seed (int > 0)
    -   `width`: number of cells on X axis (int > 0)
-   Assays: `assays.json`
    -   `startdate`: start of all experiments
    -   `enddate`: end of all experiments
    -   `filename_length`: length of stem of design/readings filenames (int > 0)
    -   `locale": locale to use when generating staff names (text)
    -   `invalid`: probability of plate being invalidted (float in 0..1)
    -   `staff`: number of staff (int > 0)
    -   `control`: nominal reading value for control wells (float > 0)
    -   `treated`: nominal reading value for treated well (float > 0)
    -   `seed`: RNG seed (int > 0)
    -   `stdev`: standard deviation on readings (float > 0)
    -   `treatment": label to use for treated wells (text)
    -   `controls`: labels to used for control wells (list of text)
    -   `experiments`: controls for multiple types of experiments
        -   key: experiment type (text)
        -   `staff`: number of staff involved (list of int)
	-   `duration`: number of days experiment took (int >= 0)
	-   `plates`: number of plates used in experiment (int > 0)

## Datasets

`./data` contains all the generated data.

-   Genomes: `genomes.json`
    -   `length`: number of base pairs (int > 0)
    -   `reference`: the unmutated reference genome (text)
    -   `individuals`: sequences for individuals (list of text)
    -   `locations`: locations of mutations (list of int)
    -   `susceptible_loc`: location of mutation of interest (int >= 0)
    -   `susceptible_base`: mutated base responsible for size change (char)
-   Grids: `grids/*.csv` (one file per site)
    -   1/0: presence/absence of contamination at sample location
-   Samples: `grids/samples.csv`
    -   `sample_id`: unique ID for genetic sample (text)
    -   `survey_id`: which survey it was taken in (text)
    -   `lon`: longitude of sample site (float)
    -   `lat`: latitude of sample site (float)
    -   `sequence`: sampled gene sequence (text)
    -   `size`: snail weight (float, grams)
-   Assays: `assays.json`
    -   `staff`:
        -   `staff_id`: unique staff member identifier (int > 0)
	-   `personal`: personal name (text)
	-   `family`: family name (text)
    -   `experiment`: experiment details
        -   `sample_id`: sample that experiment used (int > 0)
	-   `kind`: "ELISA" or "JESS" (text)
	-   `start`: start date (date, YYYY-MM-DD)
	-   `end`: end date (date, YYYY-MM-DD or None if experiment incomplete)
    -   `performed`: join table showing who performed which experiments
        -   `staff_id`: foreign key to `staff`
	-   `sample_id`: foreign key to `experiment`
    -   `plate`: details of assay plates used in experiments
        -   `plate_id`: unique plate identifier (int > 0)
	-   `sample_id`: foreign key to `sample` (text)
	-   `date`: date plate was run (date, YYYY-MM-DD)
	-   `filename`: name of design and results files (text)
    -   `invalidated`: which plates have been invalidated
        -   `plate_id`: foreign key to plate (text)
	-   `staff_id`: foreign key to staff member responsible (text)
	-   `date`: invalidation date (date, YYYY-MM-DD)
-   `designs/*.csv`: assay plate designs
    -   header: machine type, file type ("design" or "readings"), staff ID
    -   blank line
    -   table with column and row titles showing material in each well
-   `readings/*.csv`: assay plate readings
    -   header: machine type, file type ("design" or "readings"), staff ID
    -   blank line
    -   table with column and row titles showing reading from each well

## Database

`data/lab.db` is structured as shown below.
Note that the data from `assays.json` is split between several tables.

![database schema][db-schema.svg]
