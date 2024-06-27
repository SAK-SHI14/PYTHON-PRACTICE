#data frame creation 
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['john', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)
print(df)

# Create a DataFrame from a list of lists
data = [['John', 28, 'USA'],
        ['Anna', 24, 'UK'],
        ['Peter', 35, 'Australia'],
        ['Linda', 32, 'Germany']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Country'])
print(df)

# Create a DataFrame from a CSV file
df = pd.read_csv('data.csv')
print(df)

#data inspection
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Get the first few rows of the DataFrame
print(df.head())

# Get the last few rows of the DataFrame
print(df.tail())

# Get the index of the DataFrame
print(df.index)

# Get the columns of the DataFrame
print(df.columns)

# Get the data types of the columns
print(df.dtypes)

# Get a summary of the DataFrame
print(df.info())

# Get a concise summary of the DataFrame
print(df.describe())

#data exploration 
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Get the unique values in a column
print(df['Country'].unique())

# Get the count of unique values in a column
print(df['Country'].nunique())

# Get the value counts of a column
print(df['Country'].value_counts())

# Get the missing values in the DataFrame
print(df.isnull().sum())

# Get the correlation between columns
print(df.corr())

# Get the covariance between columns
print(df.cov())

# Group the DataFrame by a column and perform aggregation
print(df.groupby('Country')['Age'].mean())

# Sort the DataFrame by a column
print(df.sort_values('Age'))

# Filter the DataFrame based on a condition
print(df[df['Age'] > 30])
