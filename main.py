import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path)
    return df

def make_scatter(var1, var2):
    plt.scatter(var1, var2)
    plt.show()
    return None

def calculate_stuff(var):
    return "a lot of stuff"

def clean_stuff(df):
    return "clean df"

def more_stuff(df):
    return df
