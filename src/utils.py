import requests
import datetime
import streamlit as st

API_NIVEL_AGUA = "https://g12bbd4aea16cc4-orcl1.adb.ca-toronto-1.oraclecloudapps.com/ords/fiap/nivel_agua/"
API_VOLUME_CHUVA = "https://g12bbd4aea16cc4-orcl1.adb.ca-toronto-1.oraclecloudapps.com/ords/fiap/volume_chuva/"
API_SALVAR_LEITURA = "https://g12bbd4aea16cc4-orcl1.adb.ca-toronto-1.oraclecloudapps.com/ords/fiap/leituras/"
API_DISPARAR_SMS = "https://ijld8gsll8.execute-api.us-east-1.amazonaws.com/v1/alertaEnchente"


def buscar_nivel_rio():
    try:
        response = requests.get(API_NIVEL_AGUA, timeout=5)
        response.raise_for_status()
        # {'data_leitura': 'YYYY-MM-DDTHH:MM:SS', 'valor': X.Y}
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados do nível do rio: {e}")
        return None
    except ValueError:
        st.error("Erro ao decodificar resposta JSON (buscar_nivel_rio)")
        return None


def buscar_volume_chuva():
    try:
        response = requests.get(API_VOLUME_CHUVA, timeout=5)
        response.raise_for_status()
        # {'data_leitura': 'YYYY-MM-DDTHH:MM:SS', 'valor': X.Y}
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados do volume de chuva: {e}")
        return None
    except ValueError:
        st.error("Erro ao decodificar resposta JSON (buscar_volume_chuva)")
        return None


def salvar_leitura(sensor, valor):
    payload = {
        "data_leitura": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "sensor": sensor,
        "valor": valor
    }
    try:
        response = requests.post(API_SALVAR_LEITURA, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao salvar volume de chuva: {e}")
        return False


def enviar_alerta_sms(message: str):
    # ATENÇÃO: Os números de telefone devem ser formatados corretamente para o serviço de SMS
    # Ex: "+5511987654321" para Brasil, "+1234567890" para EUA/Canadá
    payload = {"message": message, "phone_numbers": [
        "+17782282166", "+5511938006662"]}  # Verifique esses números
    try:
        response = requests.post(API_DISPARAR_SMS, json=payload, timeout=10)
        response.raise_for_status()
        st.success(
            f"Alerta SMS enviado com sucesso! Status: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao enviar SMS: {e}")
        return False


def risco_enchente(nivel_atual, nivel_esperado, nivel_previsto_chuva, limite_moderado, limite_grave):
    # Diferenças do nível esperado que indicam atenção, mas não necessariamente enchente
        # Nível acima do esperado para um alerta de atenção
    DIFERENCA_ATENCAO_ESPERADO = 2.0
    # Nível ainda mais acima do esperado para observação
    DIFERENCA_OBSERVACAO_ESPERADO = 5.0

    risco = "Mínimo"
    cor_risco = "green"
    detalhes = []

    # --- Lógica de Classificação ---
    # Prioridade 1: Nível previsto com chuva (o cenário mais pessimista)
    if nivel_previsto_chuva >= limite_grave:
        risco = "Grave"
        cor_risco = "red"
        detalhes.append(
            f"Previsão de nível atingindo LIMITE GRAVE ({limite_grave:.2f}m).")
    elif nivel_previsto_chuva >= limite_moderado:
        risco = "Moderado"
        cor_risco = "orange"
        detalhes.append(
            f"Previsão de nível atingindo LIMITE MODERADO ({limite_moderado:.2f}m).")

    # Prioridade 2: Nível atual do rio (se já estiver alto)
    # Se já classificado como Grave, não rebaixa. Se classificado como Moderado, não rebaixa.
    if risco == "Mínimo":  # Apenas se o risco ainda não foi definido pela previsão de chuva
        if nivel_atual >= limite_grave:
            risco = "Grave"
            cor_risco = "red"
            detalhes.append(
                f"Nível ATUAL ({nivel_atual:.2f}m) já está no LIMITE GRAVE.")
        elif nivel_atual >= limite_moderado:
            risco = "Moderado"
            cor_risco = "orange"
            detalhes.append(
                f"Nível ATUAL ({nivel_atual:.2f}m) já está no LIMITE MODERADO.")

    # Prioridade 3: Avaliação do desvio em relação ao nível esperado
    # Esta parte é para casos onde o nível não atinge os limites absolutos de enchente,
    # mas está muito acima do que seria "normal" para a época.
    if risco == "Mínimo":  # Só aplica se o risco ainda for mínimo
        diferenca_atual_esperado = nivel_atual - nivel_esperado
        diferenca_prevista_esperado = nivel_previsto_chuva - nivel_esperado

        if diferenca_prevista_esperado >= DIFERENCA_OBSERVACAO_ESPERADO or \
           diferenca_atual_esperado >= DIFERENCA_OBSERVACAO_ESPERADO:
            risco = "Observação"  # Um novo nível para indicar "muito acima do esperado"
            cor_risco = "darkgoldenrod"  # Cor para esse nível
            detalhes.append(
                f"Nível ({nivel_atual:.2f}m) ou previsto ({nivel_previsto_chuva:.2f}m) muito acima do esperado ({nivel_esperado:.2f}m).")
        elif diferenca_prevista_esperado >= DIFERENCA_ATENCAO_ESPERADO or \
                diferenca_atual_esperado >= DIFERENCA_ATENCAO_ESPERADO:
            risco = "Atenção"  # Outro novo nível para "acima do esperado"
            cor_risco = "lightskyblue"  # Cor para esse nível
            detalhes.append(
                f"Nível ({nivel_atual:.2f}m) ou previsto ({nivel_previsto_chuva:.2f}m) acima do esperado ({nivel_esperado:.2f}m).")

    # Se houver um aumento significativo do nível atual para o previsto (mesmo que não atinja os limites)
    # E o risco ainda não for grave
    aumento_pela_chuva = nivel_previsto_chuva - nivel_atual
    if aumento_pela_chuva > 0.5 and risco != "Grave":  # Ex: aumento de mais de 0.5m
        # Se o nível atual já está "perto" de moderado
        if nivel_atual > (limite_moderado - DIFERENCA_ATENCAO_ESPERADO):
            if risco == "Mínimo" or risco == "Atenção":
                risco = "Moderado"
                cor_risco = "orange"
                detalhes.append(
                    f"Nível atual elevado com aumento considerável previsto pela chuva (+{aumento_pela_chuva:.2f}m).")

    # Garante que sempre haja pelo menos um detalhe
    if not detalhes:
        detalhes.append("Níveis dentro da normalidade.")

    return risco, cor_risco, ", ".join(detalhes)
