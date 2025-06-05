import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
from datetime import datetime

# === Configurações de Caminho ===
PATH_MODELOS = os.path.join(os.path.dirname(__file__), "modelos")
os.makedirs(PATH_MODELOS, exist_ok=True)

# Caminho do seu arquivo CSV
CSV_FILE_PATH = r'C:\Users\techg\Desktop\gs2oficial\nivel_rio.csv'


try:
    print(f"\n🔄 Carregando o arquivo CSV de: {CSV_FILE_PATH}")
    df = pd.read_csv(CSV_FILE_PATH, sep=';')
    print("✅ CSV carregado com sucesso.")

    # === Tratamento da coluna de data ===
    print("🔧 Convertendo 'DATA_HORA' para formato datetime...")
    df['DATA_HORA'] = pd.to_datetime(df['DATA_HORA'], errors='coerce')

    # Remover linhas com data inválida
    datas_invalidas = df['DATA_HORA'].isnull().sum()
    if datas_invalidas > 0:
        print(
            f"⚠️ {datas_invalidas} linhas com 'DATA_HORA' inválida foram removidas.")
        df.dropna(subset=['DATA_HORA'], inplace=True)
    else:
        print("✅ 'DATA_HORA' convertida sem problemas.")

    # === Limpeza da coluna CHUVA_DIA ===
    print("\n🔧 Limpando e convertendo 'CHUVA_DIA' para formato numérico...")
    df['CHUVA_DIA'] = df['CHUVA_DIA'].astype(str)  # garante que seja string
    df['CHUVA_DIA'] = df['CHUVA_DIA'].str.replace(
        '.', '', regex=False)  # remove pontos (separadores de milhar)
    # converte para float, NaN onde falhar
    df['CHUVA_DIA'] = pd.to_numeric(df['CHUVA_DIA'], errors='coerce')

    chuva_invalidas = df['CHUVA_DIA'].isnull().sum()
    if chuva_invalidas > 0:
        print(
            f"⚠️ {chuva_invalidas} linhas com 'CHUVA_DIA' inválida foram removidas.")
        df.dropna(subset=['CHUVA_DIA'], inplace=True)
    else:
        print("✅ 'CHUVA_DIA' convertida sem problemas.")

    # === Tratamento de dados ausentes nas outras colunas ===
    print("\n🔍 Verificando dados ausentes...")
    print(df[['NIVEL_RIO', 'CHUVA_DIA', 'DATA_HORA']].isnull().sum())

    # Preencher ou remover nulos nas colunas principais
    df['CHUVA_DIA'] = df['CHUVA_DIA'].fillna(0)
    df['NIVEL_RIO'] = df['NIVEL_RIO'].fillna(
        method='ffill')  # Forward fill, se desejar

    # === Extração de features ===
    df['HOUR'] = df['DATA_HORA'].dt.hour
    df['DAY_OF_YEAR'] = df['DATA_HORA'].dt.dayofyear
    df['DAY_OF_WEEK'] = df['DATA_HORA'].dt.dayofweek  # 0=Segunda, 6=Domingo

    # === Modelo 1: Nível Esperado (sem chuva) ===
    print("\n🚀 Iniciando treinamento do modelo de Nível Esperado (sem considerar chuva)...")
    X_expected = df[['HOUR', 'DAY_OF_YEAR', 'DAY_OF_WEEK']]
    y_expected = df['NIVEL_RIO']

    model_expected = LinearRegression()
    model_expected.fit(X_expected, y_expected)

    joblib.dump(model_expected, os.path.join(
        PATH_MODELOS, "modelo_nivel_esperado.joblib"))
    print("✅ Modelo 'modelo_nivel_esperado.joblib' salvo com sucesso.")

    # === Modelo 2: Previsão com Chuva ===
    print("\n🚀 Iniciando treinamento do modelo de Previsão com Chuva...")
    X_rain = df[['CHUVA_DIA', 'HOUR', 'DAY_OF_YEAR', 'DAY_OF_WEEK']]
    y_rain = df['NIVEL_RIO']

    model_rain = LinearRegression()
    model_rain.fit(X_rain, y_rain)

    joblib.dump(model_rain, os.path.join(
        PATH_MODELOS, "modelo_previsao_chuva.joblib"))
    print("✅ Modelo 'modelo_previsao_chuva.joblib' salvo com sucesso.")

    print("\n🎉 Treinamento dos modelos concluído com sucesso!")

except FileNotFoundError:
    print(
        f"\n❌ ERRO CRÍTICO: O arquivo CSV '{CSV_FILE_PATH}' não foi encontrado. Verifique o caminho.")
except KeyError as e:
    print(
        f"\n❌ ERRO CRÍTICO: Coluna '{e}' não encontrada no CSV. Verifique os nomes das colunas (NIVEL_RIO, CHUVA_DIA, DATA_HORA).")
except Exception as e:
    print(f"\n❌ OCORREU UM ERRO INESPERADO: {e}")
