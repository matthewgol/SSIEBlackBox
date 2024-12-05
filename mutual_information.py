import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
from collections import Counter
from pyinform import transfer_entropy
from pyinform import mutual_info
colors_to_numbers = {'gru': 0, 'pty': 1, 'jfk': 2, 'lax': 3, 'las': 4, 'lis': 5, 'bru': 6, 'hkg': 7, 'icn': 8, 'mex': 9}

entropy=0
entropies=[0] * 400
num_df = 4

for baseline_cell in range(399,401):#,401):
    print(baseline_cell)
    for df_counter in range(0, num_df):
        print(df_counter)
        df = pd.read_csv(r'C:\Users\matth\PhD\Fall 2024\SSIE 501-SSE 440\Programming\ScrapingOutput\DataCollector4\blackbox_'+str(df_counter)+'.csv')
        X = df.iloc[:,baseline_cell]
        for i in range(1,df.shape[1]):
            Y = df.iloc[:,i]
            entropies[i-1]+=float(mutual_info(X.replace(colors_to_numbers),Y.replace(colors_to_numbers)))
    entropies = [entropy/num_df for entropy in entropies]
    print(entropies)
    data_100,data_200,data_300,data_400 = entropies[:100],entropies[100:200],entropies[200:300],entropies[300:400]
    q1,q2,q3,q4 = np.reshape(data_100,(10,10)),np.reshape(data_200,(10,10)),np.reshape(data_300,(10,10)),np.reshape(data_400,(10,10))
    figure,axis = plt.subplots(2,2, figsize=(9,9))
    plt.figure(figsize=(8, 8))
    sns.heatmap(q1, annot=True, fmt=".1f", cmap="Blues", ax=axis[0,1], vmin=0, vmax=1)
    axis[0,1].set_title("Q1")
    sns.heatmap(q2, annot=True, fmt=".1f", cmap="Blues", ax=axis[0,0], vmin=0, vmax=1)
    axis[0,0].set_title("Q2")
    sns.heatmap(q3, annot=True, fmt=".1f", cmap="Blues", ax=axis[1,0], vmin=0, vmax=1)
    axis[1,0].set_title("Q3")
    sns.heatmap(q4, annot=True, fmt=".1f", cmap="Blues",  ax=axis[1,1], vmin=0, vmax=1)
    axis[1,1].set_title("Q4")
    figure.suptitle(f"Mutual Information For Cell#{baseline_cell-0}")
    plt.savefig(r'C:\Users\matth\PhD\Fall 2024\SSIE 501-SSE 440\Programming\BlackBox1_Full_MI\MI_cell_'+str(baseline_cell-1)+'.jpg')
    plt.show()
    entropies=[0] * 400