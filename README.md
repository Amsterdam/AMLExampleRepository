# AzureMachineLearning

#Intent
This sample script can be used to create a new compute instance in AML.

This new instance will be provisoned with a new kernel which can be used in AML.

#Script analysis (setup.sh):

sudo -u azureuser -i <<'EOF'
If the script is doing something specific to azureuser such as installing conda environment or Jupyter kernel, you'll have to put it within sudo -u azureuser.

ENVIRONMENT=python38
Kernel to be created in AML instance

VERSION=3.8
Python version to be installed in the kernel

conda create -y -n "$ENVIRONMENT" python="$VERSION"
Create the conda environment with name and python version

conda activate "$ENVIRONMENT"
Activate the conda environment

pip install ethereum -v  > ~/cloudfiles/code/Users/<xxx>/"$(date +"%Y_%m_%d_%I_%M_%p")-setup_pip.log"
Example for installing a pip package with output to a log file. This file can be retrieved from the notebook browser in the AML GUI.

pip install ipykernel -v  > ~/cloudfiles/code/Users/<xxx>/"$(date +"%Y_%m_%d_%I_%M_%p")-setup_instance.log"
python -m ipykernel install --name "$ENVIRONMENT" --display-name "$ENVIRONMENT" --user
Install the ipython kernel to be used in the AML instance.

conda deactivate
EOF

#Importing requirementsfile
For recreating / cloning environments, datascientists use the pip freeze command to summup a list of python packages with versions from the running AML instance. This file can be used to recreate a new or clone an environment.

Wiki: https://dev.azure.com/CloudCompetenceCenter/AnalyseSuite/_wiki/wikis/Analyse-Suite.wiki/12235/Setup-script-to-provision-compute-instances
