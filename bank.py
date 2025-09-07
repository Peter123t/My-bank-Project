import streamlit as st
import joblib

# Load the pre trained model
model = joblib.load('bank_term_deposit_model.model')

st.title("💰 Bank Term Deposit Prediction")

st.write("Fill the form below to predict if a client will subscribe to a term deposit.")

# creating an arrangement on how the columns will be displayed on the webpage
col1, col2 = st.columns(2)

# getting the features input
age = col1.number_input("Age", min_value=18, max_value=100, step=1)
job = col2.selectbox("Job", options = ['admin', 'blue-collar', 'entrepreneur', 'housemaid',
    'management', 'retired', 'self-employed', 'services','student', 'technician', 'unemployed'])
marital = col1.selectbox("Marital Status", options = ['single', 'married', 'divorced'])
education = col2.selectbox("Education",options = ['primary', 'secondary', 'tertiary'])
default = col1.selectbox("Credit in Default?",options = ['yes','no'])
balance = col2.number_input("Account Balance", min_value=-2000, max_value=100000, step=1)
housing = col1.selectbox("Housing Loan", options = ["yes", "no"])
loan = col2.selectbox("Personal Loan?", ["yes", "no"])
campaign = col1.number_input("Number of Contacts during Campaign", min_value=1, max_value=50, step=1)
previous = col2.number_input("Number of Previous Contacts", min_value=1, max_value=50, step=1)

# Convert categorical input    to numeric
default = 1 if default == 'yes' else 0
housing = 1 if housing == 'yes' else 0
loan = 1 if loan == 'yes' else 0

# Job mapping
if job == "admin":
    job = 0
elif job == "blue-collar":
    job = 1
elif job == "entrepreneur":
    job = 2
elif job == "housemaid":
    job = 3
elif job == "management":
    job = 4
elif job == "retired":
    job = 5
elif job == "self-employed":
    job = 6
elif job == "services":
    job = 7
elif job == "student":
    job = 8
elif job == "technician":
    job = 9
else:
    job = 10


# Marital mapping
if marital == "divorced":
    marital = 0
elif marital == "married":
    marital = 1
else:
    marital = 2


# Education mapping
if education == "primary":
    education = 0
elif education == "secondary":
    education = 1
else:
    education = 2

# Creating the functionfor the prediction
if st.button('Subscription Result'):
    features = [[age, job, marital, education, default, balance, housing, loan, campaign, previous]]
    prediction =  model.predict(features)
   
    if prediction == 1:
        st.success("✅ This client will SUBSCRIBE.")
    else:
        st.error("❌ This client will NOT subscribe.")








