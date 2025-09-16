
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# from imblearn.under_sampling import TomekLinks
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
# from imblearn.over_sampling import SMOTE
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

def low_variance(data, threshold = 0.05):
    variance = VarianceThreshold(threshold=threshold)
    return variance.fit_transform(data)

def encoder(data):
    _encoder = LabelEncoder()
    return _encoder.fit_transform(data)


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
    "./dataset/",
]

for directory in directories:
    print("loading files from: " + directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print("Loading file: " + filename)
            data_temp = pd.read_csv(
                directory + filename,
            )
            data = pd.concat([data, data_temp], ignore_index=True)

# endregion

# region separating data

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - separating data x/y")

for column in data.columns:
    print(column)
    print(f'{data.loc[data[column] == "?"]}\n\n')
exit(0)

x_data = data.iloc[:, 0:49].values
y_data = data.iloc[:, 49].values

# endregion

# region formating data

columns = [
    2,
    3,
    4,
    5,
    10,
    11,
    18,
    19,
    20,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
]

for column in columns:
    x_data[:, column] = encoder(x_data[:, column])

x_data = standard_scaler(x_data)

# endregion

# region select data

x_data_variance = low_variance(x_data)
# print(f"x_data: {x_data}")
print(f"x_data: {x_data.shape}")
# print(f"x_data_variance: {x_data_variance}")
print(f"x_data_variance: {x_data_variance.shape}")


# endregion

# region smote + standard scaler

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - splitting data with smote + standard scaler all data")
x_data, y_data_temp = smote_oversampling(x_data, y_data)
(
    x_data_trinamento,
    x_data_teste,
    y_data_treinamento,
    y_data_teste,
) = train_test_split(x_data, y_data_temp)

time = datetime.datetime.now().strftime("%H:%M:%S")
print(time + " - saving pkl with no pre processing")
save_pickle(
    [x_data_trinamento, y_data_treinamento, x_data_teste, y_data_teste],
    "./pkl/standard_smote.pkl",
)

# endregion


print("###################")
print("#                 #")
print("#      DONE       #")
print("#                 #")
print("###################")
