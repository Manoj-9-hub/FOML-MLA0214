import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Load Data
print("Loading Iris Data...")
try:
    df = pd.read_csv('iris.csv')
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
except FileNotFoundError:
    print("iris.csv not found!")
    exit()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perceptron
print("\nTraining Perceptron...")
# Perceptron is a simple linear binary classifier, but sklearn's Perceptron supports multiclass via One-Vs-Rest
perc = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
perc.fit(X_train, y_train)

# Predict
y_pred = perc.predict(X_test)

# Evaluate
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("Predictions:", y_pred)
