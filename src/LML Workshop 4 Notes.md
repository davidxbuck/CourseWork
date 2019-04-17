# Notes from the Learn Machine Learning workshop 4

## 1. Data 

- Data warehouses are highly complex
- Sources of data are not designed with Machine Learning in mind
    - Features altered
    - Impossible to do exact match
- Need to think about end-to-end
    - Do data sources permit the design of an automated end-to-end process?
    
- Data Cleaning
    - Handle missing values
        - Why missing? Drop records or replace missing values?
    - Handle outliers
        - Why are there outliers?
    
- Data Visualisation
    - Histogram, boxplot, etc.
- Feature Selection
- Feature Creation



## 2. Features
### Feature Selection

- Very important when the number of features are large
- Are all the features helpful for the model?

3 main families of feature selection algorithm 

#### Filter methods

- Select features one at a time
- Low variance, correlation with the target

#### Wrapper methods

- Evaluate a subset of methods
- Allow to detect interations between features
- Forward feature selection, backwards feature selection

#### Embedded methods

- The machine learning model performs both feature selection and classification
- Random forest



### Feature creation
- Useful to add more features to an existing dataset?

3 main families of feature creation algorithm

#### Manual creation
- create new features based on domain knowledge
- Derive new features (e.g. BMI from height and weight)

#### Feature construction algorithms
- Create new features by combining existing ones in a specific way
- E.g. X-of-N

#### Embedded methods
- The algorithm performs feature construction during the learning
- Decision Tree, NN


## 3. Model

10% of time used on the model

How large is the dataset?
- local development/cloud/cluster?

Wide range of ML algorithms
- Choose depending on problem type
- The data type (sparse datasets, images), the metric, supported tech stack, batch or real time, etc.

Pick a few algorithms and test them
- Use hyper parameter tuning to optimise and evaluate the model
- External parameters used by the ML algorithm to build a model
 - Independent of the input data (learning rate, number of clusters in kmeans, etc.)
 - Cannot be defined during the model training (coefficients of a linear regression algorithm, splitting point of a node level for decision trees, etc.
- Examples
 - Manual Search
 - Grid Search (not in practice)
 - Random Search
 

## Deployment to production

### Productionisation of the training
- Script the model development (pre-processing and model creation)
- Automate model development?

### Script the model prediction

Model built in EC2
Model stored in S3
Preductions run in AWS Lambda
AWS Lambda
200ms to instantiate
Can add any missing libraries (e.g. joblib, pandas) in layers
Can't take more than 15 mins to run
Only pay for Lambda while it's processing (not like EC2)
(Used lightgbm ML algorithm)
acloud.guru us implemented in Lambda
Can save a scikit pipline in joblib

#%%
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

#%%
df_train = pd.read_csv('https://raw.githubusercontent.com/abitravers1989/machine_learning_challenge/master/DataSet/train.csv', delimiter='\t')
df_test = pd.read_csv('https://raw.githubusercontent.com/abitravers1989/machine_learning_challenge/master/DataSet/test.csv', delimiter='\t')

#%%
X_train = df_train.drop(['label_target', 'ids'], axis=1)
y_train = df_train['label_target']
X_test = df_test.drop(['label_target', 'ids'], axis=1)
y_test = df_test['label_target']
print(X_train.info())
print(X_test.info())
print(y_train.head())
print(y_test.head())

#%%
sns.heatmap(df_train.iloc[:,33:].corr(), square=True, cmap='RdYlGn')

#%%
model = ExtraTreesClassifier()
model.fit(X_train,y_train)
print(model.feature_importances_) #use inbuilt class feature_importance of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X_train.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()




