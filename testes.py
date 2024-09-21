import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import joblib
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from scipy.stats import gaussian_kde
import pandas as pd
import plotly.express as px

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

    st.header("Impacto 2023")
    st.write("Conheça os impactos da Passos Mágicos em 2023.")

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

    df_2020 = pd.read_csv('df_2020.csv')
    df_2021 = pd.read_csv('df_2021.csv')
    df_2022 = pd.read_csv('df_2022.csv')
    df_geral = pd.read_csv('df_geral.csv')

    df_cleaned = df_geral.dropna()

    def gerar_graficos_inde_ano(df_inde, ano_especifico):
        df_inde['INDE'] = pd.to_numeric(df_inde['INDE'], errors='coerce')
        df_ano = df_inde[df_inde['ANO'] == ano_especifico]
        inde = df_ano['INDE'].dropna()
        media_inde = inde.mean()

        fig = make_subplots(rows=1, cols=2, subplot_titles=(f'Distribuição - {ano_especifico}', 'Boxplot'),
                            column_widths=[0.6, 0.4])

        fig.add_trace(go.Histogram(x=inde, nbinsx=10, opacity=0.7, name=f'Histograma {ano_especifico}',
                                   marker=dict(color='blue', line=dict(color='lightblue', width=1))), row=1, col=1)

        kde = gaussian_kde(inde)
        x_vals = np.linspace(min(inde), max(inde), 100)
        kde_vals = kde(x_vals)

        fig.add_trace(go.Scatter(x=x_vals, y=kde_vals * len(inde), mode='lines', line=dict(color='red'), name='KDE'),
                      row=1, col=1)

        fig.add_trace(go.Box(y=inde, boxmean=True, boxpoints=False, marker_color='#D2691E', name='Boxplot'), row=1, col=2)

        fig.add_annotation(x=1, y=media_inde, xref="x2", yref="y2", text=f"Média: {media_inde:.1f}", showarrow=False,
                           font=dict(size=12, color="black"), align="center", bordercolor="black", borderwidth=1,
                           borderpad=4, bgcolor="white", opacity=0.8)

        fig.update_layout(title_text=f'Análise de INDE - {ano_especifico}', xaxis_title='Valor', yaxis_title='Frequência',
                          template='plotly_white', showlegend=True, height=800, width=1200)

        st.plotly_chart(fig)

    def gerar_graficos_idade_ano(df_idade, ano_especifico):
        df_idade['IDADE'] = pd.to_numeric(df_idade['IDADE'], errors='coerce')
        df_ano = df_idade[df_idade['ANO'] == ano_especifico]
        idades = df_ano['IDADE'].dropna()
        media_idade = idades.mean()

        fig = make_subplots(rows=1, cols=2, subplot_titles=(f'Distribuição de Idades - {ano_especifico}', 'Boxplot'),
                            column_widths=[0.6, 0.4])

        fig.add_trace(go.Histogram(x=idades, nbinsx=10, opacity=0.7, name=f'Histograma {ano_especifico}',
                                   marker=dict(color='blue')), row=1, col=1)

        kde = gaussian_kde(idades)
        x_vals = np.linspace(min(idades), max(idades), 100)
        kde_vals = kde(x_vals)

        fig.add_trace(go.Scatter(x=x_vals, y=kde_vals * len(idades), mode='lines', line=dict(color='#D2691E'),
                                 name='KDE'), row=1, col=1)

        fig.add_trace(go.Box(y=idades, boxmean=True, marker_color='#D2691E', name='Boxplot'), row=1, col=2)

        fig.add_annotation(x=1, y=media_idade, xref="x2", yref="y2", text=f"Média: {media_idade:.1f}", showarrow=False,
                           font=dict(size=12, color="black"), align="center", bordercolor="black", borderwidth=1,
                           borderpad=4, bgcolor="white", opacity=0.8)

        fig.update_layout(title_text=f'Distribuição de Idade - {ano_especifico}', xaxis_title='Idade', yaxis_title='Frequência',
                          template='plotly_white', showlegend=True, height=800, width=1200)

        st.plotly_chart(fig)

    def box_plot_comparative(data_anos, labels, title):
        fig = go.Figure()
        for i, data in enumerate(data_anos):
            data['INDE'] = pd.to_numeric(data['INDE'], errors='coerce')
            fig.add_trace(go.Box(y=data['INDE'], boxmean=True, boxpoints=False, marker_color='#D2691E', name=labels[i]))

            mean_value = np.mean(data['INDE'])
            fig.add_trace(go.Scatter(x=[i-0.2, i+0.2], y=[mean_value, mean_value], mode="lines",
                                     line=dict(color="red", width=2, dash='dash'), name=f'Média {labels[i]}: {mean_value:.1f}'))

        fig.update_layout(title=title, yaxis_title='Valores', xaxis_title='Anos', template='plotly_white', boxgap=0.30,
                          boxgroupgap=0.3, showlegend=True, height=600, width=1000)
        st.plotly_chart(fig)

    def plot_barras(df, ano, coluna_pedra):
        pedras_contagem = df[coluna_pedra].value_counts()

        fig = go.Figure(go.Bar(
            x=pedras_contagem.index,
            y=pedras_contagem.values,
            marker_color=['#9966CC', '#D2691E', '#D3D3D3', '#007FFF'],
            text=pedras_contagem.values,
            textposition='outside'
        ))

        fig.update_layout(
            title=f'Distribuição de Desempenho - {ano}',
            xaxis_title='Pedras Preciosas',
            yaxis_title='Contagem',
            template='plotly_white',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            height=600,
            width=1000
        )

        st.plotly_chart(fig)

    st.write("## Análise de INDE")
    st.write("- Índice do Desenvolvimento Educacional (INDE): Métrica de Processo Avaliativo Geral do Aluno, esta faz a ponderação dos indicadores IAN, IDA, IEG, IAA, IPS, IPP e IPV. - Veremos a media das notas por ano")
    st.write("- Para o ano de 2020 o INDE(Índice do Desenvolvimento Educacional) a maior concentraçao está entre os valores 7 a 8 o que indica que a média gira em torno de 7 a 7,5, mais precisamente 7,3 como indica o bloxpot com a média, logo abaixo. A curva KDE gira em torno disso e a distribuição tem uma cauda levemente à direita, indicando valores maiores esparsos até cerca de 10.")
    gerar_graficos_inde_ano(df_cleaned, 2020)
    st.write("Já para o ano de 2021 no que se refere ao INDE(Índice do Desenvolvimento Educacional) há uma diferença comparada com o ano anterior indicando que a maior parte dos dados está concentrado entre 6 e 7, com poucos valores mais altos (acima de 8). Para este gráfico, a média gira em torno de 6,5 a 7, com um valor preciso de 6,9 como indica o grafico de bloxpot. A curva KDE gira em torno disso e nos mostra que os dados estão distribuídos de maneira relativamente simétrica ao redor desse intervalo.")
    gerar_graficos_inde_ano(df_cleaned, 2021)
    st.write("- Para o ano de 2022 o INDE(Índice do Desenvolvimento Educacional)  maioria dos valores do INDE variou entre **6** e **8**, com o valor **7** sendo o mais comum. A média dos valores parece estar em torno de **7**, já que os valores mais frequentes estão nessa região. O que reflete uma tendência similar aos anos anteriores. A distribuição mostra uma simetria ao redor de 7.")
    gerar_graficos_inde_ano(df_cleaned, 2022)

    st.write("## Distribuição de Idades")
    st.write("- Em 2020, a ONG Passos Mágicos trabalhou predominantemente com jovens cuja idade girava em torno de 12 anos. A curva de densidade suaviza a distribuição etária, revelando que, embora houvesse algumas pessoas mais jovens e mais velhas, a maior concentração estava entre 11 e 13 anos. O boxplot nos mostra que 50% da população atendida tinha idades entre 11 e 14 anos, com poucos casos abaixo de 8 ou acima de 19. A mediana de 12 anos reforça que a ONG atua majoritariamente com um grupo jovem, nos primeiros anos da adolescência, com características etárias bastante homogêneas.")
    gerar_graficos_idade_ano(df_cleaned, 2020)
    st.write("Em 2021, a ONG Passos Mágicos continuou a atender predominantemente jovens, com a idade média subindo levemente para 12,8 anos. A distribuição de idades, representada pelo histograma e suavizada pela curva de densidade, mostra uma concentração significativa entre 12 e 13 anos, sendo essa a faixa etária com maior frequência. O número de pessoas com idades abaixo de 10 anos ou acima de 15 anos foi relativamente baixo, indicando um foco claro em adolescentes no início de sua jornada.")
    st.write("O boxplot confirma essa tendência, revelando que 50% dos atendidos tinham idades entre 12 e 14 anos, com algumas observações atípicas abaixo de 10 e acima de 16 anos. A mediana de 12 anos permanece próxima à média, reforçando a homogeneidade etária desse grupo jovem. Esse perfil etário sugere que a ONG continuou a trabalhar com uma população predominantemente adolescente, consolidando seu impacto na vida de jovens em um momento crucial de suas formações pessoais e sociais.")
    gerar_graficos_idade_ano(df_cleaned, 2021)
    st.write("Em 2022, observou-se que a idade média dos beneficiados pela ONG subiu ligeiramente para 13,1 anos. A análise da distribuição etária, representada por um histograma, revela um padrão semelhante ao dos anos anteriores. Atendimentos a pessoas com menos de 10 anos ou mais de 15 foram escassos, destacando o foco da ONG nos adolescentes.")
    st.write("O boxplot reforça essa tendência, mostrando que metade dos atendidos tinha entre aproximadamente 12 e 14 anos, com algumas exceções pontuais abaixo dos 10 e acima dos 16 anos. A mediana de 13 anos, próxima à média, sugere que a tendência permanece consistente com os anos anteriores")
    gerar_graficos_idade_ano(df_cleaned, 2022)

    df_filter_2020 = df_cleaned[df_cleaned['ANO'] == 2020]
    df_filter_2021 = df_cleaned[df_cleaned['ANO'] == 2021]
    df_filter_2022 = df_cleaned[df_cleaned['ANO'] == 2022]

    st.write("## Comparativo de INDE entre 2020, 2021 e 2022")
    box_plot_comparative([df_filter_2020, df_filter_2021, df_filter_2022], ['2020', '2021', '2022'],
                         'Comparação de INDE: 2020 vs 2021 vs 2022')

    st.write("## Gráfico de Barras - Distribuição de Desempenho")
    plot_barras(df_2020, '2020', 'PEDRA_2020')
    plot_barras(df_2021, '2021', 'PEDRA_2021')
    plot_barras(df_2022, '2022', 'PEDRA_2022')
    

def exibir_cleyton():
    st.subheader("Análises - Cleyton")

    tab1, tab2 = st.tabs(["Indicadores de Alunos Efetivos vs Faltas", "Dashboard Power BI"])

    with tab1:
        st.write("""
        ### Indicadores de Alunos Efetivos vs Faltas nas Disciplinas por Professores

        **Objetivo**: Este indicador foi criado para analisar a quantidade de desistências dos cursos oferecidos pela associação Passos Mágicos aos alunos, durante o período do ano 2021 até junho/2024.

        **Conceitos**:
        - **Alunos**: crianças e jovens do município de Embu-Guaçu.
        - **Cursos ou Séries**: são programas de educação de qualidade ou educacionais oferecidos aos alunos.
        - **Cursos Extras**: são programas de educação de qualidade ou educacionais para ampliação da visão de mundo, sendo considerados como extracurriculares. Todavia foi desmembrada a série Alfabetização e os cursos Inglês e Psicologia nesse indicador para melhor visualização dos resultados.  
        - **Efetivos**: são os alunos que estão frequentando as aulas na Passos Mágicos.
        - **Faltas**: olhando para o Diário de Aula, separamos os alunos que estão com Faltas não Justificadas.
        - **Período**: trata-se do tempo em que o aluno realiza o curso ou série em cada dia possuindo o período manhã, tarde, noite e especial.
        - **Período especial**: o aluno realiza os cursos ou séries aos finais de semana, ou seja, sábado ou domingo.

        **Pontos relevantes do Indicador de Faltas**:
        - Analisando o período de 2021 a 2024, temos uma queda nas faltas por alunos matriculados, sendo que 2022 saímos de 25% para 13% em 2023 (-13%), e até o momento em 2024 está com 11% de faltas. Isso para um total de 2.093 alunos efetivamente assistindo às aulas.
        - Analisando os Turnos de Aulas, nós temos uma média 18% de Faltas, sendo o período da Manhã e Especial com 19%. Com isso, vimos que estamos na média das faltas no período analisado.
        - Analisando as Disciplinas, no período vemos Polivalente com 47% de faltas, sendo que as demais seguem uma média de 19%. Mas esse percentual alto de faltas, se dá por causa do ano de 2022 com 58% que foi o primeiro ano de aula e provavelmente os alunos não entenderam o propósito do conteúdo passado em aula, mas vemos uma queda nos anos seguintes, sendo 21% em 2023 e até o momento em 2024 com 16%. Isso também se dá pela quantidade de alunos ter baixado muito, quase 80%, os que continuam frequentando as aulas parecem estar compreendendo o conteúdo. Seria uma boa ideia avaliar o conteúdo e satisfação dos alunos.
        - Analisando os Professores, desconsiderando o Professor 20 (Português), que olhando no período está com uma média de 28% de alunos com faltas, mas como ele só trabalhou no ano de 2022 podemos desconsiderar. O nosso destaque com faltas é o Professor 10 (Inglês), com uma média de 27% de faltas. Podemos avaliar o conteúdo das aulas e a condução do professor para aumentar o interesse dos alunos pela aula, ainda mais sendo inglês, idioma fundamental hoje para um futuro promissor.
        - Tirando o ano de 2021, com média de 24% para todos os Professores, a média desse valor vem reduzindo ao longo do tempo, sendo 13% em 2023 e 11% até o momento em 2024.
        """)

    with tab2:
        st.write("### Dashboard de Power BI")

        power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiZTBjMzg5NTktNDU5MC00OTc3LWE3YWUtMWE2ODQ1OTM1ZTg2IiwidCI6ImEwNDNmMzhlLTgzYTItNDVhNC1hY2YxLWIwZDNhY2EwYjEwMiJ9"

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <iframe src="{power_bi_embed_url}" width="800" height="600" frameborder="0" allowFullScreen="true"></iframe>
            </div>
            """,
            unsafe_allow_html=True
        )


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
            options=["Visão Geral", "Dados", "Análises", "Contato", "Previsões"],  
            icons=["house", "bar-chart", "clipboard-data", "envelope", "sun"],  
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
