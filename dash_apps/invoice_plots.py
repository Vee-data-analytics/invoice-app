
import base64
import datetime
import io

import pandas as pd
import plotly.express as px

from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
from positions.models import Position

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('invoice_bar', external_stylesheets=external_stylesheets)


qs = Position.objects.all()

invoice_data = [
        {
            'Invoice':x.invoice.invoice_number,
            'Client':x.invoice.clients.name,
            'Issued date':x.created,
            'Close':x.invoice.closed,
            'Amount':x.amount,
            'Title':x.title,

        } for x in qs
    ]

df = pd.DataFrame(invoice_data)

app.layout= html.Div([
    dash_table.DataTable(
        id='our-table',

        columns=[
                 {'name':'Invoice', 'id':'Invoice', 'deletable':False, 'renamable':False},
                 {'name':'Issued date', 'id': 'Issued date', 'deletable':False, 'renamable': False},
                 {'name':'Amount', 'id': 'Amount', 'deletable':False, 'renamable':False},
                 {'name':'Client', 'id': 'Client', 'deletable':False, 'renamable': False},
                 {'name':'Close', 'id': 'Close', 'deletable':False, 'renamable': False}],
                 
        data=df.to_dict('records'),
        editable=True,                  # allow user to edit data inside tabel
        row_deletable=True,             # allow user to delete rows
        sort_action="native",           # give user capability to sort columns
        sort_mode="single",             # sort across 'multi' or 'single' columns
        filter_action="native",         # allow filtering of columns
        page_action='none',             # render all of the data at once. No paging.
           style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
    style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
    
    ),
    dcc.Graph(id='bar_graph', config= {'displaylogo': False}),
    dcc.Graph(id='my_graph', config= {'displaylogo': False})

])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable('our-table')
    ])

#------------------------------------------------------------------------------------------------------------

@app.callback(Output('output-data', 'children'),
              [Input('psql-data', 'contents')],
              [State('psql-data', 'filename'),
               State('psql-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children




@app.callback(
    Output('bar_graph', 'figure'),
    [Input('our-table', 'data')])
def make_graphs(data):
        df_fig = pd.DataFrame(data)
        bar_fig = px.bar(df_fig, x='Invoice', y='Amount', color='Close')
        bar_fig.update_yaxes()
        return bar_fig

@app.callback(
    Output('my_graph', 'figure'),
    [Input('our-table', 'data')])
def make_graphs(data):
        df_fig = pd.DataFrame(data)
        pie_fig = px.pie(df_fig, values='Amount', names='Invoice')
        pie_fig.update_traces(textinfo='percent+label')
        return pie_fig

