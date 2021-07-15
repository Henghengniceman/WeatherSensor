# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:25:57 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib as mpl
from datetime import datetime


MetroDataSet = pd.read_excel('2021_10minAVG_meteo_Swabian05.xlsx',index_col = 0)
DateTime = list(MetroDataSet.index)
Temperature = np.array(list(MetroDataSet['Ta (°C)']))
RelHum = np.array(list(MetroDataSet['Hr (%)']))

WindSpeed = np.array(list(MetroDataSet['Sa (m/s)']))
WindDirection = np.array(list(MetroDataSet['Da (°)']))
WindDirection = np.where(np.isnan(WindDirection),0,WindDirection)
scamap = plt.cm.ScalarMappable(cmap='jet')
fcolors = scamap.to_rgba(WindDirection)

Rain = np.array(list(MetroDataSet['Ra (mm)']))
RainPerHour = np.array(list(MetroDataSet['Ri (mm/h)']))

Radiation = np.array(list(MetroDataSet['Ga (W/m2)\n']))

fontdicts={'weight': 'bold', 'size': 10}

with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(5, 1, sharex=True,dpi=120, figsize=(16, 9))

    axes[0].plot(DateTime,Temperature,linewidth = 3,color='red')

    axes[0].set_ylabel('Temperature [°C]',fontdict=fontdicts,labelpad = 35)  
    axes[0].set_xlim(datetime(2021, 6, 1),datetime(2021, 6, 29))
    # for tick in axes[0].yaxis.get_major_ticks():
    #     tick.label.set_fontsize(12) 
        
    #%% RH
    axes[1].plot(DateTime,RelHum,linewidth = 3,color='royalblue')

    axes[1].set_ylabel('RH [%]',fontdict=fontdicts,labelpad = 30)  
    for tick in axes[0].yaxis.get_major_ticks():
        tick.label.set_fontsize(12) 
    #%% wind
    axes[2].scatter(DateTime,WindSpeed,color = fcolors, alpha=0.75)
    axes[2].set_ylabel('Wind Speed [m/s]',fontdict=fontdicts,labelpad = 40)
    
    #colorbar 左 下 宽 高 
    l = 0.92
    b = 0.42
    w = 0.006
    h = 0.13
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(scamap, cax=cbar_ax)
    cb.set_label('Wind Direction [°]' ,fontdict=fontdicts,labelpad =15 ) #设置colorbar的标签字体及其大小
    # axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    
    axes[3].plot(DateTime,Rain,linewidth = 3,color='red')
    axes[3].set_ylabel('Rain [mm]',fontdict=fontdicts,labelpad = 35)  

    ax=axes[3].twinx()
    ax.fill_between(DateTime,RainPerHour,0,color='blue')
    ax.set_ylabel('Rain [mm/h]',fontdict=fontdicts,labelpad = 35)  

    axes[4].plot(DateTime,Radiation,linewidth = 3,color='red')
    axes[4].set_ylabel('Radation\n[W $\mathregular{m^-}$$\mathregular{^2}$ ]',fontdict=fontdicts,labelpad = 35)  
    axes[4].set_xlabel(('Measurement Time, UTC'),fontdict={'weight': 'bold', 'size': 15},labelpad = 10)

    for i in range(4):    
        for tick in axes[i].yaxis.get_major_ticks():
            tick.label.set_fontsize(12) 
    plt.subplots_adjust(wspace=0, hspace=0,right=0.9)
    plt.savefig('2021_10minAVG_meteo_Swabian05')
    plt.close()
    

        
    
    