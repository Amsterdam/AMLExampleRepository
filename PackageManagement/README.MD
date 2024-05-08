# General Info
This example will scan the requirements.txt file for package upgrades and creates a PR if so.

# Content
This code example consists of an example requirements.txt file. In this file, some outdatated (and vulnerable) packages are present.

Scan.yml contains the pipeline code which uses the dependabot task for automatic review and PR.

# Usage
You can copy the scan.yml and dependabot.yml files in your own project to scan on vulnerabilities.

Information on how to do so can be found [here](https://marketplace.visualstudio.com/items?itemName=tingle-software.dependabot).