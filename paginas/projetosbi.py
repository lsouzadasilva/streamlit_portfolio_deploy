import streamlit as st

def bi():

    st.header('Relatórios Power BI 📶', divider=True)

    image_path_adiante = "image/adiante.png"
    image_path_mb = "image/MB.png"
    image_path_lm = "image/LM.png"
    image_path_tb = "image/tribanco.png"
    image_path_vw = "image/VW.png"
    image_path_byd = "image/BYD.png"
    image_path_localiza = "image/localiza.png"
    image_path_zelo = "image/zelo.png"
    image_path_indecx = "image/indecx.png"
    image_path_fic = "image/fic.png"
    

    st.sidebar.markdown("**Informações de contato.**")

    st.sidebar.image("image/in.png", width=30)
    st.sidebar.link_button("linkedin.",
                        "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    st.sidebar.image("image/wh.png", width=30)
    st.sidebar.link_button("Whatsapp.",
                       "https://wa.me/19994138086")



    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMDJmNmVjZmYtZmFmYS00ODg4LWI4NjctYzE1ODI0OGY5NWY4IiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col2:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/reportEmbed?reportId=8a90ede4-e194-4dd6-8166-ee6ed6dfe13e&autoAuth=true&ctid=1f301de5-d58a-442c-a282-80a1a993f044")

    with col3:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiYmRiNWNjMWYtZDI0YS00N2IxLTlkOWEtYWViOGM1N2I2NTUyIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")


    with col4:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiNjAxYjIxYjktMjczOC00NWRiLWI2NjQtNmEzNGVmMzM1NmEyIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    st.divider()


    col5, col6, col7, col8 = st.columns(4)


    with col5:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMWE4YzM3ODAtNzdmOS00OWU0LWFlM2ItMjRhZTVkODNjM2IwIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col6:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiYTM0OTUwMGYtMmJjYS00ZTVhLTlkMTktMTQzYzQzM2VmN2I3IiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")
        
    with col7:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiNWU1NWFjNDctNGMyZS00ZGJkLTk5MGEtODVkM2E4YTU5YjllIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col8:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMjg1ZDc5ZDItNDlhNi00NGQyLTk1MTMtNzAxNTU3NzY2N2EyIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")
        
    st.divider()

    st.markdown("**Criados para análise interna.**")

    col9, col10 = st.columns(2)

    with col9:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMDY3Yzc5NTAtOGM1Zi00MzI4LTlmZTUtOGRlNWViYmRmYWViIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col10:
        st.image(image_path_fic, caption="Nome do projeto ou empresa", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMTk1NzI4ZDAtNjljYS00ZTllLWI0MzMtYWNiMjcwN2E5ZWYxIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")
