# %%
import streamlit as st
import st_subgraph_signal_page
import st_subgraph_list
import st_curator_list
import st_curator_signal_subgraph
import st_helper
import st_allocationStats
import st_graph_info
st_helper._max_width_()

PAGES = {
    "Overview": st_graph_info,
    "Allocation / Indexer Stats": st_allocationStats,
    "Subgraph List": st_subgraph_list,
    "Subgraph Signal Amount": st_subgraph_signal_page,
    "Curator List": st_curator_list,
    "Curator Signal Subgraph": st_curator_signal_subgraph
    }

st.title("TheGraph General Information")


st.sidebar.title('Navigation')
st.sidebar.write('A WIP Dashboard for Displaying The Graph Information. Currently \
                 Includes five Subpages. For Indexer Information look at Pool/Price Stats')

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

