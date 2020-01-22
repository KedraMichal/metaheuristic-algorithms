import pandas as pd
import xlrd
import sklearn

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

tabu_list =[]
def tabu(tabu_lis, tabu1, tabu2):
    tabu_lis.append((tabu1, tabu2))
    if len(tabu_lis)>3:
        del tabu_lis[0]

def main(data):
    comb = []
    add_first = True
    minimalna = 0
    print(tabu_list)
    for i in range(count_rows-1):
        for j in range(i+1, count_rows):
            x1 = df.iloc[i, 0] -1# po nr zadania, zeby potem dobrze byly w tabu dodane
            x2 = df.iloc[j, 0] -1
            swap(data,x1, x2)
            whenend(data)
            odch(data)
            odchylenia = data.odchy.sum()
            comb.append(odchylenia)
            if (x1, x2) not in tabu_list and (x2, x1) not in tabu_list:
                if add_first is True or odchylenia < minimalna:
                    add_first = False
                    first = x1
                    second = x2
                    minimalna = odchylenia
            swap(data, x1, x2)

    swap(data, first, second)
    tabu(tabu_list, first, second)
    whenend(data)
    odch(data)
    print(data.odchy.sum())
    return data

df['Nakiedy'] = 0
whenend(df)
odch(df)
print(df.odchy.sum())

for i in range(15):
    final = main(df)
    df = final.copy()

print(final.odchy.sum())
final.to_csv("tabu_result.csv", index=False)













