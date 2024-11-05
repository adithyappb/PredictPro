from azureml.core import Workspace, Experiment
from azureml.train.automl import AutoMLConfig

# Set up Azure ML workspace
ws = Workspace.from_config(path="config/azure_config.yaml")
experiment = Experiment(ws, "PredictPro-AutoML")

# Define AutoML config
automl_settings = {
    "task": "classification",
    "primary_metric": "accuracy",
    "training_data": train_data,
    "label_column_name": "is_fraud",
    "n_cross_validations": 5
}

automl_config = AutoMLConfig(**automl_settings)

# Run AutoML experiment
run = experiment.submit(automl_config)
run.wait_for_completion(show_output=True)
