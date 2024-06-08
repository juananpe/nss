'''Generate sample snails with genomes and locations.'''


import argparse
import json
import math
import numpy as np
from pathlib import Path
import polars as pl
import random
from geopy.distance import lonlat, distance
from params import SampleParams, load_params


LON_LAT_PRECISION = 5
READING_PRECISION = 1
SIZE_PRECISION = 1


def main():
    '''Main driver.'''
    options = parse_args()
    random.seed(options.params.seed)
    genomes = json.loads(Path(options.genomes).read_text())
    grids = load_grids(options)
    samples = generate_samples(options, genomes, grids)
    save(options, samples)


def generate_samples(options, genomes, grids):
    '''Generate snail samples.'''
    params = options.params
    samples = []
    susc_loc = genomes['susceptible_loc']
    susc_base = genomes['susceptible_base']
    for i, seq in enumerate(genomes['individuals']):
        survey_id, point, contaminated = random_geo(options.sites, options.surveys, grids)
        limit = params.mutant if contaminated and (seq[susc_loc] == susc_base) else params.normal
        size = random.uniform(
            params.min_snail_size,
            params.min_snail_size + params.max_snail_size * limit
        )
        samples.append((i + 1, survey_id, point.longitude, point.latitude, seq, size))

    df = pl.DataFrame(samples, schema=('sample_id', 'survey_id', 'lon', 'lat', 'sequence', 'size'))
    df = df.with_columns(
        lon=df['lon'].round(LON_LAT_PRECISION),
        lat=df['lat'].round(LON_LAT_PRECISION),
        size=df['size'].round(SIZE_PRECISION),
    )

    return df


def load_grids(options):
    '''Load all grid files.'''
    return {
        s: np.loadtxt(Path(options.grids, f'{s}.csv'), dtype=int, delimiter=',')
        for s in set(options.surveys['site_id'])
    }


def parse_args():
    '''Parse command-line arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--genomes', type=str, required=True, help='genome file')
    parser.add_argument('--grids', type=str, required=True, help='grids directory')
    parser.add_argument('--outfile', type=str, help='output file')
    parser.add_argument('--params', type=str, required=True, help='parameter file')
    parser.add_argument('--sites', type=str, required=True, help='sites parameter file')
    parser.add_argument('--surveys', type=str, required=True, help='surveys parameter file')
    options = parser.parse_args()
    assert options.params != options.outfile, 'Cannot use same filename for options and parameters'
    options.params = load_params(SampleParams, options.params)
    options.surveys = pl.read_csv(options.surveys)
    options.sites = pl.read_csv(options.sites)
    return options


def random_geo(sites, surveys, grids):
    '''Select random point from one of the sample grids.'''
    survey_row = random.randrange(surveys.shape[0])
    survey_id = surveys.item(survey_row, 'survey_id')
    spacing = float(surveys.item(survey_row, 'spacing'))
    site_id = surveys.item(survey_row, 'site_id')
    site_row = sites['site_id'].to_list().index(site_id)
    site_lon = sites.item(site_row, 'lon')
    site_lat = sites.item(site_row, 'lat')

    grid = grids[site_id]
    width, height = grid.shape
    rand_x, rand_y = random.randrange(width), random.randrange(height)
    contaminated = bool(grid[rand_x, rand_x])

    corner = lonlat(site_lon, site_lat)
    rand_x *= spacing
    rand_y *= spacing
    dist = math.sqrt(rand_x**2 + rand_y**2)
    bearing = math.degrees(math.atan2(rand_y, rand_x))
    point = distance(meters=dist).destination(corner, bearing=bearing)

    return survey_id, point, contaminated


def save(options, samples):
    '''Save or show results.'''
    if options.outfile:
        samples.write_csv(Path(options.outfile))
    else:
        samples.write_csv(sys.stdout)


if __name__ == '__main__':
    main()
