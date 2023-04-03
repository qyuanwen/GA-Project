
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
title = "Welcome to SMRT Delays information page"
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
    image_url = "https://static.vecteezy.com/system/resources/previews/015/087/558/original/character-flat-drawing-train-seen-from-the-front-prepares-to-carry-passengers-quickly-safe-comfortable-to-their-destination-mass-rapid-and-public-transportation-cartoon-design-illustration-vector.jpg"
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
    st.write("Please click into SMRT Delays Predictor on the left sidebar to start.")
    st.write("Please click into SMRT Delays Tableau on the left sidebar if you are interested in the past half decade's delays/breakdown/faults information.")

    st.write("Unfortunately, NorthEast line, Sengkang and Punggol LRT have not been added into the predictor as of now, please wait for future updates.")
    
    st.write("")
    st.write("")
