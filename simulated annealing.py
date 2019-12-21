import pandas as pd
import random as rd
import numpy as np
import xlrd

df = pd.read_excel('data.xlsx', delimiter=';')
count_rows = len(df)

def swap(data, a, b):
    help = data.iloc[a].copy()
    data.iloc[a] = data.iloc[b]
    data.iloc[b] = help
    return data

def whenend(data):
    for i in range(count_rows):
        if i == 0:
            data.iloc[i, 3] = data.iloc[i, 1]
            d1 = data.iloc[i, 3].copy()
        elif i == (count_rows-1):
            data.iloc[i, 3] = data.iloc[i, 1] + d1
        else:
            data.iloc[i, 3] = data.iloc[i, 1] + d1
            d1 = data.iloc[i, 3].copy()

def odch(data):
    df['odchy'] = (df.Termin - df.Nakiedy) ** 2



# w funkcji okreslamy dlugosc
def sasiedztwo():
    list = []
    while len(list)<5:
        random = rd.randint(0, count_rows-1)
        if random not in list:
            list.append(random)
    return list

temp = 205000
def templow():
    global temp
    temp =temp * 0.99

def main(data):
    data_copy = data.copy()
    min1 = data.odchy.sum()
    s = sasiedztwo()

    min_sas = []
    for i in range(4):
        swap(data, s[0], s[i+1])
        whenend(data)
        odch(data)
        min_sas.append(data.odchy.sum())

        swap(data, s[0], s[i+1])


    best_sas = min(min_sas)
    best_index = min_sas.index(min(min_sas))
    print(best_index)
    print(s[0], s[best_index+1])
    swap(data, s[0], s[best_index+1])
    whenend(data)
    odch(data)

    data_copy2 = data.copy()

    print(min1, best_sas)

    prob = np.exp((abs(min1-best_sas))/temp).copy()
    prob2 = round(1/prob, 4)
    w = rd.random()
    print(prob2, w)
    templow()
    if min1 < best_sas and prob2<w:
        return data_copy
    else:

        return data_copy2


df['Nakiedy'] = 0
whenend(df)
odch(df)
for i in range(1500):
    final = main(df)
    df = final.copy()
#result
print(final.odchy.sum())


final.to_csv("result_sum.csv")













