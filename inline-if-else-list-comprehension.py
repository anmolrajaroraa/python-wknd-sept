a = 10
b = 20
# diff = a - b

# if a > b:
#     diff = a - b
# elif b > a:
#     diff = b - a
# else:
#     diff = 0

# diff = a - b if a > b else b - a

#single line if-else (inline if-else)
diff = (a - b) if (a > b) else ( (b - a) if (b > a) else 0 )

# print(diff)

list1 = []
for i in range(1,101):
    if i % 2 == 0 or i % 3 == 0:     #   % -> modulus (after dividing it gives us back the remainder)
        list1.append(i)

# for i in range(6,101,6):
#     list1.append(i)

# print(list1)

#list comprehension
# [ expression that will be appended in the list ; for loop ; if condition (optional) ]
# list2 = [ (i) for i in range(1,101) if ((i % 2 == 0) or (i % 3 == 0))]

list2 = [ ( i if ( ( i % 2 == 0 ) or ( i % 3 == 0 ) ) else 0 ) for i in range(1,101) ]
# print(list2)
# for i in range(1,101):
#     list2.append(i)



newList = [ 1, 2, 3, 4, [ 5, 6, 7 ], [ 8, 9, 10 ] ]
print(newList.count(5))

# for element in newList:
#     if type(element) == int:
#         print(element)
#         continue
#     for inner_element in element:
#         print(inner_element)

searchElement = 10

if newList.count(searchElement) > 0:
    print("Element exists")
else:
    for element in newList:
        if type(element) == list:
            if element.count(searchElement) > 0:
                print("Element exists")
                break