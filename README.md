# NIH Cloud Lab for GCP
---------------------------------

>This repository falls under the NIH STRIDES Initiative. STRIDES aims to harness the power of the cloud to accelerate biomedical discoveries. To learn more, visit https://cloud.nih.gov. 

There are a lot of resources available to learn about GCP, which can be overwhelming. NIH Cloud Lab’s goal is to make cloud very easy and accessible for you, so that you can stop wasting time on administrative tasks and focus on your research.

Use this repository to learn about how to use GCP by exploring the linked resources and walking through the tutorials. If you are a beginner, we suggest you begin with this Jumpstart section. If you already have foundational knowledge of GCP and cloud, feel free to skip ahead to the [tutorials](/tutorials/) section for in-depth examples of how to run specific workflows such as genomic variant calling and medical image analysis.


## Overview of Page Contents

+ [Getting Started](#GS)
+ [Overview](#OV)
+ [Command Line Tools](#CLI)
+ [Ingest and Store Data](#STO)
+ [Virtual Machines](#VM)
+ [Disk Images](#IM)
+ [Jupyter Notebooks](#JUP)
+ [Creating Conda Environments](#CO)
+ [Serverless Functionality](#SER)
+ [Clusters](#CLU)
+ [Billing and Benchmarking](#BB)
+ [Getting Support](#SUP)
+ [Additional Training](#TR)

## **Getting Started** <a name="GS"></a>
You can learn a lot of what is possible on GCP in the [GCP Getting Started Page](https://cloud.google.com/getting-started). There you can find links to [documentation](https://cloud.google.com/docs) for common GCP tools and resources, and short videos on various subjects called [cloud minute](https://www.youtube.com/playlist?list=PLIivdWyY5sqIij_cgINUHZDMnGjVx3rxi).

Even with a wealth of resources it can be difficult to know where to start on learning how to use the cloud. To help you, we thought through some of the most common tasks you will encounter doing cloud-enabled research and gathered tutorials and guides specific to those topics. We hope the following materials are helpful as you explore migrating your research to the cloud.

## **Overview** <a name="OV"></a>
There are three primary ways you can run analyses using GCP: using virtual machines, Jupyter Notebook instances, and Serverless services. We give a brief overview of each of these here and go into more detail in the sections below. [Virtual machines](https://cloud.google.com/compute) are like your desktop computers, but you access them through the cloud console and you get to decide what resources are on that computer such as CPU and memory. In GCP, the platform that hosts these virtual machines is called Compute Engine. You access VMs via SSH (secure remote connections), either through the console or via the command line. Jupyter Notebook instances are virtual machines with Jupyter Lab preloaded onto them. On GCP these are run through [Vertex AI](https://cloud.google.com/vertex-ai). You decide what kind of virtual machine you want to 'spin up' and then you can run Jupyter notebooks on that virtual machine. You access these notebooks through the console similar to the way you interact with Jupyter locally. Finally, serverless services are services allow you to run things, an analysis, an app, a website, and not have to deal with your own servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background and copies the output files to a storage bucket. The most common serverless feature you will work with here is the [Life Sciences API](https://cloud.google.com/life-sciences/docs/reference/rest). Typically, these workflows are run from the command line, either from a VM, Cloud Shell, or your local terminal.

## **Command Line Tools** <a name="CLI"></a>
One other task that will enable all that comes below is installing and configuring the GCP SDK command line tools, which will allow you to interact with instances or Google Storage buckets from your local terminal. Command line interface (CLI) tools are those that you use directly in a terminal/shell as opposed to clicking within a graphical user interface (UI). Instructions for installing the CLI can be found [here](https://cloud.google.com/sdk/docs/install). Along the same lines, it is important to familiarize yourself with the two main CLI commands: [gcloud](https://cloud.google.com/sdk/docs/cheatsheet) and [gsutil](https://cloud.google.com/storage/docs/quickstart-gsutil). There are also other commands you may come across in some circumstances like [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/). If you have trouble installing the CLI on your local computer, you can still use the same commands from a virtual machine or from [Cloud Shell](https://cloud.google.com/shell), which is a terminal environment available to users on the GCP console.

## **Ingest and Store Data using Google Cloud Storage** <a name="STO"></a>
Data can be stored in two places on the cloud, either in a cloud storage bucket, which on GCP is called Google Cloud Storage (GCS), or on an instance, which usually has Elastic Block Storage. In general, you want to keep your compute and storage separate, so you should aim to storage data in GCS for access, then only copy the data you need to a particular instance to run an analysis, then copy the results back to GCS. In addition, the data on an instance is only available when the instance is running, whereas the data in GCS is always available. [Here](https://cloud.google.com/storage/docs/quickstart-console) is a great tutorial on how to use GCS and is worth going through to learn how it all works.

We also wanted to give you a few other tips that may be helpful when it comes to moving and storing data. If your end goal is to move data to a GCS bucket, you can do that using the UI and clicking the `Upload Files` button from within a bucket, or you can use the command line by typing `gsutil cp <FILE> <gs://BUCKET>`. Of course, you need to first create the bucket, which you can do using the instructions in the tutorial linked above. If you want to move a whole folder, then use the recursive flag: `gsutil cp -r <DIR> <gs://BUCKET>`. The same applies whether moving data from your local directory or from a VM. Likewise, you can move data from GCS back to your local machine or your VM with `gsutil cp <gs://BUCKET/FILE> <DESTINATION/PATH>`. To multithread a gsutil action, use the `-m` flag, for example: `gsutil -m -r <Dir> <gs://BUCKET>`. Finally, if you are trying to move data from the Short Read Archive (SRA) to an instance, or to GCS, you can use [fasterq_dump](https://github.com/glarue/fasterq_dump) from the SRA toolkit. The best way is probably to install on an instance, then copy the data to SSD, then optionally copy it to GCS for backup or use elsewhere. See our [notebook](/tutorials/notebooks/SRADownload/) for an example.

Another important aspect of managing data storage costs is to be strategic about storing data in GCP vs. on your instances. When you have spun up a VM, you have already paid for the storage on the VM since you are paying for the size of the disk (storage space), whereas bucket storage is charged based on how much data you put in GS. This is something to think about when copying results files back to GCS for example. If they are not files you will need later, then leave them on the VM's local storage and save your money on more important data to put in GCS. Just make sure you are always either backing up by creating a machine image (see below) or keeping data you can't live without in cloud storage.

## **Spin up a Virtual Machine and run a workflow** <a name="VM"></a>
Google and other sources have a lot of great resources on how to spin up and use a VM. The first place we will point you is to the [NIH Common Data Fund resource](https://training.nih-cfde.org/en/latest/Cloud-Platforms/Introduction-to-GCP/gcp2/), which lays out how to spin up a VM, SSH into it, make a bucket, and move data around similar to what we did in the example notebooks above. One thing worth noting is that the NIH tutorial has you SSH into your instance using a gcloud command in the shell. This is a good way to SSH in, but it is a lot easier to just double click the SSH button next to the instance name on the Compute Instances page. You can find the GCP specific documentation on how to spin up an instance [here](https://cloud.google.com/compute/docs/instances/create-start-instance#console). If you want to start a Windows VM, read [the documentation](https://cloud.google.com/compute/docs/quickstart-windows). Windows VMs can have extra costs associated with them, so make sure you understand what you are getting into before starting.

## **Disk Images** <a name="IM"></a>
Part of the power of virtual machines is that they offer a blank slate for you to configure as desired. However, sometimes you want to recycle data or installed programs for your next VM instead of having to reinvent the wheel. One solution to this issue is using disk (or machine) images, where you copy your existing virtual disk to a [Machine Image](https://cloud.google.com/compute/docs/machine-images) which can serve as a backup or can be used to launch a new instance with the programs and data from a previous instance.

## **Launch a Jupyter Notebook** <a name="JUP"></a>
[Jupyter notebooks](https://github.com/STRIDES/NIHCloudLabGCP/edit/main/README.md) are web based interactive code platforms. On GCP, notebooks are launched through the Vertex AI platform. Here we are going to launch a JupyterLab environment on GCP, and then import a custom notebook from this repo to walk through running commands in Vertex AI. Vertex AI is where Google is moving with Machine Learning and Artificial Intelligence workflows. You can read more about a [Vertex AI Overview](https://cloud.google.com/vertex-ai) and [technical documentation and tutorials](https://cloud.google.com/vertex-ai/docs). 

To begin, click on the `hamburger menu` (the three horizontal lines in the top left of your console). Go to `Artificial Intelligence > Vertex AI > Workbench`. Click `New Notebook` and select `R 4.1` for the kernel, although note that you can use a variety of environments including Python, R, PyTorch, TensorFlow and others. This can also be changed later. Name your notebook a globally unique name. Note that in GCP you can only use dash not underscore. For region select the region closest to where you live, or else the region where your cloud storage bucket is.

Now click the pencil icon next to `Notebook properties`. For operating system select 'Debian 10', for 'Environment' select your desired Environment. This where you can change this if you selected something different before. Under `Machine configuration > Machine type` select your machine type. For this tutorial you can get away with using `e2-standard-4`, but you will likely want a more powerful machine for other workflows. Read more about machine families on GCP [here](https://cloud.google.com/compute/docs/machine-types), about the specifics of general purpose machine types within machine families [here](https://cloud.google.com/compute/docs/general-purpose-machines). You can follow the links in those doc pages for Compute, Memory, or Accelerator optimized machine types as well. You can figure out the cost of your selected machine [here](https://cloud.google.com/compute/all-pricing). _Remember that as long as your notebook is running (and not stopped) you will be charged per second of use. This is especially important to remember for GPU machines as these will consume your budget quickly._ Leave all other settings as default and click `Create`. 

It will take a few minutes for your new notebook environment to spin up so go brew some coffee and come back. Once the status changes from a blue spinning ball to `Open JUPYTERLAB` then your VM is ready. You may need to click `Refresh` at the top of the page to see the status change. That is a good rule of thumb on GCP; if you are waiting on something to spin up, try clicking refresh and it may already be done. 

### (bonus) Using the new Managed Notebooks feature
At the time of writing, Google had just rolled out a new feature in Vertex AI called `Managed Notebooks`, which now differ from the `User Managed Notebooks`. You can use either one for this tutorial, but the nice thing about the new `Managed Notebooks` is that you can schedule them, or just execute them similar to submitting a job to a slurm cluster. Read the documentation for [scheduling a notebook](https://cloud.google.com/vertex-ai/docs/workbench/managed/schedule-managed-notebooks-run-quickstart). Note that scheduled notebooks will be run on remote compute resources, so you need to treat them like a fresh install, copy your data in, install all packages etc. Don't expect that because you have data/dependencies copied to your current environment they will be present when your scheduled notebook is run. Also, when you spin up the managed notebook, make sure you select single users rather than Service Account to avoid permission conflicts.

### Import custom notebook and data
Once you have opened your notebook instance, note that on the left side of the page, you will see `tutorials`. You can explore these example notebooks to get a feel for the environment, and also learn some best practices for notebooks. Now from the base directory, click the git icon on the middle left bar, it kind of looks like the letter 'T' with a tilt. Click `Clone a Repository`, and then paste the following into the box: 

```
git clone https://github.com/STRIDES/NIHCloudLabGCP.git
```
Now you have the NIHCloudLabGCP directory available. Navigate to NIHCloudLabGCP > tutorials > notebooks > GWASCoatColor > GWAS_coat_color.ipynb.
Explore this notebook and see how data moves in and out of the VertexAI environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu. We can easily switch between different kernels in the top right. If you had selected Python3 when starting the instance, you would only have access to Python, but would need a different instance to open or create an R notebook, but if you start with R, then can switch between R and Python. After finishing this notebook, move onto the SRA_and_BigQuery notebook to learn about some key GCP skills like importing (SRA) data, making a cloud storage bucket and moving data in and out of the bucket, and finally how to query VCF files with BigQuery.

Here's a few tips if you are new to notebooks. The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

It is also worth noting that when you run a cell, sometimes it doesn't produce any output, but things are running in the background. If the brackets next to a cell have an * then it is still running. You can also look at the bottom where the kernel is listed (e.g., Python 3 | status) and it will show either Idle or Busy depending on if anything is running or not. 

## **Creating a Conda Environment** <a name="CO"></a>
Virtual environments allow you to manage package versions without having package conflicts. For example, if you needed Python 3 for one analysis, but Python 2.7 for another, you could create separate environments to use the two versions of Python. One of the most popular package managers used for creating virtual environments is the [conda package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing). 

Mamba is a reimplementation of conda written in C++ and runs much faster than legacy conda. Conda environments are created using configuration files in yaml format (yaml is a type of configuration file), where you specify the name of the environment, the conda channels to search, and then the programs to install. You can optionally specify a version for each program, or just list the name and have the default version installed. For example, `- bwa` or `- bwa ==0.7.17` with both install version `0.7.17`, but you could list a different version as needed. Further, some programs you may need do not play well with conda or are simply not available. If you run into lots of errors while trying to install something, consider installing via pip (python package manager) or downloading a binary (precompiled version of software). Make sure if you install anything in addition to the conda environment, you do it after activating the environment. If you are within a notebook, adding mamba to your path can act up sometimes. Either use the full path to the mamba executable or do all the environment creation/activation steps in the terminal (access from the launcher window).


To create the conda environment, first install mamba:
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge
```
Now add mamba to your path.
```
export PATH="$HOME/mambaforge/bin:$PATH"
```
List your current conda environments.
```
conda info --envs 
```
Now create the conda environment with all of your desired packages. Note that the file name doesn't matter if you have the name designation at the top of the yaml file. If you don't name the environment in the yaml, then it will be named whatever your file is named. Or you can add a -n flag to name the environment (`mamba env create -f environment.yaml -n your_name_of_choice`).
```
mamba env create -f envs/environment.yaml
```
Now list your environments again to find the path of your new environment.
```
conda info --envs 
```
Now activate your environment using the path printed from the previous command. 
```
source activate $ENVPATH
```
Now test your environment by running one of the programs you just installed. For example, type `bwa` (if you installed bwa!).

## **Serverless Functionality** <a name="SER"></a>
Serverless services are those that allow you to run things, an analysis, an app, a website etc., and not have to deal with servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background and copies the output files to a storage bucket. The most relevant serverless feature on GCP to Cloud Lab users (especially 'omics' analyses) is the [Google Cloud Life Sciences API](https://cloud.google.com/life-sciences/docs/reference/rest). You can walk through a tutorial of this service using this [notebook](/tutorials/notebooks/LifeSciencesAPI) Those doing health informatics should look into the [Google Cloud Healthcare Data Engine](https://cloud.google.com/healthcare). You can find a variety of other [tutorials](https://cloud.google.com/life-sciences/docs/tutorials) that leverage the Life Sciences API for life sciences applications, but we will point out that most of the examples are related to genomics. If you are doing other biomedical research related to imaging, NLP, or other fields, look at the [tutorials](/tutorials/) section of this repo for inspiration. Some of these also leverage the API from within the notebooks. Besides the Google-specific examples, you can use the Life Sciences API to run workflows using other workflow managers like [Snakemake](https://snakemake.readthedocs.io/en/stable/executing/cloud.html) or [Nextflow](https://cloud.google.com/life-sciences/docs/tutorials/nextflow). Google also just released a new service in preview called [Batch](https://cloud.google.com/blog/products/compute/new-batch-service-processes-batch-jobs-on-google-cloud) which is a scheduling service that should feel similar to submitting jobs to a cluster. 

## **Clusters** <a name="CLU"></a>
One great thing about the cloud is its ability to scale with demand. When you submit a job to a traditional computing cluster (a set of computers that work together to execute a function), you have to specify up front how many CPUs and Memory you want to give to your job, and you may over or under utilize these resources. Alternatively, on the cloud you can leverage a feature called autoscaling, where the compute resources will scale up or down with the demand. This is more efficient and keeps costs down when demand is low, but prevents latency when demand is high (think Black Friday shopping on a website). For most users of Cloud Lab, the best way to leverage scaling is to use an API like the Life Sciences API, but in some cases, maybe for a whole lab group or a large project, it may make sense to spin up a [Kubernetes cluster](https://cloud.google.com/kubernetes-engine/docs/quickstart) and submit jobs to the cluster using a workflow manager like [Snakemake](https://snakemake.readthedocs.io/en/stable/executing/cloud.html). 

## **Billing and Benchmarking** <a name="BB"></a>
Many Cloud Lab users are interested in understanding how to estimate the price of a large-scale project using a reduced sample size. Generally, you should be able to benchmark with a few representative samples to get an idea of time and cost required for a larger scale project. In terms of cost, the best way to estimate costs is to use the [GCP cost calculator](https://cloud.google.com/products/calculator#id=b64e9c4f-c637-432f-8e2c-4a7238dde0f2) for an initial figure. The calculator is a tool that estimates costs based on location, VM type/size, and runtime. Then, you can run some benchmarks and double check that everything is acting as you expect. For example, if you know that your analysis on your on-premises cluster takes 4 hours to run for a single sample with 12 CPUs, and that each sample needs about 30 GB of storage to run a workflow, then you can extrapolate out how much everything may cost using the calculator (e.g., compute engine + cloud storage). 

To get a more precise estimate, you can use assign labels to your workflows, then generate a report for a specific label. You can learn how to do that in our [docs](docs/How%20to%20Create%20Labels%20and%20GCP%20Billing%20Report.docx.pdf). Note that it can take up to 24 hours to update the billing account, so you may need to wait a few hours after running an analysis before you will have an accurate report.

## **Cost Optimization** <a name="COST"></a>
As you go through all the tutorials, you can keep costs down by stopping and/or deleting resources (e.g. VMs or Buckets) you no longer need. Another strategy is to ensure that you are using all the compute resources you have provisioned. If you spin up a VM with 16 CPUs, you can see if they are all being utilized using [Cloud Monitoring](https://cloud.google.com/monitoring#section-1). If you are only really using 8 CPUs for example, then just change your machine size to fit the analysis. Finally, you can play with [Spot](https://cloud.google.com/spot-vms) instances for running workflows and end up saving a lot of money. 

## **Getting Support** <a name="SUP"></a>
As part of your participation in Cloud Lab you will be added to the Cloud Lab Teams channel where you can chat with other Cloud Lab users, and gain support from the Cloud Lab team. For NIH Intramural users, you can submit a support ticket to Service Now. For all other users, you can reach out to the Cloud Lab email with questions at `CloudLab@nih.gov`. Please be sure for tickets and email to have a clear Subject line, such as AWS help with Nextflow and BATCH. For issues our team is unable to resolve, you can reach out to AWS support directly by clicking the question mark in the top right part of the console. 

## **Additional Training** <a name="TR"></a>
This repo only scratches the surface of what can be done in the cloud. If you are interested in additional cloud training opportunities, please visit the [STRIDES Training page](https://cloud.nih.gov/training/). For more information on the STRIDES Initiative at the NIH, visit [our website](https://cloud.nih.gov/) or contact the NIH STRIDES team at STRIDES@nih.gov for more information.
