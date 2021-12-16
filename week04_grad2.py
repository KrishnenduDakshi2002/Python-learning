fname = input('enter file name')
fhand = open(fname)
count=0
email= list()
for itr in fhand:
    itr = itr.rstrip()
    if itr.startswith('From:'):
        continue
    elif itr.startswith('From'):
        print(itr.split()[1])
        count=count+1
print(count)

        
