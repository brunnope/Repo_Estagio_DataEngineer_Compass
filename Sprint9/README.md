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
  * [__Saída__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint9/modelagemDados/tarefa2/saida.png)

<hr>