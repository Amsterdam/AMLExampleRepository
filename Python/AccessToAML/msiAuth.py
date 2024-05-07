from azureml.core.authentication import MsiAuthentication

msi_auth = MsiAuthentication()

#Enter details of your AzureML workspace
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCEGROUP_NAME>'
workspace_name = '<AML_WORKSPACE_NAME>'

ws = Workspace(subscription_id,
               resource_group,
               workspace_name,
               auth=msi_auth)

print("Found workspace {} at location {}".format(ws.name, ws.location))