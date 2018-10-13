#LinearSVC
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score,classification_report

feat=pd.read_csv('combined_features.csv')
targ=pd.read_csv('combined_targets.csv')
clf=LinearSVC()
xtrain,xtest,ytrain,ytest=train_test_split(feat,targ,test_size=0.5,random_state=42)
clf.fit(xtrain,ytrain)
pred=clf.predict(xtest)
df=pd.DataFrame(data={'pred':pred})
df.to_csv('pred_linsvc_test50.csv',index=False)
print('accuracy:',accuracy_score(ytest.values,pred))
print(classification_report(ytest.values,pred))
