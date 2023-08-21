# How to configure auto-shutdown on GCP Virtual Machines
This guide walks you through how to automatically configure auto-shutdown capabilities on any GCP virtual machine. Put simply, you only need to add a startup script that shuts down the VM after a specified period of inactivity. This safeguard helps ensure you don't forget to shut off your VM over the weekend, and accidentally burn through a big chunk of your budget.

## 1. Configure auto-shutdown on Vertex AI Notebook Instance
When starting a new [VertexAI notebook instance](/docs/vertexai.md), you can attach a startup script directly that will stop instances after they drop below a specified CPU threshold. We hosted a script in a public bucket that shuts down your machine after it drops below 30% CPU usage for more than 30 minutes. If you would like to modify the script, all you need to do is copy it, modify it, then copy it to your own Google Cloud Storage bucket. Then you can point to your modified script in the startup script box. 

**Create new instance** 

  ![create new vertex ai instance](/images/1_create_new_instance_CL.png)

**Select Advanced Options**

  ![select advanced options](/images/2_select_advanced_options.png)

**Enter startup script path**

We hosted this script in a public bucket, so if you want to modify it, just use this command `gsutil cp gs://nigms-sandbox/scripts/idle-shutdown.sh` and modify the `threshold` parameter to make the CPU threshold more or less sensitive, and the `wait_minutes` parameter to control how long you want the VM idle before shutting down. 
  ![shutdown parameters](/images/3_enter_startupscript_path.png)
  
For additional details on the other settings for user managed notebooks, see [this VertexAI Quickstart](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/create-user-managed-notebooks-instance-console-quickstart).

## 2. Configure auto-shutdown on Compute Engine VM
Configuring auto-shutdown on a Compute Engine VM is very simple. When you are spinning up the instance, simply add [this script](idle-shutdown.sh) to the startup script metadata. If you already have a VM, you can simply edit it, add the script, then restart the VM. After your specified period of inactivity, the VM will shut down. 

If editing an existing VM, click Edit.

<img src="/images/edit_vm.png" width="550" height="600">

Then add startup script as metadata.

<img src="/images/edit_startup.png" width="550" height="600">
