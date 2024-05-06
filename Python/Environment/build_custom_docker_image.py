#import required libraries for workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

#import required libraries for environments examples
from azure.ai.ml.entities import Environment, BuildContext


"""
build_custom_docker_image.py will build a custom docker image by using a conda.yml file
or DockerFile
"""

#Enter details of your AzureML workspace
subscription_id = 'xxxxxxxxxx'
resource_group = 'as-aml-x-rg'
workspace = 'as-weu-aml-x-xxxxxxxx'

#connect to the workspace
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)

ws=ml_client.workspaces.get(name=workspace)

# Update workspace to use a compute cluster or instance for building images on, this compute cluster
# can only be provided by Team Analyse Services as a preprovisioned build cluster. To setup this feature,
# please send a change request to Team TAS and refer to the feature preprovison buildcluster. 
# This is a one time setup, where we advice to use a dedicated cluster for building new images
# When using this feature in AML, you should 
ws.image_build_compute = "defaultBuildClusterAs"

# This following entry becomes obsolete when using a predefined / preprovisoned buildcluster.
#ml_client.workspaces.begin_update(ws)


# The path of the buildcontext should be a dedicated folder containing the Dockerfile
env_docker_context = Environment(
    build=BuildContext(path="./Python/Environment/Docker", dockerfile_path='DockerFile'),
    name="docker-context-example",
    description="Environment created from a Docker context."
)
ml_client.environments.create_or_update(env_docker_context)