import streamlit as st

def chatbot():


    st.header("Relatorio em Streamlit & Plotly 📊", divider=True)

    image_path_plotly_strem = "image/stremlit_plotly.png"
    image_path_fifa = "image/stremlit.png"


    st.sidebar.markdown("**Informações de contato.**")

    st.sidebar.image("image/in.png", width=30)
    st.sidebar.link_button("linkedin.",
                        "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    st.sidebar.image("image/wh.png", width=30)
    st.sidebar.link_button("Whatsapp.",
                       "https://wa.me/19994138086")
    

    col15, = st.columns(1)


    with col15:
        st.image(image_path_fifa, caption="Chat bot", width=200)
        st.link_button("Acesse",
                       "https://sreamlitopenai.streamlit.app/") 
        
        
        
