#Detecting null values
import pandas as pd
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, 6, 7, 8]})
print(df.isnull())

#dropping null values
df.dropna()  # drop rows with null values
df.dropna(axis=1)  # drop columns with null values
df.dropna(thresh=2)  # drop rows with at least 2 null values

#filling null values
df.fillna(0)  # fill null values with 0
df.fillna('Unknown')  # fill null values with 'Unknown'

#interpolating null values
df['A'].interpolate()  # interpolate null values in column A

#replacing null values with a specific value
df.replace({np.nan: 0})  # replace null values with 0

#Handling null values in groupby operations
df.groupby('A', dropna=False).sum()  # include null values in groupby operation

#Handling null values in merging and joining
df1.merge(df2, how='outer', indicator=True)  # include null values in merge

