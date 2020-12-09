import streamlit as st
from curatorList import * 
import st_helper
st_helper._max_width_()


def app():

    st.header("Curator  Informations")
    #%%
    curator_df = curatorList()
    st.write(curator_df)    

    fig = curatorTotalNameSignal()
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig)    