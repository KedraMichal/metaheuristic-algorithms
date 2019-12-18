import pandas as pd
import random as rd
import xlrd

df = pd.read_excel('data.xlsx')
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


def random():
    a = rd.randint(0, count_rows-1)
    b = rd.randint(0, count_rows-1)
    while a == b:
        b = rd.randint(0, count_rows-1)
    return a,b


def main(data):
    data_copy = data.copy()
    min1 = data.odchy.sum()
    k = random()
    random1 = (k[0])
    random2 = (k[1])
    swap(data, random1, random2)
    whenend(data)
    odch(data)
    min2 = data.odchy.sum()
    data_copy2 = data.copy()
    print(min1, min2)
    if min1 < min2:
        return data_copy
    else:
         return data_copy2


df['Nakiedy'] = 0
whenend(df)
odch(df)

for i in range(300):
    final = main(df)
    df = final.copy()
#result
print(final.odchy.sum())

final.to_csv("climbing_result.csv")


