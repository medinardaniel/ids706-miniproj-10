# PySpark Output

```
root
 |-- _c0: string (nullable = true)
 |-- original_ID: string (nullable = true)
 |-- name: string (nullable = true)
 |-- store: string (nullable = true)
 |-- harmonized single category: string (nullable = true)
 |-- brand: string (nullable = true)
 |-- f_FPro: string (nullable = true)
 |-- f_FPro_P: string (nullable = true)
 |-- f_min_FPro: string (nullable = true)
 |-- f_std_FPro: string (nullable = true)
 |-- f_FPro_class: string (nullable = true)
 |-- ingredientList: string (nullable = true)
 |-- has10_nuts: string (nullable = true)
 |-- is_Nuts_Converted_100g: string (nullable = true)
 |-- Protein: string (nullable = true)
 |-- Total Fat: string (nullable = true)
 |-- Carbohydrate: string (nullable = true)
 |-- Sugars, total: string (nullable = true)
 |-- Fiber, total dietary: string (nullable = true)
 |-- Calcium: string (nullable = true)
 |-- Iron: string (nullable = true)
 |-- Sodium: string (nullable = true)
 |-- Vitamin C: string (nullable = true)
 |-- Cholesterol: string (nullable = true)
 |-- Fatty acids, total saturated: string (nullable = true)
 |-- Total Vitamin A: string (nullable = true)

+-----------+------------------+
|      brand|    AverageProtein|
+-----------+------------------+
|      7DAYS|             400.0|
|Blue Ribbon|7.6923076923076925|
|       Silk|2.6511299435028253|
|   Sambazon|0.9629272711384499|
|    Hanover|3084.6027742749056|
+-----------+------------------+
only showing top 5 rows

+---+--------------------+--------------------+----------+--------------------------+--------------------+------------------+---------+------------------+------------------+------------+--------------------+----------+----------------------+------------------+------------------+------------------+-------------+--------------------+------------------+------------------+------------------+---------+-----------+----------------------------+---------------+
|_c0|         original_ID|                name|     store|harmonized single category|               brand|            f_FPro| f_FPro_P|        f_min_FPro|        f_std_FPro|f_FPro_class|      ingredientList|has10_nuts|is_Nuts_Converted_100g|           Protein|         Total Fat|      Carbohydrate|Sugars, total|Fiber, total dietary|           Calcium|              Iron|            Sodium|Vitamin C|Cholesterol|Fatty acids, total saturated|Total Vitamin A|
+---+--------------------+--------------------+----------+--------------------------+--------------------+------------------+---------+------------------+------------------+------------+--------------------+----------+----------------------+------------------+------------------+------------------+-------------+--------------------+------------------+------------------+------------------+---------+-----------+----------------------------+---------------+
|233|wf_lilys-chocolat...|45% Cacao Semi-sw...|WholeFoods|                    baking|              Lily's|0.4968888888888889|12P_min10|0.4416666666666666|0.0332414242166399|         1.0|['Ingredients: Un...|         1|                     1| 7.142857142857143|28.571428571428573|57.142857142857146|          0.0|  35.714285714285715|               0.0|0.0078571428571428|               0.0|      0.0|        0.0|          17.857142857142858|            0.0|
|240|wf_artisan-kettle...|Organic Unsweeten...|WholeFoods|                    baking|      Artisan Kettle|0.3468888888888888|12P_min10|0.3344444444444444|0.0108926439103655|         0.0|['Ingredients: Or...|         1|                     1|14.285714285714286|              50.0|28.571428571428573|          0.0|   7.142857142857143|0.1428571428571428|0.0035714285714285|               0.0|     null|        0.0|          32.142857142857146|           null|
|270|wf_lilys-chocolat...|Premium Baking Ba...|WholeFoods|                    baking|              Lily's|0.4967777777777778|12P_min10|0.4447222222222222|0.0318577325536013|         1.0|['Unsweetened Coc...|         1|                     1| 7.142857142857143|35.714285714285715|57.142857142857146|          0.0|  28.571428571428573|               0.0|0.0085714285714285|               0.0|     null|        0.0|          21.428571428571427|           null|
|286|wf_lakanto-sugar-...|Sugar Free Chocol...|WholeFoods|                    baking|             Lakanto|0.5938888888888889|12P_min10|0.5783333333333334|0.0112953475618596|         1.0|['Unsweetened Cho...|         1|                     1| 7.142857142857143|28.571428571428573|57.142857142857146|          0.0|  21.428571428571427|0.0857142857142857|0.0014285714285714|0.1071428571428571|     null|        0.0|          18.571428571428573|           null|
|288|wf_guittard-choco...|Unsweetened Choco...|WholeFoods|                    baking|Guittard Chocolat...|0.4351666666666666|12P_min10|0.4011111111111111|0.0203106658716091|         1.0|['Cacao Beans‡.',...|         1|                     1|14.285714285714286|              50.0|28.571428571428573|          0.0|  28.571428571428573|               0.0|0.0142857142857142|               0.0|     null|        0.0|          32.142857142857146|           null|
+---+--------------------+--------------------+----------+--------------------------+--------------------+------------------+---------+------------------+------------------+------------+--------------------+----------+----------------------+------------------+------------------+------------------+-------------+--------------------+------------------+------------------+------------------+---------+-----------+----------------------------+---------------+
only showing top 5 rows


```
