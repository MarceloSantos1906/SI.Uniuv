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
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        model = models.Sequential()
        model.add(layers.Conv1D(32, 2, activation="relu", input_shape=self.input_shape))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation="relu"))
        model.add(layers.Dense(self.num_classes, activation="softmax"))

        model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )
        return model

    def train(
        self,
        x_train,
        y_train,
        x_val,
        y_val,
        epochs=10,
        batch_size=32,
        patience=3,
        file="model",
        extra_callbacks=None,
    ):
        log_folder = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        y_train_cat = to_categorical(y_train, num_classes=self.num_classes)
        y_val_cat = to_categorical(y_val, num_classes=self.num_classes)

        callback = EarlyStopping(monitor="accuracy", patience=patience, verbose=1)
        checkpoint = ModelCheckpoint(
            filepath=f"./cnn/checkpoints/{file}_best.keras",
            monitor="accuracy",
            save_best_only=True,
            mode="min",
            verbose=1,
        )
        tensorBoard = TensorBoard(
            log_dir=log_folder,
            histogram_freq=1,
            write_graph=True,
            write_images=True,
            update_freq="epoch",
            profile_batch=2,
            embeddings_freq=1,
        )
        callbacks = [callback, checkpoint, tensorBoard]
        if extra_callbacks:
            callbacks.extend(extra_callbacks)
        history = self.model.fit(
            x_train,
            y_train_cat,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(x_val, y_val_cat),
            callbacks=callbacks,
            verbose=1,
        )
        return history

    def evaluate(self, x_test, y_test):
        y_test_cat = to_categorical(y_test, num_classes=self.num_classes)
        test_loss, test_acc = self.model.evaluate(x_test, y_test_cat)
        return test_loss, test_acc

    def predict(self, x):
        predictions = self.model.predict(x)
        return np.argmax(predictions, axis=1)

    def save_model(self, file_path):
        self.model.save("./cnn/" + file_path)

    def load_model(self, file_path):
        self.model = models.load_model(file_path)

    def plot_history(self, history, file_name):
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 2, 1)
        plt.plot(history.history["accuracy"], label="Training Accuracy")
        plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
        plt.title("Accuracy over epochs")
        plt.savefig(f"{file_name}_accuracy.png")

    def plot_confusion_matrix(self, y_true, y_pred, file_name):
        cm = ConfusionMatrix(self.model)
        cm.fit(y_true, y_pred)
        cm.score(y_true, y_pred)
        cm.show(outpath=f"{file_name}_confusion_matrix.png")


directory = "./pkl/"
epochs = 200
batch_size = 1000
patience = 3

for file in os.listdir(directory):
    if file.endswith(".pkl"):
        print("Loading file: " + file)
        with open(os.path.join(directory, file), "rb") as f:
            x_train, y_train, x_test, y_test = pickle.load(f)
            if len(x_train) != len(y_train) or len(x_test) != len(y_test):
                print(f"Inconsistent number of samples, skipping {file}.")
                continue

            label_encoder = LabelEncoder()
            y_train_enc = label_encoder.fit_transform(y_train)
            y_test_enc = label_encoder.transform(y_test)

            x_train_reshaped = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
            x_test_reshaped = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

            model = CNN(
                input_shape=(x_train.shape[1], 1),
                num_classes=len(np.unique(y_train_enc)),
            )
            file_name = file.split(".")[0]
            epochs_done_file = f"./cnn/checkpoints/{file_name}_epochs.json"
            epochs_done = 0
            if os.path.exists(epochs_done_file):
                with open(epochs_done_file, "r") as f_epochs:
                    epochs_done = json.load(f_epochs).get("epochs_done", 0)
            epochs_to_run = epochs - epochs_done

            epoch_tracker = EpochTracker(epochs_done_file)

            if (os.path.exists(f"./cnn/checkpoints/{file_name}_best.keras")):
                model.load_model(f"./cnn/checkpoints/{file_name}_best.keras")
                print(f"loaded existing model from ./cnn/checkpoints/{file_name}_best.keras")
                print("continuing training...")
                if epochs_to_run > 0:
                    history = model.train(
                        x_train_reshaped,
                        y_train_enc,
                        x_test_reshaped,
                        y_test_enc,
                        epochs=epochs_to_run,
                        batch_size=batch_size,
                        file=file_name,
                        extra_callbacks=[epoch_tracker]
                    )
                else:
                    print("Training already completed for the requested number of epochs.")
                    history = None
            else:
                history = model.train(
                    x_train_reshaped,
                    y_train_enc,
                    x_test_reshaped,
                    y_test_enc,
                    epochs=epochs,
                    batch_size=batch_size,
                    file=file_name,
                    extra_callbacks=[epoch_tracker]
                )
            test_loss, test_acc = model.evaluate(x_test_reshaped, y_test_enc)
            #model.plot_history(history, file_name=file.split(".")[0])
            model.save_model(f"{file_name}_cnn.keras")
            print(f"model saved at ./cnn/{file_name}_cnn.keras")
