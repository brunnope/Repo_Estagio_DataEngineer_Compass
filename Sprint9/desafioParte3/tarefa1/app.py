import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import expr

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Especifica a opção multiline ao ler o JSON
df = spark.read.option("multiline", "true").json(source_file).repartition(1)

# Converte para DynamicFrame
df_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Filtra os registros para pegar apenas os primeiros gêneros que sejam drama ou Romance
df_processado = Filter.apply(
    frame=df_dynamic_frame,
    f=lambda x: x["genres"][0]["name"].startswith("Drama") or x["genres"][0]["name"].startswith("Romance")
)

# Escreve o DynamicFrame resultante no S3 em formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=df_processado,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet",
    format_options={"encoding": "UTF-8"}
)

job.commit()
