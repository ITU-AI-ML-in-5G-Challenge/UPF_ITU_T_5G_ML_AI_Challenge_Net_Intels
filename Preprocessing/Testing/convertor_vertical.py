# This code is used to tranpose from rows to columns
import pandas as pd
import glob
import re

pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Test\\test_2\\'
for file in glob.glob(pathname+'rssi_*.csv'):
	df=pd.read_csv(file)
	file_name=re.sub('.csv','',file)
	df2=df.transpose()
	df2.to_csv(file_name+'new.csv')

for file in glob.glob(pathname+'sinr_*.csv'):
	df=pd.read_csv(file)
	file_name=re.sub('.csv','',file)
	df2=df.transpose()
	df2.to_csv(file_name+'new.csv')
