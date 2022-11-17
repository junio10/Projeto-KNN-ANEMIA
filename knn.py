import pandas as pd
import preprocessing as pr
from sklearn.neighbors import KNeighborsClassifier

url = 'https://raw.githubusercontent.com/junio10/Projeto-KNN-ANEMIA/main/anemia.csv?token=GHSAT0AAAAAAB2PNRK2VLCYNQ37HQ63EZEOY3WXE5A'
base_arquivo = pd.read_csv(url)

modelo = KNeighborsClassifier(n_neighbors = 3)
modelo.fit(normalized_attributes, classes)


