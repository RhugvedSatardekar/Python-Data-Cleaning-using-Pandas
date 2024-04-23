
# Data Cleaning using Pandas

The following Python script demonstrates how to clean data using the pandas library in Python. This script performs various data cleaning operations on a dataset named "Customer Call List.xlsx".

### Steps:

1. **Importing Libraries**: First, import the pandas library to work with dataframes.

```python
import pandas as pd
```

2. **Loading Data**: Load the dataset into a pandas dataframe.

```python
df = pd.read_excel(r"C:\Users\Rhugved\Desktop\Python for DA\Customer Call List.xlsx")
```

3. **Removing Duplicates**: Remove duplicate rows from the dataframe.

```python
df = df.drop_duplicates()
```

4. **Removing Unnecessary Columns**: Drop columns that are not useful for analysis.

```python
df = df.drop(columns='Not_Useful_Column')
```

5. **Stripping Leading and Trailing Characters**: Clean the "Last_Name" column by removing leading and trailing characters.

```python
df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")
```

6. **Stripping Characters**: Clean the "Last_Name" column by stripping specific characters.

```python
df['Last_Name'] = df['Last_Name'].str.strip("123./_% ")
```

7. **Replacing Characters**: Replace specific characters in the "Phone_Number" column.

```python
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')
```

8. **Formatting Phone Numbers**: Format phone numbers to a consistent format.

```python
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)[0:3] + '-' + str(x)[3:6] + '-' + str(x)[6:10])
```

9. **Splitting Address**: Split the "Address" column into "Street_Address", "State", and "Zip" columns.

```python
df[["Street_Address","State","Zip"]] = df["Address"].str.split(',',2,expand = True)
```

10. **Standardizing Values**: Standardize values in the "Paying Customer" and "Do_Not_Contact" columns.

```python
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
```

11. **Filling Missing Values**: Fill missing values in the dataframe with empty strings.

```python
df = df.fillna('')
```

12. **Removing Rows**: Remove rows where "Do_Not_Contact" is 'Y' or where "Phone_Number" is empty.

```python
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y" or df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
```

13. **Resetting Index**: Reset the index of the dataframe.

```python
df.reset_index(drop=True, inplace=True)
```

The script provides a comprehensive example of how to clean and preprocess data using pandas, making it suitable for further analysis.


This README section provides a clear explanation of the data cleaning process using pandas, making it easier for users to understand and replicate the steps.
