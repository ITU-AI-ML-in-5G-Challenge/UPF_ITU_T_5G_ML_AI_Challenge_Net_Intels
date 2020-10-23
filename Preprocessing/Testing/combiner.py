import pandas as pd
import glob
import re
import natsort


pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Test\\test_2\\'
for f1,f2,f3 in zip(natsort.natsorted(glob.glob(pathname+'rssi_*new.csv')),natsort.natsorted(glob.glob(pathname+'input_*.csv')),natsort.natsorted(glob.glob(pathname+'sinr_*new.csv'))):
	df1=pd.read_csv(f1)
	df2=pd.read_csv(f2)
	df3=pd.read_csv(f3)
	file_name_2=re.sub('.csv','',f2)
	df4=pd.concat([df2,df1],axis=1)
	df5=pd.concat([df4,df3],axis=1)
	df5.to_csv(file_name_2+'new.csv')