import streamlit as st

def bi():

    st.header('Relatórios Power BI 📶', divider=True)

    iamge_path_phone = "image/phone.png"
    image_path_eletric = "image/eletric.png"
    

    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")



    col1, col2 = st.columns(2)

    with col1:
        st.image(iamge_path_phone, caption="Análise de cobrança", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/reportEmbed?reportId=ee62c9c1-2df8-448d-bc1e-f922a18848d8&autoAuth=true&ctid=1f301de5-d58a-442c-a282-80a1a993f044")
        
    with col2:
        st.image(image_path_eletric, caption="Monitoramento Veiculos Eletricos", width=200)
        st.link_button("Acesse.",
                       "https://app.powerbi.com/view?r=eyJrIjoiZmJkMjEwMmEtNGNlZS00ODI2LWIyYjktMTlmYTM1M2JjM2YxIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

