![Imagem_Compass](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

<div align="center">
  <h1>SPRINT 8</h1>
</div>
<hr>

## Exercício TMDB

<p>Nesse exercício tive o primeiro contato com API no geral e como realizar uma chamada para capturar dados no tmdb.</p>

* **Códigos**:
  * [__teste 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosTMDB/testeAPI.py)
  * [__teste 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosTMDB/testeAPI2.py)

* **Resultados**:
  * [__teste 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosTMDB/resultados/testeAPI.png)
  * [__teste 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosTMDB/resultados/testeAPI2.png)
  
## Desafio parte 2

<p>Na segunda parte do desafio, usamos a API do tmdb para complementar nossos dados no RAW. Para isso utlizamos o serviço da AWWS Lambda para realizar o processo de extração e subir para o S3 onde está os outros dados capturados na sprint passada.</p>

<p>Como análise, optei por escolher fazer sobre todos os filmes brasileiros lançados desde 2010 até o fim desse ano(2023) do gênero romance e/ou drama. Assim, posso analisar posteriormente os mais bem votados, qual gênero foi mais predominante e outras coisas.</p>

* [__Aplicativo Lambda__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/desafioParte2/lambda.py)
* [__Exemplo json__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/desafioParte2/exemplo_resul.json.json)
* **Prints**:
  * [__permissões role__](https://github.com/brunnope/Repo_Compass/tree/main/Sprint8/desafioParte2/prints/permissoes_funcao)
  * [__log execução lambda__](https://github.com/brunnope/Repo_Compass/tree/main/Sprint8/desafioParte2/prints/execucao_log)
  * [__arquivos json gerados__](https://github.com/brunnope/Repo_Compass/tree/main/Sprint8/desafioParte2/prints/arquivos_json)

## Exercícios Spark Batch

<p>Nesses exercícios de spark pude relembrar códigos já antes desenvolvidos para leitura e escrita de arquivos com python, como também aprendi a manipular a lib "names" para geração de nomes completos aleatórios, algo que foi importante para criar um base de dados que permitiu sua manipulação e extração de dados com spark.</p>

<p>No geral gostei bastante pois contribuiu no aprendizado de spark e do processo ETL no geral. Assim segue o que foi desenvolvido na tarefa 3 e 4:</p>

### Tarefa 3
* **Programas**:
  * [__Warm Up 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/warmUp1.py)
  * [__Warm Up 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/warmUp2.py)
  * [__Laboratórios__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/laboratorio.py)
* **Saídas**:
  * [__Warm Up 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/saidas/warmUp.png)
  * [__Warm Up 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/saidas/warmUp2.png) - [__Arquivo Gerado CSV__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/saidas/Animais.csv)
  * [__Laboratórios__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa3/saidas/Captura%20de%20tela%202023-11-20%20150357.png) - Não coloquei o arquivo em si por causa do tamanho que excede

### Tarefa 4

<p>As saídas coloquei apenas aquele que o passo pedia para printar no console...</p>

* **Programa**:
  * [__App__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/app.py)
* **Saídas**:
  * [__Passo 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo1.png)
  * [__Passo 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo2.png)
  * [__Passo 6__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo6.png)
  * [__Passo 7__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo7.png)
  * [__Passo 8__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo8.png)
  * [__Passo 9__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo8.png) - mesma saída
  * [__Passo 10__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint8/exerciciosSparkBatch/tarefa4/saidas/passo10.png)

<hr>