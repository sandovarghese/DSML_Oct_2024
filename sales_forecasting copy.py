import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle


with open("xgb_sales_forecasting_model.pkl", "rb") as file:
    model = pickle.load(file)


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

col7, col8 = st.columns(2)
with col7:
    store_id = st.number_input("Store ID", min_value=1, value=1, step=1)
with col8:
    future_date = st.date_input("Select a Future Date")
    
month = future_date.month
year = future_date.year
day = future_date.day

location_type_dict = {"L1": 0, "L2": 1, "L3": 2, "L4": 3, "L5": 4}
store_type_dict = {"S1": 0, "S2": 1, "S3": 2, "S4": 3}
region_type_dict = {"S1": 0, "S2": 1, "S3": 2, "S4": 3}
discount_dict = {"Yes": 1, "No": 0}
holiday_dict = {"Yes": 1, "No": 0}

inputs = np.array([
    store_id,
    store_type_dict[store_type],
    location_type_dict[loc],
    region_type_dict[reg],
    holiday_dict[holiday],
    discount_dict[dis_count],
    month,
    year,
    day
]).reshape(1, -1)




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
    col5.metric("Promotional Activities", dis_count)

    prediction = model.predict(inputs)
    st.write(f"Predicted Sales for {future_date}: ${prediction[0]:.2f}")



st.dataframe(df.head())

