#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import glob
import gzip
import re
import sys
import itertools as it
from time import perf_counter

FILE_NAME = re.compile('\.\w+')

def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)

def extract(file, fp):
    output_fasta = file
    i = 0
    for line in fp:
        i += 1
        if i % 4 == 1:
            line_new = line[1:]
            output_fasta.write('>' + line_new)
        elif i % 4 == 2:
            output_fasta.write(line)
    output_fasta.close()

def fq2fa():
    for fq_file in multiple_file_types('*.fastq', '*.fq'):
        with open(fq_file) as fp:
            output_fasta = open('{0}.fa'.format(re.sub(FILE_NAME, '',fq_file)), 'w')
            extract(output_fasta, fp)

def fq_gz2fa():
    for fq_gz in glob.glob('*.fastq.gz'):
        with gzip.open(fq_gz, 'rt') as fp1:
            output_fasta1 = open('{0}.fa'.format(fq_gz[:-9]), 'w')
            extract(output_fasta1, fp1)

def main():
    print('Fastq files are below:')
    for fq_file in glob.glob('*.fastq'):
        print(fq_file)
    fq2fa()
    print('Fastq files in this folder have been converted to Fasta files')
    print('cost {0}s to finish it'.format(perf_counter()))
    print('*'*50)
    # print('Fastq.gz files are below:')
    # for fq_gz in  glob.glob('*.fastq.gz'):
    #     print(fq_gz)
    # fq_gz2fa()
    # print('Fastq.gz files in this folder have been converted to Fasta files')
    # print('cost {0}s to finish it'.format(perf_counter()))

if __name__ == '__main__':
    main()