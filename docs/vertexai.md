# Using VertexAI Notebooks

### Spin up a User-Managed VertexAI Notebook Instance
1. Start by clicking the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. 

  ![selectvertexai](/images/1_select_vertexAI.png)

2. Click **Create New**

  ![1_create_new_notebook](/images/1_create_new_notebook.png)

3. Select **Advanced Options** at the bottom of the window that pops up.

   ![advanced options](/images/2_select_advanced_options.png)
  
4. Name your notebook a globally unique name. Note that in GCP you can only use dash, not underscore. For region select the region closest to where you live, or else the region where your data is stored. If you plan to use a managed service that is only available in a particular region, go ahead and select `us-central` as your region. Click **Continue**.

  ![2_select_notebook_name](/images/3_select_notebook_name.png)

5. On the _Environment_ tab, select `Debian 11` and select your desired Environment. Many of the tutorials specify a recommended environment. Don't worry about a startup script or metadata. Click **Continue**.
   
6. Under _Machine type_ select your desired number of CPUs/GPUs. This is usually specified by the tutorial you are completing.
   
7. On the same page, click **Enable Idle Shutdown** and specify the idle minutes for shutdown. This means, if you close your browser and walk away without stopping your instance, it will shutdown automatically after this many minutes. We recommend 30 minutes.

  ![autoshutdown](/images/4_enable_auto_shutdown_mins.png)

8. It will take a few minutes for your new notebook environment to spin up. Once the status changes from a blue spinning ball to `Open JUPYTERLAB` then your VM is ready. You may need to click `Refresh` at the top of the page to see the status change. That is a good rule of thumb on GCP; if you are waiting on something to spin up, try clicking refresh and it may already be done. 

  ![launch notebook](/images/5_launch_notebooks.png)


### (Bonus) Using the new Managed Notebooks feature
At the time of writing, Google had just rolled out a new feature in Vertex AI called `Managed Notebooks`, which now differ from the `User Managed Notebooks`. You can use either one for this tutorial, but the nice thing about the new `Managed Notebooks` is that you can schedule them, or just execute them similar to submitting a job to a slurm cluster. Read the documentation for [scheduling a notebook](https://cloud.google.com/vertex-ai/docs/workbench/managed/schedule-managed-notebooks-run-quickstart). Note that scheduled notebooks will be run on remote compute resources, so you need to treat them like a fresh install, copy your data in, install all packages, etc. Don't expect that because you have data/dependencies copied to your current environment they will be present when your scheduled notebook is run. Also, when you spin up the Managed Notebook, make sure you select `Single User` rather than Service Account to avoid permission conflicts. You can also resize the machine on the fly (without shutting down), and there are some extra compute environments available. However, we have observed that conda is tightly controlled on these machines, so if you decide to try them and have issues with conda, switch back to the User Managed Notebooks.

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

