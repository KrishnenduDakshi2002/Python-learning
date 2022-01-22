import email
import re

fname = input("Enter file name-")
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From:'):continue
    pieces = line.split()
    Email = pieces[1]
    print(re.findall('.*@(.*)',Email)[0])

