#!/bin/bash

# Function to monitor Azure ML pipeline status
monitor_pipeline_status() {
    pipeline_name=$1
    status=$(az ml pipeline show --name $pipeline_name --query "status" -o tsv)
    
    if [[ "$status" == "Succeeded" ]]; then
        echo "Pipeline '$pipeline_name' has succeeded."
    elif [[ "$status" == "Failed" ]]; then
        echo "Pipeline '$pipeline_name' has failed."
    else
        echo "Pipeline '$pipeline_name' is still running. Current status: $status"
    fi
}

# Main function
if [ $# -eq 0 ]; then
    echo "No pipeline name provided. Usage: ./monitor_pipeline.sh <pipeline_name>"
    exit 1
fi

PIPELINE_NAME=$1
echo "Monitoring pipeline: $PIPELINE_NAME"

while true; do
    monitor_pipeline_status $PIPELINE_NAME
    sleep 60  # Check every minute
done
