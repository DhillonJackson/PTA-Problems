import pandas
import matplotlib.pyplot as plt
a=pandas.read_excel(r"C:\Users\86183\Desktop\try.xlsx")
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(10,60))
y=a['销量']
label=a['城市']
plt.pie(y,labels=label,autopct='%1.1f%%')
plt.axis('equal')
plt.title('What the hell')
plt.show()