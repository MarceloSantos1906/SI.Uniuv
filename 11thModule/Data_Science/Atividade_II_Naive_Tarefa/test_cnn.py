from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from yellowbrick.classifier import ConfusionMatrix
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import layers, models
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import datetime
import pickle
import os
import json


class EpochTracker(tf.keras.callbacks.Callback):
    def __init__(self, json_path):
        super().__init__()
        self.json_path = json_path
        self.epochs_done = 0

    def on_epoch_end(self, epoch, logs=None):
        self.epochs_done += 1
        with open(self.json_path, "w") as f:
            json.dump({"epochs_done": self.epochs_done + self._get_previous_epochs()}, f)

    def _get_previous_epochs(self):
        try:
            with open(self.json_path, "r") as f:
                return json.load(f).get("epochs_done", 0)
        except Exception:
            return 0


class CNN:
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def evaluate(self, x_test, y_test):
        y_test_cat = to_categorical(y_test, num_classes=self.num_classes)
        test_loss, test_acc = self.model.evaluate(x_test, y_test_cat)
        return test_loss, test_acc

    def predict(self, x):
        predictions = self.model.predict(x)
        return np.argmax(predictions, axis=1)

    def load_model(self, file_path):
        self.model = models.load_model(file_path)

    def plot_confusion_matrix(self, y_true, y_pred, file_name):
        cm = ConfusionMatrix(estimator=self.model)
        cm.fit(y_true, y_pred)
        cm.score(y_true, y_pred)
        #cm.show(outpath=f"{file_name}_confusion_matrix.png")
        cm.save(f"{file_name}_confusion_matrix.png")


directory = "./pkl/"
directory_model = "./cnn/"

for file in os.listdir(directory):
    if file.endswith(".pkl"):
        print("Loading file: " + file)
        with open(os.path.join(directory, file), "rb") as f:
            x_train, y_train, x_test, y_test = pickle.load(f)
            if len(x_train) != len(y_train) or len(x_test) != len(y_test):
                print(f"Inconsistent number of samples, skipping {file}.")
                continue

            for model in os.listdir(directory_model):
                if model.endswith(".keras") or model.endswith(".h5"):
                    
                    label_encoder = LabelEncoder()
                    y_train = label_encoder.fit_transform(y_train)
                    y_test = label_encoder.fit_transform(y_test)
                    
                    x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))
                    
                    print("Loading model: " + model)
                    model_cnn = CNN(num_classes=len(np.unique(y_train)))
                    model_cnn.load_model(os.path.join(directory_model, model))
                    #model_cnn.evaluate(x_test=x_test, y_test=y_test)
                    y_test_pred = model_cnn.predict(x_test)
                    accuracy = accuracy_score(y_test, y_test_pred)
                    print(f"Accuracy for model {model} on dataset {file} : {accuracy:.4f}")
                    #model_cnn.plot_confusion_matrix(y_true=y_test, y_pred=y_test_pred, file_name=f"{file.split('.')[0]}_{model.split('.')[0]}")
