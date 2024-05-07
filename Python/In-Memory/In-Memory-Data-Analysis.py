# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

"""
In-Memory-Data-Analysis.py shows a way to transfer data without saving it onto the compute SSD.
Thus, transfering data directly in-memory.
"""

token_credential = DefaultAzureCredential()
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCEGROUP_NAME>'
workspace_name = '<AML_WORKSPACE_NAME>'

# Get workspace
workspace = Workspace(subscription_id, resource_group, workspace_name)

# Get dataset
dataset = Dataset.get_by_name(workspace, name='parquettest')
df = dataset.to_pandas_dataframe()

# Perform transformation
transformed = df.groupby(by=["gender", "country"]).mean()

# Get the blob store
blob_service_client = BlobServiceClient(
    account_url="<BLOB_SERVICE_ENDPOINT>",
    credential=token_credential
)

# Get containers
containers = blob_service_client.list_containers()
for container in containers:
    print(container.name)

# Uploading new blob in-memory
container = blob_service_client.get_container_client(container="testtest")
container.upload_blob(name="transformed_data", data=transformed.to_csv())

# Get blob as csv
blob = blob_service_client.get_blob_client(container="testtest", blob="transformed_data")
str = blob.download_blob()
with open('transformed.csv', 'w') as f:
    f.write(str.content_as_text())

#Open the new csv from disk
import pandas as pd
pd.read_csv("transformed.csv")