import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_option_menu import option_menu
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi
from paginas.streamlit import streamlit
from paginas.chatbot import chatbot
from paginas.chatbot_huggingface import chatbot_huggingface
from paginas.certificados import certificados_skills
from paginas.machine_learnig import machine


st.set_page_config(
    page_title='Portfólio',
    page_icon= '⚡',
    layout='wide'
)

# --- Ocult menus ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)


authenticator.login()

if st.session_state["authentication_status"]:
    st.sidebar.title("Navegação")
    st.sidebar.write(f'Bem Vindo *{st.session_state["name"]}*')
    authenticator.logout("Logout", "sidebar")
    
    st.sidebar.divider()

        

    # if st.session_state["authentication_status"]: #  < - Antes
    #     authenticator.logout()
    #     st.sidebar.title("Navegação")
    #     st.sidebar.write(f'Bem Vindo *{st.session_state["name"]}*')
    #     paginas = st.sidebar.selectbox("Selecione a página", ["Sobre", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Projetos OpenAI", "Projetos huggingface"])
        
    
    # https://icons.getbootstrap.com/ - > icon
    with st.sidebar:
        paginas = option_menu(
        menu_title = "Menu",
        options = ["Sobre mim", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Projetos OpenAI", "Projetos Scikit-learn", "Projetos huggingface", "Certificados & Skills"],
        icons = ["envelope-at-fill", "bar-chart-fill", "graph-up-arrow", "robot", "cpu", "emoji-wink-fill", "award"],
        menu_icon ="cast",
        default_index = 0
        # orientation = "horizontal"  < - Agora
    )


    st.sidebar.divider()
    st.sidebar.markdown("Desenvolvido por [Leandro Souza](https://br.linkedin.com/in/leandro-souza-313136190)")


    if paginas == "Sobre mim":
        pagina_inicial()
    elif paginas == "Projetos em Power BI":
        bi()
    elif paginas == "Projetos em Streamlit & Plotly":
        streamlit()
    elif paginas == "Projetos OpenAI":
        chatbot()
    elif paginas == "Projetos huggingface":
        chatbot_huggingface()
    elif paginas == "Certificados & Skills":
        certificados_skills()
    elif paginas == "Projetos Scikit-learn":
        machine()


elif st.session_state["authentication_status"] is False:
    st.error('Usuário/Senha inválido')
elif st.session_state["authentication_status"] is None:
    st.warning('Por Favor, utilize seu usuário e senha!')


asssista = "https://www.youtube.com/watch?v=OF2TcvV_AsY"
