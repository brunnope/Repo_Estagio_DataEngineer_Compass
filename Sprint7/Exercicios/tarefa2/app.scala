//comandos usados no spark shell

// Carrega o arquivo README.md como RDD
val arq = sc.textFile("README.md")

// Divide o arquivo em palavras
val palavras = arq.flatMap(_.split(" "))

// Conta as palavras e atribui o valor
val contaPalavras = palavras.map(palavra => (palavra, 1)).reduceByKey(_ + _)

// Exibe o resultado
contaPalavras.collect().foreach(println)