# Задание №3

files = ['1.txt', '2.txt', '3.txt']

dict_r = {}
dict_w = {}

for texts in files:
    with open('./HW_3/' + texts, 'r', encoding='utf-8') as file:
        text = file.read().split('\n')
        s = len(text)
        dict_r[s] = texts
        dict_w[s] = text

with open('./HW_3/result.txt', 'w', encoding='utf-8') as f:
    for i in sorted(dict_r.keys()):
        same = '\n'.join(dict_w[i])
        f.write(f'{dict_r[i]}\n{i}\n{same}\n')

# Альтернативный способ решения

# lis = []

# for texts in files:
#     with open('./HW_3/' + texts, 'r', encoding='utf-8') as file:
#         text = file.read().split('\n')
#         lis.append([texts,len(text), '\n'.join(text)])
# sort = sorted(lis, key=lambda student: student[1])

# with open('./HW_3/result.txt', 'w', encoding='utf-8') as f:
#     for item in sort:
#         f.write(f'{item[0]}\n{item[1]}\n{item[2]}\n')