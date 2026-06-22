from flask import Flask, jsonify, render_template, request
import random
import asyncio
from datetime import datetime
import os
import main1
from main1 import app
from Code.pricedifferenceBTC.BTCPriceDifference import main
from Code.pricedifferenceETH.ETHPriceDifference import maineth
from Code.pricedifferenceBCH.BCHPriceDifference import mainbch
from Code.pricedifferenceSOL.SOLPriceDifference import mainsol
from Code.pricedifferenceETHBTC.ETHBTCPriceDifference import mainethbtc
# app = Flask(__name__)
    
@app.route('/')
async def index():
    return render_template('index.html')

@app.route('/btc')
async def btc():
    return render_template('btcprice.html')

@app.route('/eth')
async def eth():
    return render_template('ethprice.html')

@app.route('/sol')
async def sol():
    return render_template('solprice.html')

@app.route('/ethbtc')
async def ethbtc():
    return render_template('ethbtcprice.html')

@app.route('/bch')
async def bch():
    return render_template('bchprice.html')


@app.route('/btc/price')
async def btcprice():
    currency_name = "BTCUSDT"
 
    data = await main()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/eth/price')
async def ethprice():
    currency_name = "ETHUSDT"
    # currency_name = 'BTCUSDT'
    data = await maineth()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/ethbtc/price')
async def ethbtcprice():
    currency_name = "ETHBTC"
    # currency_name = 'BTCUSDT'
    data = await mainethbtc()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/sol/price')
async def solprice():
    currency_name = "SOLUSDT"
    # currency_name = 'BTCUSDT'
    data = await mainsol()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)

@app.route('/bch/price')
async def bchprice():
    currency_name = "BCHUSDT"
    # currency_name = 'BTCUSDT'
    data = await mainbch()
    combined_data = {
        'updated_data': data,
    }
    return jsonify(combined_data)


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8000, debug=True)
    app.run(debug=True)
