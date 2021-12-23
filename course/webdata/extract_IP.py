
import re
IPs =[]
source_add=[]
handle = open('netstate_data.txt')
for itr in handle:
    lst_IP4 = re.findall('^tcp4       0      0  ([0-9]*\S*)',itr)
    IPs = IPs + lst_IP4
    
for itr in IPs:
    lst = re.findall('[0-9]*.[0-9]*.[0-9]*.[0-9]*.([0-9]*)',itr)
    source_add= source_add +lst
print(IPs)
print(source_add)