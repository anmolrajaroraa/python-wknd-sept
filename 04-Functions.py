def even(x):
    return x % 2 == 0

number = 98

# print(even(number))

list1 = [i for i in range(1,101)]
list2 = [i for i in range(101,201)]
list3 = list(zip(list1,list2))
print(list3)

# even_numbers = list(map(even, list1))

# print(even_numbers)

# even_numbers = []

# for number in list1:
#     if even(number):
#         even_numbers.append(number)

# even_numbers = [number for number in list1 if even(number)]

# print(even_numbers)

new_list = list(filter(even, list1))

print(new_list)

#map calls the function for each value of iterable and appends the return result into a list
#filter calls the function for each value of iterable but checks if the value returned is true or not, if it is true it appends the arguments sent to the function into a list