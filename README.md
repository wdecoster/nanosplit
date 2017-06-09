# NanoSplit

Perform splitting of Oxford Nanopore sequencing data in a fail and pass dataset using a user defined quality cutoff. The script can read compressed input and will write to gzip compressed files.

### INSTALLATION
```
pip install NanoSplit
```

### USAGE
```
NanoSplit [-h] [-q QUALITY] [--outdir OUTDIR] fastqfile


Required arguments:
  fastqfile             Fastq file to split, can be gz compressed.

Optional arguments:
  -h, --help            show this help message and exit
  -q QUALITY, --quality QUALITY
                        Splitting on this average read quality score
                        Default: 12
  --outdir OUTDIR       Specify directory in which output has to be created.
```

### EXAMPLES
```
NanoSplit reads.fastq.gz
NanoSplit -q 6 reads.fastq.gz
NanoSplit -q 10 --outdir /home/user/datasetsplit/ reads.fastq
```
