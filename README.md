# AzureMachineLearning

## Introduction

Welcome to our example code repository for Azure Machine Learning.
This repository is created for all our customers working on Azure Machine Learning environments.

To run the code examples in this package, you may need specific packages. You can install those using the `requirements.txt` file, for example run:

```
pip install -r requirements.txt
```

Note that (as of Nov 16th, 2022) the `requirements.txt` may not be complete.

## Contributing to this repository

The intend of this repository is to promote collaboration between the Datascientists and the AML DevOps engineers. These code snippets can be used in notebooks (local with VSCode or AML notebooks).
Using this repository requires a certain workflow.

### Submit sample code to the repository

- If you use this repository for the first time than please clone the repository to your (local) environment
- When repository is already cloned in your evvironment, please pull the latest version of the repository by submitting the git pull command on the main branch
- Use your favorite GUI for submitting the code to this repository
- Create a new branch in this repository
- Make the code adjustment or insert the new code examples
- Make sure you don't push code containing secrets or other sensitive data
- Commit and push the code to the repository
- Your GUI will ask if you want to create a pull request or go to the Github repoitory page and create the PR
- This PR will be peer reviewed by the DevOps team of AIDA
- After review the PR will be merged in to the main branch

## Content

Subjects with a checkmark have been placed in this repository and are fully tested.

1. Package Management - :white_check_mark:
   1. Using pipelines for package management - :white_check_mark:
2. AML Code examples in Python, consisting of:
   1. Datastores / Datasets - &#x2610;
      1. Connecting to datastores and datasets - :white_check_mark:
      2. Uploading data to datastores (also data storage account) - &#x2610;
      3. Gathering samples of data from datasets - &#x2610;
      4. Creating /removing datasets - &#x2610;
   2. Compute instances and clusters - &#x2610;
      1. Creating /removing computes and clusters - &#x2610;
      2. Creating jobs for clusters/instances - :white_check_mark:
      3. Creating / removing pipelines - &#x2610;
   3. Models - &#x2610;
      1. Registering / Downloading models - &#x2610;
      2. Archiving models - &#x2610;
      3. Deploying as an endpoint - :white_check_mark:
   4. Data connections - &#x2610;
      1. Connecting to external APIs - :white_check_mark:
      2. Connecting to Postgres databases - &#x2610;
   5. Environments
      1. Creating a new custom environment by using Dockerfiles :white_check_mark:
3. Azure ML CLI examples that will enable the above - &#x2610;

Please contact us if you have interesting user-flows we can use as an example in this repository.

Import notes, please never add the following items to our repository:

- secrets
- tokens
- subscription id's
- usernames
- resources groups
- ip adresses
- workspacename
