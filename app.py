import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi
from paginas.streamlit import streamlit
from paginas.chatbot import chatbot


st.set_page_config(
    page_title='Home',
    page_icon='📶',
    layout='wide'
)


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
    authenticator.logout()
    st.sidebar.title("Navegação")
    st.sidebar.write(f'Bem Vindo *{st.session_state["name"]}*')
    paginas = st.sidebar.selectbox("Selecione a página", ["Sobre", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Chat bot"])
    if paginas == "Sobre":
        pagina_inicial()
    elif paginas == "Projetos em Power BI":
        bi()
    elif paginas == "Projetos em Streamlit & Plotly":
        streamlit()
    elif paginas == "Chat bot":
        chatbot()


elif st.session_state["authentication_status"] is False:
    st.error('Usuário/Senha is inválido')
elif st.session_state["authentication_status"] is None:
    st.warning('Por Favor, utilize seu usuário e senha!')


asssista = "https://www.youtube.com/watch?v=OF2TcvV_AsY"
