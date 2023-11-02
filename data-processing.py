from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

def main():
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("Grocery Data Analysis") \
        .master("local[*]") \
        .getOrCreate()

    # Load the data into a DataFrame
    df = spark.read.csv('GroceryDB_foods.csv', header=True, inferSchema=True)

    # Show the DataFrame schema to verify correct data types
    df.printSchema()

    # Calculate the average protein content per brand
    avg_protein_per_brand = df.groupBy("brand").agg(avg("Protein").alias("AverageProtein"))

    # Show the average protein content per brand
    avg_protein_per_brand.show()

    # Register the DataFrame as a SQL temporary view
    df.createOrReplaceTempView("grocery_foods")

    # Select all records where Total Fat > 20 and Sugars, total < 5 using Spark SQL
    high_fat_low_sugar_foods = spark.sql("""
    SELECT *
    FROM grocery_foods
    WHERE `Total Fat` > 20 AND `Sugars, total` < 5
    """)

    # Show the high fat, low sugar foods
    high_fat_low_sugar_foods.show(5)

    # Stop the Spark session
    spark.stop()

if __name__ == '__main__':
    main()
