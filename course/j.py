
# largest number present in this list

# largest_so_far = -1
# for num in [12,34,12,111,45,67]:
#     if num > largest_so_far:
#         largest_so_far = num
#     print(largest_so_far)
# print('after',largest_so_far)
    
    
# count = 0

# for i in [11,45,12,43,23,567]:
#     count = count+1
#     print(count,i)

# #  for addition of numbers in a list

# temp =0
# for num in [11,45,12,43,23,567]:
#     temp = temp + num
# print(temp)



    
# arr =10
# # print(id(arr))
# list_ = [1,2,45,34,23,21]
# i =0
# while i!= len(list_):
#     print(list_[i],  sep=',')
#     i = i+1

    
smallest = None
for num in [23,34,15,36,-1,9]:
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
print(smallest)
    

 

