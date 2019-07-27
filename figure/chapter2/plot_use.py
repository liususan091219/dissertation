import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

f,axn = plt.subplots()
f.set_size_inches(6,5)

df =  pd.read_csv("use_out.txt")

sns.heatmap(df, linewidths=.1,ax=axn,cmap='Blues',vmin=0.0, vmax=1.,xticklabels = False, annot=True, fmt=".2f")

plt.yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5, 8.5], ["STORAGE", "LOCATION", "PHONE", "CONTACT", "CAMERA", "MICROPH", "SMS", "CALENDA", "off-Diag"])
plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5, 7.5,8.5], ["STORAGE", "LOCATION", "PHONE", "CONTACT", "CAMERA", "MICROPH", "SMS", "CALENDA", "off-Diag"])
plt.xticks(rotation=90)
plt.yticks(rotation=0)

f.savefig("use_mat.pdf",bbox_inches='tight')
