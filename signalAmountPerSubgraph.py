#%%
from GraphClient import getGraphQuery
from queries import subgraph_Deployments_by_signal_query ,subgraph_phase2
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px

#%%
def signalAmountPerSubgraph():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=subgraph_Deployments_by_signal_query)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
    return df


def signalAmountPerSubgraphPieChart():
    df = signalAmountPerSubgraph()
    fig = px.pie(df, values='signalAmount', names='originalName')
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return fig

