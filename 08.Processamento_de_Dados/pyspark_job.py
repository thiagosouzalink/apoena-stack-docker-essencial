from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = SparkSession.builder.appName("apoena-pyspark-job").getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 100))

even_rdd = rdd.filter(lambda x: x % 2 == 0)

even_count = even_rdd.count()
even_sum = even_rdd.sum()
even_average = even_rdd.mean()

print("PySpark Job Calculations")
print("Results:")
print(f"Quantidade de Números Pares: {even_count}")
print(f"Soma dos Números Pares: {even_sum}")
print(f"Média dos Números Pares: {even_average}")

spark.stop()