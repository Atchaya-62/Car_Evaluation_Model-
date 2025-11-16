import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

data = pd.read_csv('car_evaluation.csv',names=column_names)
print(data.columns)

label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le


X = data.drop('class', axis=1)
y = data['class']


model = DecisionTreeClassifier()
model.fit(X, y)


joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print('Model and label encoders saved successfully.')       