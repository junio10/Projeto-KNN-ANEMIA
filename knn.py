import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

url = 'https://raw.githubusercontent.com/junio10/Projeto-KNN-ANEMIA/main/anemia.csv'
base_arquivo = pd.read_csv(url)
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'latin1').values

min_max = preprocessing.MinMaxScaler()
atributos_norm = min_max.fit_transform(base_Treinamento[:,:5])



diagnostico_norm = base_Treinamento[:, 5]

modelo = KNeighborsClassifier(n_neighbors = 1)
modelo.fit(atributos_norm, diagnostico_norm)

print('Acurácia: %.f' % (modelo.score(atributos_norm, diagnostico_norm)*100) + '%')

teste = [[0,11.6,22.3,30.9,74.5]]
teste2 = [[0,16.7,27.5,28.2,93]]

teste = min_max.transform(teste)
teste2 = min_max.transform(teste2)


print('Teste', modelo.predict(teste))
print('Teste2', modelo.predict(teste2))

