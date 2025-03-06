import streamlit as st

def certificados_skills():
    
    image_path_alura = "image/alura.png"
    image_path_google = "image/google_analytics.png"
    image_path_looker = "image/looker.png"
    image_asimov = "image/aprendendo_python_asimov.png"
    image_path_python = "image/python_programacao.png"
    image_figma = "image/figma.png"
    image_power_bi = "image/power_bi.png"
    image_banco_sql = "image/CG-85A6168D.png"
    image_algoritimos = "image/e6300370-de67-4e28-9ec3-2ac959ac7b01.png"
    
    st.header("Minhas Skills 🧠", divider=True)
    
    st.markdown("""
                Possuo um conjunto sólido de habilidades técnicas voltadas para **análise de dados**, **automação** e **inteligência artificial**. Minhas principais competências incluem:

                - 📊 **Análise de Dados:** Extração, limpeza e exploração de dados utilizando bibliotecas como **Pandas** e **NumPy**.
                
                - 🗃️ **Bancos de Dados SQL:** Construção de consultas avançadas para manipulação e análise de bancos de dados relacionais.
                
                - 🐍 **Python:** Desenvolvimento de scripts para **análise de dados**, **automação** de processos e integração de APIs.
                
                - ⚡ **Power Query:** Transformação e modelagem de dados de forma ágil, integrando diversas fontes.
                
                - 🤖 **Automação com Bots (CRUD):** Criação de bots em **Python** para automatizar operações **CRUD** (Create, Read, Update, Delete).
                
                - 📈 **Dashboards Interativos:** Desenvolvimento de visualizações dinâmicas e personalizadas com **Power BI**, **Looker**, **Streamlit** e **Plotly**.
                
                - 📚 **Treinamento de Modelos de IA:** Construção e avaliação de modelos de **machine learning** com **Scikit-learn** — incluindo treinamento supervisionado usando bases de treino e teste.
                
                - 🌐 **WebApps com Streamlit:** Desenvolvimento de aplicações web interativas e intuitivas para visualização de dados e modelos de IA.
                
                - 🧠 **Inteligência Artificial e IA Generativa:**  
                   * 🤖 Criação de agentes inteligentes e assistentes virtuais utilizando **ChatGPT**.  
                   * 🛠️ Desenvolvimento de bots de IA utilizando modelos gratuitos da **Hugging Face**.
                """)
    
    col_space, = st.columns(1)

    with col_space:
        st.markdown("<br><br><br>", unsafe_allow_html=True)

    
    
    st.header("Certificados 🎓", divider=True)
    
    
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.image(image_path_alura, caption="Alura - Engenharia de Prompt: criando prompts eficazes para IA Generativa", width=200)
        st.link_button("Acesse.",
                       "https://cursos.alura.com.br/certificate/2cd1add4-9363-4104-84eb-894fb7e26306")
        
    with col2:
        st.image(image_path_google, caption="Skillshop - Google Analytics", width=200)
        st.link_button("Acesse.",
                       "https://skillshop.credential.net/38864742-4bd5-4d11-98d7-fafcb97c28ce#gs.fv1ja0")
        
    with col3:
        st.image(image_path_looker, caption="Udemy - Looker Studio", width=200)
        st.link_button("Acesse.",
                       "https://www.udemy.com/certificate/UC-8df98845-d068-4947-b082-f5f646d1b285/")
        
    with col4:
        st.image(image_path_python, caption="Geek University - Programação em Python", width=200)
        st.link_button("Acesse.",
                       "https://geekuniversity.com.br/certificado/CG-8D73048E")
        

    col6,col7,col8,col9 = st.columns(4)
        
    with col6:
        st.image(image_figma, caption="Udemy - PRO FIGMA | UI DESIGN", width=200)
        st.link_button("Acesse.",
                       "https://www.udemy.com/certificate/UC-b2dabb56-4c83-4c5c-8466-bda8f0126106/")
        
    with col7:
        st.image(image_power_bi, caption="Data Science Acdademy - Microsoft Power BI Para Business Intelligence e Data Science ", width=200)
        st.link_button("Acesse.",
                       "https://mycourse.app/Rma6oxrux9t3RpTb7")
        
    with col8:
        st.image(image_banco_sql, caption="Geek University - Bancos de Dados SQL e NoSQL do básico ao avançado", width=200)
        st.link_button("Acesse.",
                       "https://www.geekuniversity.com.br/certificado/CG-85A6168D")
        
    with col9:
        st.image(image_algoritimos, caption="Geek University -  Algoritmos e Lógica de Programação", width=200)
        st.link_button("Acesse.",
                       "https://www.geekuniversity.com.br/certificado/CG-44C999E7")
    
    col10, = st.columns(1)
    
    with col10:
        st.image(image_asimov, caption="Trilha Asimov - Aprendendo Python", width=200)
        st.link_button("Acesse.",
                       "https://hub.asimov.academy/validar-certificado/642fdb32-42c9-11ef-92e4-42010a80001b")
