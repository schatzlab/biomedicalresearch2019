# EN.601.452 / AS.020.415 Computational Biomedical Research &amp; Advanced Biomedical Research
Class Hours: Monday + Wednesday @ 3p - 3:50p in Hodson 311 <br>
Schatz Office Hours: Monday @ 4-5p in Malone 323 and by appointment<br>
CA: Melanie Kirsche - Office Hours TBD

**The goal of this course is to prepare undergraduates to understand and perform state-of-the-art biomedical research.** This will be accomplished through three main components: (1) classroom-style lectures on cross cutting techniques for biomedical research focusing on data visualization, statistical inference, and scientific computing; (2) research presentations from distinguished faculty on their active research projects; and (3) a major research project to be performed under the mentorship of a JHU professor. Students will present their research during an in-class symposium at the end of the semester. Grading will be based on homework exercises, a written research proposal, an interim research report, an oral research presentation, and a final research report.

## Course Resources:
- [Syllabus and Policies](https://github.com/schatzlab/biomedicalresearch2019/tree/master/policies)
- [Piazza Discussion Board](http://piazza.com/jhu/fall2019/en601452)
- [GradeScope](https://www.gradescope.com/courses/60230) Entry Code: MPK8BX

#### Recommended Prerequisites
- Online introduction to Unix/Linux. Students are strongly recommended to complete one of the following online tutorials before class begins. 
  - [Code academy's Intro to Unix](https://www.codecademy.com/en/courses/learn-the-command-line/lessons/environment/exercises/bash-profile)
  - [Command line bootcamp](http://rik.smith-unna.com/command_line_bootcamp/?id=9xnbkx6eaof)
- Access to a Linux Machine, or Install [VirtualBox](https://github.com/schatzlab/appliedgenomics/blob/master/assignments/virtualbox.md) (Unfortuantely, even Mac will not work correctly for some programs)

#### Related Courses & Readings
- [Applied Comparative Genomics](https://github.com/schatzlab/appliedgenomics2019)
- [Bioinformatics Algorithms: An Active Learning Approach (Compeau and Pevzner)](https://www.amazon.com/Bioinformatics-Algorithms-Active-Learning-Approach/dp/0990374602)
- [Unix and Perl for Biologists (Bradnam et al)](http://korflab.ucdavis.edu/Unix_and_Perl/)
- [Molecular Biology of the Gene (Watson et al)](https://www.amazon.com/Molecular-Biology-Gene-James-Watson/dp/0321762436/ref=pd_lpo_sbs_14_t_0?_encoding=UTF8&psc=1&refRID=R6A5BW06E5RJB7GVSNPY)
- [Molecular Biology of the Cell (Alberts)](http://osp.mans.edu.eg/tmahdy/surgeons/ebooks/Books/Alberts%20-%20Molecular%20Biology%20of%20the%20Cell.pdf)
- [Biological Sequence Analysis (Durbin et al)](https://www.amazon.com/Biological-Sequence-Analysis-Probabilistic-Proteins/dp/0521629713)
- [Modern Statistics for Modern Biology (Holmes & Huber)](https://www.huber.embl.de/msmb/index.html)


## Schedule
| # | Date | Lecture | Readings & Resources | Assignment |
|:--|:-----|:--------|:---------------------|:-----------|
|1.  | Th 8/29   | [Lecture 1. Introduction](http://schatz-lab.org/biomedicalresearch2019/lectures/01.Introduction.pdf) | * [Biological data sciences in genome research (Schatz, 2015, Genome Research)](http://genome.cshlp.org/content/25/10/1417.full) <br> * [Big Data: Astronomical or Genomical? (Stephens et al, 2015, PLOS Biology)](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002195) | [Sign Up for Piazza]() |
|    | Mon 9/2   | &#x1F538; *Labor Day Break!* | | |
|2.  | Wed 9/4   | Lecture 2. [Genome Sequencing](http://schatz-lab.org/biomedicalresearch2019/lectures/02.GenomeSequencing.pdf) | * [Coming of age: ten years of next-generation sequencing technologies (Goodwin et al, 2016, Nature Reviews Genetics)](http://www.nature.com/nrg/journal/v17/n6/full/nrg.2016.49.html) <br> * [High‐throughput sequencing for biology and medicine (Soon et al, 2013, Molecular Systems Biology)](http://msb.embopress.org/content/9/1/640) | [Assignment 1](https://github.com/schatzlab/biomedicalresearch2019/blob/master/assignments/assignment1/README.md)
|3.  | Mon 9/9   | Lecture 3. Genome Assembly | * [De novo genome assembly: what every biologist should know (Baker, 2012, Nature Methods)](http://www.nature.com/nmeth/journal/v9/n4/full/nmeth.1935.html)
|4.  | Wed 9/11  | Lecture 4. The Human Genome | * [The Sequence of the Human Genome (Venter et al, 2001, Science)](http://science.sciencemag.org/content/291/5507/1304) <br> * [Initial sequencing and analysis of the human genome (IHGSP, 2001, Nature)](https://www.nature.com/nature/journal/v409/n6822/full/409860a0.html) | Assignment 2
|5.  | Mon 9/16  | Lecture 5. Read Mapping | * [How to map billions of short reads onto genomes (Trapnell and Salzberg, 2009, Nature Biotech)](http://www.nature.com/nbt/journal/v27/n5/full/nbt0509-455.html) <br> * [Bowtie: Ultrafast and memory-efficient alignment of short DNA sequences to the human genome (Langmead et al, 2009, Genome Biology)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2009-10-3-r25) <br> * [BWA-MEM: Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM (Li, 2013, arXiv)](https://arxiv.org/abs/1303.3997) <br> 
|6.  | Wed 9/18  | Lecture 6. Variant Identification | * [SAM/BAM/Samtools: The Sequence Alignment/Map format and SAMtools (Li et al, 2009, Bioinformatics)](https://academic.oup.com/bioinformatics/article/25/16/2078/204688/The-Sequence-Alignment-Map-format-and-SAMtools) <br> * [IGV: Integrative genomics viewer (Robinson et al, 2011, Nature Biotech)](http://www.nature.com/nbt/journal/v29/n1/full/nbt.1754.html) <br>  * [PolyBayes: A general approach to single-nucleotide polymorphism discovery (Marth et al, 1999, Nature Genetics)](http://www.nature.com/ng/journal/v23/n4/full/ng1299_452.html) <br> * [GATK: A framework for variation discovery and genotyping using next-generation DNA sequencing data (Depristo et al, 2011, Nature Genetics)](http://www.nature.com/ng/journal/v43/n5/full/ng.806.html) <br> * [Scalpel: Accurate de novo and transmitted indel detection in exome-capture data using microassembly (Narzisi et al, 2014, Nature Methods)](http://www.nature.com/nmeth/journal/v11/n10/full/nmeth.3069.html) | Assignment 3
|7.  | Mon 9/23  | Lecture 7. Human Evolution | * [An integrated map of genetic variation from 1,092 human genomes (1000 Genomes Consortium, 2012, Nature)](http://www.nature.com/nature/journal/v491/n7422/full/nature11632.html) <br> * [Analysis of protein-coding genetic variation in 60,706 humans (Let et al, 2016, Nature)](http://www.nature.com/nature/journal/v536/n7616/full/nature19057.html) <br> * [A Draft Sequence of the Neandertal Genome (Green et al. 2010, Science)](http://science.sciencemag.org/content/328/5979/710.full) <br> * [Excavating Neandertal and Denisovan DNA from the genomes of Melanesian individuals (Vernot et al. 2016. Science)](http://science.sciencemag.org/content/early/2016/03/16/science.aad9416.full) 
|8.  | Wed 9/25  | Lecture 8. Human Genetic Diseases | * [Genome-Wide Association Studies (Bush & Moore, 2012, PLOS Comp Bio)](https://doi.org/10.1371/journal.pcbi.1002822) <br> * [The contribution of de novo coding mutations to autism spectrum disorder (Iossifov et al, 2014, Nature)](https://www.nature.com/nature/journal/v515/n7526/full/nature13908.html) | Assignment 4
|9.  | Mon 9/30  | Lecture 9. RNA-seq | * [RNA-Seq: a revolutionary tool for transcriptomics (Wang et al, 2009. Nature Reviews Genetics)](http://www.nature.com/nrg/journal/v10/n1/full/nrg2484.html)<br> * [Differential gene and transcript expression analysis of RNA-seq experiments with TopHat and Cufflinks (Trapnell et al, 2012, Nature Protocols)](http://www.nature.com/nprot/journal/v7/n3/full/nprot.2012.016.html)<br> * [Salmon provides fast and bias-aware quantification of transcript expression (Patro et al, 2017, Nature Methods)](http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.4197.html)<br> * [Bismark: a flexible aligner and methylation caller for Bisulfite-Seq applications (Krueger and Andrews, 2011, Bioinformatics)](https://academic.oup.com/bioinformatics/article/27/11/1571/216956/Bismark-a-flexible-aligner-and-methylation-caller) 
|10. | Wed 10/2  | Research Lab 1: How to Give a Talk | | Prepare Presentation and abstract
|11. | Mon 10/7  | Faculty Presentation 1: TBD
|12. | Wed 10/9  | Faculty Presentation 2: TBD
|13. | Mon 10/14 | Lecture 10. Gene Finding & HMMs | * [Glimmer: Microbial gene identification using interpolated Markov models](http://www.cs.jhu.edu/~genomics/Glimmer/glimmer-nar.pdf) <br> * [MAKER2: an annotation pipeline and genome-database management tool for second-generation genome projects](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-491) <br> * [What is a hidden Markov model?](http://www.nature.com/nbt/journal/v22/n10/full/nbt1004-1315.html)  | 
|14. | Wed 10/16 | Research Proposal Presentations | | Oral Presentation and Written abstract
|15. | Mon 10/21 | Lecture 11. Gene Regulation | * [ChIP–seq and beyond: new and improved methodologies to detect and characterize protein–DNA interactions (Furey, 2012, Nature Reviews Genetics)](http://www.nature.com/nrg/journal/v13/n12/abs/nrg3306.html)<br> * [PeakSeq enables systematic scoring of ChIP-seq experiments relative to controls (Rozowsky et al. 2009. Nature Biotech)](http://www.nature.com/nbt/journal/v27/n1/full/nbt.1518.html) <br> * [Comprehensive Mapping of Long-Range Interactions Reveals Folding Principles of the Human Genome (Lieberman-Aiden et al, 2009, Science)](http://science.sciencemag.org/content/326/5950/289) 
|16. | Wed 10/23 | Research Lab 2: Code Design
|17. | Mon 10/28 | Faculty Presentation 3: TBD
|18. | Wed 10/30 | Research Lab 3: Code Testing
|19. | Mon 11/4  | Lecture 12. Cancer Genomics | * [The Hallmarks of Cancer (Hanahan & Weinberg, 2000, Cell)](http://www.sciencedirect.com/science/article/pii/S0092867400816839) <br> * [Evolution of Cancer Genomes (Yates & Campbell, 2012, Nature Reviews Genetics)](http://www.nature.com/nrg/journal/v13/n11/full/nrg3317.html) <br> * [Comprehensive molecular portraits of human breast tumours (TCGA, 2012, Nature)](http://www.nature.com/nature/journal/v490/n7418/full/nature11412.html) 
|20. | Wed 11/6  | Faculty Presentation 4: TBD
|21. | Mon 11/11 | Lecture 13. Metagenomics | * [Kraken: ultrafast metagenomic sequence classification using exact alignments (Wood and Salzberg, 2014, Genome Biology)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-3-r46) <br> * [Chapter 12: Human Microbiome Analysis (Morgan and Huttenhower)](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002808)
|22. | Wed 11/13 | Research Lab 4: Documentation || Intern Report
|23. | Mon 11/18 | Lecture 14. Genomic Futures |  * ["Snyderome" Personal Omics Profiling Reveals Dynamic Molecular and Medical Phenotypes (Chen et al, 2012, Cell)](http://www.sciencedirect.com/science/article/pii/S0092867412001663) <br> * [Identifying Personal Genomes by Surname Inference (Gymrek et al, 2013, Science)](http://science.sciencemag.org/content/339/6117/321) 
|24. | Wed 11/20 | Research Lab 5: Demo preparation
|    | Mon 11/25 | &#x1F538; *Thanksgiving Break!* | | |
|    | Wed 11/27 | &#x1F538; *Thanksgiving Break!* | | |
|25. | Mon 12/2  | Research Presentations I  | | Research Presentation |
|26. | Wed 12/4  | Research Presentations II | | Research Presentation |
|    | Wed 12/20 | Research Report Due       | | Research Report Due |


