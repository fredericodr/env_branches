import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path)
    return df

def make_scatter(var1, var2):
    plt.scatter(var1, var2)
    plt.show()
    return None

print("nice! we were able to run this script, that doesnt do much!")