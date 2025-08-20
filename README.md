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

## Desenvolvedores

Amanda Fragnan, Iolanda Manzali, Jonatas Gomes, Murilo Nasser, Pedro Sousa 


![Versão 1.0.0](https://img.shields.io/badge/Vers%C3%A3o%201.0.0-gray?style=flat)


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


## 🛠️ TECNOLOGIAS UTILIZADAS

![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) &nbsp; ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) &nbsp; ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=Oracle&logoColor=white) ![Oracle APEX](https://img.shields.io/badge/Oracle%20APEX-green?style=for-the-badge&logo=oracle&logoColor=white)

### 1. ORACLE

* Esse projeto utiliza duas funcionalidades Oracle:
  
  * API RESTful da Oracle, hospedada na Oracle Cloud, configurada para permitir tratamento de paginação e erros, garantindo que os dados necessários para as funcionalidades do projeto sejam carregados de maneira confiável.

  * DB Oracle, para salvar os dados gerados pelo ESP 32, simulando uma situação real de captação de dados por sensores. 

### API ORACLE

  * Requisição HTTP GET:
    
Quando buscar_nivel_rio() ou buscar_volume_chuva() são chamadas, elas executam uma operação requests.get(). Isso instrui o programa a enviar uma requisição HTTP GET para a URL especificada (API_NIVEL_AGUA ou API_VOLUME_CHUVA) em um tempo limite de 5 segundos para a requisição. Se o servidor não responder dentro desse período, uma exceção será levantada.

  * Recebimento da Resposta HTTP:
    
O servidor da API processa a requisição GET e, se tudo estiver correto, envia de volta uma resposta HTTP. Essa resposta contém um código de status (ex: 200 OK, 404 Not Found, 500 Internal Server Error) e o corpo da resposta. Isso garante que o programa não tente processar dados de uma requisição que falhou, tornando o tratamento de erros mais robusto.

  * Decodificação JSON (response.json()):
    
Se a requisição foi bem-sucedida (código de status 2xx), o corpo da resposta é esperado que esteja no formato JSON (JavaScript Object Notation). A linha data = response.json() é responsável por parsear a string JSON recebida no corpo da resposta HTTP e convertê-la em um objeto Python em um formato específico - {'data_leitura': 'YYYY-MM-DDTHH:MM:SS', 'valor': X.Y} - que será transformado em um dicionário Python com as chaves 'data_leitura' e 'valor'.

  * Tratamento de Erros:
    
As operações de consumo de API são encapsuladas em blocos try-except.
  - except requests.exceptions: Captura qualquer erro relacionado à requisição HTTP (problemas de rede, timeout, erros de status HTTP capturados por raise_for_status()).
  - except ValueError: Captura erros que ocorrem se a resposta da API não for um JSON válido ou se houver problemas na sua decodificação.

  Em ambos os casos de erro, uma mensagem é exibida usando st.error (a aplicação é construída com Streamlit para exibir esses erros na interface do usuário) e a função retorna None, sinalizando que a operação de busca falhou.

### 2. PYTHON

* Atua como a linguagem principal para definir a arquitetura da aplicação web, organizando o conteúdo através de botões de navegação no menu principal.

** maiores detalhes na seção Arquitetura do Programa

### 3. STREAMLIT

A interface do usuário é organizada em uma única página.

![pagina_inicial](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/capast.JPG)


A interface mostra os níveis atual, esperado e previsto do rio e a classificação do risco de enchente.

Na aba lateral, podemos determinar o nivel de água (grave e moderado) e tambem simular situações com valores atribuidos de nível de rio e chuva. 

## 📚 DATASETS

### INMET

Os datasets IMNET foram processados conforme o descrito a seguir:
  - Preenchimento de valores ausentes: a maioria dos valores ausentes do dataset INMET está na coluna de radiacao_global, que não foi utilizada nesse projeto. Para os campos precipitacao_total não foram encontrados valores ausentes ou duplicados.

### S2iD (Sistema Integrado de Informações sobre Desastres)

O dataset  S2iD foi processado condorme o descrito a seguir:

  - feito o download da série histórica e filtrados somente os desastres do tipo hidrológico (enxurradas, alagamentos, chuvas intensas, movimento de massa e inundações) para a cidade de São Paulo.
    
  - selecionadas as colunas mais significativas para uso no projeto para o treinamento de  ML/DL:
    
    * DATA_EVENTO
    * TIPO_EVENTO
    * ÓBITOS
    * FERIDOS 
    * ENFERMOS
    * DESABRIGADOS
    * DESALOJADOS
    * DESAPARECIDOS
    * RESIDENCIAS_DANIFICADAS
    * RESIDENCIAS_DESTRUIDAS
    * DANO_PATRIMONIO_PL

  ** Obs: todos os parâmetros acima estão estritamente relacionados aos desastres naturais.
  
#### Glossário de Impactos em Desastres

| Conceito                   | Descrição                                                                                               |
| :------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Óbitos** | Número de pessoas que **morreram** em decorrência do evento.                                            |
| **Feridos** | Pessoas que sofreram **lesões físicas** e necessitam de atendimento médico.                             |
| **Enfermos** | Indivíduos que desenvolveram **doenças** ou tiveram sua saúde agravada por causa do evento.             |
| **Desabrigados** | Pessoas que **perderam suas casas** e não têm onde morar, precisando de abrigo temporário.              |
| **Desalojados** | Indivíduos que foram **forçados a sair de suas casas temporariamente**, mas podem retornar ou se abrigaram em casas de parentes/amigos. |
| **Desaparecidos** | Pessoas cujo **paradeiro é desconhecido** após o evento e há preocupação com sua segurança ou vida.     |
| **Residências Danificadas**| Casas que sofreram **algum tipo de estrago** estrutural ou material, mas podem ser reparadas.            |
| **Residências Destruídas** | Casas que foram **completamente arrasadas** ou danificadas de forma irreparável.                        |
| **Dano Patrimônio Público**| Prejuízos causados a **bens e infraestruturas de propriedade do governo** (escolas, hospitais, estradas, etc.). |
  
## ➡️ ARQUITETURA DO PROGRAMA

O sistema é construído em Python e utiliza diversas bibliotecas para diferentes funcionalidades:

* Streamlit: Para a criação da interface de usuário interativa.
* Streamlit_autorefresh: 
* Pandas: Para manipulação e análise de dados tabulares.
* NumPy: Para operações numéricas.
* Scikit-learn (sklearn): Para implementação de modelos de machine learning (Regressão Linear, SVR, Random Forest, Gradient Boosting), divisão de dados, otimização de hiperparâmetros (GridSearchCV) e métricas de avaliação (mean_squared_error).
* OS: Para interação com o sistema operacional (criação de diretórios, verificação de arquivos).
* Requests: Para realizar requisições HTTP para obter dados de uma API Oracle.
* Datetime: Para manipulação de datas e horas.
* Matplotlib e Plotly: Para criação de visualizações de dados.
* Locale: Para formatação de números e datas de acordo com a localidade (português do Brasil).
* IO (BytesIO): Para trabalhar com dados binários em memória.
* Joblib: 

Resumo geral da arquitetura do programa:

| Arquivo/Pasta      | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app.py`           | **Interface de Usuário:** interface interativa (via Streamlit) que permite aos usuários visualizar as previsões, análises e o status geral do sistema. É o ponto de interação visual com as informações geradas pelos modelos e dados coletados.                                                                                                                                                                                                                                                                                                                                                      |
| `main.py`          | **Lógica do ESP32 e Integração com Banco de Dados:** Script principal para a execução da lógica de comunicação com o ESP 32. Sua função central é coletar dados desses dispositivos e integrá-los ao banco de dados Oracle via chamadas de API, atuando como o ponto de entrada para a ingestão de dados brutos do hardware.                                                                                                                                                                                                                                                                            |
| `oracle.sql`       | **Scripts de Banco de Dados:** Contém os comandos SQL necessários para a criação das tabelas no banco de dados Oracle, especificamente para armazenar dados de nível de água e volume de chuva.                                                                                                                                                                                                                                         |
| `requirements.txt` | **Gerenciamento de Dependências:** Lista as bibliotecas Python de terceiros e suas respectivas versões das quais o projeto depende.                                                                                                                                                                                                                    |
| `treinar_modelos.py` | **Treinamento de Modelos de ML:** Script dedicado ao ciclo de vida dos modelos preditivos. É responsável por carregar os datasets brutos, realizar o pré-processamento de dados, treinar os modelos de machine learning para previsão de chuva e nível esperado, serializá-los e salvá-los no formato `.joblib`.                                                                                                                                                                                                                                                                                 |
| `utils.py`         | **Utilitário e Lógica de Negócio Central:** Contém funções auxiliares e a lógica de negócio crítica do sistema. Inclui as chamadas às APIs de terceiros (Oracle Cloud para dados de sensores e AWS Lambda para alertas SMS), incorpora a lógica de avaliação de risco de enchente (realizando cálculos e classificações), interage com o banco de dados Oracle para salvar leituras adicionais de sensores e garante o disparo automático de alertas SMS quando as condições de risco atingem limiares predefinidos. |


## SISTEMA DE ALERTA (AWS)

![alertaaws](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/alertaaws.JPG)

A arquitetura do sistema é composta por diversas camadas interconectadas, garantindo a coleta, processamento, análise e disseminação das informações:

Um dispositivo ESP32 é responsável pela coleta de dados ambientais, como temperatura (Temp), umidade (Humid), nível do rio (RioLevel) e nível da chuva (Chuva).

Os dados coletados são enviados para uma API de dados Oracle, onde são armazenados e ficam disponíveis para consumo.

Um display local no ESP32 mostra as leituras em tempo real, indicando a temperatura, umidade, nível do rio e o nível da chuva.

Um módulo central de Monitoramento dos Níveis do Rio e da Chuva acessa os dados da API Oracle.

Os dados de nível atual (do rio e/ou da chuva) são enviados para um Aplicativo Streamlit com Inteligência Artificial.

Para a geração de alertas proativos, a arquitetura se integra com serviços da Amazon Web Services (AWS):

    Amazon API Gateway: Atua como um ponto de entrada seguro e escalável para as requisições que acionam o processo de alerta.
    
    AWS Lambda: Funções serverless que são acionadas via API Gateway para processar os dados de monitoramento e aplicar a lógica de negócio para determinar se um alerta deve ser enviado.
    
    Amazon SNS (Simple Notification Service): Uma vez que a função Lambda decide que um alerta é necessário, o SNS é utilizado para enviar notificações para os assinantes.

O Amazon SNS envia as notificações de alerta diretamente para os usuários via SMS.

A mensagem de alerta inclui informações cruciais como:

    ALERTA ENCHENTE SÃO PAULO: Indicação clara do tipo de evento.
    
    Risco GRAVE: Classificação do risco.
    
    Nível atual: O nível atual do rio.
    
    Previsão: A quantidade de chuva prevista e o nível de rio esperado.
    
    Data e Hora: O momento em que o alerta foi emitido.


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

* 1.0.0 - 03/06/2025
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
