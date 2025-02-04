import streamlit as st

def bi():

    st.header('Relatórios Power BI 📶', divider=True)


    image_path_fic = "image/fic.png"
    iamge_path_phone = "image/phone.png"
    

    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")



    col1, = st.columns(1)

    with col1:
        st.image(image_path_fic, caption="Análise de cobrança", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/reportEmbed?reportId=ee62c9c1-2df8-448d-bc1e-f922a18848d8&autoAuth=true&ctid=1f301de5-d58a-442c-a282-80a1a993f044")

