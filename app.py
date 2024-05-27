import streamlit as st
import pandas as pd
import pickle
import numpy as np


df = pickle.load(open('clean_data.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

posted_by = df['posted_by'].unique().tolist()
posted_by.insert(0,"Select")

under_construction = df['under_construction'].unique().tolist()
under_construction.insert(0,"Select")

rera = df['rera'].unique().tolist()
rera.insert(0,"Select")

bhk_or_rk = df['bhk_or_rk'].unique().tolist()
bhk_or_rk.insert(0,"Select")

ready_to_move = df['ready_to_move'].unique().tolist()
ready_to_move.insert(0,"Select")

resale = df['resale'].unique().tolist()
resale.insert(0,"Select")

address = df['address'].unique().tolist()
address.insert(0,"Select")


st.title('House price predictor')

dealer = st.selectbox(' Select the Dealer ',posted_by)
working = st.selectbox(' Home Work is running or not ',under_construction)
rera = st.selectbox(' Type of rera ',rera)
bhk = st.text_input('The Number of bhk')
bh_rk = st.selectbox(' Select BHK OR RK',bhk_or_rk)
square = st.text_input('Enter the square foot')
move = st.selectbox(' Select Ready to Move ',ready_to_move)
resale = st.selectbox(' Select the Resale ',resale)
location = st.selectbox(' Select House location',address)
longitude = st.text_input('Enter the Longitude')
latitude = st.text_input('Enter the Latitude')


if st.button('predict'):
    input_data = (dealer,working,rera,bhk,bh_rk,square,move,resale,location,longitude,latitude)
    rehape_data = np.asarray(input_data).reshape(1,-1)
    result = model.predict(rehape_data)[0]
    result = round(result, 2)
    st.success(' House Price is ' + str(result) + ' Lakh')
# try:
#     if st.button('predict'):
#         input_data = (dealer,working,rera,bhk,bh_rk,square,move,resale,location,longitude,latitude)
#         rehape_data = np.asarray(input_data).reshape(1,-1)
#         result = model.predict(rehape_data)[0]
#         result = round(result, 2)
#         st.success(' House Price is ' + str(result) + ' Lakh')
# except:
#     st.warning('Please Fill all values')
    
