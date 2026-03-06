# Step 1 – Google Cloud Environment Setup

This step prepares your Google Cloud environment for the scRNA-seq pipeline.

By the end of this section, you will have:

- A configured GCP project  
- Required APIs enabled  
- A Cloud Storage (GCS) bucket  
- A standard folder structure for this tutorial  

---

## Prerequisites

- A Google Cloud account with billing enabled  
- A GCP project already created  
- Access to the Google Cloud Console  

---

## 1. Open Google Cloud Console

1. Navigate to: https://console.cloud.google.com  
2. Sign in with your Google account.  
3. Click the **Cloud Shell** icon in the top-right corner.  

A terminal will open at the bottom of the page. You should see:

```bash
yourusername@cloudshell:~ (your-project-id)$
```

---

## 2. Confirm Your Active Project

All resources must be created inside the correct GCP project.

Check your current project:

```bash
gcloud config get-value project
```

If it returns nothing or the wrong project, set it manually:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with your actual project ID.

Verify:

```bash
gcloud config list
```

---

## 3. Enable Required APIs

The following services are required for this tutorial:

- Compute Engine (for VMs)  
- Cloud Storage  
- Vertex AI Workbench (Notebooks)  
- Vertex AI / AI Platform  
- Batch (optional but useful)  

Run:

```bash
gcloud services enable \
  compute.googleapis.com \
  storage.googleapis.com \
  notebooks.googleapis.com \
  aiplatform.googleapis.com \
  batch.googleapis.com
```

This may take 1–2 minutes. Wait for confirmation messages for each service.

---

## 4. Create a Cloud Storage Bucket

Choose a globally unique bucket name.

### Bucket Naming Rules

- Lowercase letters only   
- No spaces  
- Must be globally unique  

Example:

```bash
gsutil mb -l us-central1 gs://scrna_analysis_yourname
```

Replace `scrna_analysis_yourname` with your chosen bucket name.

Verify the bucket exists:

```bash
gsutil ls
```

You should see your new bucket listed.

---

## 5. Create Standard Folder Structure

Set an environment variable for convenience:

```bash
BUCKET="gs://scrna_analysis_yourname"
```

Create placeholder directories (empty `.keep` files so folders show up in GCS):

```bash
echo "" | gsutil cp - ${BUCKET}/raw_fastq/.keep
echo "" | gsutil cp - ${BUCKET}/cellranger_output/.keep
echo "" | gsutil cp - ${BUCKET}/analysis/.keep
echo "" | gsutil cp - ${BUCKET}/results/.keep
```

Verify the structure:

```bash
gsutil ls ${BUCKET}
```

Expected output:

```
analysis/
cellranger_output/
raw_fastq/
results/
```

---

## Completed

Your Google Cloud environment is now configured and ready for the next steps.

Proceed to: ➡️ [02_fastq_download.md](02_fastq_download.md)
