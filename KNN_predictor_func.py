import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import re
import glob
import math
from sklearn.metrics import mean_squared_error,mean_absolute_error

df=pd.read_csv('Combined_rssi_corrected_proper_sinr_row_fixed.csv')
df2=df.loc[df['node_type']==1]
del df2['node_type']
X= df2.iloc[:, :-1].values
y = df2.iloc[:, 7].values
sc = StandardScaler()
X = sc.fit_transform(X)
reg = KNeighborsRegressor(n_neighbors=10)
reg.fit(X, y) # Training done here
pred_regr_tr=reg.predict(X)
mse_regr = math.sqrt(mean_squared_error(y,pred_regr_tr))
mae_regr = (mean_absolute_error(y,pred_regr_tr))
print("Root Mean Squared error for training is ",mse_regr)
print("Mean Absolute error for training is ",mae_regr)



def predictor(filename):
	file=re.sub('.csv', '', filename)
	data=pd.read_csv(filename)# The file needed to be predicted
	AP_list_index=(data.loc[data['node_type']==0].index.values)
	AP_list=AP_list_index.tolist()
	data_2= data.loc[data['node_type']==1]
	index_list=data_2.index.values.tolist()
	data_3= data_2
	data_pred=data_2
	del data_pred['node_type']
	X_test=data_pred.values
	X_test=sc.fit_transform(X_test)
	pred_reg=reg.predict(X_test)
	pred_reg_list=pred_reg.tolist()
	predicted_dict={'Index':index_list,'Throughput':pred_reg_list}
	predicted_output=pd.DataFrame(predicted_dict)
	predicted_output=predicted_output.set_index('Index')
	pred_changer=predicted_output
	for i in AP_list:
	    line = pd.DataFrame({"Throughput": 1.3}, index=[i])
	    pred_changer = pred_changer.append(line, ignore_index=False)
	    pred_changer= pred_changer.sort_index()
	line = pd.DataFrame({"Throughput": 1.3}, index=[len(pred_changer.index)+1])
	pred_changer = pred_changer.append(line, ignore_index=True)
	AP_list_index_new=(pred_changer.loc[pred_changer['Throughput']==1.3].index.values)
	AP_list_new=AP_list_index_new.tolist()
	rng_list=[]
	for i in range(len(AP_list_new)):
	    rng_list.append([AP_list_new[i-1],AP_list_new[i]])
	del rng_list[0]
	rng_values_list=[]
	for i in rng_list:
	    rng_values_list.append(list(range(i[0],i[1],1)))
	for i in rng_values_list:
	    del i[0]
	respective_throughput_values=[]
	for i in rng_values_list:
	    #print(type(pred_changer['Throughput'].iloc[i].values))
	    respective_throughput_values.append(pred_changer['Throughput'].iloc[i].values)
	AP_throughput_value=[]
	for i in respective_throughput_values:
	    AP_throughput_value.append(np.sum(i))
	final_pred_df=pred_changer.loc[pred_changer['Throughput']!=1.3]
	for i,j in zip(AP_list,AP_throughput_value):
	    line = pd.DataFrame({"Throughput":j}, index=[i])
	    final_pred_df = final_pred_df.append(line, ignore_index=False)
	    
	final_pred_df= final_pred_df.sort_index()
	final_pred_df_transpose=final_pred_df.T
	final_pred_df_transpose.to_csv(file+'_KNN_throughput.csv',index=False,header=False)#Change the name of the file here to suit the output

pathname='C:\\Users\\venka\\Desktop\\5g_ITU\\Final_test_convertor\\Final_converted_test_data\\KNNFinal\\'

for f in glob.glob(pathname+'*new.csv'):
	predictor(f)
