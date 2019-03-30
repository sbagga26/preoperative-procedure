
#this file is basically the code to be ran in jupyter file 
#this is a simple machine learning module to do risk analysis of different procedures in terms of morbidity(chances of beinf diseased or critical)
# and mortality(the death rate)

# In[3]:


import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
import patsy
import sklearn
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score


# In[4]:


df7=pd.read_excel('Desktop/Project/Metadata.xlsx',sheet_name='Risks7') #edit the location of your metafile downloaded
df7


# In[5]:


plt.plot(df7['ASA'],df7['morbidity_per7'])
plt.text(3.5,45,'Morbidity',bbox=dict(facecolor='blue', alpha=0.1))
plt.plot(df7['ASA'],df7['mortality_per7'])
plt.text(3.5,17,'Mortality',bbox=dict(facecolor='orange', alpha=0.2))


# In[6]:


y, X = patsy.dmatrices('morbidity_per7 ~ morbidity_n7 + ASA', df7, return_type="dataframe")
print (X.columns)
y = np.ravel(y)
model = LinearRegression()
model = model.fit(X, y)
model.score(X, y)
y.mean()


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LinearRegression()
model2.fit(X_train, y_train)
predicted = model2.predict(X_test)
print (predicted)


# In[8]:


y, X = patsy.dmatrices('mortality_per7 ~ mortality_n7 + ASA', df7, return_type="dataframe")
print (X.columns)
y = np.ravel(y)
model = LinearRegression()
model = model.fit(X, y)
model.score(X, y)
y.mean()


# In[9]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model2 = LinearRegression()
model2.fit(X_train, y_train)
predicted = model2.predict(X_test)
print (predicted)

