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

<hr>