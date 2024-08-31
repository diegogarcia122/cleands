import pandas as pd

dataframe = pd.read_csv('US_AFRF.csv')

print("Head:")
print(dataframe.head(10), "\n")

#Porcentaje de valores null
percent = dataframe.isnull().sum() * 100 / len(dataframe)
missingtable = pd.DataFrame({'percent': percent})
print(missingtable, "\n")

print("Tipos:")
print(dataframe.dtypes, "\n")

# Eliminar espacios en blanco al inicio de cada dato
dataframe = dataframe.map(lambda x: x.strip() if isinstance(x, str) else x)

#Cambiando los valores null
newdf = dataframe.fillna("0")
newdf.to_csv("new_AFRF_df.csv")
print(newdf, "\n")