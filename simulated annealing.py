import pandas as pd
import random as rd
import numpy as np
import sklearn
import xlrd

df = pd.read_excel('data.xlsx', delimiter=';')
df = sklearn.utils.shuffle(df)
df = df.reset_index(drop=True)
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

def sasiedztwo():
    list = []
    while len(list)<6: #maksymalna dlugosc sasiedztwa
        random = rd.randint(0, count_rows-1)
        if random not in list:
            list.append(random)
    return list

temp = 300000
def templow():
    global temp
    temp =temp * 0.999

def main(data):
    data_copy = data.copy()
    min1 = data.odchy.sum()
    s = sasiedztwo()
    min_sas = []
    for i in range(4):# dlugosc sasiedztwa
        swap(data, s[0], s[i+1])
        whenend(data)
        odch(data)
        min_sas.append(data.odchy.sum())
        swap(data, s[0], s[i+1])

    best_sas = min(min_sas) #najlepszy wynik z sasiedztwa
    best_index = min_sas.index(min(min_sas)) #indeks najlepszego rozw w sasiedztwie
    swap(data, s[0], s[best_index+1])
    whenend(data)
    odch(data)
    data_copy2 = data.copy()
    prob = 1/(np.exp((abs(min1-best_sas))/temp))
    w = rd.random()
    print(min1, best_sas, prob, w)
    templow()
    if min1 < best_sas and prob<w:
        return data_copy
    else:
        return data_copy2


df['Nakiedy'] = 0
whenend(df)
odch(df)
for i in range(10000):
    final = main(df)
    df = final.copy()
print(final.odchy.sum())

final.to_csv("result_sim.csv", index=False)













