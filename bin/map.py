'''Create map of survey points.'''

import argparse
import plotly.express as px
import polars as pl


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
OPACITY = 0.25


def main():
    '''Main driver.'''
    options = parse_args()
    df = pl.read_csv(options.samples)
    df = df.cast({'survey_id': pl.String}).cast({'survey_id': pl.Categorical})
    fig = px.scatter_mapbox(df, lat='lat', lon='lon', color='survey_id', opacity=OPACITY, mapbox_style='white-bg')
    if options.outfile is not None:
        fig.write_image(options.outfile)
    else:
        fig.show()


def parse_args():
    '''Get command-line arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', type=str, default=None, help='output file name')
    parser.add_argument('--samples', type=str, required=True, help='samples data file')
    return parser.parse_args()


if __name__ == '__main__':
    main()
