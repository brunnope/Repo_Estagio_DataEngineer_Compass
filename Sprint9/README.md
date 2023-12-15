![Imagem_Compass](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

<div align="center">
  <h1>SPRINT 9</h1>
</div>
<hr>

## Modelagem de Dados

<p>Realizado em duas tarefas onde aprendi a como modelar os dados relacionalmente(tarefa 1) e de maneira dimensional(tarefa 2).</p>
<p>
Na tarefa 1 optei por construir as tabelas dividindo-a em diferentes objetos que possuíam características em comum, como: carro, cliente, vendedor e locação. Nesse sentido, dividi nessas 4 tabelas haja vista elas teriam suas próprias colunas com suas informações sem estarem misturadas com um outro objeto que não faria sentido, por exemplo, o nome do vendedor estar com cliente. Para unir, usei como base a tabela locação a qual armazena o id da chave principal das outras tabelas e assim permite essa conexão (como podemos ver no modelo lógico).
</p>
<p>
Na tarefa 2 (modelagem dimensional), pensando em responder minha pergunta que seria: qual vendedor mais faturou com as locações de carros? Decidi criar minha fato_locação para armazenar as informações da própria locação(quantidade diaria, valor da diaria e idVendedor) e a dimensão do vendedor para ter acesso as informações dele. Assim, através do id do vendedor na fato e dimensão, consegui fazer o join e executar a querry e obter o seguinte resultado que segue em anexo na tarefa 2.
</p> 

* **Tarefa 1**:
  * [__Código SQL__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa1/Script.sql)
  * [__Modelo Lógico__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa1/diagramaLogico.png)

* **Tarefa 2**:
  * [__Código SQL__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa2/Script-1.sql)
  * [__Modelo Lógico__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa2/diagramaLogico.png)
  * [__Resultado__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa2/saida.png)


## Desafio Parte 3

<p>Realizado em três tarefas onde colocamos em prática no desafio o que aprendemos na atividade anterior. Aqui ficamos responsáveis por limpar os dados e criar nosso camada Trusted e Refined persistindo elas no S3.</p>

### Tarefa 1
<p>
No processamento da Trusted (tarefa 1) não realizei muitas limpezas nos dados pois os mesmos não tinham colunas ou linhas inteiramente nulas. Porém, serviu para salvar com o encoding certo e deixar o arquivo final com as palavras escritas corretamente. Também, apliquei um filtro (o qual se baseia minha análise) para pegar apenas os filmes onde seu primeiro gênero era romance ou drama, assim, pegando apenas os filmes relevantes para mim. Nesse sentido, segue o código do job criado, o arquivo parquet salvo na Trusted, como também o mesmo arquivo em JSON para verificar o formato.
</p>

* [__JOB__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa1/jobCriado.py)
* [__Arquivo Parquet__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa1/dadosProcessados.parquet)
* [__Arquivo JSON__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa1/arqExemplo.json)

### Tarefa 2 e 3

<p>
Na tarefa 2 (modelagem de dados da Refined) e 3 (processamento da Refined) optei por realizar juntas no Athena, ou seja, criei a fato e suas dimensões ao mesmo tempo que salvei como parquet na pasta Refined no S3.
</p> 
<p>
Para criação da fato e dimensões pensando na minha análise - filmes de drama ou romance brasileiros lançados entre 2010 e 2023 - pensei em responder uma pergunta maior que seria: "Qual gênero é o preferido, drama ou romance ?". A partir desses questionamentos, posso visualizar a respota através dos dados e responder outras perguntas por consequência que respondem a pergunta maior, como:
</p>

* Qual gênero teve mais filmes?
* Qual gênero teve mais votos?
* Qual gênero teve uma melhor média de votos?
* Qual filme foi o mais popular?
* Qual empresa(companhia) mais produziu filmes desses gêneros nesse tempo?

Nesse sentido, realizei as seguintes queries no Athena - puxando da tabela principal da Trusted criada anteriormente - e em sequência como ficou na camada Refined após a execução de cada uma:

* **Criação Fato e Dimensões**:
  * [__Dimensão ProductionCompany__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/cria_dimCompany)
  * [__Dimensão NumericalData__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/cria_dimNumericalData)
  * [__Fato Movie__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/cria_fatoMovie)

* **Camada Refined**:
  * [__Fatos e Dimensões__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/evidencias/camadaRefined.png) - persistido na camada Refined
  * [__Exemplo Fato__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/evidencias/fatoMovie.png) - arquivo criado dentro da pasta Fato com os dados

Após o processo, as novas tabelas criadas ficam disponíveis no Athena e consequentemente para uso no QuickSight, como mostrado a seguir:

* [__Novas Tabelas__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/evidencias/fatosDimensoes.png)
* [__Exemplo Consulta na Fato__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/desafioParte3/tarefa2_e_3/evidencias/consultaFatoMovie.png)
<hr>