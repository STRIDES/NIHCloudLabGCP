# How to build a Docker container and push to the Google Artifact Registry

This doc outlines how to create a Docker container and how to push that container to the Google Artifact Registry. The Artifact Registry is Google's newer version of the Container Registry, and allows you to store much more than just containers. Read more [here](https://cloud.google.com/blog/products/application-development/understanding-artifact-registry-vs-container-registry) if interested.

## Create a Google Artifact Registry

1. Navigate to the Artifact Registry Page. It's easiest to just search at the top. 

<img src="/images/1_search_artifact_reg.png" width="550" height="225">

2. Click **CREATE REPOSITORY**

<img src="/images/2_create_registry.png" width="550" height="200">

3. Fill in the details and click create. Select the region where you typically work so that you aren't pulling your container across regions. Click **Create**.

<img src="/images/3_container_details.png" width="550" height="700">

## Build a Docker Container

We are going to use an example [Dockerfile](https://github.com/BioContainers/containers/blob/master/bamtools/2.4.0/Dockerfile) for BAMtools from [BioContainers](https://github.com/BioContainers/containers) to build a quick container just to practice pushing to Artifact Registry. Copy that file locally and save as `Dockerfile`.

From within a compute environment (VertexAI, Compute Engine, or Cloud Shell), run the following: 

`docker build -t bamtools:latest . --no-cache`

Test your container by running it and make sure Bamtools is available. 

`docker run bamtools:latest bamtools -h`

Tag your image to your Google Artifact Registry

`PROJECT=<Your_Project_Here>`

The command will look like: docker tag image:tag region-docker.pkg.dev/PROJECT/RegistryName/image:tag`

`docker tag bamtools:latest us-east4-docker.pkg.dev/$PROJECT/bamtools-example/bamtools:latest`

## Authenticate and Push to Google Artifact Registry

Add your credentials to interact with the Registry. 

`gcloud auth configure-docker us-east4-docker.pkg.dev`

Now push to the Registry.

`docker push us-east4-docker.pkg.dev/$PROJECT/bamtools-example/bamtools:latest`

## Pull the container into a new environment

You can practice pulling the container and make sure it all works as expected. 

`docker pull us-east4-docker.pkg.dev/$PROJECT/bamtools-example/bamtools:latest`

