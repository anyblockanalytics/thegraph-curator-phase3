from SubgraphCuratorSignals import *
import streamlit as st

import st_helper
st_helper._max_width_()


def app():

    st.header("Curator Signalling Subgraphs")
    test_df = subGraphCuratorSignals()
    st.write(test_df)    

