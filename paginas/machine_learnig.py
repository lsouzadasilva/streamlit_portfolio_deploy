import streamlit as st

def machine():
    
    st.header("Machine Learning 💾", divider=True)
    
    
    image_path_machine = "image/stremlit_plotly_sklearning.png"
    
    
    col1, col2 = st.columns(2)
    
    
    with col1:
        st.image(image_path_machine, caption="Predição de Categorias de Produtos com Algoritmos de Machine Learning", width=200)
        st.link_button("Acesse.",
                       "https://machinelearning-classi-pro.streamlit.app/")

    with col2:
        st.image(image_path_machine, caption="Classificação de Risco de Crédito: Prevendo o Perfil de Crédito com Machine Learning", width=200)
        st.link_button("Acesse.",
                       "https://classificacao-score-credito.streamlit.app/")
