import streamlit as st


def chatbot_huggingface():

    st.header("huggingface 🤗", divider=True)


    image_path_huggingface = "image/huggieface.png"


    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")
    


    col17, = st.columns(1)


    with col17:
        st.image(image_path_huggingface, caption="Chat Bot com Huggingface", width=200)
        st.link_button("Acesse",
                 "https://huggingface.co/spaces/lsouzadasilva/space-teste")
