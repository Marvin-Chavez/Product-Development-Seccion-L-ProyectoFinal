import streamlit as st
import requests

# Crear pestañas para cada modelo
tab1, tab2, tab3 = st.tabs(["Modelo 1", "Modelo 2", "Modelo 3"])

# Pestaña para Modelo 1
with tab1:
    st.header("Predicción con Modelo 1")

    # Crear campos para recoger los datos de entrada
    loan_amount = st.number_input("Loan Amount", min_value=0, value=1000)
    funded_amount = st.number_input("Funded Amount", min_value=0, value=1000)
    funded_amount_investor = st.number_input("Funded Amount Investor", min_value=0.0, value=1000.0)
    term = st.number_input("Term", min_value=0, value=36)
    batch_enrolled = st.text_input("Batch Enrolled")
    interest_rate = st.number_input("Interest Rate", min_value=0.0, value=5.0)
    grade = st.text_input("Grade")
    sub_grade = st.text_input("Sub Grade")
    employment_duration = st.text_input("Employment Duration")
    home_ownership = st.number_input("Home Ownership", min_value=0.0, value=100000.0)
    verification_status = st.text_input("Verification Status")
    loan_title = st.text_input("Loan Title")
    debit_to_income = st.number_input("Debit to Income", min_value=0.0, value=15.0)
    delinquency_two_years = st.number_input("Delinquency - two years", min_value=0, value=0)
    inquires_six_months = st.number_input("Inquires - six months", min_value=0, value=0)
    open_account = st.number_input("Open Account", min_value=0, value=10)
    revolving_balance = st.number_input("Revolving Balance", min_value=0, value=5000)
    revolving_utilities = st.number_input("Revolving Utilities", min_value=0.0, value=50.0)
    total_accounts = st.number_input("Total Accounts", min_value=0, value=20)
    initial_list_status = st.text_input("Initial List Status")
    total_received_interest = st.number_input("Total Received Interest", min_value=0.0, value=200.0)
    total_received_late_fee = st.number_input("Total Received Late Fee", min_value=0.0, value=0.0)
    recoveries = st.number_input("Recoveries", min_value=0.0, value=0.0)
    collection_recovery_fee = st.number_input("Collection Recovery Fee", min_value=0.0, value=0.0)
    last_week_pay = st.number_input("Last week Pay", min_value=0, value=35)
    total_collection_amount = st.number_input("Total Collection Amount", min_value=0, value=100)
    total_current_balance = st.number_input("Total Current Balance", min_value=0, value=10000)
    total_revolving_credit_limit = st.number_input("Total Revolving Credit Limit", min_value=0, value=5000)
if st.button('Predecir con Modelo 1'):
    # Empaquetar los datos en un formato JSON
    data = {
        "Loan Amount": loan_amount,
        "Funded Amount": funded_amount,
        "Funded Amount Investor": funded_amount_investor,
        "Term": term,
        "Batch Enrolled": batch_enrolled,
        "Interest Rate": interest_rate,
        "Grade": grade,
        "Sub Grade": sub_grade,
        "Employment Duration": employment_duration,
        "Home Ownership": home_ownership,
        "Verification Status": verification_status,
        "Loan Title": loan_title,
        "Debit to Income": debit_to_income,
        "Delinquency - two years": delinquency_two_years,
        "Inquires - six months": inquires_six_months,
        "Open Account": open_account,
        "Revolving Balance": revolving_balance,
        "Revolving Utilities": revolving_utilities,
        "Total Accounts": total_accounts,
        "Initial List Status": initial_list_status,
        "Total Received Interest": total_received_interest,
        "Total Received Late Fee": total_received_late_fee,
        "Recoveries": recoveries,
        "Collection Recovery Fee": collection_recovery_fee,
        "Last week Pay": last_week_pay,
        "Total Collection Amount": total_collection_amount,
        "Total Current Balance": total_current_balance,
        "Total Revolving Credit Limit": total_revolving_credit_limit
    }

    # Enviar los datos a la API y obtener la respuesta
    response = requests.post('http://127.0.0.1:5000/predict1S', json=data)
    if response.status_code == 200:
        # Mostrar la respuesta
        st.success(f'Predicción: {response.json()["Prediccion"]}')
    else:
        st.error("Error en la predicción")


# Pestañas para Modelo 2 y Modelo 3 se estructuran de manera similar
with tab2:
    st.header("Predicción con Modelo 2")
    # ... Código para la predicción con el Modelo 2 ...

with tab3:
    st.header("Predicción con Modelo 3")
    # ... Código para la predicción con el Modelo 3 ...