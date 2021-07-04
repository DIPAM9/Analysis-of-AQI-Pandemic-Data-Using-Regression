# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


def avg_data_2013():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average

def avg_data_2014():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average
    
def avg_data_2015():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average

def avg_data_2016():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average

def avg_data_2017():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average

def avg_data_2018():
    tempo = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data = rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        tempo += 1
        average.append(avg)
    return average

if __name__ == "__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    plt.plot(range(0, 365), lst2013, label = "2013 Data")
    plt.plot(range(0, 364), lst2014, label = "2014 Data")
    plt.plot(range(0, 365), lst2015, label = "2015 Data")
    plt.plot(range(0, 365), lst2016, label = "2016 Data")
    #plt.plot(range(0, 365), lst2017, label = "2017 Data")
    #plt.plot(range(0, 365), lst2018, label = "2018 Data")

