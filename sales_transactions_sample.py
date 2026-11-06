# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM `samples`.`bakehouse`.`sales_transactions`
# MAGIC LIMIT 10

# COMMAND ----------

# Run the same query from Python, show the rows, and return them as the notebook result
df = spark.sql("SELECT * FROM `samples`.`bakehouse`.`sales_transactions` LIMIT 10")
display(df)

dbutils.notebook.exit(df.toJSON().collect().__str__())
