
import requests # allows you to send html request
import pandas as pd #
from pandas.io.json import json_normalize
import json
import csv
import time
from xml.etree import ElementTree
import geopandas as gpd
from multiprocessing import Process  #For Multiprocessing i.e to Obtain Parallelism on CPU
import os #Basicly used for Getting system Information such as no of cores of your processor


global number_of_entry   # Variable for Number of Data Entry in the csv file
number_of_entry=3117710       # For now it is manual can be turned in to auto detect
global remainder         # Variable For storing remainder
remainder=number_of_entry%os.cpu_count()
#""" Remainder is calculated Because to make code very generic because every cpu has different number of cores on
#   which we can actually do Parallelism So in order to avoid data loss / data un-manuplation we actually calculate
#   the number of Possible Data Entry that can be done by Parallelism Rest are done by normal function calling
#   Example # I have 12 Core Processor So If their are 27 Data Entry We can withdraw result from 24 of the Enteries
#    with help of CPU Parallelism and Rest 3 Enteries Data Results will be calculated Normally """

def retries(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            print("here",response.status_code)#200 is a standard response for successful HTTP requests and 404 tells that the requested resource could not be found
            break
        else:
            print(response.status_code)
            # Hope it won't 500 a little later
            time.sleep(120)# multi treading can be done
            
    return response
        


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


reader =pd.read_csv('Feb-01-10.csv',encoding='utf-8', error_bad_lines=False,names=["VehicleID", "DateTime", "lat", "lon","speed","direction","reason","altitude"]) # returns a dataframe

ways_node_mapping= ('islamabaad_copy_nodes_ways_mapping.csv' )
    
df_row1 = pd.concat([reader]) #join  the Data
    
# data reading in csv
df_row=df_row1[["speed"]]
df_row["lat"]=df_row1["lat"].to_frame()
df_row["lon"]=df_row1["lon"].to_frame()
df_row["DateTime"]=df_row1["DateTime"].to_frame()
df_row["direction"]=df_row1["direction"].to_frame()
df_row["VehicleID"]=df_row1["VehicleID"].to_frame()
df_row["reason"]=df_row1["reason"].to_frame()
df_row["altitude"]=df_row1["altitude"].to_frame()
    

    

#"""Getting nodes Function is used for Getting nodes From OSRM"""
def getting_nodes(i,reader):
    lat=reader.lat[i]   #Reads the Value Stored latitude array
    lon=reader.lon[i]   #Reads the Value Stored longitude array
    url =  'http://172.30.30.30:5000/nearest/v1/driving/'+ str(lon) + ',' + str(lat) + '.json?number=1'#"""Sends the url Requests to Extract Data from OSRM"""
    response = retries(url)       # Stores Responces From URL
    print(response.status_code)   # Prints the Status Code of the URL which Standard are 200 for True and 404 for False
    data = response.json()        # Data is in the form of Json from OSRM
    flat = flatten_json(data)     # To Flatten ambiguity/multiple Entries in Single Coloumn
    if i==0: # just for making a frame
        dfObj = pd.DataFrame(flat, index=list(range(0,1))) # Arithmetic operations align on both row and column labels.
    else:    # then appends
        dfObj = dfObj.append(flat, ignore_index=True)      # index lable are not used

global last_value
last_value=0

#""" Multiprocessing Function to Actually Enable the Process of Parallelism on CPU
#
#   Last Value is Passed as Argument To keep track of Data Entries Processed So that it doesn't Start form Zero Again and
#  Again when Called
#"""
def multiprocessing(last_value,reader):
    processes = [] # An Array to Store Number of Process to be Done in Parallelism ,Size of This Depends Upon the Number of Cores your CPU has
    for i in range (last_value,os.cpu_count()+last_value):
#      """Loop starting from Last Value and Iterates till all cores are Occupied This Basically Register Cores for The
#         Process to Be done"""
#       """Remove this Print Function That is next"""
        print('registering process %d' % last_value) # Just a check that this Core has been Registered
#        """Remove till Here """
        processes.append(Process(target=getting_nodes , args=[i,reader])) # Here Process is Registered in a Single Core
        last_value+=1                                              # For Printing Up Only
        
    for process in processes: #""" For Loop to Actually Start all Process Registered in Array or Cores of CPU """
        process.start()    # Starts the Process on a Core

    for process in processes: #""" For Loop to Actually Wait for all Process Registered in Array or Cores of CPU to end """
        process.join()     # Join the  Results in Order
        
global k
k=0

#""" For loop to Actually call the MultiProcess Function with 3 Args
#    1) k*os.cpu_count() is used to start the loop each time from n position So that we can keep the Track of Data Processed
#       Depends upon the  number of Cores of CPU For Example if their are 12  Cores then i value will be 0 ,12 ,24 ... and so
#       on This help that data is not re Processed and Dupliucates are not made
#    2) number_of_entry-remainder as Disscussed earlier this enables us to only manipulate maximum amount of data through
#       Parallelism That can be done by all cores of cpu running at one time This is a perfect Divisble by Number of Cores
#    3) os.cpu_count() is used to make i jump/iterate n numbers whereas n = no of cores your CPU has for example 0,12,24...
#    """"
for i in range (k*os.cpu_count(),number_of_entry-remainder,os.cpu_count()):
    multiprocessing(i,reader)  # calling of function
    k+=1                # to actually maintain the starting value of i
    
#""" For Loop to Actually call the Function Normally it has 2 Args
#    1) number_of_entry-remainder Starting Point for 'i' which can vary but will be in between:
#    number_of_entry - no_of_cores_of _ cpu
#    2) Runs till end of Data Entry which is no more times then no_of_cores_of _ cpu - 1 For Example if CPU has 12 cores it
#    will run for max of 11 times and min of 0 times
#    """
for i in range (number_of_entry-remainder,number_of_entry):
    getting_nodes(i,reader);# Function of Getting Node is Called



nodes=dfObj[["waypoints_0_location_0",'waypoints_0_location_1',"waypoints_0_nodes_0","waypoints_0_nodes_1"]]
nodes.rename(columns = {'waypoints_0_location_0':'lon'}, inplace = True)# inplace true returns a null and returns a copy of modified data inother words Data is modified in that Place
nodes.rename(columns = {'waypoints_0_location_1':'lat'}, inplace = True)
nodes.rename(columns = {'waypoints_0_nodes_0':'start_node'}, inplace = True)
nodes.rename(columns = {'waypoints_0_nodes_1':'end_node'}, inplace = True)
nodes['speed']=select_road2['speed'].values
nodes['DateTime']=select_road2['DateTime'].values
nodes['direction']=select_road2['direction'].values
nodes['altitude']=select_road2['altitude'].values
nodes['VehicleID']=select_road2['VehicleID'].values
nodes['reason']=select_road2['reason'].values

  
ways_node_mapping.rename(columns = {'node_id':'end_node'}, inplace = True)

nodes["lat"]=nodes["lat"].astype(float)
nodes["lon"]=nodes["lon"].astype(float)
nodes["speed"]=nodes["speed"].astype(float)
nodes["DateTime"]=nodes["DateTime"].astype(str)
nodes["direction"]=nodes["direction"].astype(float)
nodes["altitude"]=nodes["altitude"].astype(float)
nodes["VehicleID"]=nodes["VehicleID"].astype(float)
nodes["reason"]=nodes["reason"].astype(str)

ls_year=[]
ls_month=[]
ls_day=[]
ls_hour=[]
ls_minute=[]
ls_second=[]



"""
Author: Amna Shamshad
"""

i=0
# appending Data
for i in range(len(nodes["DateTime"])):
    dateTime=nodes.DateTime[i]
    token=dateTime.split(' ')
    date=token[0]
    time1=token[1]
    token1=date.split('-')
    year=int(token1[0])
    month=int(token1[1])
    day=int(token1[2])
    token2=time1.split(':')
    hour=float(token2[0])
    minute=float(token2[1])
    second=float(token2[2])
    ls_year.append(year)
    ls_month.append(month)
    ls_day.append(day)
    ls_hour.append(hour)
    ls_minute.append(minute)
    ls_second.append(second)


     
nodes['year']=ls_year
nodes['month']=ls_month
nodes['day']=ls_day
nodes['hour']=ls_hour
nodes['minute']=ls_minute
nodes['second']=ls_second


nodes.rename(columns = {'waypoints_0_nodes_1':'end_node'}, inplace = True)
complete_data=pd.merge(ways_node_mapping, nodes, on=['end_node'], how='inner')
    
complete_data.to_csv(r'/home/abid/Downloads/feb_data.csv')# terminal
