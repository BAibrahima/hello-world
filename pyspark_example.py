from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Move Column Position and Save Table") \
    .getOrCreate()

# Sample DataFrame
data = [("Alice", 34, 10000, "Engineer"),
        ("Bob", 45, 15000, "Manager"),
        ("Charlie", 29, 12000, "Developer")]
df = spark.createDataFrame(data, ["Name", "Age", "Salary", "Title"])

# Define the new column order (move "Title" column to the second position)
column_order = ["Name", "Title", "Age", "Salary"]

# Reorder columns using select
df = df.select(*column_order)

# Save the DataFrame as a table
table_name = "updated_table"
df.createOrReplaceTempView(table_name)

# Alternatively, you can save it as a permanent table in Hive or any other supported storage
# df.write.saveAsTable(table_name)

# Show the result
df.show()

# Stop the SparkSession
spark.stop()
