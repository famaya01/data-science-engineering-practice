"""
 Practice on your own
In this section, spend some time practicing the contents of this chapter on your own.

- Suppose you have a function called create_plots, taking a pandas data frame, a plot type (specified by an integer), 
  and a color (such as red, orange, yellow). The output is a list. How could you specify the input data types when defining 
  this function? See this reference: https://www.w3schools.com/python/python_datatypes.asp for a list of common data types in Python.
- Now, add logic to your function so that if an incorrect data type is entered, the function will raise an error before
  attempting any code execution.
- Look up one of the free APIs here: https://github.com/public-apis/public-apis, and use one of them in a loop to collect data.
   Then, add try/except to your code to handle any error that may occur. For example, similar to our stock tickers example earlier, 
   you can test what happens you have invalid inputs and how to handle them using the examples in this chapter as a reference.
- Can you refactor the following code snippet to follow standards similar to those covered in this chapter?

import sklearn, os, math

INDEX = 5
for i in range(10):
    INDEX += i


INDEX = math.log(INDEX)


"""
import pandas as pd

def create_plots(df: pd.DataFrame, plot_type: int, color: str) -> list:

    """
    Inputs: df: pd.Dataframe, plot_type: int, color: str
    takes as input a data frame, plot type and a color and return a list 
    """
    # check input data type
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data frame must be a pandas DataFrame")
    
    if not isinstance(plot_type, int):
        raise TypeError("Plot type must be an integer")
    
    if not isinstance(color, str):
        raise TypeError("Color must be a string")
    
    # Function logic goes here
    plots = []
    # Code to create plots based on plot_type and color
    # ...
    pass


########################################################
import requests


"""
The https://randomuser.me/api/ endpoint generates a new random user profile each time a request is made. 
"""

# Number of users to fetch
num_users = 5

# Initialize dictionaries to store results and failures
all_data = {}
failures = []

# Loop to fetch data for multiple users
for i in range(num_users):
    try:
        # Send the GET request to the API
        response = requests.get("https://randomuser.me/api/")
        print(response.text)
        
        # Raise an HTTPError for bad responses 
        response.raise_for_status()
        
        # Parse the JSON response
        user_data = response.json()
        
        # Store the user data in the dictionary
        all_data[i] = user_data
        print(f"User {i+1} data downloaded SUCCESSFULLY")
    except requests.exceptions.HTTPError as http_err:
        failures.append(i)
        print(f"User {i+1} data download FAILED with HTTP error: {http_err}")
    except Exception as err:
        failures.append(i)
        print(f"User {i+1} data download FAILED with error: {err}")

# Print the results
print("\nSuccessful data collection:")
for i, data in all_data.items():
    print(f"User {i+1}: {data}")

print("\nFailed data collection:")
for i in failures:
    print(f"User {i+1}")
#################################################################################
# import packages in separate lines
import sklearn
import os
import math

index = 5
for i in range(10):
    index += i


new_index = math.log(index)