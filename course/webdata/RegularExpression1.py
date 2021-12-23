
import re

handle = open("RegularEx.txt")
count =0
for itr in handle:
    itr = itr.rstrip()
    # if re.search('^F..m',itr):
    #     print(itr)
    lst = re.findall('^From: (.*-)',itr) # here lst is list which will contain output
    if len(lst)>0:
        print(lst)
        count=count+1
        


print(count)