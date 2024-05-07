import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azureml.core.authentication import MsiAuthentication

keyVaultName = "as-platform-weu-x-x"
KVUri = f"https://as-platform-weu-x-xxxxx.vault.azure.net/"
secretName = "secretname"
secretValue = "secretvalue"

# credential = DefaultAzureCredential(managed_identity_client_id="xxxxx")
credential = DefaultAzureCredential(workspaceId="xxxxxxxxxxxx")
client = SecretClient(vault_url=KVUri, credential=credential)

print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")
print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(secretName)
print(f"Your secret is '{retrieved_secret.value}'.")
print(f"Deleting your secret from {keyVaultName} ...")

# poller = client.begin_delete_secret(secretName)
# deleted_secret = poller.result()

print(" done.")