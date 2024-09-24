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
                                   marker=dict(color='#007FFF', line=dict(color='#01A1FA', width=1)),

        kde = gaussian_kde(inde)
        x_vals = np.linspace(min(inde), max(inde), 100)
        kde_vals = kde(x_vals)

        fig.add_trace(go.Scatter(x=x_vals, y=kde_vals * len(inde), mode='lines', line=dict(color='red'), name='KDE'),
                      row=1, col=1)

        fig.add_trace(go.Box(y=inde, boxmean=True, boxpoints=False,  marker_color='orange', name='Boxplot'), row=1, col=2)

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

        fig.add_trace(go.Histogram(
            x=idades,
            nbinsx=10,
            opacity=0.7,
            name=f'Histograma {ano_especifico}',
            #marker_color='#007FFF'
            marker=dict(color='#007FFF', line=dict(color='#01A1FA', width=1))
        ), row=1, col=1)

        kde = gaussian_kde(idades)
        x_vals = np.linspace(min(idades), max(idades), 100)
        kde_vals = kde(x_vals)

        fig.add_trace(go.Scatter(x=x_vals, y=kde_vals * len(idades), mode='lines', line=dict(color='red'),
                                 name='KDE'), row=1, col=1)

        fig.add_trace(go.Box(y=idades, boxmean=True, marker_color='orange', name='Boxplot'), row=1, col=2)

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
            fig.add_trace(go.Box(y=data['INDE'], boxmean=True, boxpoints=False, marker_color='orange', name=labels[i]))

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

    # Funçao que processa a distribuiCao da idade por ano

    def processar_dist_idade_todos_anos(df_idade):
        # Garantir que a coluna IDADE seja numérica
        df_idade['IDADE'] = pd.to_numeric(df_idade['IDADE'], errors='coerce')

        # Obter todos os anos únicos
        anos = sorted(df_idade['ANO'].unique())

        # Criar DataFrames vazios para armazenar as distribuições e estatísticas descritivas
        distribuições_idade = pd.DataFrame()
        estatisticas_idade = pd.DataFrame()

        # Iterar sobre cada ano e processar as idades
        for ano in anos:
            df_ano = df_idade[df_idade['ANO'] == ano]  # Filtrar o DataFrame por ano

            # Distribuição de Idades
            dist_idade = df_ano['IDADE'].value_counts().sort_index()
            distribuições_idade[f'ANO {ano}'] = dist_idade
            total_alunos =dist_idade.sum()


            # Estatísticas descritivas
            estatisticas = df_ano['IDADE'].describe()
            estatisticas_idade[f'ANO {ano}'] = estatisticas

        # Preencher valores NaN com zeros (opcional)
        distribuições_idade = distribuições_idade.fillna(0)


        # Adicionar uma coluna para a soma total de alunos em todos os anos
        distribuições_idade['TOTAL'] = distribuições_idade.sum(axis=1)

        # Exibir os resultados
        print("\nDistribuições de Idade por Ano com Soma Total de Alunos:\n")
        display(distribuições_idade)


        print("\nEstatísticas Descritivas por Ano:\n")
        display(estatisticas_idade)

        # Processar a distribuição de idades para todos os anos
        #df_idade_dist = processar_dist_idade_todos_anos(df_cleaned)

    def radar_chart(df_aluno, title):
        categorias = df_aluno.columns[1:]  # Excluindo a coluna com o nome do aluno

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
        r=df_aluno.iloc[0, 1:].values,  # Pegando os valores de performance do aluno
        theta=categorias,
        fill='toself',
        name='Desempenho'
    ))

        fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]  # Ajuste o range conforme a escala de suas métricas
            )),
        showlegend=False,
        title=title
    )

        return fig
    

    st.title('Desempenho dos Alunos')

    aluno_selecionado = st.selectbox('Aluno:', df_geral['NOME'].unique())
    ano_selecionado = st.selectbox('Ano:', df_geral['ANO'].unique())

    # Função de exemplo para calcular dados de desempenho
    def calcular_dados_aluno(df, aluno, ano):
        # Filtra o dataframe para o aluno e ano selecionados
        df_filtrado = df[(df['NOME'] == aluno) & (df['ANO'] == ano)]
        return df_filtrado

    df_aluno = calcular_dados_aluno(df_cleaned, aluno_selecionado, ano_selecionado)

    if df_aluno.empty:
        st.write(f"Sem dados de performance para o aluno {aluno_selecionado} no ano {ano_selecionado}.")
    else:
        st.write(df_aluno)
        fig = radar_chart(df_aluno, title=f'Performance do {aluno_selecionado} - ano {ano_selecionado}')
        st.plotly_chart(fig)

 # ---- Texto Principal ----- Incial

    st.write("###Análise de Desempenho dos Alunos da ONG Passos Mágicos com Base no Índice de Desenvolvimento Educacional (INDE) e Distribuição Etária")
    st.write("- Neste primeiro momento, vamos analisar a faixa etária e a distribuição dos alunos da ONG Passos Mágicos. Inicialmente, apenas os dados"
             " referentes ao ano de 2020 incluíam informações sobre a idade dos alunos. Para gerar insights sobre os anos subsequentes, "
             "utilizamos esses dados de 2020 como base, projetando a evolução da idade dos alunos nos anos seguintes. Assim, conseguimos"
             " estimar a faixa etária para os anos posteriores, permitindo uma análise contínua da distribuição etária.")

# ------ Texto Distribuiçao de Idade --------

    st.write("### Distribuições de Idade por Ano com Soma Total de Alunos:")
    #st.dataframe(df_idade_dist)

    st.write("## Verficando a distribuiçao dos alunos por faixa etaria")
    st.write("""A tabela apresenta abaixo a distribuição de idades dos alunos da ONG Passos Mágicos ao longo dos anos de 2020, 2021 e 2022, com o total acumulado por faixa etária. Observamos que a idade dos alunos varia entre 7 e 20 anos, com as maiores concentrações em faixas específicas, como as idades de 13 e 12 anos. No ano de 2022, o número de alunos é maior, com um total de 862, em comparação com 684 em 2021 e 725 em 2020.

    Nas estatísticas descritivas por ano, observamos um aumento gradual na idade média dos alunos, de 12 anos em 2020 para 13,14 anos em 2022. A variação (desvio padrão) diminui ao longo dos anos, indicando uma concentração maior de alunos em torno de idades específicas, especialmente em 2022, quando o desvio padrão é de 1,36. Os valores mínimos e máximos para cada ano também mostram que os alunos mais novos e mais velhos estão progredindo em idade com o passar do tempo.

    Além disso, os quartis sugerem que a maioria dos alunos tem entre 10 e 13 anoao longo dos três anos analisados.""")
    processar_dist_idade_todos_anos(df_cleaned)
    st.write("### 2020")
    st.write("- Em 2020, a ONG Passos Mágicos trabalhou predominantemente com jovens cuja idade girava em torno de 12 anos. A curva de densidade suaviza a distribuição etária, revelando que, embora houvesse algumas pessoas mais jovens e mais velhas, a maior concentração estava entre 11 e 13 anos. O boxplot nos mostra que 50% da população atendida tinha idades entre 11 e 14 anos, com poucos casos abaixo de 8 ou acima de 19. A mediana de 12 anos reforça que a ONG atua majoritariamente com um grupo jovem, nos primeiros anos da adolescência, com características etárias bastante homogêneas.")
    gerar_graficos_idade_ano(df_cleaned, 2020)
    st.write("### 2021")
    st.write("Em 2021, a ONG Passos Mágicos continuou a atender predominantemente jovens, com a idade média subindo levemente para 12,8 anos. A distribuição de idades, representada pelo histograma e suavizada pela curva de densidade, mostra uma concentração significativa entre 12 e 13 anos, sendo essa a faixa etária com maior frequência. O número de pessoas com idades abaixo de 10 anos ou acima de 15 anos foi relativamente baixo, indicando um foco claro em adolescentes no início de sua jornada.")
    st.write("O boxplot confirma essa tendência, revelando que 50% dos atendidos tinham idades entre 12 e 14 anos, com algumas observações atípicas abaixo de 10 e acima de 16 anos. A mediana de 12 anos permanece próxima à média, reforçando a homogeneidade etária desse grupo jovem. Esse perfil etário sugere que a ONG continuou a trabalhar com uma população predominantemente adolescente, consolidando seu impacto na vida de jovens em um momento crucial de suas formações pessoais e sociais.")
    gerar_graficos_idade_ano(df_cleaned, 2021)
    st.write("### 2022")
    st.write("Em 2022, observou-se que a idade média dos beneficiados pela ONG subiu ligeiramente para 13,1 anos. A análise da distribuição etária, representada por um histograma, revela um padrão semelhante ao dos anos anteriores. Atendimentos a pessoas com menos de 10 anos ou mais de 15 foram escassos, destacando o foco da ONG nos adolescentes.")
    st.write("O boxplot reforça essa tendência, mostrando que metade dos atendidos tinha entre aproximadamente 12 e 14 anos, com algumas exceções pontuais abaixo dos 10 e acima dos 16 anos. A mediana de 13 anos, próxima à média, sugere que a tendência permanece consistente com os anos anteriores")
    gerar_graficos_idade_ano(df_cleaned, 2022)

# ------- Analise Inde)
    st.write("## Análise de INDE")
    st.write("""- Índice de Desenvolvimento Educacional (INDE): Esta métrica avalia o desempenho geral dos alunos, ponderando os seguintes indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV. Esses por sua vez, abrangem:
      1º - **Vida acadêmica:**: IAN, IDA e IEG
      2º - **Vida psicopedagógica::**:IPP e IPV 
      2º - **Vida psicossocial::**: IAA e IPS
    Todos esses aspectos impactam diretamente o desempenho dos alunos atendidos pela ONG' """)

    st.write("- Para o ano de 2020 o INDE(Índice do Desenvolvimento Educacional) a maior concentraçao está entre os valores 7 a 8 o que indica que a média gira em torno de 7 a 7,5, mais precisamente 7,3 como indica o bloxpot com a média, logo abaixo. A curva KDE gira em torno disso e a distribuição tem uma cauda levemente à direita, indicando valores maiores esparsos até cerca de 10.")
    gerar_graficos_inde_ano(df_cleaned, 2020)
    st.write("Já para o ano de 2021 no que se refere ao INDE(Índice do Desenvolvimento Educacional) há uma diferença comparada com o ano anterior indicando que a maior parte dos dados está concentrado entre 6 e 7, com poucos valores mais altos (acima de 8). Para este gráfico, a média gira em torno de 6,5 a 7, com um valor preciso de 6,9 como indica o grafico de bloxpot. A curva KDE gira em torno disso e nos mostra que os dados estão distribuídos de maneira relativamente simétrica ao redor desse intervalo.")
    gerar_graficos_inde_ano(df_cleaned, 2021)
    st.write("- Para o ano de 2022 o INDE(Índice do Desenvolvimento Educacional)  maioria dos valores do INDE variou entre **6** e **8**, com o valor **7** sendo o mais comum. A média dos valores parece estar em torno de **7**, já que os valores mais frequentes estão nessa região. O que reflete uma tendência similar aos anos anteriores. A distribuição mostra uma simetria ao redor de 7.")
    gerar_graficos_inde_ano(df_cleaned, 2022)



    df_filter_2020 = df_cleaned[df_cleaned['ANO'] == 2020]
    df_filter_2021 = df_cleaned[df_cleaned['ANO'] == 2021]
    df_filter_2022 = df_cleaned[df_cleaned['ANO'] == 2022]




    st.write("## Comparativo de INDE entre 2020, 2021 e 2022")
    box_plot_comparative([df_filter_2020, df_filter_2021, df_filter_2022], ['2020', '2021', '2022'],
                         'Comparação de INDE: 2020 vs 2021 vs 2022')

    st.write("## As pedras preciosas e a perfomance dos alunos")
    st.write(""" 
A performance dos alunos é representada por pedras preciosas, conforme indicado pelo INDE. O uso dessas pedras tem como objetivo medir o sucesso acadêmico dos alunos ao longo de sua estadia na ONG, além de gerar motivação e inspiração para que busquem novos níveis de crescimento. Cada pedra representa uma faixa específica de desempenho. Por exemplo:
**Pedras**:
    1º - **Quartzo**: 
        - Esta é a pedra inicial de todo aluno. Indica que os alunos que recebem esta pedra têm um desempenho geral, baseado no INDE, que varia entre 2,4 e 5,5.

    2º - **Ágata**: 
        - Logo vem pedra Ágata esta indica que os alunos que recebem esta pedra seu desempenho geral baseado no indicador INDE, varia entre 5,5 a 6,8.
 
    3º - **Ametista**: 
        - A terceira pedra, que é a Ametista indica que os alunos que recebem esta pedra seu desempenho geral baseado no indicador INDE, varia entre 5,5 a 8,2.
        
    4º - **Topazio**: 
        - E a pedra Topazio indica que os alunos que recebem esta pedra seu desempenho geral baseado no indicador INDE, varia entre 8,2 a 9,3.""")

    st.write("## 'Distribuição de Pedras    ")

    df_2020.drop(680, inplace=True)
    plot_barras(df_2020, '2020', 'PEDRA_2020')
    df_2021.drop(32, inplace=True)
    df_2021.drop(245, inplace=True)
    plot_barras(df_2021, '2021', 'PEDRA_2021')
    plot_barras(df_2022, '2022', 'PEDRA_2022')

    #----- Texto Grafico de radar

    st.write("## Performance Acadêmica: Análise Detalhada por Aluno")
    st.write(""" Concluindo tudo o que foi discutido até agora, apresentamos o gráfico de radar que ilustra o 
    desempenho dos alunos com base em todos os indicadores relacionados ao INDE mencionados anteriormente.Exibindo 
    as notas de cada indicador, a pedra preciosa correspondente à perfomance e se houve mudança de fase. 
    A progressão para a próxima fase está diretamente relacionada ao desempenho do aluno, evidenciando a 
    importância de cada indicador na trajetória de aprendizado.    """)





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

        power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiZTBjMzg5NTktNDU5MC00OTc3LWE3YWUtMWE2ODQ1OTM1ZTg2IiwidCI6ImEwNDNmMzhlLTgzYTItNDVhNC1hY2YxLWIwZDNhY2EwYjEwMiJ9&pageName=a0b089a779d2f91bc277"

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <iframe src="{power_bi_embed_url}" width="800" height="600" frameborder="0" allowFullScreen="True"></iframe>
            </div>
            """,
            unsafe_allow_html=True
        )
