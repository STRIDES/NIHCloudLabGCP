# How to configure auto-shutdown on GCP Virtual Machines
This guide walks you through how to automatically configure auto-shutdown capabilities on any GCP virtual machine. Put simply, you only need to add a startup script that shuts down the VM after a specified period of inactivity. This safeguard helps ensure you don't forget to shut off your VM over the weekend, and accidentally burn through a big chunk of your budget.

## 1. Configure auto-shutdown on Compute Engine VM
Configuring auto-shutdown on a Compute Engine VM is very simple. When you are spinning up the instance, simply add [this script](idle-shutdown.sh) to the startup script metadata. If you already have a VM, you can simply edit it, add the script, then restart the VM. After your specified period of inactivity, the VM will shut down. 

If editing an existing VM, click Edit.

<img src="/images/edit_vm.png" width="200" height="150">

Then add startup script as metadata.

<img src="/images/edit_startup.png" width="200" height="150">

## 2. Configure auto-shutdown on Vertex AI Notebook Instance
To configure auto-shutdown on a notebook instance, you need to first spin up a [notebook instance](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/create-user-managed-notebooks-instance-console-quickstart) in Vertex AI. Then, to add the startup script, navigate to Compute Engine, and edit the instance following the instructions shown above. You will need to restart the VM, navigate back to Vertex AI, and reopen the Jupyter Instance. You only need to do this once per instance. 
