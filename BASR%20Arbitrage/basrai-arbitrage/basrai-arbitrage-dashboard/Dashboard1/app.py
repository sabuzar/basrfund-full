from flask import Flask, jsonify, render_template
import pandas as pd
from collections import OrderedDict
from threading import Thread
import time

# Define the file path
file_path = 'dashboard1.xlsx'  # Replace with your actual file path

try:
    # Try reading the Excel file with openpyxl engine
    df = pd.read_excel(file_path, sheet_name='Sheet1', engine='openpyxl')
except TypeError as e:
    print(f"Error reading Excel file with openpyxl: {e}")
    print("Attempting to re-save the file as CSV to bypass the issue...")

    csv_file_path = 'dashboard1.csv'  # Replace with the path to your saved CSV file
    df = pd.read_csv(csv_file_path)
current_index = 0

app = Flask(__name__)

divvalue = {}

def update_data():
    global current_index
    global Exchange2AP1
    while True:
        if current_index < len(df):
            row = df.iloc[current_index]
            divvalue.update({
                'Exchange1': row[3],
                'Exchange1_LTP': row[4],
                'Exchange1BP1': "{:.2f}".format(row[5]),
                'Exchange1BP1V': "{:.2f}".format(row[6]),
                'Exchange2': row[7],
                'Exchange2_LTP': row[8],
                'Exchange2AP1': "{:.2f}".format(row[9]),
                'Exchange2AP1V': "{:.2f}".format(row[10]),
                'Exchange1BPAC': "{:.2f}".format(row[11]),
                'Exchange1APAC': "{:.2f}".format(row[12]),
                'RealDifference': "{:.2f}".format(row[13])
            });

            # Update table2 with values from divvalue
            table2.update({
                
                'Ask1': divvalue.get('Exchange2AP1', 0),
                'Exchange2AP1V': divvalue.get('Exchange2AP1V', 0)
            })
            table3.update({
                
                'Bid1': divvalue.get('Exchange1BP1', 0),
                'Exchange1BP1V': divvalue.get('Exchange1BP1V',0)
            })
            
            # table3.clear()
            # table3.update({
                
            #     'Exchange1BP1': divvalue.get('Exchange1BP1', 0),
            #     'Ex2A4': 130,
            #     'Ex2A3': 50,
            #     'Ex2A2': -70,
            #     'Ex2A1': 110
            # })
            current_index += 1
        else:
            current_index = 0  # Reset index if it goes out of range
        time.sleep(1)  # Wait for 1 second



table1 =  {
    'Ex1A5': "Ask5",
    'Ex1A4': "Ask4",
    'Ex1A3': "Ask3",
    'Ex1A2': "Ask2",
    'Ex1A1': "Ask1"
}

table2 =  {
    'Ex2A5': "Ask5",
    'Ex2A4': "Ask4",
    'Ex2A3': "Ask3",
    'Ex2A2': "Ask2",
    'Ask1': "Ask1",
    'Exchange2AP1V':0
}
table3={
    'Bid1': 'Ex1B1',
    'Bid2': 'Ex1B2',
    'Bid3': 'Ex1B3',
    'Bid4': 'Ex1B4',
    'Bid5':'Ex1B5',
    'Exchange1BP1V':0
    
}
table4 =  {
    'Bid1': 'Ex1B1',
    'Bid2': 'Ex1B2',
    'Bid3': 'Ex1B3',
    'Bid4': 'Ex1B4',
    'Bid5': 'Ex1B5'
}



@app.route('/')
async def index():
    # Simply return the template without awaiting since render_template is not async
    return render_template('index.html')

@app.route('/data')
async def data():
    # Simulate asynchronous data fetching
    data = await fetch_data()
    return jsonify(data)

async def fetch_data():
    # Replace with your actual async data fetching logic
    return {
        'Ex1A5': -120,
        'Ex1A4': 130,
        'Ex1A3': 50,
        'Ex1A2': -70,
        'Ex1A1': 110
    }
@app.route('/data2')
async def data2():
    # Simply return the template without awaiting since render_template is not async
    return render_template('index2.html')
@app.route('/data21')
async def data21():
    # Simulate asynchronous data fetching
    
    return jsonify(table1=table1, table2=table2, divvalue=divvalue, table3=table3, table4=table4)




if __name__ == '__main__':
    thread = Thread(target=update_data)
    thread.daemon = True
    thread.start()
    app.run(debug=True, port=5001)
