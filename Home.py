
# Import libraries
import pandas as pd
import numpy as np
import pandas as pd
import sklearn
import pickle
from PIL import Image

# Modeling libraries
from sklearn.linear_model import LogisticRegression

# Streamlit
import streamlit as st
import streamlit.components.v1 as components

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Set Page Title
st.set_page_config(page_title="Home", layout="wide")

# Set the title
title = "Welcome to SMRT Delays Predictor!"
st.title(title)

# Set the logo
st.sidebar.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.smrttrains.com.sg/portals/0/2019_SMRT%20Trains.png?ver=2019-04-18-165650-773);
                background-repeat: no-repeat;
                background-size: 250px 49px;
                padding-top: 2px;
                background-position: 20px 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
)
def set_bg_hack_url():
    '''
    A function to set background image from a url.
    '''
    image_url = "data:image/jpeg;base64,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"
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url('{image_url}');
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_bg_hack_url()
# sidebar contents
#st.sidebar.image(Image.open('image/logo/logo.jpg'))
#st.sidebar.write("For Careers/Business Opportunity, please contact me at:")
#st.sidebar.write("**Email:** junwei.ye.sg@gmail.com")
#st.sidebar.write("**Linkedin:** https://www.linkedin.com/in/ye-junwei/")
#st.sidebar.write("**Github:** https://github.com/JunweiYe91/GA-Projects")

# Set the content
with st.container():
    st.write("Welcome to SMRT Delays predictor!")
    st.write("For mobile users, please click on the \">\" button on the top right corner of the page.")
    st.write("Unfortunately, NorthEast line, Sengkang and Punggol LRT have not been added into the predictor as of now, please wait for future updates.")
    
    st.write("")
    st.write("")
