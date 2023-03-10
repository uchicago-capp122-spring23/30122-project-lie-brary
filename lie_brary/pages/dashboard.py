'''
This file contains the dashboard page.
# Author: Reza R Pratama
'''

import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import lie_brary.scripts.dashboard.helper as helper
import lie_brary.scripts.dashboard.visualization as viz

dash.register_page(__name__,  path='/')

# Import Data
data = helper.dashboard_load_data()

# Dropdowns Menu
dropdown_sentiment = dbc.Card([

    html.Div([
    # sentiment dropdown label
    html.P('Filter by Sentiment:',
           style={'margin-top':'20px', 'margin-bottom':'0px', 'padding-bottom':'0px'}),
    dcc.Dropdown(id='sentiment_dropdown',
                options=helper.sentiment_options,
                multi=True,
                value=list(helper.SENTIMENT)
                ),

    # fact dropdown label
    html.P('Filter by the Label:',
           style={'margin-top':'20px', 'margin-bottom':'0px', 'padding-bottom':'0px'}),
    dcc.Dropdown(id='fact_dropdown',
                options=helper.fact_options,
                multi=True,
                value=list(helper.FACT)
                ),

    # source dropdown label
    html.P('Filter by the Source:',
           style={'margin-top':'20px', 'margin-bottom':'0px', 'padding-bottom':'0px'}),
    dcc.Dropdown(id='source_dropdown',
                options=helper.source_options,
                multi=True,
                value=list(helper.SOURCE)
                ),

    # source dropdown label
    html.P('Filter by the Keyword:',
           style={'margin-top':'20px', 'margin-bottom':'0px', 'padding-bottom':'0px'}),
    dcc.Dropdown(id='keyword_dropdown',
                options=helper.keyword_options,
                multi=True,
                value=list(helper.KEYWORD)
                )
])

], body=True, color='light')


# LAYOUT PAGE
layout = html.Div([
    # Dropdowns Menu
    dbc.Row([
        dbc.Col(dropdown_sentiment, md=4, style={'margin-top':'20px'}),
        dbc.Col(dcc.Graph(id='line_numpost'),md=8),

    ]),

    # Barplot
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar_fact'),md=6),
        dbc.Col(dcc.Graph(id='bar_sentiment'),md=6),
    ]),


]) # End of Layout


# CALLBACKS
@callback(
    Output('bar_fact', 'figure'),
    Output('bar_sentiment', 'figure'),
    Output('line_numpost', 'figure'),
    [Input('sentiment_dropdown', 'value'),
     Input('fact_dropdown', 'value'),
     Input('source_dropdown', 'value'),
     Input('keyword_dropdown', 'value')],
)
def filtering_data(sentiment, misinfo, source, keyword):
    '''
    Filter data based on user input
    Input:
        sentiment: list of sentiment
        fact: list of fact
        source: list of source
        keyword: list of keyword
    Output:
        bar_fact: barplot of fact
        bar_sentiment: barplot of sentiment
    '''
    dff = helper.filter_data(data, sentiment, misinfo, source, keyword)
    aggregate = dff.groupby(['sentiment','misinfo']).sum().reset_index()

    bar_fact = viz.barplot_fact(aggregate)
    bar_sentiment = viz.barplot_sentiment(aggregate)
    line_numpost = viz.line_numpost(dff)

    return bar_fact, bar_sentiment, line_numpost