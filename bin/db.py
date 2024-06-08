'''Generate database from data files.'''

import argparse
import json
import polars as pl


def main():
    '''Main driver.'''
    options = parse_args()
    url = f'sqlite:///{options.dbfile}'

    csv_to_db(url, 'sample', options.samples)
    csv_to_db(url, 'site', options.sites)
    csv_to_db(url, 'survey', options.surveys, 'survey_id', 'site_id', 'date')

    assays = json.load(open(options.assays, 'r'))
    json_to_db(url, assays, 'staff')
    json_to_db(url, assays, 'experiment')
    json_to_db(url, assays, 'performed')
    json_to_db(url, assays, 'plate')
    json_to_db(url, assays, 'invalidated')


def csv_to_db(url, name, source, *columns):
    '''Create table from CSV.'''
    df = pl.read_csv(source)
    if columns:
        df = df[list(columns)]
    df.write_database(name, url, if_table_exists='replace')


def json_to_db(url, data, name):
    '''Create table from JSON.'''
    df = pl.DataFrame(data[name])
    df.write_database(name, url, if_table_exists='replace')


def parse_args():
    '''Parse command-line arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--assays', type=str, required=True, help='assay data file')
    parser.add_argument('--dbfile', type=str, required=True, help='output database file')
    parser.add_argument('--samples', type=str, required=True, help='samples data file')
    parser.add_argument('--sites', type=str, required=True, help='sites parameter file')
    parser.add_argument('--surveys', type=str, required=True, help='surveys parameter file')
    return parser.parse_args()


if __name__ == '__main__':
    main()
