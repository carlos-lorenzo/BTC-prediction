from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from __dataset import DataSet
import pickle

df = DataSet("dataBTC.csv", 2500)
X_train, X_test, y_train, y_test = df.createDataSet()

#Train :)
model = MLPClassifier()
print("Training...")
model.fit(X_train, y_train)

#Save model
with open("btc_model", "wb") as f:
    pickle.dump(model, f)
