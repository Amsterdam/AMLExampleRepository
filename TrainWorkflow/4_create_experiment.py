from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name='<testplan-fm-01_for_example>')

env = Environment.get(workspace=ws, name="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu")

# TODO: make sure the paths are correct
config = ScriptRunConfig(source_directory='<directory helpers files in this repository something like /home/username/TrainWorkflow/helpers/',
                         script='hello.py',
                         compute_target='<compute clustername from script 3.>', environment=env)

run = experiment.submit(config)
aml_url = run.get_portal_url()

print(run.get_details())
print(aml_url)
