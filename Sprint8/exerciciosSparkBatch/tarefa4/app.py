from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, lit, when, col, expr,round

#passo 1 e 2
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("exerciciosSparkBatch/tarefa3/nomes_aleatorios.txt", header=False)
df_nomes.show(5)

df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes.show(10)

#passo 3. usando rand() para gerar valor aleatório entre 0 e 1
df_nomes = df_nomes.withColumn('random', rand())

df_nomes = df_nomes.withColumn('Escolaridade', when(col('random') < 1/3, lit("Fundamental")).when(col('random') < 2/3, lit("Médio")).otherwise(lit("Superior")))
df_nomes = df_nomes.drop('random')

#passo 4 usando algo parecido do passo 3
paises = ["Brasil","Argentina","Colômbia","Peru","Venezuela","Chile","Equador","Bolívia","Paraguai","Uruguai","Guiana","Suriname","Guiana Francesa"]

#usa outros valores aleatórios para ser independente da passada
df_nomes = df_nomes.withColumn('random_Pais', rand())
df_nomes = df_nomes.withColumn('Pais', when(col('random_Pais') < 1/13, lit(paises[0]))
     .when(col('random_Pais') < 2/13, lit(paises[1]))
     .when(col('random_Pais') < 3/13, lit(paises[2]))
     .when(col('random_Pais') < 4/13, lit(paises[3]))
     .when(col('random_Pais') < 5/13, lit(paises[4]))
     .when(col('random_Pais') < 6/13, lit(paises[5]))
     .when(col('random_Pais') < 7/13, lit(paises[6]))
     .when(col('random_Pais') < 8/13, lit(paises[7]))
     .when(col('random_Pais') < 9/13, lit(paises[8]))
     .when(col('random_Pais') < 10/13, lit(paises[9]))
     .when(col('random_Pais') < 11/13, lit(paises[10]))
     .when(col('random_Pais') < 12/13, lit(paises[11]))
    .otherwise(lit(paises[12])))
df_nomes = df_nomes.drop('random_Pais')

#passo 5 usando uma lógica para encaixar o intervalo entre 1945 e 2010
df_nomes = df_nomes.withColumn('Ano Nascimento',round(expr('1945 + (2010 - 1945 + 1) * rand()')).cast('int'))

#passo 6
df_select = df_nomes.filter(col('Ano Nascimento') > 2000).select('*')
df_select.show(10)

#passo 7
df_nomes.createOrReplaceTempView ("pessoas")
spark.sql("SELECT * FROM pessoas WHERE `Ano Nascimento` > 2000").show(10)

#passo 8
numPessoas = df_nomes.filter((col('Ano Nascimento') >= 1980) & (col('Ano Nascimento') <= 1994)).select('*').count()
print(f"Número de pessoas da geração Millennials são {numPessoas}")

#passo 9
numPessoas = spark.sql("SELECT * FROM pessoas WHERE `Ano Nascimento` BETWEEN  1980 AND 1994").count()
print(f"Número de pessoas da geração Millennials são {numPessoas}")

#passo 10
df_nomes.createOrReplaceTempView ("Geracoes")
df_geracoes = spark.sql("""
    SELECT 
        Pais, 
        CASE
            WHEN `Ano Nascimento` BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN `Ano Nascimento` BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN `Ano Nascimento` BETWEEN 1980 AND 1994 THEN 'Millennials (Geração Y)'
            WHEN `Ano Nascimento` BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(Nomes) AS Quantidade
    FROM 
        Geracoes
    WHERE
        `Ano Nascimento` BETWEEN 1944 AND 2015
    GROUP BY 
        Pais, Geracao
    ORDER BY 
        Pais, Geracao, Quantidade
""")

df_geracoes.show(df_geracoes.count(), truncate=False)