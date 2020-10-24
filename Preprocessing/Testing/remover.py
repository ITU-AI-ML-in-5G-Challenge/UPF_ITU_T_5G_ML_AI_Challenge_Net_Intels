#This code is used to remove the first extra index column
import pandas as pd
import glob

pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Final_converted_test_data\\All_combined_proper\\'
for file in glob.glob(pathname+'*.csv'):
	df = pd.read_csv(file)
	# If you know the name of the column skip this
	first_column = df.columns[0]
	# Delete first
	df = df.drop([first_column], axis=1)
	df.to_csv(file, index=False)
