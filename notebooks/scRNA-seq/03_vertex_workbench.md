# Step 3 – Set Up Vertex AI Workbench (Jupyter Notebook)

**Goal:** Create a cloud-based Python environment where we will run our scRNA-seq analysis using Scanpy.

> ⚠️ Make sure you have completed:
> - `01_gcp_setup.md`
> - `02_cellranger_and_fastq_download.md`
>
> Your count matrix should already be stored in:
> ```
> gs://YOUR_BUCKET_NAME/cellranger_output/pbmc_1k/outs/filtered_feature_bc_matrix/
> ```

---

# Part 1 – Create a Vertex AI Workbench Instance (Using the Console)

## 1. Open Vertex AI

1. Go to: https://console.cloud.google.com  
2. Make sure your correct project is selected (top blue bar).  
3. Click the **Navigation Menu (☰)** in the top-left.  
4. Scroll down and click **Vertex AI**.  

---

## 2. Go to Workbench

1. In the left sidebar under Vertex AI, click **Workbench**.   
2. Click the **Create New** button.  

---

## 3. Configure Your Notebook Instance

Use the following settings:

### Instance Name
```
scrna_notebook
```

### Region / Zone
- Region: `us-central1` (or your preferred region)
- Zone: `us-central1-a` (or your preferred zone)

### Machine Type

For the PBMC 1k test dataset:

- **Machine type:** `n1-highmem-8` (recommended minimum)
- OR `n1-highmem-16` if available

> 💡 High memory is important for scRNA-seq datasets.

### Boot Disk

- Size: **200 GB**
- Type: SSD

---

## 4. Click “Create”

The instance will take about **3–5 minutes** to provision.

When ready:

- Status will show a **green check**
- The instance name will appear in the list

---

# Part 2 – Open JupyterLab

1. In the Workbench list, find `scrna-notebook`
2. Click **Open JupyterLab**

A new browser tab will open.

You are now inside your notebook VM.

> ✅ You should see the JupyterLab interface  
> Left panel = file browser  
> Center panel = Launcher  

---

# Part 3 – Install Required Python Packages

In this section, you will open a terminal inside your JupyterLab environment, clone the course repository, and install the required Python packages.

---

## 1. Open a Terminal in JupyterLab

1. Click the **"+"** button (Launcher).
2. Scroll down to the **Other** section.
3. Click **Terminal**.

A new terminal window will open.

You should see a prompt similar to:

```
jupyter@instance:~$
```

⚠️ Make sure this terminal is running inside your **notebook VM**.  
Do **not** use Cloud Shell for these steps.

---

## 2. Clone the Course Repository

In the JupyterLab terminal, run:

```bash
git clone https://github.com/STRIDES/NIHCloudLabGCP.git
```

This will create a directory called:

```
NIHCloudLabGCP/
```

Navigate into the notebooks directory:

```bash
cd NIHCloudLabGCP/notebooks/scRNAseq
```


## 3. Install Required Libraries

Run:

```bash
pip install scanpy anndata leidenalg python-igraph \
            matplotlib seaborn scikit-learn \
            pandas numpy scipy scrublet celltypist
```

This takes 3–5 minutes.

When finished, you should see:
```
Successfully installed scanpy-...
```

---

# Part 4 – Copy the Count Matrix from GCS

Still inside the JupyterLab terminal:

```bash
# Create local folder
mkdir -p ~/data/pbmc_1k/

# Copy count matrix from your bucket
gsutil -m cp -r \
  gs://YOUR_BUCKET_NAME/cellranger_output/pbmc_1k/outs/filtered_feature_bc_matrix/ \
  ~/data/pbmc_1k/
```

Verify:

```bash
ls ~/data/pbmc_1k/filtered_feature_bc_matrix/
```

You should see:

```
barcodes.tsv.gz
features.tsv.gz
matrix.mtx.gz
```

These three files are your processed gene count matrix.

---

# Part 5 – Next Step

Now proceed to:

➡️ `05_scrna_analysis.ipynb`

You are ready to:

- Load the 10x matrix
- Perform QC
- Normalize
- Cluster
- Annotate cell types

---

# Cost Control Reminder

When you are done working for the day:

1. Go back to **Vertex AI → Workbench**
2. Select `scrna-notebook`
3. Click **Stop**

Stopping the instance pauses billing but keeps your data.

To permanently delete it later:
- Click **Delete**

---

# Where You Are in the Pipeline

```
01_gcp_setup.md        ✅ Infrastructure
02_cellranger_and_fastq_download.md   ✅ FASTQ files ✅ Count matrix generated
03_vertex_workbench.md  ← You are here
04_scrna_analysis.ipynb  ← Next step
```
