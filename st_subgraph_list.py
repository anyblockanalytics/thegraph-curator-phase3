import streamlit as st
from deployedSubgraphStats import subGraphStatsRaw, subGraphInfo, subGraphStatsOrdered
import st_helper
import plotly.express as px
import plotly.graph_objects as go

st_helper._max_width_()

def app():

    st.header("Subgraph Deployment Stats")
    #%%
    ordered_subgraphStats_df = subGraphStatsOrdered()
    subgraphInfo_df = subGraphInfo()

    if st.checkbox("show Optimal Subgraphs for allocation"):
        ordered_subgraphStats_df['Difference_Quotient'] = (ordered_subgraphStats_df['signalledTokens']-ordered_subgraphStats_df['stakedTokens'])/ordered_subgraphStats_df['stakedTokens']
        st.write(ordered_subgraphStats_df[['originalName','Difference_Quotient','indexingRewardAmount','stakedTokens','signalledTokens']].sort_values(['signalledTokens','Difference_Quotient']))



    st.write(ordered_subgraphStats_df)    

    
    widgets1,widgets2 = st.beta_columns(2)
    #plot 1
    fig = px.scatter(ordered_subgraphStats_df, 
                x='signalledTokens', y="curatorFeeRewards",
                title="Curator Fee Rewards by SignalledTokens")
    st_helper.plot_background_changer(fig)
    widgets1.plotly_chart(fig)
    
    #plot 2
    fig = px.scatter(ordered_subgraphStats_df, 
                x='stakedTokens', y="indexingRewardAmount",
                title="Indexing Rewards by StakedTokens")
    st_helper.plot_background_changer(fig)
    widgets2.plotly_chart(fig)

    #plot 3

    fig = px.histogram(ordered_subgraphStats_df, 
                x='stakedTokens',
                title="stakedTokens Histogram")
    st_helper.plot_background_changer(fig)
    widgets2.plotly_chart(fig)

    #plot 4
    fig = px.histogram(ordered_subgraphStats_df, 
                x='signalAmount',
                title="signalAmount Histogram")
    st_helper.plot_background_changer(fig)
    widgets1.plotly_chart(fig)

    st.subheader("Subgraph Informations")

    st.write(subgraphInfo_df)


    sel = subgraphInfo_df

    #format the images list
    sel['html'] = ["<img src='" + r
        + f"""' style='display:block;margin-left:auto;margin-right:auto;width:100px;border:0;'><div style='text-align:center'>""" 
        + "<br>" + "</div>" 
        for r in sel['image']]
    #sel2 = sel[['model', 'html', 'rank']].pivot(index='rank', columns="model", values="html")
    sel.drop(columns={'image'}, inplace=True)
    sel.rename(columns={'html': 'Project'}, inplace=True)
    sel.set_index('Project', inplace=True)
    sel=sel[['displayName','description','codeRepository']]
    
    #show the list of images as a dataframe
    st.write(sel.to_html(escape=False), unsafe_allow_html=True)