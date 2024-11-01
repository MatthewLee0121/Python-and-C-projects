import pandas as pd


#%pwd return present working directory with jypter notebook
def printLine():
    print('----------------------------------------------------------------------------------------------------------')
    print("")
    print("")

s = pd.Series([1, 2, 3, 4]) #creates a series (1d data structure)

df = pd.DataFrame( #creates a dataFrame (2d data structure)
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
)

printLine()
print("S and df")
print(s)
print(df)
printLine()


data = { #csv example
    'Name': ['Alice', 'Bob', 'Charlie', 'Batuhan'],
    'Age': [25, 30, 35, 24],
    'City': ['New York', 'Paris', 'London', 'Newcastle']
}

datadf = pd.DataFrame(data) #creates a data frame from csv

printLine()
print("CSV data to Data Frame")
print(datadf)
printLine()
print("--------------------datadf.head()-----------------------------")
print(datadf.head()) #First 5 row
print("--------------------datadf.tail()-----------------------------")
print(datadf.tail()) # last 5 rows
print("--------------------datadf.info()-----------------------------")
print(datadf.info()) #summary of dataframe
print("--------------------datadf.describe()-------------------------")
print(datadf.describe()) #statistical summary
printLine()
print("--------------------datadf['Name'] (select 1 column)-------------------------")
print(datadf['Name'])
print("--------------------datadf['Name'] (select multiple column)-------------------------")
print(datadf[['Name', 'Age']]) #note double square
print("--------------------datadf.iloc[0] (select row via iloc index)-------------------------")
print(datadf.iloc[0]) #index row 0 
print("--------------------datadf.loc[0] (select row via  label index)-------------------------")
print(datadf.loc[1]) #index row 1 if labeled
print("--------------------df.columns (get column name)-------------------------")
print(datadf.columns)
print("--------------------filtereddata = datadf[datadf['Age'] > 30] (filter via criteria)-------------------------")
filtereddata = datadf[datadf['Age'] > 30]
print(filtereddata)
print("--------------------filtereddata = datadf[datadf['Age'] > 30] (filter via criteria)-------------------------")
filtereddata2 = datadf[datadf['City'] == 'Newcastle']
print(filtereddata2)
print("--------------------prints datadf add salery column add 1 to age then print again to see change-------------------------")
print(datadf)
datadf['Salary'] = [50000, 60000, 70000, 0]
datadf['Age'] = datadf['Age'] + 1
print(datadf)

