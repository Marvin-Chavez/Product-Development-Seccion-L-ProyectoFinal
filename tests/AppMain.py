import streamlit as st
import requests
import pandas as pd
import base64

# Función para generar un enlace de descarga
def get_download_link(file_path):
    with open(file_path, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{data}" download="{file_path}">Descargar plantilla</a>'
    return href

# Botón de descarga en la aplicación Streamlit
st.markdown(get_download_link('Plantilla_Prediccion_Prestamos.xlsx'), unsafe_allow_html=True)


# Carga de datos
data = pd.read_csv('LoanDefault.csv')

# Extracción de valores únicos o rangos
unique_batch_enrolled = data['Batch Enrolled'].dropna().unique()
unique_grade = data['Grade'].dropna().unique()
unique_sub_grade = data['Sub Grade'].dropna().unique()
unique_employment_duration = data['Employment Duration'].dropna().unique()
unique_verification_status = data['Verification Status'].dropna().unique()
unique_loan_title = data['Loan Title'].dropna().unique()
unique_initial_list_status = data['Initial List Status'].dropna().unique()

# Rangos para campos numéricos
min_loan_amount, max_loan_amount = data['Loan Amount'].min(), data['Loan Amount'].max()
min_funded_amount, max_funded_amount = data['Funded Amount'].min(), data['Funded Amount'].max()
min_funded_amount_investor, max_funded_amount_investor = data['Funded Amount Investor'].min(), data['Funded Amount Investor'].max()
min_term, max_term = data['Term'].min(), data['Term'].max()
min_interest_rate, max_interest_rate = data['Interest Rate'].min(), data['Interest Rate'].max()
min_home_ownership, max_home_ownership = data['Home Ownership'].min(), data['Home Ownership'].max()
min_debit_to_income, max_debit_to_income = data['Debit to Income'].min(), data['Debit to Income'].max()
min_delinquency_two_years, max_delinquency_two_years = data['Delinquency - two years'].min(), data['Delinquency - two years'].max()
min_inquires_six_months, max_inquires_six_months = data['Inquires - six months'].min(), data['Inquires - six months'].max()
min_open_account, max_open_account = data['Open Account'].min(), data['Open Account'].max()
min_revolving_balance, max_revolving_balance = data['Revolving Balance'].min(), data['Revolving Balance'].max()
min_revolving_utilities, max_revolving_utilities = data['Revolving Utilities'].min(), data['Revolving Utilities'].max()
min_total_accounts, max_total_accounts = data['Total Accounts'].min(), data['Total Accounts'].max()
min_total_received_interest, max_total_received_interest = data['Total Received Interest'].min(), data['Total Received Interest'].max()
min_total_received_late_fee, max_total_received_late_fee = data['Total Received Late Fee'].min(), data['Total Received Late Fee'].max()
min_recoveries, max_recoveries = data['Recoveries'].min(), data['Recoveries'].max()
min_collection_recovery_fee, max_collection_recovery_fee = data['Collection Recovery Fee'].min(), data['Collection Recovery Fee'].max()
min_last_week_pay, max_last_week_pay = data['Last week Pay'].min(), data['Last week Pay'].max()
min_total_collection_amount, max_total_collection_amount = data['Total Collection Amount'].min(), data['Total Collection Amount'].max()
min_total_current_balance, max_total_current_balance = data['Total Current Balance'].min(), data['Total Current Balance'].max()
min_total_revolving_credit_limit, max_total_revolving_credit_limit = data['Total Revolving Credit Limit'].min(), data['Total Revolving Credit Limit'].max()


# Inicializar la aplicación de Streamlit
st.title("Aplicación de Predicción de Préstamos")

# Crear pestañas para cada modelo
tab1, tab2, tab3 = st.tabs(["Modelo 1", "Modelo 2", "Modelo 3"])

# Pestaña para Modelo 1
with tab1:
    st.header("Predicción con Modelo 1")

    # Crear selección para campos categóricos con opciones
    selected_batch_enrolled = st.selectbox("Batch Enrolled", unique_batch_enrolled)
    selected_grade = st.selectbox("Grade", unique_grade)
    selected_sub_grade = st.selectbox("Sub Grade", unique_sub_grade)
    selected_employment_duration = st.selectbox("Employment Duration", unique_employment_duration)
    selected_verification_status = st.selectbox("Verification Status", unique_verification_status)
    selected_loan_title = st.selectbox("Loan Title", unique_loan_title)
    selected_initial_list_status = st.selectbox("Initial List Status", unique_initial_list_status)

    # Crear controles para campos numéricos con rangos
    loan_amount = st.slider("Loan Amount", min_loan_amount, max_loan_amount, value=min_loan_amount)
    funded_amount = st.slider("Funded Amount", min_funded_amount, max_funded_amount, value=min_funded_amount)
    funded_amount_investor = st.slider("Funded Amount Investor", min_funded_amount_investor, max_funded_amount_investor, value=min_funded_amount_investor)
    term = st.slider("Term", min_term, max_term, value=min_term)
    interest_rate = st.slider("Interest Rate", min_interest_rate, max_interest_rate, value=min_interest_rate)
    home_ownership = st.slider("Home Ownership", min_home_ownership, max_home_ownership, value=min_home_ownership)
    debit_to_income = st.slider("Debit to Income", min_debit_to_income, max_debit_to_income, value=min_debit_to_income)
    delinquency_two_years = st.slider("Delinquency - two years", min_delinquency_two_years, max_delinquency_two_years, value=min_delinquency_two_years)
    inquires_six_months = st.slider("Inquires - six months", min_inquires_six_months, max_inquires_six_months, value=min_inquires_six_months)
    open_account = st.slider("Open Account", min_open_account, max_open_account, value=min_open_account)
    revolving_balance = st.slider("Revolving Balance", min_revolving_balance, max_revolving_balance, value=min_revolving_balance)
    revolving_utilities = st.slider("Revolving Utilities", min_revolving_utilities, max_revolving_utilities, value=min_revolving_utilities)
    total_accounts = st.slider("Total Accounts", min_total_accounts, max_total_accounts, value=min_total_accounts)
    total_received_interest = st.slider("Total Received Interest", min_total_received_interest, max_total_received_interest, value=min_total_received_interest)
    total_received_late_fee = st.slider("Total Received Late Fee", min_total_received_late_fee, max_total_received_late_fee, value=min_total_received_late_fee)
    recoveries = st.slider("Recoveries", min_recoveries, max_recoveries, value=min_recoveries)
    collection_recovery_fee = st.slider("Collection Recovery Fee", min_collection_recovery_fee, max_collection_recovery_fee, value=min_collection_recovery_fee)
    last_week_pay = st.slider("Last week Pay", min_last_week_pay, max_last_week_pay, value=min_last_week_pay)
    total_collection_amount = st.slider("Total Collection Amount", min_total_collection_amount, max_total_collection_amount, value=min_total_collection_amount)
    total_current_balance = st.slider("Total Current Balance", min_total_current_balance, max_total_current_balance, value=min_total_current_balance)
    total_revolving_credit_limit = st.slider("Total Revolving Credit Limit", min_total_revolving_credit_limit, max_total_revolving_credit_limit, value=min_total_revolving_credit_limit)
    
    
    if st.button('Predecir con Modelo 1'):
        # Empaquetar los datos en un formato JSON
        data = {
            "Batch Enrolled": selected_batch_enrolled,
            "Grade": selected_grade,
            "Sub Grade": selected_sub_grade,
            "Employment Duration": selected_employment_duration,
            "Verification Status": selected_verification_status,
            "Loan Title": selected_loan_title,
            "Initial List Status": selected_initial_list_status,
            "Loan Amount": loan_amount,
            "Funded Amount": funded_amount,
            "Funded Amount Investor": funded_amount_investor,
            "Term": term,
            "Interest Rate": interest_rate,
            "Home Ownership": home_ownership,
            "Debit to Income": debit_to_income,
            "Delinquency - two years": delinquency_two_years,
            "Inquires - six months": inquires_six_months,
            "Open Account": open_account,
            "Revolving Balance": revolving_balance,
            "Revolving Utilities": revolving_utilities,
            "Total Accounts": total_accounts,
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

    # Cargador de archivos
    uploaded_file = st.file_uploader("Cargar archivo de préstamos", type=["xlsx"])

    # Verificar si se ha cargado un archivo
    if uploaded_file is not None:
        # Leer el archivo Excel
        df_cargado = pd.read_excel(uploaded_file)
        
        # Procesar los datos o realizar acciones aquí
        st.write("Archivo cargado con éxito:")
        st.write(df_cargado)


    # Botón para enviar datos a la API
    if st.button("Enviar a la API para predicción"):
        if uploaded_file is not None:
            # Leer el archivo Excel
            df_cargado = pd.read_excel(uploaded_file)

            # Convertir DataFrame a un diccionario para el envío
            data_dict = df_cargado.to_dict(orient='records')

            # Enviar el lote de datos a la API
            response = requests.post('http://127.0.0.1:5000/predict1B', json=data_dict)

            if response.status_code == 200:
                # Mostrar la respuesta
                st.success(f'Predicciones: {response.json()}')
            else:
                st.error("Error en la predicción")
        else:
            st.error("Por favor, carga un archivo primero.")

###---------------------
with tab2:
    st.header("Predicción con Modelo 2")
    
    # Crear selección para campos categóricos con opciones
    selected_batch_enrolled2 = st.selectbox("Batch Enrolled", unique_batch_enrolled, key="batch_enrolled_2")
    selected_grade2 = st.selectbox("Grade", unique_grade, key="Grade2")
    selected_sub_grade2 = st.selectbox("Sub Grade", unique_sub_grade, key="SubGrade2")
    selected_employment_duration2 = st.selectbox("Employment Duration", unique_employment_duration,  key="EmploymentDuration2")
    selected_verification_status2 = st.selectbox("Verification Status", unique_verification_status,  key="Verification2")
    selected_loan_title2 = st.selectbox("Loan Title", unique_loan_title,  key="Loan2")
    selected_initial_list_status2 = st.selectbox("Initial List Status", unique_initial_list_status,  key="Initial2")

    # Crear controles para campos numéricos con rangos
    loan_amount2 = st.slider("Loan Amount", min_loan_amount, max_loan_amount, value=min_loan_amount, key="loan_amount2")
    funded_amount2 = st.slider("Funded Amount", min_funded_amount, max_funded_amount, value=min_funded_amount, key="FundedAmount2")
    funded_amount_investor2 = st.slider("Funded Amount Investor", min_funded_amount_investor, max_funded_amount_investor, value=min_funded_amount_investor, key="FundedAmountInvestor2")
    term2 = st.slider("Term", min_term, max_term, value=min_term, key="Term2")
    interest_rate2 = st.slider("Interest Rate", min_interest_rate, max_interest_rate, value=min_interest_rate, key="InterestRate2")
    home_ownership2 = st.slider("Home Ownership", min_home_ownership, max_home_ownership, value=min_home_ownership, key="HomeOwnership2")
    debit_to_income2 = st.slider("Debit to Income", min_debit_to_income, max_debit_to_income, value=min_debit_to_income, key="DebitIncome2")
    delinquency_two_years2 = st.slider("Delinquency - two years", min_delinquency_two_years, max_delinquency_two_years, value=min_delinquency_two_years, key="Delinquency2")
    inquires_six_months2 = st.slider("Inquires - six months", min_inquires_six_months, max_inquires_six_months, value=min_inquires_six_months, key="Inquires2")
    open_account2 = st.slider("Open Account", min_open_account, max_open_account, value=min_open_account, key="OpenAccount2")
    revolving_balance2 = st.slider("Revolving Balance", min_revolving_balance, max_revolving_balance, value=min_revolving_balance, key="RevolvingBalance2")
    revolving_utilities2 = st.slider("Revolving Utilities", min_revolving_utilities, max_revolving_utilities, value=min_revolving_utilities, key="RevolvingUtilities2")
    total_accounts2 = st.slider("Total Accounts", min_total_accounts, max_total_accounts, value=min_total_accounts, key="TotalAccounts2")
    total_received_interest2 = st.slider("Total Received Interest", min_total_received_interest, max_total_received_interest, value=min_total_received_interest, key="TotalReceivedInterest2")
    total_received_late_fee2 = st.slider("Total Received Late Fee", min_total_received_late_fee, max_total_received_late_fee, value=min_total_received_late_fee, key="TotalReceivedLateFee2")
    recoveries2 = st.slider("Recoveries", min_recoveries, max_recoveries, value=min_recoveries, key="Recoveries2")
    collection_recovery_fee2 = st.slider("Collection Recovery Fee", min_collection_recovery_fee, max_collection_recovery_fee, value=min_collection_recovery_fee, key="CollectionRecoveryFee2")
    last_week_pay2 = st.slider("Last week Pay", min_last_week_pay, max_last_week_pay, value=min_last_week_pay, key="LastweekPay2")
    total_collection_amount2 = st.slider("Total Collection Amount", min_total_collection_amount, max_total_collection_amount, value=min_total_collection_amount, key="TotalCollectionAmount2")
    total_current_balance2 = st.slider("Total Current Balance", min_total_current_balance, max_total_current_balance, value=min_total_current_balance, key="TotalCurrentBalance2")
    total_revolving_credit_limit2 = st.slider("Total Revolving Credit Limit", min_total_revolving_credit_limit, max_total_revolving_credit_limit, value=min_total_revolving_credit_limit, key="TotalRevolvingCreditLimit2")

    if st.button('Predecir con Modelo 2'):
        # Empaquetar los datos en un formato JSON
        data = {
            "Batch Enrolled": selected_batch_enrolled2,
            "Grade": selected_grade2,
            "Sub Grade": selected_sub_grade2,
            "Employment Duration": selected_employment_duration2,
            "Verification Status": selected_verification_status2,
            "Loan Title": selected_loan_title2,
            "Initial List Status": selected_initial_list_status2,
            "Loan Amount": loan_amount2,
            "Funded Amount": funded_amount2,
            "Funded Amount Investor": funded_amount_investor2,
            "Term": term2,
            "Interest Rate": interest_rate2,
            "Home Ownership": home_ownership2,
            "Debit to Income": debit_to_income2,
            "Delinquency - two years": delinquency_two_years2,
            "Inquires - six months": inquires_six_months2,
            "Open Account": open_account2,
            "Revolving Balance": revolving_balance2,
            "Revolving Utilities": revolving_utilities2,
            "Total Accounts": total_accounts2,
            "Total Received Interest": total_received_interest2,
            "Total Received Late Fee": total_received_late_fee2,
            "Recoveries": recoveries2,
            "Collection Recovery Fee": collection_recovery_fee2,
            "Last week Pay": last_week_pay2,
            "Total Collection Amount": total_collection_amount2,
            "Total Current Balance": total_current_balance2,
            "Total Revolving Credit Limit": total_revolving_credit_limit2
        }

        # Enviar los datos a la API y obtener la respuesta
        response = requests.post('http://127.0.0.1:5000/predict2S', json=data)
        if response.status_code == 200:
            # Mostrar la respuesta
            st.success(f'Predicción: {response.json()["Prediccion"]}')
        else:
            st.error("Error en la predicción")


    # Cargador de archivos
    uploaded_file2 = st.file_uploader("Cargar archivo de préstamos 2", type=["xlsx"])

    # Verificar si se ha cargado un archivo
    if uploaded_file2 is not None:
        # Leer el archivo Excel
        df_cargado = pd.read_excel(uploaded_file2)
        
        # Procesar los datos o realizar acciones aquí
        st.write("Archivo cargado con éxito:")
        st.write(df_cargado)



    # Botón para enviar datos a la API
    if st.button("Enviar a la API para predicción 2"):
        if uploaded_file2 is not None:
            # Leer el archivo Excel
            df_cargado = pd.read_excel(uploaded_file2)

            # Convertir DataFrame a un diccionario para el envío
            data_dict = df_cargado.to_dict(orient='records')

            # Enviar el lote de datos a la API
            response = requests.post('http://127.0.0.1:5000/predict2B', json=data_dict)

            if response.status_code == 200:
                # Mostrar la respuesta
                st.success(f'Predicciones: {response.json()}')
            else:
                st.error("Error en la predicción")
        else:
            st.error("Por favor, carga un archivo primero.")

###------------------
with tab3:
    st.header("Predicción con Modelo 3")
    
    # Crear selección para campos categóricos con opciones
    selected_batch_enrolled23 = st.selectbox("Batch Enrolled", unique_batch_enrolled, key="batch_enrolled_23")
    selected_grade23 = st.selectbox("Grade", unique_grade, key="Grade23")
    selected_sub_grade23 = st.selectbox("Sub Grade", unique_sub_grade, key="SubGrade23")
    selected_employment_duration23 = st.selectbox("Employment Duration", unique_employment_duration,  key="EmploymentDuration23")
    selected_verification_status23 = st.selectbox("Verification Status", unique_verification_status,  key="Verification23")
    selected_loan_title23 = st.selectbox("Loan Title", unique_loan_title,  key="Loan23")
    selected_initial_list_status23 = st.selectbox("Initial List Status", unique_initial_list_status,  key="Initial23")

    # Crear controles para campos numéricos con rangos
    loan_amount23 = st.slider("Loan Amount", min_loan_amount, max_loan_amount, value=min_loan_amount, key="loan_amount23")
    funded_amount23 = st.slider("Funded Amount", min_funded_amount, max_funded_amount, value=min_funded_amount, key="FundedAmount23")
    funded_amount_investor23 = st.slider("Funded Amount Investor", min_funded_amount_investor, max_funded_amount_investor, value=min_funded_amount_investor, key="FundedAmountInvestor23")
    term23 = st.slider("Term", min_term, max_term, value=min_term, key="Term23")
    interest_rate23 = st.slider("Interest Rate", min_interest_rate, max_interest_rate, value=min_interest_rate, key="InterestRate23")
    home_ownership23 = st.slider("Home Ownership", min_home_ownership, max_home_ownership, value=min_home_ownership, key="HomeOwnership23")
    debit_to_income23 = st.slider("Debit to Income", min_debit_to_income, max_debit_to_income, value=min_debit_to_income, key="DebitIncome23")
    delinquency_two_years23 = st.slider("Delinquency - two years", min_delinquency_two_years, max_delinquency_two_years, value=min_delinquency_two_years, key="Delinquency23")
    inquires_six_months23 = st.slider("Inquires - six months", min_inquires_six_months, max_inquires_six_months, value=min_inquires_six_months, key="Inquires23")
    open_account23 = st.slider("Open Account", min_open_account, max_open_account, value=min_open_account, key="OpenAccount23")
    revolving_balance23 = st.slider("Revolving Balance", min_revolving_balance, max_revolving_balance, value=min_revolving_balance, key="RevolvingBalance23")
    revolving_utilities23 = st.slider("Revolving Utilities", min_revolving_utilities, max_revolving_utilities, value=min_revolving_utilities, key="RevolvingUtilities23")
    total_accounts23 = st.slider("Total Accounts", min_total_accounts, max_total_accounts, value=min_total_accounts, key="TotalAccounts23")
    total_received_interest23 = st.slider("Total Received Interest", min_total_received_interest, max_total_received_interest, value=min_total_received_interest, key="TotalReceivedInterest23")
    total_received_late_fee23 = st.slider("Total Received Late Fee", min_total_received_late_fee, max_total_received_late_fee, value=min_total_received_late_fee, key="TotalReceivedLateFee23")
    recoveries23 = st.slider("Recoveries", min_recoveries, max_recoveries, value=min_recoveries, key="Recoveries23")
    collection_recovery_fee23 = st.slider("Collection Recovery Fee", min_collection_recovery_fee, max_collection_recovery_fee, value=min_collection_recovery_fee, key="CollectionRecoveryFee23")
    last_week_pay23 = st.slider("Last week Pay", min_last_week_pay, max_last_week_pay, value=min_last_week_pay, key="LastweekPay23")
    total_collection_amount23 = st.slider("Total Collection Amount", min_total_collection_amount, max_total_collection_amount, value=min_total_collection_amount, key="TotalCollectionAmount23")
    total_current_balance23 = st.slider("Total Current Balance", min_total_current_balance, max_total_current_balance, value=min_total_current_balance, key="TotalCurrentBalance23")
    total_revolving_credit_limit23 = st.slider("Total Revolving Credit Limit", min_total_revolving_credit_limit, max_total_revolving_credit_limit, value=min_total_revolving_credit_limit, key="TotalRevolvingCreditLimit23")

    if st.button('Predecir con Modelo 3'):
        # Empaquetar los datos en un formato JSON
        data = {
            "Batch Enrolled": selected_batch_enrolled23,
            "Grade": selected_grade23,
            "Sub Grade": selected_sub_grade23,
            "Employment Duration": selected_employment_duration23,
            "Verification Status": selected_verification_status23,
            "Loan Title": selected_loan_title23,
            "Initial List Status": selected_initial_list_status23,
            "Loan Amount": loan_amount23,
            "Funded Amount": funded_amount23,
            "Funded Amount Investor": funded_amount_investor23,
            "Term": term23,
            "Interest Rate": interest_rate23,
            "Home Ownership": home_ownership23,
            "Debit to Income": debit_to_income23,
            "Delinquency - two years": delinquency_two_years23,
            "Inquires - six months": inquires_six_months23,
            "Open Account": open_account23,
            "Revolving Balance": revolving_balance23,
            "Revolving Utilities": revolving_utilities23,
            "Total Accounts": total_accounts23,
            "Total Received Interest": total_received_interest23,
            "Total Received Late Fee": total_received_late_fee23,
            "Recoveries": recoveries23,
            "Collection Recovery Fee": collection_recovery_fee23,
            "Last week Pay": last_week_pay23,
            "Total Collection Amount": total_collection_amount23,
            "Total Current Balance": total_current_balance23,
            "Total Revolving Credit Limit": total_revolving_credit_limit23
        }

        # Enviar los datos a la API y obtener la respuesta
        response = requests.post('http://127.0.0.1:5000/predict2S', json=data)
        if response.status_code == 200:
            # Mostrar la respuesta
            st.success(f'Predicción: {response.json()["Prediccion"]}')
        else:
            st.error("Error en la predicción")


    # Cargador de archivos
    uploaded_file23 = st.file_uploader("Cargar archivo de préstamos 3", type=["xlsx"])

    # Verificar si se ha cargado un archivo
    if uploaded_file23 is not None:
        # Leer el archivo Excel
        df_cargado = pd.read_excel(uploaded_file23)
        
        # Procesar los datos o realizar acciones aquí
        st.write("Archivo cargado con éxito:")
        st.write(df_cargado)



    # Botón para enviar datos a la API
    if st.button("Enviar a la API para predicción 3"):
        if uploaded_file23 is not None:
            # Leer el archivo Excel
            df_cargado = pd.read_excel(uploaded_file23)

            # Convertir DataFrame a un diccionario para el envío
            data_dict = df_cargado.to_dict(orient='records')

            # Enviar el lote de datos a la API
            response = requests.post('http://127.0.0.1:5000/predict3B', json=data_dict)

            if response.status_code == 200:
                # Mostrar la respuesta
                st.success(f'Predicciones: {response.json()}')
            else:
                st.error("Error en la predicción")
        else:
            st.error("Por favor, carga un archivo primero.")


