import os
import azureml.core
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.train.dnn import TensorFlow
from azureml.core.compute import ComputeTarget, AmlCompute
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Azure ML workspace from configuration
ws = Workspace.from_config()

# Define experiment
experiment_name = "anomaly_detection_experiment"
experiment = Experiment(workspace=ws, name=experiment_name)

# Set up compute target
compute_name = "gpu-cluster"
if compute_name in ws.compute_targets:
    compute_target = ws.compute_targets[compute_name]
    if compute_target and type(compute_target) is AmlCompute:
        logger.info(f"Using compute target: {compute_name}")
else:
    compute_config = AmlCompute.provisioning_configuration(vm_size="STANDARD_NC6", max_nodes=4)
    compute_target = ComputeTarget.create(ws, compute_name, compute_config)
    compute_target.wait_for_completion(show_output=True)

# Define the training environment
env = Environment(name="anomaly-detection-env")
env.docker.enabled = True
env.python.conda_dependencies_file = "./requirements.txt"

# Set up the ScriptRunConfig
script_config = ScriptRunConfig(
    source_directory="src",
    script="anomaly_detection_model.py",
    compute_target=compute_target,
    environment=env
)

# Submit the experiment
run = experiment.submit(config=script_config)
logger.info("Experiment submitted.")

# Monitor the experiment
run.wait_for_completion(show_output=True)
logger.info("Training completed. Downloading logs...")

# Save model to workspace
model = run.register_model(model_name="anomaly_detection_model", model_path="outputs/model")
logger.info("Model registered successfully.")
