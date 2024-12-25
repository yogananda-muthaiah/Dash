# -*- coding: utf-8 -*-
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value=''),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'))              
def update_output(n_clicks, input1):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}"
    '''.format(n_clicks, input1)



if __name__ == '__main__':
    app.run_server(debug=True)
