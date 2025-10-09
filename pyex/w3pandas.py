import pandas as pd

def series():
    print("Series")
    print("Create a simple Pandas Series from a list")
    a = [1, 7, 2]
    myvar = pd.Series(a, index=["x", "y", "z"])
    print(myvar)
    print("Return the first value of the Series")
    print(myvar["y"])
    print("Create your own labels")
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories)
    print(myvar)
    print("Create a Series using only data from day1 and day2")
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories, index=["day1", "day2"])
    print(myvar)
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

def read_json():
    print("Read JSON")
    df = pd.read_json('data.json')
    print(df.to_string())

def analyzing_data():
    print("Analyzing Data")

def cleaning_data():
    print("Cleaning Data")

def cleaning_empty_cells():
    print("Cleaning Empty Cells")

def cleaning_wrong_format():
    print("Cleaning Wrong Format")

def cleaning_wrong_data():
    print("Cleaning Wrong Data")

def removing_duplicates():
    print("Removing Duplicates")

def correlations():
    print("Pandas Correlations")

def plotting():
    print("Pandas Plotting")

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


