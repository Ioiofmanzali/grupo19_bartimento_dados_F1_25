import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os


def main(file_path):
    # --- 1. Ler o CSV ---
    # Manter a leitura simples, pois o formato que você mostrou já usa ponto decimal.
    print(f"\n--- Tentando ler o arquivo: {file_path} ---")
    df = pd.read_csv(file_path, sep=';')
    print("DataFrame lido com sucesso.")

    # --- DEBUG 1: Após a leitura inicial do CSV ---
    print("\n--- DEBUG 1: DataFrame após leitura inicial ---")
    print("Colunas encontradas:", df.columns.tolist())
    print("Primeiras 5 linhas (df.head()):")
    print(df.head())
    print("Tipos de dados (df.dtypes):")
    print(df.dtypes)
    print("---------------------------------------------")

    # Verifica se as colunas esperadas estão presentes
    expected_columns = ['DATA_HORA', 'CHUVA_DIA', 'NIVEL_RIO']
    if not all(col in df.columns for col in expected_columns):
        print(
            f"Erro: As colunas esperadas {expected_columns} não foram encontradas no arquivo.")
        print(f"Colunas encontradas: {df.columns.tolist()}")
        if len(df.columns) == 3:
            df.columns = expected_columns
            print("Colunas renomeadas para o formato esperado.")
        else:
            raise ValueError(
                "O número de colunas no arquivo não corresponde ao esperado (3).")

    # --- Pré-processamento das colunas numéricas (CHUVA_DIA e NIVEL_RIO) ---
    print("\n--- Iniciando pré-processamento de colunas numéricas ---")
    for col in ['CHUVA_DIA', 'NIVEL_RIO']:
        if col in df.columns:
            # Tenta converter diretamente para numérico.
            # O `errors='coerce'` é vital aqui, transforma valores inválidos em NaN.
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            print(
                f"Aviso: Coluna '{col}' não encontrada no DataFrame durante o pré-processamento numérico.")

    # Arredonda para 2 casas decimais, conforme solicitado
    df['CHUVA_DIA'] = df['CHUVA_DIA'].round(2)
    df['NIVEL_RIO'] = df['NIVEL_RIO'].round(2)

    # --- DEBUG 2: Após pré-processamento numérico e arredondamento ---
    print("\n--- DEBUG 2: DataFrame após pré-processamento numérico ---")
    print("Primeiras 5 linhas (df.head()):")
    print(df.head())
    print("Tipos de dados (df.dtypes):")
    print(df.dtypes)
    print("Valores mínimos e máximos de CHUVA_DIA:")
    print(
        f"  Min: {df['CHUVA_DIA'].min()}, Max: {df['CHUVA_DIA'].max()}, Média: {df['CHUVA_DIA'].mean():.2f}")
    print("Valores mínimos e máximos de NIVEL_RIO:")
    print(
        f"  Min: {df['NIVEL_RIO'].min()}, Max: {df['NIVEL_RIO'].max()}, Média: {df['NIVEL_RIO'].mean():.2f}")
    print("---------------------------------------------")

    # --- Converter DATA_HORA para o tipo datetime ---
    print("\n--- Iniciando conversão de DATA_HORA para datetime ---")
    df['DATETIME'] = pd.to_datetime(
        df['DATA_HORA'], format='%d/%m/%Y %H:%M', errors='coerce')

    # --- DEBUG 3: Após conversão de DATA_HORA ---
    print("\n--- DEBUG 3: DataFrame após conversão de DATA_HORA ---")
    print("Primeiras 5 linhas (df.head()):")
    print(df.head())
    print("Tipos de dados (df.dtypes):")
    print(df.dtypes)
    print("---------------------------------------------")

    # Remover linhas onde a conversão de data ou números falhou (NaNs)
    original_rows = len(df)
    df.dropna(subset=['DATETIME', 'CHUVA_DIA', 'NIVEL_RIO'], inplace=True)
    cleaned_rows = len(df)
    print(
        f"\n--- Removidas {original_rows - cleaned_rows} linhas com valores ausentes/inválidos. ---")

    # --- DEBUG 4: Após remoção de NaNs ---
    print("\n--- DEBUG 4: DataFrame Final para Treinamento ---")
    print("Primeiras 5 linhas (df.head()):")
    print(df.head())
    print("Tipos de dados (df.dtypes):")
    print(df.dtypes)
    print("Valores mínimos e máximos de CHUVA_DIA (FINAL):")
    print(
        f"  Min: {df['CHUVA_DIA'].min()}, Max: {df['CHUVA_DIA'].max()}, Média: {df['CHUVA_DIA'].mean():.2f}")
    print("Valores mínimos e máximos de NIVEL_RIO (FINAL):")
    print(
        f"  Min: {df['NIVEL_RIO'].min()}, Max: {df['NIVEL_RIO'].max()}, Média: {df['NIVEL_RIO'].mean():.2f}")
    print("---------------------------------------------")
    if df.empty:
        raise ValueError(
            "DataFrame vazio após limpeza. Verifique seu arquivo CSV.")

    # --- 2. Engenharia de Features ---
    df['HOUR'] = df['DATETIME'].dt.hour
    df['DAY_OF_YEAR'] = df['DATETIME'].dt.dayofyear
    df['DAY_OF_WEEK'] = df['DATETIME'].dt.dayofweek

    # --- 3. Preparar Diretório para Modelos ---
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modelos")
    os.makedirs(path, exist_ok=True)

    # --- 4. Definir os Modelos a serem testados ---
    models_to_train = [
        ("LinearRegression", LinearRegression()),
        ("RandomForestRegressor", RandomForestRegressor(random_state=42)),
        ("GradientBoostingRegressor", GradientBoostingRegressor(random_state=42)),
        ("Ridge", Ridge(random_state=42)),
        ("Lasso", Lasso(random_state=42))
    ]

    # --- 5. Treinar e Avaliar "Modelo Nível Esperado" ---
    print("\n--- Avaliando Modelos para 'Nível Esperado' ---")

    X_nivel_esperado = df[['HOUR', 'DAY_OF_YEAR', 'DAY_OF_WEEK']]
    y_nivel_esperado = df['NIVEL_RIO']

    X_train_ne, X_test_ne, y_train_ne, y_test_ne = train_test_split(
        X_nivel_esperado, y_nivel_esperado, test_size=0.2, random_state=42
    )

    best_model_ne = None
    best_mse_ne = float('inf')

    for name, model in models_to_train:
        print(f"Treinando {name} para Nível Esperado...")
        # Cria uma nova instância do modelo para evitar contaminação de treinamento anterior
        current_model = type(model)()
        if hasattr(current_model, 'random_state') and model.random_state is not None:
            current_model.random_state = model.random_state
        if isinstance(current_model, (Ridge, Lasso)) and hasattr(model, 'alpha'):
            current_model.alpha = model.alpha

        current_model.fit(X_train_ne, y_train_ne)
        predictions = current_model.predict(X_test_ne)
        mse = mean_squared_error(y_test_ne, predictions)
        print(f"   MSE para {name}: {mse:.4f}")

        if mse < best_mse_ne:
            best_mse_ne = mse
            best_model_ne = current_model
            best_model_name_ne = name

    print(
        f"\nMelhor modelo para 'Nível Esperado': {best_model_name_ne} com MSE de {best_mse_ne:.4f}")
    joblib.dump(best_model_ne, path + "/melhor_modelo_nivel_esperado.joblib")
    print(
        f"Melhor modelo '{best_model_name_ne}' salvo como 'melhor_modelo_nivel_esperado.joblib'.")

    # --- 6. Treinar e Avaliar "Modelo Previsão Chuva" ---
    print("\n--- Avaliando Modelos para 'Previsão Nível com Chuva' ---")

    X_previsao_chuva = df[['CHUVA_DIA', 'HOUR', 'DAY_OF_YEAR', 'DAY_OF_WEEK']]
    y_previsao_chuva = df['NIVEL_RIO']

    X_train_pc, X_test_pc, y_train_pc, y_test_pc = train_test_split(
        X_previsao_chuva, y_previsao_chuva, test_size=0.2, random_state=42
    )

    best_model_pc = None
    best_mse_pc = float('inf')

    for name, model in models_to_train:
        print(f"Treinando {name} para Previsão com Chuva...")
        # Cria uma nova instância do modelo para evitar contaminação de treinamento anterior
        current_model = type(model)()
        if hasattr(current_model, 'random_state') and model.random_state is not None:
            current_model.random_state = model.random_state
        if isinstance(current_model, (Ridge, Lasso)) and hasattr(model, 'alpha'):
            current_model.alpha = model.alpha

        current_model.fit(X_train_pc, y_train_pc)
        predictions = current_model.predict(X_test_pc)
        mse = mean_squared_error(y_test_pc, predictions)
        print(f"   MSE para {name}: {mse:.4f}")

        if mse < best_mse_pc:
            best_mse_pc = mse
            best_model_pc = current_model
            best_model_name_pc = name

    print(
        f"\nMelhor modelo para 'Previsão Nível com Chuva': {best_model_name_pc} com MSE de {best_mse_pc:.4f}")
    joblib.dump(best_model_pc, path + "/melhor_modelo_previsao_chuva.joblib")
    print("\nProcesso de treinamento, avaliação e salvamento dos melhores modelos concluído.")


if __name__ == '__main__':
    # Use o caminho correto do seu arquivo CSV.
    # Certifique-se de que o caminho corresponde exatamente ao local do seu arquivo.
    csv_file_path = r"C:\Users\techg\Desktop\gs2oficial\nivel_rio.csv"

    try:
        main(csv_file_path)
    except FileNotFoundError:
        print(
            f"Erro: O arquivo '{csv_file_path}' não foi encontrado. Por favor, verifique o caminho e o nome do arquivo.")
    except ValueError as ve:
        print(f"Erro de Validação de Dados: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
