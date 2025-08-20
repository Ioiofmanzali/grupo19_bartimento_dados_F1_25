# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# **BATIMENTOS DE DADOS - MAPEANDO O CORAÇÃO MODERNO**  

![capa](https://github.com/Ioiofmanzali/grupo19_bartimento_dados_F1_25/blob/main/assets/cora%C3%A7%C3%A3o.JPG)

## Grupo 19

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/jonatasgomes">Jônatas Gomes Alves</a>
- <a href="https://www.linkedin.com/in/iolanda-helena-fabbrini-manzali-de-oliveira-14ab8ab0">Iolanda Helena Fabbrini Manzali de Oliveira</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Murilo Carone Nasser</a> 
- <a href="https://www.linkedin.com/in/pedro-eduardo-soares-de-sousa-439552309">Pedro Eduardo Soares de Sousa</a>
- <a href= "https://www.linkedin.com/in/amanda-fragnan-b61537255">Amanda Fragnan<a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Andre Godoi Chaviato</a>


## 🔍 SOBRE O PROJETO

As doenças cardiovasculares (DCV) representam a principal causa de mortalidade e morbidade em escala global, um desafio de saúde pública que transcende fronteiras e sistemas de saúde. De acordo com a Organização Mundial da Saúde (OMS), as DCV são responsáveis por aproximadamente 19,8 milhões de mortes por ano no mundo, o que as coloca no topo da lista das causas de óbito. No Brasil, o cenário não é diferente: em 2022, as doenças cardiovasculares foram responsáveis pela perda de quase 400.000 vidas.

Essa alta incidência e mortalidade estão diretamente ligadas a uma combinação de fatores de risco. Eles são classicamente divididos em duas categorias:

Fatores de Risco Modificáveis: São aqueles que podem ser prevenidos ou controlados por meio de intervenções no estilo de vida e tratamento médico. Incluem hipertensão, diabetes, níveis elevados de colesterol, tabagismo, sedentarismo, obesidade e má alimentação. A detecção precoce e o manejo desses fatores são cruciais para a prevenção e redução da carga das DCV.

Fatores de Risco Não Modificáveis: São características inerentes ao indivíduo, como idade, gênero, histórico familiar e predisposição genética. Embora não possam ser alterados, o conhecimento desses fatores é vital para a identificação de grupos de alto risco, permitindo uma vigilância e intervenção clínica mais focada.

Nesse contexto, o projeto CardioIA surge como uma resposta inovadora a esse desafio. Ele simula um ecossistema de cardiologia inteligente, unindo o poder da Inteligência Artificial (IA) com a análise de dados clínicos, visuais e textuais. Nosso objetivo é não apenas entender a prevalência e a mortalidade das DCV, mas também construir ferramentas que possam auxiliar na triagem, diagnóstico, monitoramento e previsão de riscos, contribuindo para um futuro mais saudável.

A jornada do projeto, iniciada nesta Fase 1 - Batimentos de Dados, tem como objetivo a coleta e preparação das bases de dados. Esta etapa é fundamental, pois é o alicerce sobre o qual todos os módulos futuros de Machine Learning, Visão Computacional e Processamento de Linguagem Natural serão desenvolvidos.
    
###  🔒 GOVERNANÇA E SEGURANÇA DOS DADOS 

Este projeto foi construído com base nas seguintes práticas, garantindo total conformidade com a Lei Geral de Proteção de Dados (LGPD):

 * Anonimato dos Dados: O dataset utilizado é público, proveniente do Kaggle, e já passou por um processo de anonimização. 


 * Não Coleta de Dados Pessoais: Não houve manipulação de dados sensíveis. Cada paciente é representado por um código de identificação único, garantindo a privacidade total.

 
 * Integridade e Confidencialidade: Esta abordagem nos permite realizar a análise de dados cardiológicos de forma segura e ética, mantendo a integridade das informações e a confidencialidade dos pacientes.


## 📁 PARTE 1 - DATASETS NUMÉRICOS
O dataset original é composto por por 12 colunas e dividido em 3 categorias de variáveis: 

### 👤 Variáveis Demográficas:
    id: Identificador único do paciente.

    age: Idade do paciente em dias.

    gender: Sexo do paciente (1 = feminino, 2 = masculino).

    height: Altura do paciente em centímetros.

    weight: Peso do paciente em quilogramas.

### 🩺 Variáveis de Exame:
    ap_hi: Pressão arterial sistólica em mmHg.

    ap_lo: Pressão arterial diastólica em mmHg.

    cholesterol: Nível de colesterol (1: normal, 2: acima do normal, 3: muito acima do normal).

    gluc: Nível de glicose (1: normal, 2: acima do normal, 3: muito acima do normal).

    smoke: Se o paciente fuma (0: não, 1: sim).

    alco: Se o paciente consome álcool (0: não, 1: sim).

    active: Nível de atividade física (0: não ativo, 1: ativo).

### 🎯 Variável-alvo

    cardio: indica a presença ou ausência de doença cardiovascular (0: ausente, 1: presente).

Obs: Os números representam categorias de estado (como 'normal' ou 'acima do normal'; 'sim' ou 'não') e não devem ser interpretados como valores quantitativos. A exceção a essa regra se aplica às variáveis demográficas (age, height e weight) e as variáveis de exame relacionadas a pressão arterial (ap_hi e ap_lo). 

Esse dataset pode ser acessado através do link [[KAGGLE DVC](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset?select=cardio_train.csv)] 


## 📚 DATASETS


## SISTEMA DE ALERTA (AWS)



## 📊 ANÁLISE EXPLORATÓRIA DOS DADOS

O projeto é dividido em etapas principais: 

Coleta e Preparação dos Dados:

Foram utilizados dois arquivos CSV: inmet_sp.csv (contendo dados meteorológicos, incluindo precipitação) e desastres_sp.csv (com informações sobre eventos e desastres, onde extraímos dados relacionados ao nível de rios).
As features "chuva" (do arquivo INMET) e "rio" (do arquivo de desastres) foram selecionadas para a análise.

Análise Exploratória de Dados (EDA):

Foram realzadas as etapas de pre-processamento e tratamento dos dados.
Utilizamos histogramas para visualizar a frequência de ocorrência de diferentes volumes de chuva e níveis de rio.
Box plots foram empregados para identificar a dispersão dos dados e a presença de outliers, que podem indicar eventos extremos (chuvas intensas ou níveis de rio muito elevados/baixos).

Após a exploração e limpeza inicial, as features "chuva" e "rio" foram mescladas em um único conjunto de dados. Esta união foi feita com base em uma chave comum (provavelmente data ou localização, dependendo da estrutura original dos arquivos) para garantir a correlação correta entre os eventos de chuva e os níveis de rio correspondentes.

Para visualização do codigo  e da visualizacao gráfica dos da análise exploratória sugerimos que acesse os arquivos **desastres.ipynb** e **inmet_sp.ipynb**, ambos localizados na pasta 'docs' desse repositório.

## 📈 TREINAMENTO DO MODELO DE ML

O projeto utiliza o modelo de Regressão Linear visto que há uma relação   modelos com o objetivo de encontrar a combinação que oferece o melhor desempenho de generalização para os dados, ou seja, que consegue fazer as previsões mais precisas em dados não vistos durante o treinamento para prever o risco de enchente. 

A escolha da regressão linear como modelo ideal para analisar a relação entre "chuva" e "rio" neste projeto foi fortemente influenciada pelo tipo dos dados e tambem pelas caracteristicas das features serem quantitativas e contínuas.  Os modelos para nivel de chuva e nivel de rio foram salvos em .joblib e utilizados no app.py para previsão por IA.

## 🌧️ ESP 32 COM SENSORES

**Este projeto não requer hardware físico. Todos os componentes são virtuais e configurados dentro do ambiente de simulação Wokwi.**

Será descrita a seguir a estruturação do código, funcionalidade implementadas, dependências de hardware e software, além dos parâmetros de configuração.

![image](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/esp_32.JPG)


### Hardware (Simulador Wokwi)

  * Microcontrolador Virtual: ESP32 DevModule Kit C1 (selecionado no Wokwi).

  * Display Virtual: LCD 20x4 com módulo I2C (adicionado ao diagrama do Wokwi).

  * Sensores Virtuais:

    Sensor de Temperatura e Umidade (DHT22) conectado no pino 4

    Potenciômetro_1 (simulação de Chuva): Conectado ao pino 34
    
    Potenciômetro_2 (simulação de Nível do Rio): Conectado ao pino 35
    
  * Requisitos de Software / Bibliotecas
    
    Ambiente de Desenvolvimento Online:

    Wokwi.com (para edição, simulação e execução do código).

    Bibliotecas:
    
    Wire.h: Biblioteca padrão para comunicação I2C.
    
    LiquidCrystal_I2C.h: Biblioteca para controle de displays LCD via interface I2C.

    DHT.h: Biblioteca para leitura de sensores DHT11/DHT22 (suporte à função DHTTYPE).

    Adafruit_Sensor.h: Biblioteca genérica para sensores Adafruit (dependência da DHT.h).


Obs: Para simular um ambiente node sensores captam os dados do ambiente foi utilizado no código sketch.ino uma funcionalidade para gerar dados aleatórios

<p align="center">
  <img src="https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/dadosfake.JPG" alt="Descrição da Imagem 1" width="48%">
  <img src="https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/dadosfake1.JPG" alt="Descrição da Imagem 2" width="48%">
</p>       


[LINK PARA O PROJETO GLOBAL_SOLUTION_2](https://wokwi.com/projects/432676821844364289)


## 📣 PRÓXIMOS PASSOS

Este projeto foi desenvolvido com um protótipo funcional que demonstra o potencial de um sistema de monitoramento de enchentes, utilizando dados simulados ou de teste para suas validações.
Acreditamos que esse é o começo de uma idéia com grande potencial  e com impacto real.

   * Coleta e Integração de Dados Reais e Contínuo
     
   * Parcerias com Órgãos Governamentais para acesso aos dados de todas as estações de monitoramento

   * Integraççao de outras fontes de dados que possam influenciar enchentes (temperatura, umidade, vazão, etc.)

   * Aprimoramento dos Modelos de Machine Learning com dados reais e datasets mais robustos

   * Re-treinamento contínuo dos modelos com os novos dados coletados, garantindo que eles se adaptem a padrões sazonais e mudanças ambientais.

   *  Explorar e criar novas features a partir dos dados existentes
   
   *  Dashboards mais complexos com múltiplos painéis
   
   * Implementação de Alertas e Notificações personalizados e por múltiplos canais

   * Lógica de disparo otimizada de alertas para evitar "falsos positivos" ou o envio excessivo de mensagens, considerando a duração do risco e a severidade.

   * Deployment e Infraestrutura que permita que o projeto funcione 24/7 e atenda a usuários reais

## :octocat: CONTRIBUIÇÕES AO PROJETO

Ficamos muito felizes com a sua contribuição e valorizamos cada sugestão e esforço dedicado a aprimorá-lo.

Como Contribuir: 

* Clique no botão "Fork" no canto superior direito desta página para criar uma cópia do repositório na sua conta do GitHub.

* Clone o repositório forkado para o seu ambiente de desenvolvimento local.

* Crie uma branch separada para a sua contribuição, desenvolva suas modificações e realize os commits necessários na sua branch.

* Quando suas alterações estiverem prontas, envie um Pull Request do seu fork para a branch main deste repositório.

Seu Pull Request será revisado pela equipe e, se tudo estiver correto, será aceito e suas contribuições serão integradas ao projeto 😃!

## COMO RODAR O PROGRAMA A PARTIR DO VSCODE

### Streamlit
1. Abrir o Terminal no VS Code
     No menu superior, clique em Terminal e depois em Novo Terminal ou utilize o atalho "CTRL J". Isso abrirá um painel de terminal na parte inferior da janela do VS Code.
     
2. No terminal digite os comandos cd e run para abrir o arquivo e, em seguida, o navegador onde o aplicativo será aberto:
 
 ** após executar o comando streamlit run app.py, o Streamlit irá iniciar um servidor local e abrir automaticamente o seu aplicativo em uma nova aba do seu navegador web padrão.
 
 ** também aparecerá no terminal o endereço local onde o aplicativo está rodando (pode copiar e colar esse endereço no seu navegador, caso ele não abra automaticamente).

### Wokwi

1. Acesse o Wokwi

Abra seu navegador e vá para o link de simulação do Wokwi para este projeto:

[[LINK WOKWI](https://wokwi.com/projects/432676821844364289)]

2. Inicie a Simulação
  
Uma vez na página do Wokwi, procure e clique no botão verde "Play" (geralmente localizado na parte superior ou lateral da interface) e poderá visualizar os dados gerados pelo código atraves do monitos de LCD.

## 📁 ESTRUTURA DE PASTAS

- <b>assets</b>: imagens utilizadas no projeto e documentação

- <b>docs</b>: códigos auxiliares utilizadas no projeto
  
- <b>src</b>: códigos principais do programa
  
- <b>README.md</b>: guia e explicação geral sobre o projeto

##  🎬 VIDEO DEMONSTRATIVO

[Video demonstrativo do Projeto](https://youtu.be/Y8b9HNfbJVU)

## 🗃 HISTÓRICO DE LANÇAMENTOS

![Versão 1.0.0](https://img.shields.io/badge/Vers%C3%A3o%201.0.0-gray?style=flat)  - 03/09/2025
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
