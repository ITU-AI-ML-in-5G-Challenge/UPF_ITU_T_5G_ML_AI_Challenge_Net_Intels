# This code is to combine all the CSV files in a given directory
import pandas as pd
import os
import glob

path = "C:\\Users\\venka\\Desktop\\5g_ITU\\Combined\\"
os.chdir(path)
results = pd.DataFrame()

for counter, current_file in enumerate(glob.glob("*.csv")):
    namedf = pd.read_csv(current_file, header=None, sep="|")
    print(namedf)
    results = pd.concat([results, namedf])

results.to_csv('Combined.csv', index=None, header=None, sep="|")
