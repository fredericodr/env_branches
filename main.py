import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path)
    return df

<<<<<<< HEAD
def make_hbar(var1, var2):
    plt.hbar(var1, var2)
=======
def make_scatter(var1, var2):
    plt.scatter(var1, var2)
>>>>>>> new_features
    plt.show()
    return None

def calculate_stuff(var):
    return "a lot of stuff"

def clean_stuff(df):
    return "clean df"

def more_stuff(df):
    return df
