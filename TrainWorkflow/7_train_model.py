from azureml.core import Experiment, ScriptRunConfig, Environment, Workspace, Dataset
from azureml.core.conda_dependencies import CondaDependencies

ws = Workspace.from_config()

# Create a Python environment for the experiment
sklearn_env = Environment.get(workspace=ws, name="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu")

# Ensure the required packages are installed (we need scikit-learn and Azure ML defaults)
packages = CondaDependencies.create(pip_packages=['scikit-learn','azureml-defaults'])
sklearn_env.python.conda_dependencies = packages

curated_clone = sklearn_env.clone("customize_curated")

# retrieve an existing dataset in the workspace by name
dataset = Dataset.get_by_name(workspace=ws, name="<FOR EXAMPLE: testplan_csv_table_fm> FROM STEP 6", version="latest")

# Create a script config
script_config = ScriptRunConfig(source_directory='<THIS PATH EXAMPLE: /home/USER/AMLExampleRepository/TrainWorkflow/', # Path containing script in line 20
                                script='8_train_script.py',
                                environment=curated_clone,
                                compute_target='<compute clustername fromm step 3.>',
                                arguments=['--input-data', dataset.as_named_input('diabetes')])

# submit the experiment run
experiment_name = '<set your expirmentname>'
experiment = Experiment(workspace=ws, name=experiment_name)
run = experiment.submit(config=script_config)


# # Block until the experiment run has completed
# run.wait_for_completion()