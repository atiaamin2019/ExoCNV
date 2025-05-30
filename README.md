# ExoCNV
This is a bioinformatics pipeline for the analysis of DNA Content of small Extracellular Vesicles. It uses short read sequencing data collected from small extracellular vesicles samples of two experimental contidions and performs copy number variation analysis of the genomic windows (default 5 kbp) across the chromosomes of an eukaryotic organism. 


<img width="1080" alt="Screenshot 2024-12-18 at 11 08 49 PM" src="https://github.com/user-attachments/assets/b21e77a6-7fe4-47c7-9932-30b1b484d1c8" />

This repository contains the complete bioinformatics pipeline for analyzing sequencing data, as described in this STAR Protocol article:


[1-s2.0-S266616672300206X-main.pdf](https://github.com/user-attachments/files/18192756/1-s2.0-S266616672300206X-main.pdf)

Identification and analysis of the DNA content of small extracellular vesicles isolated from Leishmania parasites.

The pipeline provides a detailed step-by-step process to analyze sequencing data, from raw FASTQ files to downstream analyses like copy number variation (CNV) analysis and visualization. It is designed for both researchers new to bioinformatics and advanced users who require a robust, reproducible pipeline.

**Pipeline Overview**

This pipeline focuses on analyzing sequencing data from extracellular vesicle (EV) DNA. It includes tools for quality control, adapter trimming, alignment, duplicate removal, normalization, and visualization.

**Steps**
**1	Quality Control:**
        •Assess sequencing quality using FastQC.
        •Generate quality reports for raw FASTQ files.
	
 **2	Adapter Trimming:**
        Remove adapters and low-quality bases using Trimmomatic.
	
 **3	Alignment:**
	Map reads to the reference genome using Bowtie2 (short reads) or BWA-MEM (long reads).
 
 **4	SAM/BAM Processing:**
	Convert SAM to BAM, sort, and index alignments using Samtools.
 
 **5	Quality Assessment:**
       Evaluate alignment quality and remove low-quality reads with Qualimap.
       
**6	Duplicate Removal:**
       Identify and remove PCR duplicates using Picard.
       
**7.	Coverage Tracks:**
       Generate BigWig files for visualization of coverage using DeepTools.
       
**8	Read Counts Matrix:**
       Count aligned reads in genomic bins using FeatureCounts.
       
**9	Differential Abundance Analysis:**
       Perform differential analysis of copy number variations using edgeR.
       
**10	Visualization:**
       Generate Miami plots to visualize CNVs with CMplot.
       

**Getting Started**

**Prerequisites**

Before running the pipeline, ensure the following tools are installed:
•	FastQC
•	Trimmomatic
•	Bowtie2
•	BWA
•	Samtools
•	Qualimap
•	Picard
•	DeepTools
•	R Packages:
•	edgeR
•	Rsubread
•	CMplot

**Installation**
Clone the repository:

```bash
git clone https://github.com/atiaamin2019/ExoCNV.git
cd ExoCNV
```


**Cite this article:**

This pipeline is described in this article: https://www.sciencedirect.com/science/article/pii/S266616672300206X#fig5. Special thanks to all co-authors for their contributions. 
 
 
