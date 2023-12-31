from flask import Flask, request, render_template
import numpy as np
from pydantic import BaseModel
import pickle
import joblib as jb
from typing import List
from backend import model as md
from tensorflow.keras.models import load_model

app = Flask(__name__, template_folder="templates")

#http://127.0.0.1:5000
class InputData(BaseModel):
    historial_precios: List[float]
    
@app.route('/')
def raiz():
    return render_template('Index.html')

@app.route('/realizar_prediccion', methods=['POST'])
async def realizar_prediccion(data: InputData):
        model_predict = md.Modelo()
        # Obtener el historial de precios y convertirlo a un array de NumPy
        historial_precios = np.array(data.historial_precios).reshape(1, 60, 1)

        # Normalizar los datos de entrada utilizando el mismo scaler que se usó durante el entrenamiento
        #historial_precios_normalizado = scaler.transform(historial_precios)

        # Realizar predicciones con el modelo cargado
        nueva_prediccion_normalizada = model_predict.predict(historial_precios)

        # Deshacer la normalización de la predicción
        #nueva_prediccion_desnormalizada = scaler.inverse_transform(nueva_prediccion_normalizada)

        # Devolver la predicción como respuesta JSON
        return render_template('index.html', prediccion= float(nueva_prediccion_normalizada[0, 0]))
        #return render_template('index.html')

#Bloque de prueba
if __name__== "__main__":
    app.run(debug = True)