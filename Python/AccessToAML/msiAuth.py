from azureml.core.authentication import MsiAuthentication

msi_auth = MsiAuthentication()

#Enter details of your AzureML workspace
subscription_id = 'xxxxxxxxx'
resource_group = 'as-aml-x-rg'
workspace = 'as-weu-aml-x-xxxxxxxxxx'

ws = Workspace(subscription_id,
               resource_group,
               workspace_name,
               auth=msi_auth)

print("Found workspace {} at location {}".format(ws.name, ws.location))