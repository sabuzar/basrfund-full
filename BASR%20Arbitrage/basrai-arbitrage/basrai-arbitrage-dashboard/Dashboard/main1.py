from flask import jsonify, request, render_template
from datetime import datetime
import os

from pandas.core.dtypes.common import classes

from main2 import app

from Code.allstatsalgo.averagevaluedifference import calculate_average
from Code.allstatsalgo.Counter2 import get_tables_length
from  Code.algosfor24hoursdata.counter import get_tables_length_last_24_hours
from Code.algosfor24hoursdata.averagepricedifferencein24hours import calculate_average_price_difference_last_24_hours
from Code.algosfor24hoursdata.volumecalculatorfor24hoursdata import perform_calculations_last_24_hours
from Code.allstatsalgo.valuecalclualtor import calculate_value
# # app = Flask(__name__)
#

from Code.allstatsalgo.combo import perform_calculations

def save_current_time(currency_pair):
    file_path = 'currency_times.txt'
    
    # Check if the currency pair already exists in the file
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                saved_currency, _, _ = line.strip().split(',')
                if saved_currency == currency_pair:
                    return
                    # print(f"{currency_pair} is already in the file. No need to insert.")
                #     return  # Exit the function if the currency pair is found
    
    # If the currency pair is not found, save the current date and time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    
    with open(file_path, 'a') as file:
        file.write(f"{currency_pair},{current_date},{current_time}\n")
    # print(f"Saved {currency_pair} with time {current_time} on {current_date}.")

def get_time_from_file(currency_pair):
    file_path = 'currency_times.txt'
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                saved_currency, date, time = line.strip().split(',')
                if saved_currency == currency_pair:
                    return time, date
    
    return f"No time data found for {currency_pair}"

def classify_values(currency_name):
    save_current_time(currency_name)
    if currency_name == "BTCUSDT":
        VC1 = perform_calculations('Bucket99BTC', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket100to200BTC', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket200to300BTC', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket300to400BTC', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket500plusBTC', 'Exchange1BP1V')

        table_names = ['Bucket99BTC', 'Bucket100to200BTC', 'Bucket200to300BTC', 'Bucket300to400BTC', 'Bucket500plusBTC']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket99BTC']
        B2 = lengths['Bucket100to200BTC']
        B3 = lengths['Bucket200to300BTC']
        B4 = lengths['Bucket300to400BTC']
        B5 = lengths['Bucket500plusBTC']

        P1 = calculate_average('Bucket99BTC','Difference')
        P2 = calculate_average('Bucket100to200BTC','Difference')
        P3 = calculate_average('Bucket200to300BTC','Difference')
        P4 = calculate_average('Bucket300to400BTC','Difference')
        P5 = calculate_average('Bucket500plusBTC','Difference')

        classes = {


            "0":B1 ,
            "10": B2,
            "20":B3 ,
            "30":B4,
            "50": B5,

            "1": P1,
            "11": P2,
            "21":P3,
            "31": P4,
            "51": P5,

            "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,(P1) if P1 != "" else 1.0
                                 ,(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,(P2) if P2 != "" else 1.0
                                  ,(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,(P3) if P3 != "" else 1.0
                                  ,(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,(P4) if P4 != "" else 1.0
                                  ,(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    (P5) if P5 != "" else 1.0,
                    (VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 100",
            "57": "101 to 200",
            "58": "201 to 300",
            "59": "301 to 500",
            "60": "Above 500",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']

        }
        return classes
    elif currency_name == "ETHUSDT":
        VC1 = perform_calculations('Bucket5to10ETH', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket10to20ETH', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket20to30ETH', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket30to40ETH', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket50plusETH', 'Exchange1BP1V')
        table_names = ['Bucket5to10ETH', 'Bucket10to20ETH', 'Bucket20to30ETH', 'Bucket30to40ETH', 'Bucket50plusETH']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket5to10ETH']
        B2 = lengths['Bucket10to20ETH']
        B3 = lengths['Bucket20to30ETH']
        B4 = lengths['Bucket30to40ETH']
        B5 = lengths['Bucket50plusETH']
        P1 = calculate_average('Bucket5to10ETH', 'Difference')
        P2 = calculate_average('Bucket10to20ETH', 'Difference')
        P3 = calculate_average('Bucket20to30ETH', 'Difference')
        P4 = calculate_average('Bucket30to40ETH', 'Difference')
        P5 = calculate_average('Bucket50plusETH', 'Difference')
        classes = {

             "0":B1 ,
            "10": B2,
            "20":B3 ,
            "30":B4,
            "50": B5,

            "1": P1,
            "11": P2,
            "21": P3,
            "31": P4,
            "51": P5,

             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,float(P1) if P1 != "" else 1.0
                                 ,float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,float(P2) if P2 != "" else 1.0
                                  ,float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,float(P3) if P3 != "" else 1.0
                                  ,float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,float(P4) if P4 != "" else 1.0
                                  ,float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    float(P5) if P5 != "" else 1.0,
                    float(VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "5 to 10",
            "57": "11 to 20",
            "58": "21 to 30",
            "59": "31 to 50",
            "60": "Above 50",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']

        }
        return classes
    elif currency_name == "BCHUSDT":

        VC1 = perform_calculations('Bucket0to2BCH', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket2to5BCH', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket5to10BCH', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket10to20BCH', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket30plusBCH', 'Exchange1BP1V')
        table_names = ['Bucket0to2BCH', 'Bucket2to5BCH', 'Bucket5to10BCH', 'Bucket10to20BCH', 'Bucket30plusBCH']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket0to2BCH']
        B2 = lengths['Bucket2to5BCH']
        B3 = lengths['Bucket5to10BCH']
        B4 = lengths['Bucket10to20BCH']
        B5 = lengths['Bucket30plusBCH']

        P1 = calculate_average('Bucket0to2BCH', 'Difference')
        P2 = calculate_average('Bucket2to5BCH', 'Difference')
        P3 = calculate_average('Bucket5to10BCH', 'Difference')
        P4 = calculate_average('Bucket10to20BCH', 'Difference')
        P5 = calculate_average('Bucket30plusBCH', 'Difference')
        classes = {

             "0":B1 ,
            "10": B2,
            "20":B3 ,
            "30":B4,
            "50": B5,
            "1": P1,
            "11": P2,
            "21": P3,
            "31":P4,
            "51": P5,

             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,float(P1) if P1 != "" else 1.0
                                 ,float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,float(P2) if P2 != "" else 1.0
                                  ,float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,float(P3) if P3 != "" else 1.0
                                  ,float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,float(P4) if P4 != "" else 1.0
                                  ,float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    float(P5) if P5 != "" else 1.0,
                    float(VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 2",
            "57": "3 to 5",
            "58": "6 to 10",
            "59": "11 to 20",
            "60": "Above 30",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']
        }
        return classes
    elif currency_name == "SOLUSDT":
        VC1 = perform_calculations('Bucket0to2SOL', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket2to5SOL', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket5to10SOL', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket10to20SOL', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket30plusSOL', 'Exchange1BP1V')
        table_names = ['Bucket0to2SOL', 'Bucket2to5SOL', 'Bucket5to10SOL', 'Bucket10to20SOL', 'Bucket30plusSOL']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket0to2SOL']
        B2 = lengths['Bucket2to5SOL']
        B3 = lengths['Bucket5to10SOL']
        B4 = lengths['Bucket10to20SOL']
        B5 = lengths['Bucket30plusSOL']

        P1 = calculate_average('Bucket0to2SOL', 'Difference')
        P2 = calculate_average('Bucket2to5SOL', 'Difference')
        P3 = calculate_average('Bucket5to10SOL', 'Difference')
        P4 = calculate_average('Bucket10to20SOL', 'Difference')
        P5 = calculate_average('Bucket30plusSOL', 'Difference')
        classes = {

            "0": B1,
            "10": B2,
            "20": B3,
            "30": B4,
            "50": B5,
            "1": P1,
            "11": P2,
            "21": P3,
            "31":P4,
            "51": P5,
             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,float(P1) if P1 != "" else 1.0
                                 ,float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,float(P2) if P2 != "" else 1.0
                                  ,float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,float(P3) if P3 != "" else 1.0
                                  ,float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,float(P4) if P4 != "" else 1.0
                                  ,float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    float(P5) if P5 != "" else 1.0,
                    float(VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 2",
            "57": "3 to 5",
            "58": "6 to 10",
            "59": "11 to 20",
            "60": "Above 30",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']
        }
        return classes

def sclassify_values(currency_name):
    save_current_time(currency_name)
    if currency_name == "BTCUSDT":
        VC1 = perform_calculations_last_24_hours('Bucket99BTC', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket100to200BTC', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket200to300BTC', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket300to400BTC', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket500plusBTC', 'Exchange1BP1V')

        table_names = ['Bucket99BTC', 'Bucket100to200BTC', 'Bucket200to300BTC', 'Bucket300to400BTC', 'Bucket500plusBTC']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket99BTC']
        B2 = lengths['Bucket100to200BTC']
        B3 = lengths['Bucket200to300BTC']
        B4 = lengths['Bucket300to400BTC']
        B5 = lengths['Bucket500plusBTC']

        P1=calculate_average_price_difference_last_24_hours('Bucket99BTC')
        P2 = calculate_average_price_difference_last_24_hours('Bucket100to200BTC')
        P3 = calculate_average_price_difference_last_24_hours('Bucket200to300BTC')
        P4 = calculate_average_price_difference_last_24_hours('Bucket300to400BTC')
        P5 = calculate_average_price_difference_last_24_hours('Bucket500plusBTC')


        classes = {


            "0":B1,
            "10": B2,
            "20":B3,
            "30":B4,
            "50": B5,

            "1": P1,
            "11": P2,
            "21": P3,
            "31": P4,
            "51":P5,

            "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                   (P1) if P1 != "" else 1.0
                                 ,(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,(P2) if P2 != "" else 1.0
                                  ,(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,(P3) if P3 != "" else 1.0
                                  ,(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,(P4) if P4 != "" else 1.0
                                  ,(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    (P5) if P5 != "" else 1.0,
                    (VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 100",
            "57": "101 to 200",
            "58": "201 to 300",
            "59": "301 to 500",
            "60": "Above 500",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']

        }
        return classes
    elif currency_name == "ETHUSDT":
        VC1 = perform_calculations_last_24_hours('Bucket5to10ETH', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket10to20ETH', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket20to30ETH', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket30to40ETH', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket50plusETH', 'Exchange1BP1V')
        table_names = ['Bucket5to10ETH', 'Bucket10to20ETH', 'Bucket20to30ETH', 'Bucket30to40ETH', 'Bucket50plusETH']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket5to10ETH']
        B2 = lengths['Bucket10to20ETH']
        B3 = lengths['Bucket20to30ETH']
        B4 = lengths['Bucket30to40ETH']
        B5 = lengths['Bucket50plusETH']

        P1 = calculate_average_price_difference_last_24_hours('Bucket5to10ETH')
        P2 = calculate_average_price_difference_last_24_hours('Bucket10to20ETH')
        P3 = calculate_average_price_difference_last_24_hours('Bucket20to30ETH')
        P4 = calculate_average_price_difference_last_24_hours('Bucket30to40ETH')
        P5 = calculate_average_price_difference_last_24_hours('Bucket50plusETH')
        classes = {

             "0":B1 ,
            "10": B2,
            "20":B3 ,
            "30":B4,
            "50": B5,

            "1": P1,
            "11": P2,
            "21": P3,
            "31": P4,
            "51": P5,

             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13": VC2['median'],
            "23": VC3['median'],
            "33": VC4['median'],
            "53": VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 , float(P1) if P1 != "" else 1.0
                                 , float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  , float(P2) if P2 != "" else 1.0
                                  , float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  , float(P3) if P3 != "" else 1.0
                                  , float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  , float(P4) if P4 != "" else 1.0
                                  , float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                                  float(P5) if P5 != "" else 1.0,
                                  float(VC5['average']) if VC5['average'] != "" else 1.0
                                  ),

            "56": "5 to 10",
            "57": "11 to 20",
            "58": "21 to 30",
            "59": "31 to 50",
            "60": "Above 50",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']

        }
        return classes
    elif currency_name == "BCHUSDT":

        VC1 = perform_calculations_last_24_hours('Bucket0to2BCH', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket2to5BCH', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket5to10BCH', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket10to20BCH', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket30plusBCH', 'Exchange1BP1V')
        table_names = ['Bucket0to2BCH', 'Bucket2to5BCH', 'Bucket5to10BCH', 'Bucket10to20BCH', 'Bucket30plusBCH']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket0to2BCH']
        B2 = lengths['Bucket2to5BCH']
        B3 = lengths['Bucket5to10BCH']
        B4 = lengths['Bucket10to20BCH']
        B5 = lengths['Bucket30plusBCH']
        P1 = calculate_average_price_difference_last_24_hours('Bucket0to2BCH')
        P2 = calculate_average_price_difference_last_24_hours('Bucket2to5BCH')
        P3 = calculate_average_price_difference_last_24_hours('Bucket5to10BCH')
        P4 = calculate_average_price_difference_last_24_hours('Bucket10to20BCH')
        P5 = calculate_average_price_difference_last_24_hours('Bucket30plusBCH')
        classes = {

             "0":B1 ,
            "10": B2,
            "20":B3 ,
            "30":B4,
            "50": B5,
            "1": P1,
            "11": P2,
            "21": P3,
            "31": P4,
            "51": P5,

             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13":VC2['median'],
            "23":VC3['median'],
            "33":VC4['median'],
            "53":VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,float(P1) if P1 != "" else 1.0
                                 ,float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,float(P2) if P2 != "" else 1.0
                                  ,float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,float(P3) if P3 != "" else 1.0
                                  ,float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,float(P4) if P4 != "" else 1.0
                                  ,float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    float(P5) if P5 != "" else 1.0,
                    float(VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 2",
            "57": "3 to 5",
            "58": "6 to 10",
            "59": "11 to 20",
            "60": "Above 30",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']
        }
        return classes
    elif currency_name == "SOLUSDT":
        VC1 = perform_calculations_last_24_hours('Bucket0to2SOL', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket2to5SOL', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket5to10SOL', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket10to20SOL', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket30plusSOL', 'Exchange1BP1V')
        table_names = ['Bucket0to2SOL', 'Bucket2to5SOL', 'Bucket5to10SOL', 'Bucket10to20SOL', 'Bucket30plusSOL']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket0to2SOL']
        B2 = lengths['Bucket2to5SOL']
        B3 = lengths['Bucket5to10SOL']
        B4 = lengths['Bucket10to20SOL']
        B5 = lengths['Bucket30plusSOL']
        P1 = calculate_average_price_difference_last_24_hours('Bucket0to2SOL')
        P2 = calculate_average_price_difference_last_24_hours('Bucket2to5SOL')
        P3 = calculate_average_price_difference_last_24_hours('Bucket5to10SOL')
        P4 = calculate_average_price_difference_last_24_hours('Bucket10to20SOL')
        P5 = calculate_average_price_difference_last_24_hours('Bucket30plusSOL')
        classes = {

            "0": B1,
            "10": B2,
            "20": B3,
            "30": B4,
            "50": B5,
            "1": P1,
            "11": P2,
            "21": P3,
            "31": P4,
            "51": P5,
             "2": VC1['average'],
            "12":VC2['average'],
            "22":VC3['average'],
            "32":VC4['average'],
            "52":VC5['average'],

            "3": VC1['median'],
            "13": VC2['median'],
            "23": VC3['median'],
            "33": VC4['median'],
            "53": VC5['median'],

            "4": VC1['maximum'],
            "14": VC2['maximum'],
            "24": VC3['maximum'],
            "34": VC4['maximum'],
            "54": VC5['maximum'],

            "5": calculate_value(int(B1) if B1 != "" else 1
                                 ,float(P1) if P1 != "" else 1.0
                                 ,float(VC1['average'] if VC1['average'] != "" else 1.0)),
            "15": calculate_value(int(B2) if B2 != "" else 1
                                  ,float(P2) if P2 != "" else 1.0
                                  ,float(VC2['average'] if VC2['average'] != "" else 1.0)),
            "25": calculate_value(int(B3) if B3 != "" else 1
                                  ,float(P3) if P3 != "" else 1.0
                                  ,float(VC3['average'] if VC3['average'] != "" else 1.0)),
            "35": calculate_value(int(B4) if B4 != "" else 1
                                  ,float(P4) if P4 != "" else 1.0
                                  ,float(VC4['average'] if VC4['average'] != "" else 1.0)),
            "55": calculate_value(int(B5) if B5 != "" else 1,
                    float(P5) if P5 != "" else 1.0,
                    float(VC5['average']) if VC5['average'] != "" else 1.0
                        ),
            "56": "0 to 2",
            "57": "3 to 5",
            "58": "6 to 10",
            "59": "11 to 20",
            "60": "Above 30",
            "101":VC1['minimum'],
            "102":VC2['minimum'],
            "103":VC3['minimum'],
            "104":VC4['minimum'],
            "105":VC5['minimum']
        }
        return classes

    
@app.route('/btc')
async def btcmain1():
    return render_template('btcprice.html')

@app.route('/eth')
async def ethmain1():
    return render_template('ethprice.html')

@app.route('/ethbtc')
async def ethbtcmain1():
    return render_template('ethbtcprice.html')

@app.route('/sol')
async def solmain1():
    return render_template('solprice.html')

@app.route('/bch')
async def bchmain1():
    return render_template('bchprice.html')


@app.route('/main2/btc/price')
async def btcpricemain1():
    currency_name = "BTCUSDT"
    # random_values = await generate_random_values(50)
    classified_values = classify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/eth/price')
async def ethpricemain1():
    currency_name = "ETHUSDT"
    # random_values = await generate_random_values(50)
    classified_values = classify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/ethbtc/price')
async def ethbtcpricemain1():
    currency_name = "ETHBTC"
    # random_values = await generate_random_values(50)
    classified_values = classify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/sol/price')
async def solpricemain1():
    currency_name = "SOLUSDT"
    # random_values = await generate_random_values(50)
    classified_values = classify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/bch/price')
async def bchpricemain1():
    currency_name = "BCHUSDT"
    # random_values = await generate_random_values(50)
    classified_values = classify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/btc/price')
async def btcpricemain1s():
    currency_name = "BTCUSDT"
    # random_values = await generate_random_values(50)
    classified_values = sclassify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/eth/price')
async def ethpricemain1s():
    currency_name = "ETHUSDT"
    # random_values = await generate_random_values(50)
    classified_values = sclassify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)


@app.route('/main2s/ethbtc/price')
async def ethbtcpricemain1s():
    currency_name = "ETHBTC"
    # random_values = await generate_random_values(50)
    classified_values = sclassify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/sol/price')
async def solpricemain1s():
    currency_name = "SOLUSDT"
    # random_values = await generate_random_values(50)
    classified_values = sclassify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/bch/price')
async def bchpricemain1s():
    currency_name = "BCHUSDT"
    # random_values = await generate_random_values(50)
    classified_values = sclassify_values(currency_name)
    current_time = get_time_from_file(currency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)