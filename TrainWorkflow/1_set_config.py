from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

#Enter details of your AzureML workspace
tenant_id = '<TENANT_ID>'
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCEGROUP_NAME>'
workspace_name = '<AML_WORKSPACE_NAME>'

ia= InteractiveLoginAuthentication(tenant_id=tenant_id,force=True)
ws = Workspace.get(name=workspace_name,subscription_id=subscription_id, resource_group=resource_group,auth=ia)
ws.write_config(path='.azureml')
