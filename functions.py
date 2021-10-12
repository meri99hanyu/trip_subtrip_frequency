import numpy as np


def get_start_end(data, column):
    data["StartCity"] = np.NaN
    data["EndCity"] = np.NaN
    for i in range(len(data)):
        l = len(data[column][i][2:-2].split("', '"))
        data["StartCity"].loc[i] = data[column][i][2:-2].split("', '")[0]
        data["EndCity"].loc[i] = data[column][i][2:-2].split("', '")[l - 1]
    return data


def count_frequency(data, column):
    for i in range(len(data["DeviceId"])):
        for j in range(i + 1, len(data["DeviceId"])):
            if data["StartCity"][i] == data["StartCity"][j] and data["EndCity"][i] == data["EndCity"][j]:
                data[column].loc[i] = data[column][i] + 1
                data[column].loc[j] = data[column][j] + 1
    return data
