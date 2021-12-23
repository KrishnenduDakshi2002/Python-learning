
def find_max(emails):
    maxValue=0
    keyValue = ' '
    for key in emails:
        if emails[key] > maxValue:
            maxValue=emails[key] #stoing the maximum value into maxValue
            keyValue=key #key the key releted to the maxvalue
        else:
            continue
    
    print(keyValue,maxValue)

    


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
for itr in handle:
    if itr.startswith('From:'):
        continue
    elif itr.startswith('From'):
        emails[itr.split()[1]]=emails.get(itr.split()[1],0)+1


find_max(emails)
print("\n")



# this is how we can iterate in dictionary using key
for key in emails:
    print(key,emails[key])


        