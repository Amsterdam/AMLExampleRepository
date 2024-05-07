from azureml.core import Workspace

subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCEGROUP_NAME>'
workspace_name = '<AML_WORKSPACE_NAME>'

# Get workspace
ws = Workspace(subscription_id, resource_group, workspace_name)

# Retrieved from Azure Machine Learning web UI
run_id = 'aaaaaaaa-bbbb-cccc-dddd-0123456789AB'
experiment = ws.experiments['my-experiment']
run = next(run for run in experiment.get_runs() if run.id == run_id)
metrics_output_port = run.get_pipeline_output('metrics_output')
model_output_port = run.get_pipeline_output('model_output')

metrics_output_port.download('.', show_progress=True)
model_output_port.download('.', show_progress=True)