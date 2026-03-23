
# Portfólio de Extração e Preparação de Dados (Exemplo)

**Aluno:** [Nome do Aluno]
**Curso:** Ciência de Dados & IA | IBEMEC
**Semestre:** 2026.1
**Disciplina:** Extração e Preparação de Dados (IBM8915)

---

## 📋 Sobre Este Repositório
Este repositório contém o conjunto de entregas práticas desenvolvidas ao longo da disciplina. O objetivo é demonstrar competências em todo o ciclo de vida da engenharia de dados, desde a extração bruta até a orquestração de pipelines automatizados.

## 🗂️ Índice de Projetos

### 🔹 Módulo 1: Extração e Análise Exploratória (Raw Data)
Foco na obtenção de dados de diversas fontes e compreensão inicial do dataset.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 01** | [Extração de Arquivos Planos (CSV/Excel)](./notebooks/lab_01_flat_files.ipynb) | Uso de `pandas` para leitura de múltiplos formatos, tratamento de encoding e separadores. |
| **Lab 02** | [Extração via SQL (Banco Relacional)](./notebooks/lab_02_sql_extraction.ipynb) | Conexão com banco de dados via `SQLAlchemy`, execução de queries para join de tabelas. |
| **Lab 03** | [Análise Exploratória Inicial (EDA)](./notebooks/lab_03_eda_basics.ipynb) | Estatística descritiva, identificação de tipos de variáveis e histogramas. |
| **Doc** | [Dicionário de Dados](./docs/data_dictionary.md) | Documentação técnica dos metadados e schema do dataset. |

### 🔹 Módulo 2: Limpeza e Tratamento de Dados (Data Cleaning)
Técnicas para transformar dados sujos em dados confiáveis.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 04** | [Visualização de Dados Ausentes](./notebooks/lab_04_missing_values_viz.ipynb) | Identificação de padrões de nulidade (MCAR/MAR) com `missingno`. |
| **Lab 05** | [Imputação de Dados](./notebooks/lab_05_imputation.ipynb) | Estratégias de preenchimento: média, mediana vs. KNN Imputer e Iterative Imputer. |
| **Lab 06** | [Tratamento de Cardinalidade](./notebooks/lab_06_cardinality.ipynb) | Redução de dimensionalidade agrupando categorias raras ("Other"). |
| **Lab 10** | [Detecção de Outliers](./notebooks/lab_10_outliers.ipynb) | Aplicação de Z-Score, IQR e Isolation Forest para limpeza de ruídos. |
| **Lab 11** | [Datas e Séries Temporais](./notebooks/lab_11_datetime.ipynb) | Parsing de datas, extração de features cíclicas e lags. |

### 🔹 Módulo 3: Engenharia de Atributos (Feature Engineering)
Criação de novas variáveis para potencializar modelos de ML.

| Lab | Atividade | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 07** | [Encoders Categóricos](./notebooks/lab_07_encoders.ipynb) | One-Hot Encoding, Label Encoding, Target Encoding. |
| **Lab 08** | [Criação de Features](./notebooks/lab_08_feature_engineering.ipynb) | Criação de interações polinomiais e ratios de negócio. |
| **Lab 09** | [Discretização (Binning)](./notebooks/lab_09_binning.ipynb) | Transformação de variáveis contínuas em faixas (bins). |
| **Lab 12** | [Escalonamento (Scaling)](./notebooks/lab_12_scaling.ipynb) | Normalização (Min-Max) e Padronização (StandardScaler). |
| **Lab 14** | [Dados Desbalanceados](./notebooks/lab_14_imbalanced.ipynb) | Técnicas de SMOTE e Random Undersampling. |
| **Lab 15** | [Seleção de Variáveis](./notebooks/lab_15_feature_selection.ipynb) | Filter methods e Lasso/RFE para seleção de features. |

### 🔹 Módulo 4: Pipelines e Orquestração (Production Ready)
Automatização e profissionalização do fluxo de dados.

| Atividade | Arquivo | Competências Demonstradas |
| :--- | :--- | :--- |
| **Lab 13** | [Scikit-Learn Pipelines](./notebooks/lab_13_pipelines_intro.ipynb) | Encapsulamento de pré-processamento para evitar data leakage. |
| **Custom** | [Transformadores Customizados](./src/custom_transformers.py) | Criação de classes Python compatíveis com pipelines do Sklearn. |
| **Airflow** | [DAG de Orquestração](./dags/airflow_dag_pipeline.py) | **Orquestração completa**: Extração -> Validação -> Limpeza -> Carga, agendada no Apache Airflow. |

---

## 🚀 Projeto Final: [Título do Projeto]
> **Nota:** Este projeto integra todos os conceitos acima em um cenário real.

*   **Descrição:** Pipeline de dados para previsão de [Exemplo: Churn de Clientes / Preço de Imóveis].
*   **Link:** [Acessar Notebook do Projeto Final](./project/final_project_analysis.ipynb)
*   **Slides:** [Apresentação em PDF](./project/slides_presentation.pdf)

---

## 🛠️ Tecnologias Utilizadas
*   Python 3.10+
*   Pandas / Numpy
*   Scikit-Learn
*   Apache Airflow
*   SQLAlchemy
*   Matplotlib / Seaborn
