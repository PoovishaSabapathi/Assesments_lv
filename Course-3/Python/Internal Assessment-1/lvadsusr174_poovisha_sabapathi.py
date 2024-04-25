# -*- coding: utf-8 -*-
"""lvadsusr174_poovisha_sabapathi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JzPgsoKGT0VjP3pFBbsI2ylZ3cU4SY3c

1.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/sample_data/Final Dataset - IPL.csv')
df=pd.DataFrame(data)

df #no of rows and columns present in the dataset
numerical_colunms = df.columns[df.dtypes !="object"]# for numerical_colunms
cataegorical_colunms = df.columns[df.dtypes =="object"]# for categorical_colunms
df.isnull().sum()#finding any duplicates present and suming the duplicates

"""2."""

#there is no missing values prsent,as we can see in the qustion1. if there is some missing values we can relace them or we can drp them
#df.dropna(inplace=True)#for missing values in row
#df.dropna(axis=1, inplace=True)# fro missing valyes in column
df.duplicated().sum()#for finding duplicates in the table and finding its sum.here no duplicates present
df.drop_duplicates()#if the duplicates has to removed we can drop those

"""3.descriptive statistics"""

df.describe()

mean1=df['first_ings_score'].mean()
print(mean1)
median1=df['first_ings_score'].median()
print(median1)
mode1=df['first_ings_score'].mode()
print(mode1)
mean2=df['second_ings_score'].mean()
print(mean2)
median2=df['second_ings_score'].median()
print(median2)
mode2=df['second-ings-score'].mode()
print(mode2)
#here are some examples. but we can calculate using df.descibe().
#it gives the count, mean, std, min, max for all the numerical values.

"""4.data visualization"""

#histogram plot for first ings score.similarly we can do for secong ings score also.
x=df['first_ings_score'].count()
sns.histplot(data=df,x='first_ings_score',bins=10,color='green')
plt.title('histogram plot for first ings score')
plt.show()
#first ings vs secong ings wkts scatter plot.
x=df['first_ings_wkts'].count()
y=df['second_ings_wkts'].count()
sns.scatterplot(data=df,x='first_ings_wkts',y='second_ings_wkts',color='black',marker='o',alpha=0.8)
plt.title('first vs second ings wkt')
plt.show()
#bar plots for first vas second ings score
plt.figure(figsize=(50,30))
sns.barplot(data=df,x='first_ings_score',y='second_ings_score')
plt.show()
#pie chart for match winner
x=df['match_winner'].value_counts()
plt.pie(data=df,x=x,startangle=90,pcmt=True,annot=True)
plt.legend()
plt.show()

"""5.correlation"""

#correlation
a=df['toss_decision']
b=df['match_winner']
z=np.correlate(a,b)
plt.figure(figsize=(50,30))
sns.heatplot(data=df,x=z,cmap='coolwarm')
plt.title('correlation between toss decision and match winner')
plt.show()
#venue vs wonby
x=df['venue'].counts()
#print(x)
plt.plot(x=x,y=['first_ings_scores','second_ings_scores'],kind='bar',color=['orange','green'])
plt.legend()
plt.title("Venue vs first_ings_score and secon_ings_score")
plt.show()

"""6.Outlier detection"""

q1=df['margin'].quantile(0.25)
q3=df['margin'].quantile(0.75)
IQR=q3-q1
lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR
outliers=df[(df['margin']<lower_bound)|(df['margin']>upper_bound)]
print("outliers",outliers)
df['margin']=df['margin'].apply(lambda x:min(max(x,lower_bound),upper_bound))
plt.figure(figsize=(20,20))
sns.boxplot(x=df["margin"])
plt.title(f'box plot for margin')
plt.show()
#In the given data set no outliers for margin is present
#outlier for first ings score
q1=df['first_ings_score'].quantile(0.25)
q3=df['first_ings_score'].quantile(0.75)
IQR=q3-q1
lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR
outliers=df[(df['first_ings_score']<lower_bound)|(df['first_ings_score']>upper_bound)]
df['margin']=df['margin'].apply(lambda x:min(max(x,lower_bound),upper_bound))
plt.figure(figsize=(20,20))
sns.boxplot(x=df["margin"])
plt.title(f'box plot for margin')
plt.show()

"""7."""

date_played=pd.to_datetime(df['date'])
date_played['Mon']=date_played.dt.month(df['date'])
plt.plot(x=date_played['Mon'],y=date_played['Mon'].index,marker='*',color='hotpink',linestyle='--',linewidth=3)
plt.plot(x=date_played['Mon'],y=date_played['first_ings_scores'],marker='o',color='yellow',linestyle='--',linewidth=1)
plt.legend(fontsize=20,loc='upper right')
plt.xlable('Month')
plt.ylabel('first_ings_score')
plt.title("trend over venue")
plt.show()

"""8."""

x=df['player_of_the_match'].value_counts().sort_values(ascending=False).head(10)
plt.figure(figsize=(20,10))
plt.pie(data=df,x=x,startangle=90)
plt.legend(loc='upper left',fontsize=20,autopct=True)
plt.title('player of the match')
plt.show()

"""9."""

a=df['top_scorer'].value_counts().sort_values(ascensing=False).head(10)
b=df['best_bowling_figure'].value_counts().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=a,y=df['match_id'],edgecolor='red',color='yellow',width=5,data=df)
sns.barplot(x=b,y=df['match_id'],edgecolor='black',color='purple',width=3,data=df)
plt.legend(loc='upper right')
plt.show()
#the player of the match is shown and the top scorer and bowling figure is also shown. the match played in some stadium is good.