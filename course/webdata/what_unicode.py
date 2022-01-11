

#                                    what is unicode

# Fundamentally, computers just deal with numbers. They store letters and other characters by assigning a number for each one. Before Unicode was invented, there were hundreds of different systems, called character encodings, for assigning these numbers. These early character encodings were limited and could not contain enough characters to cover all the world's languages. Even for a single language like English no single encoding was adequate for all the letters, punctuation, and technical symbols in common use.

# Early character encodings also conflicted with one another. That is, two encodings could use the same number for two different characters, or use different numbers for the same character. Any given computer (especially servers) would need to support many different encodings. However, when data is passed through different computers or between different encodings, that data runs the risk of corruption.







# because of unicode we have different number of different character for every language of world
# these are japanese characters
print('japanese characters')
print(ord('し')) # here (ord) means ordinal
print(ord('ヸ'))
print(ord('ふ'))
print(ord('゛'))


#these are chinesse letters
print('chinese characters')
print(ord('⺃'))

#these are french characters
print('French characters')
print(ord('ë'))

encod = 'a'.encode()
print(encod)
print(type(encod))

#binary number 
print(bin(142)) #0b10001110  -> ignore 0b so the binary number is (10001110)


#  assuming (unicode = ASCII + other characters not included into ascii) 

#  character   unicode number  binary number
#   
#   a           97             1100001 (this binary no is of 97 not  directly of a)
#   Ë (french)  203            11001011 (binary of 203)












