import streamlit as st
import webbrowser 

def pagina_inicial():

    st.header('Sobre', divider=True)

    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)

    # st.sidebar.link_button("linkedin.",
    #            "https://br.linkedin.com/in/leandro-souza-313136190")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")


    st.markdown(
        """ 
        Especialista em Análise de Dados e Soluções Logísticas.
        Tenho sólida experiência em transformar dados em insights estratégicos e criar soluções que otimizam processos logísticos e análises de dados. Na Mobly, desenvolvi e implementei melhorias nos processos de inventário e controle de estoque, resultando em maior eficiência operacional. Já na Indecx, criei relatórios detalhados e análises mercadológicas de veículos comerciais e leves para clientes como Localiza, Mercedes-Benz, Movida,Unidas, LM Transportes, VW, BYD, Addiante Locação e outros, além de estruturar métricas de NPS e CSAT para o Tribanco, impulsionando decisões baseadas em dados.

        Atualmente, atuo na Hagens, onde sou responsável pela coleta, análise e visualização de dados, utilizando ferramentas como Power BI e Looker, gerando insights acionáveis que suportam decisões estratégicas.

        Minhas habilidades incluem:

        * Ferramentas: Power BI, Looker, Power Query, Excel, Figma, GA4, BigQuery.
        * Linguagens de Programação: Python, SQL, DAX.
        * Python: Criação de bots de automação, técnicas CRUD para gestão e manipulação de dados, e criação de Web e Apps com Streamlit.
        * Análise de Dados: Desenvolvimento de dashboards e relatórios avançados.
        * Otimização de Processos: Implementação de soluções logísticas eficientes e automação de processos.
        
        Busco sempre criar soluções inovadoras e transformar dados em decisões estratégicas, contribuindo para o sucesso das organizações.""")
    
    st.divider()

    st.markdown("**Informações de contato.**")

    col1, col2 = st.columns(2)

    col1.image("image/in.png", width=40)
    col1.link_button("Acesse.",
               "https://br.linkedin.com/in/leandro-souza-313136190")

    col2.image("image/wh.png", width=40)
    col2.link_button("Acesse.",
                       "https://wa.me/19994138086")

