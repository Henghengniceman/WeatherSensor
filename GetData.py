# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:18:40 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import requests
import json
import time
from datetime import datetime
import numpy as np
import pandas as pd 
import os 
DataOut = []
DateTimes = [datetime.now()]
Count = 0 

while True:
    try:
        Channelr =requests.get('http://141.52.172.253/websites/ab/index.php/json/api/getchannels',timeout = 5)
        success = json.loads(Channelr.text)
        Channels=json.loads(Channelr.text)['channels']
        VariableNames = []
        valueids = ''
        for channel in Channels:
            if channel['app'] == 'wsserial':
                VariableNames.append(channel['measurementname'] +'('+channel['unitname'] +')')
                valueids = valueids + channel['valueid']+','
        valueids = valueids[:-1]
        
        Valuesr =requests.get('http://141.52.172.253/websites/ab/index.php/json/api/getvalues?valueids='+valueids,timeout = 5)
        Values=json.loads(Valuesr.text)['values']
        SenOut = [] 
        for values in Values:
            SenOut.append(values['value'])
        DateTimesingle =  datetime.strptime(Values[-1]['timestamp'], '%Y-%m-%d %H:%M:%S')
        if not DateTimesingle == DateTimes[-1]:
            DateTimes.append(DateTimesingle)
            DataOut.append(SenOut)
            Count = Count + 1
            print('system is Running')
        if Count == 360:
            DataOut = np.array(DataOut)
            DateTimes = DateTimes[1:]
            Datadf = pd.DataFrame(data = DataOut,index = DateTimes,columns = VariableNames)
            Datadf.index.name = 'DateTime'
            if not os.path.exists('./Data/'):
                os.makedirs('./Data/') 
            SaveFileName = 'WS700_'+DateTimes[-1].strftime('%Y_%m_%d_%H_%M_%S')+'.txt'
            Datadf.to_csv('./Data/'+SaveFileName, sep='\t')
            print(str(len(DateTimes))+' recored has been save to file at'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            DataOut = []
            DateTimes = [datetime.now()]
            Count = 0 
    except requests.exceptions.RequestException as e:
        if len(DateTimes)>1:
            DataOut = np.array(DataOut)
            DateTimes = DateTimes[1:]
            Datadf = pd.DataFrame(data = DataOut,index = DateTimes,columns = VariableNames)
            Datadf.index.name = 'DateTime'
            if not os.path.exists('./Data/'):
                os.makedirs('./Data/') 
            SaveFileName = 'WS700_'+DateTimes[-1].strftime('%Y_%m_%d_%H_%M_%S')+'.txt'
            Datadf.to_csv('./Data/'+SaveFileName, sep='\t')
            print(str(len(DateTimes))+' recored has been save to file at'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            DataOut = []
            DateTimes = [datetime.now()]
            Count = 0 
        print('cannot connect to serve')

      # DateTimes = datetime.strptime(value., '')  

