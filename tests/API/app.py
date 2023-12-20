import pandas as pd
from flask import Flask, request, jsonify

from pycaret.classification import load_model
from pycaret.classification import predict_model
from datetime import datetime

app = Flask(__name__)
model1 = load_model('../../models/modelo1')
model2 = load_model('../../models/modelo2')
model3 = load_model('../../models/modelo3')

@app.route('/predict1S', methods=['POST'])
def predict1S():
       data = request.json
       data_to_predict = pd.json_normalize(data) #convertimos a dataframe con los tipos de datos default.
       print(data_to_predict)
       try:
              prediccion = predict_model(model1, data=data_to_predict)
              valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
              current_date = datetime.now()
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)

              print(valor_predicho)
              return jsonify({'Prediccion': valor_predicho})
       except:
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)
              return jsonify({'mensaje': "Se generó un error en la prediccicón."})

@app.route('/predict1B', methods=['POST'])
def predict1B():
    data = request.json
    try:
        # Inicializar una lista para almacenar las predicciones
        predicciones = []
        
        # Iterar sobre cada registro en los datos recibidos
        for record in data:
            data_to_predict = pd.json_normalize(record)
            prediccion = predict_model(model1, data=data_to_predict)
            valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
            predicciones.append(valor_predicho)

        # Registrar en el log
        current_date = datetime.now()
        with open('model_logs.log', 'a') as archivo_modificado:
            for valor_predicho in predicciones:
                strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                archivo_modificado.write(strLog)

        return jsonify({'Predicciones': predicciones})
    except Exception as e:
        with open('model_logs.log', 'a') as archivo_modificado:
            strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")}, {str(e)} \n'
            archivo_modificado.write(strLog)
        return jsonify({'mensaje': "Se generó un error en la predicción."})


@app.route('/predict2S', methods=['POST'])
def predict2S():
       data = request.json
       data_to_predict = pd.json_normalize(data) #convertimos a dataframe con los tipos de datos default.
       print(data_to_predict)
       try:
              prediccion = predict_model(model2, data=data_to_predict)
              valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
              current_date = datetime.now()
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)

              print(valor_predicho)
              return jsonify({'Prediccion': valor_predicho})
       except:
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)
              return jsonify({'mensaje': "Se generó un error en la prediccicón."})

@app.route('/predict2B', methods=['POST'])
def predict2B():
    data = request.json
    try:
        # Inicializar una lista para almacenar las predicciones
        predicciones = []
        
        # Iterar sobre cada registro en los datos recibidos
        for record in data:
            data_to_predict = pd.json_normalize(record)
            prediccion = predict_model(model2, data=data_to_predict)
            valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
            predicciones.append(valor_predicho)

        # Registrar en el log
        current_date = datetime.now()
        with open('model_logs.log', 'a') as archivo_modificado:
            for valor_predicho in predicciones:
                strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                archivo_modificado.write(strLog)

        return jsonify({'Predicciones': predicciones})
    except Exception as e:
        with open('model_logs.log', 'a') as archivo_modificado:
            strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")}, {str(e)} \n'
            archivo_modificado.write(strLog)
        return jsonify({'mensaje': "Se generó un error en la predicción."})


@app.route('/predict3S', methods=['POST'])
def predict3S():
       data = request.json
       data_to_predict = pd.json_normalize(data) #convertimos a dataframe con los tipos de datos default.
       print(data_to_predict)
       try:
              prediccion = predict_model(model3, data=data_to_predict)
              valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
              current_date = datetime.now()
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)

              print(valor_predicho)
              return jsonify({'Prediccion': valor_predicho})
       except:
              with open('model_logs.log', 'a') as archivo_modificado:
                     strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                     archivo_modificado.write(strLog)
              return jsonify({'mensaje': "Se generó un error en la prediccicón."})

@app.route('/predict3B', methods=['POST'])
def predict3B():
    data = request.json
    try:
        # Inicializar una lista para almacenar las predicciones
        predicciones = []
        
        # Iterar sobre cada registro en los datos recibidos
        for record in data:
            data_to_predict = pd.json_normalize(record)
            prediccion = predict_model(model3, data=data_to_predict)
            valor_predicho = round(list(prediccion['prediction_label'])[0], 4)
            predicciones.append(valor_predicho)

        # Registrar en el log
        current_date = datetime.now()
        with open('model_logs.log', 'a') as archivo_modificado:
            for valor_predicho in predicciones:
                strLog = f'{valor_predicho}, {current_date.strftime("%Y-%m-%d %H:%M:%S")} \n'
                archivo_modificado.write(strLog)

        return jsonify({'Predicciones': predicciones})
    except Exception as e:
        with open('model_logs.log', 'a') as archivo_modificado:
            strLog = f'Error, {current_date.strftime("%Y-%m-%d %H:%M:%S")}, {str(e)} \n'
            archivo_modificado.write(strLog)
        return jsonify({'mensaje': "Se generó un error en la predicción."})


@app.route('/saludo', methods=['GET'])
def saludo():
       strOut = "Servicio Arriba API"
       print(strOut)
       return jsonify({'mensaje': strOut})