##Machine learning explores the study and construction of algorithms
##that can learn from and make predictions on data.
##Closely related to computational statistics
##Used to devise complex models and algorithms that lend themselves 
## to a prediction which in commericial use is known as predictive analysis.

#Supervised Learning
#Unsupervised Learning
#Reinforcement Learning

##Classification is the problem of identifying to which set of categories
##a new observation belongs

import pandas as pd
from  sklearn.naive_bayes import MultinomialNB

#%%

df = pd.read_csv('golf_df.csv')

print(df.head())
