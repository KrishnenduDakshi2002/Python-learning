# to get the name from the txt file

from os import name
import re


handle = open("actualTxt.txt")
count =0
data={}
name=[]
email =[]
assignment=[]
for itr in handle:
    itr = itr.rstrip()
    lst = re.findall('^From: .*: ([a-zA-Z]* [a-zA-Z]*).([a-zA-Z0-9]*@\S\.[a-z]*).([a-zA-Z]*\S)',itr) # here lst is list which will contain output
    if len(lst)>0:
        name = name +lst # concatenating two lists
        
        
print(name)       


