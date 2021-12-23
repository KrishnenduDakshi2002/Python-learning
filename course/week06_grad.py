
name = input("Enter file:")
handle = open(name)
hours = dict()
for itr in handle:
    if itr.startswith('From:'):
        continue
    elif itr.startswith('From'):
        hours[itr.split()[5].split(':')[0]]= hours.get(itr.split()[5].split(':')[0],0)+1
        # what the above line is doing
        # example: From krish.dakshi210@gmail.com Sun 5 04:12:34 2021
        #when itr is on the above line
        # then I spilt itr and take out time (04:12:34) from index 5
        # then  I split the time on the basis of ':'
        # and take out the hours from index 0
        
print(hours)
listHours =[(key,value)for (key,value)in hours.items()] # list of tuples # list comoprehension
listHours=sorted(listHours,reverse=False)

for itr in listHours:
    print(itr[0],itr[1])
