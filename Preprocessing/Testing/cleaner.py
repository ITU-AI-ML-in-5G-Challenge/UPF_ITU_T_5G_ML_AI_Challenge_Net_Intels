#This code is remove all the columns except the required features
import pandas as pd
import glob
import re

pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Final_converted_test_data\\All_combined_proper_clean_final\\'
for file in glob.glob(pathname+'*.csv'):
	df=pd.read_csv(file)
	file_name=re.sub('.csv','',file)
	columns=['node_type','x(m)','y(m)','primary_channel','min_channel_allowed','max_channel_allowed','0','0.1']
	df2=df[columns]
	df2.to_csv(file_name+'.csv',index=False)
