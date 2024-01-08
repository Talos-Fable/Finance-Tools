import pandas as pd
# read the first excel file
data1 = pd.read_csv("C:\\Users\\CAU Student\\Downloads\\QQQ Historical Data 2022.csv")

# read the second excel file
data2 = pd.read_csv("C:\\Users\\CAU Student\\Downloads\\QQQ Historical Data 2021.csv")

# define the columns to compare
col1 = "Change %"
col2 = "Change %"

# Iterate over the rows
for i in range(0, len(data1)):
    # compare the columns
    if data1.at[i, col1] > data2.at[i, col2]:
        result = "positive"
    elif data1.at[i, col1] < data2.at[i, col2]:
        result = "negative"
    else:
        result = "equal"
    # print the result
    print("Comparison between files on row {} is {}".format(i, result))




import pandas as pd

# read the first csv file
data1 = pd.read_csv("C:\\Users\\CAU Student\\Downloads\\QQQ Historical Data 2021.csv")

# read the second csv file
data2 = pd.read_csv("C:\\Users\\CAU Student\\Downloads\\QQQ Historical Data 2022.csv")

# define the column to compare
col = "Change %"

# iterate over the rows
for i in range(0, len(data1)):
    # compare the column
    if data1.at[i, col] > data2.at[i, col]:
        result = "positive"
    elif data1.at[i, col] < data2.at[i, col]:
        result = "negative"
    else:
        result = "equal"
    # print the result
    print("Comparison between files for value {} is {}".format(data1.at[i, col], result))