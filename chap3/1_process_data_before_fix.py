# wrong way to import packages
#import pandas, numpy
# right way to import packages

import pandas as pd
import numpy as np

# constant variables should be defined in upper case
#num_states = 50
NUM_STATES = 50

# def PROCESSDATA(file_name, int): function should be defined in lower case
# don't use builtin function or keyword as varialble name


def process_data(file_name, num_samples):
    # global variables should be avoided
    #global df
    df = pd.read_csv(file_name)

    df = df.fillna(df.median())

    # avoid compound statements
    #if int > 0: df = df.sample(int)
    if num_samples > 0:
        df = df.sample(num_samples)

    return df
