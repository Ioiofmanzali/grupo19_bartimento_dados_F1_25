from machine import Pin, ADC
from time import sleep
import network
import urequests
import json
import time
import ntptime
import random

# ---------------------------
# Configurações Wi-Fi
# ---------------------------
print("Conectando-se ao Wi-Fi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Substituir pelo seu Wi-Fi real se necessário
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print("\nConectado ao Wi-Fi!")
print("Endereço IP:", sta_if.ifconfig()[0])

# ---------------------------
# Sincronizar horário NTP
# ---------------------------
try:
    ntptime.settime()
    print("Tempo sincronizado com NTP.")
except OSError as e:
    print("Erro ao sincronizar tempo com NTP:", e)

# ---------------------------
# Configurações dos sensores
# ---------------------------

# Potenciômetros para chuva e nível do rio
pot_chuva = ADC(Pin(34))
pot_chuva.atten(ADC.ATTN_11DB)  # Garante leitura de 0 a 3.3V

pot_rio = ADC(Pin(35))
pot_rio.atten(ADC.ATTN_11DB)

# ---------------------------
# Funções auxiliares
# ---------------------------


def gerar_temperatura_fake():
    return random.uniform(15.0, 40.0)


def gerar_umidade_fake():
    return random.randint(20, 100)


def ler_chuva():
    valor = pot_chuva.read()  # 0 a 4095
    return round((valor * 50.0) / 4095.0, 1)  # Chuva em mm (0 a 50 mm)


def ler_rio():
    valor = pot_rio.read()  # 0 a 4095
    # Nível do rio em metros (0.5 a 15 m)
    return round(((valor * (15.0 - 0.5)) / 4095.0) + 0.5, 2)


def get_current_time_iso():
    tm = time.localtime()
    year, month, day, hour, minute, second, *_ = tm
    return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}.000Z".format(year, month, day, hour, minute, second)


def enviar_dados_api(sensor, valor, timestamp):
    url_api = "https://g12bbd4aea16cc4-orcl1.adb.ca-toronto-1.oraclecloudapps.com/ords/fiap/leituras/"
    headers = {"Content-Type": "application/json"}

    data = {
        "data_leitura": timestamp,
        "sensor": sensor,
        "valor": valor
    }

    try:
        response = urequests.post(url_api, headers=headers, json=data)
        if response.status_code == 201:
            print(f"✔ Dados do sensor '{sensor}' enviados com sucesso.")
        else:
            print(
                f"❌ Erro ao enviar dados do sensor '{sensor}': {response.status_code}")
            print(response.text)
        response.close()
    except Exception as e:
        print(f"⚠ Erro de conexão ao enviar dados do sensor '{sensor}': {e}")

# ---------------------------
# Loop principal
# ---------------------------


# Valores anteriores (para evitar reenvio se não mudar)
temp_ant = None
umidade_ant = None
chuva_ant = None
rio_ant = None

while True:
    try:
        # Leitura dos sensores
        temperatura = round(gerar_temperatura_fake(), 1)
        umidade = gerar_umidade_fake()
        chuva = ler_chuva()
        rio = ler_rio()

        # Timestamp da leitura
        dt = get_current_time_iso()

        # Exibir no terminal
        print("\nLeitura atual:")
        print(f"Temperatura: {temperatura} °C")
        print(f"Umidade: {umidade} %")
        print(f"Chuva: {chuva} mm")
        print(f"Nível do Rio: {rio} m")
        print(f"Timestamp: {dt}")

        # Enviar para API apenas se houver mudança
        if temperatura != temp_ant:
            enviar_dados_api("Temperatura", temperatura, dt)
            temp_ant = temperatura

        if umidade != umidade_ant:
            enviar_dados_api("Umidade", umidade, dt)
            umidade_ant = umidade

        if chuva != chuva_ant:
            enviar_dados_api("Chuva", chuva, dt)
            chuva_ant = chuva

        if rio != rio_ant:
            enviar_dados_api("NivelRio", rio, dt)
            rio_ant = rio

    except Exception as e:
        print(f"⚠ Erro geral: {e}")

    sleep(5)  # Espera 5 segundos para a próxima leitura



    print()