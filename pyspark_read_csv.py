from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Read data from CSV file into a DataFrame
input_file_path = "file:///path/to/input.csv"
df = spark.read.csv(input_file_path, header=True, inferSchema=True)

# Perform some transformations
transformed_df = df.select("column1", "column2").filter(df["column1"] > 100)

# Write the transformed data to another CSV file
output_file_path = "file:///path/to/output.csv"
transformed_df.write.csv(output_file_path, header=True)

# Stop the SparkSession
spark.stop()
