# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import os
import pandas as pd
import random


def SI_model(event_data,p,infected):
    #The for loop loops over events in a dataframe (thus df.iterrows() is used)
    #The for loop first checks whether the events Source airport is among the infected_airports and that the Destination airport is not amongst them
    #The for loop then checks that the StartTime of the flight is later than the time that the Source airport got infected
    #Then random number is generated and checked that it is smaller or equal to the probability of infection and decides whether to infect the destination airport
    #Then the destination airport is saved amongst the infected airports to the dictionary and to the list
    
    infected_airports = list(infected.keys())
                            
    for index, flight in event_data.iterrows():
        if flight["Source"] in infected_airports and flight["Destination"] not in infected_airports:
            if flight["StartTime"] >= infected[flight["Source"]]:
                random_n = random.random()
                if random_n <= p:
                    infected[flight["Destination"]] = flight["EndTime"]
                    infected_airports.append(flight["Destination"])
                    
    return infected 
    
def prevalence_average(event_data,infected,n,p,bins,iterations,event_range):
    count = 0
    prevalence_lists = [[]] * iterations 
    while count < iterations:
        freq, bins = np.histogram(SI_model(event_data,p,infected).values(), bins=bins, range=event_range)
        freq = [float(x) / n for x in freq]
        freq = np.cumsum(freq)
        prevalence_lists[count] = freq
        count += 1
    prevalence = np.array(prevalence_lists)
    prevalence = np.mean(prevalence, axis=0)
    return bins[:len(bins)-1], prevalence
    
    



if __name__ == "__main__":
    
    headers = ["Source","Destination","StartTime","EndTime","Duration"]
    event_data = pd.read_csv('C:/Users/kette/Complex networks/events_US_air_traffic_GMT.txt', sep=" ", header=None, names = headers)
    #print(event_data.head())
    airport_data = pd.read_csv('C:/Users/kette/Complex networks/US_airport_id_info.csv')
    #print(airport_data.head())
    
    event_data = event_data.sort_values(by="EndTime",ascending=1)
    #print(event_data.head())
    #print(event_data.describe())
    #print(event_data.dtypes())
    
    infected = {}
    infected[30] = 1229231100 # here you can change which airport(s) are infected in the beginnning and their infection times (now node 0 at the start of first flight)
    #print(infected)
    
    n = 279 # number of airports in the network
    p_infection = 0.5 # here you can change the probability of infection
    p_list = [0.01, 0.05, 0.1, 0.5, 1.0]
    
    sources = event_data["Source"]
    print(sources.head())
    
    print(event_data[:1])
    print(event_data[:1]["Source"])
    
    test_events = event_data.head(1000) # since the total dataset is so large here you can choose how many rows of event data to include in your test
    #print(test_events)
    
    #task1
    
    #print(SI_model(event_data,p_infection,infected)) #might take some time since event data is so large
    #print(SI_model(test_events,p_infection,infected))
    
    #task2
            
    #print(min(event_data["StartTime"]))
    #print(max(event_data["EndTime"]))
    #freq, bins = np.histogram(SI_model(test_events,p_infection,infected).values(), bins=np.linspace(min(event_data["StartTime"]),max(event_data["EndTime"]),10), range=[min(event_data["StartTime"]), max(event_data["EndTime"])], normed=False, weights=None)
    #freq = [float(x) / n for x in freq]
    
    bins = np.linspace(min(event_data["StartTime"]),max(event_data["EndTime"]),num=50) # you can choose the number of bins by changing the scalar
    iterations = 10 # you can choose the number of iterations to get the average from 
    event_range = [min(event_data["StartTime"]),max(event_data["EndTime"])]
    print(p_list[0])
    values1 = prevalence_average(event_data,infected,n,p_list[3],bins,iterations, event_range)
    x1 = values1[0]
    y1 = values1[1]
    #values2 = prevalence_average(event_data,infected,n,p_list[1],bins,iterations,event_range)
    #x2 = values2[0]
    #y2 = values2[1]
    #values3 = prevalence_average(event_data,infected,n,p_list[2],bins,iterations,event_range)
    #x3 = values3[0]
    #y3 = values3[1]
    #values4 = prevalence_average(event_data,infected,n,p_list[3],bins,iterations,event_range)
    #x4 = values4[0]
    #y4 = values4[1]
    #values5 = prevalence_average(event_data,infected,n,p_list[4],bins,iterations,event_range)
    #x5 = values5[0]
    #y5 = values5[1]
    #print(x1)
    print(y1)
    #print(y2)
    plt.plot(x1,y1)
    #plt.plot(x2,y2)
    #plt.plot(x3,y3)
    #plt.plot(x4,y4)
    #plt.plot(x5,y5)
    plt.legend(['p=0.05'], loc="best")
    #plt.legend(['p=0.01', 'p=0.05','p=0.1','p=0.5','p=1'], loc="best")
    plt.show()

    
    #plot_prevalence(event_data,infected,n)
    
    '''for p in p_list:
        infected_list = [[]] * 10
        x = 0
        while x < 10:
            result = SI_model(test_events,p,infected)
            infected_list[x] = result 
            x+=1
        print(infected_list) 
        for dictionary in infected_list:
            print(dictionary.values())'''
                
                
        
    
        
    
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
        
    '''infected_airports = list(infected.keys())
                            
    for index, flight in event_data.iterrows():
        if flight["Source"] in infected_airports and flight["Destination"] not in infected_airports:
            if flight["StartTime"] >= infected[flight["Source"]]:
                random_n = random.random()
                if random_n <= p_infection:
                    infected[flight["Destination"]] = flight["EndTime"]
                    infected_airports.append(flight["Destination"])'''
    #The for loop loops over events in a dataframe (thus df.iterrows() is used)
    #The for loop first checks whether the events Source airport is among the infected_airports and that the Destination airport is not amongst them
    #The for loop then checks that the StartTime of the flight is later than the time that the Source airport got infected
    #Then random number is generated and checked that it is smaller or equal to the probability of infection and decides whether to infect the destination airport
    #Then the destination airport is saved amongst the infected airports to the dictionary and to the list             
    
    #print(infected)
    #df_filtered = test_events[test_events["EndTime"] == 1229269200]
    #df_filtered2 = test_events[test_events["EndTime"] == 1229266800]
    #print(df_filtered) 
    #print(test_events.filter(like=1229269200, axis=3))
                
    
        
        
        
        
    #dictionary (node ja infection time), jossa kaikki eventit --> verrataan endtimeja noden infection timeen käydään lista läpi (kaikki nodet ei infektoidu)
    