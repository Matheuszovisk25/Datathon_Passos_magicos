import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import joblib
import numpy as np

# Configurações da página - isso deve ser a primeira coisa no script
st.set_page_config(
    page_title="Passos Mágicos",
    page_icon=":sparkles:",
    layout="wide",
)

# Carregar a imagem da logo
logo = "image.png"  # Caminho da imagem que você enviou

# Função para exibir a página de "Visão Geral"
def exibir_visao_geral():
    """Exibe a seção de visão geral com texto descritivo e ícones."""
    st.image(logo, width=120)  # Reduzi a logo em 40%
    st.title("Passos Mágicos :sparkles:")
    st.subheader("Monitoramento e Impacto Social")

    # Texto descritivo sobre a Passos Mágicos
    st.write("""
    **Passos Mágicos** é uma organização não governamental dedicada a transformar a vida de crianças e adolescentes através da educação e do apoio social. 
    Fundada com a missão de proporcionar oportunidades iguais de aprendizado e crescimento, a ONG oferece uma variedade de programas que vão desde 
    apoio escolar até atividades extracurriculares, buscando sempre o desenvolvimento integral dos jovens atendidos. 

    Nosso objetivo é capacitar esses jovens com habilidades e conhecimentos que os preparem para um futuro promissor, contribuindo para a construção de uma sociedade mais justa e igualitária.
    Com a ajuda de nossos parceiros e apoiadores, continuamos a expandir nosso impacto, levando esperança e novas possibilidades para mais comunidades a cada ano.
    """)

    # Carregar as imagens
    icone_1 = Image.open("imagem_1_reduzida.png")
    icone_2 = Image.open("imagem_2_reduzida.png")
    icone_3 = Image.open("imagem_3_reduzida.png")
    icone_4 = Image.open("imagem_4_reduzida.png")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(icone_1, width=220)
        st.write("### Aceleração do Conhecimento")
        st.write("Educação de qualidade, programas educacionais, assistência psicológica e ampliação da visão de mundo. Conheça mais sobre nosso trabalho.")

    with col2:
        st.image(icone_2, width=220)
        st.write("### Programas Especiais")
        st.write("Conheça nosso projeto de apadrinhamento e de intercâmbio, visando uma maior integração dos alunos com diferentes ambientes e culturas.")

    with col3:
        st.image(icone_3, width=220)
        st.write("### Eventos e Ações Sociais")
        st.write("Anualmente, em prol dos alunos, são promovidas campanhas de arrecadação para presentear as centenas de crianças e adolescentes Passos Mágicos.")

    with col4:
        st.image(icone_4, width=220)
        st.write("### Parceiros e Apoiadores")
        st.write("Conheça nossas empresas parceiras e apoiadoras que nos ajudam a dar vida aos nossos projetos de transformação.")

# Função para exibir a página de "Dados"
def exibir_dados():
    """Exibe a seção de dados."""
    st.image(logo, width=120)  # Reduzi a logo em 40%
    st.header("Dados")
    st.write("""
    Aqui você pode carregar e visualizar os dados coletados. Os dados podem incluir métricas de impacto, número de beneficiados, entre outros.
    """)

def exibir_ronaldo():
    st.subheader("Análises - Ronaldo")
    st.write("Conteúdo específico para Ronaldo.")
    
    # Link de incorporação do Power BI
    power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiN2IxYWNmODQtOWYzOC00YzA0LTk1ZTgtM2EyZjY0NzQ0ZTFhIiwidCI6IjQwMDEyMTMxLWNlMzEtNGQ3OC05Mzc2LTY3NWFmYTA3Y2ZiNSJ9"
    
    # Centralizar o Power BI usando HTML e CSS
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <iframe src="{power_bi_embed_url}" width="800" height="600" frameborder="0" allowFullScreen="true"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

def exibir_cassia():
    st.subheader("Análises - Cassia")
    st.write("Conteúdo específico para Cassia.")

def exibir_cleyton():
    st.subheader("Análises - Cleyton")
    st.write("Conteúdo específico para Cleyton.")

# Função para exibir a página de "Análises" com submenu
def exibir_analises():
    """Exibe a seção de análises com um submenu."""
    st.image(logo, width=120)  # Reduzi a logo em 40%
    st.header("Análises")

    # Submenu dentro da seção de Análises
    selected_analysis = option_menu(
        menu_title="Selecione uma análise:",
        options=["Ronaldo", "Cassia", "Cleyton"],  # Removido "Alexandre"
        icons=["person-circle", "person-circle", "person-circle"],
        menu_icon="activity",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5px", "background-color": "#f0f0f0"},
            "icon": {"color": "blue", "font-size": "20px"},
            "nav-link": {"font-size": "14px", "text-align": "center", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#00c3ff", "color": "white"},
        },
    )

    # Exibir a análise selecionada
    if selected_analysis == "Ronaldo":
        exibir_ronaldo()
    elif selected_analysis == "Cassia":
        exibir_cassia()
    elif selected_analysis == "Cleyton":
        exibir_cleyton()

# Função para exibir a página de "Previsões"
def exibir_previsoes():
    """Exibe a seção de previsões com o conteúdo da análise de Alexandre."""
    st.image(logo, width=120)  # Reduzi a logo em 40%
    st.header("Previsões")
    
    # Copiando o conteúdo da função exibir_alexandre para a seção de Previsões
    st.subheader("Previsões com base nas análises de Alexandre")
    
    st.write('### Idade')
    input_age = float(st.slider('Selecione a idade do aluno', 1, 30, 12))

    st.write('### Fase')
    input_level = float(st.slider('Selecione a fase do aluno', 0, 7, 0))

    st.write('### Ingressante')
    input_first_year = st.radio('O aluno é ingressante?', ['Sim', 'Não'], index=0)
    ingressante_dict = {'Sim': 1., 'Não': 0.}

    st.write('### IAA')
    input_iaa = float(st.number_input('Preencha o IAA do aluno', 0., 10., 0., 0.01, "%.3f", key='iaa_previsoes'))

    st.write('### IAN')
    input_ian = float(st.number_input('Preencha o IAN do aluno', 0., 10., 0., 0.05, "%.2f", key='ian_previsoes'))

    st.write('### IEG')
    input_ieg = float(st.number_input('Preencha o IEG do aluno', 0., 10., 0., 0.01, "%.3f", key='ieg_previsoes'))

    tranformed_input = np.array([[
        input_age / 30.,
        input_level / 7.,
        input_ian / 10.,
        input_iaa / 10.,
        input_ieg / 10.,
        1. if input_first_year == 'Sim' else 0.
    ]])

    if st.button('Enviar', key='enviar_previsoes'):
        model = joblib.load('random_forest_regressor_predict_student_inde.pkl')
        pred_inde = model.predict(tranformed_input)[0] * 10
        if pred_inde <= 5.506:
            st.error(f'### Quartzo! INDE previsto: {pred_inde}')
        elif pred_inde > 5.506 and pred_inde <= 6.868:
            st.success(f'### Ágata! INDE previsto: {pred_inde}')
        elif pred_inde > 6.868 and pred_inde <= 8.230:
            st.success(f'### Ametista! INDE previsto: {pred_inde}')
        else:
            st.success(f'### Topázio! INDE previsto: {pred_inde}')
            st.balloons()

# Função para exibir a página de "Contato"
def exibir_contato():
    """Exibe a seção de contato."""
    st.image(logo, width=120)  # Reduzi a logo em 40%
    st.header("Contato")
    st.write("""
    Entre em contato com a ONG Passos Mágicos para saber mais sobre nosso trabalho ou para contribuir com nossos projetos.
    """)
    st.write("Email: contato@passosmagicos.org")
    st.write("Telefone: (11) 1234-5678")

# Função para exibir o menu lateral com o option_menu
def exibir_option_menu():
    """Exibe o menu lateral com o option_menu."""
    with st.sidebar:
        selecao_menu = option_menu(
            menu_title="Menu",  # required
            options=["Visão Geral", "Dados", "Análises", "Contato", "Previsões"],  # Adicionando a opção "Previsões"
            icons=["house", "bar-chart", "clipboard-data", "envelope", "sun"],  # Adicionando ícone para "Previsões"
            menu_icon="cast",  # optional
            default_index=0,  # optional
            styles={
                "container": {"padding": "5px", "background-color": "#f8f9fa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00c3ff", "color": "white"},
            },
        )
    return selecao_menu

# Função principal que executa o aplicativo
def main():
    """Função principal que executa o aplicativo."""
    selecao_menu = exibir_option_menu()

    if selecao_menu == "Visão Geral":
        exibir_visao_geral()
    elif selecao_menu == "Dados":
        exibir_dados()
    elif selecao_menu == "Análises":
        exibir_analises()
    elif selecao_menu == "Contato":
        exibir_contato()
    elif selecao_menu == "Previsões":
        exibir_previsoes()  # Chama a função para a nova seção "Previsões"

    st.markdown("---")

if __name__ == "__main__":
    main()
