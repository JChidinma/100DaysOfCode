from pyspark.sql import SparkSession

# Initialize spark session
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

df = spark.read.csv("s3://bucket_name/input.csv",
                    header=True, inferSchema=True)

# perfom a transformation
transfrm_df = df.filter(df['age'] > 18).select('name', 'age')

transform_df.write.csv("s3:bucket_name/output.csv", header=True)

spark.stop()

