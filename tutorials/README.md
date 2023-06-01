# GCP Tutorial Resources

_We have pulled together a variety of tutorials here from disparate sources. Some use Compute Engine, others use Vertex AI notebooks and others use only managed services. Tutorials are organized by research method, but we try to designate what GCP services are used as well to help you navigate._
---------------------------------
## Overview of Page Contents

+ [Biomedical Workflows on GCP](#bds)
+ [Medical Imaging](#mi)
+ [Machine Learning](#ml)
+ [Download SRA Data](#sra)
+ [Variant Calling](#vc)
+ [VCF Query](#vcf)
+ [GWAS](#gwas)
+ [Proteomics](#pro)
+ [RNAseq](#rna)
+ [scRNAseq](#sc)
+ [BLAST](#bl)
+ [Long Read Sequencing Analysis](#long)
+ [Using the Life Sciences API](#lsapi)
+ [Public Data Sets](#pub)

## **Biomedical Workflows on GCP** <a name="bds"></a>

There are a lot of ways to run workflows on GCP. Here we list a few possibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using one of the other methods listed here.

- The simplest method is probably to spin up a Compute Engine instance, and run your command interactively, or using `screen` or, as a [startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) attached as metadata.
- You could also run your pipeline via a Vertex AI notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). [Schedule notebooks](https://codelabs.developers.google.com/vertex_notebook_executor#0) to let them run longer.
You can find a nice tutorial for using managed notebooks [here](https://codelabs.developers.google.com/vertex_notebook_executor#0). Note that there is now a difference between `managed notebooks` and `user managed notebooks`. The `managed notebooks` have more features and can be scheduled, but give you less control about conda environments/install. 
- You can interact with `Google Life Sciences API` using a workflow manager like [Nextflow](https://cloud.google.com/life-sciences/docs/tutorials/nextflow), [Snakemake](https://snakemake.readthedocs.io/en/stable/executing/cloud.html), or [Cromwell](https://github.com/GoogleCloudPlatform/rad-lab/tree/main/modules/genomics_cromwell). If you are running the Nextflow tutorial, please first reference our [docs](/docs/nextflow.md) for how to get Nextflow running in Cloud Lab. We currently have [example notebooks](/tutorials/notebooks/LifeSciencesAPI/) for both Nextflow and Snakemake that use the Life Sciences API.
- You may find other APIs better suite your needs such as the [Google Cloud Healthcare Data Engine](https://cloud.google.com/healthcare).
- Most of the notebooks below require just a few CPUs. Start small (maybe 4 CPUs), then scale up as needed. Likewise, when you need a GPU, start with a smaller or older generation GPU (e.g. T4) for testing, then switch to a newer GPU (A100/V100) once you know things will work or you need more horsepower. 

## **Medical Image Segmentation** <a name="mi"></a>
Medical imaging analysis requires the analysis of large image files and often requires elastic storage and accelerated computing.
- Most medical imaging analyses are done in notebooks, so we would recommend downloading the Jupyter Notebook from [here](/tutorials/notebooks/SpleenLiverSegmentation) and then importing or cloning it into VertexAI. The tutorial walks through image segmentation using the Monai framework.
- You can also request early access to the new [Google Medical Imaging Suite](https://cloud.google.com/medical-imaging) to see if it would fit your use case.

## **Machine Learning** <a name='ml'></a>
Machine learning on GCP generally occurs within VertexAI. You can learn more about machine learning on GCP at this [Google Crash Course](https://developers.google.com/machine-learning/crash-course). 

## **Download Data From the Sequence Read Archive (SRA)** <a name="sra"></a>
Next Generation genetic sequence data is housed in the NCBI Sequence Read Archive (SRA). You can access these data using the SRA Toolkit. We walk you through this using [this notebook](/tutorials/notebooks/SRADownload), including how to use BigQuery to generate your list of Accessions. You can also use BigQuery to create a list of accessions for download using [this setup guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-bigquery/) and this [query guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-bigquery-examples/). Additional example notebooks can be found at this [NCBI repo](https://github.com/ncbi/ASHG-Workshop-2021). In particular, we recommend this notebook(https://github.com/ncbi/ASHG-Workshop-2021/blob/main/1_Basic_BigQuery_Examples.ipynb), which goes into more detail on using BigQuery to access the results of the SRA Taxonomic Analysis Tool, which often differ from the user input species name due to contamination, error, or due to samples being metagenomic in nature. Further, [this notebook](https://github.com/ncbi/ASHG-Workshop-2021/blob/main/2_Array_Examples.ipynb) does a deep dive on parsing the BigQuery results and may give you some good ideas on how to best search for samples from SRA. The SRA metadata and taxonomy analyses are in separate BigQuery tables, you can learn how to join those two tables using SQL from [this Powerpoint](https://github.com/NCBI-Codeathons/NCGAS-cloud-workshop/blob/main/5_BigQuery.pptx). Finally, NCBI released [this workshop](https://github.com/ncbi/workshop-asm-ngs-2022/wiki) in 2022 that walks through a wide variety of BigQuery applications with NCBI datasets, we highly recommend you take a look.

## **Variant Calling** <a name="vc"></a>
Variation in our DNA sequence to large extent determines a person's traits, propensity for disease, etc. Genomic variant calling is the identification of this DNA sequence variation for a given individual.
- This [Google tutorial](https://cloud.google.com/life-sciences/docs/tutorials/gatk) shows you how to run the GATK Best Practices pipeline for genomic variant calling using the Life Sciences API. There is a section about increasing your account quotas, you can skip that. You could also run GATK using any of the workflow managers and submitting to the Life Sciences API.
- One tutorial specific to somatic variant calling comes from the Sheffield Bioinformatics Core [here](https://sbc.shef.ac.uk/somatic-variants/index.nb.html). It runs on Galaxy, but can be adapted to run in GCP. At the very least, the [data](https://drive.google.com/drive/folders/1RhrmfW3vMhPwAiBGdFIKfINWMsdvIG6E) may prove useful to you.

## **Query a VCF file in Big Query** <a name="vcf"></a>
The output of genomic variant calling workflows is a file in the variant call format (VCF). These are often large, structured data files that can be searched using database query tools.
- Learn how to use Big Query to run queries against large VCF files from Gnomad data using [this notebook](https://github.com/GoogleCloudPlatform/rad-lab/blob/main/modules/data_science/scripts/build/notebooks/Exploring_gnomad_on_BigQuery.ipynb). If any cells give you errors, try running that cell again and it should work, there seems to be some lag time between cells.

## **Genome Wide Association Studies** <a name="gwas"></a>
Genome wide association studies, or GWAS, are statistical analyses that estimate associations between genomic variants and phenotypic traits.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using AWS, thus we have rewritten it as a notebook to work on GCP [here](/tutorials/notebooks/GWASCoatColor). Make sure you select R as your kernel when you spin up your notebook so that you can switch between R and Python (this only applies to 'User Managed Notebooks') but note that our team experienced conda permission issues with the new Managed Notebooks for this tutorial, so we recommend using the 'User Managed Notebooks'. Also, if the imported notebook has cells already printed out, just go to Kernel > Restart Kernel and Clear all Outputs.
- [This tutorial](https://github.com/david-thrower-nih/DL-gwas-gcp-example) from NIH NIEHS (credit to David Thrower) builds on a published deep learning method for GWAS of soybeans and users Kubeflow and AutoML on a Kubernetes instance. 

## **Proteomics** <a name="pro"></a>
Proteomics is the study of the proteome, which is the complement of a person's proteins. Although most primary proteomic analyses occur in proprietary software platforms, a lot of secondary analysis happens in Jupyter or R notebooks, which is what we demo here.
- Use Big Query to run a Kruskal Wallis Test on Proteomics data using [these notebooks](https://github.com/isb-cgc/Community-Notebooks/tree/master/FeaturedNotebooks). Clone the repo into Vertex AI, or just drag the notebooks into a Vertex AI Workbench instance. In the notebook titled 'ACM_BCB_2020_POSTER_KruskalWallisTest_ProteinGeneExpression_vs_ClinicalFeatures.ipyng', the first BigQuery cell may throw an error, but ignore this and keep going, the rest of the notebook should run fine. Also, in that first big cell, make sure you add your Project ID. See this [doc](/docs/protein_setup.md) for environment setup instructions.
- Run AlphaFold in Vertex AI using [this notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/community-content/alphafold_on_workbench/AlphaFold.ipynb). Make sure you have a GPU for your notebook instance, and follow [these instructures](https://cloud.google.com/blog/products/ai-machine-learning/running-alphafold-on-vertexai) for setting up your environment. Namely, under Environment, select `Custom container`, and then for `Docker container image` paste in the following: `west1-docker.pkg.dev/cloud-devrel-public-resources/alphafold/alphafold-on-gcp:latest`.

## **RNAseq** <a name="rna"></a>
RNAseq is a technique for quantifying gene levels of gene expression across the genome. Workflows are typically run using workflow managers, and final results can often be visualized in notebooks.
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/3.7) for RNAseq a variety of ways on GCP. Following the instructions outlined above, you could use Compute Engine, [Life Sciences API](https://cloud.google.com/life-sciences/docs/tutorials/nextflow), or in Vertex AI notebook.
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification go through these tutorials from the [NIGMS Sandbox Project](https://github.com/NIGMS/RNAseqUM) developed by The University of Maine INBRE.

## **Single Cell RNAseq** <a name="sc"></a>
Single Cell RNAseq (scRNAseq) analyses allow for gene expression profiling at the single cell level.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub repository that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks and it can be challenging to get set up. 
-  The [Scanpy tutorials](https://scanpy.readthedocs.io/en/stable/tutorials.html) page has a lot of good CPU-based examples you could run in Vertex AI. Clone this [GitHub repo](https://github.com/scverse/scanpy-tutorials) to get the notebooks directly.
-  Alternatively, here is a [GitHub repository](https://github.com/mdozmorov/scRNA-seq_notes) with a curated list of scRNAseq resources and tutorials. We did not test these in cloud lab, but wanted to make them available in case you needed additional resources. 

## **BLAST** <a name="bl"></a>
- This [Common Data Fund](https://training.nih-cfde.org/en/latest/Cloud-Platforms/Introduction-to-GCP/gcp3/) tutorial explains how to use basic BLAST on GCP.
- We also rewrote [this ElastBLAST tutorial](https://blast.ncbi.nlm.nih.gov/doc/elastic-blast/quickstart-gcp.html) as a [notebook](/tutorials/notebooks/elasticBLAST) that will work in VertexAI. 

## **Long Read Sequence Analysis** <a name="long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short read sequencing where reads are about 150 bp in length. Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. You can find a list and description of notebooks [here](https://labs.epi2me.io/nbindex/), or clone the [GitHub repo](https://github.com/epi2me-labs/tutorials/tree/master/tutorials). Note that these notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands.

## **Using the Life Sciences API** <a name="lsapi"></a>
You can interact with the the Life Sciences API directly to submit commands, or more commonly you can interact with it through orchestration engines like [Snakemake](https://snakemake.readthedocs.io/en/stable/executing/cloud.html), [Nextflow](https://www.nextflow.io/docs/latest/google.html), [Cromwell](https://cromwell.readthedocs.io/en/stable/backends/Google/) etc. We currently have two tutorials using [Snakemake](/tutorials/notebooks/LifeSciencesAPI/snakemake/) which runs the University of Maine RNAseq workflow, and [Nextflow](/tutorials/notebooks/LifeSciencesAPI/nextflow) where we run the nf-core Methylseq pipeline.

## **Public Data Sets** <a name="pub"></a>
Google has a lot of public datasets available that you can use for your testing. These can be viewed [here](https://cloud.google.com/life-sciences/docs/resources/public-datasets) and can be accessed via [BigQuery](https://cloud.google.com/bigquery/public-data) or directly from the cloud bucket. For example, to view Phase 3 1000 Genomes at the command line type `gsutil ls gs://genomics-public-data/1000-genomes-phase-3`. 

