import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("Heart_Disease_Prediction (2).csv")
df['Heart Disease'] = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})
df['ST depression'] = df['ST depression'].astype(int)

X = df.drop("Heart Disease", axis=1)
y = df["Heart Disease"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
