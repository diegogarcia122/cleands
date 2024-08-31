import pandas as pd

dataframe = pd.read_csv('netflix_titles.csv')

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

#Separarando fechas
dataframe['date_added'] = pd.to_datetime(dataframe['date_added'])
dataframe['day'] = dataframe['date_added'].dt.day
dataframe['month'] = dataframe['date_added'].dt.month
dataframe['year'] = dataframe['date_added'].dt.year
print(dataframe[['day', 'month', 'year']].head(5), "\n")

#Cambiando los valores null
newdf = dataframe.fillna("0")
newdf.to_csv("new_netflix_df.csv")
print(newdf, "\n")