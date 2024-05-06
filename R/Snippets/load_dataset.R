# How to use a tabular file from storage account in R.

# Upload the file you want to use in R in AML to the **data storage account** 
# as a tabular dataset (APi v1) in Azure ML.

# Reference: https://azure.github.io/azureml-sdk-for-r/reference/index.html

# Cell 1
library(azuremlsdk)
ws = get_workspace("xxxx-weu-aml-o-xxx", resource_group = "xxx-aml-x-rg", subscription_id = "xxxxx-xxxxx-")
ds = get_dataset_by_name(ws, "datasetname", version = "1")
load_dataset_into_data_frame(ds)

# Run cell
