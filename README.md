# IDS 706 Mini Project 10
#### By Daniel Medina
In this project, I use PySpark for data processing.

## Overview
The provided PySpark script is designed to perform data analysis on a CSV file named GroceryDB_foods.csv. This file is assumed to contain various nutritional information about food products. The script calculates the average protein content for each brand and identifies food items that are high in fat but low in sugar. The output is saved as markdown in output.md.

## Data Schema
The GroceryDB_foods.csv should have a header row with the following columns:
* original_ID
* name
* store
* harmonized single category
* brand
* f_FPro (and other similar prefixed columns)
* ingredientList
* has10_nuts
* is_Nuts_Converted_100g
* Protein
* Total Fat
* Carbohydrate
* Sugars, total
* Fiber, total dietary
* Calcium
* Iron
* Sodium
* Vitamin C
* Cholesterol
* Fatty acids, total saturated
* Total Vitamin A

## Script Execution
The script is executed via the spark-submit command:

sh
Copy code
spark-submit grocery_data_analysis.py

## Steps Performed by the Script
### 1. Initialization:

A SparkSession is created with the application name "Grocery Data Analysis".
The session is configured to run in local mode, utilizing all available cores on the host machine.

### 2. Data Loading:
The CSV file is loaded into a DataFrame with schema inference and headers enabled.
The DataFrame's schema is printed to verify that the data types have been correctly inferred.

### 3. Data Transformation:
The script calculates the average protein content (Protein) for each brand by grouping the data on the brand column and then using the aggregate function avg.

### 4. Displaying Results:
The top 5 brands with the highest average protein content are displayed.

### 5. Spark SQL Query:
The DataFrame is registered as a temporary SQL view called grocery_foods.
A SQL query is executed to select all records where Total Fat is greater than 20 grams and Sugars, total is less than 5 grams.

### 6. apture Output Context Manager:
A custom context manager named capture_output is defined. It temporarily redirects standard output to a string buffer, allowing us to capture anything that would normally be printed to the console.

### 7. Markdown File Generation:
After the output is captured, it is written to a Markdown file using the save_markdown function. The output is formatted as a code block within the Markdown for better readability.

### 8. Session Termination:
The Spark session is stopped to release the resources.

## Output
The script outputs two sets of results to the output.md file:
1. The top 5 brands sorted by their average protein content.
2. The top 5 food items that are high in total fat (> 20g) and low in total sugars (< 5g).

## Conclusion
This script provides a quick and automated way to perform preliminary data analysis on a nutritional dataset. It highlights the capabilities of PySpark in processing and analyzing large datasets efficiently.




