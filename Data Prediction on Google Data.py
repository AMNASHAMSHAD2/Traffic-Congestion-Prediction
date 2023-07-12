# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 02:51:50 2020

@author: amnac
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:07:35 2020

@author: Amna Shamshad
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:06:56 2020

@author: Amna Shamshad
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:51:52 2020
 
@author: Amna Shamshad
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_curve, precision_recall_curve,classification_report
from sklearn.metrics import confusion_matrix, f1_score
from sklearn import metrics

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.multiclass import OneVsRestClassifier

from sklearn.metrics import average_precision_score

from sklearn.metrics import precision_recall_fscore_support

import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
import requests
import bs4
import datetime
from time import sleep, strftime 
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QTextEdit,QMessageBox


# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:33:38 2020

@author: amnac
"""

import pandas as pd
import requests
import bs4
import datetime
from time import sleep, strftime 

   
   
   

def clean_data(data):
       '''in cleaning we have yet done a very little part i.e. converting string variables into integer or float variables
because machine learning models work with numerical values so it is mandatory to convert input and output variables into
numerical variables. We can also use pd.get_dummies() method to convert directly but in our case this method will be unable
to find corresponding numerical values'''
       # locate in data where the data['Day'] is equal to Sunday and replace the Day column at all those positions with 0
       data.loc[data['Day'] == 'Sunday', 'Day'] = 0
       data.loc[data['Day'] == 'Monday', 'Day'] = 1
       data.loc[data['Day'] == 'Tuesday', 'Day'] = 2
       data.loc[data['Day'] == 'Wednesday', 'Day'] = 3
       data.loc[data['Day'] == 'Thursday', 'Day'] = 4
       data.loc[data['Day'] == 'Friday', 'Day'] = 5
       data.loc[data['Day'] == 'Saturday', 'Day'] = 6

        data.loc[data['Weather'] == 'sunny', 'Weather'] = 0
       data.loc[data['Weather'] == 'cloudy', 'Weather'] = 1
       data.loc[data['Weather'] == 'Rain', 'Weather'] = 2
       data.loc[data['Weather'] == 'Showers', 'Weather'] = 2
       data.loc[data['Weather'] == 'Clear', 'Weather'] = 0
       data.loc[data['Weather'] == 'Mostly Cloudy', 'Weather'] = 1
       data.loc[data['Weather'] == 'Cloudy', 'Weather'] = 1
       data.loc[data['Weather'] == 'Partly Cloudy', 'Weather'] = 1
       data.loc[data['Weather'] == 'Mostly Clear', 'Weather'] = 0
       data.loc[data['Weather'] == 'Sunny', 'Weather'] = 0
       data.loc[data['Weather'] == 'Mostly Sunny', 'Weather'] = 0
       data.loc[data['Weather'] == 'Thunderstorms', 'Weather'] = 2
       data.loc[data['Weather'] == 'Scattered Thunderstorms', 'Weather'] = 2
       data.loc[data['Weather'] == 'Heavy Rain', 'Weather'] = 2
       data.loc[data['Weather'] == 'ShowersDate', 'Weather'] = 2
       
       #data.loc[data['Time'] == 'peak_hour', 'Time'] = 1
       #data.loc[data['Time'] == 'non_peak_hour', 'Time'] = 0

       data.loc[data['Holiday'] == 'yes', 'Holiday'] = 1
       data.loc[data['Holiday'] == 'no', 'Holiday'] = 0

       count_occasion=0
       for holiday in data['Special_Condition'].unique():
              # replace the location names with count variable value both in starting and destination columns
              # e.g. saddar will have value of 1 in both columns
              data.loc[data['Special_Condition'] == holiday, 'Special_Condition'] = count_occasion
              #data.loc[data['Destination_Location'] == location, 'Destination_Location'] = count
              count_occasion += 1

       count1 = 0
       # unique() returns list of every unique item in the pandas series
       # pandas series means a column in pandas
       for location in data['Starting_Location'].unique():
              # replace the location names with count variable value both in starting and destination columns
              # e.g. saddar will have value of 1 in both columns
              data.loc[data['Starting_Location'] == location, 'Starting_Location'] = count1
              #data.loc[data['Destination_Location'] == location, 'Destination_Location'] = count
              count1 += 1
       count2 = 0
       for location in data['Destination_Location'].unique():
              # replace the location names with count variable value both in starting and destination columns
              # e.g. saddar will have value of 1 in both columns
              #data.loc[data['Starting_Location'] == location, 'Starting_Location'] = count
              data.loc[data['Destination_Location'] == location, 'Destination_Location'] = count2
              count2 += 1
       

       
       data.loc[data['Fastest_Route_Name'] == 'r', 'Fastest_Route_Name'] = 200
       data.loc[data['Fastest_Route_Name'] == 'Murree Rd', 'Fastest_Route_Name'] = 0
       data.loc[data['Fastest_Route_Name'] == '6th Rd', 'Fastest_Route_Name'] = 1
       data.loc[data['Fastest_Route_Name'] == '9th Ave', 'Fastest_Route_Name'] = 2
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue and 9th Ave', 'Fastest_Route_Name'] = 3
       data.loc[data['Fastest_Route_Name'] == 'Faisal Avenue Flyover and Jinnah Avenue', 'Fastest_Route_Name'] = 4
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Ave and Faisal Avenue Flyover', 'Fastest_Route_Name'] = 5
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Ave', 'Fastest_Route_Name'] = 6
       data.loc[data['Fastest_Route_Name'] == 'Agha Khan Rd and Jinnah Ave', 'Fastest_Route_Name'] = 7
       data.loc[data['Fastest_Route_Name'] == 'Constitution Ave and Jinnah Ave', 'Fastest_Route_Name'] = 8
       data.loc[data['Fastest_Route_Name'] == 'I.J.P. Road and Stadium Rd', 'Fastest_Route_Name'] = 9
       data.loc[data['Fastest_Route_Name'] == '9th Ave and Stadium Rd', 'Fastest_Route_Name'] = 10
       data.loc[data['Fastest_Route_Name'] == 'Constitution Ave, A.K.M. Fazl-ul-Haq Road and Jinnah Ave', 'Fastest_Route_Name'] = 11
       data.loc[data['Fastest_Route_Name'] == 'Service Rd South I 8', 'Fastest_Route_Name'] = 12
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue', 'Fastest_Route_Name'] = 13
       data.loc[data['Fastest_Route_Name'] == '7th Ave', 'Fastest_Route_Name'] = 15
       data.loc[data['Fastest_Route_Name'] == '9th Av', 'Fastest_Route_Name'] = 16
       data.loc[data['Fastest_Route_Name'] == '9th Ave and Kashmir Hwy', 'Fastest_Route_Name'] = 17
       data.loc[data['Fastest_Route_Name'] == '9th Ave,Kashmir Hwy and 7th Ave', 'Fastest_Route_Name'] = 18
       data.loc[data['Fastest_Route_Name'] == 'A.K. Fazl-ul-Haq Rd', 'Fastest_Route_Name'] = 19
       data.loc[data['Fastest_Route_Name'] == 'A.K. Fazl-ul-Haq Rd and Jinnah Ave', 'Fastest_Route_Name'] = 20
       data.loc[data['Fastest_Route_Name'] == 'Agha Khan Rd', 'Fastest_Route_Name'] = 21
       data.loc[data['Fastest_Route_Name'] == 'Agha Khan Rd and Jinnah Ave', 'Fastest_Route_Name'] = 22
       data.loc[data['Fastest_Route_Name'] == 'Ahmed Faraz Rd and Aun Muhammad Rizvi Rd', 'Fastest_Route_Name'] = 23
       data.loc[data['Fastest_Route_Name'] == 'Awan-e-Sanat-o-Tiijarat', 'Fastest_Route_Name'] = 24
       data.loc[data['Fastest_Route_Name'] == 'Awan-e-Sanat-o-Tiijarat and Kashmir Hwy', 'Fastest_Route_Name'] = 25
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue and 9th Ave', 'Fastest_Route_Name'] = 26
       data.loc[data['Fastest_Route_Name'] == 'Faisal Avenue Flyover and Jinnah Avenue', 'Fastest_Route_Name'] = 27
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Ave and Faisal Avenue Flyover', 'Fastest_Route_Name'] = 28
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Ave', 'Fastest_Route_Name'] = 29
       data.loc[data['Fastest_Route_Name'] == 'Constitution Ave and Jinnah Ave', 'Fastest_Route_Name'] = 30
       data.loc[data['Fastest_Route_Name'] == '9th Ave and Stadium Rd', 'Fastest_Route_Name'] = 31
       data.loc[data['Fastest_Route_Name'] == 'Agha Khan Rd and Jinnah Ave', 'Fastest_Route_Name'] =32 
       data.loc[data['Fastest_Route_Name'] == 'Constitution Ave', 'Fastest_Route_Name'] = 33
       data.loc[data['Fastest_Route_Name'] == 'Constitution Ave and Jinnah Ave', 'Fastest_Route_Name'] =34 
       data.loc[data['Fastest_Route_Name'] == 'I.J.P. Road', 'Fastest_Route_Name'] = 35
       data.loc[data['Fastest_Route_Name'] == 'Ibn-e-Sina Rd', 'Fastest_Route_Name'] =36 
       data.loc[data['Fastest_Route_Name'] == 'Ismail Zabeeh Rd and Faisal Ave', 'Fastest_Route_Name'] = 37
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue and 9th Ave', 'Fastest_Route_Name'] = 38
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue and Faisal Avenue Flyover', 'Fastest_Route_Name'] = 39
       data.loc[data['Fastest_Route_Name'] == 'Kashmir Hwy', 'Fastest_Route_Name'] = 40
       data.loc[data['Fastest_Route_Name'] == 'Main Margalla Rd', 'Fastest_Route_Name'] = 41
       data.loc[data['Fastest_Route_Name'] == 'Nazim-ud-din Rd', 'Fastest_Route_Name'] = 42
       data.loc[data['Fastest_Route_Name'] == 'Parbat Rd and 7th Ave', 'Fastest_Route_Name'] = 43
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E', 'Fastest_Route_Name'] = 44
       data.loc[data['Fastest_Route_Name'] == 'Service Rd South I 8', 'Fastest_Route_Name'] =45 
       data.loc[data['Fastest_Route_Name'] == 'Service Rd W', 'Fastest_Route_Name'] =46 
       data.loc[data['Fastest_Route_Name'] == 'Sufi Tabasum Rd and Service Rd W', 'Fastest_Route_Name'] = 47
       data.loc[data['Fastest_Route_Name'] == 'Tipu Sultan Rd', 'Fastest_Route_Name'] = 48
       data.loc[data['Fastest_Route_Name'] == 'nishing School', 'Fastest_Route_Name'] = 49
       data.loc[data['Fastest_Route_Name'] == 'I.J.P. Rd and I.J.P. Road', 'Fastest_Route_Name'] = 61
       data.loc[data['Fastest_Route_Name'] == 'Faisal Ave', 'Fastest_Route_Name'] = 62
       data.loc[data['Fastest_Route_Name'] == 'Aun Muhammad Rizvi Rd', 'Fastest_Route_Name'] = 63
       data.loc[data['Fastest_Route_Name'] == 'Faisal Ave and Faisal Ave/Islamabad Expressway', 'Fastest_Route_Name'] = 64
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Avenue Underpass and Faisal Ave', 'Fastest_Route_Name'] = 65
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E, Street 40 and Service Road South', 'Fastest_Route_Name'] = 66
       data.loc[data['Fastest_Route_Name'] == 'Service Road East', 'Fastest_Route_Name'] = 67
       data.loc[data['Fastest_Route_Name'] == 'Murree Rd and I.J.P. Road', 'Fastest_Route_Name'] = 68
       data.loc[data['Fastest_Route_Name'] == 'Street 54 and Service Rd E', 'Fastest_Route_Name'] = 69
       data.loc[data['Fastest_Route_Name'] == 'Sufi Tabasum Rd', 'Fastest_Route_Name'] = 70
       data.loc[data['Fastest_Route_Name'] == 'Faisal Ave/Islamabad Expressway', 'Fastest_Route_Name'] = 71
       data.loc[data['Fastest_Route_Name'] == 'Ataturk Ave', 'Fastest_Route_Name'] = 72
       data.loc[data['Fastest_Route_Name'] == 'Ataturk Ave and Constitution Ave', 'Fastest_Route_Name'] = 73
       data.loc[data['Fastest_Route_Name'] == 'Stadium Rd and Murree Rd', 'Fastest_Route_Name'] = 74
       data.loc[data['Fastest_Route_Name'] == 'Aiwan-e-Sanat-o-Tijarat and Kashmir Hwy', 'Fastest_Route_Name'] = 75
       data.loc[data['Fastest_Route_Name'] == 'Murree Rd/N-75 and Khayaban-e-Suhrwardy', 'Fastest_Route_Name'] = 76
       data.loc[data['Fastest_Route_Name'] == 'Service Rd W and Faisal Ave', 'Fastest_Route_Name'] = 77
       data.loc[data['Fastest_Route_Name'] == 'Club Rd', 'Fastest_Route_Name'] = 78
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E and Kashmir Hwy', 'Fastest_Route_Name'] = 79
       data.loc[data['Fastest_Route_Name'] == 'Service Rd I 11 (South) and I.J.P. Road', 'Fastest_Route_Name'] = 80
       data.loc[data['Fastest_Route_Name'] ==  'Club Rd and Constitution Ave', 'Fastest_Route_Name'] = 81 
       data.loc[data['Fastest_Route_Name'] == 'Main Margalla Rd, 9th Ave and Kashmir Hwy', 'Fastest_Route_Name'] = 82
       data.loc[data['Fastest_Route_Name'] == 'Main Margalla Rd and 7th Ave', 'Fastest_Route_Name'] = 83
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E and 9th Ave', 'Fastest_Route_Name'] = 84
       data.loc[data['Fastest_Route_Name'] == 'Shan-ul-Haq Haqqee Rd and Kashmir Hwy', 'Fastest_Route_Name'] = 85
       data.loc[data['Fastest_Route_Name'] == '9th Ave, Kashmir Hwy and 7th Ave', 'Fastest_Route_Name'] = 86
       data.loc[data['Fastest_Route_Name'] == 'City-Sadar Road', 'Fastest_Route_Name'] = 87
       data.loc[data['Fastest_Route_Name'] == 'Service Rd W and 9th Ave', 'Fastest_Route_Name'] = 88
       data.loc[data['Fastest_Route_Name'] == 'Stadium Rd', 'Fastest_Route_Name'] = 89
       data.loc[data['Fastest_Route_Name'] == 'Nazim-ud-din Rd and Jinnah Ave', 'Fastest_Route_Name'] = 90
       data.loc[data['Fastest_Route_Name'] == 'Ibn-e-Sina Rd and 9th Ave', 'Fastest_Route_Name'] = 91
       data.loc[data['Fastest_Route_Name'] == 'Aiwan-e-Sanat-o-Tijarat', 'Fastest_Route_Name'] = 92
       data.loc[data['Fastest_Route_Name'] == 'Sufi Tabasum Rd and 9th Ave', 'Fastest_Route_Name'] = 93
       data.loc[data['Fastest_Route_Name'] == 'Luqman Hakeem Rd and Jinnah Ave', 'Fastest_Route_Name'] = 94
       data.loc[data['Fastest_Route_Name'] == 'Service Rd South I 8 and Stadium Rd', 'Fastest_Route_Name'] = 95
       data.loc[data['Fastest_Route_Name'] == 'Service Rd North (VR-30) and Main Margalla Rd', 'Fastest_Route_Name'] = 96
       data.loc[data['Fastest_Route_Name'] == 'Liaqat Rd and Murree Rd', 'Fastest_Route_Name'] = 97
       data.loc[data['Fastest_Route_Name'] == 'Liaqat Rd', 'Fastest_Route_Name'] = 98
       data.loc[data['Fastest_Route_Name'] == 'AK Brohi Rd and Faqir Aipee Road', 'Fastest_Route_Name'] = 99
       data.loc[data['Fastest_Route_Name'] == 'Gomal Rd and Main Margalla Rd', 'Fastest_Route_Name'] = 100
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E and Aun Muhammad Rizvi Rd', 'Fastest_Route_Name'] = 101
       data.loc[data['Fastest_Route_Name'] == 'Service Rd N', 'Fastest_Route_Name'] = 102
       data.loc[data['Fastest_Route_Name'] == 'Pitras Bukhari Rd', 'Fastest_Route_Name'] = 103
       data.loc[data['Fastest_Route_Name'] == 'Park Rd', 'Fastest_Route_Name'] = 104
       data.loc[data['Fastest_Route_Name'] == 'Street 40', 'Fastest_Route_Name'] = 105
       data.loc[data['Fastest_Route_Name'] == 'Jinnah Ave and Constitution Ave', 'Fastest_Route_Name'] = 106
       data.loc[data['Fastest_Route_Name'] == 'Garden Ave', 'Fastest_Route_Name'] = 107
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E, Muhammad Tufail Niazi Rd and Service Road South', 'Fastest_Route_Name'] = 108
       data.loc[data['Fastest_Route_Name'] == 'Bela Rd and Service Road South', 'Fastest_Route_Name'] = 109
       data.loc[data['Fastest_Route_Name'] == 'AK Brohi Rd', 'Fastest_Route_Name'] = 110
       data.loc[data['Fastest_Route_Name'] == 'Service Road South and Aun Muhammad Rizvi Rd', 'Fastest_Route_Name'] = 111
       data.loc[data['Fastest_Route_Name'] == 'Service Road South and Aun Muhammad Rizvi Rd', 'Fastest_Route_Name'] = 112
       data.loc[data['Fastest_Route_Name'] == 'â€«Parbat Rdâ€¬â€Ž', 'Fastest_Route_Name'] = 113
       data.loc[data['Fastest_Route_Name'] == 'Parbat Rd', 'Fastest_Route_Name'] = 113
       data.loc[data['Fastest_Route_Name'] == '\u202bParbat Rd\u202c\u200e', 'Fastest_Route_Name'] = 113
       data.loc[data['Fastest_Route_Name'] == 'Parveen Shakir Rd', 'Fastest_Route_Name'] = 114
       data.loc[data['Fastest_Route_Name'] == 'â€«Sawan Roadâ€¬â€Ž and Kurram Road', 'Fastest_Route_Name'] = 115
       data.loc[data['Fastest_Route_Name'] == '\u202bSawan Road\u202c\u200e and Kurram Road', 'Fastest_Route_Name'] = 115
       data.loc[data['Fastest_Route_Name'] == 'Aiwan-e-Sanat-o-Tijarat', 'Fastest_Route_Name'] = 116
       data.loc[data['Fastest_Route_Name'] == 'Bela Rd', 'Fastest_Route_Name'] = 117
       data.loc[data['Fastest_Route_Name'] == 'Chaman Rd', 'Fastest_Route_Name'] = 118
       data.loc[data['Fastest_Route_Name'] == 'College Rd', 'Fastest_Route_Name'] = 119
       data.loc[data['Fastest_Route_Name'] == 'Faisal Ave', 'Fastest_Route_Name'] = 120
       data.loc[data['Fastest_Route_Name'] == 'Faisal Ave and Service Road East', 'Fastest_Route_Name'] = 121
       data.loc[data['Fastest_Route_Name'] == 'Hamza Rd', 'Fastest_Route_Name'] = 122
       data.loc[data['Fastest_Route_Name'] == 'Hanna Rd', 'Fastest_Route_Name'] = 123
       data.loc[data['Fastest_Route_Name'] == 'Hillal Rd', 'Fastest_Route_Name'] = 124
       data.loc[data['Fastest_Route_Name'] == 'Hillal Rd and Major Rd', 'Fastest_Route_Name'] = 125
       data.loc[data['Fastest_Route_Name'] == 'Ibn-e-Sina Rd and Hanna Rd', 'Fastest_Route_Name'] = 126
       data.loc[data['Fastest_Route_Name'] == 'Ibn-e-Sina Rd and Service Road East', 'Fastest_Route_Name'] = 127
       data.loc[data['Fastest_Route_Name'] == 'Ismail Zabeeh Rd', 'Fastest_Route_Name'] = 128
       data.loc[data['Fastest_Route_Name'] == 'Jehlum Rd', 'Fastest_Route_Name'] = 129
       data.loc[data['Fastest_Route_Name'] == 'Jhelum Road', 'Fastest_Route_Name'] = 130
       data.loc[data['Fastest_Route_Name'] == 'Johar Rd', 'Fastest_Route_Name'] = 131
       data.loc[data['Fastest_Route_Name'] == 'Kaghan Rd', 'Fastest_Route_Name'] = 132
       data.loc[data['Fastest_Route_Name'] == 'Kohistan Rd', 'Fastest_Route_Name'] = 133
       data.loc[data['Fastest_Route_Name'] == 'Kohsar Rd', 'Fastest_Route_Name'] = 134
       data.loc[data['Fastest_Route_Name'] == 'Kurram Road', 'Fastest_Route_Name'] = 135
       data.loc[data['Fastest_Route_Name'] == 'Main Margalla Rd', 'Fastest_Route_Name'] = 136
       data.loc[data['Fastest_Route_Name'] == 'Major Rd', 'Fastest_Route_Name'] = 137
       data.loc[data['Fastest_Route_Name'] == 'Major Rd and Hillal Rd', 'Fastest_Route_Name'] = 138
       data.loc[data['Fastest_Route_Name'] == 'Mangla Rd', 'Fastest_Route_Name'] = 139
       data.loc[data['Fastest_Route_Name'] == 'Markaz Rd', 'Fastest_Route_Name'] = 140
       data.loc[data['Fastest_Route_Name'] == 'Marvi Rd', 'Fastest_Route_Name'] = 141
       data.loc[data['Fastest_Route_Name'] == 'Muhammad Tufail Niazi Rd and Rohtas Rd', 'Fastest_Route_Name'] = 142
       data.loc[data['Fastest_Route_Name'] == 'Neelam Rd', 'Fastest_Route_Name'] = 143
       data.loc[data['Fastest_Route_Name'] == 'Omeed Rd', 'Fastest_Route_Name'] = 144
       data.loc[data['Fastest_Route_Name'] == 'Park Rd', 'Fastest_Route_Name'] = 145
       data.loc[data['Fastest_Route_Name'] == 'Ravi Rd', 'Fastest_Route_Name'] = 146
       data.loc[data['Fastest_Route_Name'] == 'Rohtas Rd', 'Fastest_Route_Name'] =147 
       data.loc[data['Fastest_Route_Name'] == 'Sachal Sarmast Road', 'Fastest_Route_Name'] = 148
       data.loc[data['Fastest_Route_Name'] == 'Sawan Rd', 'Fastest_Route_Name'] = 149
       data.loc[data['Fastest_Route_Name'] == 'Sawan Rd and \u202bSawan Road\u202c\u200e', 'Fastest_Route_Name'] = 150
       data.loc[data['Fastest_Route_Name'] == 'Sawan Rd and â€«Sawan Roadâ€¬â€Ž', 'Fastest_Route_Name'] = 151
       data.loc[data['Fastest_Route_Name'] == 'Service Rd E', 'Fastest_Route_Name'] = 152
       data.loc[data['Fastest_Route_Name'] == 'Service Road East', 'Fastest_Route_Name'] = 153
       data.loc[data['Fastest_Route_Name'] == 'Service Rd N', 'Fastest_Route_Name'] = 154
       data.loc[data['Fastest_Route_Name'] == 'Service Rd North (VR-30)', 'Fastest_Route_Name'] = 155
       data.loc[data['Fastest_Route_Name'] == 'Shabbir Sharif Road', 'Fastest_Route_Name'] = 156
       data.loc[data['Fastest_Route_Name'] == 'Shan-ul-Haq Haqqee Rd', 'Fastest_Route_Name'] = 157
       data.loc[data['Fastest_Route_Name'] == 'Sumbal Rd', 'Fastest_Route_Name'] = 158
       data.loc[data['Fastest_Route_Name'] == 'Umeed Rd', 'Fastest_Route_Name'] = 159
       data.loc[data['Fastest_Route_Name'] == 'A. K. Brohi Road', 'Fastest_Route_Name'] = 160
        data.loc[data['Fastest_Route_Name'] == 'I.J.P. Road and 6th Rd', 'Fastest_Route_Name'] = 161
       data.loc[data['Fastest_Route_Name'] == 'Service Rd N and Stadium Rd', 'Fastest_Route_Name'] = 162
       data.loc[data['Fastest_Route_Name'] == 'Service Road I-12 (South) and I.J.P. Road', 'Fastest_Route_Name'] = 163
       data.loc[data['Fastest_Route_Name'] == 'Street 41', 'Fastest_Route_Name'] = 164
       data.loc[data['Fastest_Route_Name'] == 'Service Rd N and Murree Rd', 'Fastest_Route_Name'] = 165
       data.loc[data['Fastest_Route_Name'] == 'Bokra Rd', 'Fastest_Route_Name'] = 166
       data.loc[data['Fastest_Route_Name'] == 'Ibn-e-Sina Rd and Nazim-ud-din Rd', 'Fastest_Route_Name'] = 126
       data.loc[data['Fastest_Route_Name'] == 'Dhoke Hasu Rd', 'Fastest_Route_Name'] = 168
       
       
       data.loc[data['maxspeed'] == '40', 'maxspeed'] = 0
       data.loc[data['maxspeed'] == '60', 'maxspeed'] = 1
       data.loc[data['maxspeed'] == '100', 'maxspeed'] = 2
       data.loc[data['maxspeed'] == '100', 'maxspeed '] = 3
       
       data.loc[data['lanes'] == '1', 'lanes'] = 0
       data.loc[data['lanes'] == '2', 'lanes'] = 1
       data.loc[data['lanes'] == '3', 'lanes'] = 2
       data.loc[data['lanes'] == '4', 'lanes'] = 3
       
       data.loc[data['surface'] == 'asphalt', 'surface'] = 0
       data.loc[data['surface'] == 'concrete', 'surface'] = 1
       
       data.loc[data['oneway'] == 'yes', 'oneway'] = 0
       
       data.loc[data['Highway'] == 'Primary', 'Highway'] = 0
       data.loc[data['Highway'] == 'Secondary', 'Highway'] = 1
       data.loc[data['Highway'] == 'Tertiary', 'Highway'] = 2
       data.loc[data['Highway'] == 'Trunk', 'Highway'] = 3
       
       # replace Sys_Time
       data['Sys_Time'] = data['Sys_Time'].str.replace(r':(.*)', '')

       # replace Date
       data['Date'] = data['Date'].str.replace(r'/0', '')
       data['Date'] = data['Date'].str.replace(r'/2019', '')
       data['Date'] = data['Date'].str.replace(r'/', '')


# loading and cleaning training data
data_train = pd.read_csv('Predicted_2020_Features.csv')
clean_data(data_train)

# convert Fastest_Route_Time from seconds to minutes to converge them near to each other
data_train['Fastest_Route_Time'] = data_train['Fastest_Route_Time'] / 60

# seperate the data into features and target
# as the brackets [] take only one argument so we have to give one list with many column names as argument in X_train
X = data_train[['Date', 'Day', 'Sys_Time', 'Weather', 'Holiday', 'Special_Condition', 'Starting_Location',
          'Destination_Location', 'Fastest_Route_Name','maxspeed','surface','oneway','lanes','Highway']]
y = data_train['Data_prediction']

y = y.replace('slightly congested', 1)
y = y.replace('smooth', 0)
y = y.replace('blockage', 4)
y = y.replace('congested', 2)
y = y.replace('highly congested', 3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model initialization and fitting
clf = RandomForestClassifier(n_estimators=101)
#clf = Lasso(alpha=0.0004)
#clf = LinearRegression()
#clf = KNeighborsClassifier(n_neighbors=10,weights='distance')
clf.fit(X_train, y_train)


#
# predict the testing data, round() their results and store them into y_pred
# round means 4.6 will be converted into 5 while 4.4 will be converted into 4
# because minutes are not in points and round() yields better results
y_pred = clf.predict(X_test).round()
print(y_pred)

y_score = clf.predict_proba(X_test)


# print root mean squared error by comparing y_pred and y_test
print(np.sqrt(mean_squared_error(y_test, y_pred)))

n_classes = len(set(y_train))

Y = label_binarize(y_train, classes=[*range(n_classes)])


clf = OneVsRestClassifier(RandomForestClassifier(n_estimators=50,
                             max_depth=3,
                             random_state=0))
clf.fit(X_train, y_train)

y_score = clf.predict_proba(X_test)
# test last record in test.csv manually and the answer is correct which is 4 minutes i.e. 240 seconds
print(precision_recall_fscore_support(y_test, y_pred, average='micro'))
print('accuracy score', accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

print(metrics.confusion_matrix(y_test, y_pred))

# Print the precision and recall, among other metrics
print(metrics.classification_report(y_test, y_pred, digits=5))

values = y_test
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)

onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
#precision, recall, thresholds = precision_recall_curve(y_test,y_pred)
## precision recall curve
precision = dict()
recall = dict()
for i in range(5):
    precision[i], recall[i], _ = precision_recall_curve(onehot_encoded[:, i],
                                                        y_score[:, i])
    plt.plot(recall[i], precision[i], lw=5, label='class {}'.format(i))

plt.xlabel("recall")
plt.ylabel("precision")
plt.legend(loc="best")
plt.title("precision vs. recall curve")
plt.show()

#code for saving new entry that is to be tested
def start(self):
    startingLocation = dlg.comboBox.currentText()
    destinationLocation = dlg.comboBox_2.currentText()
    columns_dataframe = ['Date', 'Day', 'Sys_Time', 'Weather', 'Holiday', 'Special_Condition', 'Starting_Location',
                         'Destination_Location', 'Fastest_Route_Name']

    now = datetime.datetime.now()
    day = now.strftime("%A")
    sys_time = strftime("%H:%M:%S")
    date = strftime("%d/%m/%Y")
    
    # weather

    res = requests.get('https://www.yahoo.com/news/weather/pakistan/punjab/rawalpindi-2211387/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    weather = soup.find("span", {"class": "description Va(m) Px(2px) Fz(1.3em)--sm Fz(1.6em)"}).get_text()

    if weather == '':
        weather = 'Sunny'
        
    input_csv1= pd.read_csv('E:/fyp/8th june/Holidays2020-2021.csv')
    df_1 = pd.concat([input_csv1])
    
    for j in range(len(df_1)):
        if date==df_1.Date[j]:
            special=df_1.Holiday[j]
            break
        else:
            special='no'
    if day=='Sunday':
        holiday='yes'
    else:
        holiday='no'
                    
       
        
    fastestRouteName='r'
    temp_dataframe = pd.DataFrame([[date, day, sys_time, weather, holiday, special, startingLocation, destinationLocation,
                        fastestRouteName]], columns = columns_dataframe)

    temp_dataframe.to_csv('NewEntry.csv', index = False)
    dlg.hide()
    data_New = pd.read_csv('E:/fyp/8th june/NewEntry.csv')
    clean_data(data_New)

    X1 = data_New[['Date', 'Day', 'Sys_Time', 'Weather', 'Holiday', 'Special_Condition', 'Starting_Location',
          'Destination_Location', 'Fastest_Route_Name']]
    #y1 = data_New['Data_prediction']
    y_pr = clf.predict(X1).round()
    print(y_pr)
    if y_pr==0:
        display='slightly congested'
    elif y_pr==1:
        display='smooth'
    elif y_pr==2:
        display='blockage'
    elif y_pr==3:
        display='congested'
    elif y_pr==4:
        display='highly congested'
        
    msgBox=QMessageBox()
    msgBox.setText('The traffic from '+startingLocation+' to '+destinationLocation+' is '+display)
    msgBox.setWindowTitle("Prediction")
    msgBox.exec()
    

app = QtWidgets.QApplication([])
dlg = uic.loadUi('test.ui')

dlg.pushButton.clicked.connect(start)

dlg.show()
app.exec()