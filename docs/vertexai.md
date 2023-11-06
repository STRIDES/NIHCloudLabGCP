# Using VertexAI Notebooks

Google Cloud offers three flavors of Notebook instances: User-Managed, Google Managed, and Instances. User-Managed instances offer the most flexibility in terms of installing local software via conda/mamba or launching from custom containers. [Google Managed](https://cloud.google.com/vertex-ai/docs/workbench/managed/introduction) and [Instances](https://cloud.google.com/vertex-ai/docs/workbench/instances/introduction) allow for 'on the fly' machine resizing and notebook scheduling, as well as not worrying about resource availability, but they run in a tenant project (rather than your project) and offer less flexibility for installing custom software. Most machine-learning related software are pre-installed, but these can be hard to use for a lot of bioinformatic tasks where you need to install CLI tools with conda.

### Spin up a User-Managed Notebook Instance
1. Start by clicking the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. 

  ![selectvertexai](/images/1_select_vertexAI.png)

2. Click **Create New**

  ![1_create_new_notebook](/images/1_create_new_notebook.png)

3. Select **Advanced Options** at the bottom of the window that pops up.

   ![advanced options](/images/2_select_advanced_options.png)
  
4. Name your notebook a globally unique name. Note that in GCP you can only use dash, not underscore. For region select the region closest to where you live, or else the region where your data is stored. If you plan to use a managed service that is only available in a particular region, go ahead and select `us-central` as your region. Click **Continue**.

  ![2_select_notebook_name](/images/3_select_notebook_name.png)

5. On the _Environment_ tab, select `Debian 11` and select your desired Environment. Many of the tutorials specify a recommended environment. Don't worry about a startup script or metadata. Click **Continue**.
    - The following environments are configured for **GPU use**.

    ![GPU environments](/images/GPU_environments.png)
   
6. Under _Machine type_ select your desired number of CPUs/GPUs. This is usually specified by the tutorial you are completing. 

- **Follow the steps below if you are utilizing GPUs:** 
    - Click on the GPU dropdown menu and select your GPU processor

    ![GPU processors](/images/GPU_processor.png)
    - Then check mark where it says **'Install NVIDIA GPU driver automatically for me'** to have your notebook automatically install GPU drivers.
    - Finally select the number of GPUs you wish to utilize. The number of GPUs varies from machine type and GPU processor selected.
    
    ![Number of GPUs](/images/GPU_numbers.png)
   
7. On the same page, click **Enable Idle Shutdown** and specify the idle minutes for shutdown. This means, if you close your browser and walk away without stopping your instance, it will shutdown automatically after this many minutes. We recommend 30 minutes.

  ![autoshutdown](/images/4_enable_auto_shutdown_mins.png)

8. It will take a few minutes for your new notebook environment to spin up. Once the status changes from a blue spinning ball to `Open JUPYTERLAB` then your VM is ready. You may need to click `Refresh` at the top of the page to see the status change. If you get the following error, `The zone XYZ does not have enough resources available to fulfill the request` then try launching from a different zone.

  ![launch notebook](/images/5_launch_notebooks.png)

9. You can edit your instance by clicking on the instance name.

  ![click_instance_name](/images/6_select_instance_vertexai.png)

10. Now you can modify any of the instance settings, like resizing your machine or attaching additional disk storage.

    ![resize image](/images/7_resizevertexaiimage.png)


### Spin up a Google-Managed VertexAI Notebook Instance
The way of spinning up a notebook is the same as above. The main differences you will observe with Google Managed and Instances Notebooks is the resizing on the fly, a nice BigQuery integration, and the inability to install anything via conda/mamba.

### Import custom notebook and data

1. Now click the git icon on the middle left bar (it kind of looks like the letter 'T' with a tilt). Click `Clone a Repository`, and then paste `https://github.com/STRIDES/NIHCloudLabGCP.git` into the box. You can also open a terminal and paste in the following:

```
git clone https://github.com/STRIDES/NIHCloudLabGCP.git
```

<img src="/images/1_clone_repo_gcp.png" width="550" height="400">

2. Now you have the NIHCloudLabGCP directory available. Navigate to NIHCloudLabGCP > tutorials > notebooks > GWASCoatColor > GWAS_coat_color.ipynb.
Explore this notebook and see how data moves into and out of the Vertex AI environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu. You can easily switch between different kernels in the top right. If you had selected Python3 when starting the instance, you would only have access to Python, but would need a different instance to open or create an R notebook for example. However, if you start with R, then can switch between R and Python. After finishing this notebook, move onto the SRA_and_BigQuery notebook to learn about some key GCP skills, 
like importing (SRA) data, making a cloud storage bucket and moving data in and out of the bucket, and finally how to query VCF files with BigQuery.

<img src="/images/2_GWAS_notebook.png" width="550" height="350">

Here are a few tips if you are new to notebooks: The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

Another thing worth noting is that when you run a cell, sometimes it doesn't produce any output; however, processes are running in the background. If the brackets next to a cell have an * then it is still running. You can also look at the bottom where the kernel is listed (e.g., Python 3 | status) and it will show either Idle or Busy depending on whether anything is running or not. 

<img src="/images/3_busy_cell.png" width="550" height="550">


```python

```
