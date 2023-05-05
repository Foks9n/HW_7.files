# Задание №3

files = ['1.txt', '2.txt', '3.txt']

dict_r = {}
dict_w = {}

for texts in files:
    with open('./HW_3/' + texts, 'r', encoding='utf-8') as file:
        txt = file.read().split('\n')
        s = len(txt)
        dict_r[s] = texts
        dict_w[s] = txt

sorted_dict_r = sorted(dict_r.items())
print(sorted_dict_r)

with open('./HW_3/result.txt', 'w', encoding='utf-8') as f:
    for k, v in sorted_dict_r:
        f.write(f'{str(k)}\n{v}\n')
        for text in dict_w[k]:
            f.write(f'{text}\n')