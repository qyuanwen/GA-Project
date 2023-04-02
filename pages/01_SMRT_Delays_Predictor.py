
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
st.set_page_config(page_title="SMRT Delays Predictor", layout="wide")

# Set the title
title = "SMRT Delays Predictor"
st.title(title)

# Allow cache
#@st.cache(allow_output_mutation=True)

# Set description
st.write("This is the place where you can input the time per hour, day type and station name and the system \
        will predict whether it will be affected by delays or breakdowns. Try it now and start planning your route!")
st.markdown("##")

# Define sidebar title
st.sidebar.header('Input the 3 features below')

# Define dropdown options
ques_1_options = ['','WEEKDAY', 'WEEKENDS/HOLIDAY']
ques_2_options = ['', 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
ques_3_options = ['', 'ADMIRALTY',
'ALJUNIED','ANG MO KIO','BAKAU','BANGKIT','BARTLEY','BAYFRONT','BEAUTY WORLD','BEDOK','BEDOK NORTH','BEDOK RESERVOIR','BENCOOLEN','BENDEMEER','BISHAN','BOON KENG','BOON LAY','BOTANIC GARDENS','BRADDELL','BRAS BASAH','BRIGHT HILL','BUANGKOK','BUGIS','BUKIT BATOK','BUKIT GOMBAK','BUKIT PANJANG','BUONA VISTA','CALDECOTT','CANBERRA','CASHEW','CHANGI AIRPORT','CHENG LIM','CHINATOWN','CHINESE GARDEN','CHOA CHU KANG','CITY HALL','CLARKE QUAY','CLEMENTI','COMMONWEALTH','COMPASSVALE','CORAL EDGE','COVE','DAKOTA','DAMAI','DHOBY GHAUT','DOVER','DOWNTOWN','ESPLANADE','EUNOS','EXPO','FAJAR','FARMWAY','FARRER PARK','FARRER ROAD','FERNVALE','FORT CANNING','GARDENS BY THE BAY','GEYLANG BAHRU','GREAT WORLD','GUL CIRCLE','HARBOURFRONT','HAVELOCK','HAW PAR VILLA',
'HILLVIEW','HOLLAND VILLAGE','HOUGANG','JALAN BESAR','JELAPANG','JOO KOON','JURONG EAST','KADALOOR','KAKI BUKIT','KALLANG','KANGKAR','KEAT HONG','KEMBANGAN','KENT RIDGE','KHATIB','KING ALBERT PARK','KOVAN','KRANJI','KUPANG','LABRADOR PARK','LAKESIDE','LAVENDER','LAYAR','LENTOR','LITTLE INDIA','LORONG CHUAN','MACPHERSON','MARINA BAY','MARINA SOUTH PIER','MARSILING','MARYMOUNT','MATTAR','MAXWELL','MAYFLOWER','MERIDIAN','MOUNTBATTEN','NAPIER','NEWTON','NIBONG','NICOLL HIGHWAY','NOVENA','OASIS','ONE-NORTH','ORCHARD','ORCHARD BOULEVARD','OUTRAM PARK','PASIR PANJANG','PASIR RIS','PAYA LEBAR','PENDING','PETIR','PHOENIX','PIONEER','POTONG PASIR','PROMENADE','PUNGGOL','PUNGGOL POINT','QUEENSTOWN','RAFFLES PLACE','RANGGUNG','REDHILL','RENJONG','RIVIERA','ROCHOR','RUMBIA','SAM KEE','SAMUDERA','SEGAR','SEMBAWANG','SENGKANG','SENJA','SERANGOON','SHENTON WAY','SIMEI','SIXTH AVENUE','SOMERSET','SOO TECK','SOUTH VIEW','SPRINGLEAF','STADIUM','STEVENS','SUMANG','TAI SENG','TAMPINES','TAMPINES EAST','TAMPINES WEST','TAN KAH KEE','TANAH MERAH','TANJONG PAGAR','TECK WHYE','TELOK AYER','TELOK BLANGAH','THANGGAM','TIONG BAHRU','TOA PAYOH','TONGKANG','TUAS CRESCENT','TUAS LINK','TUAS WEST ROAD','UBI','UPPER CHANGI','UPPER THOMSON','WOODLANDS','WOODLANDS NORTH','WOODLANDS SOUTH','WOODLEIGH','YEW TEE',
'YIO CHU KANG','YISHUN']

# Set the input parameters
with st.sidebar.form(key = 'Form_1'):
    ques_1 = st.selectbox(
        'Are you planning to take a train on a weekday or weekend/holiday?',
        ques_1_options
    )
    ques_2 = st.selectbox(
        'Which hour are you planning to take the train?',
        ques_2_options
    )
    ques_3 = st.selectbox(
        'Which station will you be taking from?',
        ques_3_options
    )
    st.write("")

    st.form_submit_button("Submit")

# Import the model_selection
pickled_model = pickle.load(open('finalized_model.pkl', 'rb'))

# Saving the input as a dataframe
def user_input():
    d = {}
    for i in pickled_model.feature_names_in_.tolist():
        d[i] = [0]
    if ques_1 != '' and ques_2 != '' and ques_3 != '':
        if ques_1_options.index(ques_1) == 'WEEKDAY':
            d['day_type_WEEKDAY'][0] = 1
        else:
            d['day_type_WEEKENDS/HOLIDAY'][0] = 1
        d['time_per_hour'][0] = int(ques_2)
        station = "station_name_" + ques_3
        d[station][0] = 1
    inputs = pd.DataFrame(d)    
    return inputs

df = user_input()
st.write(df)

# Act as a check to check the inputs
#@st.subheader('User Input Parameters')
#st.write(df)


# Define predict_result_text
result_details = {
    '1': 'Yes, it will get affected',
    '0': 'No, it will not get affected.'
    }


# Make the prediction
prediction = pickled_model.predict(df)
prediction_name = result_details[str(prediction[0])]

st.write(prediction)

# Returns the details of the predictions
st.subheader('Prediction')
st.write(prediction_name)
st.write("")
