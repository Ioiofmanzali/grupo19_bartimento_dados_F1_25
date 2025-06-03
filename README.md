# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# PROJETO - GLOBAL SOLUTION 2  

![capa](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/enchente1.JPG)

## Grupo 8

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

## :page_with_curl:DOCUMENTAÇÃO

Documentação Técnica do Projeto "GLOBAL SOLUTION - 2o SEMESTRE"

![Versão 1.0.0](https://img.shields.io/badge/Vers%C3%A3o%201.0.0-gray?style=flat) 

Autores: Amanda Fragnan, Iolanda Manzali, Jonatas Gomes, Murilo Nasser, Pedro Sousa 

## 🔍 SOBRE O PROJETO

A cidade de São Paulo enfrenta, ano após ano, o desafio crescente das enchentes, alagamentos, chuvas intensas e enxurradas. Fenômenos como esses têm se tornado cada vez mais frequentes e severos, impactando diretamente a vida dos moradores, a mobilidade urbana e a infraestrutura da capital. Em 2025, por exemplo, episódios de chuva forte colocaram praticamente todas as regiões da cidade em estado de atenção, com registros de ruas e avenidas alagadas, bairros como Santo Amaro e Piraporinha submersos, quedas de árvores e milhares de imóveis sem energia elétrica.

A topografia acidentada, a impermeabilização do solo e o crescimento acelerado da cidade agravam o risco de transbordamento de rios e córregos, além de potencializar o impacto das enxurradas e enchentes. Mesmo com investimentos em drenagem, monitoramento e sistemas de alerta, São Paulo segue vulnerável a eventos extremos, que causam prejuízos materiais, perdas humanas e demandam respostas rápidas do poder público.

Diante desse cenário, torna-se fundamental investir em soluções digitais inovadoras, capazes de prever, monitorar e mitigar os impactos desses desastres. A análise de dados reais, o uso de inteligência artificial e o cruzamento de informações meteorológicas e ambientais permitem antecipar riscos, emitir alertas e orientar ações preventivas, contribuindo para uma cidade mais resiliente e segura para todos.

A aplicação foi desenvolvida para monitoramento de eventos e emissão de alertas para desastre hidrológicos (chuvas intensas, enxurradasm alagamentos e inundações) enviados via SMS (API AWS SNS) somente somente para Gestores Públicos, Defesa Civil, Corpo de Bombeiros e entidades emnvolvidas com a gestão de desastres naturais. Por isso optamos por deixar a aplicação principal somente com as informações necessárias para o nosso objetivo, que é criar uma aplicação com interface em Streamlit, amigável e que permita a visualização dos dados de nvel do rio e chuvas e dispare um alerta via SMS para os números de telefone cadastrados.

Para fins acadêmicos os arquivos relacionados a análise exploratória, treinamento de ML e DL, ESP32 estão disponíveis no GitHub, porem não são visualizados na aplicação principal do Streamlit.
    
### ❗ PRÉ-REQUISITOS 

* Ambiente de desenvolvimento compatível com Python, como VSCode ou PyCharm.

* Versão do Python superior a 3.9 instalado no seu sistema operacional (Windows, macOS ou Linux). Recomendamos a versão mais recente estável.

* Streamlit instalado (via pip)

* Versão do Oracle SQL developer superior a 12c

* Internet para download das bibliotecas e dependências

Maiores informações sobre a instalação e uso dessas linguagens de Programação pode ser obtida nos sites oficiais:

1. Python: https://www.python.org/

2. Streamlit: https://docs.streamlit.io/get-started

3. Oracle: https://www.oracle.com.br

4. APEX Oracle: https://apex.oracle.com/pt-br/


## 🛠️ TECNOLOGIAS UTILIZADAS

![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) &nbsp; ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) &nbsp; ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=Oracle&logoColor=white) ![Oracle APEX](https://img.shields.io/badge/Oracle%20APEX-green?style=for-the-badge&logo=oracle&logoColor=white)

### 1. ORACLE

* Esse projeto utiliza duas funcionalidades Oeacle:
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
  - except requests.exceptions.RequestException as e:: Captura qualquer erro relacionado à requisição HTTP (problemas de rede, timeout, erros de status HTTP capturados por raise_for_status()).
  - except ValueError:: Captura erros que ocorrem se a resposta da API não for um JSON válido ou se houver problemas na sua decodificação.

  Em ambos os casos de erro, uma mensagem é exibida usando st.error (a aplicação é construída com Streamlit para exibir esses erros na interface do usuário) e a função retorna None, sinalizando que a operação de busca falhou.

### 2. PYTHON

* Atua como a linguagem principal para definir a arquitetura da aplicação web, organizando o conteúdo através de botões de navegação no menu principal.

** maiores detalhes na seção Arquitetura do Programa

### 3. STREAMLIT

A interface do usuário é organizada em uma única página principal.

![pagina_inicial](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/app_pp.JPG)


A interface mostra os níveis atual, esperado e previsto do rio e a classificação do risco de enchente.

Na aba lateral, podemos determinar o nivel de agua (grave e moderado) e tambem simular situações com valores atribuidos de nivel do rio e chuvas. 

## DATASETS

### INMET

Os datasets IMNET foram processados conforme o descrito a seguir:
  - Preenchimento de valores ausentes: a maioria dos valores ausentes do dataset INMET está na coluna de radiacao global, que nao foi utilizada para esse projeto. Para os campos precipitacao_total não foram encontrados valores ausentes ou duplicados.

### S2iD (Sistema Integrado de Informações sobre Desastres)

O dataset  S2iD foi processado condorme o descrito a seguir:

  - feito o download da série histórica. Foram filtrados somente os desastres do tipo hidrológico (enxurradas, alagamentos, chuvas intensas, movimento de massa e inundações) para a cidade de São Paulo.
    
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

## Componentes da Arquitetura do Projeto `GS2_OFICIAL`

| Arquivo/Pasta      | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app.py`           | **Interface de Usuário:** interface interativa (via Streamlit) que permite aos usuários visualizar as previsões, análises e o status geral do sistema. É o ponto de interação visual com as informações geradas pelos modelos e dados coletados.                                                                                                                                                                                                                                                                                                                                                      |
| `main.py`          | **Lógica do ESP32 e Integração com Banco de Dados:** Script principal para a execução da lógica de comunicação com o ESP 32. Sua função central é coletar dados desses dispositivos e integrá-los ao banco de dados Oracle via chamadas de API, atuando como o ponto de entrada para a ingestão de dados brutos do hardware.                                                                                                                                                                                                                                                                            |
| `oracle.sql`       | **Scripts de Banco de Dados:** Contém os comandos SQL necessários para a criação das tabelas no banco de dados Oracle, especificamente para armazenar dados de nível de água e volume de chuva.                                                                                                                                                                                                                                         |
| `requirements.txt` | **Gerenciamento de Dependências:** Lista as bibliotecas Python de terceiros e suas respectivas versões das quais o projeto depende.                                                                                                                                                                                                                    |
| `treinar_modelos.py` | **Treinamento de Modelos de ML:** Script dedicado ao ciclo de vida dos modelos preditivos. É responsável por carregar os datasets brutos, realizar o pré-processamento de dados, treinar os modelos de machine learning para previsão de chuva e nível esperado, serializá-los e salvá-los no formato `.joblib`.                                                                                                                                                                                                                                                                                 |
| `utils.py`         | **Utilitário e Lógica de Negócio Central:** Contém funções auxiliares e a lógica de negócio crítica do sistema. Inclui as chamadas às APIs de terceiros (Oracle Cloud para dados de sensores e AWS Lambda para alertas SMS), incorpora a lógica de avaliação de risco de enchente (realizando cálculos e classificações), interage com o banco de dados Oracle para salvar leituras adicionais de sensores e garante o disparo automático de alertas SMS quando as condições de risco atingem limiares predefinidos. |

## 📊 ANÁLISE EXPLORATÓRIA DOS DADOS

falta fazer

## 📈 TREINAMENTO E ESCOLHA DO MELHOR MODELO DE ML

O projeto utiliza os modelos com o objetivo de encontrar a combinação que oferece o melhor desempenho de generalização para os dados, ou seja, que consegue fazer previsões precisas em dados não vistos durante o treinamento de regressão supervisionada para prever a produtividade agrícola. 

Os modelos implementados são:

![modelos](https://github.com/Ioiofmanzali/Sprint3_FIAP_Grupo09/blob/main/assets/modelos.JPG)

Método selecionado para selecionar o 'melhor modelo' com os 'melhores hiperparâmetros': GridSearchCV

Métrica utilizada para seleção do modelo: RMSE

Os dados sao utilizados para treinamento em um ou mais modelos selecionados pelo usuário, seus resultados são comparados e o "melhor modelo" com os "melhores parâmetros" é selecionado com base no menor RMSE, apos otimização dos hiperparâmetros utilizando o GridSearchCV.


## ESP 32 COM SENSORES

**Este projeto não requer hardware físico. Todos os componentes são virtuais e configurados dentro do ambiente de simulação Wokwi.**

Será descrita a seguir a estruturação do código, funcionalidade implementadas, dependências de hardware e software, além dos parâmetros de configuração.

![image](https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/esp32.JPG)


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

[link wokwi]( https://wokwi.com/projects/432676821844364289)

Obs: Para simular um ambiente node sensores captam os dados do ambiente foi utilizado no código sketch.ino uma funcionalidade para gerar dados aleatórios

<p align="center">
  <img src="URL_DA_SUA_IMAGEM_1.png" alt="Descrição da Imagem 1" width="48%">
  <img src="https://github.com/Ioiofmanzali/GLOBAL_SOLUTION_2_-GRUPO81TIAO/blob/main/assets/dadosfake1.JPG)" alt="Descrição da Imagem 2" width="48%">
</p>       



## 🔗 LINKS IMPORTANTES

[IBGE](https://sidra.ibge.gov.br/tabela/839)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[INMET](https://portal.inmet.gov.br/dadoshistoricos)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CONAB](https://www.conab.gov.br/info-agro/custos-de-producao/planilhas-de-custo-de-producao/item/16269-serie-historica-custos-milho-2-safra-2005-a-2021)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SATVEG](&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)



## 📣 PRÓXIMOS PASSOS

Este é um projeto em evolução. Na sua versão 1.0.0 foi selecionada a cultura de milho da cidade de  Sorriso, localizada no estado do Mato Grosso.

Para a versão 2.0.0, expandimos o escopo para incluir outras culturas e municípios do território nacional.

O programa foi construido para ser escalável e para novas versões esperamos acrescentar dados relacionados a tipo de clima e solo, a partir de coordenadas geográficas.
            

## :octocat: CONTRIBUIÇÕES AO PROJETO

Ficamos muito felizes com a sua contribuição e valorizamos cada sugestão e esforço dedicado a aprimorá-lo.

Como Contribuir: 

* Clique no botão "Fork" no canto superior direito desta página para criar uma cópia do repositório na sua conta do GitHub.

* Clone o repositório forkado para o seu ambiente de desenvolvimento local.

* Crie uma branch separada para a sua contribuição, desenvolva suas modificações e realize os commits necessários na sua branch.

* Quando suas alterações estiverem prontas, envie um Pull Request do seu fork para a branch main deste repositório.

Seu Pull Request será revisado pela equipe e, se tudo estiver correto, será aceito e suas contribuições serão integradas ao projeto 😃!

## COMO RODAR O PROGRAMA A PARTIR DO VSCODE

1. Abrir o Terminal no VS Code
     No menu superior, clique em Terminal e depois em Novo Terminal ou utilize o atalho "CTRL J". Isso abrirá um painel de terminal na parte inferior da janela do VS Code.
     
2. No terminal digite os comandos cd e run para abrir o arquico e, em seguida, o navegador onde o aplicativo será aberto:
 
 ** após executar o comando streamlit run app.py, o Streamlit irá iniciar um servidor local e abrir automaticamente o seu aplicativo em uma nova aba do seu navegador web padrão.
 
 ** também aparecerá no terminal o endereço local onde o aplicativo está rodando (pode copiar e colar esse endereço no seu navegador, caso ele não abra automaticamente).



## 📁 Estrutura de pastas

- <b>assets</b>: imagens utilizadas no projeto e documentação
  
- <b>src</b>: códigos principais do programa
  
- <b>README.md</b>: guia e explicação geral sobre o projeto

## 🗃 Histórico de lançamentos

* 2.0.0 - 26/05/2025
* 1.0.0 - 18/04/2025
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
