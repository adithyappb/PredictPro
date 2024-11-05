#!/bin/bash

echo "Deploying PredictPro pipeline..."

# Step 1: Deploy data ingestion
python3 src/data_ingestion.py

# Step 2: Train model using AutoML
python3 src/azure_auto_ml_setup.py

# Step 3: Run data pipeline
python3 src/data_pipeline.py

echo "PredictPro pipeline deployed successfully."
