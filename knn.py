import pandas as pd
import preprocessing as pr
from sklearn.neighbors import KNeighborsClassifier

modelo = KNeighborsClassifier(n_neighbors = 3)
modelo.fit(normalized_attributes, classes)
pd.read_csv()


