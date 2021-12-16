



minimum_num = None
maximum_num = None


while True:
    input_data = input('Enter number : ')
    if input_data =='done':
        break
        
    #   try and except block for invalid inputs
    try:
        finput_data = float(input_data)
    except:
        print('Invalid imput')
        continue
    
    if maximum_num is None:
        maximum_num = finput_data
    elif maximum_num < finput_data:
        maximum_num = finput_data
    
    if minimum_num is None:
        minimum_num = finput_data
    elif minimum_num > finput_data:
        minimum_num = finput_data
        
print(minimum_num,maximum_num)
