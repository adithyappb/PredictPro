import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
from azure.synapse.spark import SparkSession

# Initialize Azure Data Lake Service
def initialize_data_lake_service(storage_account_name, storage_account_key):
    service_client = DataLakeServiceClient(
        account_url=f"https://{storage_account_name}.dfs.core.windows.net",
        credential=storage_account_key
    )
    return service_client

# Function to upload data to Data Lake
def upload_to_data_lake(service_client, file_system_name, file_path, data):
    file_system_client = service_client.get_file_system_client(file_system_name)
    directory_client = file_system_client.get_directory_client("processed_data")
    file_client = directory_client.get_file_client(file_path)
    
    file_client.upload_data(data, overwrite=True)

# Load raw data and preprocess
def preprocess_data(raw_data_path):
    data = pd.read_csv(raw_data_path)
    # Example preprocessing steps
    data.dropna(inplace=True)
    data['amount'] = data['amount'].astype(float)
    data['is_fraud'] = data['is_fraud'].astype(int)
    # Feature engineering, scaling, etc.
    return data

# Main function
if __name__ == "__main__":
    storage_account_name = "<storage_account_name>"
    storage_account_key = "<storage_account_key>"
    raw_data_path = "data/raw/transactions.csv"
    processed_data_path = "data/processed/processed_transactions.csv"
    
    # Initialize service client
    service_client = initialize_data_lake_service(storage_account_name, storage_account_key)
    
    # Preprocess and upload data
    processed_data = preprocess_data(raw_data_path)
    upload_to_data_lake(service_client, "transaction-data", "processed_transactions.csv", processed_data.to_csv(index=False))
