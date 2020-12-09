import streamlit as st
from GraphOverview import * 
import st_helper
st_helper._max_width_()


def app():

    st.header("The Graph Stats")
    #%%
    st.write("Queried from: https://gateway-testnet.thegraph.com/network")
    st.write("Showing some basic information about TheGraph. ")
    graph_info_df = graphInfo()
    graph_info_df = graph_info_df.T
    st.write(graph_info_df.to_html(escape=False), unsafe_allow_html=True)