#%%
from GraphClient import getGraphQuery
from queries import the_graph_info_query, subgraph_phase2
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px
import pathlib

#%%
def graphInfo():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=the_graph_info_query)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
    return df

