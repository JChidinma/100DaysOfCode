# Create a Dataframe manually with har coded values in PySpark
# Use the createDataFrame() method from SparkSession object

from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("New Spark Session").getOrCreate()

data = [(1, 'New York'), (2, 'Toronto')]
schema = StructType([StructField(name='id', dataType=IntegerType()),
                     StructField(name='name', dataType=StringType())])

# df = spark.createDataFrame(data=data, schema=['id', 'name'])

df = spark.createDataFrame(data, schema)
df.show()
df.printSchema()

df_csv = spark.read.csv("path/to/csvfile.csv")
df_csv.show()


# # Read JSON File
df_json = spark.read.json("path/to/jsonfile.json")
df_json.show()
df_json.write.json("path/to/outputfile.json")

df_parquet = spark.read.parquet("path/to/parquet_file.parquet")
df_parquet.show()
df_json.write.json("path/to/outputfile.parquet")


# Renaming Columns
df_renamed = df_csv.withColumnRenamed("old_col_name", "new_col_name")
df_renamed.show()

# Select columns
df_selected = df_csv.select("column1", "column2")
df_selected.show()

# Filter data
df_filtered = df_csv.filter(df_csv["column1"] > 100)
df_filtered.show()

# Adding new columns

df_new_col = df_csv.withColumn(
    "new_col_name", col("col1") + col("col2")
)
df_new_col.show()

# Aggregations
df_aggregated = df_new_col.groupBy("newCol_name").sum("new_col")
df_aggregated.show()

df_aggregated.write.parquet("path/to/outputfile.parquet")

# Erro Handliing with Logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

spark.stop()
