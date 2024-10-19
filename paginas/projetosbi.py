import streamlit as st

def bi():

    st.markdown("# Relatórios ")

    image_path_adiante = "image/adiante.png"
    image_path_mb = "image/MB.png"
    image_path_lm = "image/LM.png"
    image_path_tb = "image/tribanco.png"
    image_path_vw = "image/VW.png"
    image_path_byd = "image/BYD.png"
    image_path_localiza = "image/localiza.png"
    image_path_zelo = "image/zelo.png"
    image_path_indecx = "image/indecx.png"
    

    st.sidebar.markdown("**Informações de contato.**")

    st.sidebar.image("image/in.png", width=30)

    st.sidebar.link_button("linkedin.",
               "www.linkedin.com/in/leandro-souza-313136190")

    st.sidebar.image("image/wh.png", width=30)
    st.sidebar.link_button("Whatsapp.",
                       "https://wa.me/19994138086")



    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(image_path_adiante, caption="Adiante Locações de pesados", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMDJmNmVjZmYtZmFmYS00ODg4LWI4NjctYzE1ODI0OGY5NWY4IiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col2:
        st.image(image_path_mb, caption="Mercedes Benz", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/reportEmbed?reportId=67a92227-ba38-49b0-b653-c5b7f279d3c7&autoAuth=true&ctid=1f301de5-d58a-442c-a282-80a1a993f044")

    with col3:
        st.image(image_path_lm, caption="LM Transportes", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiYmRiNWNjMWYtZDI0YS00N2IxLTlkOWEtYWViOGM1N2I2NTUyIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")


    with col4:
        st.image(image_path_tb, caption="Tribanco(NPS/CSAT)", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiYzgyNTJlMTAtOWY2NS00YmM5LWE5NzgtZGQ0YjZmY2U1NjVmIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    st.divider()


    col5, col6, col7, col8 = st.columns(4)


    with col5:
        st.image(image_path_vw, caption="Volkswagen Caminhões & Ônibus", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMWE4YzM3ODAtNzdmOS00OWU0LWFlM2ItMjRhZTVkODNjM2IwIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col6:
        st.image(image_path_byd, caption="BYD", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/reportEmbed?reportId=700f71cc-94a9-47fc-9840-e5e499ab0667&autoAuth=true&ctid=1f301de5-d58a-442c-a282-80a1a993f044")
        
    with col7:
        st.image(image_path_localiza, caption="Localiza Caminhões Usados", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiNWU1NWFjNDctNGMyZS00ZGJkLTk5MGEtODVkM2E4YTU5YjllIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col8:
        st.image(image_path_zelo, caption="Grupo Zelo", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMjg1ZDc5ZDItNDlhNi00NGQyLTk1MTMtNzAxNTU3NzY2N2EyIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")
        
    st.divider()

    st.markdown("**Criados para analise interno na minha antiga empresa onde trabalhei.**")

    col9, col10 = st.columns(2)

    with col9:
        st.image(image_path_indecx, caption="Monitoramento de veiculos eletricos", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMmY5YzdhOGEtZDY0ZC00MmMwLTk1ODAtMjY1ZmRjYTZlNDJiIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")

    with col10:
        st.image(image_path_indecx, caption="Relatorio de entregas", width=200)
        st.link_button("Acesse",
                    "https://app.powerbi.com/view?r=eyJrIjoiMTk1NzI4ZDAtNjljYS00ZTllLWI0MzMtYWNiMjcwN2E5ZWYxIiwidCI6IjFmMzAxZGU1LWQ1OGEtNDQyYy1hMjgyLTgwYTFhOTkzZjA0NCJ9")
