""" 

Código criado para dicidir o dataset principal em 2 conjuntos de dados distintos baseados nas features  'cardiomegalia' e 'vnao_cardiomegalia'

"""

import pandas as pd

# Carrega o dataset original
df = pd.read_csv('metadata_200_imagens_traduzido.csv')

# Filtra o DataFrame para criar dois novos DataFrames
# 1. Imagens com "Cardiomegalia"
df_cardiomegalia = df[df['Finding Labels'] == 'Cardiomegalia']

# 2. Imagens que não têm "Cardiomegalia"
# O output do .unique() mostrou que o outro rótulo é 'Nada Encontrado'
df_nao_cardiomegalia = df[df['Finding Labels'] != 'Cardiomegalia']

# Salva os novos DataFrames em arquivos CSV
df_cardiomegalia.to_csv('cardiomegalia.csv', index=False)
df_nao_cardiomegalia.to_csv('nao_cardiomegalia.csv', index=False)

print("Arquivos CSV criados com sucesso: 'cardiomegalia.csv' e 'nao_cardiomegalia.csv'")

