import pandas as pd
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

tabu_list =[]
def tabu(tabu_lis, tabu1, tabu2):
    tabu_lis = tabu_list
    tabu_lis.append((tabu1, tabu2))
    if len(tabu_lis)>3:
        del tabu_lis[0]

def main(data):
    comb = []
    print("dzial")
    add_first = True
    minimalna = 0
    for i in range(count_rows-1):
        for j in range(i+1, count_rows):
            swap(data, i, j)
            whenend(data)
            odch(data)
            odchylenia = data.odchy.sum()
            comb.append(odchylenia)
            if (i, j) not in tabu_list:
                if add_first is True or odchylenia < minimalna:
                    add_first = False
                    first = i
                    second = j
                    minimalna = odchylenia
            swap(data, i, j)

    swap(data, first, second)
    tabu(tabu_list, first, second)
    whenend(data)
    odch(data)
    print(data.odchy.sum())
    return data

df['Nakiedy'] = 0
whenend(df)
odch(df)

#liczba iteracji
for i in range(5):
    final = main(df)
    df = final.copy()

#result
print(final.odchy.sum())


final.to_csv("tabu.csv")













