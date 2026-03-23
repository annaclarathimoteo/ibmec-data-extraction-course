import pandas as pd 
import os



df = pd.read_excel('./dados.xlsx')


resumo = pd.DataFrame({
    'Nulos': df.isnull().sum(),
    'Percentual_Nulos': (df.isnull().sum() / len(df)) * 100,
    'Valores_Unicos': df.nunique(),
    'Tipo': df.dtypes
})

resumo.sort_values(by='Percentual_Nulos', ascending=False)



