# GCP Tutorial Resources

_We have pulled together a variety of tutorials here from disparate sources. Some use Compute Engine, others use Vertex AI notebooks and others use only managed services. Tutorials are organized by research method, but we try to designate what GCP services are used as well to help you navigate._
---------------------------------
## Overview of Page Contents

+ [Biomedical Workflows on GCP](#Bio)
+ [Variant Calling](#VC)
+ [VCF Query](#VCF)
+ [GWAS](#GWAS)
+ [Proteomics](#PRO)
+ [Medical Imaging](#IM)
+ [RNAseq](#RNA)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#Long)
+ [Public Data Sets](#Pub)

## **Biomedical Workflows on GCP** <a name="VC"></a>

There are a lot of ways to run workflows on GCP. Here we list a few posibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using one of the other methods listed here.

- The most simple method is probably to spin up a Compute Engine instance, and run your command interactively, or using `screen` or, as a [startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) attached as metadata.
- You could also run your pipeline via a Vertex AI notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). See [here](https://codelabs.developers.google.com/vertex_notebook_executor#0) about scheduling a notebook to let it run longer.
You can find a nice tutorial for using managed notebooks [here](https://codelabs.developers.google.com/vertex_notebook_executor#0). Note that there is now a difference between `managed notebooks` and `user managed notebooks`. The `managed notebooks` have more features and can be scheduled. 
- You can interact with `Google Life Sciences API` using a workflow manager like [Nextflow](https://cloud.google.com/life-sciences/docs/tutorials/nextflow), [Snakemake](https://snakemake.readthedocs.io/en/stable/executing/cloud.html), or [Cromwell](https://github.com/GoogleCloudPlatform/rad-lab/tree/main/modules/genomics_cromwell).
- You may find other APIs better suite your needs such as the [Google Cloud Healthcare Data Engine](https://cloud.google.com/healthcare).

## **Variant Calling** <a name="VC"></a>
- This [Google tutorial](https://cloud.google.com/life-sciences/docs/tutorials/gatk) shows you how to run GATK Best Practices using the Life Sciences API. There is a section about increasing your account quotas, you can skip that. You could also run GATK using any of the workflow managers and submitting to the API as described in the links one section above.
- One tutorial specific to somatic variant calling comes from the Sheffield Bioinformatics Core [here](https://sbc.shef.ac.uk/somatic-variants/index.nb.html). It runs on Galaxy, but can be adapted to run in GCP. At the very least, the [data](https://drive.google.com/drive/folders/1RhrmfW3vMhPwAiBGdFIKfINWMsdvIG6E) may prove useful to you.

## **Query a VCF file in Big Query** <a name="VCF"></a>
- Learn how to use Big Query to run queries against large VCF files from Gnomad data using [this notebook](https://github.com/GoogleCloudPlatform/rad-lab/blob/main/modules/data_science/scripts/build/notebooks/Exploring_gnomad_on_BigQuery.ipynb). If any cells give you errors, try running that cell again and it should work, there seems to be some lag time between cells.

## **Genome Wide Association Studies** <a name="GWAS"></a>
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using AWS, thus we have rewritten it as a notebook to work on GCP [here](/tutorials/notebooks/GWASCoatColor). Make sure you select R as your kernel when you spin up your notebook so that you can switch between R and Python.
- Terra has a [GWAS workspace](https://app.terra.bio/#workspaces/amp-t2d-op/2019_ASHG_Reproducible_GWAS-V2) that walks through a few tutorials and has links to public data for testing GWAS. Since it uses notebooks it should be easy enough to adapt to Vertex AI.

## **Proteomics** <a name="PRO"></a>
- Use Big Query to run a Kruskal Wallis Test on Proteomics data using [these notebooks](https://github.com/isb-cgc/Community-Notebooks/tree/master/FeaturedNotebooks). Clone the repo into Vertex AI, or just drag the notebooks into a Vertex AI Workbench instance. 

## **Medical Imaging** <a name="IM"></a>
- Most medical imaging analyses are done in notebooks, so we would recommend downloading the Jupyter Notebook from [here](/tutorials/notebooks/SpleenLiverSegmentation) and then importing or cloning it into VertexAI. The tutorial walks through image segmentation using the Monai framework.
- Download NVIDIA's example [Medical Imaging Notebook](https://developer.nvidia.com/run-jupyter-notebooks). Note that there are other interesting notebooks on that site, but be warned that most of the NVIDIA notebooks require a GPU, so be careful about spinning up expensive resources and not shutting them down!

## **RNAseq** <a name="RNA"></a>
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/usage) for RNAseq a variety of ways on GCP. Following the instructions outlined above, you could use Compute Engine, [Life Sciences API](https://cloud.google.com/life-sciences/docs/tutorials/nextflow), or in Vertex AI notebook.
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from [The University of Maine INBRE](https://github.com/MaineINBRE/rnaseq-myco-tutorial) use this [Notebook](/tutorials/notebooks/rnaseq-myco-tutorial-main). 
- There is also this NIH-written tutorial to use [Kids First data on Cavatica](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/RNAseq-on-Cavatica/rna_seq_1/). Note that you will need to pre-register for both Kids First data and Cavatica access.

## **Single Cell RNAseq** <a name="sc"></a>
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the github that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook.

## **Long Read Sequence Analysis** <a name="Long"></a>
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/). Note that these notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands.

## **Public Data Sets** <a name="Pub"></a>
Google has a lot of public datasets available that you can use for your testing. These can be viewed [here](https://cloud.google.com/life-sciences/docs/resources/public-datasets) and can be accessed via [BigQuery](https://cloud.google.com/bigquery/public-data) or directly from the cloud bucket. For example, to view phase 3 1000 genomes at the command line type `gsutil ls gs://genomics-public-data/1000-genomes-phase-3`. 
