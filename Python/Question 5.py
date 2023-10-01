import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV      
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer #transform different types


os.chdir("C:/Users/xavie/OneDrive/Desktop/Rstudio files/dataverse_files")

data7 = pd.read_csv("2007.csv")
data8 = pd.read_csv("2008.csv")

data78 = data7.merge(data8,how='outer')

data78['TotalDelay']=data78['DepDelay']+data78['CarrierDelay']
+data78['WeatherDelay']+data78['NASDelay']+data78['SecurityDelay']+data78['LateAircraftDelay']

data78['TF'] = np.where(data78['TotalDelay'] >0, 1,0)

features = ['UniqueCarrier', 'Origin', 'Dest', 'DayofMonth', 'TF']
X = data78[features].copy()

numerical_features = ['DayofMonth']

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer()),
    ('scaler', StandardScaler())])

categorical_features =['UniqueCarrier', 'Origin', 'TF','Dest']

categorical_transformer =Pipeline(steps=[
    ('imputer', SimpleImputer()),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

data_transformer= ColumnTransformer(
    transformers=[
        ('numerical', numerical_transformer, numerical_features),
        ('categorical', categorical_transformer, categorical_features)]) 

X_train, X_test, TF_train, TF_test = train_test_split(X, data78.TF, test_size=0.2,random_state=1)

param_grid= {
    'data_transformer__numerical__imputer__strategy': ['mean', 'median'],
    'data_transformer__categorical__imputer__strategy': ['constant','most_frequent']
}
pipe_lr = Pipeline(steps=[('data_transformer', data_transformer),
                      ('pipe_lr', LogisticRegression(max_iter=10000, penalty = 'none'))])
grid_lr = GridSearchCV(pipe_lr, param_grid=param_grid)
grid_lr.fit(X_train, TF_train)
