#import required libraries for workspace
from azure.ai.ml import MLClient
from azureml.core.authentication import MsiAuthentication
from azure.identity import DefaultAzureCredential

#import required libraries for environments examples
from azure.ai.ml.entities import Environment, BuildContext

#Enter details of your AzureML workspace
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCEGROUP_NAME>'
workspace_name = '<AML_WORKSPACE_NAME>'
msi_auth = MsiAuthentication()

# #connect to the workspace
# ws = Workspace (
#     subscription_id, 
#     resource_group, 
#     workspace, 
#     auth
#     )

#connect to the workspace
ml_client = MLClient(MsiAuthentication(), subscription_id, resource_group, workspace)

ws=ml_client.workspaces.get(name=workspace)