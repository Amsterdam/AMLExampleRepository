# AzureMachineLearning

# Introduction

Welcome to our example code repository for Azure Machine Learning.
This repository is created for all our customers working on Azure Machine Learning environments.

To run the code examples in this package, you may need specific packages. You can install those using the `requirements.txt` file, for example run:

```
pip install -r requirements.txt
```

Note that (as of Nov 16th, 2022) the `requirements.txt` may not be complete.

# Content

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
