#https://www.nelsontang.com/Dash-Bootstrap-KPI-Card/

import dash  # (version 1.12.0) pip install dash

import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.Div([
    dbc.Row(dbc.Col(html.H1("H1 Text"))),
])

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "$10.5 M",
                    className="card-value",
                ),
                html.P(
                    "Target: $10.0 M",
                    className="card-target",
                ),
                html.Span(
                    "Up ",
                    className="card-diff-up",
                ),
                html.Span(
                    "5.5% vs Last Year",
                    className="card-diff-up",
                ),

            ]
        ),
    ],
)

row = html.Div(
    [
        dbc.CardLink(
            [
                card,
                card,
                card,
            ]
        ),
    ], style={'padding': '25px'}
)

app.layout = html.Div([
    header,
    row,
    row
])

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
