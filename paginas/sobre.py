import streamlit as st
import webbrowser 

def pagina_inicial():


    st.header('Sobre', divider=True)

    st.sidebar.markdown("**Informações de contato.**")

    st.sidebar.image("image/in.png", width=30)

    st.sidebar.link_button("linkedin.",
               "www.linkedin.com/in/leandro-souza-313136190")

    st.sidebar.image("image/wh.png", width=30)
    st.sidebar.link_button("Whatsapp.",
                       "https://wa.me/19994138086")




    st.markdown(
        """ 
        Tenho experiência em criar soluções inovadoras que transformam processos logísticos e análises de dados. Na Mobly, desenvolvi ideias que otimizaram processos de inventário e controle de estoque. Na Indecx, fui responsável pela criação de relatórios e análises detalhadas baseadas em dados mercadológicos de veículos comerciais e leves para empresas como Localiza, Mercedes-Benz, Movida, Unidas, LM Transportes, VW, BYD e Addiante, além de desenvolver métricas de NPS e CSAT para o Tribanco.

        Atualmente, trabalho na Hagens, onde sou responsável pela coleta, análise e geração de insights por meio de relatórios utilizando Power BI, com foco no Grupo Zelo. Minha trajetória profissional inclui a implementação de soluções logísticas eficientes e a transformação de dados complexos em insights acionáveis, impulsionando a eficiência operacional.

        Possuo também conhecimento em Python, com habilidades em técnicas CRUD para gestão e manipulação de dados, além de experiência na criação de bots de automação para otimizar diversos processos.""")

