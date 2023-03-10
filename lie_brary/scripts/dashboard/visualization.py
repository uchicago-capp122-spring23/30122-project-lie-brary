'''
This script is used to create the visualization function for the dashboard
by Reza R Pratama
'''

import plotly.express as px
import datetime

def barplot_fact(aggregate_df):
    '''
    Create barchart of fact
    Input:
        aggregate_df: dataframe
    Output:
        fig: barchart of fact
    '''
    fig = px.bar(aggregate_df,
            x='misinfo',
            y='count',
            color='sentiment',
            color_discrete_sequence=['#FB475E','#E5DDC8','#019992'],
            labels={'misinfo':'Minsinformation Label',
                    'count':'Number of Posts',
                    'sentiment':'Sentiment'},
            title='Number of Posts by Misinformation Label',
            )
    return fig.update_layout(showlegend=False)


def barplot_sentiment(aggregate_df):
    '''
    Create barchart of sentiment
    Input:
        aggregate_df: dataframe
    Output:
        fig: barchart of fact
    '''
    fig2 = px.bar(aggregate_df,
             x='sentiment',
             y='count',
             color='misinfo',
             color_discrete_sequence=['#FB475E','#01949A'],
             labels={'misinfo':'Minsinformation Label',
                     'count':'Number of Posts',
                     'sentiment':'Sentiment'},
             title='Number of Posts by Sentiment')
    return fig2.update_layout(showlegend=False)


# create line chart, number of posts by date
def line_numpost(df):
    '''
    Create line chart of number of posts by date
    Input:
        df: dataframe
    Output:
        fig: line chart of number of posts by date
    '''
    grouped = df.groupby(['bydate','keyword']).sum().reset_index()
    grouped = grouped.loc[grouped['bydate'] >= datetime.date(2021,1,1)]
    fig = px.line(grouped,
                 x='bydate',
                 y='count',
                 color='keyword',
                 labels={'bydate':'Date',
                         'count':'Number of Posts',
                         'keyword':'Keyword'},
                 title='Number of Posts by Date',
                 template='seaborn'
                 )
    return fig