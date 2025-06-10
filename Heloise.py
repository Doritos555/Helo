import streamlit as st
from PIL import Image
import random

def menu():
    
    st.title("Para Heloise")
    st.write("""
             OIII BB <3
              """)

    if 'ms' not in st.session_state:
        st.session_state.ms = []
        st.session_state.ts = []
        st.session_state.r = 0

    st.sidebar.header("MENU")

    st.image("https://i.pinimg.com/736x/87/31/08/8731088a968b11bc574e19413a472ce5.jpg")

    opcao = st.sidebar.selectbox(
        "SELECIONE A FUNÇÃO:",
        options=[
            "Mulher mais linda do mundo",
            "Cantada misteriosa",
            "Presente misterioso",
            "Musica do Stray Kids",
            "Pica Pau",
            "Segredo"
        ]
    )

    if opcao == "Mulher mais linda do mundo":
        if st.sidebar.button("Executar"):

            st.image("Fofa.jpeg", caption="A mulher mais linda do mundo 💖")

    elif opcao == "Cantada misteriosa":
        if st.sidebar.button("Executar"):
            cantadas = [
                "Seu nome é Wi-Fi? Porque eu sinto uma conexão.",
                "Você não é Google, mas tem tudo que eu procuro.",
                "Você é feita de cobre e telúrio? Porque você é Cu-Te.",
                "Se beleza fosse tempo, você seria a eternidade.",
                "Se eu fosse um gato, passaria todas as minhas 7 vidas com você."
            ]
            frase_escolhida = random.choice(cantadas)
            st.success(frase_escolhida)

    elif opcao == "Presente misterioso":
        if st.sidebar.button("Executar"):
            imagens_presentes = [
                r"presente1.png",
                r"presente2.png",
                r"presente3.png",
                r"presente4.png",
                r"presente5.png"
            ]
            imagem_escolhida = random.choice(imagens_presentes)

            try:
                img = Image.open(imagem_escolhida)
                st.image(img, caption="Seu presente misterioso 🎁", use_column_width=True)
            except Exception as e:
                st.error(f"Erro ao abrir imagem: {e}")

    elif opcao == "Musica do Stray Kids":
        if st.sidebar.button("Executar"):
            st.video("https://youtu.be/NNi34HGhbao?si=bg41Loe9J5tX9eIw")

    elif opcao == "Pica Pau":
        if st.sidebar.button("Executar"):
            st.video("https://youtu.be/Zqk9eTtZpzY?si=Oz-pg_zVh_IGF39a") 

    elif opcao == "Segredo":
        if st.sidebar.button("Executar"):
            st.image("te amo.jpg", caption="Te amo 💖")



if __name__ == '__main__':
    menu()
