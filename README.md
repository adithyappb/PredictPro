## PredictPro

PredictPro is a machine learning pipeline for detecting fraudulent transactions using Azure services. The project leverages Azure Data Lake for data storage, Azure AutoML for model training, and custom neural networks for anomaly detection.

# Setup Instructions
- pip install -r requirements.txt

# Configure your Azure resources in: 
- config/azure_config.yaml.

# Run the deployment script:
- ./scripts/deploy_pipeline.sh
