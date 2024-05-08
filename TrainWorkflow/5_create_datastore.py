from azureml.core import Workspace, Datastore

ws = Workspace.from_config()

# Register a new datastore
blob_ds = Datastore.register_azure_blob_container(workspace=ws,
                                                  datastore_name='<aml datastore name>',
                                                  container_name='<containername>',
                                                  account_name='<storage accountname>',
                                                  account_key='') # Leave accountkey empty

for ds_name in ws.datastores:
    print(ds_name)


# You can also skip this step if you already have a datastore in AML.