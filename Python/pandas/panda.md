What is Pandas : Pandas is a Python library used for working with data sets.

	           It has functions for analyzing, cleaning, exploring, and manipulating data.

	           The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Why Use Pandas?
		1.Pandas allows us to analyze big data and make conclusions based on statistical theories.

		2.Pandas can clean messy data sets, and make them readable and relevant.

		3. Relevant data is very important in data science.

Installation of Pandas :  C:\Users\Your Name>pip install pandas

Import Pandas:  Once Pandas is installed, import it in your applications by adding the "import" keyword:

	import pandas

Create an alias with the as keyword while importing: import pandas as pd
Now the Pandas package can be referred to as pd instead of pandas.

Checking Pandas Version: The version string is stored under __version__ attribute.

import pandas as pd

print(pd.__version__)

What is a Series? : A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

Labels: If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.This label can be used to access a specified
 value.

What is a DataFrame? : A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
	import pandas as pd

	data = {
  	"calories": [420, 380, 390],
 	 "duration": [50, 40, 45]
		}

	#load data into a DataFrame object:
	df = pd.DataFrame(data)

	print(df) 

Locate Row:  As you can see from the result above, the DataFrame is like a table with rows and columns.Pandas use the loc attribute to return one or more specified row(s).

Locate Named Indexes: Use the named index in the loc attribute to return the specified row(s).
	#refer to the named index:
	print(df.loc["day2"])

Load Files Into a DataFrame: If your data sets are stored in a file, Pandas can load them into a DataFrame.
	import pandas as pd

	df = pd.read_csv('data.csv')

	print(df) 

Viewing the Data: One of the most used method for getting a quick overview of the DataFrame, is the head() method.
	            The head() method returns the headers and a specified number of rows, starting from the top.

     	            import pandas as pd

	            df = pd.read_csv('data.csv')

                            print(df.head(10))

Info About the Data:  The DataFrames object has a method called info(), that gives you more information about the data set.
		print(df.info())

A great aspect of the Pandas module is the corr() method.

The corr() method calculates the relationship between each column in your data set.
df.corr()





