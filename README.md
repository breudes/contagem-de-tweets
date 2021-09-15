## Contagem de Tweets usando Python

## Sobre o projeto
Neste trabalho realizamos uma integração com a API do twitter para realizar a contagem de tweets por palavras chave definidas pelo o usuário. Essa contagem é feita utilizando o produto padrão chamado de Tweet Counts, um serviço dispobilizado pela API focado na contagem de tweets. Cada contagem é resultante de uma requisição HTTPS feita à API.

O projeto se baseia nas palavras chave para realizar a contagem de tweets em dois intervalos de tempo: nas últimas 24 (vinte e quatro) horas e nos últimos 7 (sete) dias. Cada intervalo de tempo é utilizado em uma requisição, que nos retorna o resultado de contagem de tweets; ou seja, ao final de duas requisições, temos duas contagens para mostrar. Ambas as contagens são usadas para gerar gráficos: o primeiro referente a contagem das últimas 24 horas, e o segundo referente a contagem dos últimos 7 dias.

Observação: para utilizar este projeto, é necessário que o usuário possua, além da conta regular do Twitter, também possua uma conta de desenvolvedor no Twitter, pois nesse perfil de desenvolvedor é onde é gerado a chave que utilizamos para realizar as requisições. Para isso, é necessário fazer uma requisição ao Twitter para obter a conta, peça sua conta de desenvolvedor em https://developer.twitter.com/en/apply-for-access.

Este projeto foi feito como atividade avaliativa na disciplina Redes de Computadores, do curso de Bacharelado em Tecnologia da Informação (IMD - UFRN), ministrada pelo docente Augusto Jose Venancio Neto.

## Como compilar
Primeiro, é necessário que a linguagem de programação Python esteja instalada em sua máquina. Para fins de referência, este projeto foi feito utilizando Python versão 3.9. Para instalar o Python em sua máquina acesse https://www.python.org/downloads/.

Para compilar o projeto (arquivo tweet_counts.py), execute tais comandos (assumindo $ como o prompt de seu terminal):
    
    # Executar o projeto
    $ python tweet_counts.py
    # Inserir os parâmetros necessários
    $ Informe o bearer token: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
    $ Informe o conjunto de palavras chave para a consulta: palavra1 palavra2 ...

Para utilizar o projeto no Google Colab, basta adicionar o arquivo tweet_counts.ipynb ao Google Colab e selecionar a opção de Ambiente de Execução chamada 'Executar tudo'.

## Exemplos
Segue alguns exemplos de palavras chave para a consulta, entretanto, existem mais possibilidades. Para ver mais sobre criação de consultas para requisições do Tweet Counts, acesse https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query.

1. Exemplo de consulta de tweets que contêm duas ou mais palavras chave (estrutura: palavra1 palavra2 ...). Neste caso, tweets que contêm as palavras vacina e covid-19: 
    ```    
    $ Informe o conjunto de palavras chave para a consulta: vacina covid-19
    ```
2. Exemplo de consulta de tweets que contêm uma palavra ou outra (estrutura: palavra1 OR palavra2). Neste caso, tweets que contêm ou a palavra vacina ou a palavra covid-19. Observação: deve-se utilizar o operador OR (do inglês, OU) em letra maiúscula para seguir o padrão aceito pela API, este operador pode ser utilizado com mais de duas palavras: 
    ```    
    $ Informe o conjunto de palavras chave para a consulta: vacina OR covid-19
    ```
3. Exemplo de consulta de tweets de um perfil específico do Twitter (estrutura: 'from:'+usuário).
    ```    
    $ Informe o conjunto de palavras chave para a consulta: from:_breudes
    ```
## Autor 
Este projeto foi feito por Brenda Alexandra de Souza Silva (https://github.com/breudes)
