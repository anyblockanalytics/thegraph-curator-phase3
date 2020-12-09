import streamlit as st
import plotly as px
def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

def plot_background_changer(fig,plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'):
        return fig.update_layout({
        'plot_bgcolor' : 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'})