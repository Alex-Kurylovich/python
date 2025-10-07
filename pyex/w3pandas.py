import pandas as pd

def series():
    print("Series")
    a = [1, 7, 2]
    myvar = pd.Series(a, index=["x", "y", "z"])
    print(myvar)
    print(myvar["y"])
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories)
    print(myvar)
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories, index=["day1", "day2"])
    print(myvar)

def data_frames():
    print("DataFrames")

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


