import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi


st.set_page_config(
    page_title='Home',
    page_icon='🏚️',
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
    paginas = st.sidebar.selectbox("Selecione a página", ["Sobre", "Projetos BI"])
    if paginas == "Sobre":
        pagina_inicial()
    elif paginas == "Projetos BI":
        bi()

elif st.session_state["authentication_status"] is False:
    st.error('Usuário/Senha is inválido')
elif st.session_state["authentication_status"] is None:
    st.warning('Por Favor, utilize seu usuário e senha!')


asssista = "https://www.youtube.com/watch?v=OF2TcvV_AsY"
