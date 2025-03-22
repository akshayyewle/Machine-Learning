# Import Packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, RandomizedSearchCV, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, make_scorer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Data Import
df = pd.read_csv('vehicle_emissions.csv')
# print(df.info())

# Feature-Target Split
X = df.drop(columns=['CO2_Emissions'],axis=1)
y = df['CO2_Emissions']

# Categorical-Numerical Split
X_cat_cols = ['Make', 'Model', 'Vehicle_Class', 'Transmission']
X_num_cols = ['Model_Year', 'Engine_Size', 'Cylinders', 'Fuel_Consumption_in_City(L/100 km)', 'Fuel_Consumption_in_City_Hwy(L/100 km)',
              'Fuel_Consumption_comb(L/100km)','Smog_Level']
X_cat = X.select_dtypes(include=['object'])
X_num = X.select_dtypes(exclude=['number'])

# Preprocessing Pipeline - Numerical Features
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Preprocessing Pipeline - Categorical Features
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Preprocessing Pipeline - Column Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, X_num_cols),
        ('cat', cat_transformer, X_cat_cols)
    ]
)

# Final Pipeline
from sklearn.ensemble import RandomForestRegressor
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Train
pipeline.fit(X_train, y_train)

# Model Prediction
y_pred = pipeline.predict(X_test)
# print("Predictions: ", y_pred)

# Model Evaluation
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", root_mean_squared_error(y_test, y_pred))
print("R2 Score: ", r2_score(y_test, y_pred))

# References:
# https://github.com/Joshwen7947/Machine-Learning-Pipeline 
# https://www.youtube.com/watch?v=777Qb0gHuJU