'''Create map of survey points.'''

import argparse
import plotly.graph_objects as go
import polars as pl


def main():
    '''Main driver.'''
    options = parse_args()
    samples = pl.read_csv(options.samples)['survey_id', 'lon', 'lat']
    fig = go.Figure(go.Scattermapbox(
        lon=samples['lon'],
        lat=samples['lat'],
        marker=go.scattermapbox.Marker(color=samples['survey_id']),
    ))
    fig.update_layout(
        mapbox={
            'style': 'open-street-map',
            'center': {'lon': -124.2, 'lat': 48.85},
            'zoom': 11,
        },
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    )
    fig.show()
    if options.outfile:
        fig.write_image(options.outfile)


def parse_args():
    '''Get command-line arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', type=str, required=True, help='output file name')
    parser.add_argument('--samples', type=str, required=True, help='samples data file')
    return parser.parse_args()


if __name__ == '__main__':
    main()
