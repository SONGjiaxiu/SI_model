# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import os
import pandas as pd
import random

if __name__ == "__main__":
    
    headers = ["Source","Destination","StartTime","EndTime","Duration"]
    event_data = pd.read_csv('C:/Users/kette/Complex networks/events_US_air_traffic_GMT.txt', sep=" ", header=None, names = headers)
    print(event_data.head())
    airport_data = pd.read_csv('C:/Users/kette/Complex networks/US_airport_id_info.csv')
    print(airport_data.head())
    
    event_data = event_data.sort_values(by="EndTime",ascending=1)
    print(event_data.head())
    print(event_data.describe())
    #print(event_data.dtypes())
    
    infected = {}
    infected[0] = 1229244950
    print(infected)
    
    p_infection = 1
    
    sources = event_data["Source"]
    print(sources.head())
    
    print(event_data[:1])
    print(event_data[:1]["Source"])
    
    test_events = event_data.head(100)
    print(test_events)
    
    '''for index, flight in event_data.iterrows():
        for key in infected.items():
             if flight[:2] == key:
                 infected[flight["Destination"]] = flight["Endtime"]'''
                    
    for index, flight in test_events.iterrows():
        for key in infected.items():
            if flight["Source"] == key[0]:
                random_n = random.random()
                if random_n <= p_infection:
                    infected[flight["Destination"]] = flight["EndTime"]
                
    print(infected)
                
    
        
        
        
        
    #dictionary (node ja infection time), jossa kaikki eventit --> verrataan endtimeja noden infection timeen käydään lista läpi (kaikki nodet ei infektoidu)
    