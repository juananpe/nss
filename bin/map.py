'''Create map of survey points.'''

import argparse
import pandas as pd
import plotly.express as px


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
OPACITY = 0.5


def main():
    '''Main driver.'''
    options = parse_args()
    df = pd.read_csv(options.samples)
    df['survey_id'] = df['survey_id'].astype(str)
    fig = px.scatter_mapbox(df, lat='lat', lon='lon', color='survey_id', opacity=OPACITY, mapbox_style='white-bg')
    fig.write_image(options.outfile)


def parse_args():
    '''Get command-line arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', type=str, required=True, help='output file name')
    parser.add_argument('--samples', type=str, required=True, help='samples data file')
    return parser.parse_args()


if __name__ == '__main__':
    main()
