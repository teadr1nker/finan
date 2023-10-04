#!/usr/bin/python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp


def analyse(x, name):
    print('\n', name)
    figure, axis = plt.subplots(1, 3)
    axis[0].plot(x)
    axis[0].set_title(name)
    axis[0].text(0, min(x), str(x.describe()))
    axis[1].hist(x)
    axis[1].set_title(f'Histogram {name}')
    axis[2].boxplot(x)
    axis[2].set_title(f'Boxplot {name}')

    try:
        x = list(x[0])
    except:
        x = list(x)
    res = sp.stats.shapiro(x)
    res2 = sp.stats.kstest(x, 'norm')
    print(res2)
    axis[1].set_xlabel(f'shapiro pvalue: {round(res.pvalue, 5)}\nkstest pvalue: {round(res2.pvalue, 5)}')
    plt.show()
    print(res)


path = 'datasets/'
files = []
for sheet in os.listdir(path):
    files.append(sheet)

n = int(input(f'Choose file\n{files}\n0-{len(files)-1}: '))
if 'FINAM' in files[n]:
    tag = '<CLOSE>'
    delimiter = ','
else:
    tag = 'Close'
    delimiter = ','

df = pd.read_csv(path + files[n], delimiter=delimiter)

analyse(df[tag], f'dataset {files[n]}')

profit = [(df[tag][i+1] - df[tag][i]) / df[tag][i] for i in range(len(df)-1)]
analyse(pd.DataFrame(profit), f'profit {files[n]}')
