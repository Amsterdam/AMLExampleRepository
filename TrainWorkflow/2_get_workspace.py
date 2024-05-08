from azureml.core import Workspace

# This automatically looks for a directory .azureml, or pass the location where you stored the file.
ws = Workspace.from_config()
details = ws.get_details()
print(details)
