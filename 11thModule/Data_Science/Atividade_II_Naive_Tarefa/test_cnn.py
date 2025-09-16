from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


directory = "./pkl/"
directory_model = "./cnn/"

for file in os.listdir(directory):
    if file.endswith(".pkl"):
        print("Loading file: " + file)
        with open(os.path.join(directory, file), "rb") as f:
            x_train, y_train, x_test, y_test = pickle.load(f)

        # Skip inconsistent datasets
        if len(x_train) != len(y_train) or len(x_test) != len(y_test):
            print(f"Inconsistent number of samples, skipping {file}.")
            continue

        # Encode labels
        label_encoder = LabelEncoder()
        y_train_enc = label_encoder.fit_transform(y_train)
        y_test_enc = label_encoder.transform(y_test)

        # Reshape input for CNN
        x_test_reshaped = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))
        dataset_timesteps = x_test_reshaped.shape[1]
        dataset_channels = x_test_reshaped.shape[2]
        dataset_num_classes = len(np.unique(y_train_enc))

        for model_file in os.listdir(directory_model):
            if model_file.endswith(".keras") or model_file.endswith(".h5"):
                print("Loading model: " + model_file)
                try:
                    model_cnn = load_model(os.path.join(directory_model, model_file))
                    # Force recompile (important!)
                    model_cnn.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
                except Exception as e:
                    print(f"Could not load/compile model {model_file}: {e}")
                    continue

                # Inspect model shapes
                try:
                    model_input_shape = model_cnn.input_shape
                    expected_timesteps = model_input_shape[1]
                    expected_channels = model_input_shape[2] if len(model_input_shape) > 2 else 1
                    model_num_classes = model_cnn.output_shape[-1]
                except Exception as e:
                    print(f"Could not inspect model {model_file}: {e}. Skipping.")
                    continue

                # Compatibility checks
                if expected_timesteps != dataset_timesteps:
                    print(f"Skipping model {model_file}: expected timesteps {expected_timesteps}, dataset has {dataset_timesteps}.")
                    continue
                if expected_channels != dataset_channels:
                    print(f"Skipping model {model_file}: expected channels {expected_channels}, dataset has {dataset_channels}.")
                    continue
                if model_num_classes != dataset_num_classes:
                    print(f"Skipping model {model_file}: expected {model_num_classes} classes, dataset has {dataset_num_classes}.")
                    continue

                # Predictions
                y_test_pred_probs = model_cnn.predict(x_test_reshaped, batch_size=1024, verbose=0)
                y_test_pred = np.argmax(y_test_pred_probs, axis=1)

                # Accuracy (sklearn)
                accuracy = accuracy_score(y_test_enc, y_test_pred)
                print(f"SKLearn Accuracy for model {model_file} on dataset {file}: {accuracy:.4f}")

                # TensorFlow evaluate (only if shapes align)
                y_test_cat = to_categorical(y_test_enc, num_classes=model_num_classes)
                if y_test_cat.shape[1] == model_num_classes:
                    loss, acc = model_cnn.evaluate(x_test_reshaped, y_test_cat, verbose=0)
                    print(f"TF evaluate -> loss: {loss:.4f}, acc: {acc:.4f}")
                else:
                    print(f"Skipping TF evaluate: y_test_cat {y_test_cat.shape}, model expects {model_num_classes} classes")
