# -*- coding: utf-8 -*-
from dash import Dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout =  dbc.Container(
    [
        dcc.Store(id="store"),
        html.Br([]),
        html.H1('Dash Tabs component demo'),
        html.Div([
    dcc.Input(id='input-1-state', type='text', value=''),
    dcc.Input(id='input-2-state', style={"margin-left": "45px"}, type='password', value=''),
    html.Button(id='submit-button-state',style={"margin-left": "25px"}, n_clicks=0, children='Submit'),
    html.Div(id='output-state')
]),
    html.Br([]),
    html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style)
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
]),
    html.Div([
        dcc.Checklist(
            id="all-or-none",
            options=[{"label": "Select All", "value": "All"}],
            value=[],
            labelStyle={"display": "inline-block", "margin-left": "25px"},
        ),
        dcc.Checklist(
            id="my-checklist",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value=[],
            labelStyle={"display": "inline-block","margin-left": "25px"},
        ),
    ])
    
    ]
)


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))              
def update_output(n_clicks, input1,input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        Input 2 is "{}"
    '''.format(n_clicks, input1,input2)



'''
app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style)
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])
'''

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1'),
            ])            
             
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])

@app.callback(
    Output("my-checklist", "value"),
    [Input("all-or-none", "value")],
    [State("my-checklist", "options")],
    )
def select_all_none(all_selected, options):
    all_or_none = []
    all_or_none = [option["value"] for option in options if all_selected]
    return all_or_none



if __name__ == '__main__':
    app.run_server(debug=True)
