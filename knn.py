import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


#importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/junio10/Projeto-KNN-ANEMIA/main/anemia.csv'
base_arquivo = pd.read_csv(url)
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'latin1').values

#normalizando os dados
min_max = preprocessing.MinMaxScaler()
#normalizando os dados
def normaliazarDados(base_Treinamento):
    return min_max.fit_transform(base_Treinamento[:,:5])

#treinando a rede
def treinarRede(atributos_norm,diagnostico_norm):
    modelo = KNeighborsClassifier(n_neighbors = 1)
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo



def Treinar(n1,n2,n3,n4,n5):
    dadosT = normaliazarDados(base_Treinamento)
    diagnostico_norm = base_Treinamento[:, 5]
    modelo = treinarRede(dadosT,diagnostico_norm)
    teste = [[n1,n2,n3,n4,n5]]
    testeT = min_max.transform(teste)
    return modelo.predict(testeT)
