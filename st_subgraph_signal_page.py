import streamlit as st
from signalAmountPerSubgraph import signalAmountPerSubgraphPieChart, signalAmountPerSubgraph
import st_helper
st_helper._max_width_()
def app():

    st.header("Signal Amount per Subgraph")
    #%%
    
    df = signalAmountPerSubgraph()
    st.write(df)


    plt = signalAmountPerSubgraphPieChart()
    plt.update_layout(width=1000)

    st.plotly_chart(plt)