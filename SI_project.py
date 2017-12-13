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
    infected[0] = 0 # here you can change which airport(s) are infected in the beginnning and their infection times
    print(infected)
    
    p_infection = 1
    
    sources = event_data["Source"]
    print(sources.head())
    
    print(event_data[:1])
    print(event_data[:1]["Source"])
    
    test_events = event_data.head(20000) # since the total dataset is so large here you can choose how many rows of event data to include in your test
    #print(test_events)
    
    '''for index, flight in event_data.iterrows():
        for key in infected.items():
             if flight[:2] == key:
                 infected[flight["Destination"]] = flight["Endtime"]'''
                    
    
    
    '''for index, flight in test_events.iterrows():
        for key in infected.items():
            if flight["Source"] == key[0]:
                random_n = random.random()
                if random_n <= p_infection:
                    infected[flight["Destination"]] = flight["EndTime"]'''
        
    infected_airports = list(infected.keys())
                            
    for index, flight in test_events.iterrows():
        if flight["Source"] in infected_airports and flight["Destination"] not in infected_airports:
            if flight["StartTime"] >= infected[flight["Source"]]:
                random_n = random.random()
                if random_n <= p_infection:
                    infected[flight["Destination"]] = flight["EndTime"]
                    infected_airports.append(flight["Destination"])
    #The for loop loops over events in a dataframe (thus df.iterrows() is used)
    #The for loop first checks whether the events Source airport is among the infected_airports and that the Destination airport is not amongst them
    #The for loop then checks that the StartTime of the flight is later than the time that the Source airport got infected
    #Then random number is generated and checked that it is smaller or equal to the probability of infection and decides whether to infect the destination airport
    #Then the destination airport is saved amongst the infected airports to the dictionary and to the list             
    
    print(infected)
    #df_filtered = test_events[test_events["EndTime"] == 1229269200]
    #df_filtered2 = test_events[test_events["EndTime"] == 1229266800]
    #print(df_filtered) 
    #print(test_events.filter(like=1229269200, axis=3))
                
    
        
        
        
        
    #dictionary (node ja infection time), jossa kaikki eventit --> verrataan endtimeja noden infection timeen käydään lista läpi (kaikki nodet ei infektoidu)
    