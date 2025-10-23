import pandas as pd
import matplotlib.pyplot as plt

def series():
    print("Series")
    print("Create a simple Pandas Series from a list")
    a = [1, 7, 2]
    ser = pd.Series(a, index=["x", "y", "z"])
    print(ser)
    print("Return the first value of the Series")
    print(ser["y"])
    print("Create your own labels")
    calories = {"day1": 420, "day2": 380, "day3": 390}
    ser = pd.Series(calories)
    print(ser)
    print("Create a Series using only data from day1 and day2")
    calories = {"day1": 420, "day2": 380, "day3": 390}
    ser = pd.Series(calories, index=["day1", "day2"])
    print(ser)
    print()

def data_frames():
    print("DataFrames")
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    print("Load data into a DataFrame object")
    print('max_rows', str(pd.options.display.max_rows))
    pd.options.display.max_rows = 200
    df = pd.DataFrame(data)
    print(df)
    print("Refer to the row index")
    print(df.loc[0])
    print("Use a list of indexes")
    print(df.loc[[0, 1]])
    print("Add a list of names to give each row a name")
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    df = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(df)
    print("Use the named index in the loc attribute to return the specified row(s)")
    print(df.loc["day2"])
    print()

def read_csv():
    print("Read CSV")
    df = pd.read_csv('data.csv')
    print(df.info())
    print()

def read_json():
    print("Read JSON")
    df = pd.read_json('data.json')
    print(df.head())
    print()

def analyzing_data():
    print("Analyzing Data")
    df = pd.read_csv('data.csv')
    print("Get a quick overview by printing the first 5 rows of the DataFrame")
    print(df.head())
    print("Print the last 5 rows of the DataFrame")
    print(df.tail())
    print("Print information about the data")
    print(df.info())
    print()

def cleaning_data():
    print("Cleaning Data")
    df = pd.read_csv('data.csv')
    print("Return a new Data Frame with empty cells")
    filtered_df_is_null = df[df['Calories'].isnull()]
    print(filtered_df_is_null)
    print("Replace NULL values with the number 130")
    df = pd.read_csv('data.csv')
    filtered_df_is_130 = filtered_df_is_null.fillna(130)
    print(filtered_df_is_130)
    print("Calculate the MEAN, and replace any empty values with it")
    df = pd.read_csv('data.csv')
    mean = df["Calories"].mean()
    print(mean)
    filtered_df_is_mean = filtered_df_is_null.fillna(mean)
    print(filtered_df_is_mean)
    print("Calculate the MODE, and replace any empty values with it")
    df = pd.read_csv('data.csv')
    mode = df["Calories"].mode()
    print(mode)
    filtered_df_is_mode = filtered_df_is_null.fillna(mode.iloc[0])
    print(filtered_df_is_mode)
    print()

def cleaning_wrong_format():
    # The result from the converting in the example above gave us a NaT value,
    # which can be handled as a NULL value,
    # and we can remove the row by using the dropna() method.
    print("Cleaning Wrong Format")
    df = pd.read_csv('data_wrong.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    print(df.to_string())
    print()

def cleaning_wrong_data():
    print("Cleaning Wrong Data")
    df = pd.read_csv('data_wrong.csv')
    df.loc[7, 'Duration'] = 45
    print(df.to_string())

    print("Loop through all values in the Duration column")
    df = pd.read_csv('data_wrong.csv')
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120
    print(df.to_string())

    print("Delete rows where Duration is higher than 120")
    df = pd.read_csv('data_wrong.csv')
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.drop(x, inplace=True)
    # remember to include the 'inplace = True' argument to make the changes
    # in the original DataFrame object instead of returning a copy
    print(df.to_string())

    print()

def removing_duplicates():
    print("Removing Duplicates")
    print("Duplicate rows are rows that have been registered more than one time")
    df = pd.read_csv('data_wrong.csv')
    print(df.duplicated())
    # Removing Duplicates
    # Notice that row 12 has been removed from the result
    df = pd.read_csv('data_wrong.csv')
    df.drop_duplicates(inplace = True)
    print(df.to_string())
    print()

def correlations():
    print("Pandas Correlations")
    df = pd.read_csv('data.csv')
    print(df.corr())
    print()

def plotting():
    print("Pandas Plotting")
    df = pd.read_csv('data.csv')
    df.plot()
    plt.show()
    print()

if __name__ == '__main__':
    series()
    data_frames()
    read_csv()
    read_json()
    analyzing_data()
    cleaning_data()
    cleaning_wrong_format()
    cleaning_wrong_data()
    removing_duplicates()
    correlations()
    plotting()


