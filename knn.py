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
atributos_norm = min_max.fit_transform(base_Treinamento[:,:5])

diagnostico_norm = base_Treinamento[:, 5]

#treinando a rede
modelo = KNeighborsClassifier(n_neighbors = 1)
modelo.fit(atributos_norm, diagnostico_norm)
print('Acurácia: %.f' % (modelo.score(atributos_norm, diagnostico_norm) * 100) + '%')

