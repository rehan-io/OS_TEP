import argparse
import random

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-s", "--seed", action="store", default=10)
parser.add_argument("-a", "--asize", action="store", default=2048) # 1k
parser.add_argument("-p", "--psize", action="store", default=65536) # 64k
parser.add_argument("-n", "--numAddresses", action="store", default=5)
parser.add_argument("-b", "--base", action="store", default=256)
parser.add_argument("-l", "--limit", action="store", default=1024)
parser.add_argument("-c", "--compute", action="store_true", default=False)
parser.add_argument("-h", "--help", action="store_true", default=False)
args = parser.parse_args()

help = """Usage: relocation.py [options]

Options:
  -h, --help            show this help message and exit
  -s SEED, --seed=SEED  the random seed
  -a ASIZE, --asize=ASIZE address space size (e.g., 16, 64k, 32m)
  -p PSIZE, --physmem=PSIZE physical memory size (e.g., 16, 64k)
  -n NUM, --addresses=NUM # of virtual addresses to generate
  -b BASE, --b=BASE     value of base register
  -l LIMIT, --l=LIMIT   value of limit register
  -c, --compute         compute answers for me
"""

if args.help:
    print(help)

random.seed(args.seed, version=2)

VA = []
for i in range(0, int(args.numAddresses)):
    va = int(args.asize*random.random() + 1)
    VA.append(va)

if not args.help and not args.compute:
    print("\nBase and Bount informatin\n")
    print("\tBase :", hex(int(args.base)), " ( Decimal: ", int(args.base), ")")
    print("\tLimit: ", int(args.limit))
    print("\nVirtual Address Trace:\n")
    for i in range(0, int(args.numAddresses)):
        print("\tVA ", i, ": ", hex(VA[i]), " (decimal:", int(VA[i]),") -> PA or violation?")
    print("")

if args.compute:
    print("\nVirtual Address Trace")
    for i in range(0, int(args.numAddresses)):
        if VA[i] <= int(args.limit):
            print("\tVA ", i, ": ", hex(VA[i]), "(decimal: ",VA[i] ,") -> VALID : ", hex(VA[i] + int(args.base)), "(decimal: ", VA[i]+int(args.base),")")
        else:
            print("\tVA ", i, ": ", hex(VA[i]), "(decimal: ",VA[i] ,") -> SEGMENTATION VIOLATION")
    print("")
