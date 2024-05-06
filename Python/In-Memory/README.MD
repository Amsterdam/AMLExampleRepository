#Intent
This sample code will show sample code on how to use in-memory data analysis. 
As datastores do not natively support this, the Azure blob API is used.

#Prerequisites
Please install the preview version of the Python SDK. This version is compatible with the new V2 of the Azure ML CLI.

pip install --pre azure-ai-ml
pip show azure-ai-ml

#Workflow
The script will execute the following:
1. Use an existing dataset from a datastore and transform it to a pandas dataset
2. Do transformations for this dataset
3. Get the blob service client from the blob API
   1. Note the token_credential here. A token will be used directly from the compute instance which has access to the data storage account Do not give your own credentials here!
4. List all containers that are available for us to use
5. Use one of the container names that were available for upload
6. Upload the blob as csv 

We also show how to get a stream of data directly from the blob storage.
1. Get the blob by name
2. Download the blob as a String and save it to the local hard drive of the compute instance

#Usage
This code can be used directly in notebooks, jobs or Python scripts. Please note the following parameters that have to be filled in:

- **<SUBSCRIPTION_ID>:** Subscription ID where the AML workspace lives. You can find it by using ``az account list``
- **<RESOURCEGROUP_NAME>**: Resource group name where the AML workspace lives. You can find it in the Azure Portal
- **<AML_WORKSPACE_NAME>**: The name of the workspace. You can find it when logged into the AML workspace
- **<BLOB_SERVICE_ENDPOINT>:** The endpoint of the blob service from the **Data storage account**. You can find it by using ``az storage account show --name <datastorageaccountname> --query "primaryEndpoints.blob"``