#symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG HPQ'

"""Accessing and Assigning the elements in the list"""
#list_of_sym=symbols.split()
# print(list_of_sym)

# print(list_of_sym[2])
# print(list_of_sym[-1])

# list_of_sym[-2]='NET'
# print(list_of_sym)

"""Looping over lists"""

# for item in list_of_sym:
#     print("Item=",item)

# for index in range(len(list_of_sym)):
#     print(index,list_of_sym[index])


# element=list_of_sym[0]

# for index in range(2,len(list_of_sym)):
#     if element in list_of_sym[index]:
#         print(True)

#     if element == list_of_sym[index]:
#         print(index)
"""Insert,append elements in the lists"""

# try:
#     list_of_sym.pop(9)  # There is element in the 9th position here
# except:
#     list_of_sym.append('RHQ')
#     list_of_sym.insert(1,'NBQ')

# 

"""list of lists"""
my_list=[[123,55],[123]]

print(my_list)
print(my_list[0][1])




