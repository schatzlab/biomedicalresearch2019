## Assignment 1: Chromosome Structures
Assignment Date: Wednesday, Sept 4, 2019 <br>
Due Date: Wednesday, Sept. 11, 2019 @ 11:59pm <br>

### Assignment Overview

In this assignment you will profile the overall structure of the genomes of several important species and then consider the sequencing data needed for each of them.
As a reminder, any questions about the assignment should be posted to [Piazza](https://piazza.com/jhu/spring2019/en601749/home)

### Question 1: Chromosome structures (10 pts)

Download the chomosome size files for the following genomes (Note these have been preprocessed to only include main chromosomes):

1. [Arabidopsis thaliana (TAIR10)](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/TAIR10.chrom.sizes) - An important plant model species [[info]](https://en.wikipedia.org/wiki/Arabidopsis_thaliana)
2. [E. coli (Escherichia coli K12)](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/ecoli.chrom.sizes) - One of the most commonly studied bacteria [[info]](https://en.wikipedia.org/wiki/Escherichia_coli)
3. [Fruit Fly (Drosophila melanogaster, dm6)](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/dm6.chrom.sizes) - One of the most important model species for genetics [[info]](https://en.wikipedia.org/wiki/Drosophila_melanogaster)
4. [Human (hg38)](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/hg38.chrom.sizes) - us :) [[info]](https://en.wikipedia.org/wiki/Homo_sapiens)
5. [Yeast (Saccharomyces cerevisiae, sacCer3)](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/yeast.chrom.sizes) - an important eukaryotic model species, also good for bread and beer [[info]](https://en.wikipedia.org/wiki/Saccharomyces_cerevisiae)

Using these files, make a table with the following information per species:

- Question 1.1. Total genome size
- Question 1.2. Number of chromosomes
- Question 1.3. Largest chromosome size and name
- Question 1.4. Smallest chromosome size and name
- Question 1.5. Mean chromosome length


### Question 2: Coverage Statistics (10pts)

This script [readsim.py](http://schatz-lab.org/biomedicalresearch2019/assignments/assignment1/readsim.py) will simulate shotgun sequencing of a genome of given length. The arguments for it are:

```
$ readsim.py genomelength readlength numberreads > reads.bed
```

Here `genomelength` is the total length of the genome; `readlength` is the length of each of the reads; `numberreads` is the total number of reads to simulate. The output file is a [bed file](https://genome.ucsc.edu/FAQ/FAQformat.html) that just lists the chromosome name, start and end position of each read, and read name.

- Question 2.1 How many 100bp reads should we simulate so that we cover the E. coli genome with 5x, 10x, 50x, and 100x coverage (mean coverage)?
- Question 2.2 Run readsim.py with the 4 numbers of reads from Q2.1, and plot the histogram of coverage for each dataset. Hint: allocate an array the size of the genome initialized to 0, and use for loops to add +1 to each position covered by each read. Then use the numpy histogram function (or write your own) to tally how many bases have how much coverage
- Question 2.3 Compute the mean and standard deviation from the 4 simulated datasets. How does this compare to your expectations? Is 5x coverage enough to sequence the genome?


### Hints

- Many of the questions can be addressed with standard command line [tools](http://lh3lh3.users.sourceforge.net/biounix.shtml) such as grep, wc, awk, sort, fold, etc
- You may wish to try out [datamash](https://www.gnu.org/software/datamash/)
- Plotting can be done in any language; R or Python are recommended; Excel is okay but ugly :-P
- The final PDF can be made in any system: Markdown, Word, Google Docs, LaTeX, HTML, ...
- Be sure to clearly mark each question and subquestion
- Mac and Linux can use the builtin terminal
- If you are using Windows, you may want to install [Ubuntu for Windows](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0)


### Packaging

The solutions to the above questions should be submitted as a single PDF document that includes your name, email address, and 
all relevant figures (as needed). Make sure to clearly label each of the subproblems and give the exact commands and/or code snippets you used for 
solving the question. You do not need to show code for plotting. Submit your solutions by uploading the PDF to [GradeScope](https://www.gradescope.com/courses/60230). The Entry Code is: MPK8BX 

If you submit after this time, you will start to use up your late days. Remember, you are only allowed 5 late days (120 hours) for the entire semester!
