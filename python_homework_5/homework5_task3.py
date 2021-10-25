with open('test_3.txt') as file:
    file_lines = file.readlines()
    staff = {}
    sum_salary = 0
    for line in file_lines:
        staff_info = line.split()
        staff.update({staff_info[0]: float(staff_info[1])})
        sum_salary += float(staff_info[1])
average_sal = sum_salary / len(staff)
print(f'Average = {average_sal}')

for k, v in staff.items():
    if v < 20000:
        print(f'{k}: {v}')
