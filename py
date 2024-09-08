import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import joblib
import numpy as np

st.set_page_config(
    page_title="Passos Mágicos",
    page_icon=":sparkles:",
    layout="wide",
)

logo = "image.png"  

def exibir_visao_geral():
    """Exibe a seção de visão geral com texto descritivo e ícones."""
    st.image(logo, width=120)  
    st.title("Passos Mágicos :sparkles:")
    st.subheader("Monitoramento e Impacto Social")

    st.write("""
    **Passos Mágicos** é uma organização não governamental dedicada a transformar a vida de crianças e adolescentes através da educação e do apoio social. 
    Fundada com a missão de proporcionar oportunidades iguais de aprendizado e crescimento, a ONG oferece uma variedade de programas que vão desde 
    apoio escolar até atividades extracurriculares, buscando sempre o desenvolvimento integral dos jovens atendidos. 

    Nosso objetivo é capacitar esses jovens com habilidades e conhecimentos que os preparem para um futuro promissor, contribuindo para a construção de uma sociedade mais justa e igualitária.
    Com a ajuda de nossos parceiros e apoiadores, continuamos a expandir nosso impacto, levando esperança e novas possibilidades para mais comunidades a cada ano.
    """)

    # Impacto 2023 - Elemento visual inspirado na imagem (sem fundo laranja)
    st.header("Impacto 2023")
    st.write("Conheça os impactos da Passos Mágicos em 2023.")

    # Organização dos números de impacto em colunas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<h1 style='text-align: center;'>4400</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Pessoas impactadas</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: center;'>1100</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Alunos no programa de Aceleração do Conhecimento</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h1 style='text-align: center;'>100</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Bolsistas em instituições de ensino particular</p>", unsafe_allow_html=True)

    with col4:
        st.markdown("<h1 style='text-align: center;'>94</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Bolsistas em instituições de ensino superior</p>", unsafe_allow_html=True)

    # Continuação da seção de ícones e projetos
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

def exibir_dados():
    """Exibe a seção de dados."""
    st.image(logo, width=120)  
    st.header("Dados")
    st.write("""
    Dados.
    """)

def exibir_ronaldo():
    """Exibe a seção Ronaldo com um submenu utilizando tabs."""
    st.subheader("Análises - Ronaldo")

    # Criação do submenu usando tabs
    tab1, tab2 = st.tabs(["Indicadores de Matrículas vs Desistências", "Dashboard Power BI"])

    with tab1:
        st.write("""
        ### Indicadores de Matrículas vs Desistências nos Cursos ou Séries

        **Objetivo**: Este indicador foi criado para analisar a quantidade de desistências dos cursos oferecidos pela associação Passos Mágicos aos alunos, durante o período do ano 2021 até junho/2024.

        **Conceitos**:
        - **Alunos**: crianças e jovens do município de Embu-Guaçu.
        - **Cursos ou Séries**: são programas de educação de qualidade ou educacionais oferecidos aos alunos.
        - **Cursos Extras**: são programas de educação de qualidade ou educacionais para ampliação da visão de mundo, sendo considerados como extracurriculares. Todavia foi desmembrada a série Alfabetização e os cursos Inglês e Psicologia nesse indicador para melhor visualização dos resultados.  
        - **Matrículas**: são os cadastros dos alunos nos cursos ou séries oferecidas pela Passos Mágicos.
        - **Ticket Médio**: é o resultado da frequência das matrículas por aluno nos cursos ou séries, que especifica quantas matrículas são realizadas por aluno no período em evidência nesse indicador.
        - **Turma**: é o termo utilizado para representar cada curso ou série de forma única dos programas de educação de qualidade ou educacionais.
        - **Desistências**: trata-se da situação do aluno na turma que de alguma forma interrompeu o curso ou a série antes da conclusão por algum motivo que não será especificado nesse indicador, sendo necessário outros estudos para investigar essas desistências.
        - **Série ou Cursos Agrupados**: é o agrupamento de alguns cursos ou séries para melhor visualização dos resultados no dashboard, mantendo as séries e agrupando especificamente os cursos extracurriculares.
        - **Período**: trata-se do tempo em que o aluno realiza o curso ou série em cada dia possuindo o período manhã, tarde e noite, integral, semi-integral e especial.
        - **Período Integral**: o aluno realiza os cursos ou séries nos três períodos do dia que é manhã, tarde e noite.
        - **Período semi-integral**: o aluno realiza os cursos ou séries em dois períodos do dia sendo manhã e tarde ou tarde e noite.
        - **Período especial**: o aluno realiza os cursos ou séries aos finais de semana, ou seja, sábado ou domingo.

        **Pontos relevantes do Indicador de Desistência**:
        Podemos analisar com esse indicador de desistência que no período do ano de 2021 até o ano de 2024 tivemos a frequência de 4,1 matrículas nos cursos ou séries por cada aluno. Se realizamos o filtro por ano em 2021 tivemos 2,2 matrículas por aluno, em 2022 o resultado foi de 1,2 matrículas por aluno, em 2023 tivemos 0,5 matrículas por aluno e em 2024 com 0,3 matrículas por aluno. Isso quer dizer que a quantidade de matrículas foi diminuindo, porém este indicador não detalha os motivos por não ser esse o objetivo. 

        Do outro lado tivemos de 2021 até 2024 o percentual de desistência de 16,87% que em 2021 ficou 14,73%, em 2022 temos 20,19%, em 2023 ficou 21,86% e em 2024 estamos até o momento de junho com 10,30%.

        O total de alunos que tiveram matrículas realizadas no período de 2021 até 2024 foi de 2.163 e nesse mesmo período tivemos 9.157 matrículas em algum dos 38 cursos ou séries oferecidas pela Passos Mágicos, porém o percentual de desistência foi de 16,87% que representa 1.545.

        Analisando o primeiro gráfico percebemos que o percentual maior de desistências foi no curso Psicologia com 28,6% de desistências no período de 2021 até 2024 e se filtrarmos por ano em 2021 tivemos 28,3% nesse mesmo curso, em 2022 o resultado foi de 35%, já em 2023 foi de 37% e em 2024 foi de 10,5%. 

        Nesse último ano como temos somente até o mês de junho, não podemos dizer que tivemos uma redução de desistências no curso de Psicologia e se observarmos os anos anteriores o percentual está aumentando. Nesse mesmo gráfico observamos que a série Fase 8 é a que possui menor percentual de desistência com 4,5%, talvez pelo fato de os alunos ingressarem nas oportunidades de Programas Especiais oferecidas pela Passos Mágicos, como projetos de apadrinhamento e de intercâmbio, visando uma maior integração dos alunos com diferentes ambientes e culturas para aqueles que conseguiram superar os desafios particulares durante toda a jornada e crescimento estudantil.

        Analisando o segundo gráfico podemos verificar que a maior quantidade de matrículas está concentrada no período da tarde com 3.678 cadastros dos alunos em algum curso ou série no período de 2021 até 2024, sendo o maior percentual de desistência no período Especial com 19,27% e logo atrás o período noturno com 18,99%. Provavelmente, esses são alunos que já iniciaram uma jornada de trabalho devido a necessidades particulares e, por ser exaustivo, acabam desistindo dos estudos.

        Analisando a primeira tabela temos especificado de forma analítica os nomes dos cursos ou séries especificando em qual agrupamento elas pertencem. Esses dados estão em ordem decrescente por % de desistências, podendo ser alterados clicando em alguma das colunas. Dessa forma, podemos observar que o curso “Construindo Sonhos” teve 44,44% de desistências nesse período de 2021 até 2024 e está agrupado no curso “Extra”. Em segundo lugar, temos o curso “Psicologia” com 28,57% de desistências.

        Portanto, podemos dizer com esse indicador de matrículas versus desistências nos cursos ou séries que os cursos extras foram descontinuados em 2023, provavelmente pela falta de interesse dos alunos por esses assuntos ou pela dificuldade de estarem disponíveis por mais tempo por questões particulares. Observamos também que a quantidade de matrículas diminuiu com o passar dos anos, possivelmente pela falta de disponibilidade de vagas para novos alunos ou pela redução de novos cursos extras. Esse fato precisaria de mais indicadores para ser detalhado, mas é importante acompanhar que, com o passar dos anos, o percentual de desistência está aumentando cada vez mais, o que pode comprometer a contribuição da associação Passos Mágicos para as vidas das crianças e jovens do município de Embu-Guaçu.
        """)

    with tab2:
        st.write("### Dashboard de Power BI")
        
        power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiN2IxYWNmODQtOWYzOC00YzA0LTk1ZTgtM2EyZjY0NzQ0ZTFhIiwidCI6IjQwMDEyMTMxLWNlMzEtNGQ3OC05Mzc2LTY3NWFmYTA3Y2ZiNSJ9"

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

def exibir_cleyton():
    st.subheader("Análises - Cleyton")


def exibir_analises():
    """Exibe a seção de análises com um submenu."""
    st.image(logo, width=120)  
    st.header("Análises")

    
    selected_analysis = option_menu(
        menu_title="Selecione uma análise:",
        options=["Ronaldo", "Cassia", "Cleyton"],  
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

    
    if selected_analysis == "Ronaldo":
        exibir_ronaldo()
    elif selected_analysis == "Cassia":
        exibir_cassia()
    elif selected_analysis == "Cleyton":
        exibir_cleyton()


def exibir_previsoes():
    """Exibe a seção de previsões com um submenu de opções."""
    st.image(logo, width=120)  
    st.header("Previsões")

    # Submenu com diferentes previsões
    selected_option = option_menu(
        menu_title="Selecione a opção de previsão:",
        options=["Análise Geral", "Previsão Detalhada"],  
        icons=["bar-chart", "clipboard-data"],
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

    # Exibindo o conteúdo conforme a seleção no submenu
    if selected_option == "Análise Geral":
        st.write("""
        Desenvolvido com a proposta de auxiliar no desenvolvimento dos alunos, esse modelo prevê, antes do final do ano letivo, o INDE (Índice de Desenvolvimento Educacional) de um aluno. A previsão é feita com apenas três dos sete indicadores utilizados na ponderação do INDE e algumas informações do aluno. Em mais detalhes, o modelo utiliza:

        - a idade do aluno
        - a fase atual do aluno
        - informação se o aluno é ingressante ou não
        - o IAN (Indicador de adequação de nível) do aluno
        - o IEG (Indicador de Engajamento) do aluno
        - o IAA (Indicador de Autoavaliação) do aluno

        Planejado para aplicações reais, note que o IEG e IAA são as únicas informações que precisam ser colhidas. Todas as outras, já estão disponíveis nos dados administrativos do aluno. Mesmo assim, considerando que o IEG já é colhido para o cálculo do INDE, entende-se que essa informação é de fácil acesso. Dessa forma, apenas o valor do IAA do aluno que realmente seria necessário coletar de informações para realizar a previsão. E sendo o IAA um questionário de cinco questões, entende-se que é um esforço aceitável para a previsão do INDE.

        Sobre as aplicações práticas, o modelo pode ser disponibilizado para os professores ou para os próprios alunos. Para os docentes é possível a análise de vários alunos de forma eficiente, entendendo quais precisam de apoio. O modelo também pode ser utilizado para que o educador confirme suas intuições sobre alunos individualmente. Já para os alunos, o modelo é ideal para terem visibilidade do seu progresso durante a fase.

        Considerando o quão sensível e impactante pode ser para um aluno ter seu INDE previsto, no sentido de se desmotivar por ter um INDE aquém do desejado, ressalta-se que o modelo foi desenvolvido para calcular qual é o previsto se nenhuma ação for tomada. Indicando como o aluno está indo no momento. Em caso de INDE baixo, o aluno pode experimentar no modelo um IEG maior, pensando "e se eu fizer todas as lições de casa pelo resto do ano". Justamente nesse sentido, ele pode ser utilizado no decorrer do ano, em que o aluno ainda pode mudar o seu IEG e IAA. Contribuindo para o aluno entender a importância do IEG e IAA no impacto indireto em todos os outros indicadores. Assim, a previsão não é para limitar as expectativas e sim para auxiliar e motivar o desenvolvimento.

        Por fim, seguem algumas informações técnicas sobre o modelo:
        - Ele não realiza previsões para alunos da fase 8, por causa das características específicas dessa fase.
        - Nos dados de testes as estatísticas são:
            - Erro médio absoluto: 0.44
            - Erro quadrático médio: 0.032
            - Coeficiente de determinação (R²): 0.773
            - Maior erro absoluto: 1.79
        """)

    elif selected_option == "Previsão Detalhada":
        st.write("Insira os dados abaixo para gerar a previsão:")

        # Formulário de input de dados
        with st.form(key='previsoes_form'):
            input_age = st.slider('Idade do aluno', min_value=1, max_value=30, value=12, key='age_slider')

            input_level = st.slider('Fase do aluno', min_value=0, max_value=7, value=0, key='level_slider')

            input_first_year = st.radio('O aluno é ingressante?', ['Sim', 'Não'], index=0, key='first_year_radio')

            st.write("Preencha os índices acadêmicos do aluno:")

            input_iaa = st.number_input('IAA (Índice de Aproveitamento Acadêmico)', min_value=0.0, max_value=10.0, value=0.0, step=0.01, key='iaa_previsoes')

            input_ian = st.number_input('IAN (Índice de Aproveitamento Não-Curricular)', min_value=0.0, max_value=10.0, value=0.0, step=0.05, key='ian_previsoes')

            input_ieg = st.number_input('IEG (Índice de Evolução Geral)', min_value=0.0, max_value=10.0, value=0.0, step=0.01, key='ieg_previsoes')

            submitted = st.form_submit_button("Prever INDE")

        # Processamento da previsão após o envio do formulário
        if submitted:
            tranformed_input = np.array([[
                input_age / 30.,
                input_level / 7.,
                input_ian / 10.,
                input_iaa / 10.,
                input_ieg / 10.,
                1. if input_first_year == 'Sim' else 0.
            ]])

            model = joblib.load('random_forest_regressor_predict_student_inde.pkl')
            pred_inde = model.predict(tranformed_input)[0] * 10

            if pred_inde <= 5.506:
                st.error(f'### Quartzo! INDE previsto: {pred_inde:.2f}')
            elif pred_inde > 5.506 and pred_inde <= 6.868:
                st.success(f'### Ágata! INDE previsto: {pred_inde:.2f}')
            elif pred_inde > 6.868 and pred_inde <= 8.230:
                st.success(f'### Ametista! INDE previsto: {pred_inde:.2f}')
            else:
                st.success(f'### Topázio! INDE previsto: {pred_inde:.2f}')
                st.balloons()


def exibir_contato():
    """Exibe a seção de contato."""
    st.image(logo, width=120) 
    st.header("Contato")
    st.write("""
    Entre em contato com a ONG Passos Mágicos 
    """)
    st.write("Email: ")
    st.write("Telefone: ")


def exibir_option_menu():
    """Exibe o menu lateral com o option_menu."""
    with st.sidebar:
        selecao_menu = option_menu(
            menu_title="Menu",  
            options=["Visão Geral", "Dados", "Análises", "Contato", "Previsões"],  # Adicionando a opção "Previsões"
            icons=["house", "bar-chart", "clipboard-data", "envelope", "sun"],  # Adicionando ícone para "Previsões"
            menu_icon="cast",  
            default_index=0,  
            styles={
                "container": {"padding": "5px", "background-color": "#f8f9fa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#00c3ff", "color": "white"},
            },
        )
    return selecao_menu

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
        exibir_previsoes() 

    st.markdown("---")

if __name__ == "__main__":
    main()
