# %%
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
import re
import glob

# %%
data = pd.read_csv('Combined_rssi_corrected_proper_sinr_row_fixed.csv',delimiter=',')# The large CSV for the training location

df2=data.loc[data['node_type']==1]
del df2['node_type']
X = df2.iloc[:,:-1].values
y = df2.iloc[:,7].values


# %%
print(data)

# %%
print(df2)

# %%
from sklearn.preprocessing import StandardScaler

# %%
sc = StandardScaler()
X = sc.fit_transform(X)

# %%
from tensorflow.keras.layers import Input, Dense, Activation,Dropout
from tensorflow.keras.models import Model

# %%
input_layer = Input(shape=(X.shape[1],))
dense_layer_1 = Dense(1024, activation='relu')(input_layer)
dense_layer_2 = Dense(1024, activation='relu')(dense_layer_1)
dense_layer_3 = Dense(1024, activation='relu')(dense_layer_2)
dense_layer_4 = Dense(1024, activation='relu')(dense_layer_3)
dense_layer_5 = Dense(1024, activation='relu')(dense_layer_4)
dense_layer_6 = Dense(1024, activation='relu')(dense_layer_5)
dense_layer_7 = Dense(512, activation='relu')(dense_layer_6)

output = Dense(1)(dense_layer_7)

model = Model(inputs=input_layer, outputs=output)

model.compile(loss="mean_squared_error" , optimizer="adam", metrics=["mean_squared_error","mean_absolute_error"])

# %%
history = model.fit(X, y, batch_size=250, epochs=1000)

# %%
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import r2_score
from math import sqrt
pred_train = model.predict(X)

print(np.sqrt(mean_squared_error(y,pred_train)))#RMSE
print(mean_absolute_error(y,pred_train))#MAE
print(r2_score(y,pred_train))#R2_score
print(1-(1-r2_score(y, pred_train))*((len(X)-1)/(len(X)-len(X[0])-1)))#adjusted R2


print(pred_train)

from keras.models import load_model

#### The below code is used to save the model as HDF5 file so that this model can be used again and there will be no need to train all over again. ####
#model.save('Final_ANN_ITU_predictor_500_epochs.h5')  # creates a HDF5 file 'my_model.h5'
#del model  # deletes the existing model
#model = load_model('Final_ANN_ITU_predictor.h5')
#model = load_model('/content/drive/My Drive/ITU/Final/Final_ANN_ITU_predictor.h5')
################################################################################################################






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
  pred_model=model.predict(X_test)
  pred_model_list=pred_model.tolist()
  flat_list=[]
  for sublist in pred_model_list:
    for item in sublist:
      flat_list.append(item)
  #print(pred_model_list)
  pred_model_list= list(map(abs,flat_list))
  predicted_dict={'Index':index_list,'Throughput':pred_model_list}
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
  final_pred_df_transpose.to_csv(file+'_ANN_throughput.csv',index=False,header=False)#Change the name of the file here to suit the output

pathname=''#path to all the testing CSV files

for f in glob.glob(pathname+'*new.csv'):
	predictor(f)


