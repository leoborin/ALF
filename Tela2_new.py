import webbrowser
import shutil
from tkinter import filedialog
from datetime import datetime, timedelta
import pandas as pd
from tkinter import ttk
import customtkinter
import tkinter as tk
from tkinter import messagebox
import os
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
tamanho = int(10000000)
sys.setrecursionlimit(tamanho)
# from tkinter import ttk
agregado2 = pd.DataFrame()
dfcorte = pd.DataFrame()
DTQPanel = pd.DataFrame()
keylog = 1


def abrir_pdf():
    file_path = "manualALF.pdf"  # Substitua pelo caminho completo do seu arquivo PDF
    os.system(f"start {file_path}")


def exibir_popup():
    # Criar a caixa de diálogo
    resultado = messagebox.askquestion(
        "Abrir Manual", "Deseja ler o Manual?", icon='question')

    # Verificar o resultado da caixa de diálogo
    if resultado == 'yes':
        abrir_pdf()


exibir_popup()

# Obter a data de hoje
data_hoje = datetime.now()

# Formatando a data de hoje no formato '%d/%m/%Y'
data_hoje_formatada = data_hoje.strftime('%d/%m/%Y')

# Calcular a data de ontem
data_ontem = data_hoje - timedelta(days=1)

# Formatando a data de ontem no formato '%d/%m/%Y'
data_ontem_formatada = data_ontem.strftime('%d/%m/%Y')


def on_treeview_select(event):
    global keylog
    keylog = 1
    print("click")
    entrada_j2.delete(0, tk.END)
    entrada_j1.delete(0, tk.END)
    entrada_poste.delete(0, tk.END)

    # Limpar campos anteriores
    limpar_campos()

    # Obter item selecionado
    item = tabela2.selection()

    # Obter valores da linha selecionada
    if item:
        values = tabela2.item(item, 'values')

        # Atualizar campos com os valores obtidos
        # Substitua esta parte do código com a lógica específica para seus campos
        for i, coluna in enumerate(colunas):
            # Exemplo: Se você tem Entry widgets para cada coluna, pode fazer algo como:
            entry_widgets[i].insert(0, values[i])

    item_selecionado = tabela2.focus()

    valores = tabela2.item(item_selecionado, "values")

    if valores:
        entrada_equipamento.delete(0, tk.END)
        entrada_equipamento.insert(0, valores[2])
        print("plow")
        deviceData.delete(0, tk.END)  # buscapiloto
        deviceData.insert(0, "_"+valores[2]+"_"+valores[1])

        # print(df_Share)

        data_hora = valores[1]

        from datetime import datetime, timedelta

        data_hora_formatada = datetime.strptime(
            data_hora, "%Y-%m-%d %H:%M:%S%z")

        # Subtrair 12 horas da data e hora
        nova_data_inicio = data_hora_formatada - timedelta(hours=2)
        nova_data_fim = data_hora_formatada + timedelta(hours=2)

        data_inicio = nova_data_inicio.strftime("%d/%m/%Y")
        hora_i = nova_data_inicio.strftime("%H:%M")

        data_fim = nova_data_fim.strftime("%d/%m/%Y")
        hora_f = nova_data_fim.strftime("%H:%M")

        hora_i, minuto_i = map(int, hora_i.split(":"))
        hora_f, minuto_f = map(int, hora_f.split(":"))

        entrada_data_inicio.delete(0, tk.END)
        entrada_data_inicio.insert(0, data_inicio)
        entrada_hora_inicio.delete(0, tk.END)
        entrada_hora_inicio.insert(0, hora_i)
        entrada_minuto_inicio.delete(0, tk.END)
        entrada_minuto_inicio.insert(0, minuto_i)

        entrada_data_fim.delete(0, tk.END)
        entrada_data_fim.insert(0, data_fim)
        entrada_hora_fim.delete(0, tk.END)
        entrada_hora_fim.insert(0, hora_f)
        entrada_minuto_fim.delete(0, tk.END)
        entrada_minuto_fim.insert(0, minuto_f)

    # Achar_pontos()


def limpar_campos():
    # Adicione a lógica para limpar os campos aqui
    pass


def DTQPlaca():
    global tabela2
    global entry_widgets  # Torna entry_widgets uma variável global
    print("consle.log")

    from elasticsearch import Elasticsearch
    from datetime import datetime, timedelta
    import pandas as pd
    import pandas as pd
    import json

    # Create the client instance

    Placa = filtroplaca.get()
    print(len(Placa))

    data_inicioapp = datainiciofiltro.get()
    hora_inicioapp = '00'
    minuto_inicioapp = '00'
    data_fimapp = datafimfiltro.get()
    hora_fimapp = '23'
    minuto_fimapp = '59'

    import warnings

    from datetime import datetime, timedelta

    # Data de início no formato original
    data_inicio_str = data_inicioapp + " " + \
        hora_inicioapp + ":" + minuto_inicioapp
    print(data_inicio_str)

    # Converter para objeto de data e hora
    data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_inicio = data_inicio + timedelta(hours=3)

    # Converter para o formato desejado
    data_inicio_formatada = data_inicio.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_inicio_formatada)

    # Data de início no formato original
    data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
    print(data_final_str)

    # Converter para objeto de data e hora
    data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_final = data_final + timedelta(hours=3)

    # Converter para o formato desejado
    data_final_formatada = data_final.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_final_formatada)

    Data_inicio = data_inicio_formatada
    Data_fim = data_final_formatada
    es = Elasticsearch(
        "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")
    print(data_inicio_formatada)
    print(data_final_formatada)
    # Successful response!
    es.info()

    # -----------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Search Elastic----------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------"
    print(f"Search Elastic")
    index_name = "rumo-supervisorio-dds"
    doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

    agregado = pd.DataFrame()

    # Teste
    # anomalia 1
    # Teste

    # Teste
    if len(Placa) != 0:
        query = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"state.reported.eventType": "35"}},
                        {"term": {"state.reported.dds.keyword": ""+Placa+""}},

                        {
                            "range": {
                                "state.reported.device_data": {
                                    "gte": ""+Data_inicio+"",
                                    "lte": ""+Data_fim+""
                                }
                            }
                        }
                    ]
                }
            },
            "size": 1000  # Define o tamanho da página para 100 resultados
        }
    else:
        query = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"state.reported.eventType": "35"}},

                        # {"term": {"state.reported.dds.keyword": ""+Placa+""}},

                        {
                            "range": {
                                "state.reported.device_data": {
                                    "gte": ""+Data_inicio+"",
                                    "lte": ""+Data_fim+""
                                }
                            }
                        }
                    ]
                }
            },
            "size": 1000  # Define o tamanho da página para 100 resultados
        }

    try:
        # Execute a consulta
        result = es.search(index=index_name, body=query, timeout="30s")

        # Itere pelos documentos correspondentes
        for hit in result['hits']['hits']:

            df6 = pd.DataFrame(hit['_source'])
            json = df6['state']['reported']
            df7 = pd.DataFrame([json], index=['row1'])

            # print("------------------------------------------")
            agregado = pd.concat([agregado, df7], ignore_index=True)

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta: {str(e)}")

    # print(agregado)

    print(f"Search Elastic fim")
    import datetime

    df = agregado[['status', 'device_data', 'dds',
                   'avaliacaoDTQ', 'classificacao', 'observacoesCco']]

    # Função para extrair 'causa' do dicionário
    def extract_cause(avaliacaoDTQ):
        print("B1")
        if isinstance(avaliacaoDTQ, dict):
            print("B2")
            return avaliacaoDTQ.get('causa')

        else:
            return None

    # Função para extrair 'dataFim' do dicionário
    def extract_dataFim(avaliacaoDTQ):
        if isinstance(avaliacaoDTQ, dict):
            return avaliacaoDTQ.get('dataFim')
        else:
            return None

    # Aplicar as funções e criar as novas colunas
    df['avaliacaoDTQ.causa'] = df['avaliacaoDTQ'].apply(extract_cause)

    # Remover a coluna original 'avaliacaoDTQ'
    df.drop('avaliacaoDTQ', axis=1, inplace=True)

    # df['device_data'] = pd.to_datetime(df['device_data'], infer_datetime_format=True)
    # Assuming df is your DataFrame
    # formats = ['%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z']

    df['device_data'] = df['device_data'].replace(".000000", "", regex=True)
    df['device_data'] = pd.to_datetime(
        df['device_data'], errors='coerce', infer_datetime_format=True)
    print("D")
    # Classificar o DataFrame pela coluna 'device_data' da mais recente para a mais antiga
    df = df.sort_values(by='device_data', ascending=False)

    df_filtered = df.loc[df['status'].notna()]
    df_filtered["NomePortal"] = "#"
    # acharcod
    selected_value = tk.StringVar()
    selected_value.set(dropbox.get())
    print("Textocombox")
    print(selected_value.get())

    if selected_value.get() == "" or selected_value.get() == "Tudo":
        df_filtered = df_filtered
    else:
        df_filtered = df_filtered[df_filtered['classificacao']
                                  == selected_value.get()]

    nomes_unicos = df_filtered['dds'].unique()
    comp = pd.DataFrame()

    for xName in nomes_unicos:
        print(xName)

    # ------------------------------------------------ Codigo Placa
        es = Elasticsearch(
            "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

        # Successful response!
        es.info()
        import pandas as pd

        # Initialize an empty DataFrame

        query = {
            "query": {
                "bool": {
                    "filter": [
                        # {"term": {"state.reported.eventType": "54"}},
                        {"term": {"attributes.dds.keyword": ""+xName+""}},
                    ]
                }
            },
            "size": 5000  # Define o tamanho da página para 100 resultados
        }

        index_name = "rumo-supervisorio-dds-cadastro"
        result = es.search(index=index_name, body=query, timeout="300s")

        df = pd.json_normalize(result, max_level=1)
        df1 = df['hits.hits'][0]
        df2 = pd.json_normalize(df1, max_level=1)
        df2 = df2[df2['_source.attributes'].notnull()]

        for i in df2.index:
            var1 = df2['_source.attributes'][i]
            var2 = pd.json_normalize(var1, max_level=1)

            # df7 = pd.DataFrame([json], index=['row1'])
            print(var2[['kilometer', 'meter']])

            print("------------------------------------------")

            comp = pd.concat([comp, var2], ignore_index=True)

        # Exibir o DataFrame

    comp2 = comp[['dds', 'regiao', 'trecho', 'nomeSB', 'kilometer', 'meter']]
    comp2["coluna_completa"] = comp2[["regiao", "trecho", "nomeSB",
                                      "kilometer", "meter"]].apply(lambda x: " | ".join(x.dropna()), axis=1)
    comp2 = comp2[['dds', "coluna_completa"]]

    merged_df = pd.merge(df_filtered, comp2, on='dds', how='left')
    merged_df['NomePortal'] = merged_df['coluna_completa']
    df = merged_df
    # "Aqui9"

    # Criação da tabela (Treeview) ------------------------------------------------------------TABELA2
    colunas = ("status", "device_data", "dds", "classificacao",
               "observacoesCco", "avaliacaoDTQ.causa", "NomePortal")
    tabela2 = ttk.Treeview(janela, columns=colunas, show="headings")

    # Configurar as colunas
    for coluna in colunas:
        tabela2.heading(coluna, text=coluna)
        tabela2.column(coluna, width=200)

    # Preencher a tabela com os dados do DataFrame
    for index, row in df.iterrows():
        tabela2.insert("", "end", values=(row["status"], row["device_data"], row["dds"],
                       row["classificacao"], row["observacoesCco"], row["avaliacaoDTQ.causa"], row["NomePortal"]))

    # Conectar a função atualizar_campos à seleção na tabela

    tabela2.bind("<ButtonRelease-1>", on_treeview_select)
    tabela2.grid(row=0+ajusteDesigner, column=0,
                 columnspan=8, padx=20, pady=60)
    entry_widgets = [tk.Entry(janela) for _ in colunas]

    return df

    return merged_df
    # ------------------------------------------------ CodigoPlacaFim


def DTQPanel():

    # tk.messagebox.showinfo(
    #    "Atualizando Dados!", "Atualizando dados Painel DTQ e Sharepoint, Aguarde alguns segundos! Click em OK para iniciar")
    global tabela2
    global entry_widgets  # Torna entry_widgets uma variável global
    print("consle.log")

    from elasticsearch import Elasticsearch
    from datetime import datetime, timedelta
    import pandas as pd
    import pandas as pd
    import json

    # Create the client instance

    """
    #------------------------------------------------ Codigo Placa
    es = Elasticsearch("https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

    # Successful response!
    es.info()
    import pandas as pd

    # Initialize an empty DataFrame
    comp = pd.DataFrame()

    query = {
        "query": {
            "bool": {
                "filter": [
                    #{"term": {"state.reported.eventType": "54"}},
                    #{"term": {"attributes.dds.keyword": ""+placabusca+""}},
                ]
            }
        },
        "size": 5000  # Define o tamanho da página para 100 resultados
    }

    index_name = "rumo-supervisorio-dds-cadastro"
    result = es.search(index=index_name, body=query, timeout="300s")

    df = pd.json_normalize(result, max_level=1)
    df1 = df['hits.hits'][0]
    df2 = pd.json_normalize(df1, max_level=1)
    df2 = df2[df2['_source.attributes'].notnull()]


    for i in df2.index:
        var1 = df2['_source.attributes'][i]
        var2 = pd.json_normalize(var1, max_level=1)


        #df7 = pd.DataFrame([json], index=['row1'])


        #print("------------------------------------------")
        comp = pd.concat([comp, var2], ignore_index=True)




    # Exibir o DataFrame

    comp2 = comp[['dds','regiao','trecho','nomeSB','kilometer','meter']]
    comp2["coluna_completa"] = comp2[["regiao", "trecho", "nomeSB", "kilometer", "meter"]].apply(lambda x: " | ".join(x.dropna()), axis=1)
    print(comp2)

    #------------------------------------------------ CodigoPlacaFim
    """

    Placa = filtroplaca.get()
    print(len(Placa))

    data_inicioapp = datainiciofiltro.get()
    hora_inicioapp = '00'
    minuto_inicioapp = '00'
    data_fimapp = datafimfiltro.get()
    hora_fimapp = '23'
    minuto_fimapp = '59'

    import warnings

    from datetime import datetime, timedelta

    # Data de início no formato original
    data_inicio_str = data_inicioapp + " " + \
        hora_inicioapp + ":" + minuto_inicioapp
    print(data_inicio_str)

    # Converter para objeto de data e hora
    data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_inicio = data_inicio + timedelta(hours=3)

    # Converter para o formato desejado
    data_inicio_formatada = data_inicio.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_inicio_formatada)

    # Data de início no formato original
    data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
    print(data_final_str)

    # Converter para objeto de data e hora
    data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_final = data_final + timedelta(hours=3)

    # Converter para o formato desejado
    data_final_formatada = data_final.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_final_formatada)

    Data_inicio = data_inicio_formatada
    Data_fim = data_final_formatada
    es = Elasticsearch(
        "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")
    print(data_inicio_formatada)
    print(data_final_formatada)
    # Successful response!
    es.info()

    # -----------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Search Elastic----------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------"
    print(f"Search Elastic")
    index_name = "rumo-supervisorio-dds"
    doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

    agregado = pd.DataFrame()

    # Teste
    # anomalia 1
    # Teste

    # Teste
    if len(Placa) != 0:
        query = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"state.reported.eventType": "35"}},
                        {"term": {"state.reported.dds.keyword": ""+Placa+""}},

                        {
                            "range": {
                                "state.reported.device_data": {
                                    "gte": ""+Data_inicio+"",
                                    "lte": ""+Data_fim+""
                                }
                            }
                        }
                    ]
                }
            },
            "size": 1000  # Define o tamanho da página para 100 resultados
        }
    else:
        query = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"state.reported.eventType": "35"}},

                        # {"term": {"state.reported.dds.keyword": ""+Placa+""}},

                        {
                            "range": {
                                "state.reported.device_data": {
                                    "gte": ""+Data_inicio+"",
                                    "lte": ""+Data_fim+""
                                }
                            }
                        }
                    ]
                }
            },
            "size": 1000  # Define o tamanho da página para 100 resultados
        }

    try:
        # Execute a consulta
        result = es.search(index=index_name, body=query, timeout="30s")

        # Itere pelos documentos correspondentes
        for hit in result['hits']['hits']:

            df6 = pd.DataFrame(hit['_source'])
            json = df6['state']['reported']
            df7 = pd.DataFrame([json], index=['row1'])

            # print("------------------------------------------")
            agregado = pd.concat([agregado, df7], ignore_index=True)

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta: {str(e)}")

    print(agregado)

    print(f"Search Elastic fim")
    import datetime

    print("A")
    df = agregado[['status', 'device_data', 'dds',
                   'avaliacaoDTQ', 'classificacao', 'observacoesCco']]

    # Função para extrair 'causa' do dicionário
    def extract_cause(avaliacaoDTQ):
        if isinstance(avaliacaoDTQ, dict):
            return avaliacaoDTQ.get('causa')
        else:
            return None

    # Função para extrair 'dataFim' do dicionário
    def extract_dataFim(avaliacaoDTQ):
        if isinstance(avaliacaoDTQ, dict):
            return avaliacaoDTQ.get('dataFim')
        else:
            return None
    print("B")
    # Aplicar as funções e criar as novas colunas
    df['avaliacaoDTQ.causa'] = df['avaliacaoDTQ'].apply(extract_cause)

    print("B#")
    # Remover a coluna original 'avaliacaoDTQ'
    df.drop('avaliacaoDTQ', axis=1, inplace=True)
    print("C")
    print(df.device_data)
    # df['device_data'] = pd.to_datetime(df['device_data'], infer_datetime_format=True)
    # formats = ['%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z']
    df['device_data'] = df['device_data'].replace(".000000", "", regex=True)
    df['device_data'] = pd.to_datetime(
        df['device_data'], errors='coerce', infer_datetime_format=True)
    print("D")
    # Classificar o DataFrame pela coluna 'device_data' da mais recente para a mais antiga
    df = df.sort_values(by='device_data', ascending=False)

    df_filtered = df.loc[df['status'].notna()]
    df_filtered["NomePortal"] = "#"

    # print(df_filtered)
    print("E")
    import pandas as pd

    # Combine as colunaes = Elasticsearch("httpss em uma única coluna de data e hora
    # Converter a coluna 'device_data' para um formato de data e hora
    # df_filtered['data2'] = df_filtered['device_data'][:3]

    # df_ListPanelDTQ = pd.merge(df_filtered, comp2, on="dds",  how="left")
    # df_ListPanelDTQ
    # condicao =
    # df_filtered = df_filtered[condicao]
    selected_value = tk.StringVar()
    selected_value.set(dropbox.get())
    print("Textocombox")
    print(selected_value.get())

    if selected_value.get() == "" or selected_value.get() == "Tudo":
        df = df_filtered
    else:
        print("filtrou!!!!")
        df = df_filtered[df_filtered['classificacao'] == selected_value.get()]
        df_filtered = df
    # "Aqui9"
  # inico modificações  share
    df_filtered["key"] = "_"+df_filtered["dds"] + \
        "_"+df_filtered["device_data"].astype(str)

    # Código Final!!!
    # sharePoint Extration
    from office365.runtime.auth.client_credential import ClientCredential
    from office365.sharepoint.client_context import ClientContext
    from office365.sharepoint.lists.list import List

    client_id = '5261bace-701e-48ac-8bd3-d200b9144a14'
    client_secret = 'T+fRB2N9VMGgtoxOU/+VO22pncv6lmYcmQHtSApBHcw='
    url = "https://rumolog.sharepoint.com/sites/CENTRODEINTELIGNCIADAMANUTENO/"

    client_credentials = ClientCredential(client_id, client_secret)
    ctx = ClientContext(url).with_credentials(client_credentials)

    # Obtenha a lista pelo título
    list_title = "Analise_ALF"
    target_list = ctx.web.lists.get_by_title(list_title)

    data = {
        'Title': [],
        'ID': [],
        'dt_Inicio_Alarme': [],
        'dt_Fim_Alarme': [],
        'dt_Inicio_Ronda': [],
        'dt_Fim_Ronda': [],
        'dt_Previsao_Termino': [],
        'hr_AnomaliaEncontrada': [],
        'Momento_Analise': [],
        'Km_Real_Fratura': [],
        'Km_Algoritimo': [],
        'Status': [],
        'placa': [],
        'corridas': [],
        'usercriador': []



    }

    # Obtenha todos os itens da lista
    items = target_list.get_items().get().execute_query()
    for item in items:
        print("ID: {0}".format(item.properties['ID']))
        data['ID'].append(item.properties['ID'])
        data['Title'].append(item.properties['Title'])
        data['dt_Inicio_Alarme'].append(item.properties['dt_Inicio_Alarme'])
        data['dt_Fim_Alarme'].append(item.properties['dt_Fim_Alarme'])
        data['dt_Inicio_Ronda'].append(item.properties['dt_Inicio_Ronda'])
        data['dt_Fim_Ronda'].append(item.properties['dt_Fim_Ronda'])
        data['dt_Previsao_Termino'].append(
            item.properties['dt_Previsao_Termino'])
        data['hr_AnomaliaEncontrada'].append(
            item.properties['hr_AnomaliaEncontrada'])
        data['Momento_Analise'].append(item.properties['Momento_Analise'])
        data['Km_Real_Fratura'].append(item.properties['Km_Real_Fratura'])
        data['Km_Algoritimo'].append(item.properties['Km_Algoritimo'])
        data['Status'].append(item.properties['Status'])
        data['placa'].append(item.properties['placa'])
        print("viw")
        data['corridas'].append(item.properties['corridas'])
        data['usercriador'].append(item.properties['usercriador'])

    global df_Share
    df = pd.DataFrame(data)
    df_Share = df
    df_Share["key"] = df_Share['Title']
    df_Share = df_Share.drop_duplicates(subset='key', keep='last')
    df_Share

    merged_df = pd.merge(df_filtered, df_Share, on='key', how='left')
    print(merged_df)
    df = merged_df
    df.fillna('', inplace=True)
    print("addveafsa")
    # df = df.sort_values(by='ID', ascending=False)

    # Manter apenas a primeira ocorrência de cada ID (que é a de maior valor de ID)
    # df = df.drop_duplicates(subset='Title', keep='first')


# fim  modificações  share
    # Criação da tabela (Treeview) ------------------------------------------------------------TABELA2
    colunas = ("status", "device_data", "dds", "Status", "classificacao",
               "observacoesCco", "avaliacaoDTQ.causa", "NomePortal")

    tabela2 = ttk.Treeview(janela, columns=colunas, show="headings")

    # Configurar as colunas
    for coluna in colunas:
        tabela2.heading(coluna, text=coluna)
        tabela2.column(coluna, width=200)

    # Preencher a tabela com os dados do DataFrame
    for index, row in df.iterrows():
        tabela2.insert("", "end", values=(row["status"], row["device_data"], row["dds"], row["Status"],
                       row["classificacao"], row["observacoesCco"], row["avaliacaoDTQ.causa"], row["NomePortal"]))

    # Conectar a função atualizar_campos à seleção na tabela

    tabela2.bind("<ButtonRelease-1>", on_treeview_select)
    tabela2.grid(row=0+ajusteDesigner, column=0,
                 columnspan=8, padx=20, pady=60)
    entry_widgets = [tk.Entry(janela) for _ in colunas]

    return df
# fimPanel!!!!!!!!!!!!!!!!!!!!!


def atualizar_campos(event):

    item_selecionado = tabela.focus()

    valores = tabela.item(item_selecionado, "values")

    if valores:
        entrada_equipamento.delete(0, tk.END)
        entrada_equipamento.insert(0, valores[2])

        data_hora = valores[1]

        from datetime import datetime, timedelta

        data_hora_formatada = datetime.strptime(
            data_hora, "%Y-%m-%d %H:%M:%S%z")

        # Subtrair 12 horas da data e hora
        nova_data_inicio = data_hora_formatada - timedelta(hours=2)
        nova_data_fim = data_hora_formatada + timedelta(hours=2)

        data_inicio = nova_data_inicio.strftime("%d/%m/%Y")
        hora_i = nova_data_inicio.strftime("%H:%M")

        data_fim = nova_data_fim.strftime("%d/%m/%Y")
        hora_f = nova_data_fim.strftime("%H:%M")

        hora_i, minuto_i = map(int, hora_i.split(":"))
        hora_f, minuto_f = map(int, hora_f.split(":"))

        entrada_data_inicio.delete(0, tk.END)
        entrada_data_inicio.insert(0, data_inicio)
        entrada_hora_inicio.delete(0, tk.END)
        entrada_hora_inicio.insert(0, hora_i)
        entrada_minuto_inicio.delete(0, tk.END)
        entrada_minuto_inicio.insert(0, minuto_i)

        entrada_data_fim.delete(0, tk.END)
        entrada_data_fim.insert(0, data_fim)
        entrada_hora_fim.delete(0, tk.END)
        entrada_hora_fim.insert(0, hora_f)
        entrada_minuto_fim.delete(0, tk.END)
        entrada_minuto_fim.insert(0, minuto_f)

# Função para salvar os dados do formulário


def salvar_formulario():
    equipamentoapp = entrada_equipamento.get()
    posteapp = entrada_poste.get()
    j1app = entrada_j1.get()
    j2app = entrada_j2.get()
    data_inicioapp = entrada_data_inicio.get()
    hora_inicioapp = entrada_hora_inicio.get()
    minuto_inicioapp = entrada_minuto_inicio.get()
    data_fimapp = entrada_data_fim.get()
    hora_fimapp = entrada_hora_fim.get()
    minuto_fimapp = entrada_minuto_fim.get()

    # Aqui você pode fazer o que desejar com os dados do formulário
    # Por exemplo, imprimir no console ou salvá-los em algum lugar
    print("Equipamento:", equipamentoapp)
    print("Poste:", posteapp)
    print("J1:", j1app)
    print("J2:", j2app)
    print("Data Início:", data_inicioapp)
    print("Hora Início:", hora_inicioapp)
    print("Minuto Início:", minuto_inicioapp)
    print("Data Fim:", data_fimapp)
    print("Hora Fim:", hora_fimapp)
    print("Minuto Fim:", minuto_fimapp)

    entrada_equipamento.delete(0, tk.END)
    entrada_poste.delete(0, tk.END)
    entrada_j1.delete(0, tk.END)
    entrada_j2.delete(0, tk.END)
    entrada_data_inicio.delete(0, tk.END)
    entrada_hora_inicio.delete(0, tk.END)
    entrada_minuto_inicio.delete(0, tk.END)
    entrada_data_fim.delete(0, tk.END)
    entrada_hora_fim.delete(0, tk.END)
    entrada_minuto_fim.delete(0, tk.END)


def limpar_formulario():
    entrada_equipamento.delete(0, tk.END)
    entrada_poste.delete(0, tk.END)
    entrada_j1.delete(0, tk.END)
    entrada_j2.delete(0, tk.END)
    entrada_data_inicio.delete(0, tk.END)
    entrada_hora_inicio.delete(0, tk.END)
    entrada_minuto_inicio.delete(0, tk.END)
    entrada_data_fim.delete(0, tk.END)
    entrada_hora_fim.delete(0, tk.END)
    entrada_minuto_fim.delete(0, tk.END)
    zoomapp2.delete(0, tk.END)
    zoomapp1.delete(0, tk.END)


def preencher_equipamento():
    entrada_equipamento.delete(0, tk.END)
    entrada_equipamento.insert(0, "1.470C.49EA.EBA0")

    entrada_poste.delete(0, tk.END)
    entrada_poste.insert(0, "64729")

    entrada_j1.delete(0, tk.END)
    entrada_j1.insert(0, "62840")

    entrada_j2.delete(0, tk.END)
    entrada_j2.insert(0, "66833")

    entrada_data_inicio.delete(0, tk.END)
    entrada_data_inicio.insert(0, "13/09/2023")

    entrada_hora_inicio.delete(0, tk.END)
    entrada_hora_inicio.insert(0, "06")

    entrada_minuto_inicio.delete(0, tk.END)
    entrada_minuto_inicio.insert(0, "25")

    entrada_data_fim.delete(0, tk.END)
    entrada_data_fim.insert(0, "13/09/2023")

    entrada_hora_fim.delete(0, tk.END)
    entrada_hora_fim.insert(0, "06")

    entrada_minuto_fim.delete(0, tk.END)
    entrada_minuto_fim.insert(0, "51")


# Cria a janela principal
ajusteDesigner = 4
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
janela = customtkinter.CTk()
janela.geometry("1680×1050")
janela.title("Fratura DTQ")
janela.tabview = customtkinter.CTkTabview(janela)  # width=250
janela.tabview.grid(row=0+ajusteDesigner, column=0, columnspan=8,
                    padx=(10, 10), pady=(10, 10), sticky="nsew")
janela.iconbitmap("Logo3.ico")
# janela.textbox = customtkinter.CTkTextbox(janela, width=250)
# janela.textbox.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
janela.logo_label = customtkinter.CTkLabel(
    janela, text="ALF - Analisador de Local de Fratura v3_migred", font=customtkinter.CTkFont(size=30, weight="bold"))
janela.logo_label.grid(row=0, column=0, columnspan=8,
                       rowspan=2, padx=20, pady=(20, 10))
janela.logo_label = customtkinter.CTkLabel(
    janela.tabview, text=" Lista Fraturas: (Selecione a fratura) ")
janela.logo_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(5, 10))
janela.logo_label = customtkinter.CTkLabel(
    janela, text="*Clique para buscar os pontos de J1 | Poste |J2")
janela.logo_label.grid(row=1+ajusteDesigner, column=4,
                       columnspan=2, padx=20, pady=(5, 10))
# janela.tabview2 = customtkinter.CTkTabview(janela, width=250)#width=250
# janela.tabview2.grid(row=1+ajusteDesigner, column=0,columnspan=8,rowspan=6, padx=(10, 10), pady=(10, 10), sticky="nsew")
# row=0, column=0, columnspan=8,padx=60, pady=60
# Criar a caixa de seleção (dropbox)

janela.logo_label = customtkinter.CTkLabel(janela, text="classificação")
janela.logo_label.grid(row=3, column=0, padx=10, pady=10)

options = ["Tudo", "Trilho Quebrado", "VIA - Bondeamento",
           "Boletim", "Ocupação", "TO - Análise", "Manutenção TO"]
dropbox = customtkinter.CTkOptionMenu(janela, values=options)
dropbox.grid(row=3, column=1, padx=10, pady=10)

# Criar um DataFrame de exemplo


# Cria os campos do formulário
rotulo_equipamento = customtkinter.CTkLabel(janela, text="Equipamento:")
rotulo_equipamento.grid(row=1+ajusteDesigner, column=0, padx=10, pady=5)
entrada_equipamento = customtkinter.CTkEntry(janela)
entrada_equipamento.grid(row=1+ajusteDesigner, column=1, padx=10, pady=5)

rotulo_poste = customtkinter.CTkLabel(janela, text="Poste:")
rotulo_poste.grid(row=2+ajusteDesigner, column=2, padx=10, pady=5)
entrada_poste = customtkinter.CTkEntry(janela)
entrada_poste.grid(row=2+ajusteDesigner, column=3, padx=10, pady=5)

rotulo_j1 = customtkinter.CTkLabel(janela, text="J1:")
rotulo_j1.grid(row=2+ajusteDesigner, column=0, padx=10, pady=5)
entrada_j1 = customtkinter.CTkEntry(janela)
entrada_j1.grid(row=2+ajusteDesigner, column=1, padx=10, pady=5)

rotulo_j2 = customtkinter.CTkLabel(janela, text="J2:")
rotulo_j2.grid(row=2+ajusteDesigner, column=4, padx=10, pady=5)
entrada_j2 = customtkinter.CTkEntry(janela)
entrada_j2.grid(row=2+ajusteDesigner, column=5, padx=10, pady=5)

rotulo_T1 = customtkinter.CTkLabel(janela, text="Linha:")
rotulo_T1.grid(row=8+ajusteDesigner, column=0, padx=10, pady=5)
entrada_T1 = customtkinter.CTkEntry(janela)
entrada_T1.grid(row=8+ajusteDesigner, column=1, padx=10, pady=5)
valor_padrao = "T1"
entrada_T1.insert(0, valor_padrao)


zoomapp1 = customtkinter.CTkEntry(janela)
zoomapp1.grid(row=12+ajusteDesigner, column=0, padx=10, pady=5)
zoomapp2 = customtkinter.CTkEntry(janela)
zoomapp2.grid(row=11+ajusteDesigner, column=0, padx=10, pady=5)


def aplicar_mascara(event):
    texto = entrada_data_inicio.get()
    if len(texto) == 2:
        entrada_data_inicio.insert(2, '/')
    elif len(texto) == 5:
        entrada_data_inicio.insert(5, '/')


def aplicar_mascara_FIM(event):
    texto = entrada_data_fim.get()
    if len(texto) == 2:
        entrada_data_fim.insert(2, '/')
    elif len(texto) == 5:
        entrada_data_fim.insert(5, '/')


rotulo_data_inicio = customtkinter.CTkLabel(janela, text="Data Início:")
rotulo_data_inicio.grid(row=5+ajusteDesigner, column=0, padx=10, pady=5)


entrada_data_inicio = customtkinter.CTkEntry(
    janela, placeholder_text="dd/mm/yyyy")
entrada_data_inicio.grid(row=5+ajusteDesigner, column=1, padx=10, pady=5)
entrada_data_inicio.bind("<KeyRelease>", aplicar_mascara)

rotulo_hora_inicio = customtkinter.CTkLabel(janela, text="Hora:")
rotulo_hora_inicio.grid(row=5+ajusteDesigner, column=2, padx=10, pady=5)
entrada_hora_inicio = customtkinter.CTkEntry(janela, placeholder_text="HH")
entrada_hora_inicio.grid(row=5+ajusteDesigner, column=3, padx=10, pady=5)

rotulo_minuto_inicio = customtkinter.CTkLabel(janela, text="Minuto:")
rotulo_minuto_inicio.grid(row=5+ajusteDesigner, column=4, padx=10, pady=5)
entrada_minuto_inicio = customtkinter.CTkEntry(janela, placeholder_text="MM")
entrada_minuto_inicio.grid(row=5+ajusteDesigner, column=5, padx=10, pady=5)

rotulo_data_fim = customtkinter.CTkLabel(janela, text="Data Fim:")
rotulo_data_fim.grid(row=6+ajusteDesigner, column=0, padx=10, pady=5)


entrada_data_fim = customtkinter.CTkEntry(
    janela, placeholder_text="dd/mm/yyyy")
entrada_data_fim.grid(row=6+ajusteDesigner, column=1, padx=10, pady=5)
entrada_data_fim.bind("<KeyRelease>", aplicar_mascara_FIM)


rotulo_hora_fim = customtkinter.CTkLabel(janela, text="Hora:")
rotulo_hora_fim.grid(row=6+ajusteDesigner, column=2, padx=10, pady=5)
entrada_hora_fim = customtkinter.CTkEntry(janela, placeholder_text="HH")
entrada_hora_fim.grid(row=6+ajusteDesigner, column=3, padx=10, pady=5)

rotulo_minuto_fim = customtkinter.CTkLabel(janela, text="Minuto:")
rotulo_minuto_fim.grid(row=6+ajusteDesigner, column=4, padx=10, pady=5)
entrada_minuto_fim = customtkinter.CTkEntry(janela, placeholder_text="MM")
entrada_minuto_fim.grid(row=6+ajusteDesigner, column=5, padx=10, pady=5)

checkbox_var = tk.BooleanVar()
checkbox = customtkinter.CTkCheckBox(
    janela, text="4.Inverter --> Carregado ", variable=checkbox_var)
checkbox.grid(row=12+ajusteDesigner, column=2, padx=10, pady=5)

fitting = customtkinter.CTkEntry(janela, placeholder_text="Fitting")
fitting.grid(row=10+ajusteDesigner, column=0, padx=10, pady=5)
deviceData = customtkinter.CTkEntry(janela, placeholder_text="deviceData")
deviceData.grid(row=13+ajusteDesigner, column=0, padx=10, pady=5)
# checkbox.pack()

datainiciofiltrolabel = customtkinter.CTkLabel(
    janela, text="Data Incio Fraturas:")
datainiciofiltrolabel.grid(row=2, column=0, padx=10, pady=5)

datainiciofiltro = customtkinter.CTkEntry(
    janela, placeholder_text="dd/mm/yyyy")
datainiciofiltro.grid(row=2, column=1, padx=10, pady=5)

datafimfiltrolabel = customtkinter.CTkLabel(janela, text="Data fim Fraturas:")
datafimfiltrolabel.grid(row=2, column=2, padx=10, pady=5)

datafimfiltro = customtkinter.CTkEntry(janela, placeholder_text="dd/mm/yyyy")
datafimfiltro.grid(row=2, column=3, padx=10, pady=5)

filtroplaca = customtkinter.CTkEntry(janela, placeholder_text="Placa")
filtroplaca.grid(row=2, column=4, padx=10, pady=5)

datainiciofiltro.delete(0, tk.END)
datainiciofiltro.insert(0, data_ontem_formatada)
datafimfiltro.delete(0, tk.END)
datafimfiltro.insert(0, data_hoje_formatada)


# Carregar dados do Excel em um DataFrame
nome_arquivo_excel = "DTQ Analise.xlsx"

df = pd.read_excel(nome_arquivo_excel)
dados = df
df = pd.DataFrame(dados)

# Função para atualizar os campos de entrada de texto

# campo_idade.delete(0, tk.END)
# campo_idade.insert(0, valores[1])

# Criação da tabela (Treeview) ------------------------------------------------------------TABELA1
"""
colunas = ("DDS2", "Data Evento","KMREAL","Analisado")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

# Configurar as colunas
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=200)

# Preencher a tabela com os dados do DataFrame
for index, row in df.iterrows():
    tabela.insert("", "end", values=(row["DDS2"], row["Data Evento"],row["KMREAL"],row["Analisado"]))

# Conectar a função atualizar_campos à seleção na tabela
tabela.bind("<ButtonRelease-1>", atualizar_campos)

tabela.grid(row=0+ajusteDesigner, column=0, columnspan=8,padx=20, pady=60)
"""


# Criação da tabela (Treeview) ------------------------------------------------------------TABELA2
colunas = ("status", "device_data", "dds", "classificacao",
           "observacoesCco", "avaliacaoDTQ.causa", "coluna_completa")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

# Configurar as colunas
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=200)

# Preencher a tabela com os dados do DataFrame
for index, row in df.iterrows():
    tabela.insert("", "end", values=(row["status"], row["device_data"], row["dds"],
                  row["classificacao"], row["observacoesCco"], row["avaliacaoDTQ.causa"], row["coluna_completa"]))

# Conectar a função atualizar_campos à seleção na tabela
tabela.bind("<ButtonRelease-1>", atualizar_campos)

tabela.grid(row=0+ajusteDesigner, column=0, columnspan=8, padx=20, pady=60)

# -----------------------------------------------------------------------------------------------------------------------------------------"
# -----------------------------------------------------------Programação Algoritimo--------------------------------------------------------"
# -----------------------------------------------------------------------------------------------------------------------------------------"


def plot_grafico1():
    tk.messagebox.showinfo("Antenção!", "Para utilizar o Modo Automático, é essencial ter um entendimento da teoria funcionamento. Certifique-se de que a resposta esteja consistente. Em caso de erros ou dúvidas, por favor, informe à equipe de Engenharia ou Monitoramento TO.")
    try:
        # -----------------------------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Input---------------------------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------------------------"

        varAngleD = 10*1.0
        varAngleE = 10*0.5
        VarAmplitudeE = 0.075
        VarAmplitudeD = -0.025
        varreta = 600
        VarAjuste2 = 0.75
        varposte = 20

        equipamentoapp = entrada_equipamento.get()
        posteapp = entrada_poste.get()
        j1app = entrada_j1.get()
        j2app = entrada_j2.get()
        data_inicioapp = entrada_data_inicio.get()
        hora_inicioapp = entrada_hora_inicio.get()
        minuto_inicioapp = entrada_minuto_inicio.get()
        data_fimapp = entrada_data_fim.get()
        hora_fimapp = entrada_hora_fim.get()
        minuto_fimapp = entrada_minuto_fim.get()
        T1_app = entrada_T1.get()

        import warnings

        from datetime import datetime, timedelta

        # Data de início no formato original
        data_inicio_str = data_inicioapp + " " + \
            hora_inicioapp + ":" + minuto_inicioapp
        print(data_inicio_str)

        # Converter para objeto de data e hora
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

        # Acrescentar 3 horas
        data_inicio = data_inicio + timedelta(hours=3)

        # Converter para o formato desejado
        data_inicio_formatada = data_inicio.strftime("%Y-%m-%dT%H:%M:%S.999Z")

        print(data_inicio_formatada)

        # Data de início no formato original
        data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
        print(data_final_str)

        # Converter para objeto de data e hora
        data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

        # Acrescentar 3 horas
        data_final = data_final + timedelta(hours=3)

        # Converter para o formato desejado
        data_final_formatada = data_final.strftime("%Y-%m-%dT%H:%M:%S.999Z")

        print(data_final_formatada)

        J1_Km = int(j1app)
        J2_Km = int(j2app)
        Poste_KM = int(posteapp)
        # Data_inicio = "2023-09-13T09:25:00.000Z"
        # Data_fim = "2023-09-13T09:51:59.999Z"
        Data_inicio = data_inicio_formatada
        Data_fim = data_final_formatada
        # Placa = "1.470C.49EA.EBA0"
        Placa = equipamentoapp

        import warnings

        # Suprimir todos os warnings
        warnings.filterwarnings('ignore')

        if (keylog == 1):
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Conexão Elastic---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            import warnings

            # Suprimir todos os warnings
            warnings.filterwarnings('ignore')

            print(f"Conexão Elastic")
            from elasticsearch import Elasticsearch
            from datetime import datetime, timedelta
            import pandas as pd

            # Create the client instance
            es = Elasticsearch(
                "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

            # Successful response!
            es.info()

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Search Elastic----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Search Elastic")
            index_name = "rumo-supervisorio-dds"
            doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

            agregado = pd.DataFrame()

            # Teste
            # anomalia 1
            # Teste

            # Teste
            query = {
                "query": {
                    "bool": {
                        "filter": [
                            {"term": {"state.reported.eventType": "54"}},
                            {"term": {"state.reported.dds.keyword": ""+Placa+""}},
                            {"term": {"state.reported.collectOrigin.keyword": ""+T1_app+""}},


                            {
                                "range": {
                                    "state.reported.device_data": {
                                        "gte": ""+Data_inicio+"",
                                        "lte": ""+Data_fim+""
                                    }
                                }
                            }
                        ]
                    }
                },
                "size": 1000  # Define o tamanho da página para 100 resultados
            }

            try:
                # Execute a consulta
                result = es.search(index=index_name, body=query, timeout="30s")

                # Itere pelos documentos correspondentes
                for hit in result['hits']['hits']:

                    df6 = pd.DataFrame(hit['_source'])
                    json = df6['state']['reported']
                    df7 = pd.DataFrame([json], index=['row1'])

                    # print("------------------------------------------")
                    agregado = pd.concat([agregado, df7], ignore_index=True)

            except Exception as e:
                print(f"Ocorreu um erro durante a consulta: {str(e)}")

            # agregado

            print(f"Search Elastic fim")
        else:
            agregado = dfcorte

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Ajustes Bases-----------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print(f"Ajustes Bases")

        colunas_desejadas = [
            'resistenciadoCabo',
            'resistenciaTotalMedida',
            'pontoAlarmeAbsoluto',
            'pontoAlarmeDaMedia',
            'device_data',
        ]

        dfagragado = agregado[colunas_desejadas]
        # dfagragado

        import pandas as pd
        import numpy as np

        dfagragado['data_com_fuso'] = pd.to_datetime(dfagragado['device_data'])
        dfagragado['data_sem_fuso'] = dfagragado['data_com_fuso'].dt.tz_localize(
            None)

        dfagragado['intdt'] = pd.to_numeric(
            dfagragado['data_sem_fuso'], downcast='integer')

        df = dfagragado.sort_values(by='data_sem_fuso').reset_index()

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Valorando x-----------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"

        df['x1'] = df['intdt']
        df['y1'] = df['resistenciaTotalMedida']
        df['x2'] = 0
        df['y2'] = 0
        df['x-1'] = 0
        df['y-1'] = 0

        zoomapp1_var = float(zoomapp1.get())
        zoomapp2_var = float(zoomapp2.get())

        for x in df.index:
            # print(x)
            maxx = len(df)-1
            if 0 < x < maxx:
                df['x2'][x] = df['intdt'][x+1]
                df['y2'][x] = df['resistenciaTotalMedida'][x+1]
                df['x-1'][x] = df['intdt'][x-1]
                df['y-1'][x] = df['resistenciaTotalMedida'][x-1]

        df['incl'] = 0
        df['x1'] = df['intdt']/10000000000000*VarAjuste2
        df['x2'] = df['x2']/10000000000000*VarAjuste2
        df['x-1'] = df['x-1']/10000000000000*VarAjuste2
        df['grau'] = 'blank'
        df['cor'] = 'blue'

        # if zoomapp1_var != '':#
        print(df['x1'])
        print("zoomapp1_var")
        print(float(zoomapp1_var)*VarAjuste2)

        print("zoomapp2_var")
        print(float(zoomapp2_var)*VarAjuste2)
        print("----")

        # if zoomapp2_var != '':

        print("----------------Filtrar")

        df = df.loc[(df['x1'] >= zoomapp1_var*VarAjuste2) &
                    (df['x1'] <= zoomapp2_var*VarAjuste2)]

        agregado = df
        print(df['x1'])
        print(zoomapp1_var)

        maxx = len(df)-1

        for x in df.index:
            x1 = df['x1'][x]
            y1 = df['y1'][x]
            x2 = df['x2'][x]
            y2 = df['y2'][x]
            incl = (y2 - y1) / (x2 - x1)
            perto_poste = df['resistenciadoCabo'][x] - \
                df['resistenciaTotalMedida'][x]

            df['incl'][x] = round(incl, 2)
            if -varreta <= incl <= varreta:

                if -varposte <= perto_poste <= varposte:
                    df['grau'][x] = 'reto poste'
                    df['cor'][x] = 'blue'
                else:
                    df['grau'][x] = 'reto'
                    df['cor'][x] = 'purple'

            else:

                df['grau'][x] = 'curva'
                df['cor'][x] = 'green'

        # df = df.drop('index', axis=1)
        df = df.reset_index()
        print('df_view')
        print(df)

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Poste J1 J2 ------------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print(f"Poste J1 J2")

        # poste localizar
        print(f"Poste loc")

        df_filtrado = df[df['grau'] == 'reto poste']
        print(f"Poste loc1")
        Poste1_id = df_filtrado.index[0]
        print(f"Poste loc2")
        print(Poste1_id)
        Poste1_id = Poste1_id
        print(f"Poste loc3")
        Poste_X = df['x1'][Poste1_id]
        print(f"Poste loc4")
        Poste_Y = df['y1'][Poste1_id]
        Poste1_id
        print(f"Poste max")
        # poste localizar max
        df_filtrado = df[df['grau'] == 'reto poste']

        Poste1_id_max = df_filtrado.index[-1]
        Poste1_id_max = Poste1_id_max
        Poste_X_max = df['x1'][Poste1_id_max]+1
        Poste_Y_max = df['y1'][Poste1_id_max]+1

        # Poste1_id_max
        df['grau'][Poste1_id_max+1] = 'reto poste'

        df_ext = df[df['grau'] == 'reto']

        for x in df_ext.index:
            x1_ext = df_ext['x1'][x]

            if x1_ext > Poste_X:
                df['grau'][x] = 'reto Direita'
                df['cor'][x] = 'purple'

            else:
                df['grau'][x] = 'reto Esquerda'
                df['cor'][x] = 'Orange'
        print(f"j1 loc")
        # J1 localizar
        df_filtrado2 = df[df['grau'] == 'reto Esquerda']

        J1_id = df_filtrado2.index[-1]+1
        J1_id = J1_id
        J1_X = df['x1'][J1_id]
        J1_Y = df['y1'][J1_id]

        # J2 localizar
        print(f"j2 loc")
        df_filtrado3 = df[df['grau'] == 'reto Direita']

        J2_id = df_filtrado3.index[0]
        J2_id = J2_id
        J2_X = df['x1'][J2_id]
        J2_Y = df['y1'][J2_id]

        print(J1_id)
        print(J2_id)

        # direita e esquerda

        df_filtrado4 = df[df['grau'] == 'curva']

        for x in df_filtrado4.index:
            x1_curva = df_filtrado4['x1'][x]

            if x1_curva > Poste_X:
                df['grau'][x] = 'curva Direita'
                df['cor'][x] = '#c8ff00'

            else:
                df['grau'][x] = 'curva Esquerda'
                df['cor'][x] = '#52baa7'

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Int para KM ------------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print(f"KM")

        df['m'] = 0
        df['b'] = 0
        df['cof'] = 0
        df['b2'] = 0
        df['cof2'] = 0

        J1_int = J1_X
        J2_int = J2_X
        Poste_int = Poste_X

        a_int = Poste_int - J1_int
        a_km = Poste_KM - J1_Km

        a_int2 = Poste_int - J2_int
        a_km2 = Poste_KM - J2_Km

        df['b'] = df['x1'] - J1_int
        df['cof'] = df['b'] / a_int * -1
        df['m'] = J1_Km + a_km * df['cof']

        df['m']

        a_km_inverter = Poste_KM - J2_Km
        a_km2_inverter = J1_Km - Poste_KM

        # flag inverter
        varcheck = checkbox_var.get()
        print("varCheck" + str(varcheck))

        if str(varcheck) == "True":
            inverter = "Sim"
        else:
            inverter = "Não"

        if inverter == "Não":

            for i in df.index:
                if df['x1'][i] <= Poste_int:

                    df['b'][i] = df['x1'][i] - J1_int
                    df['cof'][i] = df['b'][i] / a_int
                    df['m'][i] = J1_Km + (a_km * df['cof'][i])

                else:

                    df['b2'][i] = df['x1'][i] - Poste_int
                    df['cof2'][i] = df['b2'][i] / a_int2
                    df['m'][i] = Poste_KM + (a_km2 * df['cof2'][i])

        else:

            for i in df.index:
                if df['x1'][i] <= Poste_int:

                    df['b'][i] = df['x1'][i] - J1_int
                    df['cof'][i] = df['b'][i] / a_int
                    df['m'][i] = J2_Km + (a_km_inverter * df['cof'][i])

                else:

                    df['b2'][i] = df['x1'][i] - Poste_int
                    df['cof2'][i] = df['b2'][i] / a_int2
                    df['m'][i] = Poste_KM - (a_km2_inverter * df['cof2'][i])

        df['km'] = round(df['m']/1000, 3)

        import pandas as pd

        # Crie um DataFrame de exemplo com uma coluna de quilometragem

        # Função para formatar uma única entrada de quilometragem
        def aplicar_mascara(quilometragem):
            parte_inteira = int(quilometragem)
            parte_decimal = int((quilometragem - parte_inteira) * 1000)
            return f"{parte_inteira:03d}+{parte_decimal:03d}"

        # Aplicar a função para formatar a coluna inteira
        df['KM_Name'] = df['km'].apply(aplicar_mascara)

        df['km2'] = 0
        df['km-1'] = 0

        for x in df.index:
            # print(x)
            maxx = len(df)-1
            if 0 < x < maxx:
                df['km2'][x] = df['km'][x+1]
                df['km-1'][x] = df['km'][x-1]

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Variação Graus Anomalia-------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print(f"Anomalia")
        import math

        df_CD = df[(df['grau'] == 'curva Esquerda')]

        df_CD

        df["angle_anomalia"] = 0

        for i in df_CD.index:
            # Defina as coordenadas dos três pontos
            x1 = df['km-1'][i]
            y1 = df['y-1'][i]/varAngleD
            x2 = df['km'][i]
            y2 = df['y1'][i]/varAngleD
            x3 = df['km2'][i]
            y3 = df['y2'][i]/varAngleD

        #    x1 = 169448.4857
        #    y1 = 259.94
        #    x2 = 169448.4921
        #    y2 = 259.82
        #    x3 = 169448.4985
        #    y3 = 177.62

            # Calcule os vetores entre os pontos
            v1 = (x1 - x2, y1 - y2)
            v2 = (x3 - x2, y3 - y2)

            # Calcule os ângulos entre os vetores usando a função atan2
            angle1 = math.atan2(v1[1], v1[0])
            angle2 = math.atan2(v2[1], v2[0])

            # Calcule o ângulo entre os vetores subtraindo os ângulos
            angle = angle2 - angle1

            # Certifique-se de que o ângulo resultante esteja no intervalo de 0 a 2*pi
            if angle < 0:
                angle += 2 * math.pi

            # Converter o ângulo de radianos para graus, se necessário
            angle_degrees = math.degrees(angle)
            df['angle_anomalia'][i] = angle_degrees

            print(f"O ângulo entre os pontos é de {angle_degrees} graus.")

        # df_CE = df[(df['grau'] == 'curva Direita') & (df['x1'] < Poste_X) & (df['x1'] > J2_X)]
        df_CE = df[(df['grau'] == 'curva Direita')]
        # df["angle_anomalia"]=0

        for i in df_CE.index:
            # Defina as coordenadas dos três pontos

            x1 = df['km-1'][i]
            y1 = df['y-1'][i]/varAngleE
            x2 = df['km'][i]
            y2 = df['y1'][i]/varAngleE
            x3 = df['km2'][i]
            y3 = df['y2'][i]/varAngleE

            # Calcule os vetores entre os pontos
            v1 = (x1 - x2, y1 - y2)
            v2 = (x3 - x2, y3 - y2)

            # Calcule os ângulos entre os vetores usando a função atan2
            angle1 = math.atan2(v1[1], v1[0])
            angle2 = math.atan2(v2[1], v2[0])

            # Calcule o ângulo entre os vetores subtraindo os ângulos
            angle = angle2 - angle1

            # Certifique-se de que o ângulo resultante esteja no intervalo de 0 a 2*pi
            if angle < 0:
                angle += 2 * math.pi

            # Converter o ângulo de radianos para graus, se necessário
            angle_degrees = math.degrees(angle)
            df['angle_anomalia'][i] = angle_degrees

            print(f"O ângulo entre os pontos é de {angle_degrees} graus.")

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Nivel de Fitting--------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"

        # encontrar Printar
        df['anomalia_desc'] = "N"

        df_f_anomalia_e = df.loc[(df['grau'] == 'curva Esquerda') & (
            df['x1'] <= Poste_X) & (df['x1'] > J1_X)]
        # df_f_anomalia_d =df.loc[(df['grau'] == 'curva Direita')& (df['x1'] > Poste_X_max) & (df['x1'] < J2_X)]
        df_f_anomalia_d = df.loc[(
            df['grau'] == 'curva Direita') & (df['x1'] < J2_X)]
        # df_f_anomalia_d = df_f_anomalia_d.drop(0)

        df_f_anomalia_e2_fit1 = df_f_anomalia_e.loc[(df['angle_anomalia'] < 175 - (
            165.5*VarAmplitudeE)) | (df['angle_anomalia'] > 185 + (185*VarAmplitudeE))]
        df_f_anomalia_d2_fit1 = df_f_anomalia_d.loc[(df['angle_anomalia'] < 175-(
            165.5*VarAmplitudeD)) | (df['angle_anomalia'] > 185 + (185*VarAmplitudeD))]

        df_f_anomalia_e2_fit2 = df_f_anomalia_e.loc[(df['angle_anomalia'] < 172.5-(
            172.5*VarAmplitudeE)) | (df['angle_anomalia'] > 187.5+(187.5*VarAmplitudeE))]
        df_f_anomalia_d2_fit2 = df_f_anomalia_d.loc[(df['angle_anomalia'] < 172.5-(
            172.5*VarAmplitudeD)) | (df['angle_anomalia'] > 187.5+(187.5*VarAmplitudeD))]

        df_f_anomalia_e2_fit3 = df_f_anomalia_e.loc[(df['angle_anomalia'] < 170-(
            170*VarAmplitudeE)) | (df['angle_anomalia'] > 190+(190*VarAmplitudeE))]
        df_f_anomalia_d2_fit3 = df_f_anomalia_d.loc[(df['angle_anomalia'] < 170-(
            170*VarAmplitudeD)) | (df['angle_anomalia'] > 190+(190*VarAmplitudeD))]

        df_f_anomalia_e2_fit4 = df_f_anomalia_e.loc[(df['angle_anomalia'] < 165.5-(
            165.5*VarAmplitudeE)) | (df['angle_anomalia'] > 192.5+(192.5*VarAmplitudeE))]
        df_f_anomalia_d2_fit4 = df_f_anomalia_d.loc[(df['angle_anomalia'] < 165.5-(
            165.5*VarAmplitudeD)) | (df['angle_anomalia'] > 192.5+(192.5*VarAmplitudeD))]

        # df.loc[(df['angle_anomalia'] >= 182) | (df['angle_anomalia'] <= 178) & (df['grau'] == 'curva Esquerda')& (df['x1'] < Poste_X) & (df['x1'] > J1_X), 'anomalia_desc'] = 'P1 Anomalia'
        # df.loc[(df['angle_anomalia'] >= 182) | (df['angle_anomalia'] <= 178) & (df['grau'] == 'curva Direita')& (df['x1'] > Poste_X_max) & (df['x1'] < J2_X), 'anomalia_desc'] = 'P1 Anomalia'
        lista_anomalias_fit1 = pd.concat(
            [df_f_anomalia_e2_fit1, df_f_anomalia_d2_fit1], axis=0)
        lista_anomalias_fit2 = pd.concat(
            [df_f_anomalia_e2_fit2, df_f_anomalia_d2_fit2], axis=0)
        lista_anomalias_fit3 = pd.concat(
            [df_f_anomalia_e2_fit3, df_f_anomalia_d2_fit3], axis=0)
        lista_anomalias_fit4 = pd.concat(
            [df_f_anomalia_e2_fit4, df_f_anomalia_d2_fit4], axis=0)

        fit_1 = len(lista_anomalias_fit1)
        fit_2 = len(lista_anomalias_fit2)
        fit_3 = len(lista_anomalias_fit3)
        fit_4 = len(lista_anomalias_fit4)

        fitenviado = fitting.get()

        if fitenviado == '1':
            fit_escolhido = lista_anomalias_fit1
            print("print fit1 ")
        elif fitenviado == '2':
            fit_escolhido = lista_anomalias_fit2
            print("print fit2 ")

        elif fitenviado == '3':
            fit_escolhido = lista_anomalias_fit3
            print("print fit3 ")

        elif fitenviado == '4':
            fit_escolhido = lista_anomalias_fit4
            print("print fit4 ")

        else:
            fit_escolhido = lista_anomalias_fit2
            print("fit padrao")

        print(
            f"Fit1: {fit_1}   df['angle_anomalia'] < 170)   | (df['angle_anomalia'] > 185)")
        print(
            f"Fit2: {fit_2}   df['angle_anomalia'] < 167.5) | (df['angle_anomalia'] > 187.5)")
        print(
            f"Fit3: {fit_3}   df['angle_anomalia'] < 165)   | (df['angle_anomalia'] > 190)")
        print(
            f"Fit4: {fit_4}   df['angle_anomalia'] < 162.5) | (df['angle_anomalia'] > 192.5")

        # fit_escolhido = lista_anomalias_fit3
        lista_anomalias = fit_escolhido

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Print Gráfico ----------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print(f"Print")

        import pandas as pd
        import matplotlib.pyplot as plt

        # Supondo que você já tenha um DataFrame chamado df
        # e as colunas e linhas especificadas

        # Primeiro, selecione as colunas desejadas
        colunas_x = df['x1']
        linhas = [
            'resistenciadoCabo',
            'resistenciaTotalMedida',
            'pontoAlarmeAbsoluto',
            'pontoAlarmeDaMedia'
        ]

        pontos = [

            'resistenciaTotalMedida',

        ]

        xponto = df['x1']
        yponto = df['y1']

        # Configure um gráfico de linhas
        plt.figure(figsize=(15, 7))  # Define o tamanho da figura

        x_anomalia = lista_anomalias['x1']
        y_anomalia = lista_anomalias['y1']
        x_kmname = lista_anomalias['KM_Name']

        KM_Name_cl = df['KM_Name']

        if str(varcheck) != "True":
            labelJ1 = "J1 KM: " + str(J1_Km)
            labelJ2 = "J2 KM: " + str(J2_Km)
            LabelPoste = "Poste KM: " + str(Poste_KM)
        else:
            labelJ1 = "J2 KM: " + str(J2_Km)
            labelJ2 = "J1 KM: " + str(J1_Km)
            LabelPoste = "Poste KM: " + str(Poste_KM)

        # Plote cada linha
        for linha in linhas:
            plt.plot(colunas_x, df[linha], label=linha)

        for ponto in pontos:
            cores = df["cor"].tolist()
            plt.scatter(colunas_x, df[pontos], label=ponto, c=cores)

        # print("chegou até aqui")
        plt.scatter(Poste_X, Poste_Y, label="Poste", color='green')
        texto = LabelPoste
        plt.annotate(texto, (Poste_X, Poste_Y), textcoords="offset points", xytext=(
            10, 10), ha='center', color='green')

        plt.scatter(J1_X, J1_Y, label=labelJ1, color='green')
        texto2 = labelJ1
        plt.annotate(texto2, (J1_X, J1_Y), textcoords="offset points",
                     xytext=(10, 10), ha='center', color='green', zorder=0)

        plt.scatter(J2_X, J2_Y, label=labelJ2, color='green')
        texto = labelJ2
        plt.annotate(texto, (J2_X, J2_Y), textcoords="offset points",
                     xytext=(10, 10), ha='center', color='green')

        # for anotate Anomalia:

        for i, (xi, yi, x_kmnamei) in enumerate(zip(x_anomalia, y_anomalia, x_kmname)):
            plt.annotate(f'Anomalia {str(x_kmnamei)}', (
                xi, yi), textcoords='offset points', xytext=(-55, 10), ha='center', color='red')

        # Anmalias
        plt.scatter(x_anomalia, y_anomalia, color='red')

        # plt.scatter(x_procurar, y_procurar, color='green')

        # Configurações do gráfico
        plt.xlabel('x1')  # Rótulo do eixo x
        plt.ylabel('Valor')  # Rótulo do eixo y
        plt.title('Gráfico de Linhas')  # Título do gráfico
        # plt.legend()  # Mostra a legenda
        plt.grid(True)  # Mostra as grades de fundo
        # Defina os rótulos personalizados e opcionalmente gire-os
        plt.xticks(colunas_x, KM_Name_cl, rotation=90)

        plt.grid(False)
        # plt.axis('off')
        print("Equipamento:", equipamentoapp)
        print("Poste:", posteapp)
        print("J1:", j1app)
        print("J2:", j2app)
        print("Data de Início:", data_inicioapp)
        print("Hora de Início:", hora_inicioapp)
        print("Minuto de Início:", minuto_inicioapp)
        print("Data de Fim:", data_fimapp)
        print("Hora de Fim:", hora_fimapp)
        print("Minuto de Fim:", minuto_fimapp)
        print("T1:", T1_app)

        # Exibe o gráfico
        plt.show()
    except Exception as erro:
        tk.messagebox.showerror(
            "Erro", f"Erro em algum parâmetro do Algoritimo, por favor utilizar o Modo Manual!")


def Localizar_Passagem():
    try:

        # -----------------------------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Input---------------------------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------------------------"
        global dfcorte
        print("keylog")
        print(keylog)
        equipamentoapp = entrada_equipamento.get()
        posteapp = entrada_poste.get()
        j1app = entrada_j1.get()
        j2app = entrada_j2.get()
        data_inicioapp = entrada_data_inicio.get()
        hora_inicioapp = entrada_hora_inicio.get()
        minuto_inicioapp = entrada_minuto_inicio.get()
        data_fimapp = entrada_data_fim.get()
        hora_fimapp = entrada_hora_fim.get()
        minuto_fimapp = entrada_minuto_fim.get()
        T1_app = entrada_T1.get()

        print("agregado2")
        # print(agregado2)
        if (keylog == 1):

            import warnings

            from datetime import datetime, timedelta

            # Data de início no formato original
            data_inicio_str = data_inicioapp + " " + \
                hora_inicioapp + ":" + minuto_inicioapp
            print(data_inicio_str)

            # Converter para objeto de data e hora
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_inicio = data_inicio + timedelta(hours=3)

            # Converter para o formato desejado
            data_inicio_formatada = data_inicio.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_inicio_formatada)

            # Data de início no formato original
            data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
            print(data_final_str)

            # Converter para objeto de data e hora
            data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_final = data_final + timedelta(hours=3)

            # Converter para o formato desejado
            data_final_formatada = data_final.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_final_formatada)

            J1_Km = int(j1app)
            J2_Km = int(j2app)
            Poste_KM = int(posteapp)
            # Data_inicio = "2023-09-13T09:25:00.000Z"
            # Data_fim = "2023-09-13T09:51:59.999Z"
            Data_inicio = data_inicio_formatada
            Data_fim = data_final_formatada
            # Placa = "1.470C.49EA.EBA0"
            Placa = equipamentoapp

            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Conexão Elastic---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            import warnings

            # Suprimir todos os warnings
            warnings.filterwarnings('ignore')

            print(f"Conexão Elastic")
            from elasticsearch import Elasticsearch
            from datetime import datetime, timedelta
            import pandas as pd

            # Create the client instance
            es = Elasticsearch(
                "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

            # Successful response!
            es.info()

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Search Elastic----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Search Elastic")
            index_name = "rumo-supervisorio-dds"
            doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

            agregado = pd.DataFrame()

            # Teste
            # anomalia 1
            # Teste

            # Teste
            query = {
                "query": {
                    "bool": {
                        "filter": [
                            {"term": {"state.reported.eventType": "54"}},
                            {"term": {"state.reported.dds.keyword": ""+Placa+""}},
                            {"term": {"state.reported.collectOrigin.keyword": ""+T1_app+""}},

                            {
                                "range": {
                                    "state.reported.device_data": {
                                        "gte": ""+Data_inicio+"",
                                        "lte": ""+Data_fim+""
                                    }
                                }
                            }
                        ]
                    }
                },
                "size": 1000  # Define o tamanho da página para 100 resultados
            }

            try:
                # Execute a consulta
                result = es.search(index=index_name, body=query, timeout="30s")

                # Itere pelos documentos correspondentes
                for hit in result['hits']['hits']:

                    df6 = pd.DataFrame(hit['_source'])
                    json = df6['state']['reported']
                    df7 = pd.DataFrame([json], index=['row1'])

                    # print("------------------------------------------")
                    agregado = pd.concat([agregado, df7], ignore_index=True)

            except Exception as e:
                print(f"Ocorreu um erro durante a consulta: {str(e)}")

            # agregado

            print(f"Search Elastic fim")

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Ajustes Bases-----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Ajustes Bases")

            colunas_desejadas = [
                'resistenciadoCabo',
                'resistenciaTotalMedida',
                'pontoAlarmeAbsoluto',
                'pontoAlarmeDaMedia',
                'device_data',
            ]

            dfagragado = agregado[colunas_desejadas]
            # dfagragado
        else:
            import pandas as pd
            dfagragado = agregado2
            dfagragado.sort_values(by='device_data')
            # agregado2 = dfagragado
            print('masseratti')
            print(dfagragado)
            data_inicioapp = entrada_data_inicio.get()
            hora_inicioapp = entrada_hora_inicio.get()
            minuto_inicioapp = entrada_minuto_inicio.get()
            data_fimapp = entrada_data_fim.get()
            hora_fimapp = entrada_hora_fim.get()
            minuto_fimapp = entrada_minuto_fim.get()
            dfagragado['resistenciadoCabo'] = dfagragado['resistenciadoCabo'].astype(
                float)
            dfagragado['resistenciaTotalMedida'] = dfagragado['resistenciaTotalMedida'].astype(
                float)
            dfagragado['pontoAlarmeAbsoluto'] = dfagragado['pontoAlarmeAbsoluto'].astype(
                float)
            dfagragado['pontoAlarmeDaMedia'] = dfagragado['pontoAlarmeDaMedia'].astype(
                float)

            # agregado2['data'] = pd.to_datetime(agregado2['checkedAt'])

            data_inicio = data_inicioapp+' '+hora_inicioapp+':'+minuto_inicioapp
            data_fim = data_fimapp+' '+hora_fimapp+':'+minuto_fimapp
            print('dtinicio')
            print(data_inicio)
            print('dtfim')
            print(data_fim)

            print('Tesla1')
            dfagragado = dfagragado.loc[(dfagragado['data'] >= data_inicio) & (
                dfagragado['data'] <= data_fim)]
            print('Tesla2')
            print(dfagragado)

        print('Miata01')
        import pandas as pd
        import numpy as np
        print('Miata02')
        dfagragado['data_com_fuso'] = pd.to_datetime(dfagragado['device_data'])
        dfagragado['data_sem_fuso'] = dfagragado['data_com_fuso'].dt.tz_localize(
            None)

        print('Miata03')
        dfagragado['intdt'] = pd.to_numeric(
            dfagragado['data_sem_fuso'], downcast='integer')

        print('Miata04')
        df = dfagragado.sort_values(by='data_sem_fuso').reset_index()

        # -----------------------------------------------------------------------------------------------------------------------"
        # -----------------------------------------------------------Valorando x-----------------------------------------------"
        # -----------------------------------------------------------------------------------------------------------------------"
        print('Miata05')
        df['x1'] = df['intdt']
        df['y1'] = df['resistenciaTotalMedida']
        df['x2'] = 0
        df['y2'] = 0
        df['x-1'] = 0
        df['y-1'] = 0

        import matplotlib.pyplot as plt
        from matplotlib.widgets import SpanSelector

        # Dados de exemplo
        x = df['x1']

        linhas = [
            'resistenciadoCabo',
            'resistenciaTotalMedida',
            'pontoAlarmeAbsoluto',
            'pontoAlarmeDaMedia'
        ]

        if (keylog == 1):
            y = df[['resistenciadoCabo', 'resistenciaTotalMedida',
                    'pontoAlarmeAbsoluto', 'pontoAlarmeDaMedia']]
            ymed = y['resistenciaTotalMedida']
        else:
            y = df['resistenciaTotalMedida']
            ymed = y
            # x = x.tolist()
            # print(x)
            # y = y.tolist()
            # print(y)

        print('Miata06')
        print()

        # Variáveis para armazenar os pontos de início e fim do zoom
        zoom_start = None
        zoom_end = None
        print('Miata07')
        # Função a ser chamada quando o intervalo é selecionado

        def onselect(xmin, xmax):
            print('Miata08')
            from tkinter import messagebox
            global zoom_start, zoom_end
            zoom_start = xmin
            zoom_end = xmax

            ax.set_xlim(xmin, xmax)
            ax.fill_between(x, 0, ymed, where=(x >= xmin) & (
                x <= xmax), alpha=0.5, facecolor='red')
            fig.canvas.draw()

            print(f'Ponto de início do zoom: {zoom_start}')
            print(f'Ponto de fim do zoom: {zoom_end}')
            print('Miata09')
            zoomapp1.delete(0, tk.END)
            zoomapp1.insert(0, zoom_start/10000000000000)
            zoomapp2.delete(0, tk.END)
            zoomapp2.insert(0, zoom_end/10000000000000)
            plt.close()

            # messagebox.showinfo("Periodo selecionado", f"Periodo selecionado, Escolha o tipo de Análise Manual ou Automática")
        print('Miata10')
        # Cria o gráfico
        fig, ax = plt.subplots(figsize=(18, 8))
        # Define os rótulos do eixo x como 'device_data' a cada 10 valores
        rotulos_a_cada = 10
        ax.set_xticks(x[::rotulos_a_cada])
        ax.set_xticklabels(df['data_sem_fuso']
                           [::rotulos_a_cada], rotation=45, ha='right')
        fig.tight_layout()
        ax.plot(x, y)

        # Cria um seletor de intervalo
        span = SpanSelector(ax, onselect, 'horizontal', useblit=True)

        dfcorte = df
        print("Fim DFCORTE")

        plt.show()
        tk.messagebox.showinfo(
            "Sucesso", "Sucesso! Selecione a forma de Analise! Manual ou Automática!")

        return dfcorte

    except Exception as erro:
        tk.messagebox.showerror(
            "Erro", f"Verifique se as informações de Data | Placa | J1 | Poste | J2 . Estão preenchidas corretamente!")


def Achar_pontos():
    try:
        from elasticsearch import Elasticsearch
        from datetime import datetime, timedelta
        import pandas as pd
        placabusca = entrada_equipamento.get()
    # Create the client instance
        es = Elasticsearch(
            "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

    # Successful response!
        es.info()
        import pandas as pd

        # Initialize an empty DataFrame
        dtqfinal = pd.DataFrame()

        query = {
            "query": {
                "bool": {
                    "filter": [
                        # {"term": {"state.reported.eventType": "54"}},
                        {"term": {"attributes.dds.keyword": ""+placabusca+""}},
                    ]
                }
            },
            "size": 100  # Define o tamanho da página para 100 resultados
        }

        index_name = "rumo-supervisorio-dds-cadastro"
        result = es.search(index=index_name, body=query, timeout="30s")

        # Itere pelos documentos correspondentes
        for hit in result['hits']['hits']:
            # print(hit)
            df6 = pd.DataFrame(hit['_source'])
            dtq = pd.DataFrame(df6['attributes']['subDevices'])
            dtq = dtq['dtq']['T1']
            dtq = pd.DataFrame([dtq], index=['row1'])
            dtq = dtq[['kmJumper1', 'kmJumper2', 'meterJumper1',
                       'meterJumper2', 'kmDTQ', 'meterDTQ']]
            # Append the DataFrame to 'agregado'
            dtqfinal = pd.concat([dtqfinal, dtq], ignore_index=True)

        # Print the 'agregado' DataFrame
        dtqfinal["placa"] = placabusca

        kmJumper1 = dtq.loc['row1', 'kmJumper1']
        meterJumper1 = dtq.loc['row1', 'meterJumper1']
        kmJumper2 = dtq.loc['row1', 'kmJumper2']
        meterJumper2 = dtq.loc['row1', 'meterJumper2']
        kmDTQ = dtq.loc['row1', 'kmDTQ']
        meterDTQ = dtq.loc['row1', 'meterDTQ']

        Jumper1_resultado = kmJumper1 * 1000 + meterJumper1
        Jumper2_resultado = kmJumper2 * 1000 + meterJumper2
        kmDTQ_resultado = kmDTQ * 1000 + meterDTQ

        entrada_poste.delete(0, tk.END)
        entrada_poste.insert(0, kmDTQ_resultado)

        entrada_j1.delete(0, tk.END)
        entrada_j1.insert(0, Jumper1_resultado)

        entrada_j2.delete(0, tk.END)
        entrada_j2.insert(0, Jumper2_resultado)

        lbl = entrada_j1.get()

        print("fora")
        print(lbl)

    except Exception as erro:
        # print("entrou")
        # print(lbl)
        tk.messagebox.showerror("Erro", f"Não encontrado plano no portal DTQ")


def Manual():
    # -----------------------------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Input---------------------------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------------------------"
    equipamentoapp = entrada_equipamento.get()
    posteapp = entrada_poste.get()
    j1app = entrada_j1.get()
    j2app = entrada_j2.get()
    data_inicioapp = entrada_data_inicio.get()
    hora_inicioapp = entrada_hora_inicio.get()
    minuto_inicioapp = entrada_minuto_inicio.get()
    data_fimapp = entrada_data_fim.get()
    hora_fimapp = entrada_hora_fim.get()
    minuto_fimapp = entrada_minuto_fim.get()

    import warnings

    from datetime import datetime, timedelta

    # Data de início no formato original
    data_inicio_str = data_inicioapp + " " + \
        hora_inicioapp + ":" + minuto_inicioapp
    print(data_inicio_str)

    # Converter para objeto de data e hora
    data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_inicio = data_inicio + timedelta(hours=3)

    # Converter para o formato desejado
    data_inicio_formatada = data_inicio.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_inicio_formatada)

    # Data de início no formato original
    data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
    print(data_final_str)

    # Converter para objeto de data e hora
    data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

    # Acrescentar 3 horas
    data_final = data_final + timedelta(hours=3)

    # Converter para o formato desejado
    data_final_formatada = data_final.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    print(data_final_formatada)

    J1_Km = int(j1app)
    J2_Km = int(j2app)
    Poste_KM = int(posteapp)
    # Data_inicio = "2023-09-13T09:25:00.000Z"
    # Data_fim = "2023-09-13T09:51:59.999Z"
    Data_inicio = data_inicio_formatada
    Data_fim = data_final_formatada
    # Placa = "1.470C.49EA.EBA0"
    Placa = equipamentoapp

    # -----------------------------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Conexão Elastic---------------------------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------------------------"
    import warnings

    # Suprimir todos os warnings
    warnings.filterwarnings('ignore')

    print(f"Conexão Elastic")
    from elasticsearch import Elasticsearch
    from datetime import datetime, timedelta
    import pandas as pd

    # Create the client instance
    es = Elasticsearch(
        "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

    # Successful response!
    es.info()

    # -----------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Search Elastic----------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------"
    print(f"Search Elastic")
    index_name = "rumo-supervisorio-dds"
    doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

    agregado = pd.DataFrame()

    # Teste
    # anomalia 1
    # Teste

    # Teste
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"state.reported.eventType": "54"}},
                    {"term": {"state.reported.dds.keyword": ""+Placa+""}},

                    {
                        "range": {
                            "state.reported.device_data": {
                                "gte": ""+Data_inicio+"",
                                "lte": ""+Data_fim+""
                            }
                        }
                    }
                ]
            }
        },
        "size": 1000  # Define o tamanho da página para 100 resultados
    }

    try:
        # Execute a consulta
        result = es.search(index=index_name, body=query, timeout="30s")

        # Itere pelos documentos correspondentes
        for hit in result['hits']['hits']:

            df6 = pd.DataFrame(hit['_source'])
            json = df6['state']['reported']
            df7 = pd.DataFrame([json], index=['row1'])

            # print("------------------------------------------")
            agregado = pd.concat([agregado, df7], ignore_index=True)

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta: {str(e)}")

    # agregado

    print(f"Search Elastic fim")

    # -----------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Ajustes Bases-----------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------"
    print(f"Ajustes Bases")

    colunas_desejadas = [
        'resistenciadoCabo',
        'resistenciaTotalMedida',
        'pontoAlarmeAbsoluto',
        'pontoAlarmeDaMedia',
        'device_data',
    ]

    VarAjuste2 = 0.75

    dfagragado = agregado[colunas_desejadas]

    zoomapp1_var = float(zoomapp1.get())
    zoomapp2_var = float(zoomapp2.get())
    # dfagragado

    import pandas as pd
    import numpy as np

    dfagragado['data_com_fuso'] = pd.to_datetime(dfagragado['device_data'])
    dfagragado['data_sem_fuso'] = dfagragado['data_com_fuso'].dt.tz_localize(
        None)

    dfagragado['intdt'] = pd.to_numeric(
        dfagragado['data_sem_fuso'], downcast='integer')

    df = dfagragado.sort_values(by='data_sem_fuso').reset_index()

    df['x1'] = df['intdt']/10000000000000*VarAjuste2

    df = df.loc[(df['x1'] >= zoomapp1_var*VarAjuste2) &
                (df['x1'] <= zoomapp2_var*VarAjuste2)]

    # -----------------------------------------------------------------------------------------------------------------------"
    # -----------------------------------------------------------Valorando x-----------------------------------------------"
    # -----------------------------------------------------------------------------------------------------------------------"

    df['x1'] = df['intdt']
    df['y1'] = df['resistenciaTotalMedida']
    df['x2'] = 0
    df['y2'] = 0
    df['x-1'] = 0
    df['y-1'] = 0

    import matplotlib.pyplot as plt
    from matplotlib.widgets import SpanSelector

    # Dados de exemplo
    x = df['x1']

    linhas = [
        'resistenciadoCabo',
        'resistenciaTotalMedida',
        'pontoAlarmeAbsoluto',
        'pontoAlarmeDaMedia'
    ]

    y = df['resistenciaTotalMedida']

    # Variáveis para armazenar os pontos de início e fim do zoom
    zoom_start = None
    zoom_end = None

    # Função a ser chamada quando o intervalo é selecionado
    def onselect(xmin, xmax):
        global zoom_start, zoom_end
        zoom_start = xmin
        zoom_end = xmax

        ax.set_xlim(xmin, xmax)
        ax.fill_between(x, 0, y, where=(x >= xmin) & (
            x <= xmax), alpha=0.5, facecolor='red')
        fig.canvas.draw()

        print(f'Ponto de início do zoom: {zoom_start}')
        print(f'Ponto de fim do zoom: {zoom_end}')

        zoomapp1.delete(0, tk.END)
        zoomapp1.insert(0, zoom_start/10000000000000)
        zoomapp2.delete(0, tk.END)
        zoomapp2.insert(0, zoom_end/10000000000000)

    # Cria o gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Cria um seletor de intervalo
    span = SpanSelector(ax, onselect, 'horizontal', useblit=True)

    plt.show()


def Manual2():
    # try:

    import tkinter as tk
    from tkinter import messagebox
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    class InteractiveGraph:
        def __init__(self, root):
            print("keylog")
            print(keylog)
            print("Ferrari1")
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Input---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            equipamentoapp = entrada_equipamento.get()
            posteapp = entrada_poste.get()
            j1app = entrada_j1.get()
            j2app = entrada_j2.get()
            data_inicioapp = entrada_data_inicio.get()
            hora_inicioapp = entrada_hora_inicio.get()
            minuto_inicioapp = entrada_minuto_inicio.get()
            data_fimapp = entrada_data_fim.get()
            hora_fimapp = entrada_hora_fim.get()
            minuto_fimapp = entrada_minuto_fim.get()
            T1_app = entrada_T1.get()
            print("Ferrari2")

            import warnings

            from datetime import datetime, timedelta

            # Data de início no formato original
            data_inicio_str = data_inicioapp + " " + \
                hora_inicioapp + ":" + minuto_inicioapp
            print(data_inicio_str)
            print("Ferrari3")

            # Converter para objeto de data e hora
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_inicio = data_inicio + timedelta(hours=3)
            print("Ferrari4")

            # Converter para o formato desejado
            data_inicio_formatada = data_inicio.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_inicio_formatada)

            # Data de início no formato original
            data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
            print(data_final_str)
            print("Ferrari5")

            # Converter para objeto de data e hora
            data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_final = data_final + timedelta(hours=3)
            print("Ferrari6")

            # Converter para o formato desejado
            data_final_formatada = data_final.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_final_formatada)
            print("Ferrari7")

            J1_Km = int(j1app)
            J2_Km = int(j2app)
            Poste_KM = int(posteapp)
            # Data_inicio = "2023-09-13T09:25:00.000Z"
            # Data_fim = "2023-09-13T09:51:59.999Z"
            Data_inicio = data_inicio_formatada
            Data_fim = data_final_formatada
            # Placa = "1.470C.49EA.EBA0"
            Placa = equipamentoapp
            print("Ferrari8")

            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Conexão Elastic---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            import warnings

            # Suprimir todos os warnings
            warnings.filterwarnings('ignore')

            print(f"Conexão Elastic")
            from elasticsearch import Elasticsearch
            from datetime import datetime, timedelta
            import pandas as pd

            if (keylog == 1):

                # Create the client instance
                es = Elasticsearch(
                    "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

                # Successful response!
                es.info()

                # -----------------------------------------------------------------------------------------------------------------------"
                # -----------------------------------------------------------Search Elastic----------------------------------------------"
                # -----------------------------------------------------------------------------------------------------------------------"
                print(f"Search Elastic")
                index_name = "rumo-supervisorio-dds"
                doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

                agregado = pd.DataFrame()

                # Teste
                # anomalia 1
                # Teste

                # Teste
                query = {
                    "query": {
                        "bool": {
                            "filter": [
                                {"term": {"state.reported.eventType": "54"}},
                                {"term": {"state.reported.dds.keyword": ""+Placa+""}},
                                {"term": {
                                    "state.reported.collectOrigin.keyword": ""+T1_app+""}},


                                {
                                    "range": {
                                        "state.reported.device_data": {
                                            "gte": ""+Data_inicio+"",
                                            "lte": ""+Data_fim+""
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "size": 1000  # Define o tamanho da página para 100 resultados
                }

                try:
                    # Execute a consulta
                    result = es.search(
                        index=index_name, body=query, timeout="30s")

                    # Itere pelos documentos correspondentes
                    for hit in result['hits']['hits']:

                        df6 = pd.DataFrame(hit['_source'])
                        json = df6['state']['reported']
                        df7 = pd.DataFrame([json], index=['row1'])

                        # print("------------------------------------------")
                        agregado = pd.concat(
                            [agregado, df7], ignore_index=True)

                except Exception as e:
                    print(f"Ocorreu um erro durante a consulta: {str(e)}")
            else:
                print("Porche911")
                agregado = dfcorte
                print("Porche912")
                print(dfcorte)
                # massserati2

            # agregado

            print(f"Search Elastic fim")

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Ajustes Bases-----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Ajustes Bases")

            colunas_desejadas = [
                'resistenciadoCabo',
                'resistenciaTotalMedida',
                'pontoAlarmeAbsoluto',
                'pontoAlarmeDaMedia',
                'device_data',
            ]

            VarAjuste2 = 0.75

            dfagragado = agregado[colunas_desejadas]

            zoomapp1_var = float(zoomapp1.get())
            zoomapp2_var = float(zoomapp2.get())
            # dfagragado

            import pandas as pd
            import numpy as np

            dfagragado['data_com_fuso'] = pd.to_datetime(
                dfagragado['device_data'])
            dfagragado['data_sem_fuso'] = dfagragado['data_com_fuso'].dt.tz_localize(
                None)

            dfagragado['intdt'] = pd.to_numeric(
                dfagragado['data_sem_fuso'], downcast='integer')

            df = dfagragado.sort_values(by='data_sem_fuso').reset_index()

            df['x1'] = df['intdt']/10000000000000*VarAjuste2

            df = df.loc[(df['x1'] >= zoomapp1_var*VarAjuste2) &
                        (df['x1'] <= zoomapp2_var*VarAjuste2)]

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Valorando x-----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"

            df['x1'] = df['intdt']
            df['y1'] = df['resistenciaTotalMedida']
            df['x2'] = 0
            df['y2'] = 0
            df['x-1'] = 0
            df['y-1'] = 0

            global dfcorte2

            dfcorte2 = df
            import matplotlib.pyplot as plt
            from matplotlib.widgets import SpanSelector

            # Dados de exemplo
            x = df['x1']

            linhas = [
                'resistenciadoCabo',
                'resistenciaTotalMedida',
                'pontoAlarmeAbsoluto',
                'pontoAlarmeDaMedia'
            ]
            y = df['resistenciaTotalMedida']

            self.root = root
            self.root.title("Gráfico Interativo")
            self.fig = Figure(figsize=(15, 7))  # , dpi=100
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, master=root)
            self.canvas.get_tk_widget().pack()
            self.canvas.mpl_connect('button_press_event', self.on_click)
            self.clicked_points = []

            anotacoes = [
                "1 Click Selecione J1",
                "2 Click Selecione Poste",
                "3 Click Selecione J2",
                "4 Click Selecione Fratura"
                # Adicione mais explicações conforme necessário
            ]

# Adicionar as anotações à direita do gráfico
            for i, texto in enumerate(anotacoes):
                self.ax.text(1.05, 0.9 - i * 0.1, texto, transform=self.ax.transAxes,
                             fontsize=10, verticalalignment='top')
            rotulos_a_cada = 2

            self.ax.set_xticks(x[::rotulos_a_cada])
            # Ajusta a rotação e alinhamento dos rótulos
            self.ax.set_xticklabels(
                df['data_sem_fuso'][::rotulos_a_cada], rotation=45, ha='right')

            # Ajusta a posição dos rótulos do eixo x
            self.fig.tight_layout()

            # Adicione um gráfico de linha inicial (dados fictícios)
            self.ax.plot(x, y, 'b-')
            self.canvas.draw()

        def on_click(self, event):
            if event.inaxes is not None:

                x, y = event.xdata, event.ydata

                self.clicked_points.append((x, y))
                ponto = len(self.clicked_points)
                lista = ["a", "J1", "Poste", "J2", "pt Fratura1",
                         "pt Fratura2", "pt Fratura3", "pt Fratura4", "pt Fratura5"]
                listap = lista[ponto]
                self.ax.plot(x, y, 'ro')  # Marca o ponto no gráfico
                self.ax.annotate(
                    f'Ponto {listap}', (x, y), textcoords="offset points", xytext=(5, 5), ha='center')
                self.canvas.draw()

        def clear_points(self):
            # Limpa os pontos salvos e as anotações no gráfico
            for annotation in self.ax.texts:
                annotation.remove()  # Remove a anotação

            for point in self.clicked_points:
                x, y = point
                # Sobrescreve o ponto com a cor de fundo do gráfico
                self.ax.plot(x, y, 'wo')

            self.clicked_points = []
            self.saved_points = []
            anotacoes = [
                "1 Click Selecione J1",
                "2 Click Selecione Poste",
                "3 Click Selecione J2",
                "4 Click Selecione Fratura"
                # Adicione mais explicações conforme necessário
            ]

            # Adicionar as anotações à direita do gráfico
            for i, texto in enumerate(anotacoes):
                self.ax.text(1.05, 0.9 - i * 0.1, texto, transform=self.ax.transAxes,
                             fontsize=10, verticalalignment='top')

            self.canvas.draw()

        def save_points(self):

            print("dfcorte2")

            print(dfcorte2)

            self.saved_points = self.clicked_points
            minha_tupla = self.saved_points
            listpoint = minha_tupla[:8]
            print(f"QTD Lista: { len(listpoint)}")
            if len(listpoint) < 9:
                ajustelen = len(listpoint) - 9
            else:
                ajustelen = 0

            print(self.saved_points)

            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Input---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            equipamentoapp = entrada_equipamento.get()
            posteapp = entrada_poste.get()
            j1app = entrada_j1.get()
            j2app = entrada_j2.get()
            data_inicioapp = entrada_data_inicio.get()
            hora_inicioapp = entrada_hora_inicio.get()
            minuto_inicioapp = entrada_minuto_inicio.get()
            data_fimapp = entrada_data_fim.get()
            hora_fimapp = entrada_hora_fim.get()
            minuto_fimapp = entrada_minuto_fim.get()
            T1_app = entrada_T1.get()

            import warnings

            from datetime import datetime, timedelta

            # Data de início no formato original
            data_inicio_str = data_inicioapp + " " + \
                hora_inicioapp + ":" + minuto_inicioapp
            print(data_inicio_str)

            # Converter para objeto de data e hora
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_inicio = data_inicio + timedelta(hours=3)

            # Converter para o formato desejado
            data_inicio_formatada = data_inicio.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_inicio_formatada)

            # Data de início no formato original
            data_final_str = data_fimapp + " " + hora_fimapp + ":" + minuto_fimapp
            print(data_final_str)

            # Converter para objeto de data e hora
            data_final = datetime.strptime(data_final_str, "%d/%m/%Y %H:%M")

            # Acrescentar 3 horas
            data_final = data_final + timedelta(hours=3)

            # Converter para o formato desejado
            data_final_formatada = data_final.strftime(
                "%Y-%m-%dT%H:%M:%S.999Z")

            print(data_final_formatada)

            J1_Km = int(j1app)
            J2_Km = int(j2app)
            Poste_KM = int(posteapp)
            # Data_inicio = "2023-09-13T09:25:00.000Z"
            # Data_fim = "2023-09-13T09:51:59.999Z"
            Data_inicio = data_inicio_formatada
            Data_fim = data_final_formatada
            # Placa = "1.470C.49EA.EBA0"
            Placa = equipamentoapp

            # -----------------------------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Conexão Elastic---------------------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------------------------"
            import warnings

            # Suprimir todos os warnings
            warnings.filterwarnings('ignore')

            if (keylog == 1):

                print(f"Conexão Elastic")
                from elasticsearch import Elasticsearch
                from datetime import datetime, timedelta
                import pandas as pd

                # Create the client instance
                es = Elasticsearch(
                    "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

                # Successful response!
                es.info()

                # -----------------------------------------------------------------------------------------------------------------------"
                # -----------------------------------------------------------Search Elastic----------------------------------------------"
                # -----------------------------------------------------------------------------------------------------------------------"
                print(f"Search Elastic")
                index_name = "rumo-supervisorio-dds"
                doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

                agregado = pd.DataFrame()

                # Teste
                # anomalia 1
                # Teste
                # Lamborguine
                # Teste

                query = {
                    "query": {
                        "bool": {
                            "filter": [
                                {"term": {"state.reported.eventType": "54"}},
                                {"term": {"state.reported.dds.keyword": ""+Placa+""}},
                                {"term": {
                                    "state.reported.collectOrigin.keyword": ""+T1_app+""}},

                                {
                                    "range": {
                                        "state.reported.device_data": {
                                            "gte": ""+Data_inicio+"",
                                            "lte": ""+Data_fim+""
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    "size": 1000  # Define o tamanho da página para 100 resultados
                }

                try:
                    # Execute a consulta
                    result = es.search(
                        index=index_name, body=query, timeout="30s")

                    # Itere pelos documentos correspondentes
                    for hit in result['hits']['hits']:

                        df6 = pd.DataFrame(hit['_source'])
                        json = df6['state']['reported']
                        df7 = pd.DataFrame([json], index=['row1'])

                        # print("------------------------------------------")
                        agregado = pd.concat(
                            [agregado, df7], ignore_index=True)

                except Exception as e:
                    print(f"Ocorreu um erro durante a consulta: {str(e)}")
            else:
                agregado = dfcorte2

            # agregado

            print(f"Search Elastic fim")

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Ajustes Bases-----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Ajustes Bases")

            colunas_desejadas = [
                'resistenciadoCabo',
                'resistenciaTotalMedida',
                'pontoAlarmeAbsoluto',
                'pontoAlarmeDaMedia',
                'device_data',
            ]

            dfagragado = agregado[colunas_desejadas]
            # dfagragado

            import pandas as pd
            import numpy as np

            dfagragado['data_com_fuso'] = pd.to_datetime(
                dfagragado['device_data'])
            dfagragado['data_sem_fuso'] = dfagragado['data_com_fuso'].dt.tz_localize(
                None)

            dfagragado['intdt'] = pd.to_numeric(
                dfagragado['data_sem_fuso'], downcast='integer')

            df = dfagragado.sort_values(by='data_sem_fuso').reset_index()

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Valorando x-----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"

            df['x1'] = df['intdt']
            df['y1'] = df['resistenciaTotalMedida']
            df['x2'] = 0
            df['y2'] = 0
            df['x-1'] = 0
            df['y-1'] = 0

            zoomapp1_var = float(zoomapp1.get())
            zoomapp2_var = float(zoomapp2.get())

            VarAjuste2 = 0.75

            for x in df.index:
                # print(x)
                maxx = len(df)-1
                if 0 < x < maxx:
                    df['x2'][x] = df['intdt'][x+1]
                    df['y2'][x] = df['resistenciaTotalMedida'][x+1]
                    df['x-1'][x] = df['intdt'][x-1]
                    df['y-1'][x] = df['resistenciaTotalMedida'][x-1]

            df['incl'] = 0
            df['x1'] = df['intdt']/10000000000000*VarAjuste2
            df['x2'] = df['x2']/10000000000000*VarAjuste2
            df['x-1'] = df['x-1']/10000000000000*VarAjuste2
            df['grau'] = 'blank'
            df['cor'] = 'blue'

            # if zoomapp1_var != '':#
            print(df['x1'])
            print("zoomapp1_var")
            print(float(zoomapp1_var)*VarAjuste2)

            print("zoomapp2_var")
            print(float(zoomapp2_var)*VarAjuste2)
            print("----")

            # if zoomapp2_var != '':

            print("----------------Filtrar")

            df = df.loc[(df['x1'] >= zoomapp1_var*VarAjuste2) &
                        (df['x1'] <= zoomapp2_var*VarAjuste2)]

            agregado = df
            print(df['x1'])
            print(zoomapp1_var)

            maxx = len(df)-1

            J1_X = listpoint[0][0]/10000000000000*VarAjuste2
            J1_Y = listpoint[0][1]
            print("?")

            # J2 localizar

            # Aobaaa

            J2_X = listpoint[2][0]/10000000000000*VarAjuste2
            J2_Y = listpoint[2][1]

            Poste_X = listpoint[1][0]/10000000000000*VarAjuste2
            Poste_Y = listpoint[1][1]
            print("//")

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Int para KM ------------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"KM")

            df['m'] = 0
            df['b'] = 0
            df['cof'] = 0
            df['b2'] = 0
            df['cof2'] = 0

            print("#")

            J1_int = J1_X
            J2_int = J2_X
            Poste_int = Poste_X
            print("$")

            a_int = Poste_int - J1_int
            a_km = Poste_KM - J1_Km

            a_int2 = Poste_int - J2_int
            a_km2 = Poste_KM - J2_Km
            print("$")

            df['b'] = df['x1'] - J1_int
            df['cof'] = df['b'] / a_int * -1
            df['m'] = J1_Km + a_km * df['cof']
            print("*")

            df['m']

            a_km_inverter = Poste_KM - J2_Km
            a_km2_inverter = J1_Km - Poste_KM
            print("**")

            # flag inverter
            varcheck = checkbox_var.get()
            print("varCheck" + str(varcheck))
            print("***")

            if str(varcheck) == "True":
                inverter = "Sim"
            else:
                inverter = "Não"
            print("****")

            print("else inverter")
            if inverter == "Não":

                for i in df.index:
                    if df['x1'][i] <= Poste_int:

                        df['b'][i] = df['x1'][i] - J1_int
                        df['cof'][i] = df['b'][i] / a_int
                        df['m'][i] = J1_Km + (a_km * df['cof'][i])

                    else:

                        df['b2'][i] = df['x1'][i] - Poste_int
                        df['cof2'][i] = df['b2'][i] / a_int2
                        df['m'][i] = Poste_KM + (a_km2 * df['cof2'][i])
                        print("****$")

            else:

                for i in df.index:
                    if df['x1'][i] <= Poste_int:

                        df['b'][i] = df['x1'][i] - J1_int
                        df['cof'][i] = df['b'][i] / a_int
                        df['m'][i] = J2_Km + (a_km_inverter * df['cof'][i])

                    else:

                        df['b2'][i] = df['x1'][i] - Poste_int
                        df['cof2'][i] = df['b2'][i] / a_int2
                        df['m'][i] = Poste_KM - \
                            (a_km2_inverter * df['cof2'][i])
                        print("****$$")

            df['km'] = round(df['m']/1000, 3)

            import pandas as pd

            print("transforamar km")

            # Crie um DataFrame de exemplo com uma coluna de quilometragem

            # Função para formatar uma única entrada de quilometragem
            def aplicar_mascara(quilometragem):
                parte_inteira = int(quilometragem)
                parte_decimal = int((quilometragem - parte_inteira) * 1000)
                return f"{parte_inteira:03d}+{parte_decimal:03d}"

            # Aplicar a função para formatar a coluna inteira
            df['KM_Name'] = df['km'].apply(aplicar_mascara)

            print(listpoint)

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Lista KM anomalia ----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"

            print("anomalia valid")

            varlen = (6 + ajustelen)*-1

            print('ajustelen')
            print(ajustelen)

            print('varlen')
            print(varlen)

            lista_anomalias = listpoint[varlen:]

            print(lista_anomalias)

            colunas_lista_anomalias = ['x1', "Coluna_Y"]

            df_anomalia = pd.DataFrame(
                lista_anomalias, columns=colunas_lista_anomalias)

            df_anomalia['x1'] = df_anomalia['x1']/10000000000000*VarAjuste2

            df_anomalia['m'] = 0
            df_anomalia['b'] = 0
            df_anomalia['cof'] = 0
            df_anomalia['b2'] = 0
            df_anomalia['cof2'] = 0
            print("$#")

            J1_int = J1_X
            J2_int = J2_X
            Poste_int = Poste_X

            a_int = Poste_int - J1_int
            a_km = Poste_KM - J1_Km

            a_int2 = Poste_int - J2_int
            a_km2 = Poste_KM - J2_Km

            df_anomalia['b'] = df_anomalia['x1'] - J1_int
            df_anomalia['cof'] = df_anomalia['b'] / a_int * -1
            df_anomalia['m'] = J1_Km + a_km * df_anomalia['cof']
            print("$#$")

            df_anomalia['m']

            a_km_inverter = Poste_KM - J2_Km
            a_km2_inverter = J1_Km - Poste_KM
            print("$#$ff")

            # flag inverter
            varcheck = checkbox_var.get()
            print("varCheck" + str(varcheck))
            print("$#$dd")

            if str(varcheck) == "True":
                inverter = "Sim"
            else:
                inverter = "Não"
                print("$#ss")

            if inverter == "Não":

                for i in df_anomalia.index:
                    if df_anomalia['x1'][i] <= Poste_int:

                        df_anomalia['b'][i] = df_anomalia['x1'][i] - J1_int
                        df_anomalia['cof'][i] = df_anomalia['b'][i] / a_int
                        df_anomalia['m'][i] = J1_Km + \
                            (a_km * df_anomalia['cof'][i])

                    else:

                        df_anomalia['b2'][i] = df_anomalia['x1'][i] - Poste_int
                        df_anomalia['cof2'][i] = df_anomalia['b2'][i] / a_int2
                        df_anomalia['m'][i] = Poste_KM + \
                            (a_km2 * df_anomalia['cof2'][i])
                        print("$#$aa")

            else:

                for i in df_anomalia.index:
                    if df_anomalia['x1'][i] <= Poste_int:

                        df_anomalia['b'][i] = df_anomalia['x1'][i] - J1_int
                        df_anomalia['cof'][i] = df_anomalia['b'][i] / a_int
                        df_anomalia['m'][i] = J2_Km + \
                            (a_km_inverter * df_anomalia['cof'][i])

                    else:

                        df_anomalia['b2'][i] = df_anomalia['x1'][i] - Poste_int
                        df_anomalia['cof2'][i] = df_anomalia['b2'][i] / a_int2
                        df_anomalia['m'][i] = Poste_KM - \
                            (a_km2_inverter * df_anomalia['cof2'][i])
                        print("$#$oo")
            print("$#$oo3")
            df_anomalia['km'] = round(df_anomalia['m']/1000, 3)
            print("$#$oo3s")
            print(df_anomalia)

            def aplicar_mascara(quilometragem):
                parte_inteira = int(quilometragem)
                parte_decimal = int((quilometragem - parte_inteira) * 1000)
                return f"{parte_inteira:03d}+{parte_decimal:03d}"

            print("$#$oo3sw")
            print(df_anomalia)

            # Aplicar a função para formatar a coluna inteira
            df_anomalia['KM_Name'] = df_anomalia['km'].apply(aplicar_mascara)
            print("$#$oo3seee")
            print(df_anomalia)

            # -----------------------------------------------------------------------------------------------------------------------"
            # -----------------------------------------------------------Print Gráfico ----------------------------------------------"
            # -----------------------------------------------------------------------------------------------------------------------"
            print(f"Print")

            import pandas as pd
            import matplotlib.pyplot as plt

            # Supondo que você já tenha um DataFrame chamado df
            # e as colunas e linhas especificadas

            # Primeiro, selecione as colunas desejadas
            colunas_x = df['x1']
            linhas = [
                'resistenciadoCabo',
                'resistenciaTotalMedida',
                'pontoAlarmeAbsoluto',
                'pontoAlarmeDaMedia'
            ]

            pontos = [

                'resistenciaTotalMedida',

            ]

            # xponto = df['x1']
            # yponto = df['y1']

            # Configure um gráfico de linhas
            plt.figure(figsize=(15, 7))  # Define o tamanho da figura

            x_anomalia = df_anomalia['x1']
            y_anomalia = df_anomalia['Coluna_Y']
            print(df_anomalia['KM_Name'])
            x_kmname = df_anomalia['KM_Name']

            KM_Name_cl = df['KM_Name']

            if str(varcheck) != "True":
                labelJ1 = "J1 KM: " + str(J1_Km)
                labelJ2 = "J2 KM: " + str(J2_Km)
                LabelPoste = "Poste KM: " + str(Poste_KM)
            else:
                labelJ1 = "J2 KM: " + str(J2_Km)
                labelJ2 = "J1 KM: " + str(J1_Km)
                LabelPoste = "Poste KM: " + str(Poste_KM)

            # Plote cada linha
            for linha in linhas:
                plt.plot(colunas_x, df[linha], label=linha)

            # for ponto in pontos:
            #    cores = df["cor"].tolist()
            #    plt.scatter(colunas_x, df[pontos], label=ponto,c=cores)

            # print("chegou até aqui")
            plt.scatter(Poste_X, Poste_Y, label="Poste", color='green')
            texto = LabelPoste
            plt.annotate(texto, (Poste_X, Poste_Y), textcoords="offset points", xytext=(
                10, 10), ha='center', color='green')

            plt.scatter(J1_X, J1_Y, label=labelJ1, color='green')
            texto2 = labelJ1
            plt.annotate(texto2, (J1_X, J1_Y), textcoords="offset points", xytext=(
                10, 10), ha='center', color='green', zorder=0)

            plt.scatter(J2_X, J2_Y, label=labelJ2, color='green')
            texto = labelJ2
            plt.annotate(texto, (J2_X, J2_Y), textcoords="offset points", xytext=(
                10, 10), ha='center', color='green')

            # for anotate Anomalia:

            for i, (xi, yi, x_kmnamei) in enumerate(zip(x_anomalia, y_anomalia, x_kmname)):
                plt.annotate(f'Anomalia {x_kmnamei}', (
                    xi, yi), textcoords='offset points', xytext=(-55, 10), ha='center', color='red')

            # Anmalias
            plt.scatter(x_anomalia, y_anomalia, color='red')

            # plt.scatter(x_procurar, y_procurar, color='green')

            # Configurações do gráfico
            plt.xlabel('x1')  # Rótulo do eixo x
            plt.ylabel('Valor')  # Rótulo do eixo y
            plt.title('Gráfico de Linhas')  # Título do gráfico
            # plt.legend()  # Mostra a legenda
            plt.grid(True)  # Mostra as grades de fundo
            # Defina os rótulos personalizados e opcionalmente gire-os
            plt.xticks(colunas_x, KM_Name_cl, rotation=90)

            plt.grid(False)
            # plt.axis('off')

            # Exibe o gráfico
            plt.show()
            # app.close()
            plt.close(self.fig)
            self.root.destroy()

            # messagebox.showinfo("Pontos Salvos", f"Os pontos foram salvos nas variáveis 'saved_points'.")
            print("Equipamento:", equipamentoapp)
            print("Poste:", posteapp)
            print("J1:", j1app)
            print("J2:", j2app)
            print("Data de Início:", data_inicioapp)
            print("Hora de Início:", hora_inicioapp)
            print("Minuto de Início:", minuto_inicioapp)
            print("Data de Fim:", data_fimapp)
            print("Hora de Fim:", hora_fimapp)
            print("Minuto de Fim:", minuto_fimapp)
            print("T1:", T1_app)
    root = tk.Tk()
    app = InteractiveGraph(root)

    save_button = tk.Button(root, text="Gerar Gráfico",
                            command=app.save_points)
    save_button.pack()

    resetbut = tk.Button(root, text="Limpar Pontos", command=app.clear_points)
    resetbut.pack()

    root.mainloop()
    # except Exception as erro:
    #    tk.messagebox.showerror("Erro", f"Verifique se os J1 | Poste | J2 Estão preenchidos. Verifique se foi selecionado 3.Localizar Pontos")


def transformar_log_df():
    import pandas as pd

    global agregado2
    global keylog

    # Especifica la ruta del archivo de texto
    archivo_txt = 'logs_importados.txt'

    # Lee el archivo de texto y crea un DataFrame
    df = pd.read_csv(archivo_txt, header=None)

    # Imprime el DataFrame

    df = df.rename(columns={0: 'Pacote_Completo'})
    df
    # Criar uma nova coluna com os cinco primeiros caracteres da coluna 'Nome'
    df['Event'] = df['Pacote_Completo'].str[:8]

    # Imprimir o DataFrame resultante
    # Separar os valores da coluna 'Nomes' por vírgula e expandir em colunas individuais
    df_novas_colunas = df['Event'].str.split(';', expand=True)

    # Renomear as novas colunas, se necessário
    df_novas_colunas.columns = [
        f'Nome{i+1}' for i in range(df_novas_colunas.shape[1])]

    # Concatenar as novas colunas com o DataFrame original
    df = pd.concat([df, df_novas_colunas], axis=1)
    df = df.drop('Nome1', axis=1)
    df = df.drop('Nome3', axis=1)
    # Imprimir o DataFrame resultante
    df = df.rename(columns={'Nome2': 'Eventok'})
    df_filtrado = df[df['Eventok'] == '54']
    df = df_filtrado

    new_df = df['Pacote_Completo'].str.split(';', expand=True)

    # Renomear as colunas do novo DataFrame
    new_df.columns = [f'Coluna_{i}' for i in range(1, new_df.shape[1] + 1)]

    # Concatenar o novo DataFrame com o DataFrame original
    result_df = pd.concat([df, new_df], axis=1)
    result_df = result_df.drop('Pacote_Completo', axis=1)
    result_df = result_df.drop('Event', axis=1)
    result_df = result_df.drop('Eventok', axis=1)
    # Exibir o resultado
    colunas = ["deviceType", "eventType", "numLinha", "dds", "collectOrigin", "day", "month", "year",
               "hour", "min", "sec", "NSDTQ", "id", "resistenciaLastro", "resistenciaTotalMedida",
               "taxaVariacaoResistencia", "ICM1", "ICM2", "pontoAlarmeDaMedia", "resistenciadoCabo",
               "resistenciaMinimaTrilhoUmido", "pontoAlarmeAbsoluto", "temperaturaTrilho",
               "temperaturaCPUDTQ", "resistenciaTotalMedidaSemlimite", "bitsAlarme", "mensagemRadioVoz",
               "statusDTQ", "tensaoTrilho", "correnteTrilho", "12V", "V", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10",
               "checkSum", "statusDTQT2", "b"]

    result_df.columns = colunas
    df = result_df
    df['month'] = df['month'].astype(str).str.zfill(2)
    df['day'] = df['day'].astype(str).str.zfill(2)
    df['hour'] = df['hour'].astype(str).str.zfill(2)
    df['min'] = df['min'].astype(str).str.zfill(2)
    df['sec'] = df['sec'].astype(str).str.zfill(2)
    result_df = df
    result_df["device_data"] = "20"+result_df["year"]+"-"+result_df["month"]+"-" + \
        result_df["day"]+"T"+result_df["hour"] + \
        ":"+result_df["min"]+":"+result_df["sec"]
    result_df["checkedAt"] = "20"+result_df["year"]+"-"+result_df["month"]+"-" + \
        result_df["day"]+" "+result_df["hour"] + \
        ":"+result_df["min"]+":"+result_df["sec"]

    agregado2 = result_df

    keylog = 0

    # Convertendo a coluna 'data' para o tipo datetime
    df = agregado2
    df['data'] = pd.to_datetime(df['checkedAt'])

    # Pegando a data mais recente da coluna 'data'
    data_mais_recente = df['data'].max()
    data_subtrai_24h = data_mais_recente - pd.Timedelta(hours=8)

    print(f'Data mais recente: {data_mais_recente}')
    print(f'Data subtraindo 24 horas: {data_subtrai_24h}')
    formato_string = '%d/%m/%Y'
    data_fim = data_mais_recente.strftime(formato_string)
    data_inicio = data_subtrai_24h.strftime(formato_string)

    hora_f = str(data_mais_recente.hour).zfill(2)
    minuto_f = str(data_mais_recente.minute).zfill(2)
    hora_i = str(data_subtrai_24h.hour).zfill(2)
    minuto_i = str(data_subtrai_24h.minute).zfill(2)

    print(data_inicio)
    print(data_fim)
    print(hora_i)
    print(minuto_i)
    print(hora_f)
    print(minuto_f)
    print("----------------------------------------------------------------")
    print(agregado2)
    entrada_j2.delete(0, tk.END)
    entrada_j1.delete(0, tk.END)
    entrada_poste.delete(0, tk.END)
    entrada_equipamento.delete(0, tk.END)
    entrada_equipamento.insert(0, agregado2['dds'][1])
    entrada_data_inicio.insert(0, data_inicio)
    entrada_hora_inicio.delete(0, tk.END)
    entrada_hora_inicio.insert(0, hora_i)
    entrada_minuto_inicio.delete(0, tk.END)
    entrada_minuto_inicio.insert(0, minuto_i)

    entrada_data_fim.delete(0, tk.END)
    entrada_data_fim.insert(0, data_fim)
    entrada_hora_fim.delete(0, tk.END)
    entrada_hora_fim.insert(0, hora_f)
    entrada_minuto_fim.delete(0, tk.END)
    entrada_minuto_fim.insert(0, minuto_f)

    return agregado2, keylog


def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    pasta_destino = os.path.dirname(__file__)
    novo_nome = os.path.join(pasta_destino, 'logs_importados.txt')
    shutil.copy(arquivo, novo_nome)
    tk.messagebox.showinfo("Sucesso", "Arquivo importado com sucesso!")
    transformar_log_df()

# botao_salvar = customtkinter.CTkButton(janela, text="Salvar", command=salvar_formulario())
# botao_salvar.grid(row=6, column=0, columnspan=6, padx=10, pady=10)


def open_form_screen():  # Salvar Análise

    form_screen = tk.Toplevel(janela)
    form_screen.title("Formulário")

    zzplaca = entrada_equipamento.get()

    dtInicio = entrada_data_inicio.get()
    h_inicio = entrada_hora_inicio.get().zfill(2)
    m_inicio = entrada_minuto_inicio.get().zfill(2)

    dt_fim = entrada_data_fim.get()
    h_fim = entrada_hora_fim.get().zfill(2)
    m_fim = entrada_minuto_fim.get().zfill(2)

    # h_fim = h_fim.zfill(2)  # Garante que h_fim tenha pelo menos 2 dígitos, preenchendo com zeros à esquerda, se necessário
    # m_fim = m_fim.zfill(2)  # Garante que m_fim tenha pelo menos 2 dígitos, preenchendo com zeros à esquerda, se necessário

    txt_inicio = dtInicio + " " + h_inicio + ":" + m_inicio
    txt_fim = dt_fim + " " + h_fim + ":" + m_fim

    # Output
    print(txt_inicio)
    print(txt_fim)

    def submit_form():
        placa = placa_entry.get()
        deviceinfo = deviceData.get()
        dt_Inicio_Alarme = data_inicio_entry.get()
        dt_Fim_Alarme = data_fim_entry.get()
        Momento_Analise = antes_do_acionamento_var.get()
        Km_Real_Fratura = km_real_entry.get()
        Km_Algoritimo = km_algoritmo_entry.get()

        userstr = dropbox2.get()
        qtdcorr = QTDCorridas__entry.get()

        # dt_Inicio_Acionamento = data_inicio_Acionamento.get()
        # dt_Fim_FimAtendimento = data_fim_FimAtendimento.get()
        # Km_Algoritimo = data_fim_entry_ronda.get()
        # dt_Previsao_Termino = hrprevisao_entry.get()
        hr_AnomaliaEncontrada = data_horaanomaliaencontrada_entry.get()

        if Km_Algoritimo != '' and Km_Real_Fratura != '':
            if Momento_Analise == "Real":
                status = "Analisado Real"
            else:
                status = "Analisado Pós"

        # elif dt_Fim_FimAtendimento != '00/00/00 00:00':
        #    status = "Em andamento"
        # else:
        #    status = "Não Analisado"

        Title = deviceinfo

        # begin SharePoint

        # coleta dados do elastic testa envios que ja foram feitos para o sharepoint e envia apenas os não repetidos para o sharepoint.
        import pandas as pd
        from datetime import datetime, timedelta
        from office365.sharepoint.client_context import ClientContext, ClientCredential
        from elasticsearch import Elasticsearch

        # Create the client instance
        es = Elasticsearch(
            "https://vpc-rumo-elastic-bnuz2l5d67om2pql6wzb2bz4oy.us-east-1.es.amazonaws.com:443")

        # Configurações de autenticação e URL do SharePoint
        client_id = '9db74ea9-5685-4810-8e73-b257df502805'
        client_secret = 'Fm0793WHNbAI0LovUjUCVka253GcuzrUiCVPHQy71sg='
        url = "https://americalatinalogistica.sharepoint.com/sites/CENTRODEINTELIGNCIADAMANUTENO/"

        # Crie o contexto do cliente e autentique-se
        client_credentials = ClientCredential(client_id, client_secret)
        ctx = ClientContext(url).with_credentials(client_credentials)

        # Defina o título da lista no SharePoint
        list_title = "Analise_ALF"
        tasks_list = ctx.web.lists.get_by_title(list_title)

        # Consulta de query Coldwheels
        # index_name = "rumo-supervisorio-atlas2"
        # doc_type = "_doc"  # Substitua pelo tipo de documento real que você está usando

        # caminho_arquivo = idpf

        # Title = "0"
        # dt_Inicio_Alarme = "0"
        # dt_Fim_Alarme = "0"
        # dt_Inicio_Ronda = "0",
        # dt_Fim_Ronda = "0"
        # dt_Previsao_Termino = "0"
        # hr_AnomaliaEncontrada = "0"
        # Momento_Analise = "0"
        # Km_Real_Fratura = "0"
        # Km_Algoritimo = "0"

        existe_arquivo = False

        # items = tasks_list.get_items().execute_query()
        # for item in items:
        #    if "ARQUIVO" in item.properties:
        #        if item.properties["ARQUIVO"] == caminho_arquivo:
        #            existe_arquivo = True
        #            break

        if not existe_arquivo:
            # Adicionar esses dados na lista do SharePoint
            dados_de_exemplo = {
                "Title": str(Title),
                "dt_Inicio_Alarme": str(dt_Inicio_Alarme),
                "dt_Fim_Alarme": str(dt_Fim_Alarme),
                # "dt_hrAcionamento": str(dt_Inicio_Acionamento),
                # "dt_fimAtendimento": str(dt_Fim_FimAtendimento),
                # "dt_Previsao_Teo": str(dt_Previsao_Termino),
                "hr_AnomaliaEncontrada": str(hr_AnomaliaEncontrada),
                "Momento_Analise": str(Momento_Analise),
                "Km_Real_Fratura": str(Km_Real_Fratura),
                "Km_Algoritimo": str(Km_Algoritimo),
                "placa": str(placa),
                "Status": str(status),
                "usercriador": str(userstr),
                "corridas": str(qtdcorr)

            }

            # Adicione o item à lista no SharePoint
            task_item = tasks_list.add_item(dados_de_exemplo).execute_query()

            # O item foi adicionado com sucesso
            print("Item adicionado ao SharePoint com sucesso.")
            tk.messagebox.showinfo(
                "Success!", "Salvo Com Sucesso! Atualizando banco, aguarde alguns segundos!")
            form_screen.destroy()
        else:
            print(f"erro")
            tk.messagebox.showinfo(
                "Erro!", "Erro SharePoint Contate o Administrador")
            form_screen.destroy()

        # end Share Point

        print("Placa:", placa)
        print("ID:", Title)

        # print("Tempo de Corrida:", tempo_corrida)

        print('fim')
        print("end - Salvar Dados Banco")
        DTQPanel()


# ----------------------

    # Placa
    placa_label = tk.Label(form_screen, text="Placa:")
    placa_label.grid(row=0, column=0)
    placa_entry = tk.Entry(form_screen)
    placa_entry.grid(row=0, column=1)

    # Data Inicio Alarme
    data_inicio_label = tk.Label(form_screen, text="Data Inicio Alarme:")
    data_inicio_label.grid(row=1, column=0)
    data_inicio_entry = tk.Entry(form_screen)
    data_inicio_entry.grid(row=1, column=1)

    # Data Fim Alarme
    data_fim_label = tk.Label(form_screen, text="Data Fim Alarme:")
    data_fim_label.grid(row=2, column=0)
    data_fim_entry = tk.Entry(form_screen)
    data_fim_entry.grid(row=2, column=1)

    # Data Inicio Ronda
    # data_inicio_Acionamento = tk.Label(
    #    form_screen, text="Data/Hora Acionamento:")
    # print("A")
    # data_inicio_Acionamento.grid(row=3, column=0)
    # print("A1")
    # data_inicio_Acionamento = tk.Entry(form_screen)
    # print("A2")
    # data_inicio_Acionamento.grid(row=3, column=1)
    # print("A3")
    # data_inicio_Acionamento.delete(0, tk.END)
    # print("A4")
    # data_inicio_Acionamento.insert(0, "00/00/00 00:00")
    # print("A5")

    # Data Fim Ronda
    # data_fim_FimAtendimento = tk.Label(
    #    form_screen, text="Data/Hora Fim Atendimento:")
    # data_fim_FimAtendimento.grid(row=4, column=0)
    # data_fim_FimAtendimento = tk.Entry(form_screen)
    # data_fim_FimAtendimento.grid(row=4, column=1)
    # data_fim_FimAtendimento.delete(0, tk.END)
    # data_fim_FimAtendimento.insert(0, "00/00/00 00:00")

    # Previsão termino
    # hrprevisao_label = tk.Label(form_screen, text="Previsão termino:")
    # hrprevisao_label.grid(row=5, column=0)
    # hrprevisao_entry = tk.Entry(form_screen)
    # hrprevisao_entry.grid(row=5, column=1)
    # hrprevisao_entry.delete(0, tk.END)
    # hrprevisao_entry.insert(0, "00/00/00 00:00")
    valor_procurado = deviceData.get()

    filtro = df_Share['Title'] == valor_procurado

    statusVarFim = df_Share[filtro]['Momento_Analise'].values[0] if any(
        filtro) else "Pós Acionamento"
    print(statusVarFim)

    # Hora anomalia encontrada
    # data_horaanomaliaencontrada_label = tk.Label(
    #    form_screen, text="Hora anomalia encontrada:")
    # data_horaanomaliaencontrada_label.grid(row=6, column=0)
    data_horaanomaliaencontrada_entry = tk.Entry(form_screen)
    data_horaanomaliaencontrada_entry.grid(row=6, column=1)
    data_horaanomaliaencontrada_entry.delete(0, tk.END)
    data_horaanomaliaencontrada_entry.insert(0, "00/00/00 00:00")

    # Momento da Análise
    antes_do_acionamento_label = tk.Label(
        form_screen, text="Momento da Análise:")
    antes_do_acionamento_label.grid(row=7, column=0)
    antes_do_acionamento_var = tk.StringVar(value=statusVarFim)
    antes_do_acionamento_yes = tk.Radiobutton(
        form_screen, text="Real", variable=antes_do_acionamento_var, value="Real")
    antes_do_acionamento_yes.grid(row=7, column=1)
    antes_do_acionamento_no = tk.Radiobutton(
        form_screen, text="Pós Acionamento", variable=antes_do_acionamento_var, value="Pós Acionamento")
    antes_do_acionamento_no.grid(row=7, column=2)

    # Km Real
    km_real_label = tk.Label(form_screen, text="Km Real:")
    km_real_label.grid(row=8, column=0)
    km_real_entry = tk.Entry(form_screen)
    km_real_entry.grid(row=8, column=1)

    # Km Algoritmo
    km_algoritmo_label = tk.Label(form_screen, text="Km APP Estipulado:")
    km_algoritmo_label.grid(row=9, column=0)
    km_algoritmo_entry = tk.Entry(form_screen)
    km_algoritmo_entry.grid(row=9, column=1)

    QTDCorridas_label = tk.Label(form_screen, text="QTD Corridas")
    QTDCorridas_label.grid(row=10, column=0)
    QTDCorridas__entry = tk.Entry(form_screen)
    QTDCorridas__entry.grid(row=10, column=1)

    lblop = tk.Label(form_screen, text="User")
    lblop.grid(row=11, column=0)
    options2 = ["Cristiano", "Everson", "Helio",
                "Geovane", "Jean", "Pedro", "Willian", "Gabriel", "Outro"]
    dropbox2 = customtkinter.CTkOptionMenu(form_screen, values=options2)
    dropbox2.grid(row=11, column=1, padx=10, pady=10)

    # ----------------------

    data_inicio_entry.delete(0, tk.END)
    data_inicio_entry.insert(0, txt_inicio)

    data_fim_entry.delete(0, tk.END)
    data_fim_entry.insert(0, txt_fim)
    placa_entry.delete(0, tk.END)
    placa_entry.insert(0, zzplaca)

    print(df_Share)

    dt_Inicio_Alarme = df_Share[filtro]['dt_Inicio_Alarme'].values[0] if any(
        filtro) else "00/00/00 00:00"
    dt_Fim_Alarme = df_Share[filtro]['dt_Fim_Alarme'].values[0] if any(
        filtro) else "00/00/00 00:00"
    hr_AnomaliaEncontrada = df_Share[filtro]['hr_AnomaliaEncontrada'].values[0] if any(
        filtro) else "00/00/00 00:00"
    Km_Real_Fratura = df_Share[filtro]['Km_Real_Fratura'].values[0] if any(
        filtro) and df_Share[filtro]['Km_Real_Fratura'].values[0] is not None else ""
    Km_Algoritimo = df_Share[filtro]['Km_Algoritimo'].values[0] if any(
        filtro) and df_Share[filtro]['Km_Algoritimo'].values[0] is not None else ""
    print("flak1")

    corridasshare = df_Share[filtro]['corridas'].values[0] if any(
        filtro) and df_Share[filtro]['corridas'].values[0] is not None else ""

    usercriador = df_Share[filtro]['usercriador'].values[0] if any(
        filtro) and df_Share[filtro]['usercriador'].values[0] is not None else ""

    dropbox2.set(usercriador)
    print("flak2")

    QTDCorridas__entry.delete(0, tk.END)
    print("GolBolinha1")
    QTDCorridas__entry.insert(0, corridasshare)

    print(Km_Algoritimo)

    km_algoritmo_entry.delete(0, tk.END)
    print("GolBolinha1")
    km_algoritmo_entry.insert(0, Km_Algoritimo)
    print("GolBolinha2")
    km_real_entry.delete(0, tk.END)
    print("GolBolinha3")
    km_real_entry.insert(0, Km_Real_Fratura)
    print("GolBolinha4")
    data_horaanomaliaencontrada_entry.delete(0, tk.END)
    data_horaanomaliaencontrada_entry.insert(0, hr_AnomaliaEncontrada)
    print("GolBolinha5")
    # data_fim_FimAtendimento.delete(0, tk.END)
    # data_fim_FimAtendimento.insert(0, dt_Fim_Alarme)
    print("GolBolinha6")
    # data_inicio_Acionamento.delete(0, tk.END)
    # data_inicio_Acionamento.insert(0, dt_Inicio_Alarme)

    # Botão para enviar os dados
    submit_button = tk.Button(
        form_screen, text="Enviar SharePoint", command=submit_form)
    submit_button.grid(row=13, columnspan=4, pady=10)

    # Centralizar a tela do formulário
    window_width = form_screen.winfo_reqwidth()
    window_height = form_screen.winfo_reqheight()
    position_right = int(form_screen.winfo_screenwidth()/2 - window_width/2)
    position_down = int(form_screen.winfo_screenheight()/2 - window_height/2)
    form_screen.geometry("+{}+{}".format(position_right, position_down))


botao_limpar = customtkinter.CTkButton(
    janela, text="0.Limpar", command=limpar_formulario)
botao_limpar.grid(row=12+ajusteDesigner, column=5,  padx=10, pady=10)

buscar_dados2 = customtkinter.CTkButton(
    janela, text="2.Buscar Pontos", command=Achar_pontos)
buscar_dados2.grid(row=1+ajusteDesigner, column=3, padx=10, pady=10)

buscar_dados = customtkinter.CTkButton(
    janela, text="Teste", command=preencher_equipamento)
buscar_dados.grid(row=11+ajusteDesigner, column=5,  padx=10, pady=10)

plote_grafico = customtkinter.CTkButton(
    janela, text="3.Localizar Pontos", command=Localizar_Passagem)
plote_grafico.grid(row=9+ajusteDesigner, column=3,  padx=10, pady=10)

plote_grafico = customtkinter.CTkButton(
    janela, text="5.1.Encontrar Anomalia Manual", command=Manual2)
plote_grafico.grid(row=11+ajusteDesigner, column=3,
                   padx=10, pady=10)  # columnspan=5,

plote_grafico = customtkinter.CTkButton(
    janela, text="5.2.Encontrar Anomalia Automático", command=plot_grafico1)
plote_grafico.grid(row=12+ajusteDesigner, column=3,  padx=10, pady=10)

salvarA = customtkinter.CTkButton(
    janela, text="Salvar Análise", command=open_form_screen)
salvarA.grid(row=12+ajusteDesigner+1, column=3,  padx=10, pady=10)

PanelDTQ = customtkinter.CTkButton(
    janela, text="1.Atualizar Fraturas", command=DTQPanel)
PanelDTQ.grid(row=2, column=5, padx=10, pady=5)

PlacaDTQ = customtkinter.CTkButton(
    janela, text="Placa Portal Eng", command=DTQPlaca)
PlacaDTQ.grid(row=2, column=6, padx=10, pady=5)

janela.btn_selecionar_arquivo = tk.Button(
    janela, text="Selecionar Arquivo", command=selecionar_arquivo)
janela.btn_selecionar_arquivo.grid(
    row=11+ajusteDesigner, column=6,  padx=10, pady=5)


# Criar botão
buttonpdf = tk.Button(janela, text="Abrir PDF Manual", command=abrir_pdf)
buttonpdf.grid(row=12+ajusteDesigner, column=6,  padx=10, pady=5)


def abrir_link():
    # URL que você deseja abrir
    url = "https://app.powerbi.com/links/Mu6DxTvtwp?ctid=837ce9c2-30fa-4613-b9ee-1f114ce71ff1&pbi_source=linkShare"
    # Abrir o link no navegador padrão
    webbrowser.open_new(url)


botaoBI = tk.Button(janela, text="Abrir PowerBI", command=abrir_link)
botaoBI.grid(row=10+ajusteDesigner, column=6,  padx=10, pady=5)


# PanelDTQ2 = customtkinter.CTkButton(janela, text="Atualizar Ativos", command=Achar_pontos)
# PanelDTQ2.grid(row=1, column=0 , padx=10, pady=10)


# janela.attributes('-fullscreen', True)

janela.mainloop()
