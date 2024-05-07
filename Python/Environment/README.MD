#Intent
This sample code will show sample code on how to use build a new environment by using a custom docker image. 

##Please note

The code below is only required to be set one time. This will enable the Workspace to build images on the specified compute instance or cluster.

We do recommend to use a dedicated cluster for your team to build your images on.

```
ws.image_build_compute ="testcluster"
ml_client.workspaces.begin_update(ws)
```