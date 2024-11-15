import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
from datetime import datetime
import pickle

#loading model
with open("xgb_model.pkl", "rb") as file:
    model = pickle.load(file)

#function to predict the sales value
def predict_sales(store_id, store_type, location_type, region_code, holiday, discount, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    
    data = {
        'Store_id': [store_id],
        'Store_Type': [store_type],
        'Location_Type': [location_type],
        'Region_Code': [region_code],
        'Holiday': [holiday],
        'Discount': [discount],
        'month': [month],
        'year': [year],
        'day': [day]
    }
    
    input_data = pd.DataFrame(data)
    
    predicted_sales = model.predict(input_data)[0]
    return predicted_sales


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
    

location_type_dict = {"L1": 0, "L2": 1, "L3": 2, "L4": 3, "L5": 4}
store_type_dict = {"S1": 0, "S2": 1, "S3": 2, "S4": 3}
region_type_dict = {"R1": 0, "R2": 1, "R3": 2, "R4": 3}
discount_dict = {"Yes": 1, "No": 0}
holiday_dict = {"Yes": 1, "No": 0}


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

    #st.write("You selected:", future_date)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Store Type", store_type)
    col2.metric("Location", loc)
    col3.metric("Region", reg)
    col4.metric("Holiday", holiday)
    col5.metric("Promotional Activities", dis_count)

    sales_prediction = predict_sales(store_id, store_type_dict[store_type], location_type_dict[loc], region_type_dict[reg],
                                     holiday_dict[holiday], discount_dict[dis_count], str(future_date))
    st.success(f"Predicted Sales for {future_date}: ${sales_prediction:.2f}")


st.dataframe(df.head())

