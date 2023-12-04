import pickle
import numpy as np
from tensorflow.keras.models import load_model


class Modelo():
    def __init__(self):
        self = load_model("modelo_lstm.h5")