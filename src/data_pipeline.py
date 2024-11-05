from azure.synapse.spark import SparkSession

def initialize_spark():
    spark = SparkSession.builder \
        .appName("PredictPro Pipeline") \
        .getOrCreate()
    return spark

def load_data_from_data_lake(spark, file_path):
    return spark.read.csv(file_path, header=True, inferSchema=True)

def save_data_to_synapse(dataframe, synapse_table):
    dataframe.write \
        .format("com.databricks.spark.sqldw") \
        .option("url", synapse_url) \
        .option("dbtable", synapse_table) \
        .save()

# Run the pipeline
if __name__ == "__main__":
    spark = initialize_spark()
    data = load_data_from_data_lake(spark, "adl://<account_name>.dfs.core.windows.net/processed/transactions.csv")
    save_data_to_synapse(data, "synapse_database.transaction_table")
