import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("student_data.csv")

X = df[['hours_studied', 'sleep_hours', 'phone_usage', 'attendance']]
y = df['marks']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))