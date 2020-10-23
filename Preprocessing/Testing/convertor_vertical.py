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

'''
for f1,f2 in zip(glob.glob(pathname+'rssi_*new.csv'),(pathname+'input_*.csv')):
	df1=pd.read_csv(f1)
	df2=pd.read_csv(f2)
	file_name_2=re.sub('.csv','',f2)
	df3=pd.concat(df1,df2)
	df3.to_csv(file_name_2+'new.csv')'''