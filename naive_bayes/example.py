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


print(df.info())

df = df.apply(lambda x : x.astype('category'))

df1 = df.apply(lambda x : x.cat.codes)

#%%

train = df[:10]
test = df1[-4:]

y_train = train.pop('Play')
x_train = train

y_test = test.pop('Play')
x_test = test

#%%

model = MultinomialNB()

model_obj = model.fit(x_test, y_test)
#model_obj = model.fit(x_train, y_train) 

#%%

y_out = model.predict(x_test)
#y_out = model.predict(x_train)

#%%
print('Testing Accuracy:', model.score(x_test, y_test))
#print('Training Accuracy: ', model.score(x_train, y_train))

