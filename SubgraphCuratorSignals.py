#%%
from GraphClient import getGraphQuery
from queries import subgraph_curator_signal_stats, subgraph_phase2, subgraph_list
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px
import pathlib

#%%
def subGraphCuratorSignals():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=subgraph_curator_signal_stats)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
    # after concat we get 2 columns named "ID" -> first is Curator ID , second is SubgraphID
    
    df.columns = ['lastSignalChange', 'realizedRewards', 'signalledTokens', 
                  'unsignalledTokens', 'CuratorID','SubgraphID' ]
    return df


# DataFrame export to HTML Table ("index.html")
def subGraphCuratorSignalsTable():
    df = subGraphStats()
    html = df.to_html()

    #write html to file
    pathlib.Path('./export').mkdir(parents=True, exist_ok=True) 
    text_file = open("./export/index.html", "w")
    text_file.write(html)
    text_file.close()


# %%
