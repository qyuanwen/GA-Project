import streamlit as st
from streamlit.components.v1 import components

# Embedding Tableau dashboard in Streamlit app
tableau_url = "https://public.tableau.com/views/SMRT_Delays/Dashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
tableau_width = "100%"
tableau_height = "900" # set the height to a fixed value or adjust as needed

components.html(f'<iframe src="{tableau_url}" width="{tableau_width}" height="{tableau_height}"></iframe>')
