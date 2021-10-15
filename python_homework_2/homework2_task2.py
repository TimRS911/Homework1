user_list = input('Введите список:')
result_list = user_list.split()

len_list = len(result_list)
i = 0
if len_list > 1:
    while i < len_list - 1:
        result_list[i], result_list[i+1] = result_list[i+1], result_list[i]
        i += 2

print(result_list)