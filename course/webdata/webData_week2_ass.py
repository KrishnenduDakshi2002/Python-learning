import re

values =[]
sum =0
count =0
handle = open('test.txt')
for itr in handle:
    itr = itr.rstrip()
    lst = re.findall('([0-9]+)',itr)
    values = values +lst
    
    
for itr in values:
    intVal = int(itr)
    sum = sum + intVal
    count = count+1
    
print(sum)