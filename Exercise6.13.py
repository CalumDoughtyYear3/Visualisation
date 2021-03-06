import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import seaborn as sns #datasets library
import numpy as np

trains = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week6//Visualisation//files//train.csv")
#3
#trains.plot(kind='box', subplots=True, layout=(4,4))

#4
#count passengerId where Survived=1
# trains['Survived'].value_counts().sort_values(ascending=True).plot.bar()
# plt.title('Titanic')
# plt.ylabel("No. of Survivors")
# plt.xlabel("1 = Survived")
# plt.show()

#5
#Produce a horizontal bar chart showing all passenger classes (in numerical order)
#trains['Pclass'].value_counts().sort_values().plot.barh()
#trains['Pclass'].value_counts(sort=True).plot.barh()
trains.groupby(['Pclass']).size().plot(kind='barh') #decent
#sns.barplot(x=trains['Pclass'].value_counts().sort_values(), y=trains['Pclass'], data=trains, orient='h')
plt.title('Titanic classes')
plt.xlabel("No. in a class")
plt.ylabel("Classes")
plt.tight_layout()
plt.show()

#6
#Produce a density plot for number of siblings (SibSp)

