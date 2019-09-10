## Assignment 2: De novo assembly
Assignment Date: Wednesday, Sept 11, 2019 <br>
Due Date: Wednesday, Sept. 18, 2019 @ 11:59pm <br>

### Assignment Overview

In this assignment you will assemble a few simple datasets by hand and then by using an automated assembler called Spades.
As a reminder, any questions about the assignment should be posted to [Piazza](https://piazza.com/jhu/fall2019/en601452/resources)

### Question 1: de Bruijn graph construction (10 pts)

1a. Draw (by hand or in code) the de Bruijn graph for the following reads using k=3 (assume all reads are from the forward strand, no sequencing errors, complete coverage of the genome)

	ACTA
	ATCA
	ATCG
	ATCT
	CATC
	CTAC
	CTAT
	GATC
	TACT
	TATC
	TCAT
	TCTA

1b. Write one possible genome sequence from this graph
(Hint: your solution should visit every node in the graph at least once)

1c. Why might you want to use longer reads? (In a few sentences)


### Question 2: Genome Assembly (10pts)

Download the reads from: [https://github.com/schatzlab/biomedicalresearch2019/raw/master/assignments/assignment2/reads.fq.gz]()

- Question 2a. How many reads are provided and how long are they? 
- Question 2b. Assume the genome is 100kbp long. How much coverage do you expect to have? [Hint: A little arthmetic]
- Question 2c. Assemble the reads using Spades.  How many contigs were produced? [Hint: try `grep -c '>' contigs.fasta`]
- Question 2d. What is the total length of the contigs? [Hint: try `samtools faidx`, plus a short script/excel]
- Question 2e. What is the size of your large contig? [Hint: check `samtools faidx` plus `sort -n`]
- Question 2f. What is the contig N50 size? [Hint: Write a short script/excel]


### Packaging

The solutions to the above questions should be submitted as a single PDF document that includes your name, email address, and 
all relevant figures (as needed). Make sure to clearly label each of the subproblems and give the exact commands and/or code snippets you used for 
solving the question. You do not need to show code for plotting. 
Submit your solutions by uploading the PDF to [GradeScope](https://www.gradescope.com/courses/60230). The Entry Code is: MPK8BX 

If you submit after this time, you will start to use up your late days. Remember, you are only allowed 5 late days (120 hours) for the entire semester!


### Resources

####  [Spades](http://cab.spbu.ru/software/spades/) - Short Read Assembler.

Normally spades would try several values of k and merge the results together, but here we will force it to just use k=31 to save time. The assembly should take less than 1 minute.

```
$ spades.py --s1 reads.fq -o asm -t 4 -k 31
```

#### [SAMTools](http://www.htslib.org/) - Index a fasta file and record the length of every sequence as the second column

```
$ ./samtools faidx /path/to/genome.fa 
```

