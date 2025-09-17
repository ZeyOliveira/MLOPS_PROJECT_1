[![author](https://img.shields.io/badge/Zeygler&nbsp;Oliveira-red.svg)](https://www.linkedin.com/in/zeygler-oliveira-a021a92a4/)
[![](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

# Previsão de Cancelamento de Reservas Hoteleiras: Um Projeto MLOps End-to-End

Este repositório é o resultado de uma jornada completa, desde a coleta de dados até a implantação de um modelo em produção, tudo orquestrado com as melhores práticas de Machine Learning Operations (MLOps).

Meu objetivo aqui é mostrar como transformei um problema de negócio real em uma solução robusta e escalável, utilizando um pipeline de ML completo.

## O Problema e a Solução

Imagine um hotel que não consegue prever quais reservas serão canceladas. Isso gera quartos vazios inesperados, perda de receita e dificuldade no planejamento. Meu projeto visa resolver exatamente isso:

**O Desafio:** Prever se um cliente irá honrar sua reserva ou cancelar.

**A Solução:** Um modelo de Machine Learning preditivo, integrado em um pipeline MLOps, que permite ao hotel tomar decisões proativas, otimizar a ocupação e maximizar a receita.

## A Jornada do Projeto: Workflow MLOps

Este projeto foi construído seguindo um workflow MLOps detalhado, garantindo que cada etapa do ciclo de vida do modelo fosse gerenciada de forma eficiente e automatizada. Aqui está um resumo dessa jornada, passo a passo:

### 1. **Database Setup (Configuração do Banco de Dados)**
*   **O que foi feito:** Preparamos o ambiente para armazenar nossos dados de reserva.
*   **Por que é importante:** Um banco de dados bem estruturado é a base para qualquer projeto de dados, garantindo que as informações estejam organizadas e acessíveis.
*   **Ferramenta:** **Google Cloud**, mais especificamente o uso de Buckets.

### 2. 🚀 **Project Setup (Configuração do Projeto)**
*   **O que foi feito:** Estruturamos o ambiente de desenvolvimento, definindo dependências e a organização do código.
*   **Por que é importante:** Garante que o projeto seja replicável, fácil de manter e que todos os colaboradores possam rodar sem problemas.
*   **Ferramentas/Conceitos:** Python, `venv` (ambiente virtual), `requirements.txt` (gerenciamento de dependências), `setup.py` (empacotamento do projeto).

### 3. 📥 **Data Ingestion (Ingestão de Dados)**
*   **O que foi feito:** Desenvolvemos scripts para coletar e carregar os dados brutos das reservas.
*   **Por que é importante:** É o primeiro contato com os dados! Garantir que a ingestão seja limpa e eficiente é crucial para a qualidade de todo o pipeline.
*   **Habilidades em jogo:** Scripting em Python, manipulação de dados.

### **Data Processing (Processamento de Dados)**
*   **O que foi feito:** Limpamos, transformamos e preparamos os dados brutos para o treinamento do modelo. Isso inclui tratamento de valores ausentes, engenharia de features e codificação de variáveis.
*   **Por que é importante:** Dados de qualidade são importantes para o modelo.
*   **Habilidades em jogo:** Python (Pandas, NumPy), pré-processamento de dados, engenharia de features.

### **Model Training (Treinamento do Modelo)**
*   **O que foi feito:** Selecionamos e treinamos o modelo de Machine Learning para prever o status da reserva.
*   **Por que é importante:** Aqui é onde a mágica acontece! O modelo aprende padrões nos dados para fazer previsões precisas.
*   **Habilidades em jogo:** Machine Learning (Scikit-learn, etc.), avaliação de modelos, otimização de hiperparâmetros.

### 6. 🧪 **Jupyter Notebook Testing (Testes em Jupyter Notebook)**
*   **O que fizemos:** Utilizamos Jupyter Notebooks para explorar os dados (EDA), prototipar modelos e testar ideias rapidamente.
*   **Por que é importante:** É o nosso laboratório! Permite experimentação ágil e documentação interativa do processo de desenvolvimento.
*   **Ferramentas/Conceitos:** Jupyter Notebook (`notebook` folder), **Análise Exploratória de Dados (EDA)**.

### 7. 📊 **Experiment Tracking (Rastreamento de Experimentos)**
*   **O que fizemos:** Registramos e comparamos diferentes experimentos de treinamento de modelos, incluindo métricas, parâmetros e artefatos.
*   **Por que é importante:** Essencial para a reprodutibilidade e para saber qual modelo performou melhor e por quê. Sem isso, é fácil se perder em um mar de experimentos!
*   **Ferramentas/Conceitos:** **MLflow** (`mlruns`, `mlartifacts` folders) – uma ferramenta fantástica para gerenciar o ciclo de vida do ML.

### 8. ⚙️ **Training Pipeline (Pipeline de Treinamento)**
*   **O que fizemos:** Automatizamos todo o processo de treinamento do modelo, desde a ingestão até o registro do modelo.
*   **Por que é importante:** Garante que o modelo possa ser retreinado de forma consistente e automática com novos dados, mantendo sua relevância ao longo do tempo.
*   **Habilidades em jogo:** Orquestração de pipelines, scripting Python (`pipeline` folder).

### 9. ��️ **Data Versioning (Versionamento de Dados)**
*   **O que fizemos:** Implementamos um sistema para versionar os datasets utilizados no treinamento.
*   **Por que é importante:** Tão importante quanto versionar o código! Garante que possamos reproduzir resultados e entender como as mudanças nos dados afetam o modelo.
*   **Ferramentas/Conceitos:** Git (para metadados), DVC (Data Version Control - comum em MLOps).

### 10. 🚀 **CI-CD Deployment (Implantação Contínua e Entrega Contínua)**
*   **O que fizemos:** Criamos um pipeline de CI/CD para automatizar a construção, teste e implantação do modelo e da aplicação.
*   **Por que é importante:** Leva o modelo do laboratório para o mundo real! Garante que novas versões do modelo ou da aplicação sejam entregues de forma rápida e segura.
*   **Ferramentas/Conceitos:** **Jenkins** (`Jenkinsfile`, `custom_jenkins` folder), **Docker** (`Dockerfile`), **Google Cloud** (para implantação e gerenciamento de recursos).

### 11. �� **User App Building (Construção da Aplicação do Usuário)**
*   **O que fizemos:** Desenvolvemos uma interface simples para que os usuários possam interagir com o modelo e obter previsões.
*   **Por que é importante:** O modelo só tem valor se puder ser usado! Uma aplicação amigável torna a inteligência artificial acessível.
*   **Ferramentas/Conceitos:** Python (Flask/Streamlit/Dash), desenvolvimento web (`application.py`, `static`, `templates` folders).

### 12. 📜 **Code Versioning (Versionamento de Código)**
*   **O que fizemos:** Gerenciamos todas as alterações de código usando Git.
*   **Por que é importante:** Colaboração, rastreabilidade e a capacidade de reverter para versões anteriores são fundamentais em qualquer projeto de software.
*   **Ferramentas/Conceitos:** **Git** (`.gitignore`), GitHub.

## 🛠️ Tecnologias e Habilidades em Destaque

Este projeto me permitiu aprofundar e demonstrar minhas habilidades em diversas áreas:

*   **Linguagens de Programação:** Python (avançado), SQL (minha base forte!).
*   **Bibliotecas de Data Science:** Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib.
*   **MLOps:** MLflow (rastreamento de experimentos e registro de modelos), Docker (containerização), Jenkins (CI/CD).
*   **Cloud:** Experiência com **Google Cloud Platform** (implantação e gerenciamento de recursos).
*   **Desenvolvimento Web:** Flask (para a aplicação de usuário).
*   **Versionamento:** Git e GitHub.
*   **Visualização de Dados:** Além das bibliotecas Python, tenho experiência com **Power BI** e **Excel** para dashboards e análises de negócio.

## 🚀 Como Ver o Projeto em Ação

Para um entrevistador, sei que ver é crer! Estou preparando demonstrações visuais e textuais para ilustrar o funcionamento deste pipeline:

*   **Gravações de Tela:** Em breve, adicionarei vídeos curtos mostrando o pipeline de CI/CD em ação no Jenkins, a interface da aplicação e o rastreamento de experimentos no MLflow.
*   **Screenshots:** Capturas de tela do Google Cloud Console (em português, claro!), do MLflow UI e da aplicação, sempre com cuidado para não vazar informações pessoais.
*   **Instruções de Execução:** Detalhes sobre como configurar o ambiente e rodar o projeto localmente (ou acessar a versão deployada, se aplicável).

## 💡 Próximos Passos e Melhorias Futuras

A jornada de um projeto de MLOps nunca termina! Algumas ideias para o futuro incluem:

*   Implementar monitoramento de modelo em produção (drift, performance).
*   Explorar outras ferramentas de orquestração (Airflow, Kubeflow).
*   Aprimorar a interface do usuário com mais funcionalidades.
*   Testar modelos mais avançados (Deep Learning, ensembles).

---

Espero que este `README.md` te dê uma visão clara e empolgante do meu trabalho e das minhas capacidades como estudante de Ciência de Dados buscando uma oportunidade na área de TI. Estou aberto a perguntas e ansioso para discutir mais sobre este projeto!

---

**Observações para você, Zeygler:**

*   **Preencha os detalhes:** Onde coloquei `[Link para o Dataset]` ou `[Detalhes sobre a implantação]`, você pode adicionar informações específicas.
*   **Crie os vídeos/screenshots:** A seção "Como Ver o Projeto em Ação" é crucial. Comece a planejar como você vai gerar esses materiais, lembrando de evitar informações pessoais.
*   **Adapte a linguagem:** Se sentir que "mais ou menos informal" precisa ser um pouco mais ou menos, ajuste! O importante é que soe como você.
*   **Seu nome:** Lembre-se de que o `README` é sobre *você*. Considere adicionar uma pequena seção "Sobre Mim" ou "Contato" no final, com seu nome e LinkedIn, por exemplo.

Este `README` não apenas descreve o projeto, mas também vende suas habilidades e sua paixão pela área! Boa sorte!
