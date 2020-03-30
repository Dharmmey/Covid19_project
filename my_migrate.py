from my_db_functions import *

file1 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/timeseriescovid19confirmedglobal.csv")
file2 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/timeseriescovid19deathsglobal.csv")
file3 = open("C:/Users/BABATOLA/Documents/Pandemic period/My_covid19/My_covid_data/timeseriescovid19recoveredglobalnarrow.csv")

countries_of_choice = ['Nigeria','Italy','Switzerland','Iran', 'US']
heading = file1.readlines(1)


for line3 in file3.readlines():
    line_data3 = line3.split(",")
    if line_data3[1] in countries_of_choice:
        data_recoveries = line_data3[5:]

for line2 in file2.readlines():
    line_data2 = line2.split(",")
    if line_data2[1] in countries_of_choice:
        data_deaths = line_data2[4:]

for line1 in file1.readlines():
    line_data1 = line1.split(",")
    country_name = line_data1[1]

    
if country_name in countries_of_choice:
    country_exists = check_country(country_name)

    if country_exists:

        for data in list(zip(line_data1[4:], data_deaths, data_recoveries, heading[0].split(",")[4:])):
            write_case(country_exists[0]['id'], data[0], data[1], data[2], format_time(data[3]))

    else:
        write_country(country_name, line_data1[2], line_data1[3])



