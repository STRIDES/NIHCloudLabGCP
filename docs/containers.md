# How to build a Docker container and push to the Google Artifact Registry

This doc outlines how to create a Docker container and how to push that container to the Google Artifact Registry. The Artifact Registry is Google's newer version of the Container Registry, and allows you to store much more than just containers. Read more [here](https://cloud.google.com/blog/products/application-development/understanding-artifact-registry-vs-container-registry) if interested.

## 1. Build a Docker Container

We are going to use an example [Dockerfile](https://github.com/BioContainers/containers/blob/master/bamtools/2.4.0/Dockerfile) for BAMtools from [BioContainers](https://github.com/BioContainers/containers) to build a quick container just to practice pushing to Artifact Registry. Copy that file locally and save as `Dockerfile`.

From within a compute environment (VertexAI, Compute Engine, or Cloud Shell), run the following: 

`docker build -t bamtools:latest . --no-cache`

Test your container by running it and make sure Bamtools is available. 
docker run -it bamtools:latest

#tag to google repo
docker tag nf-tower:0.04 us-east4-docker.pkg.dev/us-gcp-ame-adv-c01-npd-1/nextflow-tower-automation/nf-tower:1.04
```

## 2. Authenticate and Push to Google Artifact Registry
gcloud auth configure-docker us-east4-docker.pkg.dev
docker push us-east4-docker.pkg.dev/us-gcp-ame-adv-c01-npd-1/nextflow-tower-automation/nf-tower:1.04


<img src="/images/launch_terminal.png" width="550" height="400">

### Install mamba
```
