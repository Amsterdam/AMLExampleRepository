# !NOTE!
# This is a PoC, this feature is not yet supported by Analyse Services.

# This script sets up a managed online endpoint.
# For more/other examples, check the example repo for AML:
# https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints

# Import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration,
)
from azure.identity import DefaultAzureCredential

# Enter details of your AML workspace
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace = "<AML_WORKSPACE_NAME>"

# Connect to workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)

# Create a unique endpoint name with current datetime to avoid conflicts
import datetime

online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")

# Create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is a sample online endpoint",
    auth_mode="token",
    tags={"foo": "bar"},
    public_network_access="disabled",  # Disable public network access, because the workspace is inside private network
)

ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Create a deployment in the endpoint
model = Model(path="../model-1/model/sklearn_regression_model.pkl")
env = Environment(
    conda_file="../model-1/environment/conda.yml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
)

blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=online_endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="../model-1/onlinescoring", scoring_script="score.py"
    ),
    instance_type="Standard_DS2_v2",
    instance_count=1,
    egress_public_network_access="disabled",  # Disable public network access, because the workspace is inside private network
)

ml_client.online_deployments.begin_create_or_update(blue_deployment).result()

# Set percentage of traffic that should go to the 'blue' deployment
endpoint.traffic = {"blue": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
