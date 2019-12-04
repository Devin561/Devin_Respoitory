#!/usr/bin/env python3
# coding: utf-8
# Author: Devin561
# E-Mail: zengzhen561@163.com

import re
import os


def get_miR(num, file):
    outfile = open(os.path.basename(file).split('.')[0] + "_{0}.".format(num) + os.path.basename(file).split('.')[1], 'w')
    dict = {}
    num = str(num)
    with open(file, 'r') as fasta:
        for line in fasta:
            if line.startswith('>'):
                name = line.lstrip('>').strip()
                dict[name] = ''
            else:
                dict[name] += line.strip()
                RE = re.search(r'\D' + num + r'\D', name)
                if RE:
                    outfile.write('>' + name + '\n' + str(''.join(dict[name])) + '\n')
                else:
                    pass
    outfile.close()


if __name__ == '__main__':
    get_miR(399, './mature.fa')
