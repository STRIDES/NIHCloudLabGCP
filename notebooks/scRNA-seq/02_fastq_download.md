# Downloading & Processing Test FASTQ Data for scRNA-seq
## Google Cloud Console + CellRanger 10.0.0

---

> **How to read this guide:**
> - Every line starting with `$` is a command you type in the terminal and press **Enter**
> - Lines starting with `#` are comments — they explain what the next command does. You do NOT need to type them
> - Wherever you see `YOUR_BUCKET_NAME` replace it with your actual bucket name (e.g. `scrna_analysis`)
> - Do steps **in order** — each step builds on the previous one

---

## What Dataset Are We Using?

**PBMC 1k v3** — Human Peripheral Blood Mononuclear Cells (immune blood cells), ~1,000 cells.

| Property | Value |
|---|---|
| Organism | Human |
| Tissue | Blood (immune cells) |
| Expected number of cells | ~1,000 |
| Download size | ~5.2 GB |
| CellRanger run time | ~45–90 minutes |
| Source | 10x Genomics (free, no login needed) |

---



# STEP 1: Set Your Bucket Name Variable

```bash
# Replace YOUR_BUCKET_NAME with your actual bucket name
# Example: BUCKET="gs://scrna_analysis"
BUCKET="gs://YOUR_BUCKET_NAME"

# Confirm it is set correctly
echo $BUCKET
```

> ✅ Should print your bucket path e.g. `gs://scrna_analysis`

---

# STEP 2: Create the CellRanger VM

```bash
# Create a VM with 16 CPUs and ~104GB RAM
gcloud compute instances create cellranger-vm \
  --zone=us-central1-a \
  --machine-type=n1-highmem-16 \
  --boot-disk-size=500GB \
  --boot-disk-type=pd-ssd \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

> ✅ You'll see a table with NAME, ZONE, MACHINE_TYPE, STATUS: RUNNING
>
> ⚠️ **Note:** You may see a warning about disk size being larger than image size — this is safe to ignore. Ubuntu will automatically use the full 500GB.
>
> ❌ If you get an image not found error, try `--image-family=ubuntu-2204-lts` (use 22.04 not 20.04)
>
> ❌ If you get a quota error, try `--machine-type=n1-highmem-8` instead

---

# STEP 3: Log Into the VM

```bash
gcloud compute ssh cellranger-vm --zone=us-central1-a
```

> When prompted:
> - **"Do you want to continue (Y/n)?"** → type `Y` and press Enter
> - **"Enter passphrase (empty for no passphrase):"** → just press Enter
> - **"Enter same passphrase again:"** → just press Enter again
>
> ✅ Your prompt changes to: `YOURUSERNAME@cellranger-vm:~$`
> This means you are now inside the VM.

---

# STEP 4: Install CellRanger

**First, get your download command:**
1. Go to [https://www.10xgenomics.com/support/software/cell-ranger/downloads](https://www.10xgenomics.com/support/software/cell-ranger/downloads)
2. Create a free account or sign in
3. Scroll down to find **"Cell Ranger 10.0.0"**
4. Click the **"Copy"** 📋 button next to the `curl` command in the grey box
5. Paste it into your VM terminal

```bash
# The command you paste will look like this — paste yours, don't type this manually:
curl -o cellranger-10.0.0.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-10.0.0.tar.gz?..."

# Extract it (~828 MB, takes 1-2 minutes)
tar -xzvf cellranger-10.0.0.tar.gz

# Add CellRanger to your PATH so the terminal can find it
export PATH=$PATH:$HOME/cellranger-10.0.0

# Test the installation
cellranger --version
```

> ✅ Should print: `cellranger cellranger-10.0.0`

---

# STEP 5: Download the Human Reference Genome

```bash
# Go to home directory
cd ~

# Download the human GRCh38 reference genome (~11 GB, takes 5-10 minutes)
wget https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz

# Extract it
tar -xzvf refdata-gex-GRCh38-2020-A.tar.gz

# Confirm it's there
ls ~/refdata-gex-GRCh38-2020-A/
```

> ✅ You should see folders: `fasta/`, `genes/`, `star/`
>
> 💡 If CellRanger can't find the genome later, use the full path instead of `~`:
> ```bash
> find ~ -name "refdata-gex-GRCh38*" -type d
> ```
> This prints the full path (e.g. `/home/YOURUSERNAME/refdata-gex-GRCh38-2020-A`) — use that in the CellRanger command.

---
# STEP 7: Download the Test FASTQ Files

```bash
# Create a folder for the test data
mkdir -p ~/test_fastqs/pbmc_1k
cd ~/test_fastqs/pbmc_1k

# Download the PBMC 1k dataset (~5.2 GB, takes 3-5 minutes)
wget https://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_1k_v3/pbmc_1k_v3_fastqs.tar
```

> ✅ You'll see a download progress bar reaching 100%

```bash
# Extract the files
tar -xvf pbmc_1k_v3_fastqs.tar

# Confirm all 6 files are there
ls pbmc_1k_v3_fastqs/
```

> ✅ You should see exactly these 6 files:
> ```
> pbmc_1k_v3_S1_L001_I1_001.fastq.gz
> pbmc_1k_v3_S1_L001_R1_001.fastq.gz
> pbmc_1k_v3_S1_L001_R2_001.fastq.gz
> pbmc_1k_v3_S1_L002_I1_001.fastq.gz
> pbmc_1k_v3_S1_L002_R1_001.fastq.gz
> pbmc_1k_v3_S1_L002_R2_001.fastq.gz
> ```

---

# STEP 8: Upload FASTQ Files to Your Bucket

```bash
# Set your bucket variable (needs to be set again inside the VM)
BUCKET="gs://YOUR_BUCKET_NAME"

# Upload the FASTQ files
gsutil -m cp -r ~/test_fastqs/pbmc_1k/pbmc_1k_v3_fastqs/ ${BUCKET}/raw_fastq/pbmc_1k/

# Verify
gsutil ls ${BUCKET}/raw_fastq/pbmc_1k/
```

> ✅ You should see all 6 `.fastq.gz` files listed in your bucket

---

# STEP 9: Run CellRanger

```bash
# Go back to home directory first
cd ~

# Make sure CellRanger is still in your PATH
export PATH=$PATH:$HOME/cellranger-10.0.0

# Run CellRanger — use full paths (not ~ shortcuts) to avoid errors
cellranger count \
  --id=pbmc_1k_run \
  --create-bam=true \
  --transcriptome=/home/YOURNAME/refdata-gex-GRCh38-2020-A \
  --fastqs=/home/YOURNAME/test_fastqs/pbmc_1k/pbmc_1k_v3_fastqs/ \
  --sample=pbmc_1k_v3 \
  --localcores=16 \
  --localmem=100
```

> ⚠️ **Important notes:**
> - Replace `YOURUSERNAME` with your actual username 
> - `--create-bam=true` is **required** in CellRanger 10.0.0 — older guides may not include it
> - `--sample=pbmc_1k_v3` must exactly match the filename prefix of your FASTQ files
>
> ⏳ This takes **45–90 minutes**. You'll see a live scrolling log — this is normal, just let it run.
>
> ✅ When done you'll see: `Pipestance completed successfully!`

---

# STEP 10: Upload CellRanger Results to Your Bucket

```bash
# Upload the output — note the folder name matches --id=pbmc_1k_run from above
gsutil -m cp -r /home/YOURUSERNAME/pbmc_1k_run/outs/ ${BUCKET}/cellranger_output/pbmc_1k/

# Verify the upload
gsutil ls ${BUCKET}/cellranger_output/pbmc_1k/
```

> ✅ You should see:
> ```
> gs://YOUR_BUCKET_NAME/cellranger_output/pbmc_1k/outs/
> ```

---

# STEP 11: Exit and Delete the VM

**Important:** The VM costs money every minute it's running. Delete it now.

```bash
# Exit the VM — brings you back to Cloud Shell
exit
```

> ✅ Prompt changes back to: `YOURUSERNAME@cloudshell:~ (PROJECT ID)$`

```bash
# If Cloud Shell lost your session, re-authenticate first:
gcloud auth login
gcloud config set project YOUR PROJECT ID

# Then delete the VM
gcloud compute instances delete cellranger-vm --zone=us-central1-a
```

> Type **`Y`** when prompted
> ✅ You'll see: `Deleted [cellranger-vm]`

---

# STEP 12: You're Ready for the Notebook!

All your data is processed and safely stored in GCS. Now move to **Phase 3 of the main guide** to set up your Vertex AI Workbench notebook and run the Python analysis.

Your processed data is at:
```
gs://YOUR_BUCKET_NAME/cellranger_output/pbmc_1k/outs/filtered_feature_bc_matrix/
```

---

# Summary

```
STEP 1  → Open Google Cloud Shell
STEP 2  → Set bucket variable
STEP 3  → Create CellRanger VM (ubuntu-2204-lts)
STEP 4  → Log into VM (Y → Enter → Enter for SSH keys)
STEP 5  → Install CellRanger 10.0.0 (curl command from 10x website)
STEP 6  → Download reference genome (~11 GB)
STEP 7  → Download PBMC 1k FASTQ files (~5.2 GB)
STEP 8  → Upload FASTQs to GCS bucket
STEP 9  → Run CellRanger (--create-bam=true required, use full paths)
STEP 10 → Upload results to GCS bucket
STEP 11 → Exit VM, re-authenticate if needed, delete VM
STEP 12 → Move to main guide Phase 3 (Notebook setup)
```

---

# Estimated Time & Cost

| Step | Time | Cost |
|---|---|---|
| VM creation | 2–3 min | Free |
| CellRanger install | 5 min | ~$0.10 |
| Reference genome download | 5–10 min | ~$0.20 |
| FASTQ download | 3–5 min | ~$0.10 |
| CellRanger run | 45–90 min | ~$1–3 |
| GCS storage | Ongoing | ~$0.10/month |
| **Total** | **~1.5–2 hours** | **~$2–4** |

Proceed to:

➡️ [03_vertex_workbench.md](03_vertex_workbench.md)
