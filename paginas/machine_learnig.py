import streamlit as st

def machine():
    
    st.header("Machine Learning 💾", divider=True)
    
    
    image_path_machine = "image/stremlit_plotly_sklearning.png"
    
    
    col1, = st.columns(1)
    
    
    with col1:
        st.image(image_path_machine, caption="Predição de Categorias de Produtos com Algoritmos de Machine Learning", width=200)
        st.link_button("Acesse.",
                       "https://machinelearning-classi-pro.streamlit.app/")