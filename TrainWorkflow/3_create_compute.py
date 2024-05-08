from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config()

# Choose a name for your CPU cluster
# CPU name must be between 2 and 16 characters
cpu_cluster_name = "<insert_clustername_to_be_created>"

# Verify that the cluster does not exist already
try:
    cpu_cluster = ComputeTarget(workspace=ws, name=<insert_cpu_cluster_name>)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2',
                                                           idle_seconds_before_scaledown=1200,
                                                           min_nodes=1,
                                                           max_nodes=1, enable_node_public_ip=False, vnet_name='<vnet-name>',
                                                            vnet_resourcegroup_name='<vnet_resource_groupname>',
                                                             subnet_name='<subnetname>', identity_type='SystemAssigned')
    cpu_cluster = ComputeTarget.create(ws, cpu_cluster_name, compute_config)
    cpu_cluster.wait_for_completion

cpu_cluster.wait_for_completion(show_output=True)
