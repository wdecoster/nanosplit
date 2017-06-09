#wdecoster
'''
Example usage:
NanoSplit reads.fastq.gz
NanoSplit -q 6 reads.fastq.gz
NanoSplit -q 10 --outdir /home/user/datasetsplit/ reads.fastq
'''

from Bio import SeqIO
import argparse
import gzip
import os
from nanomath import aveQual
from nanoget import handlecompressedFastq

__version__= "0.1.2"


def main():
    args = getArgs()
    fqin = handlecompressedFastq(args.fastqfile.name)
    splitFq(fqin, args)


def getArgs():
    parser = argparse.ArgumentParser(description="Perform splitting of a fastq file based on average basecall quality.")
    parser.add_argument("-q", "--quality", help="Splitting on this average read quality score", default=12, type=int)
    parser.add_argument("fastqfile", help="Fastq file to split, can be gz compressed.", type=argparse.FileType('r'))
    parser.add_argument("--outdir", help="Specify directory in which output has to be created.", default=".")
    return parser.parse_args()


def splitFq(fq, args):
    '''
    Split a fastq file in a fail and pass file
    Optionally trim a number of nucleotides from beginning and end.
    '''
    prefix = os.path.join(args.outdir, os.path.basename(args.fastqfile.name).replace('.fastq', '').replace('.gz', '').replace('.fq', ''))
    p, f = 0, 0
    with gzip.open(prefix + ".pass.fastq.gz", 'wt') as passed, gzip.open(prefix + ".fail.fastq.gz", 'wt') as failed:
        for record in SeqIO.parse(fq, "fastq"):
            if aveQual(record.letter_annotations["phred_quality"]) >= args.quality:
                p+=1
                passed.write(record.format("fastq"))
            else:
                failed.write(record.format("fastq"))
                f+=1
    print("Split the file in {} reads in <pass> and {} reads in <fail>".format(p, f))


if __name__ == "__main__":
    main()
