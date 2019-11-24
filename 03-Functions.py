#map,filter,operator,lambda,reduce,accumulate,enumerate,zip

def convert_temp_to_f(c):
    return 9/5 * c + 32

# temp = 35
# f = convert_temp_to_f(temp)
# print(f)

temp_list = [0,9,19,29,39,49,59,69,79,89,99]

# f_list = []
# for temp in temp_list:
#     # print(convert_temp_to_f(temp))
#     f_list.append(convert_temp_to_f(temp))

f_list = [convert_temp_to_f(temp) for temp in temp_list]

print(f_list)

new_f_list = list(map(convert_temp_to_f, temp_list)) 
print(new_f_list)

# for i in range(len(temp_list)):
#     print(convert_temp_to_f(temp_list[i]))