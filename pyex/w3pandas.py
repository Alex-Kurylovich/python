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
    print(df.to_string())
    print()

def analyzing_data():
    print("Analyzing Data")
    print("Get a quick overview by printing the first 10 rows of the DataFrame")
    df = pd.read_csv('data.csv')
    print(df.head(10))
    print("Print the last 5 rows of the DataFrame")
    print(df.tail())
    print("Print information about the data")
    print(df.info())
    print()

def cleaning_data():
    print("Cleaning Data")
    print("Return a new Data Frame with no empty cells")
    df = pd.read_csv('data.csv')
    print(df.dropna())
    print("Return a new Data Frame with empty cells")
    print(df[df.isnull().any(axis=1)])
    print("Replace NULL values with the number 130")
    print(df.fillna({"Calories": 130}, inplace=True))
    print(df)
    print("Calculate the MEAN, and replace any empty values with it")
    df = pd.read_csv('data.csv')
    cal = df["Calories"].mean()
    print(cal)
    print(df.fillna({"Calories": cal}, inplace=True))
    print(df)
    print("Calculate the MODE, and replace any empty values with it")
    df = pd.read_csv('data.csv')
    mode = df["Calories"].mode()[0]
    print(mode)
    print(df.fillna({"Calories": mode}, inplace=True))
    print(df)

    print()

def cleaning_empty_cells():
    print("Cleaning Empty Cells")
    print()

def cleaning_wrong_format():
    print("Cleaning Wrong Format")
    print()

def cleaning_wrong_data():
    print("Cleaning Wrong Data")
    print()

def removing_duplicates():
    print("Removing Duplicates")
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

# Quiz/Exercises
# Pandas Editor
# Pandas Quiz
# Pandas Exercises
# Pandas Syllabus
# Pandas Study Plan
# Pandas Certificate
# DataFrames Reference

if __name__ == '__main__':
    series()
    data_frames()
    read_csv()
    read_json()
    analyzing_data()
    cleaning_data()
    cleaning_empty_cells()
    cleaning_wrong_format()
    cleaning_wrong_data()
    removing_duplicates()
    correlations()
    plotting()

# pd.options.display.max_rows = 200
# df = pd.read_csv('data.csv')
# print(pd.options.display.max_rows)
# print(df.loc[[0, 1]])
# print(df, end='\n\n')


