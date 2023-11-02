from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
import sys
from io import StringIO
import contextlib


@contextlib.contextmanager
def capture_output():
    new_stdout, new_stderr = StringIO(), StringIO()
    old_stdout, old_stderr = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_stdout, new_stderr
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr


def save_markdown(output, filename="output.md"):
    with open(filename, "w") as f:
        f.write("# PySpark Output\n\n")
        f.write("```\n")
        f.write(output)
        f.write("\n```\n")


def main():
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("Grocery Data Analysis") \
        .master("local[*]") \
        .getOrCreate()

    # Load the data into a DataFrame
    df = spark.read.csv('GroceryDB_foods.csv', header=True, inferSchema=True)

    # Calculate the average protein content per brand
    avg_protein_per_brand = df.groupBy("brand").agg(avg("Protein").alias("AverageProtein"))

    # Register the DataFrame as a SQL temporary view
    df.createOrReplaceTempView("grocery_foods")

    # Select all records where Total Fat > 20 and Sugars, total < 5 using Spark SQL
    high_fat_low_sugar_foods = spark.sql("""
    SELECT *
    FROM grocery_foods
    WHERE `Total Fat` > 20 AND `Sugars, total` < 5
    """)

    # Capture the output
    with capture_output() as (out, err):
        # Show the DataFrame schema to verify correct data types
        df.printSchema()

        # Show the average protein content per brand
        avg_protein_per_brand.show(5)

        # Show the high fat, low sugar foods
        high_fat_low_sugar_foods.show(5)

    # Save the output to markdown
    save_markdown(out.getvalue())

    # Stop the Spark session
    spark.stop()


if __name__ == '__main__':
    main()
