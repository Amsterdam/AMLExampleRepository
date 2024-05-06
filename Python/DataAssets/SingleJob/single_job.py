from azure.ai.ml import command
from azure.ai.ml.entities import Data, IdentityConfiguration, Environment
from azure.ai.ml import Input, MLClient
from azure.ai.ml.constants import AssetTypes, ManagedServiceIdentityType
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

"""
single_job.py is created train a single job with the Python SDK V2
It is using a user assigned managed identity which can be used with any kind of compute
"""
class AMLWorkspace:
    def __init__(self, identity_config: IdentityConfiguration):
        self.identity_config = identity_config
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient.from_config(credential=self._connect())

    def _connect(self) -> MLClient:
        """
        Connects to the ML workspace and other components using the Managed Identity of the workspace
        """
        try:
            credential = DefaultAzureCredential()
            # Check if given credential can get token successfully.
            credential.get_token("https://management.azure.com/.default")
        except Exception as ex:
            # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
            # This will open a browser page for
            credential = InteractiveBrowserCredential()
        
        
        return credential

    def create_environment(self, env: Environment) -> None:
        """
        Creates a new Docker image and environment.
        """
        self.ml_client.environments.create_or_update(env)

    def create_job(self, job: command) -> None:
        """
        Submits a job to the workspace.
        """
        self.ml_client.jobs.create_or_update(job)

# create identity
identity_config = IdentityConfiguration(type=ManagedServiceIdentityType.USER_ASSIGNED)
aml = AMLWorkspace(identity_config)

# create environment
env_docker_conda = Environment(
    image="mcr.microsoft.com/azureml/curated/acpt-pytorch-1.12-py38-cuda11.6-gpu:4",
    conda_file="conda.yaml",
    name="testenvironment",
    description="Environment created from a Docker image plus Conda environment.",
)

# create the environment 
aml.create_environment(env_docker_conda)

# get the registered dataset
registered_data_asset = aml.ml_client.data.get(name="testtest", version="1")
job_inputs = {
    "dataset": Input(type=AssetTypes.URI_FILE, path=registered_data_asset.id)
}

# create the job
job = command(
    code=".", 
    command="python hello.py --dataset ${{inputs.dataset}}",
    inputs=job_inputs,
    environment=env_docker_conda.name + "@latest",
    compute="test-test2",
    identity=aml.identity_config.user_assigned_identities
)

# submit the job
aml.create_job(job)