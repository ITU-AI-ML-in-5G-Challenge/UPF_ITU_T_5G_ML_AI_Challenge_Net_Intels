import csv
import os
import pandas as pd
import glob
import natsort
import pandas as pd
import glob
import re

pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Test\\'
for f1,f2,f3 in zip(glob.glob(pathname+'rssi_*new.csv'),glob.glob(pathname+'input_*.csv'),glob.glob(pathname+'sinr_*new.csv')):
	df1=pd.read_csv(f1)
	df2=pd.read_csv(f2)
	file_name_2=re.sub('.csv','',f2)
	t_file_1=f1
	t_file_2=f3
	with open(t_file_1) as f:
		t_list_1=[]
		for line in f:
            #print(line)
			t_list_1.append((line))
		t_list_1.pop(0)
	print(t_list_1)
	with open(t_file_2) as f:
		t_list_2=[]
		for line in f:
            #print(line)
			t_list_2.append((line))
		t_list_2.pop(0)
	print(t_list_2)

	df=pd.read_csv(f2)
	df['RSSI']=t_list_1
	df['SINR']=t_list_2
	df.to_csv(file_name_2+'new.csv',index=False)
