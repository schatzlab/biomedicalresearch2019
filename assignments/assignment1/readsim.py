#!/usr/bin/env python3

import sys
import random

if (len(sys.argv) != 4):
  print("USAGE: readsim.py genomelength readlength numberreads > reads.bed")
  sys.exit(0)

## Parse the command line arguments
genomelength = int(sys.argv[1])
readlength = int(sys.argv[2])
numberreads = int(sys.argv[3])
chromo = "genome"


## Now print the simulated read positions by repeatedly picking a starting position at random
print("Simulating {} reads that are {}bp long from a {} bp genome".format(numberreads, readlength, genomelength), file=sys.stderr)

for idx in range(numberreads):
  startpos = random.randint(0, genomelength-readlength+1)
  endpos = startpos + readlength
  print("{}\t{}\t{}\tread{}".format(chromo, startpos, endpos, idx))
