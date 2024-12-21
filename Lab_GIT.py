import json
import csv


# 1)

path = './log_100.json'

with open(path) as fp:
    j = json.load(fp)


ip_dict = {}

for row in j:
    if row['ip'] not in ip_dict:
        ip_dict[row['ip']] = 1

    else:
        ip_dict[row['ip']] += 1

tmp_lst = []

for val in ip_dict.values():
    tmp_lst.append(val)
tmp_lst.sort(reverse=True)
print((sum(tmp_lst[:3]) / len(j)) * 100)


# 2)
path = './log_100.json'

with open(path) as fp:
    j = json.load(fp)

ip_dict = {}

for row in j:
    if row['ip'] not in ip_dict:
        ip_dict[row['ip']] = 1

    else:
        ip_dict[row['ip']] += 1


tmp_lst = []

for val in ip_dict.values():
    if val == 1:
        tmp_lst.append(val)
    else:
        continue

print(len(tmp_lst))


# 3)

path = './log_cereals.csv'
d = {}

with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        d[row[0]] = row[1]
    del d['Год']

min_key = min(d, key=d.get)
min_value = d[min_key]
print(f"В {min_key} году пачка манки (1кг) стоила: {min_value}")

# 4)

path = './log_cereals.csv'
d_m = {}
d_g = {}

with open(path) as f:
    reader = list(csv.reader(f))

for row in reader:
    if row[0] != 'Год':
        d_m[row[0]] = row[1]
for row in reader:
    if row[0] != 'Год':
        d_g[row[0]] = row[2]


tmp_lst_m = []
tmp_lst_g = []
for val in d_m.values():
    tmp_lst_m.append(float(val))
for val in d_g.values():
    tmp_lst_g.append(float(val))

print(f"""Средняя цену за манную крупу: {
    sum(tmp_lst_m) / len(tmp_lst_m)}, а за крупу гречневую: {
    sum(tmp_lst_g) / len(tmp_lst_g)} """)


# 5)

path = './log_full.csv'

with open(path) as f:
    reader = list(csv.reader(f))

lst = []

for row in reader:
    j = str(row[1])
    lst.append(j)

d = {}

for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

max_key = max(d, key=d.get)
print(max_key)

# 6)
result = d[max_key] / len(lst)*100
print(result)

# 7)

lst_1 = []

for row in reader:
    if row[1] == max_key:
        j = str(row[0])
        lst_1.append(j)

result_1 = lst_1[-1]


lst_2 = []

for row in reader:
    if row[1] == max_key:
        j = str(row[2])
        lst_2.append(j)

result_2 = lst_2[-1]

suspicious_agent = {
    "ip": max_key,            # самый частовстречаемый ip в логах
    'fraction': result,     # процент запросов с таким ip от общего кол-ва запросов
    'count': d[max_key],         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': result_2,     # последний user-agent для этого ip
        'timestamp': result_1,  # последний timestap для этого ip
    }
}

print(suspicious_agent)
