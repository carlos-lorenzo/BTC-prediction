from statistics import mode
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from datasetv2 import DataSet
import pickle

df = DataSet("dataBTC_h1.csv", 30000)
X_train, X_test, y_train, y_test = df.createDataSet()

#Train :)
model = MLPClassifier()
print("Training...")
model.fit(X_train, y_train)

#Save model
with open("btc_model", "wb") as f:
    pickle.dump(model, f)
