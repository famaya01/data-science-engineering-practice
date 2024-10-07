import pandas as pd
import time

#read dataset
artists = pd.read_csv("data/artists.csv")

#define the letters to search

letters = {'a', 'e', 'i', 'o', 'u'}

start = time.time()

#Mehtod 1: using a list
artists_names_list = list(artists["name"]) 
filtered_names_list = [name for name in artists_names_list if name.lower().startswith(letters)]
end = time.time()
print(f"list time: {end - start}")


#Mehtod 1: using a set
start = time.time()

artists_names_set = set(artists["name"]) 
filtered_names_list = [name for name in artists_names_list if name.lower().startswith(letters)]
end = time.time()
print(f"set time: {end - start}")