import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron


#importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/junio10/Projeto-KNN-ANEMIA/main/anemia.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'latin1').values

#normalizando os dados
min_max = preprocessing.MinMaxScaler()
#normalizando os dados
def normalizarDados(base_Treinamento):
    return min_max.fit_transform(base_Treinamento[:,:5])

#treinando a rede Knn
def treinarRedeKNN(atributos_norm,diagnostico_norm):
    modelo = KNeighborsClassifier(n_neighbors = 7)
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo
#treinan rede preceptron
def treinarRedePreceptron(atributos_norm,diagnostico_norm):
    modelo =  Perceptron()
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo

def Treinar(gender,hemoglobin,mch,mchc,mcv,algoritmo):
    dadosT = normalizarDados(base_Treinamento)
    diagnostico_norm = base_Treinamento[:, 5]
    if algoritmo == 1:
        modelo = treinarRedeKNN(dadosT,diagnostico_norm)
    else:
        modelo = treinarRedePreceptron(dadosT,diagnostico_norm)
    
    teste = [[gender,hemoglobin,mch,mchc,mcv]]
    testeT = min_max.transform(teste)
    return modelo.predict(testeT)
