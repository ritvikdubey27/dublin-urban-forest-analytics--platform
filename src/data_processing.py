import os
os.environ['PYSPARK_PYTHON'] = r'C:\Users\ritvi\AppData\Local\Programs\Python\Python39\python.exe'

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, regexp_replace
from pyspark.sql.functions import struct
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DublinTreesAnalysis") \
    .config("spark.pyspark.python", r"C:\Users\ritvi\AppData\Local\Programs\Python\Python39\python.exe") \
    .getOrCreate()

spark = SparkSession.builder.appName("DublinTreesAnalysis").getOrCreate()

df = spark.read.csv("../data/dublin_trees.csv", header=True, inferSchema=True)

# Cleaning column names (remove spaces and special characters)
for column in df.columns:
    df = df.withColumnRenamed(column, column.replace(" ", "_").lower())

print("Initial Dataset:")
df.printSchema()
print(f"Number of records: {df.count()}")


# Replacing empty strings with null values
for column in df.columns:
    df = df.withColumn(column, when(col(column) == "", None).otherwise(col(column)))

# Handling missing values
df = df.na.fill({"age_desc": "Unknown", "condition": "Unknown"})
df = df.na.drop(subset=["tree_id", "species_desc", "common_name"])

print("\nMissing values handled.")

df = df.withColumn("height", regexp_replace(col("height"), "metres", "").cast("double"))
df = df.withColumn("spread", regexp_replace(col("spread"), "metres", "").cast("double"))

df = df.withColumn("trunk", regexp_replace(col("trunk"), "cm", "").cast("int"))

print("\nFormats standardized.")

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Age categories
def categorize_age(age_desc):
    if age_desc in ["Young", "Newly Planted"]:
        return "Young"
    elif age_desc in ["Semi-Mature", "Mature"]:
        return "Mature"
    else:
        return "Unknown"

age_udf = udf(categorize_age, StringType())
df = df.withColumn("age_category", age_udf(col("age_desc")))

# Health index
df = df.withColumn("health_index", 
    when(col("condition") == "Good", 3)
    .when(col("condition").isin("Fair", "Fair to Good"), 2)
    .when(col("condition").isin("Poor", "Fair - Poor"), 1)
    .otherwise(0))

print("\nDerived features created.")

# Creatibg a location column combining latitude and longitude
df = df.withColumn("location", struct(col("lat").alias("latitude"), col("long").alias("longitude")))

print("\nGeospatial transformations implemented.")

print("\nProcessed Dataset:")
df.show(5)
df.printSchema()

df.write.parquet("../data/processed_dublin_trees.parquet", mode="overwrite")
print("\nProcessed dataset saved as parquet file.")

spark.stop()
