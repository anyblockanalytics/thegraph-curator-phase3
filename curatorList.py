#%%
from GraphClient import getGraphQuery
from queries import curator_list, subgraph_phase2
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px
import pathlib

#%%
def curatorList():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=curator_list)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
    return df



def curatorTotalNameSignal():
    df = curatorList()
    fig = px.pie(df, values='totalNameSignal', names='id')
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return fig