import pandas as pd  # If there's no error, Pandas is installed
print("Pandas is installed.")
print("Pandas version:", pd.__version__)

#PANDAS SERIES 
#from lists
import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

#From a NumPy Array
import pandas as pd
import numpy as np

data = np.array([1, 2, 3, 4, 5])
series = pd.Series(data)
print(series)

#From a Dictionary
import pandas as pd

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series = pd.Series(data)
print(series)

#Common Attributes
import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
print(df.index)  

#columns
print(df.columns)  
#values
print(df.values)
#shape
print(df.shape)
#dtypes
print(df.dtypes)

#common methods
#head()
print(df.head(2))  
#tail()
print(df.tail(2))
#info()
print(df.info())
#describe()
print(df.describe())
#loc[] and iloc[]
print(df.loc[0])
print(df.iloc[0])
#sort values()
print(df.sort_values(by='Age'))
#goupby()
print(df.groupby('Age').count())
