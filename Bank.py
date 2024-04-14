import streamlit as st
import pandas as pd
import numpy as np
import sklearn

df = pd.read_csv('BankChurners.csv')

# Label Encode Attrition Flag column
from sklearn.preprocessing import LabelEncoder

# Attrition_Flag
Attrition_Flag_encode = LabelEncoder()
df['Attrition_Flag'] = Attrition_Flag_encode.fit_transform(df['Attrition_Flag'])

sel_columns = ['Total_Trans_Amt', 'Total_Amt_Chng_Q4_Q1', 'Total_Ct_Chng_Q4_Q1', 'Total_Trans_Ct',
 'Total_Revolving_Bal', 'Customer_Age', 'Credit_Limit', 'Total_Relationship_Count','Attrition_Flag']
sel_data = df[sel_columns]

# split into train and test
x = sel_data.drop('Attrition_Flag', axis = 1)
y = sel_data.Attrition_Flag
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.20, random_state = 98, stratify = y)

from imblearn.over_sampling import SMOTE

# Apply SMOTE to balance the dataset

smote = SMOTE(sampling_strategy='auto', random_state= 29) #  AUTO IT DECIDES ITSELF 
X_resampled, y_resampled = smote.fit_resample(xtrain, ytrain)

new_balanced_data_smote = pd.concat([X_resampled, y_resampled], axis = 1)

from sklearn.metrics import confusion_matrix, classification_report

#--------- RandomForest CLASSIFIER MODELLING --------------

from sklearn.ensemble import RandomForestClassifier

Ran_model = RandomForestClassifier()

Ran_model.fit(X_resampled, y_resampled)


st.set_page_config(page_title='Bankchurn Project',page_icon=':bank:')

col1, col2 = st.columns([0.1,0.9])
with col1:
    st.image('BankCus.png', width = 100)
html_title = """<style>.title-test{font-weight:bold;padding:5px;border-radius:6px;}
                </style><center><h5 class="title-test">Bank Churners Predictor: Streamlit and Python Project Overview</h5></center>
               """

st.write('This project focuses on the development of a predictive machine learning model designed to identify customers at risk of churn within banking institutions. By harnessing historical customer data and pertinent factors, our goal is to unveil patterns and indicators preceding customer churn. Through predictive analytics, banks will gain the capability to intervene promptly with targeted retention strategies. This includes personalized customer interactions and tailored retention initiatives to meet individual needs. Ultimately, our aim is to significantly reduce churn rates and cultivate enduring, long-term customer relationships.')

st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)

with col2:
     st.markdown(html_title,unsafe_allow_html= True)
st.markdown("<h4 style = 'margin: -30px; color: #FBFCFC ; text-align: center; font-family: cursive '>Built By Chiemeziem Okeke</h4>", unsafe_allow_html = True)

st.markdown("<br>", unsafe_allow_html= True)
with st.expander('Data Preview'):
    st.dataframe(df,use_container_width = True)

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)


col3,col4, col5 = st.columns(3)

with col3:
    st.image('BankCus4.png',caption = 'Welcome Distinguished Customer')

with col4:
    T_T_Amt = col4.number_input('Total_Trans_Amt',100,1000000)
    Total_Amt_Chng = col4.number_input('Total_Amt_Chng_Q4_Q1', 0.000,10.000)
    Total_Ct_Chng = col4.number_input('Total_Ct_Chng_Q4_Q1', 0.000,10.000)
    Trans_Ct = col4.number_input('Total_Trans_Ct',10,500)
with col4:
    Total_Rev_Bal = col5.number_input('Total_Revolving_Bal', 0,1000000)
    Cus_Age = col5.number_input('Customer_Age', 18,80)
    Cred_Lim = col5.number_input('Credit_Limit', 1000,100000)
    Total_ship_Count = col5.number_input('Total_Relationship_Count', 1,10)


st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)

st.markdown("<h4 style = 'margin: -30px; color: #EEEEE8; text-align: center; font-family: helvetica '> Input Variable </h4>", unsafe_allow_html = True)   

inputs = pd.DataFrame()

inputs['Total_Trans_Amt'] = [T_T_Amt]
inputs['Total_Amt_Chng_Q4_Q1'] = [Total_Amt_Chng]
inputs['Total_Ct_Chng_Q4_Q1'] = [Total_Ct_Chng]
inputs['Total_Trans_Ct'] = [Trans_Ct]
inputs['Total_Revolving_Bal'] = [Total_Rev_Bal]
inputs['Customer_Age'] = [Cus_Age]
inputs['Credit_Limit'] = [Cred_Lim]
inputs['Total_Relationship_Count'] = [Total_ship_Count]


st.dataframe(inputs, use_container_width= True)


pusher = st.button('Predict Attrition')

# Model Prediction

if pusher:
    predicted = Ran_model.predict(inputs)
    if predicted[0]== 1:
        st.success(f'Congratulations, Thank you for being part of our banking family')
        st.image('BankCus3.png', width = 200)
    else: 
        st.error(f'Please, lets rebuild your financial journey together')
        st.image('BankCus1.png', width = 200)





