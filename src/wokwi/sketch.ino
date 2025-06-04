#include <Wire.h>             // Biblioteca padrão para comunicação I2C
#include <LiquidCrystal_I2C.h> // Biblioteca para LCD via I2C
#include <DHT.h>
#include <Adafruit_Sensor.h>

// --- Configurações dos Pinos (não serão usados para leituras reais neste código de simulação)
#define DHTPIN 4
#define DHTTYPE DHT22
#define POT_PIN 35 // Mantido, mas não usado para simulação direta aqui

// --- Endereço I2C do LCD ---
const int LCD_ADDR = 0x27; // Endereço I2C do seu LCD
const int LCD_COLUMNS = 20; // Número de colunas do seu LCD
const int LCD_ROWS = 4;     // Número de linhas do seu LCD

// --- Inicialização do LCD ---
LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLUMNS, LCD_ROWS); // Cria um objeto LCD

// --- Variáveis Globais ---
float temperatura = 0.0;
float umidade = 0.0;
float chuva = 0.0; // Variável para Precipitação (Chuva)
float rio = 0.0;   // Variável para Nível do Rio

unsigned long lastReadTime = 0;
const long readInterval = 10000; // Intervalo de atualização dos dados em milissegundos (10 segundos)

// --- Funções Auxiliares para Dados Fake ---
// Geração de números aleatórios para Temperatura
float generateFakeTemperature() {
  // Gera temperatura entre 15.0 e 40.0 *C
  return random(050, 401) / 10.0; // Multiplica por 10 e divide depois para ter casas decimais
}

// Geração de números aleatórios para Umidade
float generateFakeHumidity() {
  // Gera umidade entre 20% e 100%
  return random(20, 101); // O limite superior é exclusivo, então 96 para incluir 95
}

// Geração de números aleatórios para Chuva (Precipitação)
float generateFakeChuva() { // Alterado o nome da função para 'generateFakeChuva'
  // Gera precipitação entre 0.0 e 50.0 mm (pode simular sem chuva ou chuva forte)
  // random(min * 10, max * 10 + 1) / 10.0 para floats
  return random(0, 501) / 10.0; // De 0.0 a 50.0 mm
}

// Geração de números aleatórios para Nível do Rio
float generateFakeRio() { // NOVA FUNÇÃO para o nível do rio
  // Gera nível do rio entre 0.5 e 15.0 metros
  // Ajuste estes limites para simular níveis normais e de enchente
  return random(5, 151) / 10.0; // De 0.5 a 15.0 metros
}

// --- SETUP ---
void setup() {
  Serial.begin(115200); // Inicia a comunicação serial
  Serial.println("Estação Meteorológica Global Solution - Iniciando...");

  // Inicializa o LCD
  lcd.init();       // Inicializa o I2C para o LCD
  lcd.backlight();  // Liga a luz de fundo do LCD

  lcd.clear(); // Limpa a tela
  lcd.setCursor(0, 0); // Define o cursor na coluna 0, linha 0
  lcd.print("Estacao GS2");
  lcd.setCursor(0, 1);
  lcd.print("Gerando dados...");
  delay(2000); // Espera 2 segundos
  randomSeed(analogRead(0)); // Inicializa o gerador de números aleatórios (para maior aleatoriedade)
}

// --- LOOP ---
void loop() {
  unsigned long currentTime = millis();

  // Gera e exibe dados fake a cada 'readInterval'
  if (currentTime - lastReadTime >= readInterval) {
    lastReadTime = currentTime;

    // --- Gerar Dados Fake ---
    temperatura = generateFakeTemperature();
    umidade = generateFakeHumidity();
    chuva = generateFakeChuva(); // Chamando a nova função para chuva
    rio = generateFakeRio();     // Chamando a nova função para o rio

    // --- Enviar dados para o Monitor Serial ---
    Serial.print("Temperatura: ");
    Serial.print(temperatura, 1); // 1 casa decimal
    Serial.print(" *C\t");
    Serial.print("Umidade: ");
    Serial.print(umidade, 0); // Sem casas decimais
    Serial.print(" %\t");
    Serial.print("Chuva: "); // Alterado o rótulo
    Serial.print(chuva, 1);   // Variável 'chuva'
    Serial.println(" mm");
    Serial.print("Rio: ");   // NOVO: Exibindo o nível do rio
    Serial.print(rio, 2);    // 2 casas decimais para o rio
    Serial.println(" m");


    // --- Exibir dados no LCD2004 ---
    lcd.clear(); // Limpa o LCD para cada nova atualização

    // Linha 0: Temperatura
    lcd.setCursor(0, 0);
    lcd.print("Temp:"); // Encurtado para caber no LCD
    lcd.print(temperatura, 1); // 1 casa decimal
    lcd.print((char)223); // Caractere de grau
    lcd.print("C");

    // Linha 1: Umidade
    lcd.setCursor(0, 1);
    lcd.print("Umidade:");
    lcd.print(umidade, 0); // Sem casas decimais
    lcd.print("%");

    // Linha 2: Chuva
    lcd.setCursor(0, 2);
    lcd.print("Chuva:");
    lcd.print(chuva, 1); // 1 casa decimal
    lcd.print("mm");

    // Linha 3: Rio
    lcd.setCursor(0, 3);
    lcd.print("Rio:"); // Encurtado para caber
    lcd.print(rio, 2);  // 2 casas decimais
    lcd.print("m");

  }
}