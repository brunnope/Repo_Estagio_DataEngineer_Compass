![Imagem_Compass](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

<div align="center">
  <h1>SPRINT 7</h1>
</div>
<hr>

## Exercícios

<p>Nos exercícios colocamos em prática a manipulação de dados com o pandas e numpy - tarefa 1 - e criamos uma aplicação de contagem de palavras com Spark - tarefa 2. </p>

### Tarefa 1

* **Programas**:
  1. [__Ator Maior Média__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/resolucoes/atorMaiorMedia.py)
  2. [__Ator Maior Número Filmes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/resolucoes/atorMaiorNumeroFilmes.py)
  3. [__Filmes Mais Frequentes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/resolucoes/filmesMaisFrequencia.py)
  4. [__Média Número de Filmes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/resolucoes/mediaNumFilmes.py)

* **Saídas Programas**:
  1. [__Ator Maior Média__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/saidas/atorMaiorMediaFilme.png)
  2. [__Ator Maior Número Filmes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/saidas/atorMaiorNumFilmes.png)
  3. [__Filmes Mais Frequentes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/saidas/frequenciaFilmes.png)
  4. [__Média Número de Filmes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa1/saidas/mediaNumFilmes.png)
  
### Tarefa 2

* [__Aplicativo__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa2/app.scala)

* **Passos**:
  1. [__Baixar Readme__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa2/baixandoReadme.png)
  2. [__Código__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa2/resultado.png)
  3. [__Parte dos Resultados__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/Exercicios/tarefa2/resultCont.png)

## Laboratório AWS

<p> Nesse laboratório, aprendemos a criar, rodar e subir arquivos para o s3 utilizando o glue. Segue os passos e os códigos de cada job criado:</p>

* **Etapas Udemy**:
  1. [__S3 criado__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/s3Criado.png)
  2. [__Role criada__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/funcaoCriada.png)
  3. [__DataBase Criado__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/criacaoDataBase.png) - [__Administrador__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/administradorDataBase.png)
  4. [__Criação Job__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/jobCriado.png) - [__Executados__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/jobsCriados.png)
  5. [__Resultados jobs__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/arquivosGeradosJobs.png)
  6. [__Crawler Criado e Executado__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/evidencias/crawlerExecutado.png)

* **Códigos**:
  * [__Imprimir Schema__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/imprimirSchema.txt)
  * [__Nomes em Maiúsculo__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/nomeMaiusculo.txt)
  * [__Contagem Número de Linhas__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/imprimirNumLinhas.txt)
  * [__Imprimir Contagem de Nomes__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/imprimirContagemNomes.txt)
  * [__Nome Feminino Maior Registro__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/nomeFemininoMaisRegistros.txt)
  * [__Nome Masculino Maior Registro__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/nomeFemininoMaisRegistros.txt)
  * [__Total Registros__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/contagemRegistros.txt)
  * [__Nomes em Maiúsculos Particionados__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/LaboratoriosAWS_Glue/codigos/nomesMaiusculosParticonados.txt)



## Desafio - Parte 1

<p> Nessa primeira parte do desafio fizemos um processo ETL usando a lib Boto3, a qual permite se comunicar e realizar operações na nossa conta da AWS. Nesse sentido, usamos para subir dois arquivos csv para nosso bucket s3.</p>

* [__Programa Principal__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/app.py)
* [__Dockerfile__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/Dockerfile)
* [__.gitignore__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/.gitignore) - criado para não subir para o git arquivos tão grandes e permite a leitura e transferência para o container

* **Etapas Udemy**:
  1. [__Primeira parte do app__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/etapas/appBoto.png)
  2. [__Segunda parte__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/etapas/appBoto2.png)
  3. [__Criando Imagem__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/etapas/criandoImagem.png)
  4. [__Executando Container__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint7/DesafioParte1ETL/etapas/executandoContainer.png)

<hr>