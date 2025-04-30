# How to configure auto-shutdown on GCP Virtual Machines
This guide walks you through how to automatically configure auto-shutdown capabilities on any GCP virtual machine. Put simply, you only need to add a startup script that shuts down the VM after a specified period of inactivity. This safeguard helps ensure you don't forget to shut off your VM over the weekend, and accidentally burn through a big chunk of your budget.

## 1. Configure auto-shutdown on Vertex AI Notebook Instance
When starting a new VertexAI notebook, you can enable idle shutdown by navigating to **Advanced options** and checking the box for enabling auto-shutdown. You must specify the amount of time you want your machine idle before it shuts down. See our [VertexAI startup guide](/docs/vertexai.md) to see how to enable this important feature. 

![image showing idle shutdown selection](/images/images_for_creating_GCP_instances/6_instance_idle_shutdown.png) 

For additional details on the other settings for user managed notebooks, see [this VertexAI Quickstart](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/create-user-managed-notebooks-instance-console-quickstart).

## 2. Configure auto-shutdown on Compute Engine VM
Configuring auto-shutdown on a Compute Engine VM is very simple. When you are spinning up the instance, simply add [this script](idle-shutdown.sh) to the startup script metadata. If you already have a VM, you can simply edit it, add the script, then restart the VM. After your specified period of inactivity, the VM will shut down. 

If editing an existing VM, click Edit.

<img src="/images/edit_vm.png" width="550" height="600">

Then add startup script as metadata.

<img src="/images/edit_startup.png" width="550" height="600">
