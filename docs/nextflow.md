### Running Nextflow on GCP with the Life Sciences API
You can learn to run Nextflow on GCP following these [instructions](https://cloud.google.com/life-sciences/docs/tutorials/nextflow).

You can skip most of the section titled 'Create a service account and add roles', except the part called 'Provide credentials to your application', you still need to do that part. You are unable to create or modify service accounts within Cloud Lab, so we added the necessary permissions to the Compute Engine default service account for you. Thus, you need to authenticate using the credentials of the Compute Engine default service account. You can get the json key following [these instructions](https://cloud.google.com/iam/docs/creating-managing-service-account-keys), but in brief, go to `IAM & Admin`. On the left menu click `Service Account`, click on `Compute Engine default service account`, at the top go to `Keys`. Select `Add Key` and then `Create new key`. 

Now that you have a json file, authenticate the service account with `export GOOGLE_APPLICATION_CREDENTIALS=./YOURKEYNAMEHERE.json`

All that is left is to set your project ID with `Need to gcloud config set project $projectID`, and then the rest of the tutorial should be smooth sailing. If you have any issues, reach out to Cloud Lab support. 

