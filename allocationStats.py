#%%
from GraphClient import getGraphQuery
from queries import allocation_list, subgraph_phase2
import pandas as pd
from helper import graphQueryToDf,concatDictColumns
import plotly.express as px
import pathlib
import datetime
#%%
def allocationStats():
    data = getGraphQuery(subgraph_url=subgraph_phase2,query=allocation_list)
    df = graphQueryToDf(data)
    df = concatDictColumns(df)
  
    df["date"] = df.createdAt.apply(lambda d: datetime.datetime.fromtimestamp(int(d)).strftime('%Y-%m-%d'))
    df['createdAt'] = pd.to_datetime(df['createdAt'],unit='s')
    df['allocatedTokens'] = (df['allocatedTokens'].astype("float")/10**18).astype("int")
    df['indexingRewards'] = (df['indexingRewards'].astype("float")/10**18).astype("int")
    df['effectiveAllocation'] = (df['effectiveAllocation'].astype("float")/10**18).astype("int")
    df['queryFeeRebates'] = (df['queryFeeRebates'].astype("float")/10**18)
    df['queryFeesCollected'] = (df['queryFeeRebates'].astype("float")/10**18)
    return df


def allocationStats_Time(df):
    df = df.set_index('createdAt').groupby(pd.Grouper(freq='D')).aggregate({
        'allocatedTokens' : [('allocatedTokensSum','sum'),('allocatedTokensMean','mean' ),
                            ( 'allocatedTokensMin', 'min'), ('allocatedTokensMax','max')] ,
        'indexingRewards' : [('indexingRewardsSum', 'sum'),( 'indexingRewardsMean','mean'),
                            ('indexingRewardsMin','min'), ('indexingRewardsMax','max')]
    })
    df.columns = df.columns.get_level_values(1)
    return df
