#%%
import streamlit as st
from allocationStats import * 
import st_helper
import pandas as pd

st_helper._max_width_()


def app():
    allocation_df = allocationStats()
    df_time = allocationStats_Time(allocation_df)
    st.header("Allocation  Informations")

    # checkbox showing all allocations
    if st.checkbox("Show Entire DataFrame with all Allocations by all Indexers on all Subgraphs"):
        st.write(allocation_df[['indexerID', 'originalName', 'indexingRewards', 'allocatedTokens']])    
    # split into 2 columns
    col1, col2 = st.beta_columns(2)
    # Select Indexer
    option_list_indexer =["all"]
    for i in allocation_df['indexerID'].unique():
        option_list_indexer.append(i)

    option_indexer = col1.selectbox('Which Indexer are you interested in?:', option_list_indexer)

    # Select Subgraph
    option_list_subgraph=["all"]
    for i in allocation_df['originalName'].unique():
        option_list_subgraph.append(i)

    option_subgraph = col2.selectbox('Which Subgraph  are you interested in?:', option_list_subgraph)


    # all Options
    # indexer = specific, subgraph = all
    if option_indexer != "all" and option_subgraph=="all":
        st.write(allocation_df[allocation_df['indexerID'] == option_indexer])

        bar1, bar2 = st.beta_columns(2)

        fig = px.bar(allocation_df[allocation_df['indexerID'] == option_indexer], 
                    x='originalName', y="indexingRewards",
                    title="Indexing Rewards by Indexer for Subgraph")
        st_helper.plot_background_changer(fig)
        bar1.plotly_chart(fig)

        fig = px.bar(allocation_df[allocation_df['indexerID'] == option_indexer], 
                    x='originalName', y="allocatedTokens",
                    title="Allocation Amount by Indexer in Subgraph")
        st_helper.plot_background_changer(fig)

        bar2.plotly_chart(fig)
    # indexer all, subgraph = specific
    if option_indexer =="all" and option_subgraph != "all":
        # split into 2 columns

        st.write(allocation_df[allocation_df['originalName'] == option_subgraph])
        pie1, pie2 = st.beta_columns(2)
        #pie chart for indexing rewards on Subgraph by Indexer
        fig = px.pie(allocation_df[allocation_df['originalName'] == option_subgraph], 
                    values='indexingRewards', names="indexerID", 
                    title="Indexing Rewards on Subgraph by Indexer")
        fig.update_layout(width=500)
        fig.update_layout({"legend_orientation":"h"})
        
        pie1.plotly_chart(fig)

        # pie chart for allocated tokens on Subgraph by Indexer
        fig = px.pie(allocation_df[allocation_df['originalName'] == option_subgraph], 
            values='allocatedTokens', names="indexerID", 
            title="Allocated Tokens on Subgraph by Indexer")
        fig.update_layout(width=500)
        fig.update_layout({"legend_orientation":"h"})
        
        pie2.plotly_chart(fig)

    if option_indexer == "all" and option_subgraph == "all":

        st.write(allocation_df)
        """
        fig = px.bar(allocation_df, 
            x='originalName', y="indexingRewards", title="IndexingRewards Sum by Subgraph")
        fig.update_layout(width=1000)
        st.plotly_chart(fig)
    	"""
        # Allocated Tokens by Subgraph
        """
        fig = px.bar(allocation_df, 
            x='originalName', y="allocatedTokens", title="Allocated Tokens Sum by Subgraph")
        fig.update_layout(width=1000)
        st.plotly_chart(fig)
        """
        pie1, pie2 = st.beta_columns(2)
        
        # IndexingRewards by Subgraph
        fig = px.pie(allocation_df, 
            values='indexingRewards', names="originalName", 
            title="IndexingRewards Sum by Subgraph")
        fig.update_traces(textposition='inside', textinfo='percent')

     
        fig.update_layout(width=500)
        #fig.update_layout({"legend_orientation":"h"})
        pie1.plotly_chart(fig)
        # Allocated Tokens by Subgraph

        fig = px.pie(allocation_df, 
            values='allocatedTokens', names="originalName", title="Allocated Tokens Sum by Subgraph")
        fig.update_layout(width=500)
        fig.update_traces(textposition='inside', textinfo='percent')
        #fig.update_layout({"legend_orientation":"h"})
        
        pie2.plotly_chart(fig)

        # Time Series
        st.header('Aggregation by Day')
        st.write(df_time)

        ts_1, ts_2 = st.beta_columns(2)

        # Day Aggregation of allocatedTokens
        fig = px.line(df_time, x= df_time.index, y = [df_time['allocatedTokensSum'],
                                                      df_time['allocatedTokensMean'],
                                                      df_time['allocatedTokensMax']],
                      labels= {'createdAt' : 'Day', 'value': 'Token Allocation on Subgraphs'})
        fig.update_layout({
        'plot_bgcolor' : 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'})

        ts_1.plotly_chart(fig)

        # Day Aggregation of indexingRewards

        fig = px.line(df_time, x= df_time.index, y = [df_time['indexingRewardsSum'],
                                                      df_time['indexingRewardsMean'],
                                                      df_time['indexingRewardsMax']],
                      labels= {'createdAt' : 'Day', 'value': 'Indexing Rewards per Day on Subgraphs'})
        fig.update_layout({
        'plot_bgcolor' : 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'})

        ts_2.plotly_chart(fig)


    # if specific indexer and specific Subgraph
    # cobb douglas
    if option_indexer != "all" and option_subgraph != "all":
        subset_df = allocation_df[(allocation_df.originalName == option_subgraph) & 
                (allocation_df.indexerID == option_indexer)]
        st.write(subset_df)
