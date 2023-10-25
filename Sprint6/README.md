![Imagem_Compass](https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-covers/cl7god9gt00lx04wg4p2a93zt.jpg)

<div align="center">
  <h1>SPRINT 5</h1>
</div>
<hr>

## Resumo

<p>   No primeiro curso aprendi sobre o processo de análise e avaliação que consiste no processo de compilar, processar e analisar os dados para que possa usá-los para tomar decisões. Revisei os tipos de dados e possíveis ferramentas da AWS para cada um, como: Amazon RDS ou Amazon Redshift para dados estruturados e Amazon DynamoDB para semi e não estruturados, por exemplo. Olhei em específico alguns serviços focados em Data & Analytics e aprofundei no processamento de dados, seja eles em batch (processamento de maneira periódica ou agendada - Amazon EMR) ou em Stream (dados em tempo real - Amazon Kinisiss). Finalizando, foi apresentado o conceito de ETL que consiste na extração, transformação e carregamento. Onde o AWS Glue é uma ótima ferramenta para esse processo.
<br>
    No segundo revisei coisas já vistas como o conceito de big
data e os desafios das empresas nas análises de dados atualmente. Ainda, vi serviços focados para a migração de dados para a nuvem, como: AWS Direct Conect ou S3 Transfer Acceleration.
<br>
  Daqui adiante foram cursos rápidos focados em serviços
específicos que serão listados a seguir: 
</p>

* <p><b>Amazon Kinesis Stream</b> - coleta, processa e analisa dados em tempo real gerando isights. Temos os produtores (gravam os dados) e os consumidores. Os resultados são perdidos em 24h ou 7 dias, assim, cabe armazená-los.</p>

* <p><b>Amazon Kinesis Analytics</b> - coleta, processa e analisa dados de streaming em tempo real com norma SQL. Usa uma base de dados em steam e tem a capacidade de mandar os insights para onde queira.</p>

* <p><b>Amazon Elastic Mapreduce(EMR)</b> - permite criar e gerenciar clusters do Hadoop, baseado em computação em nuvem elástica ou EC2s.</p>

* <p><b>Amazon Athena</b> - não usa servidor, serve para fazer consultas em S3 e paga apenas pelas consultas execultadas.</p>

* <p><b>Amazon Quicksight</b> - ferramenta que permite analisar grandes quantidades de dados de várias fontes de maneira rápida e apresentá-los aos usuários finais em painéis dinâmicos e fáceis de manipular.</p>

* <p><b>Amazon IOT Analytics</b> - serviço usado para análise de massivos dados em IOT. Processa, gera valor, armazena, analisa e visualiza.</p>

* <p><b>Amazon Redshift</b> - solução eficiente para lidar com coleta, armazenamento e análise de dados estruturados ou semi. Usa SQL para consultas e pode ser usado para dados em serviço ou machine learning, por exemplo.</p>

* <p><b>Amazon IOT Analytics</b> - serviço usado para análise de massivos dados em IOT. Processa, gera valor, armazena, analisa e visualiza.</p>

<p>No geral foi muito proveitoso e de grande conteúdo aprendido. Assim, segue em sequência um resumo de cada curso e os conteúdos nele abordado para futuramente facilitar os estudos.
</p>


## Lab AWS S3

<p>  Nessa atividade, aprendi como criar um S3 na AWS, configurá-lo para ser visível ao público e estático, como carregar arquivos e pastas e finalizei testando se o site estava acessível e funcionando como devia. Segue as etapas:</p>

* [__Criando Bucket__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/bucketCriado.png)
* [__Habilitando Hospedagem Estática__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/hospedagemEstatica.png)
* [__Permitindo Acesso Publico__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/acessoPublico.png)
* [__Adicionando Politica ao Bucket__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/politicaBucket.png)
* [__Documento de Indice__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/documentoIndice.png)
* [__Documento de Erro__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/documentoError.png)
* [__Testando Site__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_S3/etapas/testeSite.png)

## Lab AWS Athena

<p>  Essa atividade focou no serviço da Athena da AWS que é voltado para a realização de consultas em SQL. Aprendi como configurá-lo, definir um S3 para salvar as consultas, criar um banco, tabelas e realizar as próprias consultas nesse banco.
Segue as etapas: </p>

* [__Criando pasta queries__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/criandoPastaQueries.png)
* [__Configurando Athena__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/configuracaoAWSAthena.png)
* [__Criando Banco de Dados__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/criandoBancoDeDados.png)
* [__Testando Tabela Criada__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/criandoTabela.png)

* **Querie Pedida** - Entender os quatro princípios da arquitetura da AWS:
  1. [__Parte 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/queriePedida.png)
  2. [__Parte 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/queriePedida2.png)
  
* **Resultados** - Entender os quatro princípios da arquitetura da AWS:
  1. [__Parte 1__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/resultados.png)
  2. [__Parte 2__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Athena/resultados2.png)

## Lab AWS Lambda

<p>  Nessa atividade pude ter uma melhor noção de como funciona o Lambda e como criá-la desde o início. Segue as etapas: </p>

* [__Criando a Função Lambda__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Lambda/etapas/criandoFuncaoLambda.png)
* [__Construindo Código__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Lambda/etapas/construindoCodigo.png)
* [__Criando Layer__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Lambda/etapas/criandoLayer.png)
* [__Resultado Final Layer__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/LabAWS_Lambda/etapas/resultadoFinal.png)

## Limpeza

<p>  Por último encerrei todos os serviços, principalmente o S3. Segue: </p>

* [__Esvaziando S3__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/limpeza/esvaziandoBucket.png)
* [__Excluindo S3__](https://github.com/brunnope/Repo_Compass/blob/main/Sprint6/exerciciosAWS/limpeza/excluindo.png)
<hr>