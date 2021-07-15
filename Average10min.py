# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:50:53 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import os 
import numpy as np
import pandas as pd
from tqdm import tqdm 
from datetime import datetime,timedelta
import matplotlib.pyplot as plt 
print(os.listdir('./RawData'))
#%% start from 13
# VariableName = ['Ta','Hr','Pa','Sa','Da','Ra','Ga'] 
SetColumns = [2,5,6,7,9,10,13] 
DateTimes  = []
Datas  = []
for filename in tqdm(os.listdir('./RawData')[12:]):
    if filename.startswith('WS700'):
       with open('./RawData/'+filename) as f:
           lines = f.readlines()
           VariableName = lines[0].split('\t')[2:14]
           #%% 2 T; 5 HR; 6 Pa;  7 Sa; 9 Da; 10 Ra; 13 Ga
           for i in range(1,len(lines)):
               Data  = lines[i].split('\t')
               
               if float(lines[i].split('\t')[1]) >-100:  # ignore error file 
                   DateTimes.append(datetime.strptime(lines[i].split('\t')[0],'%Y-%m-%d %H:%M:%S'))
                   DataOneLine = []
                   # for setcolumns in SetColumns:
                   #     DataOneLine.append(float(lines[i].split('\t')[setcolumns]))
                   for setcolumns in range(2,14):
                        DataOneLine.append(float(lines[i].split('\t')[setcolumns]))
                   DataOneLine = np.array(DataOneLine) 
                   Datas.append(DataOneLine)
               
Datas = np.array(Datas)           
dfData = pd.DataFrame(data=Datas,index=DateTimes,columns=VariableName) 
dfAverage =  dfData.resample("10T").mean()

dfAverage.to_excel('2021_10minAVG_meteo_Swabian05.xlsx')


# Dates = pd.date_range(start=DateTimes[0].strftime('%Y-%m-%d'),end=(DateTimes[-1]++timedelta(days=1)).strftime('%Y-%m-%d'), freq='10Min')

# dates = Dates.strftime('%Y-%m-%d %H:%M')
# dfData.between_time('2021-02-11 00:00', '2021-02-11 00:10')

# # dataMeans = []
# # dataStdS = [] 
# # for date in dates:
# #       dataMeans.append(dfData[date].mean().values)
# #       dataStdS.append(dfData[date].std().values)
# # dataMeans = np.array(dataMeans)
# # dataStdS = np.array(dataStdS)

# # dfDataMean=pd.DataFrame(data=dataMeans,index=dates,columns=VariableName)  # 1st row as the column names
# # dfDataStd = pd.DataFrame(data=dataStdS,index=dates,columns=VariableName)  # 1st row as the column names

# # writer = pd.ExcelWriter(('../DATA/DailyMean&std.xlsx'), engine='xlsxwriter')
# # dfDataMean.to_excel(writer, sheet_name='Mean')
# # dfDataStd.to_excel(writer, sheet_name='Std')
# # writer.save()

# # # aa =  dfData.resample('10Min')
# #            # VariableName =  lines[0].split('\t')
           
           
      
           