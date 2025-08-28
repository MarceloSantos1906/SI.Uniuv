from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pickle
import os

directory = "./pkl/"
pickle_data = []

print("\n\n--- Gaussian Naive Bayes Classifier ---\n\n")

for file in os.listdir(directory):
    if file.endswith(".pkl"):
        print("Loading file: " + file)
        with open(os.path.join(directory, file), "rb") as f:
            x_train, y_train, x_test, y_test = pickle.load(f)
            print(f"x_train shape: {x_train.shape}, y_train shape: {y_train.shape}")
            print(f"x_test shape: {x_test.shape}, y_test shape: {y_test.shape}")
            if len(x_train) != len(y_train) or len(x_test) != len(y_test):
                print(f"Inconsistent number of samples, skipping {file}.")
                continue
            model = GaussianNB()
            model.fit(x_train, y_train)
            previsoes = model.predict(x_test)
            accuracy = accuracy_score(y_test, previsoes)
            cm = ConfusionMatrix(model)
            cm.fit(x_train, y_train)
            cm.score(x_test, y_test)
            print(f"Accuracy for {file}: {accuracy}")

print("\n\n--- KNN Classifier ---\n\n")

for file in os.listdir(directory):
    if file.endswith(".pkl"):
        print("Loading file: " + file)
        with open(os.path.join(directory, file), "rb") as f:
            unpickler = pickle.Unpickler(f)
            x_train, y_train, x_test, y_test = unpickler.load()
            print(f"x_train shape: {x_train.shape}, y_train shape: {y_train.shape}")
            print(f"x_test shape: {x_test.shape}, y_test shape: {y_test.shape}")
            if len(x_train) != len(y_train) or len(x_test) != len(y_test):
                print(f"Inconsistent number of samples, skipping {file}.")
                continue
            model = KNeighborsClassifier(n_neighbors=5)
            model.fit(x_train, y_train)
            previsoes = model.predict(x_test)
            accuracy = accuracy_score(y_test, previsoes)
            cm = ConfusionMatrix(model)
            cm.fit(x_train, y_train)
            cm.score(x_test, y_test)
            print(f"Accuracy for {file}: {accuracy}")

