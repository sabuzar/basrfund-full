from flask import Flask, jsonify, render_template, request
from datetime import datetime
import os


from Code.valuedifferencedashboardBTC.BTCValueDifference import mainvalue
from Code.valuedifferencedashboardETH.ETHValueDifference import mainvalue3
from Code.valuedifferencedashboardSOL.SOLValueDifference import mainvalue4
from Code.valuedifferencedashboardBCH.BCHValueDifference import mainvalue2
from Code.valuedifferencedashboardETHBTC.ETHBTCValueDifference import mainvalue5
from Code.allstatsalgo.averagevaluedifference import calculate_average
from Code.allstatsalgo.Counter2 import get_tables_length
from  Code.algosfor24hoursdata.counter import get_tables_length_last_24_hours
from Code.algosfor24hoursdata.averagepricedifferencein24hours import calculate_average_value_difference_last_24_hours
from Code.algosfor24hoursdata.volumecalculatorfor24hoursdata import perform_calculations_last_24_hours
from Code.allstatsalgo.valuecalclualtor import calculate_value
from Code.allstatsalgo.combo import perform_calculations
app = Flask(__name__)


def save_current_time(currency_pair):
    file_path = 'currency_times.txt'
    
    # Check if the currency pair already exists in the file
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                saved_currency, _, _ = line.strip().split(',')
                if saved_currency == currency_pair:
                    return  # Exit the function if the currency pair is found
    
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
        VC1 = perform_calculations('Bucket99BTCtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket100to200BTCtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket200to300BTCtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket300to400BTCtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket500plusBTCtradeable', 'Exchange1BP1V')

        table_names = ['Bucket99BTCtradeable', 'Bucket100to200BTCtradeable', 'Bucket200to300BTCtradeable', 'Bucket300to400BTCtradeable', 'Bucket500plusBTCtradeable']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket99BTCtradeable']
        B2 = lengths['Bucket100to200BTCtradeable']
        B3 = lengths['Bucket200to300BTCtradeable']
        B4 = lengths['Bucket300to400BTCtradeable']
        B5 = lengths['Bucket500plusBTCtradeable']

        P1 = calculate_average('Bucket99BTCtradeable','RealDifference')
        P2 = calculate_average('Bucket100to200BTCtradeable','RealDifference')
        P3 = calculate_average('Bucket200to300BTCtradeable','RealDifference')
        P4 = calculate_average('Bucket300to400BTCtradeable','RealDifference')
        P5 = calculate_average('Bucket500plusBTCtradeable','RealDifference')

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
        VC1 = perform_calculations('Bucket5to10ETHtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket10to20ETHtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket20to30ETHtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket30to40ETHtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket50plusETHtradeable', 'Exchange1BP1V')
        table_names = ['Bucket5to10ETHtradeable', 'Bucket10to20ETHtradeable', 'Bucket20to30ETHtradeable', 'Bucket30to40ETHtradeable', 'Bucket50plusETHtradeable']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket5to10ETHtradeable']
        B2 = lengths['Bucket10to20ETHtradeable']
        B3 = lengths['Bucket20to30ETHtradeable']
        B4 = lengths['Bucket30to40ETHtradeable']
        B5 = lengths['Bucket50plusETHtradeable']
        P1 = calculate_average('Bucket5to10ETHtradeable', 'RealDifference')
        P2 = calculate_average('Bucket10to20ETHtradeable', 'RealDifference')
        P3 = calculate_average('Bucket20to30ETHtradeable', 'RealDifference')
        P4 = calculate_average('Bucket30to40ETHtradeable', 'RealDifference')
        P5 = calculate_average('Bucket50plusETHtradeable', 'RealDifference')
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

        VC1 = perform_calculations('Bucket0to2BCHtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket2to5BCHtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket5to10BCHtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket10to20BCHtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket30plusBCHtradeable', 'Exchange1BP1V')
        table_names = ['Bucket0to2BCHtradeable', 'Bucket2to5BCHtradeable', 'Bucket5to10BCHtradeable', 'Bucket10to20BCHtradeable', 'Bucket30plusBCHtradeable']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket0to2BCHtradeable']
        B2 = lengths['Bucket2to5BCHtradeable']
        B3 = lengths['Bucket5to10BCHtradeable']
        B4 = lengths['Bucket10to20BCHtradeable']
        B5 = lengths['Bucket30plusBCHtradeable']

        P1 = calculate_average('Bucket0to2BCHtradeable', 'RealDifference')
        P2 = calculate_average('Bucket2to5BCHtradeable', 'RealDifference')
        P3 = calculate_average('Bucket5to10BCHtradeable', 'RealDifference')
        P4 = calculate_average('Bucket10to20BCHtradeable', 'RealDifference')
        P5 = calculate_average('Bucket30plusBCHtradeable', 'RealDifference')
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
        VC1 = perform_calculations('Bucket0to2SOLtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations('Bucket2to5SOLtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations('Bucket5to10SOLtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations('Bucket10to20SOLtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations('Bucket30plusSOLtradeable', 'Exchange1BP1V')
        table_names = ['Bucket0to2SOLtradeable', 'Bucket2to5SOLtradeable', 'Bucket5to10SOLtradeable', 'Bucket10to20SOLtradeable', 'Bucket30plusSOLtradeable']
        lengths = get_tables_length(table_names)
        B1 = lengths['Bucket0to2SOLtradeable']
        B2 = lengths['Bucket2to5SOLtradeable']
        B3 = lengths['Bucket5to10SOLtradeable']
        B4 = lengths['Bucket10to20SOLtradeable']
        B5 = lengths['Bucket30plusSOLtradeable']

        P1 = calculate_average('Bucket0to2SOLtradeable', 'RealDifference')
        P2 = calculate_average('Bucket2to5SOLtradeable', 'RealDifference')
        P3 = calculate_average('Bucket5to10SOLtradeable', 'RealDifference')
        P4 = calculate_average('Bucket10to20SOLtradeable', 'RealDifference')
        P5 = calculate_average('Bucket30plusSOLtradeable', 'RealDifference')
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
        VC1 = perform_calculations_last_24_hours('Bucket99BTCtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket100to200BTCtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket200to300BTCtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket300to400BTCtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket500plusBTCtradeable', 'Exchange1BP1V')

        table_names = ['Bucket99BTCtradeable', 'Bucket100to200BTCtradeable', 'Bucket200to300BTCtradeable', 'Bucket300to400BTCtradeable', 'Bucket500plusBTCtradeable']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket99BTCtradeable']
        B2 = lengths['Bucket100to200BTCtradeable']
        B3 = lengths['Bucket200to300BTCtradeable']
        B4 = lengths['Bucket300to400BTCtradeable']
        B5 = lengths['Bucket500plusBTCtradeable']

        P1=calculate_average_value_difference_last_24_hours('Bucket99BTCtradeable')
        P2 = calculate_average_value_difference_last_24_hours('Bucket100to200BTCtradeable')
        P3 = calculate_average_value_difference_last_24_hours('Bucket200to300BTCtradeable')
        P4 = calculate_average_value_difference_last_24_hours('Bucket300to400BTCtradeable')
        P5 = calculate_average_value_difference_last_24_hours('Bucket500plusBTCtradeable')


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
        VC1 = perform_calculations_last_24_hours('Bucket5to10ETHtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket10to20ETHtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket20to30ETHtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket30to40ETHtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket50plusETHtradeable', 'Exchange1BP1V')
        table_names = ['Bucket5to10ETHtradeable', 'Bucket10to20ETHtradeable', 'Bucket20to30ETHtradeable', 'Bucket30to40ETHtradeable', 'Bucket50plusETHtradeable']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket5to10ETHtradeable']
        B2 = lengths['Bucket10to20ETHtradeable']
        B3 = lengths['Bucket20to30ETHtradeable']
        B4 = lengths['Bucket30to40ETHtradeable']
        B5 = lengths['Bucket50plusETHtradeable']

        P1 = calculate_average_value_difference_last_24_hours('Bucket5to10ETHtradeable')
        P2 = calculate_average_value_difference_last_24_hours('Bucket10to20ETHtradeable')
        P3 = calculate_average_value_difference_last_24_hours('Bucket20to30ETHtradeable')
        P4 = calculate_average_value_difference_last_24_hours('Bucket30to40ETHtradeable')
        P5 = calculate_average_value_difference_last_24_hours('Bucket50plusETHtradeable')
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

        VC1 = perform_calculations_last_24_hours('Bucket0to2BCHtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket2to5BCHtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket5to10BCHtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket10to20BCHtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket30plusBCHtradeable', 'Exchange1BP1V')
        table_names = ['Bucket0to2BCHtradeable', 'Bucket2to5BCHtradeable', 'Bucket5to10BCHtradeable', 'Bucket10to20BCHtradeable', 'Bucket30plusBCHtradeable']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket0to2BCHtradeable']
        B2 = lengths['Bucket2to5BCHtradeable']
        B3 = lengths['Bucket5to10BCHtradeable']
        B4 = lengths['Bucket10to20BCHtradeable']
        B5 = lengths['Bucket30plusBCHtradeable']
        P1 = calculate_average_value_difference_last_24_hours('Bucket0to2BCHtradeable')
        P2 = calculate_average_value_difference_last_24_hours('Bucket2to5BCHtradeable')
        P3 = calculate_average_value_difference_last_24_hours('Bucket5to10BCHtradeable')
        P4 = calculate_average_value_difference_last_24_hours('Bucket10to20BCHtradeable')
        P5 = calculate_average_value_difference_last_24_hours('Bucket30plusBCHtradeable')
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
        VC1 = perform_calculations_last_24_hours('Bucket0to2SOLtradeable', 'Exchange1BP1V')
        VC2 = perform_calculations_last_24_hours('Bucket2to5SOLtradeable', 'Exchange1BP1V')
        VC3 = perform_calculations_last_24_hours('Bucket5to10SOLtradeable', 'Exchange1BP1V')
        VC4 = perform_calculations_last_24_hours('Bucket10to20SOLtradeable', 'Exchange1BP1V')
        VC5 = perform_calculations_last_24_hours('Bucket30plusSOLtradeable', 'Exchange1BP1V')
        table_names = ['Bucket0to2SOLtradeable', 'Bucket2to5SOLtradeable', 'Bucket5to10SOLtradeable', 'Bucket10to20SOLtradeable', 'Bucket30plusSOLtradeable']
        lengths = get_tables_length_last_24_hours(table_names)
        B1 = lengths['Bucket0to2SOLtradeable']
        B2 = lengths['Bucket2to5SOLtradeable']
        B3 = lengths['Bucket5to10SOLtradeable']
        B4 = lengths['Bucket10to20SOLtradeable']
        B5 = lengths['Bucket30plusSOLtradeable']
        P1 = calculate_average_value_difference_last_24_hours('Bucket0to2SOLtradeable')
        P2 = calculate_average_value_difference_last_24_hours('Bucket2to5SOLtradeable')
        P3 = calculate_average_value_difference_last_24_hours('Bucket5to10SOLtradeable')
        P4 = calculate_average_value_difference_last_24_hours('Bucket10to20SOLtradeable')
        P5 = calculate_average_value_difference_last_24_hours('Bucket30plusSOLtradeable')
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


@app.route('/btcvalue')
async def main_btc():

    return render_template('btcvalue.html')
@app.route('/ethvalue')
async def main_eth():
    
    return render_template('ethvalue.html')

@app.route('/ethbtcvalue')
async def main_ethbtc():
   
    return render_template('ethbtcvalue.html')

@app.route('/solvalue')
async def main_sol():
   
    return render_template('solvalue.html')

@app.route('/bchvalue')
async def main_value():

    return render_template('bchvalue.html')

@app.route('/btc/value')
async def main_btcvalue():
    currency_name = 'BTCUSDT'
    data = await mainvalue()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/sol/value')
async def main_solvalue():
    currency_name = 'SOLUSDT'
    data = await mainvalue4()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/ethbtc/value')
async def main_ethbtcvalue():
    currency_name = 'ETHBTC'
    data = await mainvalue5()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/eth/value')
async def main_ethvalue():
    currency_name = 'ETHUSDT'
    data = await mainvalue3()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/bch/value')
async def main_bchvalue():
    currency_name = 'BCHUSDT'
    data = await mainvalue2()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)


@app.route('/main2/btc/value')
async def main2btcvalue():
    curency_name = "BTCUSDT"
    classified_values = classify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/eth/value')
async def main2ethvalue():
    curency_name = "ETHUSDT"
    classified_values = classify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/ethbtc/value')
async def main2ethbtcvalue():
    curency_name = "ETHBTC"
    classified_values = classify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/sol/value')
async def main2solvalue():
    curency_name = "SOLUSDT"
    classified_values = classify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2/bch/value')
async def main2bchvalue():
    curency_name = "BCHUSDT"
    classified_values = classify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/btc/value')
async def main2btcvalues():
    curency_name = "BTCUSDT"
    classified_values = sclassify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/eth/value')
async def main2ethvalues():
    curency_name = "ETHUSDT"
    classified_values = sclassify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/ethbtc/value')
async def main2ethbtcvalues():
    curency_name = "ETHBTC"
    classified_values = sclassify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/sol/value')
async def main2solvalues():
    curency_name = "SOLUSDT"
    classified_values = sclassify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)

@app.route('/main2s/bch/value')
async def main2bchvalues():
    curency_name = "BCHUSDT"
    classified_values = sclassify_values(curency_name)
    current_time = get_time_from_file(curency_name)
    combined_data = {
        
        'classified_values': classified_values,
        'current_time': current_time,
    }
    return jsonify(combined_data)


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
