# Program to remove extra index in converted csv files
import pandas as pd
import glob

pathname=''# Path to converted files
for file in glob.glob(pathname+'*.csv'):
	df = pd.read_csv(file)
	first_column = df.columns[0]
	df = df.drop([first_column], axis=1)
	df.to_csv(file, index=False)
