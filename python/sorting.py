# list = ["6", "4", "2", "0", "9"]
# # list.sort()
# # print(list)
# # list_len = len(list)
# for i in range(list_len):

# #     list.pop(list_len-1)

# # print(list)
# # # print(a)
# # # print(b)
# # # print(c)

my_list = ["6", "4", "2", "0", "9"]
new_list = []

while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)

print(new_list)