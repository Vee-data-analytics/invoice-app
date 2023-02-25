import pandas as pd
import plotly.express as px

import plotly.offline as pyo
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from positions.models import Position

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('payed_bar', external_stylesheets=external_stylesheets)

qs = Position.objects.filter()

invoice_data = [
        {
            'Invoice':x.invoice.invoice_number,
            'Client':x.invoice.clients.name,
            'Issued date':x.created,
            'Close':x.invoice.closed,
            'Amount':x.amount,
            'Title':x.title,
            'Payed':x.invoice.payed,

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
                 {'name':'Payed', 'id': 'Payed', 'deletable':False, 'renamable': False},
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




@app.callback(
    Output('bar_graph', 'figure'),
    [Input('our-table', 'data')])
def make_graphs(data):
        df_fig = pd.DataFrame(data)
        bar_fig = px.bar(df_fig, x='Invoice', y='Amount', color='Payed')
        return bar_fig

@app.callback(
    Output('my_graph', 'figure'),
    [Input('our-table', 'data')])
def make_graphs(data):
        df_fig = pd.DataFrame(data)
        bar_fig = px.pie(df_fig, values='Amount', names='Invoice', color='Payed')
        return bar_fig
