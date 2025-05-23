# GCP Tutorial Resources

_We have pulled together a variety of tutorials here from disparate sources. Some use Compute Engine, others use Vertex AI notebooks, and others use only managed services. Tutorials are organized by research method, but we try to designate what GCP services are used to help you navigate._
---------------------------------
## Overview of Page Contents

+ [Biomedical Workflows on GCP](#bds)
+ [Artificial Intelligence and Machine Learning](#ml)
+ [Medical Imaging](#mi)
+ [Download SRA Data](#sra)
+ [Variant Calling](#vc)
+ [VCF Query](#vcf)
+ [GWAS](#gwas)
+ [Proteomics](#pro)
+ [RNAseq and Transcriptome Assembly](#rna)
+ [scRNAseq](#sc)
+ [ATACseq and scATACseq](#atac)
+ [Methylseq](#ms)
+ [Metagenomics](#meta)
+ [Multiomics and Biomarker Analysis](#mo)
+ [BLAST+](#bl)
+ [Long Read Sequencing Analysis](#long)
+ [Drug Discovery](#atom)
+ [Using Google Batch](#gbatch)
+ [Using the Life Sciences API (deprecated)](#lsapi)
+ [Public Data Sets](#pub)

## **Biomedical Workflows on GCP** <a name="bds"></a>
There are a lot of ways to run workflows on GCP. Here we list a few possibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using one of the other methods listed here.

- The simplest method is probably to spin up a Compute Engine instance, and run your command interactively, or using `screen` or, as a [startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) attached as metadata.
- You could also run your pipeline via a Vertex AI notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). [Schedule notebooks](https://codelabs.developers.google.com/vertex_notebook_executor#0) to let them run longer. 
- You can interact with [Google Batch](https://cloud.google.com/batch/docs/get-started), using a workflow manager like [Nextflow](https://cloud.google.com/batch/docs/nextflow), [Snakemake](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/googlebatch.html), or [Cromwell](https://github.com/GoogleCloudPlatform/rad-lab/tree/main/modules/genomics_cromwell). We currently have example notebooks for [Google Batch with Nextflow](/notebooks/GoogleBatch/nextflow) as well as a [local version of Snakemake run via Pangolin](/notebooks/pangolin). You can learn how to use SnakeMake for Google Batch [here](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/googlebatch.html.
- You may find other APIs better suited for your needs such as the [Google Cloud Healthcare Data Engine](https://cloud.google.com/healthcare).
- Most of the notebooks below require just a few CPUs. Start small (maybe 4 CPUs), then scale up as needed. Likewise, when you need a GPU, start with a smaller or older generation GPU (e.g. T4) for testing, then switch to a newer GPU (A100/V100) once you know things will work or you need more compute power. 

## **Artificial Intelligence and Machine Learning** <a name='ml'></a>
Machine learning is a subfield of artificial intelligence that focuses on the development of algorithms and models that enable computers to learn from and make predictions or decisions based on data, without being explicitly programmed. Machine learning on GCP generally occurs within VertexAI. You can learn more about machine learning on GCP at this [Google Crash Course](https://developers.google.com/machine-learning/crash-course). For hands-on examples, try out [this module](https://github.com/NIGMS/COVIDMachineLearningSFSU) developed by San Francisco State University or [this one from the University of Arkansas](https://github.com/NIGMS/MachineLearningUA) developed for the NIGMS Sandbox Project.

Now that the age of **Generative AI** (Gen AI) has arrived, Google has released a host of Gen AI offerings within the Vertex AI suite. Some examples of what generative AI models are capable of are extracting wanted information from text, transforming speech into text, generating images from descriptions and vice versa, and much more. Vertex AI's [Vertex AI Studio](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/generative-ai-studio) console allows the user to rapidly create, test, and train generative AI models on the cloud in a safe and secure setting, see our overview in [this tutorial](/notebooks/GenAI/VertexAIStudioGCP.ipynb). The studio also has ready-to-use models all contained within the [Model Garden](https://cloud.google.com/vertex-ai/docs/start/explore-models). These models range from foundation models, fine-tunable models, and task-specific solutions. 
- To learn more about Gen AI on GCP take a look at our [GenAI tutorials](/notebooks/GenAI) that go over several GCP products such as [Gemini](/notebooks/GenAI/Gemini_Intro.ipynb) and [Vector Search](/notebooks/GenAI/Pubmed_RAG_chatbot.ipynb) and other tools like [Langchain](/notebooks/GenAI/langchain_on_vertex.ipynb) and [Huggingface](/notebooks/GenAI/GCP_GenAI_Huggingface.ipynb) to deploy, train, prompt, and implement techniques like [Retrieval-Augmented Generation (RAG)](/notebooks/GenAI/Pubmed_RAG_chatbot.ipynb) to GenAI models.
- Google also provides many generative AI tutorials hosted on [GitHub](https://github.com/GoogleCloudPlatform/generative-ai/tree/main). Some examples they provide are under [language here](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/language).

## **Medical Image Segmentation** <a name="mi"></a>
Medical image analysis is the application of computational algorithms and techniques to extract meaningful information from medical images for diagnosis, treatment planning, and research purposes. Medical image analysis requires large image files and often elastic storage and accelerated computing.
- Most medical imaging analyses are done in notebooks, so we would recommend downloading the Jupyter Notebook from [here](/notebooks/SpleenLiverSegmentation) and then importing or cloning it into VertexAI. The tutorial walks through image segmentation using the Monai framework.
- You can also request early access to the new [Google Medical Imaging Suite](https://cloud.google.com/medical-imaging) to see if it would fit your use case.

## **Download Data From the Sequence Read Archive (SRA)** <a name="sra"></a>
Next Generation genetic sequence data is housed in the NCBI Sequence Read Archive (SRA). You can access this data using the SRA Toolkit. We walk you through this using [this notebook](/notebooks/SRADownload), including how to use BigQuery to generate your list of Accessions. You can also use BigQuery to create a list of accessions for download using [this setup guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-bigquery/) and this [query guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-bigquery-examples/). Additional example notebooks can be found at this [NCBI repo](https://github.com/ncbi/ASHG-Workshop-2021). In particular, we recommend this notebook(https://github.com/ncbi/ASHG-Workshop-2021/blob/main/1_Basic_BigQuery_Examples.ipynb), which goes into more detail on using BigQuery to access the results of the SRA Taxonomic Analysis Tool, which often differ from the user input species name due to contamination, error, or due to samples being metagenomic in nature. Further, [this notebook](https://github.com/ncbi/ASHG-Workshop-2021/blob/main/2_Array_Examples.ipynb) does a deep dive on parsing the BigQuery results and may give you some good ideas on how to search for samples from SRA. The SRA metadata and taxonomy analyses are in separate BigQuery tables, you can learn how to join those two tables using SQL from [this Powerpoint](https://github.com/NCBI-Codeathons/NCGAS-cloud-workshop/blob/main/5_BigQuery.pptx) or from our tutorial [here](/notebooks/ncbi-stat-tutorial/). Finally, NCBI released [this workshop](https://github.com/ncbi/workshop-asm-ngs-2022/wiki) that walks through a wide variety of BigQuery applications with NCBI datasets.

## **Variant Calling** <a name="vc"></a>
Genomic variant calling is the process of identifying and characterizing genetic variations from DNA sequencing data to understand differences in an individual's genetic makeup. 
- This [Google tutorial](https://cloud.google.com/life-sciences/docs/tutorials/gatk) shows you how to run the GATK Best Practices pipeline for genomic variant calling using the Life Sciences API. There is a section about increasing your account quotas, you can skip that. You could also run GATK using any of the workflow managers and submit to Google Batch.
- One tutorial specific to somatic variant calling comes from the Sheffield Bioinformatics Core [here](https://sbc.shef.ac.uk/somatic-variants/index.nb.html). It runs on Galaxy, but can be adapted to run in GCP. At the very least, the [data](https://drive.google.com/drive/folders/1RhrmfW3vMhPwAiBGdFIKfINWMsdvIG6E) may prove useful to you.

## **Query a VCF file in Big Query** <a name="vcf"></a>
The output of genomic variant calling workflows is a file in the variant call format (VCF). These are often large, structured data files that can be searched using database query tools such as Big Query.
- Learn how to use Big Query to run queries against large VCF files from Gnomad data using [this notebook](https://github.com/GoogleCloudPlatform/rad-lab/blob/main/modules/data_science/scripts/build/notebooks/Exploring_gnomad_on_BigQuery.ipynb). If any cells give you errors, try running that cell again and it should work, there seems to be some lag time between cells.

## **Genome Wide Association Studies** <a name="gwas"></a>
Genome-wide association studies (GWAS) are large-scale investigations that analyze the genomes of many individuals to identify common genetic variants associated with traits, diseases, or other phenotypes.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using AWS, thus we have rewritten it as a notebook to work on GCP [here](/notebooks/GWASCoatColor). Make sure you select R as your kernel when you spin up your notebook so that you can switch between R and Python (this only applies to 'User Managed Notebooks') but note that our team experienced conda permission issues with the new Managed Notebooks for this tutorial, so we recommend using the 'User Managed Notebooks'. Also, if the imported notebook has cells already printed out, just go to Kernel > Restart Kernel and Clear all Outputs.
- [This tutorial](https://github.com/STRIDES/NIHCloudLabGCP/tree/main/notebooks/DL-gwas-gcp-example) from NIH NIEHS (credit to David Thrower) builds on a published deep learning method for GWAS of soybeans and uses Kubeflow and AutoML on a Kubernetes instance. 

## **Proteomics** <a name="pro"></a>
Proteomics is the study of the entire set of proteins in a cell, tissue, or organism, aiming to understand their structure, function, and interactions to uncover insights into biological processes and diseases. Although most primary proteomic analyses occur in proprietary software platforms, a lot of secondary analysis happens in Jupyter or R notebooks, we give several examples here:
- Use Big Query to run a Kruskal Wallis Test on Proteomics data using [these notebooks](https://github.com/isb-cgc/Community-Notebooks/tree/master/FeaturedNotebooks). Clone the repo into Vertex AI, or just drag the notebooks into a Vertex AI Workbench instance. In the notebook titled 'ACM_BCB_2020_POSTER_KruskalWallisTest_ProteinGeneExpression_vs_ClinicalFeatures.ipynb', the first BigQuery cell may throw an error, but ignore this and keep going, the rest of the notebook should run fine. Also, in that first big cell, make sure you add your Project ID. See this [doc](/docs/protein_setup.md) for environment setup instructions.
- Run AlphaFold in Vertex AI using [this notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/community-content/alphafold_on_workbench/AlphaFold.ipynb). Make sure you have a GPU for your notebook instance, and follow [these instructions](https://cloud.google.com/blog/products/ai-machine-learning/running-alphafold-on-vertexai) for setting up your environment. Namely, under Environment, select `Custom container`, and then for `Docker container image` paste in the following: `west1-docker.pkg.dev/cloud-devrel-public-resources/alphafold/alphafold-on-gcp:latest`.
- Conduct secondary analysis of Proteomic data using this [NIGMS Sandbox notebook](https://github.com/NIGMS/ProteomicsUAMS), developed by the University of Arkansas for Medical Sciences.

## **RNAseq and Transcriptome Assembly** <a name="rna"></a>
RNA-seq analysis is a high-throughput sequencing method that allows the measurement and characterization of gene expression levels and transcriptome dynamics. Workflows are typically run using workflow managers, and final results can often be visualized in notebooks.
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/3.7) for RNAseq a variety of ways on GCP. Following the instructions outlined above, you could use Compute Engine, [Google Batch](https://cloud.google.com/batch/docs/nextflow), or a Vertex AI notebook.
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification go through these tutorials from the [NIGMS Sandbox Project](https://github.com/NIGMS/RNAseqUM) developed by The University of Maine.
- Likewise, [This multi-omics module](https://github.com/NIGMS/MultiomicsUND) from the University of North Dakota includes an RNAseq component. 

Transcriptome assembly is the process of reconstructing the complete set of RNA transcripts in a cell or tissue from fragmented sequencing data, providing valuable insights into gene expression and functional analysis.
- [This module](https://github.com/NIGMS/rnaAssemblyMDI) developed by the MDI Biological Laboratory for the NIGMS Sandbox Project walks you through transcriptome assembly using Nextflow. 

## **Single Cell RNAseq** <a name="sc"></a>
Single-cell RNA sequencing (scRNA-seq) is a technique that enables the analysis of gene expression at the individual cell level, providing insights into cellular heterogeneity, identifying rare cell types, and revealing cellular dynamics and functional states within complex biological systems.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub repository that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. 
-  The [Scanpy tutorials](https://scanpy.readthedocs.io/en/stable/tutorials.html) page has a lot of good CPU-based examples you could run in Vertex AI. Clone this [GitHub repo](https://github.com/scverse/scanpy-tutorials) to get the notebooks directly.
-  Alternatively, here is a [GitHub repository](https://github.com/mdozmorov/scRNA-seq_notes) with a curated list of scRNAseq resources and tutorials. We did not test these in Cloud Lab, but wanted to make them available in case you needed additional resources. 

## **ATACseq and Single Cell ATACseq** <a name="atac"></a>
ATAC-seq is a technique that allows scientists to understand how DNA is packaged in cells by identifying the regions of DNA that are accessible and potentially involved in gene regulation.
-[This module](https://github.com/NIGMS/atacseqUNMC) walks you through how to work through an ATACseq and single-cell ATACseq workflow on Google Cloud. The module was developed by the University of Nebraska Medical Center for the NIGMS Sandbox Project. 

## **Methylseq** <a name="ms"></a>
As one of the most abundant and well-studied epigenetic modifications, DNA methylation plays an essential role in normal cell development and has various effects on transcription, genome stability, and DNA packaging within cells. Methylseq is a technique to identify methylated regions of the genome. 
- The University of Hawai'i at Manoa developed [this set of notebooks](https://github.com/NIGMS/MethylSeqUH) that walk you through a Methylseq analysis as part of the NIGMS Sandbox Program.

## **Metagenomics** <a name="meta"></a>
Metagenomics is the study of genetic material collected directly from environmental samples, enabling the exploration of microbial communities, their diversity, and their functional potential, without the need for laboratory culturing.
-[This module](https://github.com/NIGMS/MetagenomicsUSD) walks you through conducting a metagenomic analysis using the command line and Nextflow. The module was developed by the University of South Dakota as part of the NIGMS Sandbox Project.

## **Multiomic Analysis and Biomarker Discovery** <a name="mo"></a>
Multiomic analysis involves integrating data across modalities (e. g. genomic, transcriptomic, phenotypic) to generate additive insights. 
- [This set of notebooks](https://github.com/NIGMS/MultiomicsUND) gives you an example of conducting multiomic analysis in Jupyter notebooks and was developed by the University of North Dakota as part of the NIGMS Sandbox Project.

Biomarker discovery is the process of identifying specific molecules or characteristics that can serve as indicators of biological processes, diseases, or treatment responses, aiding in diagnosis, prognosis, and personalized medicine. Biomarker discovery is typically conducted through comprehensive analysis of various types of data, such as genomics, proteomics, metabolomics, and clinical data, using advanced techniques including high-throughput screening, bioinformatics, and statistical analysis to identify patterns or signatures that differentiate between healthy and diseased individuals, or responders and non-responders to specific treatments.
- [This module](https://github.com/NIGMS/BiomarkersURI), developed by the University of Rhode Island for the NIGMS Sandbox Project, walks you through conducting some common biomarker discovery analyses in R. 

## **BLAST+** <a name="bl"></a>
NCBI BLAST (Basic Local Alignment Search Tool) is a widely used bioinformatics program provided by the National Center for Biotechnology Information (NCBI) that compares nucleotide or protein sequences against a large database to identify similar sequences and infer evolutionary relationships, functional annotations, and structural information.
- This [Common Data Fund](https://training.nih-cfde.org/en/latest/Cloud-Platforms/Introduction-to-GCP/gcp3/) tutorial explains how to use basic BLAST on GCP.
- We also rewrote [this ElastBLAST tutorial](https://blast.ncbi.nlm.nih.gov/doc/elastic-blast/quickstart-gcp.html) as a [notebook](/notebooks/elasticBLAST) that will work in VertexAI. 

## **Long Read Sequence Analysis** <a name="long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short-read sequencing, where reads are about 150 bp in length. Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. You can find a list and description of notebooks [here](https://labs.epi2me.io/nbindex/), or clone the [GitHub repo](https://github.com/epi2me-labs). Note that these notebooks expect you to be running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks.

## **Drug Discovery** <a name="atom"></a>
The [Accelerating Therapeutics for Opportunities in Medicine (ATOM) Consortium](https://atomscience.org/) created a series of [Jupyter notebooks](https://github.com/ATOMScience-org/AMPL/tree/master/atomsci/ddm/examples/tutorials) that walk you through the ATOM approach to Drug Discovery. 

These notebooks were created to run in Google Colab, so if you run them in Google Cloud, you will need to make a few modifications. First, we recommend you use a [Google Managed Notebook](https://cloud.google.com/vertex-ai/docs/workbench/managed/introduction) rather than a User-Managed notebook simply because the Google Managed notebooks already have Tensorflow and other dependencies installed. Be sure to attach a GPU to your instance (T4 is fine). Also, you will need to comment out `%tensorflow_version 2.x` since that is a Colab-specific command. You will also need to `pip install` a few packages as needed. If you get errors with `deepchem`, try running `pip install --pre deepchem[tensorflow]` and/or `pip install --pre deepchem[torch]`. Also, some notebooks will require a TensorFlow kernel, while others require PyTorch. You may also run into a Pandas error, reach out to the ATOM GitHub developers for the best solution to this issue.

## **Using Google Batch** <a name="gbatch"></a>
You can interact with Google Batch directly to submit commands, or more commonly, you can interact with it through orchestration engines like [Nextflow](https://www.Nextflow.io/docs/latest/google.html) and [Cromwell](https://cromwell.readthedocs.io/en/latest/backends/GCPBatch/), etc. We have tutorials that utilize Google Batch using [Nextflow](/notebooks/GoogleBatch/nextflow) where we run the nf-core Methylseq pipeline, as well as several from the NIGMS Sandbox, including [transcriptome assembly](https://github.com/NIGMS/rnaAssemblyMDI), [multiomics](https://github.com/NIGMS/MultiomicsUND), [methylseq](https://github.com/NIGMS/MethylSeqUH), and [metagenomics](https://github.com/NIGMS/MetagenomicsUSD).

## **Using the Life Sciences API (deprecated)** <a name="lsapi"></a>
__Life Science API is deprecated on GCP and will no longer be available by July 8, 2025 on the platform,__ we recommend using Google Batch instead. You can learn how to use SnakeMake with Google Batch [here](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/googlebatch.html).

## **Public Data Sets** <a name="pub"></a>
Google has a lot of public datasets available that you can use for your testing. These can be viewed [here](https://cloud.google.com/life-sciences/docs/resources/public-datasets) and can be accessed via [BigQuery](https://cloud.google.com/bigquery/public-data) or directly from the cloud bucket. For example, to view Phase 3 1k Genomes at the command line type `gsutil ls gs://genomics-public-data/1000-genomes-phase-3`. 
