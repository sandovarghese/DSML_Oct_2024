import streamlit as st
import pandas as pd
import datetime
import pickle

st.header("Product Sales Predictor", divider="gray")
df = pd.read_csv("./sales_data.csv")

#no. of products store sells - factors store typ, loc, reg, activities, holiday n seasn

col1, col2, col3 = st.columns(3)

with col1:
    store_type = st.radio(
    "Which store you would like to select?",
    [":rainbow[S1]", ":rainbow[S2]", ":rainbow[S3]", ":rainbow[S4]"],
    horizontal=True,
)


with col2:
    loc = st.radio(
    "Which Location you would like to select?",
    [":rainbow[L1]", ":rainbow[L2]", ":rainbow[L3]", ":rainbow[L4]",":rainbow[L5]"],
    horizontal=True,
)



with col3:
    reg = st.radio(
    "Which Region you would like to select?",
    [":rainbow[R1]", ":rainbow[R2]", ":rainbow[R3]", ":rainbow[R4]"],
    horizontal=True,
)   
    
col5, col6 = st.columns(2)

with col5:
    Holiday_on = st.toggle("Holiday or not")
    holiday = 'No'


with col6:
    discount = st.toggle("Discount provided or not")
    dis_count = 'No'

if st.button("Submit"):
    if discount:
        dis_count = 'Yes'

    if Holiday_on:
        holiday = 'Yes'

    encode_dict = {"store_type": {':rainbow[S1]': 'S1',':rainbow[S2]': 'S2', ':rainbow[S3]': 'S3', ':rainbow[S4]': 'S4'},
                "loc": {':rainbow[L1]': 'L1',':rainbow[L2]': 'L2', ':rainbow[L3]': 'L3', ':rainbow[L4]': 'L4', ':rainbow[L5]': 'L5'},
                "reg": {':rainbow[R1]': 'R1',':rainbow[R2]': 'R2', ':rainbow[R3]': 'R3', ':rainbow[R4]': 'R4'}
    }

    store_type = encode_dict['store_type'][store_type]
    loc = encode_dict['loc'][loc]
    reg = encode_dict['reg'][reg]

    st.write("You selected:")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Store Type", store_type)
    col2.metric("Location", loc)
    col3.metric("Region", reg)
    col4.metric("Holiday", holiday)
    col5.metric("Discount provider", dis_count)

st.dataframe(df.head())

