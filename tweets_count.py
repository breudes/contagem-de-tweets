import requests # módulo que permite a realização de requisições HTTP/HTTPS
import json # módulo para manuseio de objetos json
import datetime # módulo para manuseio de datas e horas
import matplotlib.pyplot as plt # biblioteca para criação de gráficos e visualizações de dados
import numpy as np # biblioteca para manuseio de elementos matemáticos

# variavéis recebidas do usuário
bearer_token = ""
keywords = ""

# gera o cabeçalho para a requisição com o bearer token
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "RecentTweetsCountWithPython"
    return r

# conecta com o endpoint da API e retorna a reposta da requisição em formato JSON
def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print("Status da requisição: ",response.status_code) # mostra no terminal a resposta da requisição
    if response.status_code != 200: # caso ocorra algum erro, mostra o erro 
        raise Exception(response.status_code, response.text)
    return response.json() # retorna resposta

# gera e plota gráfico de barra
def plot_bar_charts(x_values,y_values, total_counts, second_x_values, second_y_values, second_total_counts):
    # primeiro gráfico
    first_labels = x_values # valores da coordenada x
    first_means = y_values # valores da coordenada y

    x = np.arange(len(first_labels))  # localização da label
    width = 0.35  # comprimento das barras

    fig, (ax,ax2) = plt.subplots(nrows=2, ncols=1) 
    fig.set_size_inches(20, 10) # tamanho da figura do gráfico em polegadas 
    rects1 = ax.bar(x - (width/2), first_means, width, align = 'edge') # array com a quantidade barras presentes no gráfico
    ax.set_ylabel('Contagem de tweets') # label da coordenada Y
    ax.set_xlabel('Hora') # label da coordenada X
    ax.set_title('Contagem de tweets das últimas 24 horas \n Palavras chave: '+str(keywords) +'\n Contagem total: '+str(total_counts)) # titulo do gráfico
    
    # labels na coordenada x
    ax.set_xticks(x)
    ax.set_xticklabels(first_labels) 
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()

    # segundo gráfico
    second_labels = second_x_values # valores da coordenada x
    second_means = second_y_values # valores da coordenada y

    x2 = np.arange(len(second_labels))  # localização da label

    rects2 = ax2.bar(x2 - (width/2), second_means, width, align = 'edge') # array com a quantidade barras presentes no gráfico
    ax2.set_ylabel('Contagem de tweets') # label da coordenada Y
    ax2.set_xlabel('Dia') # label da coordenada X
    ax2.set_title('Contagem de tweets dos últimos 7 dias \n Palavras chave: '+str(keywords) +'\n Contagem total: '+str(second_total_counts)) # titulo do gráfico
    
    # labels na coordenada x
    ax2.set_xticks(x2)
    ax2.set_xticklabels(second_labels) 
    ax2.bar_label(rects2, padding=3)
    fig.tight_layout()

    # mostra o gráfico
    plt.show()

if __name__ == '__main__':
    search_url = "https://api.twitter.com/2/tweets/counts/recent" # URL para as requisições 

    # bearer token e palavras chave para as requisições
    bearer_token = input("Informe o bearer token: ")
    keywords = input("Informe o conjunto de palavras chave para a consulta: ")

    # define intervalo de tempo referente as últimas 24 horas
    # data e hora atual
    current_date_time = datetime.datetime.now(datetime.timezone.utc).astimezone()
    str_current_date = current_date_time.strftime('%Y-%m-%dT%H:%M:%Sz') # converte variável do tipo datetime para string
                
    # data e hora de 24 horas atrás
    last_day_date_time = datetime.datetime.now(datetime.timezone.utc).astimezone() - datetime.timedelta(hours = 24)
    str_last_date = last_day_date_time.strftime('%Y-%m-%dT%H:%M:%Sz') # converte variável do tipo datetime para string

    # primeira requisição: contagem de tweets referente às últimas 24 horas
    # criação da query (consulta)
    query_params = {
        'query': keywords,
        'start_time': str_last_date,
        'end_time': str_current_date
    }
    # requisição 
    json_response = connect_to_endpoint(search_url, query_params)

    # tratamento dos dados 
    json_array = json.loads(json.dumps(json_response, indent=4, sort_keys=True)) # transforma o objeto JSON em um dicionário Python
    
    print(json_array)
    
    total_counts = json_array['meta']['total_tweet_count'] # contagem total dos resultados

    # organiza os resultados por hora
    hours = []
    counts = []

    for x in range(len(json_array['data'])):
        # hora de início da contagem
        hour = datetime.datetime.strptime(json_array['data'][x]['start'], "%Y-%m-%dT%H:%M:%S.%fZ").hour   
        hours.append(hour)
        # contagem referente à hora de início 
        count = json_array['data'][x]['tweet_count']
        counts.append(count)
    
    # soma o resultado da última hora (hora atual) com a hora anterior
    counts_length = len(counts)
    counts[counts_length-2] += counts[counts_length-1]
    counts.pop(counts_length-1)
    hours.pop(len(hours)-1)

    # segunda requisição: contagem de tweets referente dos últimos 7 dias
    # criação da query (consulta)
    second_query_params = {
        'query': keywords,
        # como os resultados são organizados, nesse caso são organizados por dia (padrão da API é resultados organizados por hora)
        'granularity': 'day'
    }
    # requisição 
    second_json_response = connect_to_endpoint(search_url, second_query_params)

    # tratamento dos dados 
    second_json_array = json.loads(json.dumps(second_json_response, indent=4, sort_keys=True)) # transforma o objeto JSON em um dicionário Python
    second_total_counts = second_json_array['meta']['total_tweet_count'] # contagem total dos resultados

    # organiza os resultados por dia
    days = []
    second_counts = []

    for x in range(len(second_json_array['data'])):
        # dia de início da contagem
        day = datetime.datetime.strptime(second_json_array['data'][x]['start'], "%Y-%m-%dT%H:%M:%S.%fZ").day   
        days.append(day)
        # contagem referente ao dia de início 
        second_count = second_json_array['data'][x]['tweet_count']
        second_counts.append(second_count)
    
    # soma o resultado do último dia (dia atual) com o dia anterior
    second_counts[1] += second_counts[0]
    second_counts.pop(0)
    days.pop(0)

    # gera os gráficos juntos
    plot_bar_charts(hours,counts,total_counts,days,second_counts,second_total_counts)