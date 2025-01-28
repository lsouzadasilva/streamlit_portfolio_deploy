import streamlit as st


def chatbot_huggingface():

    st.header("Chat Bot com huggingface 🤗", divider=True)


    image_path_huggingface = "image/huggieface.png"


    st.sidebar.markdown("**Informações de contato.**")

    st.sidebar.image("image/in.png", width=30)
    st.sidebar.link_button("linkedin.",
                        "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    st.sidebar.image("image/wh.png", width=30)
    st.sidebar.link_button("Whatsapp.",
                       "https://wa.me/19994138086")
    


    col15, = st.columns(1)


    with col15:
        st.image(image_path_fifa,caption="Chat Bot com Huggingface", width=200)
        st.link_button("Acesse",
                 "https://huggingface.co/spaces/lsouzadasilva/space-teste")