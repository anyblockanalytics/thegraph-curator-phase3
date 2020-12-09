#%%
from GraphClient import getGraphQuery
from queries import subgraph_deployment_stats, subgraph_phase2, subgraphs_query
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px
import pathlib

#%%
def subGraphStatsRaw():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=subgraph_deployment_stats)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
    return df

def subGraphStatsOrdered():
    ordered_subgraphStats_df = subGraphStatsRaw()
    ordered_subgraphStats_df = ordered_subgraphStats_df[['originalName','curatorFeeRewards','indexingRewardAmount',
                      'stakedTokens','signalledTokens',
                      'signalAmount', 'queryFeesAmount', 'queryFeeRebates',
                      'id'
                      ]]
    ordered_subgraphStats_df.stakedTokens = ordered_subgraphStats_df.stakedTokens.astype("float")/10**18
    ordered_subgraphStats_df.curatorFeeRewards = ordered_subgraphStats_df.curatorFeeRewards.astype("float")/10**18
    ordered_subgraphStats_df.indexingRewardAmount = ordered_subgraphStats_df.indexingRewardAmount.astype("float")/10**18
    ordered_subgraphStats_df.signalledTokens = ordered_subgraphStats_df.signalledTokens.astype("float")/10**18
    ordered_subgraphStats_df.queryFeesAmount = ordered_subgraphStats_df.queryFeesAmount.astype("float")/10**18
    ordered_subgraphStats_df.queryFeeRebates = ordered_subgraphStats_df.queryFeeRebates.astype("float")/10**18
    ordered_subgraphStats_df.signalAmount = ordered_subgraphStats_df.signalAmount.astype("float")/10**18
    return ordered_subgraphStats_df

# DataFrame export to HTML Table ("index.html")
def subGraphStatsTable():
    df = subGraphStatsRaw()
    html = df.to_html()

    #write html to file
    pathlib.Path('./export').mkdir(parents=True, exist_ok=True) 
    text_file = open("./export/index.html", "w")
    text_file.write(html)
    text_file.close()


def subGraphInfo():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=subgraphs_query)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)

    df = df[['image','displayName', 'description',
             'createdAt', 'codeRepository', 'nameSignalAmount',
             'signalledTokens', 'totalIndexingRewards',
             'totalQueryFeesCollected', 'unsignalledTokens',
             'withdrawableTokens', 'withdrawnTokens', 'id']]
    df.nameSignalAmount = df.nameSignalAmount.astype("float")/10**18
    df.signalledTokens = df.signalledTokens.astype("float")/10**18
    df.totalIndexingRewards = df.totalIndexingRewards.astype("float")/10**18
    df.totalQueryFeesCollected = df.totalQueryFeesCollected.astype("float")/10**18
    df.unsignalledTokens = df.unsignalledTokens.astype("float")/10**18
    df.withdrawableTokens = df.withdrawableTokens.astype("float")/10**18
    df.withdrawnTokens = df.withdrawnTokens.astype("float")/10**18

    return df
# %%
