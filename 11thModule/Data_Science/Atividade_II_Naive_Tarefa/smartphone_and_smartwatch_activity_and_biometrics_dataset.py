from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import TomekLinks
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pickle
import datetime
import os

""" 
Variable reminders

- x_data: Original feature set
- y_data: labels

- x_data_tomek: Feature set after Tomek Links undersampling
- y_data_tomek: Labels after Tomek Links undersampling

- x_data_smote: Feature set after SMOTE oversampling
- y_data_smote: Labels after SMOTE oversampling

- x_data_standard: Feature set after standard scaling
- x_data_minmax: Feature set after min-max scaling

"""

# region functions


def standard_scaler(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)


def minmax_scaler(data):
    scaler = MinMaxScaler()
    return scaler.fit_transform(data)


def train_test_split_(x_data, y_data, test_size=0.2, random_state=0):
    return train_test_split(
        x_data, y_data, test_size=test_size, random_state=random_state
    )


def tomek_links_undersampling(x_data, y_data):
    tl = TomekLinks()
    return tl.fit_resample(x_data, y_data)


def smote_oversampling(x_data, y_data):
    smote = SMOTE()
    return smote.fit_resample(x_data, y_data)


def save_pickle(obj, filename):
    with open(filename, mode="wb") as f:
        pickle.dump(obj, f)
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{time} - {filename} saved")


# endregion

# region getting data

data = pd.DataFrame()
directories = [
    "./dataset/phone/accel/",
    "./dataset/phone/gyro/",
    "./dataset/watch/accel/",
    "./dataset/watch/gyro/",
]

for directory in directories:
    print("loading files from: " + directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            print("Loading file: " + filename)
            data_temp = pd.read_csv(
                directory + filename,
                header=None,
            )
            data = pd.concat([data, data_temp], ignore_index=True)

# endregion

# region formating data

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - formating data")

data.columns = ["subject-id", "activity", "timestamp", "x", "y", "z"]
data["activity"] = data.pop("activity")

og_labels = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "O",
    "P",
    "Q",
    "R",
    "S",
]
corret_labels = [
    "Walking",
    "Jogging",
    "Stairs",
    "Sitting",
    "Standing",
    "Typing",
    "Brushing Teeth",
    "Eating Soup",
    "Eating Chips",
    "Eating Pasta",
    "Drinking from Cup",
    "Eating Sandwich",
    "Kicking (Soccer Ball)",
    "Playing Catch w/Tennis Ball",
    "Dribblinlg (Basketball)",
    "Writing",
    "Clapping",
    "Folding Clothes",
]

for i in range(len(og_labels)):
    data["activity"] = data["activity"].str.replace(og_labels[i], corret_labels[i])

data["z"] = data["z"].str.replace(";", "", regex=False).astype(float)

# endregion

# region separating data

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - separating data x/y")

x_data = data.iloc[:, 0:5].values
y_data = data.iloc[:, 5].values

# endregion

# region full data

# region no processing at all
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with no pre processing")
x_data_trinamento, x_data_teste, y_data_treinamento, y_data_teste = train_test_split_(
    x_data, y_data
)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with no pre processing")
save_pickle(
    [x_data_trinamento, y_data_treinamento, x_data_teste, y_data_teste],
    "./pkl/Dataset_raw.pkl",
)
# endregion

# region standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with standard scaler all data")
x_data_temp = standard_scaler(x_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento,
        y_data_teste_temp,
        y_data_teste,
    ],
    "./pkl/Dataset_standard.pkl",
)

# endregion

# region MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with MinMax scaler all data")
x_data_temp = minmax_scaler(x_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento,
        y_data_teste_temp,
        y_data_teste,
    ],
    "./pkl/Dataset_minmax.pkl",
)

# endregion

# region tomek
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek undersampling all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split_(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek undersampling all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_tomek.pkl",
)

# endregion

# region tomek + standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek + standard scaler all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
x_data_temp = standard_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek + standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_standard_tomek.pkl",
)

# endregion

# region tomek + MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek + MinMax scaler all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
x_data_temp = minmax_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek + MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_minmax_tomek.pkl",
)

# endregion

# region smote
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote oversampling all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split_(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote oversampling all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_smote.pkl",
)

# endregion

# region smote + standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote + standard scaler all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
x_data_temp = standard_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote + standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_standard_smote.pkl",
)

# endregion

# region smote + MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote + MinMax scaler all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
x_data_temp = minmax_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote + MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_minmax_smote.pkl",
)

# endregion

# endregion

# region without subject-id

data = data.drop(["subject-id"], axis=1)

x_data = data.iloc[:, 0:4].values
y_data = data.iloc[:, 4].values


# region no processing at all
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with no pre processing")
x_data_trinamento, x_data_teste, y_data_treinamento, y_data_teste = train_test_split_(
    x_data, y_data
)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with no pre processing")
save_pickle(
    [x_data_trinamento, y_data_treinamento, x_data_teste, y_data_teste],
    "./pkl/Dataset_raw_no_subject-id.pkl",
)
# endregion

# region standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with standard scaler all data")
x_data_temp = standard_scaler(x_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento,
        y_data_teste_temp,
        y_data_teste,
    ],
    "./pkl/Dataset_standard_no_subject-id.pkl",
)

# endregion

# region MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with MinMax scaler all data")
x_data_temp = minmax_scaler(x_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento,
        y_data_teste_temp,
        y_data_teste,
    ],
    "./pkl/Dataset_minmax_no_subject-id.pkl",
)

# endregion

# region tomek
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek undersampling all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split_(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek undersampling all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_tomek_no_subject-id.pkl",
)

# endregion

# region tomek + standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek + standard scaler all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
x_data_temp = standard_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek + standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_standard_tomek_no_subject-id.pkl",
)

# endregion

# region tomek + MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with tomek + MinMax scaler all data")
x_data_temp, y_data_temp = tomek_links_undersampling(x_data, y_data)
x_data_temp = minmax_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with tomek + MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_minmax_tomek_no_subject-id.pkl",
)

# endregion

# region smote
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote oversampling all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split_(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote oversampling all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_smote_no_subject-id.pkl",
)

# endregion

# region smote + standard scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote + standard scaler all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
x_data_temp = standard_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote + standard scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_standard_smote_no_subject-id.pkl",
)

# endregion

# region smote + MinMax scaler
time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote + MinMax scaler all data")
x_data_temp, y_data_temp = smote_oversampling(x_data, y_data)
x_data_temp = minmax_scaler(x_data_temp)
(
    x_data_treinamento_temp,
    x_data_teste_temp,
    y_data_treinamento_temp,
    y_data_teste_temp,
) = train_test_split(x_data_temp, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with smote + MinMax scaler all data")
save_pickle(
    [
        x_data_treinamento_temp,
        y_data_treinamento_temp,
        x_data_teste_temp,
        y_data_teste_temp,
    ],
    "./pkl/Dataset_minmax_smote_no_subject-id.pkl",
)

# endregion

# endregion


print("###################")
print("#                 #")
print("#      DONE       #")
print("#                 #")
print("###################")
