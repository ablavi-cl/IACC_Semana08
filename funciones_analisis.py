
import numpy as np
from scipy import stats
from joblib import dump, load


def calcular_promedio(datos):
    datos = np.array(datos)
    return np.mean(datos)


def calcular_intervalo():
    media = 125
    intervalo = stats.t.interval(0.95, df=2, loc=media, scale=1.5)
    return intervalo


def guardar_resultado(resultado, nombre_archivo):
    dump(resultado, nombre_archivo)
