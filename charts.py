# -*- Encoding: utf-8 -*-
import sys
import numpy as np
import matplotlib
matplotlib.use('GTK')
import matplotlib.pyplot as plt


def genrateChart(resluts, lowerbounds, chartFileName):
    N = resluts.__len__()

    ind = np.arange(N)
    width = 0.35   
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, resluts, width, color='r')


    rects2 = ax.bar(ind + width, lowerbounds, width, color='y')

    ax.set_ylabel('Czas wykonania zadań')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((""))

    ax.legend((rects1[0], rects2[0]), ('Wynik', 'Najlepsze znane dolne ograniczenie'),loc="lower left")


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='left', va='top')

    autolabel(rects1)
    autolabel(rects2)

    #plt.show()
    fig.savefig(chartFileName)

def readFile(f):
    return [int(line) for line in f]   


for num,testGroupName in enumerate(sys.argv):
    if num == 0:
        continue
    f1 = open("results/"+testGroupName)
    f2 = open("lowerbounds/"+testGroupName)
    genrateChart(readFile(f1),readFile(f2), "charts/" + testGroupName + "chart.png")
    f1.close()
    f2.close()