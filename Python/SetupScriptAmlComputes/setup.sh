#!/bin/bash

set -e

# This script installs a pip package in compute instance python38 environment.

sudo -u azureuser -i <<'EOF'
ENVIRONMENT=python38
VERSION=3.8
conda create -y -n "$ENVIRONMENT" python="$VERSION"
conda activate "$ENVIRONMENT"
pip install ethereum -v  > ~/cloudfiles/code/Users/<xxx>/"$(date +"%Y_%m_%d_%I_%M_%p")-setup_pip.log"
pip install ipykernel -v  > ~/cloudfiles/code/Users/<xxx>/"$(date +"%Y_%m_%d_%I_%M_%p")-setup_instance.log"
python -m ipykernel install --name "$ENVIRONMENT" --display-name "$ENVIRONMENT" --user
conda deactivate
EOF