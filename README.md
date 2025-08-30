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

Esse dataset pode ser acessado através dos links abaixo:

[[KAGGLE DVC](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset?select=cardio_train.csv)] 

[[GoogleDrive](https://drive.google.com/file/d/1Zj2PfvhN10cAB9Szs-Gg0pyQ7twgAKbe/view?usp=sharing)] 


## 📁 PARTE 2 - DATASETS TEXTUAIS

### 📊 Análise de Textos Médicos com NLP

Este repositório demonstra como **técnicas de Processamento de Linguagem Natural (NLP)** em artigos científicos sobre **doenças cardiovasculares** e fatores de risco associados podem ser explorados. O objetivo é extrair insights relevantes que apoiem projetos de **Inteligência Artificial em Saúde**, contribuindo para prevenção, diagnóstico e políticas públicas.

---

### 🗂️ Artigos Utilizados

1. **[Inflamação sistêmica causada pela periodontite crônica em pacientes vítimas de ataque cardíaco isquêmico agudo](https://github.com/Ioiofmanzali/grupo19_bartimento_dados_F1_25/blob/main/Ataque_Cardiaco.pdf)**  
   - Estuda a associação entre periodontite, inflamação sistêmica e risco de infarto.  
   - Contém dados clínicos: LDL, HDL, triglicerídeos, glicemia, e agentes biológicos como bactérias periodontais.

2. **[Associação entre saúde cardiovascular e depressão autorreferida: Pesquisa Nacional de Saúde 2019](https://github.com/Ioiofmanzali/grupo19_bartimento_dados_F1_25/blob/main/Depressao_Doencas_Cardiovasculares.pdf)**  
   - Explora a relação entre saúde mental (depressão) e indicadores de saúde cardiovascular: IMC, tabagismo, hipertensão e diabetes.  
   - Base populacional: 57.898 adultos brasileiros.


### ⚙️ Aplicações de NLP

#### 🔬 1. Extração de Entidades Médicas (NER)
- Identificação automática de **biomarcadores**: LDL, HDL, glicemia.  
- Reconhecimento de **agentes infecciosos**: *Porphyromonas gingivalis*, *Prevotella intermedia*.  
- Extração de **condições clínicas**: hipertensão, diabetes, depressão.  
- Mapeamento para terminologias padronizadas como **SNOMED-CT** e **UMLS**.

**💡 Benefício:** Permite estruturar informações clínicas de textos livres, facilitando integração com **bancos de dados de saúde** e **sistemas clínicos**.


#### 📑 2. Classificação de Tópicos
- **Artigo 1:** *doenças periodontais*, *inflamação sistêmica*, *cardiopatias isquêmicas*.  
- **Artigo 2:** *fatores biológicos*, *hábitos comportamentais*, *saúde mental*.

**💡 Benefício:** Organiza automaticamente a literatura científica, apoiando **pesquisadores** na identificação de conexões entre condições de saúde.

---

#### ❤️ 3. Mineração de Relações Causais
- Identificação de padrões como:  
  - *“Periodontite crônica → inflamação → risco de infarto”* (Artigo 1).  
  - *“Depressão → maior prevalência de doenças cardiovasculares”* (Artigo 2).

**💡 Benefício:** Fundamenta **modelos explicáveis de risco clínico**, essenciais para **IA interpretável em saúde**.

---

#### 🙂 4. Análise de Sentimentos e Autorrelatos
- Processamento de depoimentos de pacientes para detectar indícios de **tristeza, ansiedade ou risco de depressão**.  
- Classificação automática de relatos em **neutros**, **positivos** ou **depressivos**.

**💡 Benefício:** Suporta **triagem populacional** e programas de **atenção primária à saúde mental**.

---

#### 📊 5. Integração com Modelos Preditivos
- Dados extraídos dos textos podem alimentar **modelos de Machine Learning** para prever risco cardiovascular ou depressão.  
- Exemplo: pacientes com periodontite crônica grave + LDL elevado → maior probabilidade de infarto.

**💡 Benefício:** Viabiliza **sistemas de apoio à decisão clínica** e recomendações preventivas.


#### 🧠 Conclusão

A aplicação de NLP aos artigos selecionados evidencia como a **Inteligência Artificial pode transformar textos científicos em bases de conhecimento estruturadas**, permitindo:

- Diagnóstico precoce de doenças cardiovasculares e mentais.  
- Apoio à **formulação de políticas públicas** de saúde.  
- Integração da **saúde física e mental** do paciente.  
- Avanço científico com insights de alto valor clínico.  

## 📁 PARTE 3 - DADOS VISUAIS

Para esse projeto o dataset selecionado está relacionado a radiografias de tórax por diversas razões: 

 * A radiografia de tórax é uma ferramenta amplamente disponivel e de baixo custo para triagem e estratificação da doença cardíaca. Esses exames possivilitam uma visualização direta da silhueta cardíaca em relação à cavidade torácica. Isso permite a implementação de uma tarefa de VC clara e clinicamente relevante: a detecção de cardiomegalia (aumento do coração) através do cálculo da Relação Cardiotorácica (RCT). A RCT é uma métrica estabelecida que os radiologistas usam, tornando sua automação um exemplo exemplar de como os algoritmos de VC podem replicar e padronizar a análise diagnóstica. A tarefa envolve a segmentação de estruturas anatômicas (coração e tórax), extração de características (diâmetros máximos) e classificação baseada em regras (RCT > 0.5), que se alinham perfeitamente com os princípios básicos da visão computacional.
   
 * Grandes conjuntos de dados públicos e bem documentados, como o NIH ChestX-ray14 e o CheXpert de Stanford, estão prontamente disponíveis para uso em pesquisa acadêmica. Esses repositórios contêm dezenas a centenas de milhares de imagens, muitas já em formatos de imagem padrão como PNG ou JPG, eliminando a necessidade de conversão complexa de formatos.

### Link do Dataset Entregável

[Dataset no Google Drive](https://drive.google.com/drive/folders/1cY4-paZR1OyQm40j44xzDhXDnm8m5ENr?usp=sharing)

### Conteúdo do Dataset Entregável

*   Pasta imagens_rx: 200 imagens (100 imagens da feature cardiomegalia e 100 da feature sem cardiomegalia)
*   1 arquivo CSV contendo o rótulo da patologia em cada imagem

### Dataset Original Completo (Kaggle)

[NIH Chest X-rays Dataset](https://www.kaggle.com/datasets/nih-chest-xrays/data/data)

### Notebook Usado na Extração das Imagens

[FIAP_F1_25](https://www.kaggle.com/code/iolandahfmanzali/fiap-f1-25?scriptVersionId=257394881)

### Código Python Usado para Copiar as Imagens

```python
import pandas as pd
import os
import shutil
import zipfile
import glob

# --- Configuração ---
NUM_IMAGENS_POR_CLASSE = 200
TOTAL_IMAGENS = NUM_IMAGENS_POR_CLASSE * 2

# Define os nomes das pastas e arquivos de saída
PASTA_DE_SAIDA = f'/kaggle/working/imagens_selecionadas_{TOTAL_IMAGENS}'
NOME_ARQUIVO_CSV = f'metadata_{TOTAL_IMAGENS}_imagens_traduzido.csv'
NOME_ARQUIVO_ZIP = f'/kaggle/working/dataset_raiox_{TOTAL_IMAGENS}.zip'

# Caminhos dos dados dentro do ambiente Kaggle
ARQUIVO_METADADOS = '/kaggle/input/nih-chest-xrays/data/Data_Entry_2017.csv'
CAMINHO_PESQUISA_IMAGENS = '/kaggle/input/nih-chest-xrays/data/images_*/images/*.png'

# --- 1. Criar diretório de saída ---
if os.path.exists(PASTA_DE_SAIDA):
    shutil.rmtree(PASTA_DE_SAIDA) # Limpa a pasta se já existir
os.makedirs(PASTA_DE_SAIDA)

# --- 2. Carregar e filtrar metadados ---
df = pd.read_csv(ARQUIVO_METADADOS)

# Selecionar 200 imagens com o rótulo 'Cardiomegaly'
df_cardiomegaly = df[df['Finding Labels'] == 'Cardiomegaly'].head(NUM_IMAGENS_POR_CLASSE)

# Selecionar 200 imagens com o rótulo 'No Finding'
df_no_finding = df[df['Finding Labels'] == 'No Finding'].head(NUM_IMAGENS_POR_CLASSE)

# Combinar as duas seleções em um único DataFrame
df_selecionado = pd.concat([df_cardiomegaly, df_no_finding])

# --- 3. Traduzir os rótulos no DataFrame selecionado ---
translation_map = {
    'Cardiomegaly': 'Cardiomegalia',
    'No Finding': 'Nada Encontrado'
}
# Usamos.copy() para evitar o SettingWithCopyWarning
df_selecionado_traduzido = df_selecionado.copy()
df_selecionado_traduzido['Finding Labels'] = df_selecionado_traduzido['Finding Labels'].replace(translation_map)
print("Rótulos traduzidos com sucesso no DataFrame.")

# --- 4. Salvar o arquivo CSV com os dados traduzidos ---
caminho_csv_saida = os.path.join(PASTA_DE_SAIDA, NOME_ARQUIVO_CSV)
df_selecionado_traduzido.to_csv(caminho_csv_saida, index=False)
print(f"Arquivo CSV '{NOME_ARQUIVO_CSV}' criado com os metadados traduzidos.")

# --- 5. Mapear e copiar as imagens selecionadas ---
print("Mapeando todos os caminhos de imagem...")
mapa_de_imagens = {os.path.basename(p): p for p in glob.glob(CAMINHO_PESQUISA_IMAGENS)}
print(f"Mapeamento concluído. {len(mapa_de_imagens)} imagens encontradas no total.")

print(f"Copiando {len(df_selecionado)} imagens selecionadas...")
imagens_copiadas = 0
# Itera sobre o DataFrame original para garantir que os nomes dos arquivos correspondam
for nome_arquivo in df_selecionado['Image Index']:
    if nome_arquivo in mapa_de_imagens:
        caminho_origem = mapa_de_imagens[nome_arquivo]
        caminho_destino = os.path.join(PASTA_DE_SAIDA, nome_arquivo)
        shutil.copy(caminho_origem, caminho_destino)
        imagens_copiadas += 1
    else:
        print(f"Aviso: Imagem {nome_arquivo} não encontrada nos caminhos de pesquisa.")

print(f"Cópia concluída. Total de imagens na pasta de saída: {imagens_copiadas}")

# --- 6. Compactar a pasta (com imagens e CSV traduzido) para download ---
if imagens_copiadas > 0:
    shutil.make_archive(base_name=f'/kaggle/working/dataset_raiox_{TOTAL_IMAGENS}', 
                        format='zip', 
                        root_dir=PASTA_DE_SAIDA)
    print(f"\nArquivo zip '{os.path.basename(NOME_ARQUIVO_ZIP)}' criado com sucesso!")
    print("Você pode baixar este arquivo na seção 'Output' do seu Notebook Kaggle.")
else:
    print("\nNenhuma imagem foi copiada, o arquivo zip não foi criado.")
```
  

## 📣 PRÓXIMAS FASES



## :octocat: CONTRIBUIÇÕES AO PROJETO

Ficamos muito felizes com a sua contribuição e valorizamos cada sugestão e esforço dedicado a aprimorá-lo.

Como Contribuir: 

* Clique no botão "Fork" no canto superior direito desta página para criar uma cópia do repositório na sua conta do GitHub.

* Clone o repositório forkado para o seu ambiente de desenvolvimento local.

* Crie uma branch separada para a sua contribuição, desenvolva suas modificações e realize os commits necessários na sua branch.

* Quando suas alterações estiverem prontas, envie um Pull Request do seu fork para a branch main deste repositório.

Seu Pull Request será revisado pela equipe e, se tudo estiver correto, será aceito e suas contribuições serão integradas ao projeto 😃!


## 📁 ESTRUTURA DE PASTAS

- <b>assets</b>: imagens utilizadas no projeto e documentação

- <b>docs</b>: códigos auxiliares utilizadas no projeto
  
- <b>src</b>: códigos principais do programa
  
- <b>README.md</b>: guia e explicação geral sobre o projeto



## 🗃 HISTÓRICO DE LANÇAMENTOS

![Versão 1.0.0](https://img.shields.io/badge/Vers%C3%A3o%201.0.0-gray?style=flat)  - 03/09/2025
    

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
