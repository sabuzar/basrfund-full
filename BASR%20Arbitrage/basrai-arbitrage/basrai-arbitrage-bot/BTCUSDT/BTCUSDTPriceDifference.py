import threading
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio


# from models import checker
from modelsPriceDifference import checker
from BTCUSDTAPIRequest import Data
from BaseAlgorithm import Exchange


"""
BTCUSDT Price Difference Analyzer

This script analyzes the bid-ask price differences for the BTC/USDT trading pair across multiple cryptocurrency exchanges. 
It uses asynchronous programming to process data efficiently and calculates price differences for each exchange.

Key Features:
1. Retrieves bid and ask prices from a pre-populated data structure.
2. Calculates the price differences between bid and ask prices for individual exchanges and across exchanges.
3. Stores results for further analysis or display.

Modules and Classes Used:
- `modelsPriceDifference`: Provides the `checker` function for validation or calculations.
- `BTCUSDTAPIRequest`: Supplies the market data required for analysis.
- `BaseAlgorithm`: Contains the `Exchange` class, which calculates bid-ask differences.

Main Functions:
1. `Bid_Ask1(results, initial_time)`: 
   - Accepts market data for various exchanges in the form of bid and ask prices.
   - Computes price differences within each exchange and between exchanges.
   - Stores and logs results for further use.

Exchanges Supported:
- Binance, Bybit, OKX, Upbit, Kucoin, Bitget, Bitstamp, Gemini, Kraken, Gate.io, HTX, MEXC, and many more.

Dependencies:
- asyncio: Handles asynchronous tasks for concurrent processing.
- `BTCUSDTAPIRequest` and `modelsPriceDifference` for fetching and validating input data.

Usage:
- This script should be executed within an asynchronous event loop.
- Ensure that input data is formatted correctly and passed to the main function.

Note:
- The script is designed to handle large volumes of data, making it suitable for high-frequency trading or arbitrage analysis.
"""



async def Bid_Ask1(results,inital_time):
    start = time.perf_counter_ns()



    # Binance
    BinanceBP1 = results["BinanceBP1"]
    BinanceBP1V = results["BinanceBP1V"]
    BinanceAP1 = results["BinanceAP1"]
    BinanceAP1V = results["BinanceAP1V"]
    BinanceOBT = results["BinanceOBT"]
    BinanceLTP = results["BinanceLTP"]

    # Bybit
    BybitBP1 = results["BybitBP1"]
    BybitBP1V = results["BybitBP1V"]
    BybitAP1 = results["BybitAP1"]
    BybitAP1V = results["BybitAP1V"]
    BybitOBT = results["BybitOBT"]
    BybitLTP = results["BybitLTP"]

    # OKX
    OKXBP1 = results["OKXBP1"]
    OKXBP1V = results["OKXBP1V"]
    OKXAP1 = results["OKXAP1"]
    OKXAP1V = results["OKXAP1V"]
    OKXOBT = results["OKXOBT"]
    OKXLTP = results["OKXLTP"]

    # Upbit
    UpbitBP1 = results["UpbitBP1"]
    UpbitBP1V = results["UpbitBP1V"]
    UpbitAP1 = results["UpbitAP1"]
    UpbitAP1V = results["UpbitAP1V"]
    UpbitOBT = results["UpbitOBT"]
    UpbitLTP = results["UpbitLTP"]

    # Kucoin
    KucoinBP1 = results["KucoinBP1"]
    KucoinBP1V = results["KucoinBP1V"]
    KucoinAP1 = results["KucoinAP1"]
    KucoinAP1V = results["KucoinAP1V"]
    KucoinOBT = results["KucoinOBT"]
    KucoinLTP = results["KucoinLTP"]

    # Bitget
    BitgetBP1 = results["BitgetBP1"]
    BitgetBP1V = results["BitgetBP1V"]
    BitgetAP1 = results["BitgetAP1"]
    BitgetAP1V = results["BitgetAP1V"]
    BitgetOBT = results["BitgetOBT"]
    BitgetLTP = results["BitgetLTP"]

    # Bitstamp
    BitstampBP1 = results["BitstampBP1"]
    BitstampBP1V = results["BitstampBP1V"]
    BitstampAP1 = results["BitstampAP1"]
    BitstampAP1V = results["BitstampAP1V"]
    BitstampOBT = results["BitstampOBT"]
    BitstampLTP = results["BitstampLTP"]

    # Gemini
    GeminiBP1 = results["GeminiBP1"]
    GeminiBP1V = results["GeminiBP1V"]
    GeminiAP1 = results["GeminiAP1"]
    GeminiAP1V = results["GeminiAP1V"]
    GeminiOBT = results["GeminiOBT"]
    GeminiLTP = results["GeminiLTP"]

    # Kraken
    KrakenBP1 = results["KrakenBP1"]
    KrakenBPV1 = results["KrakenBP1V"]
    KrakenAP1 = results["KrakenAP1"]
    KrakenAPV1 = results["KrakenAP1V"]
    KrakenOBT = results["KrakenOBT"]
    KrakenLTP = results["KrakenLTP"]

    # Gateio
    GateioBP1 = results["GateioBP1"]
    GateioBPV1 = results["GateioBP1V"]
    GateioAP1 = results["GateioAP1"]
    GateioAPV1 = results["GateioAP1V"]
    GateioOBT = results["GateioOBT"]
    GateioLTP = results["GateioLTP"]

    # HTX
    HTXBP1 = results["HTXBP1"]
    HTXBP1V = results["HTXBP1V"]
    HTXAP1 = results["HTXAP1"]
    HTXAP1V = results["HTXAP1V"]
    HTXOBT = results["HTXOBT"]
    HTXLTP = results["HTXLTP"]

    # MEXC
    MEXCBP1 = results["MEXCBP1"]
    MEXCBP1V = results["MEXCBP1V"]
    MEXCAP1 = results["MEXCAP1"]
    MEXCAP1V = results["MEXCAP1V"]
    MEXCOBT = results["MEXCOBT"]
    MEXCLTP = results["MEXCLTP"]

    # Lbank
    LbankBP1 = results["LbankBP1"]
    LbankBP1V = results["LbankBP1V"]
    LbankAP1 = results["LbankAP1"]
    LbankAP1V = results["LbankAP1V"]
    LbankOBT = results["LbankOBT"]
    LbankLTP = results["LbankLTP"]

    # Bitmart
    BitmartBP1 = results["BitmartBP1"]
    BitmartBP1V = results["BitmartBP1V"]
    BitmartAP1 = results["BitmartAP1"]
    BitmartAP1V = results["BitmartAP1V"]
    BitmartOBT = results["BitmartOBT"]
    BitmartLTP = results["BitmartLTP"]

    # Deepcoin
    DeepcoinBP1 = results["DeepcoinBP1"]
    DeepcoinBP1V = results["DeepcoinBP1V"]
    DeepcoinAP1 = results["DeepcoinAP1"]
    DeepcoinAP1V = results["DeepcoinAP1V"]
    DeepcoinOBT = results["DeepcoinOBT"]
    DeepcoinLTP = results["DeepcoinLTP"]

    # Bitfinex
    BitfinexBP1 = results["BitfinexBP1"]
    BitfinexBP1V = results["BitfinexBP1V"]
    BitfinexAP1 = results["BitfinexAP1"]
    BitfinexAP1V = results["BitfinexAP1V"]
    BitfinexOBT = results["BitfinexOBT"]
    BitfinexLTP = results["BitfinexLTP"]

    # BingX
    BingXBP1 = results["BingXBP1"]
    BingXBP1V = results["BingXBP1V"]
    BingXAP1 = results["BingXAP1"]
    BingXAP1V = results["BingXAP1V"]
    BingXOBT = results["BingXOBT"]
    BingXLTP = results["BingXLTP"]

    # OrangeX
    OrangeXBP1 = results["OrangeXBP1"]
    OrangeXBP1V = results["OrangeXBP1V"]
    OrangeXAP1 = results["OrangeXAP1"]
    OrangeXAP1V = results["OrangeXAP1V"]
    OrangeXOBT = results["OrangeXOBT"]
    OrangeXLTP = results["OrangeXLTP"]

    # Bitvenus
    BitvenusBP1 = results["BitvenusBP1"]
    BitvenusBP1V = results["BitvenusBP1V"]
    BitvenusAP1 = results["BitvenusAP1"]
    BitvenusAP1V = results["BitvenusAP1V"]
    BitvenusOBT = results["BitvenusOBT"]
    BitvenusLTP = results["BitvenusLTP"]

    # Biconomy
    BiconomyBP1 = results["BiconomyBP1"]
    BiconomyBP1V = results["BiconomyBP1V"]
    BiconomyAP1 = results["BiconomyAP1"]
    BiconomyAP1V = results["BiconomyAP1V"]
    BiconomyOBT = results["BiconomyOBT"]
    BiconomyLTP = results["BiconomyLTP"]

    # XT
    XTBP1 = results["XTBP1"]
    XTBP1V = results["XTBP1V"]
    XTAP1 = results["XTAP1"]
    XTAP1V = results["XTAP1V"]
    XTOBT = results["XTOBT"]
    XTLTP = results["XTLTP"]

    # Bitflyer
    BitflyerBP1 = results["BitflyerBP1"]
    BitflyerBP1V = results["BitflyerBP1V"]
    BitflyerAP1 = results["BitflyerAP1"]
    BitflyerAP1V = results["BitflyerAP1V"]
    BitflyerOBT = results["BitflyerOBT"]
    BitflyerLTP = results["BitflyerLTP"]

    # CoinW
    CoinWBP1 = results["CoinWBP1"]
    CoinWBP1V = results["CoinWBP1V"]
    CoinWAP1 = results["CoinWAP1"]
    CoinWAP1V = results["CoinWAP1V"]
    CoinWOBT = results["CoinWOBT"]
    CoinWLTP = results["CoinWLTP"]

    # Toobit
    ToobitBP1 = results["ToobitBP1"]
    ToobitBP1V = results["ToobitBP1V"]
    ToobitAP1 = results["ToobitAP1"]
    ToobitAP1V = results["ToobitAP1V"]
    ToobitOBT = results["ToobitOBT"]
    ToobitLTP = results["ToobitLTP"]

    # TapBit
    TapbitBP1 = results["TapBitBP1"]
    TapbitBP1V = results["TapBitBP1V"]
    TapbitAP1 = results["TapBitAP1"]
    TapbitAP1V = results["TapBitAP1V"]
    TapbitOBT = results["TapBitOBT"]
    TapbitLTP = results["TapBitLTP"]

    Binance_Status = results['Binance_Status']
    BybitStatus = results['Bybit_Status']
    OKX_Status = results['OKX_Status']
    Upbit_Status = results['Upbit_Status']
    Kucoin_Status = results['Kucoin_Status']
    Bitget_Status = results['Bitget_Status']
    Bitstamp_Status = results['Bitstamp_Status']
    Gemini_Status = results['Gemini_Status']
    Kraken_Status = results['Kraken_Status']
    Gateio_Status = results['Gateio_Status']
    HTX_Status = results['HTX_Status']
    MEXC_Status = results['MEXC_Status']
    Lbank_Status = results['Lbank_Status']
    Bitmart_Status = results['Bitmart_Status']
    Deepcoin_Status = results['Deepcoin_Status']
    Bitfinex_Status = results['Bitfinex_Status']
    BingX_Status = results['BingX_Status']
    OrangeX_Status = results['OrangeX_Status']
    Bitvenus_Status = results['Bitvenus_Status']
    Biconomy_Status = results['Biconomy_Status']
    XT_Status = results['XT_Status']
    Bitflyer_Status = results['Bitflyer_Status']
    CoinW_Status = results['CoinW_Status']
    Toobit_Status = results['Toobit_Status']
    TapBit_Status = results['TapBit_Status']

    bid_prices = {
        "Binance": BinanceBP1,
        "Bybit": BybitBP1,
        "OKX": OKXBP1,
        "Upbit": UpbitBP1,
        "Kucoin": KucoinBP1,
        "Bitget": BitgetBP1,
        "Bitstamp": BitstampBP1,
        "Gemini": GeminiBP1,
        "Kraken": KrakenBP1,
        "Gate.io": GateioBP1,
        "HTX": HTXBP1,
        "MEXC": MEXCBP1,
        "Lbank": LbankBP1,
        "Bitmart": BitmartBP1,
        "Deepcoin": DeepcoinBP1,
        "Bitfinex": BitfinexBP1,
        "BingX": BingXBP1,
        "OrangeX": OrangeXBP1,
        "Bitvenus": BitvenusBP1,
        "Biconomy": BiconomyBP1,
        "XT": XTBP1,
        "Bitflyer": BitflyerBP1,
        "CoinW": CoinWBP1,
        "Toobit": ToobitBP1,
        "TapBit": TapbitBP1
    }

    ask_prices = {
        "Binance": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bybit": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "OKX": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Upbit": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Kucoin": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitget": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitstamp": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Gemini": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Kraken": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Gate.io": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "HTX": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "MEXC": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Lbank": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitmart": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Deepcoin": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitfinex": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "BingX": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "OrangeX": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitvenus": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Biconomy": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "XT": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Bitflyer": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "CoinW": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "Toobit": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        },
        "TapBit": {
            "Binance": BinanceAP1,
            "Bybit": BybitAP1,
            "OKX": OKXAP1,
            "Upbit": UpbitAP1,
            "Kucoin": KucoinAP1,
            "Bitget": BitgetAP1,
            "Bitstamp": BitstampAP1,
            "Gemini": GeminiAP1,
            "Kraken": KrakenAP1,
            "Gate.io": GateioAP1,
            "HTX": HTXAP1,
            "MEXC": MEXCAP1,
            "Lbank": LbankAP1,
            "Bitmart": BitmartAP1,
            "Deepcoin": DeepcoinAP1,
            "Bitfinex": BitfinexAP1,
            "BingX": BingXAP1,
            "OrangeX": OrangeXAP1,
            "Bitvenus": BitvenusAP1,
            "Biconomy": BiconomyAP1,
            "XT": XTAP1,
            "Bitflyer": BitflyerAP1,
            "CoinW": CoinWAP1,
            "Toobit": ToobitAP1,
            "TapBit": TapbitAP1
        }
    }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect differences from all exchanges
    all_differences = {}
    for exchange in exchanges:
        all_differences.update(exchange.get_differences())

    results = {}
    for key, value in all_differences.items():
        results[key] = value

    # Print stored variables
    for key in sorted(results.keys()):
        results[key]

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_Gate.ioAP']
    BinanceBP_HTXAP = results['BinanceBP_HTXAP']
    BinanceBP_MEXCAP = results['BinanceBP_MEXCAP']
    BinanceBP_LbankAP = results['BinanceBP_LbankAP']
    BinanceBP_BitmartAP = results['BinanceBP_BitmartAP']
    BinanceBP_DeepcoinAP = results['BinanceBP_DeepcoinAP']
    BinanceBP_BitfinexAP = results['BinanceBP_BitfinexAP']
    BinanceBP_BingXAP = results['BinanceBP_BingXAP']
    BinanceBP_OrangeXAP = results['BinanceBP_OrangeXAP']
    BinanceBP_BitvenusAP = results['BinanceBP_BitvenusAP']
    BinanceBP_BiconomyAP = results['BinanceBP_BiconomyAP']
    BinanceBP_XTAP = results['BinanceBP_XTAP']
    BinanceBP_BitflyerAP = results['BinanceBP_BitflyerAP']
    BinanceBP_CoinWAP = results['BinanceBP_CoinWAP']
    BinanceBP_ToobitAP = results['BinanceBP_ToobitAP']
    BinanceBP_TapBitAP = results['BinanceBP_TapBitAP']

    BybitBP_BinanceAP = results['BybitBP_BinanceAP']
    BybitBP_BybitAP = results['BybitBP_BybitAP']
    BybitBP_OKXAP = results['BybitBP_OKXAP']
    BybitBP_UpbitAP = results['BybitBP_UpbitAP']
    BybitBP_KucoinAP = results['BybitBP_KucoinAP']
    BybitBP_BitgetAP = results['BybitBP_BitgetAP']
    BybitBP_BitstampAP = results['BybitBP_BitstampAP']
    BybitBP_GeminiAP = results['BybitBP_GeminiAP']
    BybitBP_KrakenAP = results['BybitBP_KrakenAP']
    BybitBP_GateioAP = results['BybitBP_Gate.ioAP']
    BybitBP_HTXAP = results['BybitBP_HTXAP']
    BybitBP_MEXCAP = results['BybitBP_MEXCAP']
    BybitBP_LbankAP = results['BybitBP_LbankAP']
    BybitBP_BitmartAP = results['BybitBP_BitmartAP']
    BybitBP_DeepcoinAP = results['BybitBP_DeepcoinAP']
    BybitBP_BitfinexAP = results['BybitBP_BitfinexAP']
    BybitBP_BingXAP = results['BybitBP_BingXAP']
    BybitBP_OrangeXAP = results['BybitBP_OrangeXAP']
    BybitBP_BitvenusAP = results['BybitBP_BitvenusAP']
    BybitBP_BiconomyAP = results['BybitBP_BiconomyAP']
    BybitBP_XTAP = results['BybitBP_XTAP']
    BybitBP_BitflyerAP = results['BybitBP_BitflyerAP']
    BybitBP_CoinWAP = results['BybitBP_CoinWAP']
    BybitBP_ToobitAP = results['BybitBP_ToobitAP']
    BybitBP_TapBitAP = results['BybitBP_TapBitAP']

    OKXBP_BinanceAP = results['OKXBP_BinanceAP']
    OKXBP_BybitAP = results['OKXBP_BybitAP']
    OKXBP_OKXAP = results['OKXBP_OKXAP']
    OKXBP_UpbitAP = results['OKXBP_UpbitAP']
    OKXBP_KucoinAP = results['OKXBP_KucoinAP']
    OKXBP_BitgetAP = results['OKXBP_BitgetAP']
    OKXBP_BitstampAP = results['OKXBP_BitstampAP']
    OKXBP_GeminiAP = results['OKXBP_GeminiAP']
    OKXBP_KrakenAP = results['OKXBP_KrakenAP']
    OKXBP_GateioAP = results['OKXBP_Gate.ioAP']
    OKXBP_HTXAP = results['OKXBP_HTXAP']
    OKXBP_MEXCAP = results['OKXBP_MEXCAP']
    OKXBP_LbankAP = results['OKXBP_LbankAP']
    OKXBP_BitmartAP = results['OKXBP_BitmartAP']
    OKXBP_DeepcoinAP = results['OKXBP_DeepcoinAP']
    OKXBP_BitfinexAP = results['OKXBP_BitfinexAP']
    OKXBP_BingXAP = results['OKXBP_BingXAP']
    OKXBP_OrangeXAP = results['OKXBP_OrangeXAP']
    OKXBP_BitvenusAP = results['OKXBP_BitvenusAP']
    OKXBP_BiconomyAP = results['OKXBP_BiconomyAP']
    OKXBP_XTAP = results['OKXBP_XTAP']
    OKXBP_BitflyerAP = results['OKXBP_BitflyerAP']
    OKXBP_CoinWAP = results['OKXBP_CoinWAP']
    OKXBP_ToobitAP = results['OKXBP_ToobitAP']
    OKXBP_TapBitAP = results['OKXBP_TapBitAP']

    UpbitBP_BinanceAP = results['UpbitBP_BinanceAP']
    UpbitBP_BybitAP = results['UpbitBP_BybitAP']
    UpbitBP_OKXAP = results['UpbitBP_OKXAP']
    UpbitBP_UpbitAP = results['UpbitBP_UpbitAP']
    UpbitBP_KucoinAP = results['UpbitBP_KucoinAP']
    UpbitBP_BitgetAP = results['UpbitBP_BitgetAP']
    UpbitBP_BitstampAP = results['UpbitBP_BitstampAP']
    UpbitBP_GeminiAP = results['UpbitBP_GeminiAP']
    UpbitBP_KrakenAP = results['UpbitBP_KrakenAP']
    UpbitBP_GateioAP = results['UpbitBP_Gate.ioAP']
    UpbitBP_HTXAP = results['UpbitBP_HTXAP']
    UpbitBP_MEXCAP = results['UpbitBP_MEXCAP']
    UpbitBP_LbankAP = results['UpbitBP_LbankAP']
    UpbitBP_BitmartAP = results['UpbitBP_BitmartAP']
    UpbitBP_DeepcoinAP = results['UpbitBP_DeepcoinAP']
    UpbitBP_BitfinexAP = results['UpbitBP_BitfinexAP']
    UpbitBP_BingXAP = results['UpbitBP_BingXAP']
    UpbitBP_OrangeXAP = results['UpbitBP_OrangeXAP']
    UpbitBP_BitvenusAP = results['UpbitBP_BitvenusAP']
    UpbitBP_BiconomyAP = results['UpbitBP_BiconomyAP']
    UpbitBP_XTAP = results['UpbitBP_XTAP']
    UpbitBP_BitflyerAP = results['UpbitBP_BitflyerAP']
    UpbitBP_CoinWAP = results['UpbitBP_CoinWAP']
    UpbitBP_ToobitAP = results['UpbitBP_ToobitAP']
    UpbitBP_TapBitAP = results['UpbitBP_TapBitAP']

    KucoinBP_BinanceAP = results['KucoinBP_BinanceAP']
    KucoinBP_BybitAP = results['KucoinBP_BybitAP']
    KucoinBP_OKXAP = results['KucoinBP_OKXAP']
    KucoinBP_UpbitAP = results['KucoinBP_UpbitAP']
    KucoinBP_KucoinAP = results['KucoinBP_KucoinAP']
    KucoinBP_BitgetAP = results['KucoinBP_BitgetAP']
    KucoinBP_BitstampAP = results['KucoinBP_BitstampAP']
    KucoinBP_GeminiAP = results['KucoinBP_GeminiAP']
    KucoinBP_KrakenAP = results['KucoinBP_KrakenAP']
    KucoinBP_GateioAP = results['KucoinBP_Gate.ioAP']
    KucoinBP_HTXAP = results['KucoinBP_HTXAP']
    KucoinBP_MEXCAP = results['KucoinBP_MEXCAP']
    KucoinBP_LbankAP = results['KucoinBP_LbankAP']
    KucoinBP_BitmartAP = results['KucoinBP_BitmartAP']
    KucoinBP_DeepcoinAP = results['KucoinBP_DeepcoinAP']
    KucoinBP_BitfinexAP = results['KucoinBP_BitfinexAP']
    KucoinBP_BingXAP = results['KucoinBP_BingXAP']
    KucoinBP_OrangeXAP = results['KucoinBP_OrangeXAP']
    KucoinBP_BitvenusAP = results['KucoinBP_BitvenusAP']
    KucoinBP_BiconomyAP = results['KucoinBP_BiconomyAP']
    KucoinBP_XTAP = results['KucoinBP_XTAP']
    KucoinBP_BitflyerAP = results['KucoinBP_BitflyerAP']
    KucoinBP_CoinWAP = results['KucoinBP_CoinWAP']
    KucoinBP_ToobitAP = results['KucoinBP_ToobitAP']
    KucoinBP_TapBitAP = results['KucoinBP_TapBitAP']

    BitgetBP_BinanceAP = results['BitgetBP_BinanceAP']
    BitgetBP_BybitAP = results['BitgetBP_BybitAP']
    BitgetBP_OKXAP = results['BitgetBP_OKXAP']
    BitgetBP_UpbitAP = results['BitgetBP_UpbitAP']
    BitgetBP_KucoinAP = results['BitgetBP_KucoinAP']
    BitgetBP_BitgetAP = results['BitgetBP_BitgetAP']
    BitgetBP_BitstampAP = results['BitgetBP_BitstampAP']
    BitgetBP_GeminiAP = results['BitgetBP_GeminiAP']
    BitgetBP_KrakenAP = results['BitgetBP_KrakenAP']
    BitgetBP_GateioAP = results['BitgetBP_Gate.ioAP']
    BitgetBP_HTXAP = results['BitgetBP_HTXAP']
    BitgetBP_MEXCAP = results['BitgetBP_MEXCAP']
    BitgetBP_LbankAP = results['BitgetBP_LbankAP']
    BitgetBP_BitmartAP = results['BitgetBP_BitmartAP']
    BitgetBP_DeepcoinAP = results['BitgetBP_DeepcoinAP']
    BitgetBP_BitfinexAP = results['BitgetBP_BitfinexAP']
    BitgetBP_BingXAP = results['BitgetBP_BingXAP']
    BitgetBP_OrangeXAP = results['BitgetBP_OrangeXAP']
    BitgetBP_BitvenusAP = results['BitgetBP_BitvenusAP']
    BitgetBP_BiconomyAP = results['BitgetBP_BiconomyAP']
    BitgetBP_XTAP = results['BitgetBP_XTAP']
    BitgetBP_BitflyerAP = results['BitgetBP_BitflyerAP']
    BitgetBP_CoinWAP = results['BitgetBP_CoinWAP']
    BitgetBP_ToobitAP = results['BitgetBP_ToobitAP']
    BitgetBP_TapBitAP = results['BitgetBP_TapBitAP']

    BitstampBP_BinanceAP = results['BitstampBP_BinanceAP']
    BitstampBP_BybitAP = results['BitstampBP_BybitAP']
    BitstampBP_OKXAP = results['BitstampBP_OKXAP']
    BitstampBP_UpbitAP = results['BitstampBP_UpbitAP']
    BitstampBP_KucoinAP = results['BitstampBP_KucoinAP']
    BitstampBP_BitgetAP = results['BitstampBP_BitgetAP']
    BitstampBP_BitstampAP = results['BitstampBP_BitstampAP']
    BitstampBP_GeminiAP = results['BitstampBP_GeminiAP']
    BitstampBP_KrakenAP = results['BitstampBP_KrakenAP']
    BitstampBP_GateioAP = results['BitstampBP_Gate.ioAP']
    BitstampBP_HTXAP = results['BitstampBP_HTXAP']
    BitstampBP_MEXCAP = results['BitstampBP_MEXCAP']
    BitstampBP_LbankAP = results['BitstampBP_LbankAP']
    BitstampBP_BitmartAP = results['BitstampBP_BitmartAP']
    BitstampBP_DeepcoinAP = results['BitstampBP_DeepcoinAP']
    BitstampBP_BitfinexAP = results['BitstampBP_BitfinexAP']
    BitstampBP_BingXAP = results['BitstampBP_BingXAP']
    BitstampBP_OrangeXAP = results['BitstampBP_OrangeXAP']
    BitstampBP_BitvenusAP = results['BitstampBP_BitvenusAP']
    BitstampBP_BiconomyAP = results['BitstampBP_BiconomyAP']
    BitstampBP_XTAP = results['BitstampBP_XTAP']
    BitstampBP_BitflyerAP = results['BitstampBP_BitflyerAP']
    BitstampBP_CoinWAP = results['BitstampBP_CoinWAP']
    BitstampBP_ToobitAP = results['BitstampBP_ToobitAP']
    BitstampBP_TapBitAP = results['BitstampBP_TapBitAP']

    GeminiBP_BinanceAP = results['GeminiBP_BinanceAP']
    GeminiBP_BybitAP = results['GeminiBP_BybitAP']
    GeminiBP_OKXAP = results['GeminiBP_OKXAP']
    GeminiBP_UpbitAP = results['GeminiBP_UpbitAP']
    GeminiBP_KucoinAP = results['GeminiBP_KucoinAP']
    GeminiBP_BitgetAP = results['GeminiBP_BitgetAP']
    GeminiBP_BitstampAP = results['GeminiBP_BitstampAP']
    GeminiBP_GeminiAP = results['GeminiBP_GeminiAP']
    GeminiBP_KrakenAP = results['GeminiBP_KrakenAP']
    GeminiBP_GateioAP = results['GeminiBP_Gate.ioAP']
    GeminiBP_HTXAP = results['GeminiBP_HTXAP']
    GeminiBP_MEXCAP = results['GeminiBP_MEXCAP']
    GeminiBP_LbankAP = results['GeminiBP_LbankAP']
    GeminiBP_BitmartAP = results['GeminiBP_BitmartAP']
    GeminiBP_DeepcoinAP = results['GeminiBP_DeepcoinAP']
    GeminiBP_BitfinexAP = results['GeminiBP_BitfinexAP']
    GeminiBP_BingXAP = results['GeminiBP_BingXAP']
    GeminiBP_OrangeXAP = results['GeminiBP_OrangeXAP']
    GeminiBP_BitvenusAP = results['GeminiBP_BitvenusAP']
    GeminiBP_BiconomyAP = results['GeminiBP_BiconomyAP']
    GeminiBP_XTAP = results['GeminiBP_XTAP']
    GeminiBP_BitflyerAP = results['GeminiBP_BitflyerAP']
    GeminiBP_CoinWAP = results['GeminiBP_CoinWAP']
    GeminiBP_ToobitAP = results['GeminiBP_ToobitAP']
    GeminiBP_TapBitAP = results['GeminiBP_TapBitAP']

    KrakenBP_BinanceAP = results['KrakenBP_BinanceAP']
    KrakenBP_BybitAP = results['KrakenBP_BybitAP']
    KrakenBP_OKXAP = results['KrakenBP_OKXAP']
    KrakenBP_UpbitAP = results['KrakenBP_UpbitAP']
    KrakenBP_KucoinAP = results['KrakenBP_KucoinAP']
    KrakenBP_BitgetAP = results['KrakenBP_BitgetAP']
    KrakenBP_BitstampAP = results['KrakenBP_BitstampAP']
    KrakenBP_GeminiAP = results['KrakenBP_GeminiAP']
    KrakenBP_KrakenAP = results['KrakenBP_KrakenAP']
    KrakenBP_GateioAP = results['KrakenBP_Gate.ioAP']
    KrakenBP_HTXAP = results['KrakenBP_HTXAP']
    KrakenBP_MEXCAP = results['KrakenBP_MEXCAP']
    KrakenBP_LbankAP = results['KrakenBP_LbankAP']
    KrakenBP_BitmartAP = results['KrakenBP_BitmartAP']
    KrakenBP_DeepcoinAP = results['KrakenBP_DeepcoinAP']
    KrakenBP_BitfinexAP = results['KrakenBP_BitfinexAP']
    KrakenBP_BingXAP = results['KrakenBP_BingXAP']
    KrakenBP_OrangeXAP = results['KrakenBP_OrangeXAP']
    KrakenBP_BitvenusAP = results['KrakenBP_BitvenusAP']
    KrakenBP_BiconomyAP = results['KrakenBP_BiconomyAP']
    KrakenBP_XTAP = results['KrakenBP_XTAP']
    KrakenBP_BitflyerAP = results['KrakenBP_BitflyerAP']
    KrakenBP_CoinWAP = results['KrakenBP_CoinWAP']
    KrakenBP_ToobitAP = results['KrakenBP_ToobitAP']
    KrakenBP_TapBitAP = results['KrakenBP_TapBitAP']

    GateioBP_BinanceAP = results['Gate.ioBP_BinanceAP']
    GateioBP_BybitAP = results['Gate.ioBP_BybitAP']
    GateioBP_OKXAP = results['Gate.ioBP_OKXAP']
    GateioBP_UpbitAP = results['Gate.ioBP_UpbitAP']
    GateioBP_KucoinAP = results['Gate.ioBP_KucoinAP']
    GateioBP_BitgetAP = results['Gate.ioBP_BitgetAP']
    GateioBP_BitstampAP = results['Gate.ioBP_BitstampAP']
    GateioBP_GeminiAP = results['Gate.ioBP_GeminiAP']
    GateioBP_KrakenAP = results['Gate.ioBP_KrakenAP']
    GateioBP_GateioAP = results['Gate.ioBP_Gate.ioAP']
    GateioBP_HTXAP = results['Gate.ioBP_HTXAP']
    GateioBP_MEXCAP = results['Gate.ioBP_MEXCAP']
    GateioBP_LbankAP = results['Gate.ioBP_LbankAP']
    GateioBP_BitmartAP = results['Gate.ioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['Gate.ioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['Gate.ioBP_BitfinexAP']
    GateioBP_BingXAP = results['Gate.ioBP_BingXAP']
    GateioBP_OrangeXAP = results['Gate.ioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['Gate.ioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['Gate.ioBP_BiconomyAP']
    GateioBP_XTAP = results['Gate.ioBP_XTAP']
    GateioBP_BitflyerAP = results['Gate.ioBP_BitflyerAP']
    GateioBP_CoinWAP = results['Gate.ioBP_CoinWAP']
    GateioBP_ToobitAP = results['Gate.ioBP_ToobitAP']
    GateioBP_TapBitAP = results['Gate.ioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_Gate.ioAP']
    HTXBP_HTXAP = results['HTXBP_HTXAP']
    HTXBP_MEXCAP = results['HTXBP_MEXCAP']
    HTXBP_LbankAP = results['HTXBP_LbankAP']
    HTXBP_BitmartAP = results['HTXBP_BitmartAP']
    HTXBP_DeepcoinAP = results['HTXBP_DeepcoinAP']
    HTXBP_BitfinexAP = results['HTXBP_BitfinexAP']
    HTXBP_BingXAP = results['HTXBP_BingXAP']
    HTXBP_OrangeXAP = results['HTXBP_OrangeXAP']
    HTXBP_BitvenusAP = results['HTXBP_BitvenusAP']
    HTXBP_BiconomyAP = results['HTXBP_BiconomyAP']
    HTXBP_XTAP = results['HTXBP_XTAP']
    HTXBP_BitflyerAP = results['HTXBP_BitflyerAP']
    HTXBP_CoinWAP = results['HTXBP_CoinWAP']
    HTXBP_ToobitAP = results['HTXBP_ToobitAP']
    HTXBP_TapBitAP = results['HTXBP_TapBitAP']

    MEXCBP_BinanceAP = results['MEXCBP_BinanceAP']
    MEXCBP_BybitAP = results['MEXCBP_BybitAP']
    MEXCBP_OKXAP = results['MEXCBP_OKXAP']
    MEXCBP_UpbitAP = results['MEXCBP_UpbitAP']
    MEXCBP_KucoinAP = results['MEXCBP_KucoinAP']
    MEXCBP_BitgetAP = results['MEXCBP_BitgetAP']
    MEXCBP_BitstampAP = results['MEXCBP_BitstampAP']
    MEXCBP_GeminiAP = results['MEXCBP_GeminiAP']
    MEXCBP_KrakenAP = results['MEXCBP_KrakenAP']
    MEXCBP_GateioAP = results['BinanceBP_Gate.ioAP']
    MEXCBP_HTXAP = results['MEXCBP_HTXAP']
    MEXCBP_MEXCAP = results['MEXCBP_MEXCAP']
    MEXCBP_LbankAP = results['MEXCBP_LbankAP']
    MEXCBP_BitmartAP = results['MEXCBP_BitmartAP']
    MEXCBP_DeepcoinAP = results['MEXCBP_DeepcoinAP']
    MEXCBP_BitfinexAP = results['MEXCBP_BitfinexAP']
    MEXCBP_BingXAP = results['MEXCBP_BingXAP']
    MEXCBP_OrangeXAP = results['MEXCBP_OrangeXAP']
    MEXCBP_BitvenusAP = results['MEXCBP_BitvenusAP']
    MEXCBP_BiconomyAP = results['MEXCBP_BiconomyAP']
    MEXCBP_XTAP = results['MEXCBP_XTAP']
    MEXCBP_BitflyerAP = results['MEXCBP_BitflyerAP']
    MEXCBP_CoinWAP = results['MEXCBP_CoinWAP']
    MEXCBP_ToobitAP = results['MEXCBP_ToobitAP']
    MEXCBP_TapBitAP = results['MEXCBP_TapBitAP']

    LbankBP_BinanceAP = results['LbankBP_BinanceAP']
    LbankBP_BybitAP = results['LbankBP_BybitAP']
    LbankBP_OKXAP = results['LbankBP_OKXAP']
    LbankBP_UpbitAP = results['LbankBP_UpbitAP']
    LbankBP_KucoinAP = results['LbankBP_KucoinAP']
    LbankBP_BitgetAP = results['LbankBP_BitgetAP']
    LbankBP_BitstampAP = results['LbankBP_BitstampAP']
    LbankBP_GeminiAP = results['LbankBP_GeminiAP']
    LbankBP_KrakenAP = results['LbankBP_KrakenAP']
    LbankBP_GateioAP = results['LbankBP_Gate.ioAP']
    LbankBP_HTXAP = results['LbankBP_HTXAP']
    LbankBP_MEXCAP = results['LbankBP_MEXCAP']
    LbankBP_LbankAP = results['LbankBP_LbankAP']
    LbankBP_BitmartAP = results['LbankBP_BitmartAP']
    LbankBP_DeepcoinAP = results['LbankBP_DeepcoinAP']
    LbankBP_BitfinexAP = results['LbankBP_BitfinexAP']
    LbankBP_BingXAP = results['LbankBP_BingXAP']
    LbankBP_OrangeXAP = results['LbankBP_OrangeXAP']
    LbankBP_BitvenusAP = results['LbankBP_BitvenusAP']
    LbankBP_BiconomyAP = results['LbankBP_BiconomyAP']
    LbankBP_XTAP = results['LbankBP_XTAP']
    LbankBP_BitflyerAP = results['LbankBP_BitflyerAP']
    LbankBP_CoinWAP = results['LbankBP_CoinWAP']
    LbankBP_ToobitAP = results['LbankBP_ToobitAP']
    LbankBP_TapBitAP = results['LbankBP_TapBitAP']

    BitmartBP_BinanceAP = results['BitmartBP_BinanceAP']
    BitmartBP_BybitAP = results['BitmartBP_BybitAP']
    BitmartBP_OKXAP = results['BitmartBP_OKXAP']
    BitmartBP_UpbitAP = results['BitmartBP_UpbitAP']
    BitmartBP_KucoinAP = results['BitmartBP_KucoinAP']
    BitmartBP_BitgetAP = results['BitmartBP_BitgetAP']
    BitmartBP_BitstampAP = results['BitmartBP_BitstampAP']
    BitmartBP_GeminiAP = results['BitmartBP_GeminiAP']
    BitmartBP_KrakenAP = results['BitmartBP_KrakenAP']
    BitmartBP_GateioAP = results['BitmartBP_Gate.ioAP']
    BitmartBP_HTXAP = results['BitmartBP_HTXAP']
    BitmartBP_MEXCAP = results['BitmartBP_MEXCAP']
    BitmartBP_LbankAP = results['BitmartBP_LbankAP']
    BitmartBP_BitmartAP = results['BitmartBP_BitmartAP']
    BitmartBP_DeepcoinAP = results['BitmartBP_DeepcoinAP']
    BitmartBP_BitfinexAP = results['BitmartBP_BitfinexAP']
    BitmartBP_BingXAP = results['BitmartBP_BingXAP']
    BitmartBP_OrangeXAP = results['BitmartBP_OrangeXAP']
    BitmartBP_BitvenusAP = results['BitmartBP_BitvenusAP']
    BitmartBP_BiconomyAP = results['BitmartBP_BiconomyAP']
    BitmartBP_XTAP = results['BitmartBP_XTAP']
    BitmartBP_BitflyerAP = results['BitmartBP_BitflyerAP']
    BitmartBP_CoinWAP = results['BitmartBP_CoinWAP']
    BitmartBP_ToobitAP = results['BitmartBP_ToobitAP']
    BitmartBP_TapBitAP = results['BitmartBP_TapBitAP']

    DeepcoinBP_BinanceAP = results['DeepcoinBP_BinanceAP']
    DeepcoinBP_BybitAP = results['DeepcoinBP_BybitAP']
    DeepcoinBP_OKXAP = results['DeepcoinBP_OKXAP']
    DeepcoinBP_UpbitAP = results['DeepcoinBP_UpbitAP']
    DeepcoinBP_KucoinAP = results['DeepcoinBP_KucoinAP']
    DeepcoinBP_BitgetAP = results['DeepcoinBP_BitgetAP']
    DeepcoinBP_BitstampAP = results['DeepcoinBP_BitstampAP']
    DeepcoinBP_GeminiAP = results['DeepcoinBP_GeminiAP']
    DeepcoinBP_KrakenAP = results['DeepcoinBP_KrakenAP']
    DeepcoinBP_GateioAP = results['DeepcoinBP_Gate.ioAP']
    DeepcoinBP_HTXAP = results['DeepcoinBP_HTXAP']
    DeepcoinBP_MEXCAP = results['DeepcoinBP_MEXCAP']
    DeepcoinBP_LbankAP = results['DeepcoinBP_LbankAP']
    DeepcoinBP_BitmartAP = results['DeepcoinBP_BitmartAP']
    DeepcoinBP_DeepcoinAP = results['DeepcoinBP_DeepcoinAP']
    DeepcoinBP_BitfinexAP = results['DeepcoinBP_BitfinexAP']
    DeepcoinBP_BingXAP = results['DeepcoinBP_BingXAP']
    DeepcoinBP_OrangeXAP = results['DeepcoinBP_OrangeXAP']
    DeepcoinBP_BitvenusAP = results['DeepcoinBP_BitvenusAP']
    DeepcoinBP_BiconomyAP = results['DeepcoinBP_BiconomyAP']
    DeepcoinBP_XTAP = results['DeepcoinBP_XTAP']
    DeepcoinBP_BitflyerAP = results['DeepcoinBP_BitflyerAP']
    DeepcoinBP_CoinWAP = results['DeepcoinBP_CoinWAP']
    DeepcoinBP_ToobitAP = results['DeepcoinBP_ToobitAP']
    DeepcoinBP_TapBitAP = results['DeepcoinBP_TapBitAP']

    BitfinexBP_BinanceAP = results['BitfinexBP_BinanceAP']
    BitfinexBP_BybitAP = results['BitfinexBP_BybitAP']
    BitfinexBP_OKXAP = results['BitfinexBP_OKXAP']
    BitfinexBP_UpbitAP = results['BitfinexBP_UpbitAP']
    BitfinexBP_KucoinAP = results['BitfinexBP_KucoinAP']
    BitfinexBP_BitgetAP = results['BitfinexBP_BitgetAP']
    BitfinexBP_BitstampAP = results['BitfinexBP_BitstampAP']
    BitfinexBP_GeminiAP = results['BitfinexBP_GeminiAP']
    BitfinexBP_KrakenAP = results['BitfinexBP_KrakenAP']
    BitfinexBP_GateioAP = results['BitfinexBP_Gate.ioAP']
    BitfinexBP_HTXAP = results['BitfinexBP_HTXAP']
    BitfinexBP_MEXCAP = results['BitfinexBP_MEXCAP']
    BitfinexBP_LbankAP = results['BitfinexBP_LbankAP']
    BitfinexBP_BitmartAP = results['BitfinexBP_BitmartAP']
    BitfinexBP_DeepcoinAP = results['BitfinexBP_DeepcoinAP']
    BitfinexBP_BitfinexAP = results['BitfinexBP_BitfinexAP']
    BitfinexBP_BingXAP = results['BitfinexBP_BingXAP']
    BitfinexBP_OrangeXAP = results['BitfinexBP_OrangeXAP']
    BitfinexBP_BitvenusAP = results['BitfinexBP_BitvenusAP']
    BitfinexBP_BiconomyAP = results['BitfinexBP_BiconomyAP']
    BitfinexBP_XTAP = results['BitfinexBP_XTAP']
    BitfinexBP_BitflyerAP = results['BitfinexBP_BitflyerAP']
    BitfinexBP_CoinWAP = results['BitfinexBP_CoinWAP']
    BitfinexBP_ToobitAP = results['BitfinexBP_ToobitAP']
    BitfinexBP_TapBitAP = results['BitfinexBP_TapBitAP']

    BingXBP_BinanceAP = results['BingXBP_BinanceAP']
    BingXBP_BybitAP = results['BingXBP_BybitAP']
    BingXBP_OKXAP = results['BingXBP_OKXAP']
    BingXBP_UpbitAP = results['BingXBP_UpbitAP']
    BingXBP_KucoinAP = results['BingXBP_KucoinAP']
    BingXBP_BitgetAP = results['BingXBP_BitgetAP']
    BingXBP_BitstampAP = results['BingXBP_BitstampAP']
    BingXBP_GeminiAP = results['BingXBP_GeminiAP']
    BingXBP_KrakenAP = results['BingXBP_KrakenAP']
    BingXBP_GateioAP = results['BingXBP_Gate.ioAP']
    BingXBP_HTXAP = results['BingXBP_HTXAP']
    BingXBP_MEXCAP = results['BingXBP_MEXCAP']
    BingXBP_LbankAP = results['BingXBP_LbankAP']
    BingXBP_BitmartAP = results['BingXBP_BitmartAP']
    BingXBP_DeepcoinAP = results['BingXBP_DeepcoinAP']
    BingXBP_BitfinexAP = results['BingXBP_BitfinexAP']
    BingXBP_BingXAP = results['BingXBP_BingXAP']
    BingXBP_OrangeXAP = results['BingXBP_OrangeXAP']
    BingXBP_BitvenusAP = results['BingXBP_BitvenusAP']
    BingXBP_BiconomyAP = results['BingXBP_BiconomyAP']
    BingXBP_XTAP = results['BingXBP_XTAP']
    BingXBP_BitflyerAP = results['BingXBP_BitflyerAP']
    BingXBP_CoinWAP = results['BingXBP_CoinWAP']
    BingXBP_ToobitAP = results['BingXBP_ToobitAP']
    BingXBP_TapBitAP = results['BingXBP_TapBitAP']

    OrangeXBP_BinanceAP = results['OrangeXBP_BinanceAP']
    OrangeXBP_BybitAP = results['OrangeXBP_BybitAP']
    OrangeXBP_OKXAP = results['OrangeXBP_OKXAP']
    OrangeXBP_UpbitAP = results['OrangeXBP_UpbitAP']
    OrangeXBP_KucoinAP = results['OrangeXBP_KucoinAP']
    OrangeXBP_BitgetAP = results['OrangeXBP_BitgetAP']
    OrangeXBP_BitstampAP = results['OrangeXBP_BitstampAP']
    OrangeXBP_GeminiAP = results['OrangeXBP_GeminiAP']
    OrangeXBP_KrakenAP = results['OrangeXBP_KrakenAP']
    OrangeXBP_GateioAP = results['OrangeXBP_Gate.ioAP']
    OrangeXBP_HTXAP = results['OrangeXBP_HTXAP']
    OrangeXBP_MEXCAP = results['OrangeXBP_MEXCAP']
    OrangeXBP_LbankAP = results['OrangeXBP_LbankAP']
    OrangeXBP_BitmartAP = results['OrangeXBP_BitmartAP']
    OrangeXBP_DeepcoinAP = results['OrangeXBP_DeepcoinAP']
    OrangeXBP_BitfinexAP = results['OrangeXBP_BitfinexAP']
    OrangeXBP_BingXAP = results['OrangeXBP_BingXAP']
    OrangeXBP_OrangeXAP = results['OrangeXBP_OrangeXAP']
    OrangeXBP_BitvenusAP = results['OrangeXBP_BitvenusAP']
    OrangeXBP_BiconomyAP = results['OrangeXBP_BiconomyAP']
    OrangeXBP_XTAP = results['OrangeXBP_XTAP']
    OrangeXBP_BitflyerAP = results['OrangeXBP_BitflyerAP']
    OrangeXBP_CoinWAP = results['OrangeXBP_CoinWAP']
    OrangeXBP_ToobitAP = results['OrangeXBP_ToobitAP']
    OrangeXBP_TapBitAP = results['OrangeXBP_TapBitAP']

    BitvenusBP_BinanceAP = results['BitvenusBP_BinanceAP']
    BitvenusBP_BybitAP = results['BitvenusBP_BybitAP']
    BitvenusBP_OKXAP = results['BitvenusBP_OKXAP']
    BitvenusBP_UpbitAP = results['BitvenusBP_UpbitAP']
    BitvenusBP_KucoinAP = results['BitvenusBP_KucoinAP']
    BitvenusBP_BitgetAP = results['BitvenusBP_BitgetAP']
    BitvenusBP_BitstampAP = results['BitvenusBP_BitstampAP']
    BitvenusBP_GeminiAP = results['BitvenusBP_GeminiAP']
    BitvenusBP_KrakenAP = results['BitvenusBP_KrakenAP']
    BitvenusBP_GateioAP = results['BitvenusBP_Gate.ioAP']
    BitvenusBP_HTXAP = results['BitvenusBP_HTXAP']
    BitvenusBP_MEXCAP = results['BitvenusBP_MEXCAP']
    BitvenusBP_LbankAP = results['BitvenusBP_LbankAP']
    BitvenusBP_BitmartAP = results['BitvenusBP_BitmartAP']
    BitvenusBP_DeepcoinAP = results['BitvenusBP_DeepcoinAP']
    BitvenusBP_BitfinexAP = results['BitvenusBP_BitfinexAP']
    BitvenusBP_BingXAP = results['BitvenusBP_BingXAP']
    BitvenusBP_OrangeXAP = results['BitvenusBP_OrangeXAP']
    BitvenusBP_BitvenusAP = results['BitvenusBP_BitvenusAP']
    BitvenusBP_BiconomyAP = results['BitvenusBP_BiconomyAP']
    BitvenusBP_XTAP = results['BitvenusBP_XTAP']
    BitvenusBP_BitflyerAP = results['BitvenusBP_BitflyerAP']
    BitvenusBP_CoinWAP = results['BitvenusBP_CoinWAP']
    BitvenusBP_ToobitAP = results['BitvenusBP_ToobitAP']
    BitvenusBP_TapBitAP = results['BitvenusBP_TapBitAP']

    BiconomyBP_BinanceAP = results['BiconomyBP_BinanceAP']
    BiconomyBP_BybitAP = results['BiconomyBP_BybitAP']
    BiconomyBP_OKXAP = results['BiconomyBP_OKXAP']
    BiconomyBP_UpbitAP = results['BiconomyBP_UpbitAP']
    BiconomyBP_KucoinAP = results['BiconomyBP_KucoinAP']
    BiconomyBP_BitgetAP = results['BiconomyBP_BitgetAP']
    BiconomyBP_BitstampAP = results['BiconomyBP_BitstampAP']
    BiconomyBP_GeminiAP = results['BiconomyBP_GeminiAP']
    BiconomyBP_KrakenAP = results['BiconomyBP_KrakenAP']
    BiconomyBP_GateioAP = results['BiconomyBP_Gate.ioAP']
    BiconomyBP_HTXAP = results['BiconomyBP_HTXAP']
    BiconomyBP_MEXCAP = results['BiconomyBP_MEXCAP']
    BiconomyBP_LbankAP = results['BiconomyBP_LbankAP']
    BiconomyBP_BitmartAP = results['BiconomyBP_BitmartAP']
    BiconomyBP_DeepcoinAP = results['BiconomyBP_DeepcoinAP']
    BiconomyBP_BitfinexAP = results['BiconomyBP_BitfinexAP']
    BiconomyBP_BingXAP = results['BiconomyBP_BingXAP']
    BiconomyBP_OrangeXAP = results['BiconomyBP_OrangeXAP']
    BiconomyBP_BitvenusAP = results['BiconomyBP_BitvenusAP']
    BiconomyBP_BiconomyAP = results['BiconomyBP_BiconomyAP']
    BiconomyBP_XTAP = results['BiconomyBP_XTAP']
    BiconomyBP_BitflyerAP = results['BiconomyBP_BitflyerAP']
    BiconomyBP_CoinWAP = results['BiconomyBP_CoinWAP']
    BiconomyBP_ToobitAP = results['BiconomyBP_ToobitAP']
    BiconomyBP_TapBitAP = results['BiconomyBP_TapBitAP']

    XTBP_BinanceAP = results['XTBP_BinanceAP']
    XTBP_BybitAP = results['XTBP_BybitAP']
    XTBP_OKXAP = results['XTBP_OKXAP']
    XTBP_UpbitAP = results['XTBP_UpbitAP']
    XTBP_KucoinAP = results['XTBP_KucoinAP']
    XTBP_BitgetAP = results['XTBP_BitgetAP']
    XTBP_BitstampAP = results['XTBP_BitstampAP']
    XTBP_GeminiAP = results['XTBP_GeminiAP']
    XTBP_KrakenAP = results['XTBP_KrakenAP']
    XTBP_GateioAP = results['XTBP_Gate.ioAP']
    XTBP_HTXAP = results['XTBP_HTXAP']
    XTBP_MEXCAP = results['XTBP_MEXCAP']
    XTBP_LbankAP = results['XTBP_LbankAP']
    XTBP_BitmartAP = results['XTBP_BitmartAP']
    XTBP_DeepcoinAP = results['XTBP_DeepcoinAP']
    XTBP_BitfinexAP = results['XTBP_BitfinexAP']
    XTBP_BingXAP = results['XTBP_BingXAP']
    XTBP_OrangeXAP = results['XTBP_OrangeXAP']
    XTBP_BitvenusAP = results['XTBP_BitvenusAP']
    XTBP_BiconomyAP = results['XTBP_BiconomyAP']
    XTBP_XTAP = results['XTBP_XTAP']
    XTBP_BitflyerAP = results['XTBP_BitflyerAP']
    XTBP_CoinWAP = results['XTBP_CoinWAP']
    XTBP_ToobitAP = results['XTBP_ToobitAP']
    XTBP_TapBitAP = results['XTBP_TapBitAP']

    BitflyerBP_BinanceAP = results['BitflyerBP_BinanceAP']
    BitflyerBP_BybitAP = results['BitflyerBP_BybitAP']
    BitflyerBP_OKXAP = results['BitflyerBP_OKXAP']
    BitflyerBP_UpbitAP = results['BitflyerBP_UpbitAP']
    BitflyerBP_KucoinAP = results['BitflyerBP_KucoinAP']
    BitflyerBP_BitgetAP = results['BitflyerBP_BitgetAP']
    BitflyerBP_BitstampAP = results['BitflyerBP_BitstampAP']
    BitflyerBP_GeminiAP = results['BitflyerBP_GeminiAP']
    BitflyerBP_KrakenAP = results['BitflyerBP_KrakenAP']
    BitflyerBP_GateioAP = results['BitflyerBP_Gate.ioAP']
    BitflyerBP_HTXAP = results['BitflyerBP_HTXAP']
    BitflyerBP_MEXCAP = results['BitflyerBP_MEXCAP']
    BitflyerBP_LbankAP = results['BitflyerBP_LbankAP']
    BitflyerBP_BitmartAP = results['BitflyerBP_BitmartAP']
    BitflyerBP_DeepcoinAP = results['BitflyerBP_DeepcoinAP']
    BitflyerBP_BitfinexAP = results['BitflyerBP_BitfinexAP']
    BitflyerBP_BingXAP = results['BitflyerBP_BingXAP']
    BitflyerBP_OrangeXAP = results['BitflyerBP_OrangeXAP']
    BitflyerBP_BitvenusAP = results['BitflyerBP_BitvenusAP']
    BitflyerBP_BiconomyAP = results['BitflyerBP_BiconomyAP']
    BitflyerBP_XTAP = results['BitflyerBP_XTAP']
    BitflyerBP_BitflyerAP = results['BitflyerBP_BitflyerAP']
    BitflyerBP_CoinWAP = results['BitflyerBP_CoinWAP']
    BitflyerBP_ToobitAP = results['BitflyerBP_ToobitAP']
    BitflyerBP_TapBitAP = results['BitflyerBP_TapBitAP']

    CoinWBP_BinanceAP = results['CoinWBP_BinanceAP']
    CoinWBP_BybitAP = results['CoinWBP_BybitAP']
    CoinWBP_OKXAP = results['CoinWBP_OKXAP']
    CoinWBP_UpbitAP = results['CoinWBP_UpbitAP']
    CoinWBP_KucoinAP = results['CoinWBP_KucoinAP']
    CoinWBP_BitgetAP = results['CoinWBP_BitgetAP']
    CoinWBP_BitstampAP = results['CoinWBP_BitstampAP']
    CoinWBP_GeminiAP = results['CoinWBP_GeminiAP']
    CoinWBP_KrakenAP = results['CoinWBP_KrakenAP']
    CoinWBP_GateioAP = results['CoinWBP_Gate.ioAP']
    CoinWBP_HTXAP = results['CoinWBP_HTXAP']
    CoinWBP_MEXCAP = results['CoinWBP_MEXCAP']
    CoinWBP_LbankAP = results['CoinWBP_LbankAP']
    CoinWBP_BitmartAP = results['CoinWBP_BitmartAP']
    CoinWBP_DeepcoinAP = results['CoinWBP_DeepcoinAP']
    CoinWBP_BitfinexAP = results['CoinWBP_BitfinexAP']
    CoinWBP_BingXAP = results['CoinWBP_BingXAP']
    CoinWBP_OrangeXAP = results['CoinWBP_OrangeXAP']
    CoinWBP_BitvenusAP = results['CoinWBP_BitvenusAP']
    CoinWBP_BiconomyAP = results['CoinWBP_BiconomyAP']
    CoinWBP_XTAP = results['CoinWBP_XTAP']
    CoinWBP_BitflyerAP = results['CoinWBP_BitflyerAP']
    CoinWBP_CoinWAP = results['CoinWBP_CoinWAP']
    CoinWBP_ToobitAP = results['CoinWBP_ToobitAP']
    CoinWBP_TapBitAP = results['CoinWBP_TapBitAP']

    ToobitBP_BinanceAP = results['ToobitBP_BinanceAP']
    ToobitBP_BybitAP = results['ToobitBP_BybitAP']
    ToobitBP_OKXAP = results['ToobitBP_OKXAP']
    ToobitBP_UpbitAP = results['ToobitBP_UpbitAP']
    ToobitBP_KucoinAP = results['ToobitBP_KucoinAP']
    ToobitBP_BitgetAP = results['ToobitBP_BitgetAP']
    ToobitBP_BitstampAP = results['ToobitBP_BitstampAP']
    ToobitBP_GeminiAP = results['ToobitBP_GeminiAP']
    ToobitBP_KrakenAP = results['ToobitBP_KrakenAP']
    ToobitBP_GateioAP = results['ToobitBP_Gate.ioAP']
    ToobitBP_HTXAP = results['ToobitBP_HTXAP']
    ToobitBP_MEXCAP = results['ToobitBP_MEXCAP']
    ToobitBP_LbankAP = results['ToobitBP_LbankAP']
    ToobitBP_BitmartAP = results['ToobitBP_BitmartAP']
    ToobitBP_DeepcoinAP = results['ToobitBP_DeepcoinAP']
    ToobitBP_BitfinexAP = results['ToobitBP_BitfinexAP']
    ToobitBP_BingXAP = results['ToobitBP_BingXAP']
    ToobitBP_OrangeXAP = results['ToobitBP_OrangeXAP']
    ToobitBP_BitvenusAP = results['ToobitBP_BitvenusAP']
    ToobitBP_BiconomyAP = results['ToobitBP_BiconomyAP']
    ToobitBP_XTAP = results['ToobitBP_XTAP']
    ToobitBP_BitflyerAP = results['ToobitBP_BitflyerAP']
    ToobitBP_CoinWAP = results['ToobitBP_CoinWAP']
    ToobitBP_ToobitAP = results['ToobitBP_ToobitAP']
    ToobitBP_TapBitAP = results['ToobitBP_TapBitAP']

    TapBitBP_BinanceAP = results['TapBitBP_BinanceAP']
    TapBitBP_BybitAP = results['TapBitBP_BybitAP']
    TapBitBP_OKXAP = results['TapBitBP_OKXAP']
    TapBitBP_UpbitAP = results['TapBitBP_UpbitAP']
    TapBitBP_KucoinAP = results['TapBitBP_KucoinAP']
    TapBitBP_BitgetAP = results['TapBitBP_BitgetAP']
    TapBitBP_BitstampAP = results['TapBitBP_BitstampAP']
    TapBitBP_GeminiAP = results['TapBitBP_GeminiAP']
    TapBitBP_KrakenAP = results['TapBitBP_KrakenAP']
    TapBitBP_GateioAP = results['TapBitBP_Gate.ioAP']
    TapBitBP_HTXAP = results['TapBitBP_HTXAP']
    TapBitBP_MEXCAP = results['TapBitBP_MEXCAP']
    TapBitBP_LbankAP = results['TapBitBP_LbankAP']
    TapBitBP_BitmartAP = results['TapBitBP_BitmartAP']
    TapBitBP_DeepcoinAP = results['TapBitBP_DeepcoinAP']
    TapBitBP_BitfinexAP = results['TapBitBP_BitfinexAP']
    TapBitBP_BingXAP = results['TapBitBP_BingXAP']
    TapBitBP_OrangeXAP = results['TapBitBP_OrangeXAP']
    TapBitBP_BitvenusAP = results['TapBitBP_BitvenusAP']
    TapBitBP_BiconomyAP = results['TapBitBP_BiconomyAP']
    TapBitBP_XTAP = results['TapBitBP_XTAP']
    TapBitBP_BitflyerAP = results['TapBitBP_BitflyerAP']
    TapBitBP_CoinWAP = results['TapBitBP_CoinWAP']
    TapBitBP_ToobitAP = results['TapBitBP_ToobitAP']
    TapBitBP_TapBitAP = results['TapBitBP_TapBitAP']

    end = time.perf_counter_ns()
    processingtime = (end - start)+inital_time


    # "Binance",BinanceLTP,BinanceAP1,BinanceAP1V,BinanceBP1,BinanceBP1V,
    def Buckets(Name, LTP, AP1, AP1V, BP1, BP1V, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11,
                sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19, sub20, sub21, sub22, sub23, sub24, sub25,
                Status):
        tasks = []
        with ThreadPoolExecutor() as executor:
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Binance", BinanceLTP, BinanceAP1,
                                BinanceAP1V, BinanceBP1, BinanceBP1V, processingtime, sub1, Status, Binance_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bybit", BybitLTP, BybitAP1,
                                BybitAP1V, BybitBP1, BybitBP1V, processingtime, sub2, Status, BybitStatus))
            tasks.append(
                executor.submit(checker, OKXOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "OKX", OKXLTP, OKXAP1, OKXAP1V,
                                OKXBP1, OKXBP1V, processingtime, sub3, Binance_Status, OKX_Status))
            tasks.append(
                executor.submit(checker, UpbitOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Upbit", UpbitLTP, UpbitAP1,
                                UpbitAP1V, UpbitBP1, UpbitBP1V, processingtime, sub4, Status, Upbit_Status))
            tasks.append(
                executor.submit(checker, KucoinOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Kucoin", KucoinLTP, KucoinAP1,
                                KucoinAP1V, KucoinBP1, KucoinBP1V, processingtime, sub5, Status, Kucoin_Status))
            tasks.append(
                executor.submit(checker, BitgetOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitget", BitgetLTP, BitgetAP1,
                                BitgetAP1V, BitgetBP1, BitgetBP1V, processingtime, sub6, Status, Bitget_Status))
            tasks.append(executor.submit(checker, BitstampOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitstamp", BitstampLTP,
                                         BitstampAP1, BitstampAP1V, BitstampBP1, BitstampBP1V, processingtime, sub7,
                                         Status, Bitstamp_Status))
            tasks.append(
                executor.submit(checker, KrakenOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Kraken", KrakenLTP, KrakenAP1,
                                KrakenAPV1, KrakenBP1, KrakenBPV1, processingtime, sub8, Status, Kraken_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Gate.io", GateioLTP, GateioAP1,
                                GateioAPV1, GateioBP1, GateioBPV1, processingtime, sub9, Status, Gateio_Status))
            tasks.append(
                executor.submit(checker, HTXOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "HTX", HTXLTP, HTXAP1, HTXAP1V,
                                HTXBP1, HTXBP1V, processingtime, sub10, Status, HTX_Status))
            tasks.append(
                executor.submit(checker, MEXCOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "MEXC", MEXCLTP, MEXCAP1, MEXCAP1V,
                                MEXCBP1, MEXCBP1V, processingtime, sub11, Status, MEXC_Status))
            tasks.append(
                executor.submit(checker, LbankOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Lbank", LbankLTP, LbankAP1,
                                LbankAP1V, LbankBP1, LbankBP1V, processingtime, sub12, Status, Lbank_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitmart", BitmartLTP, BitmartAP1,
                                BitmartAP1V, BitmartBP1, BitmartBP1V, processingtime, sub13, Status, Bitmart_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Deepcoin", DeepcoinLTP,
                                         DeepcoinAP1, DeepcoinAP1V, DeepcoinBP1, DeepcoinBP1V, processingtime, sub14,
                                         Status, Deepcoin_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitfinex", BitfinexLTP,
                                         BitfinexAP1, BitfinexAP1V, BitfinexBP1, BitfinexBP1V, processingtime, sub15,
                                         Status, Bitfinex_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "BingX", BingXLTP, BingXAP1,
                                BingXAP1V, BingXBP1, BingXBP1V, processingtime, sub16, Status, BingX_Status))
            tasks.append(
                executor.submit(checker, OrangeXOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "OrangeX", OrangeXLTP, OrangeXAP1,
                                OrangeXAP1V, OrangeXBP1, OrangeXBP1V, processingtime, sub17, Status, OrangeX_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitvenus", BitvenusLTP,
                                         BitvenusAP1, BitvenusAP1V, BitvenusBP1, BitvenusBP1V, processingtime, sub18,
                                         Status, Bitvenus_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Biconomy", BiconomyLTP,
                                         BiconomyAP1, BiconomyAP1V, BiconomyBP1, BiconomyBP1V, processingtime, sub19,
                                         Status, Biconomy_Status))
            tasks.append(
                executor.submit(checker, GeminiOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Gemini", GeminiLTP, GeminiAP1,
                                GeminiAP1V, GeminiBP1, GeminiBP1V, processingtime, sub20, Status, Gemini_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "XT", XTLTP, XTAP1, XTAP1V, XTBP1,
                                XTBP1V, processingtime, sub21, Binance_Status, XT_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Bitflyer", BitflyerLTP, BitflyerAP1,
                                BitflyerAP1V, BitflyerBP1, BitflyerBP1V, processingtime, sub22, Status,
                                Bitflyer_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "CoinW", CoinWLTP, CoinWAP1, CoinWAP1V,
                                CoinWBP1, CoinWBP1V, processingtime, sub23, Status, CoinW_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Toobit", ToobitLTP, ToobitAP1,
                                ToobitAP1V, ToobitBP1, ToobitBP1V, processingtime, sub24, Status, Toobit_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP1, AP1V, BP1, BP1V, "Tapbit", TapbitLTP, TapbitAP1,
                                TapbitAP1V, TapbitBP1, TapbitBP1V, processingtime, sub25, Status, TapBit_Status))

            # Wait for all tasks to complete
            for task in tasks:
                task.result()

    buckets_args = [
        (
            "Binance", BinanceLTP, BinanceAP1, BinanceAP1V, BinanceBP1, BinanceBP1V, BinanceBP_BinanceAP,
            BinanceBP_BybitAP,
            BinanceBP_OKXAP, BinanceBP_UpbitAP, BinanceBP_KucoinAP, BinanceBP_BitgetAP, BinanceBP_BitstampAP,
            BinanceBP_GeminiAP, BinanceBP_KrakenAP, BinanceBP_GateioAP, BinanceBP_HTXAP, BinanceBP_MEXCAP,
            BinanceBP_LbankAP, BinanceBP_BitmartAP, BinanceBP_DeepcoinAP, BinanceBP_BitfinexAP, BinanceBP_BingXAP,
            BinanceBP_OrangeXAP, BinanceBP_BitvenusAP, BinanceBP_BiconomyAP, BinanceBP_XTAP, BinanceBP_BitflyerAP,
            BinanceBP_CoinWAP, BinanceBP_ToobitAP, BinanceBP_TapBitAP, Binance_Status),
        ("Bybit", BybitLTP, BybitAP1, BybitAP1V, BybitBP1, BybitBP1V, BybitBP_BinanceAP, BybitBP_BybitAP, BybitBP_OKXAP,
         BybitBP_UpbitAP, BybitBP_KucoinAP, BybitBP_BitgetAP, BybitBP_BitstampAP, BybitBP_GeminiAP, BybitBP_KrakenAP,
         BybitBP_GateioAP, BybitBP_HTXAP, BybitBP_MEXCAP, BybitBP_LbankAP, BybitBP_BitmartAP, BybitBP_DeepcoinAP,
         BybitBP_BitfinexAP, BybitBP_BingXAP, BybitBP_OrangeXAP, BybitBP_BitvenusAP, BybitBP_BiconomyAP, BybitBP_XTAP,
         BybitBP_BitflyerAP, BybitBP_CoinWAP, BybitBP_ToobitAP, BybitBP_TapBitAP, BybitStatus),
        ("OKX", OKXLTP, OKXAP1, OKXAP1V, OKXBP1, OKXBP1V, OKXBP_BinanceAP, OKXBP_BybitAP, OKXBP_OKXAP, OKXBP_UpbitAP,
         OKXBP_KucoinAP, OKXBP_BitgetAP, OKXBP_BitstampAP, OKXBP_GeminiAP, OKXBP_KrakenAP, OKXBP_GateioAP, OKXBP_HTXAP,
         OKXBP_MEXCAP, OKXBP_LbankAP, OKXBP_BitmartAP, OKXBP_DeepcoinAP, OKXBP_BitfinexAP, OKXBP_BingXAP,
         OKXBP_OrangeXAP, OKXBP_BitvenusAP, OKXBP_BiconomyAP, OKXBP_XTAP, OKXBP_BitflyerAP, OKXBP_CoinWAP,
         OKXBP_ToobitAP, OKXBP_TapBitAP, OKX_Status),
        ("Upbit", UpbitLTP, UpbitAP1, UpbitAP1V, UpbitBP1, UpbitBP1V, UpbitBP_BinanceAP, UpbitBP_BybitAP, UpbitBP_OKXAP,
         UpbitBP_UpbitAP, UpbitBP_KucoinAP, UpbitBP_BitgetAP, UpbitBP_BitstampAP, UpbitBP_GeminiAP, UpbitBP_KrakenAP,
         UpbitBP_GateioAP, UpbitBP_HTXAP, UpbitBP_MEXCAP, UpbitBP_LbankAP, UpbitBP_BitmartAP, UpbitBP_DeepcoinAP,
         UpbitBP_BitfinexAP, UpbitBP_BingXAP, UpbitBP_OrangeXAP, UpbitBP_BitvenusAP, UpbitBP_BiconomyAP, UpbitBP_XTAP,
         UpbitBP_BitflyerAP, UpbitBP_CoinWAP, UpbitBP_ToobitAP, UpbitBP_TapBitAP, Upbit_Status),
        ("Kucoin", KucoinLTP, KucoinAP1, KucoinAP1V, KucoinBP1, KucoinBP1V, KucoinBP_BinanceAP, KucoinBP_BybitAP,
         KucoinBP_OKXAP, KucoinBP_UpbitAP, KucoinBP_KucoinAP, KucoinBP_BitgetAP, KucoinBP_BitstampAP, KucoinBP_GeminiAP,
         KucoinBP_KrakenAP, KucoinBP_GateioAP, KucoinBP_HTXAP, KucoinBP_MEXCAP, KucoinBP_LbankAP, KucoinBP_BitmartAP,
         KucoinBP_DeepcoinAP, KucoinBP_BitfinexAP, KucoinBP_BingXAP, KucoinBP_OrangeXAP, KucoinBP_BitvenusAP,
         KucoinBP_BiconomyAP, KucoinBP_XTAP, KucoinBP_BitflyerAP, KucoinBP_CoinWAP, KucoinBP_ToobitAP,
         KucoinBP_TapBitAP, Kucoin_Status),
        ("Bitget", BitgetLTP, BitgetAP1, BitgetAP1V, BitgetBP1, BitgetBP1V, BitgetBP_BinanceAP, BitgetBP_BybitAP,
         BitgetBP_OKXAP, BitgetBP_UpbitAP, BitgetBP_KucoinAP, BitgetBP_BitgetAP, BitgetBP_BitstampAP, BitgetBP_GeminiAP,
         BitgetBP_KrakenAP, BitgetBP_GateioAP, BitgetBP_HTXAP, BitgetBP_MEXCAP, BitgetBP_LbankAP, BitgetBP_BitmartAP,
         BitgetBP_DeepcoinAP, BitgetBP_BitfinexAP, BitgetBP_BingXAP, BitgetBP_OrangeXAP, BitgetBP_BitvenusAP,
         BitgetBP_BiconomyAP, BitgetBP_XTAP, BitgetBP_BitflyerAP, BitgetBP_CoinWAP, BitgetBP_ToobitAP,
         BitgetBP_TapBitAP, Bitget_Status),
        ("Bitstamp", BitstampLTP, BitstampAP1, BitstampAP1V, BitstampBP1, BitstampBP1V, BitstampBP_BinanceAP,
         BitstampBP_BybitAP, BitstampBP_OKXAP, BitstampBP_UpbitAP, BitstampBP_KucoinAP, BitstampBP_BitgetAP,
         BitstampBP_BitstampAP, BitstampBP_GeminiAP, BitstampBP_KrakenAP, BitstampBP_GateioAP, BitstampBP_HTXAP,
         BitstampBP_MEXCAP, BitstampBP_LbankAP, BitstampBP_BitmartAP, BitstampBP_DeepcoinAP, BitstampBP_BitfinexAP,
         BitstampBP_BingXAP, BitstampBP_OrangeXAP, BitstampBP_BitvenusAP, BitstampBP_BiconomyAP, BitstampBP_XTAP,
         BitstampBP_BitflyerAP, BitstampBP_CoinWAP, BitstampBP_ToobitAP, BitstampBP_TapBitAP, Bitstamp_Status),
        ("Kraken", KrakenLTP, KrakenAP1, KrakenAPV1, KrakenBP1, KrakenBPV1, KrakenBP_BinanceAP, KrakenBP_BybitAP,
         KrakenBP_OKXAP, KrakenBP_UpbitAP, KrakenBP_KucoinAP, KrakenBP_BitgetAP, KrakenBP_BitstampAP, KrakenBP_GeminiAP,
         KrakenBP_KrakenAP, KrakenBP_GateioAP, KrakenBP_HTXAP, KrakenBP_MEXCAP, KrakenBP_LbankAP, KrakenBP_BitmartAP,
         KrakenBP_DeepcoinAP, KrakenBP_BitfinexAP, KrakenBP_BingXAP, KrakenBP_OrangeXAP, KrakenBP_BitvenusAP,
         KrakenBP_BiconomyAP, KrakenBP_XTAP, KrakenBP_BitflyerAP, KrakenBP_CoinWAP, KrakenBP_ToobitAP,
         KrakenBP_TapBitAP, Kraken_Status),
        ("Gate.io", GateioLTP, GateioAP1, GateioAPV1, GateioBP1, GateioBPV1, GateioBP_BinanceAP, GateioBP_BybitAP,
         GateioBP_OKXAP, GateioBP_UpbitAP, GateioBP_KucoinAP, GateioBP_BitgetAP, GateioBP_BitstampAP, GateioBP_GeminiAP,
         GateioBP_KrakenAP, GateioBP_GateioAP, GateioBP_HTXAP, GateioBP_MEXCAP, GateioBP_LbankAP, GateioBP_BitmartAP,
         GateioBP_DeepcoinAP, GateioBP_BitfinexAP, GateioBP_BingXAP, GateioBP_OrangeXAP, GateioBP_BitvenusAP,
         GateioBP_BiconomyAP, GateioBP_XTAP, GateioBP_BitflyerAP, GateioBP_CoinWAP, GateioBP_ToobitAP,
         GateioBP_TapBitAP, Gateio_Status),
        ("HTX", HTXLTP, HTXAP1,
         HTXAP1V,
         HTXBP1, HTXBP1V,
         HTXBP_BinanceAP, HTXBP_BybitAP, HTXBP_OKXAP, HTXBP_UpbitAP, HTXBP_KucoinAP,
         HTXBP_BitgetAP, HTXBP_BitstampAP
         , HTXBP_GeminiAP, HTXBP_KrakenAP, HTXBP_GateioAP, HTXBP_HTXAP, HTXBP_MEXCAP,
         HTXBP_LbankAP, HTXBP_BitmartAP
         , HTXBP_DeepcoinAP, HTXBP_BitfinexAP, HTXBP_BingXAP, HTXBP_OrangeXAP, HTXBP_BitvenusAP,
         HTXBP_BiconomyAP,
         HTXBP_XTAP, HTXBP_BitflyerAP, HTXBP_CoinWAP, HTXBP_ToobitAP, HTXBP_TapBitAP, HTX_Status
         ),
        ("MEXC", MEXCLTP,
         MEXCAP1, MEXCAP1V,
         MEXCBP1, MEXCBP1V,
         MEXCBP_BinanceAP, MEXCBP_BybitAP, MEXCBP_OKXAP, MEXCBP_UpbitAP, MEXCBP_KucoinAP,
         MEXCBP_BitgetAP, MEXCBP_BitstampAP
         , MEXCBP_GeminiAP, MEXCBP_KrakenAP, MEXCBP_GateioAP, MEXCBP_HTXAP, MEXCBP_MEXCAP,
         MEXCBP_LbankAP, MEXCBP_BitmartAP
         , MEXCBP_DeepcoinAP, MEXCBP_BitfinexAP, MEXCBP_BingXAP, MEXCBP_OrangeXAP, MEXCBP_BitvenusAP,
         MEXCBP_BiconomyAP,
         MEXCBP_XTAP, MEXCBP_BitflyerAP, MEXCBP_CoinWAP, MEXCBP_ToobitAP, MEXCBP_TapBitAP, MEXC_Status
         ),
        ("Lbank", LbankLTP,
         LbankAP1, LbankAP1V,
         LbankBP1, LbankBP1V,
         LbankBP_BinanceAP, LbankBP_BybitAP, LbankBP_OKXAP, LbankBP_UpbitAP, LbankBP_KucoinAP,
         LbankBP_BitgetAP, LbankBP_BitstampAP
         , LbankBP_GeminiAP, LbankBP_KrakenAP, LbankBP_GateioAP, LbankBP_HTXAP, LbankBP_MEXCAP,
         LbankBP_LbankAP, LbankBP_BitmartAP
         , LbankBP_DeepcoinAP, LbankBP_BitfinexAP, LbankBP_BingXAP, LbankBP_OrangeXAP, LbankBP_BitvenusAP,
         LbankBP_BiconomyAP,
         LbankBP_XTAP, LbankBP_BitflyerAP, LbankBP_CoinWAP, LbankBP_ToobitAP, LbankBP_TapBitAP, Lbank_Status
         ),
        ("Bitmart",
         BitmartLTP, BitmartAP1, BitmartAP1V,
         BitmartBP1, BitmartBP1V,
         BitmartBP_BinanceAP, BitmartBP_BybitAP, BitmartBP_OKXAP, BitmartBP_UpbitAP, BitmartBP_KucoinAP,
         BitmartBP_BitgetAP, BitmartBP_BitstampAP
         , BitmartBP_GeminiAP, BitmartBP_KrakenAP, BitmartBP_GateioAP, BitmartBP_HTXAP, BitmartBP_MEXCAP,
         BitmartBP_LbankAP, BitmartBP_BitmartAP
         , BitmartBP_DeepcoinAP, BitmartBP_BitfinexAP, BitmartBP_BingXAP, BitmartBP_OrangeXAP, BitmartBP_BitvenusAP,
         BitmartBP_BiconomyAP,
         BitmartBP_XTAP, BitmartBP_BitflyerAP, BitmartBP_CoinWAP, BitmartBP_ToobitAP, BitmartBP_TapBitAP, Bitmart_Status
         ),
        ("Deepcoin",
         DeepcoinLTP,
         DeepcoinAP1, DeepcoinAP1V, DeepcoinBP1, DeepcoinBP1V,
         DeepcoinBP_BinanceAP, DeepcoinBP_BybitAP, DeepcoinBP_OKXAP, DeepcoinBP_UpbitAP, DeepcoinBP_KucoinAP,
         DeepcoinBP_BitgetAP, DeepcoinBP_BitstampAP
         , DeepcoinBP_GeminiAP, DeepcoinBP_KrakenAP, DeepcoinBP_GateioAP, DeepcoinBP_HTXAP, DeepcoinBP_MEXCAP,
         DeepcoinBP_LbankAP, DeepcoinBP_BitmartAP
         , DeepcoinBP_DeepcoinAP, DeepcoinBP_BitfinexAP, DeepcoinBP_BingXAP, DeepcoinBP_OrangeXAP,
         DeepcoinBP_BitvenusAP,
         DeepcoinBP_BiconomyAP,
         DeepcoinBP_XTAP, DeepcoinBP_BitflyerAP, DeepcoinBP_CoinWAP, DeepcoinBP_ToobitAP, DeepcoinBP_TapBitAP,
         Deepcoin_Status
         ),
        ("Bitfinex",
         BitfinexLTP, BitfinexAP1, BitfinexAP1V,
         BitfinexBP1, BitfinexBP1V,
         BitfinexBP_BinanceAP, BitfinexBP_BybitAP, BitfinexBP_OKXAP, BitfinexBP_UpbitAP, BitfinexBP_KucoinAP,
         BitfinexBP_BitgetAP, BitfinexBP_BitstampAP
         , BitfinexBP_GeminiAP, BitfinexBP_KrakenAP, BitfinexBP_GateioAP, BitfinexBP_HTXAP, BitfinexBP_MEXCAP,
         BitfinexBP_LbankAP, BitfinexBP_BitmartAP
         , BitfinexBP_DeepcoinAP, BitfinexBP_BitfinexAP, BitfinexBP_BingXAP, BitfinexBP_OrangeXAP,
         BitfinexBP_BitvenusAP,
         BitfinexBP_BiconomyAP,
         BitfinexBP_XTAP, BitfinexBP_BitflyerAP, BitfinexBP_CoinWAP, BitfinexBP_ToobitAP, BitfinexBP_TapBitAP,
         Bitfinex_Status
         ),
        ("BingX", BingXLTP,
         BingXAP1, BingXAP1V,
         BingXBP1, BingXBP1V,
         BingXBP_BinanceAP, BingXBP_BybitAP, BingXBP_OKXAP, BingXBP_UpbitAP, BingXBP_KucoinAP,
         BingXBP_BitgetAP, BingXBP_BitstampAP
         , BingXBP_GeminiAP, BingXBP_KrakenAP, BingXBP_GateioAP, BingXBP_HTXAP, BingXBP_MEXCAP,
         BingXBP_LbankAP, BingXBP_BitmartAP
         , BingXBP_DeepcoinAP, BingXBP_BitfinexAP, BingXBP_BingXAP, BingXBP_OrangeXAP, BingXBP_BitvenusAP,
         BingXBP_BiconomyAP,
         BingXBP_XTAP, BingXBP_BitflyerAP, BingXBP_CoinWAP, BingXBP_ToobitAP, BingXBP_TapBitAP, BingX_Status
         ),
        ("OrangeX",
         OrangeXLTP, OrangeXAP1, OrangeXAP1V,
         OrangeXBP1, OrangeXBP1V,
         OrangeXBP_BinanceAP, OrangeXBP_BybitAP, OrangeXBP_OKXAP, OrangeXBP_UpbitAP, OrangeXBP_KucoinAP,
         OrangeXBP_BitgetAP, OrangeXBP_BitstampAP
         , OrangeXBP_GeminiAP, OrangeXBP_KrakenAP, OrangeXBP_GateioAP, OrangeXBP_HTXAP, OrangeXBP_MEXCAP,
         OrangeXBP_LbankAP, OrangeXBP_BitmartAP
         , OrangeXBP_DeepcoinAP, OrangeXBP_BitfinexAP, OrangeXBP_BingXAP, OrangeXBP_OrangeXAP, OrangeXBP_BitvenusAP,
         OrangeXBP_BiconomyAP,
         OrangeXBP_XTAP, OrangeXBP_BitflyerAP, OrangeXBP_CoinWAP, OrangeXBP_ToobitAP, OrangeXBP_TapBitAP, OrangeX_Status
         ),
        ("Bitvenus",
         BitvenusLTP, BitvenusAP1, BitvenusAP1V,
         BitvenusBP1, BitvenusBP1V,
         BitvenusBP_BinanceAP, BitvenusBP_BybitAP, BitvenusBP_OKXAP, BitvenusBP_UpbitAP, BitvenusBP_KucoinAP,
         BitvenusBP_BitgetAP, BitvenusBP_BitstampAP
         , BitvenusBP_GeminiAP, BitvenusBP_KrakenAP, BitvenusBP_GateioAP, BitvenusBP_HTXAP, BitvenusBP_MEXCAP,
         BitvenusBP_LbankAP, BitvenusBP_BitmartAP
         , BitvenusBP_DeepcoinAP, BitvenusBP_BitfinexAP, BitvenusBP_BingXAP, BitvenusBP_OrangeXAP,
         BitvenusBP_BitvenusAP,
         BitvenusBP_BiconomyAP,
         BitvenusBP_XTAP, BitvenusBP_BitflyerAP, BitvenusBP_CoinWAP, BitvenusBP_ToobitAP, BitvenusBP_TapBitAP,
         Bitvenus_Status
         ),
        ("Biconomy",
         BiconomyLTP, BiconomyAP1, BiconomyAP1V,
         BiconomyBP1, BiconomyBP1V,
         BiconomyBP_BinanceAP, BiconomyBP_BybitAP, BiconomyBP_OKXAP, BiconomyBP_UpbitAP, BiconomyBP_KucoinAP,
         BiconomyBP_BitgetAP, BiconomyBP_BitstampAP
         , BiconomyBP_GeminiAP, BiconomyBP_KrakenAP, BiconomyBP_GateioAP, BiconomyBP_HTXAP, BiconomyBP_MEXCAP,
         BiconomyBP_LbankAP, BiconomyBP_BitmartAP
         , BiconomyBP_DeepcoinAP, BiconomyBP_BitfinexAP, BiconomyBP_BingXAP, BiconomyBP_OrangeXAP,
         BiconomyBP_BitvenusAP,
         BiconomyBP_BiconomyAP,
         BiconomyBP_XTAP, BiconomyBP_BitflyerAP, BiconomyBP_CoinWAP, BiconomyBP_ToobitAP, BiconomyBP_TapBitAP,
         Biconomy_Status
         ),
        ("Gemini", GeminiLTP,
         GeminiAP1, GeminiAP1V,
         GeminiBP1, GeminiBP1V,
         GeminiBP_BinanceAP, GeminiBP_BybitAP, GeminiBP_OKXAP, GeminiBP_UpbitAP, GeminiBP_KucoinAP,
         GeminiBP_BitgetAP, GeminiBP_BitstampAP
         , GeminiBP_GeminiAP, GeminiBP_KrakenAP, GeminiBP_GateioAP, GeminiBP_HTXAP, GeminiBP_MEXCAP,
         GeminiBP_LbankAP, GeminiBP_BitmartAP
         , GeminiBP_DeepcoinAP, GeminiBP_BitfinexAP, GeminiBP_BingXAP, GeminiBP_OrangeXAP, GeminiBP_BitvenusAP,
         GeminiBP_BiconomyAP,
         GeminiBP_XTAP, GeminiBP_BitflyerAP, GeminiBP_CoinWAP, GeminiBP_ToobitAP, GeminiBP_TapBitAP, Gemini_Status
         ),
        ("XT", XTLTP, XTAP1,
         XTAP1V,
         XTBP1, XTBP1V,
         XTBP_BinanceAP, XTBP_BybitAP, XTBP_OKXAP, XTBP_UpbitAP, XTBP_KucoinAP,
         XTBP_BitgetAP, XTBP_BitstampAP
         , XTBP_GeminiAP, XTBP_KrakenAP, XTBP_GateioAP, XTBP_HTXAP, XTBP_MEXCAP,
         XTBP_LbankAP, XTBP_BitmartAP
         , XTBP_DeepcoinAP, XTBP_BitfinexAP, XTBP_BingXAP, XTBP_OrangeXAP, XTBP_BitvenusAP,
         XTBP_BiconomyAP,
         XTBP_XTAP, XTBP_BitflyerAP, XTBP_CoinWAP, XTBP_ToobitAP, XTBP_TapBitAP, XT_Status
         ),
        ("Bitflyer", BitflyerLTP,
         BitflyerAP1, BitflyerAP1V,
         BitflyerBP1, BitflyerBP1V,
         BitflyerBP_BinanceAP, BitflyerBP_BybitAP, BitflyerBP_OKXAP, BitflyerBP_UpbitAP, BitflyerBP_KucoinAP,
         BitflyerBP_BitgetAP, BitflyerBP_BitstampAP
         , BitflyerBP_GeminiAP, BitflyerBP_KrakenAP, BitflyerBP_GateioAP, BitflyerBP_HTXAP, BitflyerBP_MEXCAP,
         BitflyerBP_LbankAP, BitflyerBP_BitmartAP
         , BitflyerBP_DeepcoinAP, BitflyerBP_BitfinexAP, BitflyerBP_BingXAP, BitflyerBP_OrangeXAP,
         BitflyerBP_BitvenusAP,
         BitflyerBP_BiconomyAP,
         BitflyerBP_XTAP, BitflyerBP_BitflyerAP, BitflyerBP_CoinWAP, BitflyerBP_ToobitAP, BitflyerBP_TapBitAP,
         Bitflyer_Status
         ),
        ("CoinW", CoinWLTP,
         CoinWAP1, CoinWAP1V,
         CoinWBP1, CoinWBP1V,
         CoinWBP_BinanceAP, CoinWBP_BybitAP, CoinWBP_OKXAP, CoinWBP_UpbitAP, CoinWBP_KucoinAP,
         CoinWBP_BitgetAP, CoinWBP_BitstampAP
         , CoinWBP_GeminiAP, CoinWBP_KrakenAP, CoinWBP_GateioAP, CoinWBP_HTXAP, CoinWBP_MEXCAP,
         CoinWBP_LbankAP, CoinWBP_BitmartAP
         , CoinWBP_DeepcoinAP, CoinWBP_BitfinexAP, CoinWBP_BingXAP, CoinWBP_OrangeXAP, CoinWBP_BitvenusAP,
         CoinWBP_BiconomyAP,
         CoinWBP_XTAP, CoinWBP_BitflyerAP, CoinWBP_CoinWAP, CoinWBP_ToobitAP, CoinWBP_TapBitAP, CoinW_Status
         ),
        ("Toobit", ToobitLTP,
         ToobitAP1, ToobitAP1V,
         ToobitBP1, ToobitBP1V,
         ToobitBP_BinanceAP, ToobitBP_BybitAP, ToobitBP_OKXAP, ToobitBP_UpbitAP, ToobitBP_KucoinAP,
         ToobitBP_BitgetAP, ToobitBP_BitstampAP
         , ToobitBP_GeminiAP, ToobitBP_KrakenAP, ToobitBP_GateioAP, ToobitBP_HTXAP, ToobitBP_MEXCAP,
         ToobitBP_LbankAP, ToobitBP_BitmartAP
         , ToobitBP_DeepcoinAP, ToobitBP_BitfinexAP, ToobitBP_BingXAP, ToobitBP_OrangeXAP, ToobitBP_BitvenusAP,
         ToobitBP_BiconomyAP,
         ToobitBP_XTAP, ToobitBP_BitflyerAP, ToobitBP_CoinWAP, ToobitBP_ToobitAP, ToobitBP_TapBitAP, Toobit_Status
         ),
        ("Tapbit", TapbitLTP,
         TapbitAP1, TapbitAP1V,
         TapbitBP1, TapbitBP1V,
         TapBitBP_BinanceAP, TapBitBP_BybitAP, TapBitBP_OKXAP, TapBitBP_UpbitAP, TapBitBP_KucoinAP,
         TapBitBP_BitgetAP, TapBitBP_BitstampAP
         , TapBitBP_GeminiAP, TapBitBP_KrakenAP, TapBitBP_GateioAP, TapBitBP_HTXAP, TapBitBP_MEXCAP,
         TapBitBP_LbankAP, TapBitBP_BitmartAP
         , TapBitBP_DeepcoinAP, TapBitBP_BitfinexAP, TapBitBP_BingXAP, TapBitBP_OrangeXAP, TapBitBP_BitvenusAP,
         TapBitBP_BiconomyAP,
         TapBitBP_XTAP, TapBitBP_BitflyerAP, TapBitBP_CoinWAP, TapBitBP_ToobitAP, TapBitBP_TapBitAP, TapBit_Status
         )

        # Add other exchanges similarly
    ]

    # Create a list to hold the threads
    threads = []

    # Create and start a thread for each PriceDifference function call
    for args in buckets_args:
        thread = threading.Thread(target=Buckets, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



async def Bid_Ask2(results,inital_time):
    start = time.perf_counter_ns()



    # Binance
    BinanceBP2 = results["BinanceBP2"]
    BinanceBP2V = results["BinanceBP2V"]
    BinanceAP2 = results["BinanceAP2"]
    BinanceAP2V = results["BinanceAP2V"]
    BinanceOBT = results["BinanceOBT"]
    BinanceLTP = results["BinanceLTP"]

    # Bybit
    BybitBP2 = results["BybitBP2"]
    BybitBP2V = results["BybitBP2V"]
    BybitAP2 = results["BybitAP2"]
    BybitAP2V = results["BybitAP2V"]
    BybitOBT = results["BybitOBT"]
    BybitLTP = results["BybitLTP"]

    # OKX
    OKXBP2 = results["OKXBP2"]
    OKXBP2V = results["OKXBP2V"]
    OKXAP2 = results["OKXAP2"]
    OKXAP2V = results["OKXAP2V"]
    OKXOBT = results["OKXOBT"]
    OKXLTP = results["OKXLTP"]

    # Upbit
    UpbitBP2 = results["UpbitBP2"]
    UpbitBP2V = results["UpbitBP2V"]
    UpbitAP2 = results["UpbitAP2"]
    UpbitAP2V = results["UpbitAP2V"]
    UpbitOBT = results["UpbitOBT"]
    UpbitLTP = results["UpbitLTP"]

    # Kucoin
    KucoinBP2 = results["KucoinBP2"]
    KucoinBP2V = results["KucoinBP2V"]
    KucoinAP2 = results["KucoinAP2"]
    KucoinAP2V = results["KucoinAP2V"]
    KucoinOBT = results["KucoinOBT"]
    KucoinLTP = results["KucoinLTP"]

    # Bitget
    BitgetBP2 = results["BitgetBP2"]
    BitgetBP2V = results["BitgetBP2V"]
    BitgetAP2 = results["BitgetAP2"]
    BitgetAP2V = results["BitgetAP2V"]
    BitgetOBT = results["BitgetOBT"]
    BitgetLTP = results["BitgetLTP"]

    # Bitstamp
    BitstampBP2 = results["BitstampBP2"]
    BitstampBP2V = results["BitstampBP2V"]
    BitstampAP2 = results["BitstampAP2"]
    BitstampAP2V = results["BitstampAP2V"]
    BitstampOBT = results["BitstampOBT"]
    BitstampLTP = results["BitstampLTP"]

    # Gemini
    GeminiBP2 = results["GeminiBP2"]
    GeminiBP2V = results["GeminiBP2V"]
    GeminiAP2 = results["GeminiAP2"]
    GeminiAP2V = results["GeminiAP2V"]
    GeminiOBT = results["GeminiOBT"]
    GeminiLTP = results["GeminiLTP"]

    # Kraken
    KrakenBP2 = results["KrakenBP2"]
    KrakenBPV2 = results["KrakenBP2V"]
    KrakenAP2 = results["KrakenAP2"]
    KrakenAPV2 = results["KrakenAP2V"]
    KrakenOBT = results["KrakenOBT"]
    KrakenLTP = results["KrakenLTP"]

    # Gateio
    GateioBP2 = results["GateioBP2"]
    GateioBPV2 = results["GateioBP2V"]
    GateioAP2 = results["GateioAP2"]
    GateioAPV2 = results["GateioAP2V"]
    GateioOBT = results["GateioOBT"]
    GateioLTP = results["GateioLTP"]

    # HTX
    HTXBP2 = results["HTXBP2"]
    HTXBP2V = results["HTXBP2V"]
    HTXAP2 = results["HTXAP2"]
    HTXAP2V = results["HTXAP2V"]
    HTXOBT = results["HTXOBT"]
    HTXLTP = results["HTXLTP"]

    # MEXC
    MEXCBP2 = results["MEXCBP2"]
    MEXCBP2V = results["MEXCBP2V"]
    MEXCAP2 = results["MEXCAP2"]
    MEXCAP2V = results["MEXCAP2V"]
    MEXCOBT = results["MEXCOBT"]
    MEXCLTP = results["MEXCLTP"]

    # Lbank
    LbankBP2 = results["LbankBP2"]
    LbankBP2V = results["LbankBP2V"]
    LbankAP2 = results["LbankAP2"]
    LbankAP2V = results["LbankAP2V"]
    LbankOBT = results["LbankOBT"]
    LbankLTP = results["LbankLTP"]

    # Bitmart
    BitmartBP2 = results["BitmartBP2"]
    BitmartBP2V = results["BitmartBP2V"]
    BitmartAP2 = results["BitmartAP2"]
    BitmartAP2V = results["BitmartAP2V"]
    BitmartOBT = results["BitmartOBT"]
    BitmartLTP = results["BitmartLTP"]

    # Deepcoin
    DeepcoinBP2 = results["DeepcoinBP2"]
    DeepcoinBP2V = results["DeepcoinBP2V"]
    DeepcoinAP2 = results["DeepcoinAP2"]
    DeepcoinAP2V = results["DeepcoinAP2V"]
    DeepcoinOBT = results["DeepcoinOBT"]
    DeepcoinLTP = results["DeepcoinLTP"]

    # Bitfinex
    BitfinexBP2 = results["BitfinexBP2"]
    BitfinexBP2V = results["BitfinexBP2V"]
    BitfinexAP2 = results["BitfinexAP2"]
    BitfinexAP2V = results["BitfinexAP2V"]
    BitfinexOBT = results["BitfinexOBT"]
    BitfinexLTP = results["BitfinexLTP"]

    # BingX
    BingXBP2 = results["BingXBP2"]
    BingXBP2V = results["BingXBP2V"]
    BingXAP2 = results["BingXAP2"]
    BingXAP2V = results["BingXAP2V"]
    BingXOBT = results["BingXOBT"]
    BingXLTP = results["BingXLTP"]

    # OrangeX
    OrangeXBP2 = results["OrangeXBP2"]
    OrangeXBP2V = results["OrangeXBP2V"]
    OrangeXAP2 = results["OrangeXAP2"]
    OrangeXAP2V = results["OrangeXAP2V"]
    OrangeXOBT = results["OrangeXOBT"]
    OrangeXLTP = results["OrangeXLTP"]

    # Bitvenus
    BitvenusBP2 = results["BitvenusBP2"]
    BitvenusBP2V = results["BitvenusBP2V"]
    BitvenusAP2 = results["BitvenusAP2"]
    BitvenusAP2V = results["BitvenusAP2V"]
    BitvenusOBT = results["BitvenusOBT"]
    BitvenusLTP = results["BitvenusLTP"]

    # Biconomy
    BiconomyBP2 = results["BiconomyBP2"]
    BiconomyBP2V = results["BiconomyBP2V"]
    BiconomyAP2 = results["BiconomyAP2"]
    BiconomyAP2V = results["BiconomyAP2V"]
    BiconomyOBT = results["BiconomyOBT"]
    BiconomyLTP = results["BiconomyLTP"]

    # XT
    XTBP2 = results["XTBP2"]
    XTBP2V = results["XTBP2V"]
    XTAP2 = results["XTAP2"]
    XTAP2V = results["XTAP2V"]
    XTOBT = results["XTOBT"]
    XTLTP = results["XTLTP"]

    # Bitflyer
    BitflyerBP2 = results["BitflyerBP2"]
    BitflyerBP2V = results["BitflyerBP2V"]
    BitflyerAP2 = results["BitflyerAP2"]
    BitflyerAP2V = results["BitflyerAP2V"]
    BitflyerOBT = results["BitflyerOBT"]
    BitflyerLTP = results["BitflyerLTP"]

    # CoinW
    CoinWBP2 = results["CoinWBP2"]
    CoinWBP2V = results["CoinWBP2V"]
    CoinWAP2 = results["CoinWAP2"]
    CoinWAP2V = results["CoinWAP2V"]
    CoinWOBT = results["CoinWOBT"]
    CoinWLTP = results["CoinWLTP"]

    # Toobit
    ToobitBP2 = results["ToobitBP2"]
    ToobitBP2V = results["ToobitBP2V"]
    ToobitAP2 = results["ToobitAP2"]
    ToobitAP2V = results["ToobitAP2V"]
    ToobitOBT = results["ToobitOBT"]
    ToobitLTP = results["ToobitLTP"]

    # TapBit
    TapbitBP2 = results["TapBitBP2"]
    TapbitBP2V = results["TapBitBP2V"]
    TapbitAP2 = results["TapBitAP2"]
    TapbitAP2V = results["TapBitAP2V"]
    TapbitOBT = results["TapBitOBT"]
    TapbitLTP = results["TapBitLTP"]

    Binance_Status = results['Binance_Status']
    BybitStatus = results['Bybit_Status']
    OKX_Status = results['OKX_Status']
    Upbit_Status = results['Upbit_Status']
    Kucoin_Status = results['Kucoin_Status']
    Bitget_Status = results['Bitget_Status']
    Bitstamp_Status = results['Bitstamp_Status']
    Gemini_Status = results['Gemini_Status']
    Kraken_Status = results['Kraken_Status']
    Gateio_Status = results['Gateio_Status']
    HTX_Status = results['HTX_Status']
    MEXC_Status = results['MEXC_Status']
    Lbank_Status = results['Lbank_Status']
    Bitmart_Status = results['Bitmart_Status']
    Deepcoin_Status = results['Deepcoin_Status']
    Bitfinex_Status = results['Bitfinex_Status']
    BingX_Status = results['BingX_Status']
    OrangeX_Status = results['OrangeX_Status']
    Bitvenus_Status = results['Bitvenus_Status']
    Biconomy_Status = results['Biconomy_Status']
    XT_Status = results['XT_Status']
    Bitflyer_Status = results['Bitflyer_Status']
    CoinW_Status = results['CoinW_Status']
    Toobit_Status = results['Toobit_Status']
    TapBit_Status = results['TapBit_Status']

    bid_prices = {
        "Binance": BinanceBP2,
        "Bybit": BybitBP2,
        "OKX": OKXBP2,
        "Upbit": UpbitBP2,
        "Kucoin": KucoinBP2,
        "Bitget": BitgetBP2,
        "Bitstamp": BitstampBP2,
        "Gemini": GeminiBP2,
        "Kraken": KrakenBP2,
        "Gate.io": GateioBP2,
        "HTX": HTXBP2,
        "MEXC": MEXCBP2,
        "Lbank": LbankBP2,
        "Bitmart": BitmartBP2,
        "Deepcoin": DeepcoinBP2,
        "Bitfinex": BitfinexBP2,
        "BingX": BingXBP2,
        "OrangeX": OrangeXBP2,
        "Bitvenus": BitvenusBP2,
        "Biconomy": BiconomyBP2,
        "XT": XTBP2,
        "Bitflyer": BitflyerBP2,
        "CoinW": CoinWBP2,
        "Toobit": ToobitBP2,
        "TapBit": TapbitBP2
    }

    ask_prices = {
        "Binance": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bybit": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "OKX": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Upbit": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Kucoin": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitget": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitstamp": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Gemini": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Kraken": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Gate.io": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "HTX": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "MEXC": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Lbank": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitmart": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Deepcoin": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitfinex": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "BingX": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "OrangeX": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitvenus": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Biconomy": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "XT": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Bitflyer": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "CoinW": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "Toobit": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        },
        "TapBit": {
            "Binance": BinanceAP2,
            "Bybit": BybitAP2,
            "OKX": OKXAP2,
            "Upbit": UpbitAP2,
            "Kucoin": KucoinAP2,
            "Bitget": BitgetAP2,
            "Bitstamp": BitstampAP2,
            "Gemini": GeminiAP2,
            "Kraken": KrakenAP2,
            "Gate.io": GateioAP2,
            "HTX": HTXAP2,
            "MEXC": MEXCAP2,
            "Lbank": LbankAP2,
            "Bitmart": BitmartAP2,
            "Deepcoin": DeepcoinAP2,
            "Bitfinex": BitfinexAP2,
            "BingX": BingXAP2,
            "OrangeX": OrangeXAP2,
            "Bitvenus": BitvenusAP2,
            "Biconomy": BiconomyAP2,
            "XT": XTAP2,
            "Bitflyer": BitflyerAP2,
            "CoinW": CoinWAP2,
            "Toobit": ToobitAP2,
            "TapBit": TapbitAP2
        }
    }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect differences from all exchanges
    all_differences = {}
    for exchange in exchanges:
        all_differences.update(exchange.get_differences())

    results = {}
    for key, value in all_differences.items():
        results[key] = value

    # Print stored variables
    for key in sorted(results.keys()):
        results[key]

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_Gate.ioAP']
    BinanceBP_HTXAP = results['BinanceBP_HTXAP']
    BinanceBP_MEXCAP = results['BinanceBP_MEXCAP']
    BinanceBP_LbankAP = results['BinanceBP_LbankAP']
    BinanceBP_BitmartAP = results['BinanceBP_BitmartAP']
    BinanceBP_DeepcoinAP = results['BinanceBP_DeepcoinAP']
    BinanceBP_BitfinexAP = results['BinanceBP_BitfinexAP']
    BinanceBP_BingXAP = results['BinanceBP_BingXAP']
    BinanceBP_OrangeXAP = results['BinanceBP_OrangeXAP']
    BinanceBP_BitvenusAP = results['BinanceBP_BitvenusAP']
    BinanceBP_BiconomyAP = results['BinanceBP_BiconomyAP']
    BinanceBP_XTAP = results['BinanceBP_XTAP']
    BinanceBP_BitflyerAP = results['BinanceBP_BitflyerAP']
    BinanceBP_CoinWAP = results['BinanceBP_CoinWAP']
    BinanceBP_ToobitAP = results['BinanceBP_ToobitAP']
    BinanceBP_TapBitAP = results['BinanceBP_TapBitAP']

    BybitBP_BinanceAP = results['BybitBP_BinanceAP']
    BybitBP_BybitAP = results['BybitBP_BybitAP']
    BybitBP_OKXAP = results['BybitBP_OKXAP']
    BybitBP_UpbitAP = results['BybitBP_UpbitAP']
    BybitBP_KucoinAP = results['BybitBP_KucoinAP']
    BybitBP_BitgetAP = results['BybitBP_BitgetAP']
    BybitBP_BitstampAP = results['BybitBP_BitstampAP']
    BybitBP_GeminiAP = results['BybitBP_GeminiAP']
    BybitBP_KrakenAP = results['BybitBP_KrakenAP']
    BybitBP_GateioAP = results['BybitBP_Gate.ioAP']
    BybitBP_HTXAP = results['BybitBP_HTXAP']
    BybitBP_MEXCAP = results['BybitBP_MEXCAP']
    BybitBP_LbankAP = results['BybitBP_LbankAP']
    BybitBP_BitmartAP = results['BybitBP_BitmartAP']
    BybitBP_DeepcoinAP = results['BybitBP_DeepcoinAP']
    BybitBP_BitfinexAP = results['BybitBP_BitfinexAP']
    BybitBP_BingXAP = results['BybitBP_BingXAP']
    BybitBP_OrangeXAP = results['BybitBP_OrangeXAP']
    BybitBP_BitvenusAP = results['BybitBP_BitvenusAP']
    BybitBP_BiconomyAP = results['BybitBP_BiconomyAP']
    BybitBP_XTAP = results['BybitBP_XTAP']
    BybitBP_BitflyerAP = results['BybitBP_BitflyerAP']
    BybitBP_CoinWAP = results['BybitBP_CoinWAP']
    BybitBP_ToobitAP = results['BybitBP_ToobitAP']
    BybitBP_TapBitAP = results['BybitBP_TapBitAP']

    OKXBP_BinanceAP = results['OKXBP_BinanceAP']
    OKXBP_BybitAP = results['OKXBP_BybitAP']
    OKXBP_OKXAP = results['OKXBP_OKXAP']
    OKXBP_UpbitAP = results['OKXBP_UpbitAP']
    OKXBP_KucoinAP = results['OKXBP_KucoinAP']
    OKXBP_BitgetAP = results['OKXBP_BitgetAP']
    OKXBP_BitstampAP = results['OKXBP_BitstampAP']
    OKXBP_GeminiAP = results['OKXBP_GeminiAP']
    OKXBP_KrakenAP = results['OKXBP_KrakenAP']
    OKXBP_GateioAP = results['OKXBP_Gate.ioAP']
    OKXBP_HTXAP = results['OKXBP_HTXAP']
    OKXBP_MEXCAP = results['OKXBP_MEXCAP']
    OKXBP_LbankAP = results['OKXBP_LbankAP']
    OKXBP_BitmartAP = results['OKXBP_BitmartAP']
    OKXBP_DeepcoinAP = results['OKXBP_DeepcoinAP']
    OKXBP_BitfinexAP = results['OKXBP_BitfinexAP']
    OKXBP_BingXAP = results['OKXBP_BingXAP']
    OKXBP_OrangeXAP = results['OKXBP_OrangeXAP']
    OKXBP_BitvenusAP = results['OKXBP_BitvenusAP']
    OKXBP_BiconomyAP = results['OKXBP_BiconomyAP']
    OKXBP_XTAP = results['OKXBP_XTAP']
    OKXBP_BitflyerAP = results['OKXBP_BitflyerAP']
    OKXBP_CoinWAP = results['OKXBP_CoinWAP']
    OKXBP_ToobitAP = results['OKXBP_ToobitAP']
    OKXBP_TapBitAP = results['OKXBP_TapBitAP']

    UpbitBP_BinanceAP = results['UpbitBP_BinanceAP']
    UpbitBP_BybitAP = results['UpbitBP_BybitAP']
    UpbitBP_OKXAP = results['UpbitBP_OKXAP']
    UpbitBP_UpbitAP = results['UpbitBP_UpbitAP']
    UpbitBP_KucoinAP = results['UpbitBP_KucoinAP']
    UpbitBP_BitgetAP = results['UpbitBP_BitgetAP']
    UpbitBP_BitstampAP = results['UpbitBP_BitstampAP']
    UpbitBP_GeminiAP = results['UpbitBP_GeminiAP']
    UpbitBP_KrakenAP = results['UpbitBP_KrakenAP']
    UpbitBP_GateioAP = results['UpbitBP_Gate.ioAP']
    UpbitBP_HTXAP = results['UpbitBP_HTXAP']
    UpbitBP_MEXCAP = results['UpbitBP_MEXCAP']
    UpbitBP_LbankAP = results['UpbitBP_LbankAP']
    UpbitBP_BitmartAP = results['UpbitBP_BitmartAP']
    UpbitBP_DeepcoinAP = results['UpbitBP_DeepcoinAP']
    UpbitBP_BitfinexAP = results['UpbitBP_BitfinexAP']
    UpbitBP_BingXAP = results['UpbitBP_BingXAP']
    UpbitBP_OrangeXAP = results['UpbitBP_OrangeXAP']
    UpbitBP_BitvenusAP = results['UpbitBP_BitvenusAP']
    UpbitBP_BiconomyAP = results['UpbitBP_BiconomyAP']
    UpbitBP_XTAP = results['UpbitBP_XTAP']
    UpbitBP_BitflyerAP = results['UpbitBP_BitflyerAP']
    UpbitBP_CoinWAP = results['UpbitBP_CoinWAP']
    UpbitBP_ToobitAP = results['UpbitBP_ToobitAP']
    UpbitBP_TapBitAP = results['UpbitBP_TapBitAP']

    KucoinBP_BinanceAP = results['KucoinBP_BinanceAP']
    KucoinBP_BybitAP = results['KucoinBP_BybitAP']
    KucoinBP_OKXAP = results['KucoinBP_OKXAP']
    KucoinBP_UpbitAP = results['KucoinBP_UpbitAP']
    KucoinBP_KucoinAP = results['KucoinBP_KucoinAP']
    KucoinBP_BitgetAP = results['KucoinBP_BitgetAP']
    KucoinBP_BitstampAP = results['KucoinBP_BitstampAP']
    KucoinBP_GeminiAP = results['KucoinBP_GeminiAP']
    KucoinBP_KrakenAP = results['KucoinBP_KrakenAP']
    KucoinBP_GateioAP = results['KucoinBP_Gate.ioAP']
    KucoinBP_HTXAP = results['KucoinBP_HTXAP']
    KucoinBP_MEXCAP = results['KucoinBP_MEXCAP']
    KucoinBP_LbankAP = results['KucoinBP_LbankAP']
    KucoinBP_BitmartAP = results['KucoinBP_BitmartAP']
    KucoinBP_DeepcoinAP = results['KucoinBP_DeepcoinAP']
    KucoinBP_BitfinexAP = results['KucoinBP_BitfinexAP']
    KucoinBP_BingXAP = results['KucoinBP_BingXAP']
    KucoinBP_OrangeXAP = results['KucoinBP_OrangeXAP']
    KucoinBP_BitvenusAP = results['KucoinBP_BitvenusAP']
    KucoinBP_BiconomyAP = results['KucoinBP_BiconomyAP']
    KucoinBP_XTAP = results['KucoinBP_XTAP']
    KucoinBP_BitflyerAP = results['KucoinBP_BitflyerAP']
    KucoinBP_CoinWAP = results['KucoinBP_CoinWAP']
    KucoinBP_ToobitAP = results['KucoinBP_ToobitAP']
    KucoinBP_TapBitAP = results['KucoinBP_TapBitAP']

    BitgetBP_BinanceAP = results['BitgetBP_BinanceAP']
    BitgetBP_BybitAP = results['BitgetBP_BybitAP']
    BitgetBP_OKXAP = results['BitgetBP_OKXAP']
    BitgetBP_UpbitAP = results['BitgetBP_UpbitAP']
    BitgetBP_KucoinAP = results['BitgetBP_KucoinAP']
    BitgetBP_BitgetAP = results['BitgetBP_BitgetAP']
    BitgetBP_BitstampAP = results['BitgetBP_BitstampAP']
    BitgetBP_GeminiAP = results['BitgetBP_GeminiAP']
    BitgetBP_KrakenAP = results['BitgetBP_KrakenAP']
    BitgetBP_GateioAP = results['BitgetBP_Gate.ioAP']
    BitgetBP_HTXAP = results['BitgetBP_HTXAP']
    BitgetBP_MEXCAP = results['BitgetBP_MEXCAP']
    BitgetBP_LbankAP = results['BitgetBP_LbankAP']
    BitgetBP_BitmartAP = results['BitgetBP_BitmartAP']
    BitgetBP_DeepcoinAP = results['BitgetBP_DeepcoinAP']
    BitgetBP_BitfinexAP = results['BitgetBP_BitfinexAP']
    BitgetBP_BingXAP = results['BitgetBP_BingXAP']
    BitgetBP_OrangeXAP = results['BitgetBP_OrangeXAP']
    BitgetBP_BitvenusAP = results['BitgetBP_BitvenusAP']
    BitgetBP_BiconomyAP = results['BitgetBP_BiconomyAP']
    BitgetBP_XTAP = results['BitgetBP_XTAP']
    BitgetBP_BitflyerAP = results['BitgetBP_BitflyerAP']
    BitgetBP_CoinWAP = results['BitgetBP_CoinWAP']
    BitgetBP_ToobitAP = results['BitgetBP_ToobitAP']
    BitgetBP_TapBitAP = results['BitgetBP_TapBitAP']

    BitstampBP_BinanceAP = results['BitstampBP_BinanceAP']
    BitstampBP_BybitAP = results['BitstampBP_BybitAP']
    BitstampBP_OKXAP = results['BitstampBP_OKXAP']
    BitstampBP_UpbitAP = results['BitstampBP_UpbitAP']
    BitstampBP_KucoinAP = results['BitstampBP_KucoinAP']
    BitstampBP_BitgetAP = results['BitstampBP_BitgetAP']
    BitstampBP_BitstampAP = results['BitstampBP_BitstampAP']
    BitstampBP_GeminiAP = results['BitstampBP_GeminiAP']
    BitstampBP_KrakenAP = results['BitstampBP_KrakenAP']
    BitstampBP_GateioAP = results['BitstampBP_Gate.ioAP']
    BitstampBP_HTXAP = results['BitstampBP_HTXAP']
    BitstampBP_MEXCAP = results['BitstampBP_MEXCAP']
    BitstampBP_LbankAP = results['BitstampBP_LbankAP']
    BitstampBP_BitmartAP = results['BitstampBP_BitmartAP']
    BitstampBP_DeepcoinAP = results['BitstampBP_DeepcoinAP']
    BitstampBP_BitfinexAP = results['BitstampBP_BitfinexAP']
    BitstampBP_BingXAP = results['BitstampBP_BingXAP']
    BitstampBP_OrangeXAP = results['BitstampBP_OrangeXAP']
    BitstampBP_BitvenusAP = results['BitstampBP_BitvenusAP']
    BitstampBP_BiconomyAP = results['BitstampBP_BiconomyAP']
    BitstampBP_XTAP = results['BitstampBP_XTAP']
    BitstampBP_BitflyerAP = results['BitstampBP_BitflyerAP']
    BitstampBP_CoinWAP = results['BitstampBP_CoinWAP']
    BitstampBP_ToobitAP = results['BitstampBP_ToobitAP']
    BitstampBP_TapBitAP = results['BitstampBP_TapBitAP']

    GeminiBP_BinanceAP = results['GeminiBP_BinanceAP']
    GeminiBP_BybitAP = results['GeminiBP_BybitAP']
    GeminiBP_OKXAP = results['GeminiBP_OKXAP']
    GeminiBP_UpbitAP = results['GeminiBP_UpbitAP']
    GeminiBP_KucoinAP = results['GeminiBP_KucoinAP']
    GeminiBP_BitgetAP = results['GeminiBP_BitgetAP']
    GeminiBP_BitstampAP = results['GeminiBP_BitstampAP']
    GeminiBP_GeminiAP = results['GeminiBP_GeminiAP']
    GeminiBP_KrakenAP = results['GeminiBP_KrakenAP']
    GeminiBP_GateioAP = results['GeminiBP_Gate.ioAP']
    GeminiBP_HTXAP = results['GeminiBP_HTXAP']
    GeminiBP_MEXCAP = results['GeminiBP_MEXCAP']
    GeminiBP_LbankAP = results['GeminiBP_LbankAP']
    GeminiBP_BitmartAP = results['GeminiBP_BitmartAP']
    GeminiBP_DeepcoinAP = results['GeminiBP_DeepcoinAP']
    GeminiBP_BitfinexAP = results['GeminiBP_BitfinexAP']
    GeminiBP_BingXAP = results['GeminiBP_BingXAP']
    GeminiBP_OrangeXAP = results['GeminiBP_OrangeXAP']
    GeminiBP_BitvenusAP = results['GeminiBP_BitvenusAP']
    GeminiBP_BiconomyAP = results['GeminiBP_BiconomyAP']
    GeminiBP_XTAP = results['GeminiBP_XTAP']
    GeminiBP_BitflyerAP = results['GeminiBP_BitflyerAP']
    GeminiBP_CoinWAP = results['GeminiBP_CoinWAP']
    GeminiBP_ToobitAP = results['GeminiBP_ToobitAP']
    GeminiBP_TapBitAP = results['GeminiBP_TapBitAP']

    KrakenBP_BinanceAP = results['KrakenBP_BinanceAP']
    KrakenBP_BybitAP = results['KrakenBP_BybitAP']
    KrakenBP_OKXAP = results['KrakenBP_OKXAP']
    KrakenBP_UpbitAP = results['KrakenBP_UpbitAP']
    KrakenBP_KucoinAP = results['KrakenBP_KucoinAP']
    KrakenBP_BitgetAP = results['KrakenBP_BitgetAP']
    KrakenBP_BitstampAP = results['KrakenBP_BitstampAP']
    KrakenBP_GeminiAP = results['KrakenBP_GeminiAP']
    KrakenBP_KrakenAP = results['KrakenBP_KrakenAP']
    KrakenBP_GateioAP = results['KrakenBP_Gate.ioAP']
    KrakenBP_HTXAP = results['KrakenBP_HTXAP']
    KrakenBP_MEXCAP = results['KrakenBP_MEXCAP']
    KrakenBP_LbankAP = results['KrakenBP_LbankAP']
    KrakenBP_BitmartAP = results['KrakenBP_BitmartAP']
    KrakenBP_DeepcoinAP = results['KrakenBP_DeepcoinAP']
    KrakenBP_BitfinexAP = results['KrakenBP_BitfinexAP']
    KrakenBP_BingXAP = results['KrakenBP_BingXAP']
    KrakenBP_OrangeXAP = results['KrakenBP_OrangeXAP']
    KrakenBP_BitvenusAP = results['KrakenBP_BitvenusAP']
    KrakenBP_BiconomyAP = results['KrakenBP_BiconomyAP']
    KrakenBP_XTAP = results['KrakenBP_XTAP']
    KrakenBP_BitflyerAP = results['KrakenBP_BitflyerAP']
    KrakenBP_CoinWAP = results['KrakenBP_CoinWAP']
    KrakenBP_ToobitAP = results['KrakenBP_ToobitAP']
    KrakenBP_TapBitAP = results['KrakenBP_TapBitAP']

    GateioBP_BinanceAP = results['Gate.ioBP_BinanceAP']
    GateioBP_BybitAP = results['Gate.ioBP_BybitAP']
    GateioBP_OKXAP = results['Gate.ioBP_OKXAP']
    GateioBP_UpbitAP = results['Gate.ioBP_UpbitAP']
    GateioBP_KucoinAP = results['Gate.ioBP_KucoinAP']
    GateioBP_BitgetAP = results['Gate.ioBP_BitgetAP']
    GateioBP_BitstampAP = results['Gate.ioBP_BitstampAP']
    GateioBP_GeminiAP = results['Gate.ioBP_GeminiAP']
    GateioBP_KrakenAP = results['Gate.ioBP_KrakenAP']
    GateioBP_GateioAP = results['Gate.ioBP_Gate.ioAP']
    GateioBP_HTXAP = results['Gate.ioBP_HTXAP']
    GateioBP_MEXCAP = results['Gate.ioBP_MEXCAP']
    GateioBP_LbankAP = results['Gate.ioBP_LbankAP']
    GateioBP_BitmartAP = results['Gate.ioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['Gate.ioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['Gate.ioBP_BitfinexAP']
    GateioBP_BingXAP = results['Gate.ioBP_BingXAP']
    GateioBP_OrangeXAP = results['Gate.ioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['Gate.ioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['Gate.ioBP_BiconomyAP']
    GateioBP_XTAP = results['Gate.ioBP_XTAP']
    GateioBP_BitflyerAP = results['Gate.ioBP_BitflyerAP']
    GateioBP_CoinWAP = results['Gate.ioBP_CoinWAP']
    GateioBP_ToobitAP = results['Gate.ioBP_ToobitAP']
    GateioBP_TapBitAP = results['Gate.ioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_Gate.ioAP']
    HTXBP_HTXAP = results['HTXBP_HTXAP']
    HTXBP_MEXCAP = results['HTXBP_MEXCAP']
    HTXBP_LbankAP = results['HTXBP_LbankAP']
    HTXBP_BitmartAP = results['HTXBP_BitmartAP']
    HTXBP_DeepcoinAP = results['HTXBP_DeepcoinAP']
    HTXBP_BitfinexAP = results['HTXBP_BitfinexAP']
    HTXBP_BingXAP = results['HTXBP_BingXAP']
    HTXBP_OrangeXAP = results['HTXBP_OrangeXAP']
    HTXBP_BitvenusAP = results['HTXBP_BitvenusAP']
    HTXBP_BiconomyAP = results['HTXBP_BiconomyAP']
    HTXBP_XTAP = results['HTXBP_XTAP']
    HTXBP_BitflyerAP = results['HTXBP_BitflyerAP']
    HTXBP_CoinWAP = results['HTXBP_CoinWAP']
    HTXBP_ToobitAP = results['HTXBP_ToobitAP']
    HTXBP_TapBitAP = results['HTXBP_TapBitAP']

    MEXCBP_BinanceAP = results['MEXCBP_BinanceAP']
    MEXCBP_BybitAP = results['MEXCBP_BybitAP']
    MEXCBP_OKXAP = results['MEXCBP_OKXAP']
    MEXCBP_UpbitAP = results['MEXCBP_UpbitAP']
    MEXCBP_KucoinAP = results['MEXCBP_KucoinAP']
    MEXCBP_BitgetAP = results['MEXCBP_BitgetAP']
    MEXCBP_BitstampAP = results['MEXCBP_BitstampAP']
    MEXCBP_GeminiAP = results['MEXCBP_GeminiAP']
    MEXCBP_KrakenAP = results['MEXCBP_KrakenAP']
    MEXCBP_GateioAP = results['BinanceBP_Gate.ioAP']
    MEXCBP_HTXAP = results['MEXCBP_HTXAP']
    MEXCBP_MEXCAP = results['MEXCBP_MEXCAP']
    MEXCBP_LbankAP = results['MEXCBP_LbankAP']
    MEXCBP_BitmartAP = results['MEXCBP_BitmartAP']
    MEXCBP_DeepcoinAP = results['MEXCBP_DeepcoinAP']
    MEXCBP_BitfinexAP = results['MEXCBP_BitfinexAP']
    MEXCBP_BingXAP = results['MEXCBP_BingXAP']
    MEXCBP_OrangeXAP = results['MEXCBP_OrangeXAP']
    MEXCBP_BitvenusAP = results['MEXCBP_BitvenusAP']
    MEXCBP_BiconomyAP = results['MEXCBP_BiconomyAP']
    MEXCBP_XTAP = results['MEXCBP_XTAP']
    MEXCBP_BitflyerAP = results['MEXCBP_BitflyerAP']
    MEXCBP_CoinWAP = results['MEXCBP_CoinWAP']
    MEXCBP_ToobitAP = results['MEXCBP_ToobitAP']
    MEXCBP_TapBitAP = results['MEXCBP_TapBitAP']

    LbankBP_BinanceAP = results['LbankBP_BinanceAP']
    LbankBP_BybitAP = results['LbankBP_BybitAP']
    LbankBP_OKXAP = results['LbankBP_OKXAP']
    LbankBP_UpbitAP = results['LbankBP_UpbitAP']
    LbankBP_KucoinAP = results['LbankBP_KucoinAP']
    LbankBP_BitgetAP = results['LbankBP_BitgetAP']
    LbankBP_BitstampAP = results['LbankBP_BitstampAP']
    LbankBP_GeminiAP = results['LbankBP_GeminiAP']
    LbankBP_KrakenAP = results['LbankBP_KrakenAP']
    LbankBP_GateioAP = results['LbankBP_Gate.ioAP']
    LbankBP_HTXAP = results['LbankBP_HTXAP']
    LbankBP_MEXCAP = results['LbankBP_MEXCAP']
    LbankBP_LbankAP = results['LbankBP_LbankAP']
    LbankBP_BitmartAP = results['LbankBP_BitmartAP']
    LbankBP_DeepcoinAP = results['LbankBP_DeepcoinAP']
    LbankBP_BitfinexAP = results['LbankBP_BitfinexAP']
    LbankBP_BingXAP = results['LbankBP_BingXAP']
    LbankBP_OrangeXAP = results['LbankBP_OrangeXAP']
    LbankBP_BitvenusAP = results['LbankBP_BitvenusAP']
    LbankBP_BiconomyAP = results['LbankBP_BiconomyAP']
    LbankBP_XTAP = results['LbankBP_XTAP']
    LbankBP_BitflyerAP = results['LbankBP_BitflyerAP']
    LbankBP_CoinWAP = results['LbankBP_CoinWAP']
    LbankBP_ToobitAP = results['LbankBP_ToobitAP']
    LbankBP_TapBitAP = results['LbankBP_TapBitAP']

    BitmartBP_BinanceAP = results['BitmartBP_BinanceAP']
    BitmartBP_BybitAP = results['BitmartBP_BybitAP']
    BitmartBP_OKXAP = results['BitmartBP_OKXAP']
    BitmartBP_UpbitAP = results['BitmartBP_UpbitAP']
    BitmartBP_KucoinAP = results['BitmartBP_KucoinAP']
    BitmartBP_BitgetAP = results['BitmartBP_BitgetAP']
    BitmartBP_BitstampAP = results['BitmartBP_BitstampAP']
    BitmartBP_GeminiAP = results['BitmartBP_GeminiAP']
    BitmartBP_KrakenAP = results['BitmartBP_KrakenAP']
    BitmartBP_GateioAP = results['BitmartBP_Gate.ioAP']
    BitmartBP_HTXAP = results['BitmartBP_HTXAP']
    BitmartBP_MEXCAP = results['BitmartBP_MEXCAP']
    BitmartBP_LbankAP = results['BitmartBP_LbankAP']
    BitmartBP_BitmartAP = results['BitmartBP_BitmartAP']
    BitmartBP_DeepcoinAP = results['BitmartBP_DeepcoinAP']
    BitmartBP_BitfinexAP = results['BitmartBP_BitfinexAP']
    BitmartBP_BingXAP = results['BitmartBP_BingXAP']
    BitmartBP_OrangeXAP = results['BitmartBP_OrangeXAP']
    BitmartBP_BitvenusAP = results['BitmartBP_BitvenusAP']
    BitmartBP_BiconomyAP = results['BitmartBP_BiconomyAP']
    BitmartBP_XTAP = results['BitmartBP_XTAP']
    BitmartBP_BitflyerAP = results['BitmartBP_BitflyerAP']
    BitmartBP_CoinWAP = results['BitmartBP_CoinWAP']
    BitmartBP_ToobitAP = results['BitmartBP_ToobitAP']
    BitmartBP_TapBitAP = results['BitmartBP_TapBitAP']

    DeepcoinBP_BinanceAP = results['DeepcoinBP_BinanceAP']
    DeepcoinBP_BybitAP = results['DeepcoinBP_BybitAP']
    DeepcoinBP_OKXAP = results['DeepcoinBP_OKXAP']
    DeepcoinBP_UpbitAP = results['DeepcoinBP_UpbitAP']
    DeepcoinBP_KucoinAP = results['DeepcoinBP_KucoinAP']
    DeepcoinBP_BitgetAP = results['DeepcoinBP_BitgetAP']
    DeepcoinBP_BitstampAP = results['DeepcoinBP_BitstampAP']
    DeepcoinBP_GeminiAP = results['DeepcoinBP_GeminiAP']
    DeepcoinBP_KrakenAP = results['DeepcoinBP_KrakenAP']
    DeepcoinBP_GateioAP = results['DeepcoinBP_Gate.ioAP']
    DeepcoinBP_HTXAP = results['DeepcoinBP_HTXAP']
    DeepcoinBP_MEXCAP = results['DeepcoinBP_MEXCAP']
    DeepcoinBP_LbankAP = results['DeepcoinBP_LbankAP']
    DeepcoinBP_BitmartAP = results['DeepcoinBP_BitmartAP']
    DeepcoinBP_DeepcoinAP = results['DeepcoinBP_DeepcoinAP']
    DeepcoinBP_BitfinexAP = results['DeepcoinBP_BitfinexAP']
    DeepcoinBP_BingXAP = results['DeepcoinBP_BingXAP']
    DeepcoinBP_OrangeXAP = results['DeepcoinBP_OrangeXAP']
    DeepcoinBP_BitvenusAP = results['DeepcoinBP_BitvenusAP']
    DeepcoinBP_BiconomyAP = results['DeepcoinBP_BiconomyAP']
    DeepcoinBP_XTAP = results['DeepcoinBP_XTAP']
    DeepcoinBP_BitflyerAP = results['DeepcoinBP_BitflyerAP']
    DeepcoinBP_CoinWAP = results['DeepcoinBP_CoinWAP']
    DeepcoinBP_ToobitAP = results['DeepcoinBP_ToobitAP']
    DeepcoinBP_TapBitAP = results['DeepcoinBP_TapBitAP']

    BitfinexBP_BinanceAP = results['BitfinexBP_BinanceAP']
    BitfinexBP_BybitAP = results['BitfinexBP_BybitAP']
    BitfinexBP_OKXAP = results['BitfinexBP_OKXAP']
    BitfinexBP_UpbitAP = results['BitfinexBP_UpbitAP']
    BitfinexBP_KucoinAP = results['BitfinexBP_KucoinAP']
    BitfinexBP_BitgetAP = results['BitfinexBP_BitgetAP']
    BitfinexBP_BitstampAP = results['BitfinexBP_BitstampAP']
    BitfinexBP_GeminiAP = results['BitfinexBP_GeminiAP']
    BitfinexBP_KrakenAP = results['BitfinexBP_KrakenAP']
    BitfinexBP_GateioAP = results['BitfinexBP_Gate.ioAP']
    BitfinexBP_HTXAP = results['BitfinexBP_HTXAP']
    BitfinexBP_MEXCAP = results['BitfinexBP_MEXCAP']
    BitfinexBP_LbankAP = results['BitfinexBP_LbankAP']
    BitfinexBP_BitmartAP = results['BitfinexBP_BitmartAP']
    BitfinexBP_DeepcoinAP = results['BitfinexBP_DeepcoinAP']
    BitfinexBP_BitfinexAP = results['BitfinexBP_BitfinexAP']
    BitfinexBP_BingXAP = results['BitfinexBP_BingXAP']
    BitfinexBP_OrangeXAP = results['BitfinexBP_OrangeXAP']
    BitfinexBP_BitvenusAP = results['BitfinexBP_BitvenusAP']
    BitfinexBP_BiconomyAP = results['BitfinexBP_BiconomyAP']
    BitfinexBP_XTAP = results['BitfinexBP_XTAP']
    BitfinexBP_BitflyerAP = results['BitfinexBP_BitflyerAP']
    BitfinexBP_CoinWAP = results['BitfinexBP_CoinWAP']
    BitfinexBP_ToobitAP = results['BitfinexBP_ToobitAP']
    BitfinexBP_TapBitAP = results['BitfinexBP_TapBitAP']

    BingXBP_BinanceAP = results['BingXBP_BinanceAP']
    BingXBP_BybitAP = results['BingXBP_BybitAP']
    BingXBP_OKXAP = results['BingXBP_OKXAP']
    BingXBP_UpbitAP = results['BingXBP_UpbitAP']
    BingXBP_KucoinAP = results['BingXBP_KucoinAP']
    BingXBP_BitgetAP = results['BingXBP_BitgetAP']
    BingXBP_BitstampAP = results['BingXBP_BitstampAP']
    BingXBP_GeminiAP = results['BingXBP_GeminiAP']
    BingXBP_KrakenAP = results['BingXBP_KrakenAP']
    BingXBP_GateioAP = results['BingXBP_Gate.ioAP']
    BingXBP_HTXAP = results['BingXBP_HTXAP']
    BingXBP_MEXCAP = results['BingXBP_MEXCAP']
    BingXBP_LbankAP = results['BingXBP_LbankAP']
    BingXBP_BitmartAP = results['BingXBP_BitmartAP']
    BingXBP_DeepcoinAP = results['BingXBP_DeepcoinAP']
    BingXBP_BitfinexAP = results['BingXBP_BitfinexAP']
    BingXBP_BingXAP = results['BingXBP_BingXAP']
    BingXBP_OrangeXAP = results['BingXBP_OrangeXAP']
    BingXBP_BitvenusAP = results['BingXBP_BitvenusAP']
    BingXBP_BiconomyAP = results['BingXBP_BiconomyAP']
    BingXBP_XTAP = results['BingXBP_XTAP']
    BingXBP_BitflyerAP = results['BingXBP_BitflyerAP']
    BingXBP_CoinWAP = results['BingXBP_CoinWAP']
    BingXBP_ToobitAP = results['BingXBP_ToobitAP']
    BingXBP_TapBitAP = results['BingXBP_TapBitAP']

    OrangeXBP_BinanceAP = results['OrangeXBP_BinanceAP']
    OrangeXBP_BybitAP = results['OrangeXBP_BybitAP']
    OrangeXBP_OKXAP = results['OrangeXBP_OKXAP']
    OrangeXBP_UpbitAP = results['OrangeXBP_UpbitAP']
    OrangeXBP_KucoinAP = results['OrangeXBP_KucoinAP']
    OrangeXBP_BitgetAP = results['OrangeXBP_BitgetAP']
    OrangeXBP_BitstampAP = results['OrangeXBP_BitstampAP']
    OrangeXBP_GeminiAP = results['OrangeXBP_GeminiAP']
    OrangeXBP_KrakenAP = results['OrangeXBP_KrakenAP']
    OrangeXBP_GateioAP = results['OrangeXBP_Gate.ioAP']
    OrangeXBP_HTXAP = results['OrangeXBP_HTXAP']
    OrangeXBP_MEXCAP = results['OrangeXBP_MEXCAP']
    OrangeXBP_LbankAP = results['OrangeXBP_LbankAP']
    OrangeXBP_BitmartAP = results['OrangeXBP_BitmartAP']
    OrangeXBP_DeepcoinAP = results['OrangeXBP_DeepcoinAP']
    OrangeXBP_BitfinexAP = results['OrangeXBP_BitfinexAP']
    OrangeXBP_BingXAP = results['OrangeXBP_BingXAP']
    OrangeXBP_OrangeXAP = results['OrangeXBP_OrangeXAP']
    OrangeXBP_BitvenusAP = results['OrangeXBP_BitvenusAP']
    OrangeXBP_BiconomyAP = results['OrangeXBP_BiconomyAP']
    OrangeXBP_XTAP = results['OrangeXBP_XTAP']
    OrangeXBP_BitflyerAP = results['OrangeXBP_BitflyerAP']
    OrangeXBP_CoinWAP = results['OrangeXBP_CoinWAP']
    OrangeXBP_ToobitAP = results['OrangeXBP_ToobitAP']
    OrangeXBP_TapBitAP = results['OrangeXBP_TapBitAP']

    BitvenusBP_BinanceAP = results['BitvenusBP_BinanceAP']
    BitvenusBP_BybitAP = results['BitvenusBP_BybitAP']
    BitvenusBP_OKXAP = results['BitvenusBP_OKXAP']
    BitvenusBP_UpbitAP = results['BitvenusBP_UpbitAP']
    BitvenusBP_KucoinAP = results['BitvenusBP_KucoinAP']
    BitvenusBP_BitgetAP = results['BitvenusBP_BitgetAP']
    BitvenusBP_BitstampAP = results['BitvenusBP_BitstampAP']
    BitvenusBP_GeminiAP = results['BitvenusBP_GeminiAP']
    BitvenusBP_KrakenAP = results['BitvenusBP_KrakenAP']
    BitvenusBP_GateioAP = results['BitvenusBP_Gate.ioAP']
    BitvenusBP_HTXAP = results['BitvenusBP_HTXAP']
    BitvenusBP_MEXCAP = results['BitvenusBP_MEXCAP']
    BitvenusBP_LbankAP = results['BitvenusBP_LbankAP']
    BitvenusBP_BitmartAP = results['BitvenusBP_BitmartAP']
    BitvenusBP_DeepcoinAP = results['BitvenusBP_DeepcoinAP']
    BitvenusBP_BitfinexAP = results['BitvenusBP_BitfinexAP']
    BitvenusBP_BingXAP = results['BitvenusBP_BingXAP']
    BitvenusBP_OrangeXAP = results['BitvenusBP_OrangeXAP']
    BitvenusBP_BitvenusAP = results['BitvenusBP_BitvenusAP']
    BitvenusBP_BiconomyAP = results['BitvenusBP_BiconomyAP']
    BitvenusBP_XTAP = results['BitvenusBP_XTAP']
    BitvenusBP_BitflyerAP = results['BitvenusBP_BitflyerAP']
    BitvenusBP_CoinWAP = results['BitvenusBP_CoinWAP']
    BitvenusBP_ToobitAP = results['BitvenusBP_ToobitAP']
    BitvenusBP_TapBitAP = results['BitvenusBP_TapBitAP']

    BiconomyBP_BinanceAP = results['BiconomyBP_BinanceAP']
    BiconomyBP_BybitAP = results['BiconomyBP_BybitAP']
    BiconomyBP_OKXAP = results['BiconomyBP_OKXAP']
    BiconomyBP_UpbitAP = results['BiconomyBP_UpbitAP']
    BiconomyBP_KucoinAP = results['BiconomyBP_KucoinAP']
    BiconomyBP_BitgetAP = results['BiconomyBP_BitgetAP']
    BiconomyBP_BitstampAP = results['BiconomyBP_BitstampAP']
    BiconomyBP_GeminiAP = results['BiconomyBP_GeminiAP']
    BiconomyBP_KrakenAP = results['BiconomyBP_KrakenAP']
    BiconomyBP_GateioAP = results['BiconomyBP_Gate.ioAP']
    BiconomyBP_HTXAP = results['BiconomyBP_HTXAP']
    BiconomyBP_MEXCAP = results['BiconomyBP_MEXCAP']
    BiconomyBP_LbankAP = results['BiconomyBP_LbankAP']
    BiconomyBP_BitmartAP = results['BiconomyBP_BitmartAP']
    BiconomyBP_DeepcoinAP = results['BiconomyBP_DeepcoinAP']
    BiconomyBP_BitfinexAP = results['BiconomyBP_BitfinexAP']
    BiconomyBP_BingXAP = results['BiconomyBP_BingXAP']
    BiconomyBP_OrangeXAP = results['BiconomyBP_OrangeXAP']
    BiconomyBP_BitvenusAP = results['BiconomyBP_BitvenusAP']
    BiconomyBP_BiconomyAP = results['BiconomyBP_BiconomyAP']
    BiconomyBP_XTAP = results['BiconomyBP_XTAP']
    BiconomyBP_BitflyerAP = results['BiconomyBP_BitflyerAP']
    BiconomyBP_CoinWAP = results['BiconomyBP_CoinWAP']
    BiconomyBP_ToobitAP = results['BiconomyBP_ToobitAP']
    BiconomyBP_TapBitAP = results['BiconomyBP_TapBitAP']

    XTBP_BinanceAP = results['XTBP_BinanceAP']
    XTBP_BybitAP = results['XTBP_BybitAP']
    XTBP_OKXAP = results['XTBP_OKXAP']
    XTBP_UpbitAP = results['XTBP_UpbitAP']
    XTBP_KucoinAP = results['XTBP_KucoinAP']
    XTBP_BitgetAP = results['XTBP_BitgetAP']
    XTBP_BitstampAP = results['XTBP_BitstampAP']
    XTBP_GeminiAP = results['XTBP_GeminiAP']
    XTBP_KrakenAP = results['XTBP_KrakenAP']
    XTBP_GateioAP = results['XTBP_Gate.ioAP']
    XTBP_HTXAP = results['XTBP_HTXAP']
    XTBP_MEXCAP = results['XTBP_MEXCAP']
    XTBP_LbankAP = results['XTBP_LbankAP']
    XTBP_BitmartAP = results['XTBP_BitmartAP']
    XTBP_DeepcoinAP = results['XTBP_DeepcoinAP']
    XTBP_BitfinexAP = results['XTBP_BitfinexAP']
    XTBP_BingXAP = results['XTBP_BingXAP']
    XTBP_OrangeXAP = results['XTBP_OrangeXAP']
    XTBP_BitvenusAP = results['XTBP_BitvenusAP']
    XTBP_BiconomyAP = results['XTBP_BiconomyAP']
    XTBP_XTAP = results['XTBP_XTAP']
    XTBP_BitflyerAP = results['XTBP_BitflyerAP']
    XTBP_CoinWAP = results['XTBP_CoinWAP']
    XTBP_ToobitAP = results['XTBP_ToobitAP']
    XTBP_TapBitAP = results['XTBP_TapBitAP']

    BitflyerBP_BinanceAP = results['BitflyerBP_BinanceAP']
    BitflyerBP_BybitAP = results['BitflyerBP_BybitAP']
    BitflyerBP_OKXAP = results['BitflyerBP_OKXAP']
    BitflyerBP_UpbitAP = results['BitflyerBP_UpbitAP']
    BitflyerBP_KucoinAP = results['BitflyerBP_KucoinAP']
    BitflyerBP_BitgetAP = results['BitflyerBP_BitgetAP']
    BitflyerBP_BitstampAP = results['BitflyerBP_BitstampAP']
    BitflyerBP_GeminiAP = results['BitflyerBP_GeminiAP']
    BitflyerBP_KrakenAP = results['BitflyerBP_KrakenAP']
    BitflyerBP_GateioAP = results['BitflyerBP_Gate.ioAP']
    BitflyerBP_HTXAP = results['BitflyerBP_HTXAP']
    BitflyerBP_MEXCAP = results['BitflyerBP_MEXCAP']
    BitflyerBP_LbankAP = results['BitflyerBP_LbankAP']
    BitflyerBP_BitmartAP = results['BitflyerBP_BitmartAP']
    BitflyerBP_DeepcoinAP = results['BitflyerBP_DeepcoinAP']
    BitflyerBP_BitfinexAP = results['BitflyerBP_BitfinexAP']
    BitflyerBP_BingXAP = results['BitflyerBP_BingXAP']
    BitflyerBP_OrangeXAP = results['BitflyerBP_OrangeXAP']
    BitflyerBP_BitvenusAP = results['BitflyerBP_BitvenusAP']
    BitflyerBP_BiconomyAP = results['BitflyerBP_BiconomyAP']
    BitflyerBP_XTAP = results['BitflyerBP_XTAP']
    BitflyerBP_BitflyerAP = results['BitflyerBP_BitflyerAP']
    BitflyerBP_CoinWAP = results['BitflyerBP_CoinWAP']
    BitflyerBP_ToobitAP = results['BitflyerBP_ToobitAP']
    BitflyerBP_TapBitAP = results['BitflyerBP_TapBitAP']

    CoinWBP_BinanceAP = results['CoinWBP_BinanceAP']
    CoinWBP_BybitAP = results['CoinWBP_BybitAP']
    CoinWBP_OKXAP = results['CoinWBP_OKXAP']
    CoinWBP_UpbitAP = results['CoinWBP_UpbitAP']
    CoinWBP_KucoinAP = results['CoinWBP_KucoinAP']
    CoinWBP_BitgetAP = results['CoinWBP_BitgetAP']
    CoinWBP_BitstampAP = results['CoinWBP_BitstampAP']
    CoinWBP_GeminiAP = results['CoinWBP_GeminiAP']
    CoinWBP_KrakenAP = results['CoinWBP_KrakenAP']
    CoinWBP_GateioAP = results['CoinWBP_Gate.ioAP']
    CoinWBP_HTXAP = results['CoinWBP_HTXAP']
    CoinWBP_MEXCAP = results['CoinWBP_MEXCAP']
    CoinWBP_LbankAP = results['CoinWBP_LbankAP']
    CoinWBP_BitmartAP = results['CoinWBP_BitmartAP']
    CoinWBP_DeepcoinAP = results['CoinWBP_DeepcoinAP']
    CoinWBP_BitfinexAP = results['CoinWBP_BitfinexAP']
    CoinWBP_BingXAP = results['CoinWBP_BingXAP']
    CoinWBP_OrangeXAP = results['CoinWBP_OrangeXAP']
    CoinWBP_BitvenusAP = results['CoinWBP_BitvenusAP']
    CoinWBP_BiconomyAP = results['CoinWBP_BiconomyAP']
    CoinWBP_XTAP = results['CoinWBP_XTAP']
    CoinWBP_BitflyerAP = results['CoinWBP_BitflyerAP']
    CoinWBP_CoinWAP = results['CoinWBP_CoinWAP']
    CoinWBP_ToobitAP = results['CoinWBP_ToobitAP']
    CoinWBP_TapBitAP = results['CoinWBP_TapBitAP']

    ToobitBP_BinanceAP = results['ToobitBP_BinanceAP']
    ToobitBP_BybitAP = results['ToobitBP_BybitAP']
    ToobitBP_OKXAP = results['ToobitBP_OKXAP']
    ToobitBP_UpbitAP = results['ToobitBP_UpbitAP']
    ToobitBP_KucoinAP = results['ToobitBP_KucoinAP']
    ToobitBP_BitgetAP = results['ToobitBP_BitgetAP']
    ToobitBP_BitstampAP = results['ToobitBP_BitstampAP']
    ToobitBP_GeminiAP = results['ToobitBP_GeminiAP']
    ToobitBP_KrakenAP = results['ToobitBP_KrakenAP']
    ToobitBP_GateioAP = results['ToobitBP_Gate.ioAP']
    ToobitBP_HTXAP = results['ToobitBP_HTXAP']
    ToobitBP_MEXCAP = results['ToobitBP_MEXCAP']
    ToobitBP_LbankAP = results['ToobitBP_LbankAP']
    ToobitBP_BitmartAP = results['ToobitBP_BitmartAP']
    ToobitBP_DeepcoinAP = results['ToobitBP_DeepcoinAP']
    ToobitBP_BitfinexAP = results['ToobitBP_BitfinexAP']
    ToobitBP_BingXAP = results['ToobitBP_BingXAP']
    ToobitBP_OrangeXAP = results['ToobitBP_OrangeXAP']
    ToobitBP_BitvenusAP = results['ToobitBP_BitvenusAP']
    ToobitBP_BiconomyAP = results['ToobitBP_BiconomyAP']
    ToobitBP_XTAP = results['ToobitBP_XTAP']
    ToobitBP_BitflyerAP = results['ToobitBP_BitflyerAP']
    ToobitBP_CoinWAP = results['ToobitBP_CoinWAP']
    ToobitBP_ToobitAP = results['ToobitBP_ToobitAP']
    ToobitBP_TapBitAP = results['ToobitBP_TapBitAP']

    TapBitBP_BinanceAP = results['TapBitBP_BinanceAP']
    TapBitBP_BybitAP = results['TapBitBP_BybitAP']
    TapBitBP_OKXAP = results['TapBitBP_OKXAP']
    TapBitBP_UpbitAP = results['TapBitBP_UpbitAP']
    TapBitBP_KucoinAP = results['TapBitBP_KucoinAP']
    TapBitBP_BitgetAP = results['TapBitBP_BitgetAP']
    TapBitBP_BitstampAP = results['TapBitBP_BitstampAP']
    TapBitBP_GeminiAP = results['TapBitBP_GeminiAP']
    TapBitBP_KrakenAP = results['TapBitBP_KrakenAP']
    TapBitBP_GateioAP = results['TapBitBP_Gate.ioAP']
    TapBitBP_HTXAP = results['TapBitBP_HTXAP']
    TapBitBP_MEXCAP = results['TapBitBP_MEXCAP']
    TapBitBP_LbankAP = results['TapBitBP_LbankAP']
    TapBitBP_BitmartAP = results['TapBitBP_BitmartAP']
    TapBitBP_DeepcoinAP = results['TapBitBP_DeepcoinAP']
    TapBitBP_BitfinexAP = results['TapBitBP_BitfinexAP']
    TapBitBP_BingXAP = results['TapBitBP_BingXAP']
    TapBitBP_OrangeXAP = results['TapBitBP_OrangeXAP']
    TapBitBP_BitvenusAP = results['TapBitBP_BitvenusAP']
    TapBitBP_BiconomyAP = results['TapBitBP_BiconomyAP']
    TapBitBP_XTAP = results['TapBitBP_XTAP']
    TapBitBP_BitflyerAP = results['TapBitBP_BitflyerAP']
    TapBitBP_CoinWAP = results['TapBitBP_CoinWAP']
    TapBitBP_ToobitAP = results['TapBitBP_ToobitAP']
    TapBitBP_TapBitAP = results['TapBitBP_TapBitAP']

    end = time.perf_counter_ns()
    processingtime = (end - start)+inital_time


    # "Binance",BinanceLTP,BinanceAP1,BinanceAP1V,BinanceBP1,BinanceBP1V,
    def Buckets(Name, LTP, AP2, AP2V, BP2, BP2V, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11,
                sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19, sub20, sub21, sub22, sub23, sub24, sub25,
                Status):
        tasks = []
        with ThreadPoolExecutor() as executor:
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Binance", BinanceLTP, BinanceAP2,
                                BinanceAP2V, BinanceBP2, BinanceBP2V, processingtime, sub1, Status, Binance_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bybit", BybitLTP, BybitAP2,
                                BybitAP2V, BybitBP2, BybitBP2V, processingtime, sub2, Status, BybitStatus))
            tasks.append(
                executor.submit(checker, OKXOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "OKX", OKXLTP, OKXAP2, OKXAP2V,
                                OKXBP2, OKXBP2V, processingtime, sub2, Binance_Status, OKX_Status))
            tasks.append(
                executor.submit(checker, UpbitOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Upbit", UpbitLTP, UpbitAP2,
                                UpbitAP2V, UpbitBP2, UpbitBP2V, processingtime, sub2, Status, Upbit_Status))
            tasks.append(
                executor.submit(checker, KucoinOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Kucoin", KucoinLTP, KucoinAP2,
                                KucoinAP2V, KucoinBP2, KucoinBP2V, processingtime, sub2, Status, Kucoin_Status))
            tasks.append(
                executor.submit(checker, BitgetOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitget", BitgetLTP, BitgetAP2,
                                BitgetAP2V, BitgetBP2, BitgetBP2V, processingtime, sub2, Status, Bitget_Status))
            tasks.append(executor.submit(checker, BitstampOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitstamp", BitstampLTP,
                                         BitstampAP2, BitstampAP2V, BitstampBP2, BitstampBP2V, processingtime, sub2,
                                         Status, Bitstamp_Status))
            tasks.append(
                executor.submit(checker, KrakenOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Kraken", KrakenLTP, KrakenAP2,
                                KrakenAPV2, KrakenBP2, KrakenBPV2, processingtime, sub2, Status, Kraken_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Gate.io", GateioLTP, GateioAP2,
                                GateioAPV2, GateioBP2, GateioBPV2, processingtime, sub2, Status, Gateio_Status))
            tasks.append(
                executor.submit(checker, HTXOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "HTX", HTXLTP, HTXAP2, HTXAP2V,
                                HTXBP2, HTXBP2V, processingtime, sub2, Status, HTX_Status))
            tasks.append(
                executor.submit(checker, MEXCOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "MEXC", MEXCLTP, MEXCAP2, MEXCAP2V,
                                MEXCBP2, MEXCBP2V, processingtime, sub2, Status, MEXC_Status))
            tasks.append(
                executor.submit(checker, LbankOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Lbank", LbankLTP, LbankAP2,
                                LbankAP2V, LbankBP2, LbankBP2V, processingtime, sub2, Status, Lbank_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitmart", BitmartLTP, BitmartAP2,
                                BitmartAP2V, BitmartBP2, BitmartBP2V, processingtime, sub2, Status, Bitmart_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Deepcoin", DeepcoinLTP,
                                         DeepcoinAP2, DeepcoinAP2V, DeepcoinBP2, DeepcoinBP2V, processingtime, sub2,
                                         Status, Deepcoin_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitfinex", BitfinexLTP,
                                         BitfinexAP2, BitfinexAP2V, BitfinexBP2, BitfinexBP2V, processingtime, sub2,
                                         Status, Bitfinex_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "BingX", BingXLTP, BingXAP2,
                                BingXAP2V, BingXBP2, BingXBP2V, processingtime, sub2, Status, BingX_Status))
            tasks.append(
                executor.submit(checker, OrangeXOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "OrangeX", OrangeXLTP, OrangeXAP2,
                                OrangeXAP2V, OrangeXBP2, OrangeXBP2V, processingtime, sub2, Status, OrangeX_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitvenus", BitvenusLTP,
                                         BitvenusAP2, BitvenusAP2V, BitvenusBP2, BitvenusBP2V, processingtime, sub2,
                                         Status, Bitvenus_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Biconomy", BiconomyLTP,
                                         BiconomyAP2, BiconomyAP2V, BiconomyBP2, BiconomyBP2V, processingtime, sub2,
                                         Status, Biconomy_Status))
            tasks.append(
                executor.submit(checker, GeminiOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Gemini", GeminiLTP, GeminiAP2,
                                GeminiAP2V, GeminiBP2, GeminiBP2V, processingtime, sub2, Status, Gemini_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "XT", XTLTP, XTAP2, XTAP2V, XTBP2,
                                XTBP2V, processingtime, sub2, Binance_Status, XT_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Bitflyer", BitflyerLTP, BitflyerAP2,
                                BitflyerAP2V, BitflyerBP2, BitflyerBP2V, processingtime, sub2, Status,
                                Bitflyer_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "CoinW", CoinWLTP, CoinWAP2, CoinWAP2V,
                                CoinWBP2, CoinWBP2V, processingtime, sub2, Status, CoinW_Status))

            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Toobit", ToobitLTP, ToobitAP2,
                                ToobitAP2V, ToobitBP2, ToobitBP2V, processingtime, sub24, Status, Toobit_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP2, AP2V, BP2, BP2V, "Tapbit", TapbitLTP, TapbitAP2,
                                TapbitAP2V, TapbitBP2, TapbitBP2V, processingtime, sub25, Status, TapBit_Status))

            # Wait for all tasks to complete
            for task in tasks:
                task.result()

    buckets_args = [
        (
            "Binance", BinanceLTP, BinanceAP2, BinanceAP2V, BinanceBP2, BinanceBP2V, BinanceBP_BinanceAP,
            BinanceBP_BybitAP,
            BinanceBP_OKXAP, BinanceBP_UpbitAP, BinanceBP_KucoinAP, BinanceBP_BitgetAP, BinanceBP_BitstampAP,
            BinanceBP_GeminiAP, BinanceBP_KrakenAP, BinanceBP_GateioAP, BinanceBP_HTXAP, BinanceBP_MEXCAP,
            BinanceBP_LbankAP, BinanceBP_BitmartAP, BinanceBP_DeepcoinAP, BinanceBP_BitfinexAP, BinanceBP_BingXAP,
            BinanceBP_OrangeXAP, BinanceBP_BitvenusAP, BinanceBP_BiconomyAP, BinanceBP_XTAP, BinanceBP_BitflyerAP,
            BinanceBP_CoinWAP, BinanceBP_ToobitAP, BinanceBP_TapBitAP, Binance_Status),
        ("Bybit", BybitLTP, BybitAP2, BybitAP2V, BybitBP2, BybitBP2V, BybitBP_BinanceAP, BybitBP_BybitAP, BybitBP_OKXAP,
         BybitBP_UpbitAP, BybitBP_KucoinAP, BybitBP_BitgetAP, BybitBP_BitstampAP, BybitBP_GeminiAP, BybitBP_KrakenAP,
         BybitBP_GateioAP, BybitBP_HTXAP, BybitBP_MEXCAP, BybitBP_LbankAP, BybitBP_BitmartAP, BybitBP_DeepcoinAP,
         BybitBP_BitfinexAP, BybitBP_BingXAP, BybitBP_OrangeXAP, BybitBP_BitvenusAP, BybitBP_BiconomyAP, BybitBP_XTAP,
         BybitBP_BitflyerAP, BybitBP_CoinWAP, BybitBP_ToobitAP, BybitBP_TapBitAP, BybitStatus),
        ("OKX", OKXLTP, OKXAP2, OKXAP2V, OKXBP2, OKXBP2V, OKXBP_BinanceAP, OKXBP_BybitAP, OKXBP_OKXAP, OKXBP_UpbitAP,
         OKXBP_KucoinAP, OKXBP_BitgetAP, OKXBP_BitstampAP, OKXBP_GeminiAP, OKXBP_KrakenAP, OKXBP_GateioAP, OKXBP_HTXAP,
         OKXBP_MEXCAP, OKXBP_LbankAP, OKXBP_BitmartAP, OKXBP_DeepcoinAP, OKXBP_BitfinexAP, OKXBP_BingXAP,
         OKXBP_OrangeXAP, OKXBP_BitvenusAP, OKXBP_BiconomyAP, OKXBP_XTAP, OKXBP_BitflyerAP, OKXBP_CoinWAP,
         OKXBP_ToobitAP, OKXBP_TapBitAP, OKX_Status),
        ("Upbit", UpbitLTP, UpbitAP2, UpbitAP2V, UpbitBP2, UpbitBP2V, UpbitBP_BinanceAP, UpbitBP_BybitAP, UpbitBP_OKXAP,
         UpbitBP_UpbitAP, UpbitBP_KucoinAP, UpbitBP_BitgetAP, UpbitBP_BitstampAP, UpbitBP_GeminiAP, UpbitBP_KrakenAP,
         UpbitBP_GateioAP, UpbitBP_HTXAP, UpbitBP_MEXCAP, UpbitBP_LbankAP, UpbitBP_BitmartAP, UpbitBP_DeepcoinAP,
         UpbitBP_BitfinexAP, UpbitBP_BingXAP, UpbitBP_OrangeXAP, UpbitBP_BitvenusAP, UpbitBP_BiconomyAP, UpbitBP_XTAP,
         UpbitBP_BitflyerAP, UpbitBP_CoinWAP, UpbitBP_ToobitAP, UpbitBP_TapBitAP, Upbit_Status),
        ("Kucoin", KucoinLTP, KucoinAP2, KucoinAP2V, KucoinBP2, KucoinBP2V, KucoinBP_BinanceAP, KucoinBP_BybitAP,
         KucoinBP_OKXAP, KucoinBP_UpbitAP, KucoinBP_KucoinAP, KucoinBP_BitgetAP, KucoinBP_BitstampAP, KucoinBP_GeminiAP,
         KucoinBP_KrakenAP, KucoinBP_GateioAP, KucoinBP_HTXAP, KucoinBP_MEXCAP, KucoinBP_LbankAP, KucoinBP_BitmartAP,
         KucoinBP_DeepcoinAP, KucoinBP_BitfinexAP, KucoinBP_BingXAP, KucoinBP_OrangeXAP, KucoinBP_BitvenusAP,
         KucoinBP_BiconomyAP, KucoinBP_XTAP, KucoinBP_BitflyerAP, KucoinBP_CoinWAP, KucoinBP_ToobitAP,
         KucoinBP_TapBitAP, Kucoin_Status),
        ("Bitget", BitgetLTP, BitgetAP2, BitgetAP2V, BitgetBP2, BitgetBP2V, BitgetBP_BinanceAP, BitgetBP_BybitAP,
         BitgetBP_OKXAP, BitgetBP_UpbitAP, BitgetBP_KucoinAP, BitgetBP_BitgetAP, BitgetBP_BitstampAP, BitgetBP_GeminiAP,
         BitgetBP_KrakenAP, BitgetBP_GateioAP, BitgetBP_HTXAP, BitgetBP_MEXCAP, BitgetBP_LbankAP, BitgetBP_BitmartAP,
         BitgetBP_DeepcoinAP, BitgetBP_BitfinexAP, BitgetBP_BingXAP, BitgetBP_OrangeXAP, BitgetBP_BitvenusAP,
         BitgetBP_BiconomyAP, BitgetBP_XTAP, BitgetBP_BitflyerAP, BitgetBP_CoinWAP, BitgetBP_ToobitAP,
         BitgetBP_TapBitAP, Bitget_Status),
        ("Bitstamp", BitstampLTP, BitstampAP2, BitstampAP2V, BitstampBP2, BitstampBP2V, BitstampBP_BinanceAP,
         BitstampBP_BybitAP, BitstampBP_OKXAP, BitstampBP_UpbitAP, BitstampBP_KucoinAP, BitstampBP_BitgetAP,
         BitstampBP_BitstampAP, BitstampBP_GeminiAP, BitstampBP_KrakenAP, BitstampBP_GateioAP, BitstampBP_HTXAP,
         BitstampBP_MEXCAP, BitstampBP_LbankAP, BitstampBP_BitmartAP, BitstampBP_DeepcoinAP, BitstampBP_BitfinexAP,
         BitstampBP_BingXAP, BitstampBP_OrangeXAP, BitstampBP_BitvenusAP, BitstampBP_BiconomyAP, BitstampBP_XTAP,
         BitstampBP_BitflyerAP, BitstampBP_CoinWAP, BitstampBP_ToobitAP, BitstampBP_TapBitAP, Bitstamp_Status),
        ("Kraken", KrakenLTP, KrakenAP2, KrakenAPV2, KrakenBP2, KrakenBPV2, KrakenBP_BinanceAP, KrakenBP_BybitAP,
         KrakenBP_OKXAP, KrakenBP_UpbitAP, KrakenBP_KucoinAP, KrakenBP_BitgetAP, KrakenBP_BitstampAP, KrakenBP_GeminiAP,
         KrakenBP_KrakenAP, KrakenBP_GateioAP, KrakenBP_HTXAP, KrakenBP_MEXCAP, KrakenBP_LbankAP, KrakenBP_BitmartAP,
         KrakenBP_DeepcoinAP, KrakenBP_BitfinexAP, KrakenBP_BingXAP, KrakenBP_OrangeXAP, KrakenBP_BitvenusAP,
         KrakenBP_BiconomyAP, KrakenBP_XTAP, KrakenBP_BitflyerAP, KrakenBP_CoinWAP, KrakenBP_ToobitAP,
         KrakenBP_TapBitAP, Kraken_Status),
        ("Gate.io", GateioLTP, GateioAP2, GateioAPV2, GateioBP2, GateioBPV2, GateioBP_BinanceAP, GateioBP_BybitAP,
         GateioBP_OKXAP, GateioBP_UpbitAP, GateioBP_KucoinAP, GateioBP_BitgetAP, GateioBP_BitstampAP, GateioBP_GeminiAP,
         GateioBP_KrakenAP, GateioBP_GateioAP, GateioBP_HTXAP, GateioBP_MEXCAP, GateioBP_LbankAP, GateioBP_BitmartAP,
         GateioBP_DeepcoinAP, GateioBP_BitfinexAP, GateioBP_BingXAP, GateioBP_OrangeXAP, GateioBP_BitvenusAP,
         GateioBP_BiconomyAP, GateioBP_XTAP, GateioBP_BitflyerAP, GateioBP_CoinWAP, GateioBP_ToobitAP,
         GateioBP_TapBitAP, Gateio_Status),
        ("HTX", HTXLTP, HTXAP2,
         HTXAP2V,
         HTXBP2, HTXBP2V,
         HTXBP_BinanceAP, HTXBP_BybitAP, HTXBP_OKXAP, HTXBP_UpbitAP, HTXBP_KucoinAP,
         HTXBP_BitgetAP, HTXBP_BitstampAP
         , HTXBP_GeminiAP, HTXBP_KrakenAP, HTXBP_GateioAP, HTXBP_HTXAP, HTXBP_MEXCAP,
         HTXBP_LbankAP, HTXBP_BitmartAP
         , HTXBP_DeepcoinAP, HTXBP_BitfinexAP, HTXBP_BingXAP, HTXBP_OrangeXAP, HTXBP_BitvenusAP,
         HTXBP_BiconomyAP,
         HTXBP_XTAP, HTXBP_BitflyerAP, HTXBP_CoinWAP, HTXBP_ToobitAP, HTXBP_TapBitAP, HTX_Status
         ),
        ("MEXC", MEXCLTP,
         MEXCAP2, MEXCAP2V,
         MEXCBP2, MEXCBP2V,
         MEXCBP_BinanceAP, MEXCBP_BybitAP, MEXCBP_OKXAP, MEXCBP_UpbitAP, MEXCBP_KucoinAP,
         MEXCBP_BitgetAP, MEXCBP_BitstampAP
         , MEXCBP_GeminiAP, MEXCBP_KrakenAP, MEXCBP_GateioAP, MEXCBP_HTXAP, MEXCBP_MEXCAP,
         MEXCBP_LbankAP, MEXCBP_BitmartAP
         , MEXCBP_DeepcoinAP, MEXCBP_BitfinexAP, MEXCBP_BingXAP, MEXCBP_OrangeXAP, MEXCBP_BitvenusAP,
         MEXCBP_BiconomyAP,
         MEXCBP_XTAP, MEXCBP_BitflyerAP, MEXCBP_CoinWAP, MEXCBP_ToobitAP, MEXCBP_TapBitAP, MEXC_Status
         ),
        ("Lbank", LbankLTP,
         LbankAP2, LbankAP2V,
         LbankBP2, LbankBP2V,
         LbankBP_BinanceAP, LbankBP_BybitAP, LbankBP_OKXAP, LbankBP_UpbitAP, LbankBP_KucoinAP,
         LbankBP_BitgetAP, LbankBP_BitstampAP
         , LbankBP_GeminiAP, LbankBP_KrakenAP, LbankBP_GateioAP, LbankBP_HTXAP, LbankBP_MEXCAP,
         LbankBP_LbankAP, LbankBP_BitmartAP
         , LbankBP_DeepcoinAP, LbankBP_BitfinexAP, LbankBP_BingXAP, LbankBP_OrangeXAP, LbankBP_BitvenusAP,
         LbankBP_BiconomyAP,
         LbankBP_XTAP, LbankBP_BitflyerAP, LbankBP_CoinWAP, LbankBP_ToobitAP, LbankBP_TapBitAP, Lbank_Status
         ),
        ("Bitmart",
         BitmartLTP, BitmartAP2, BitmartAP2V,
         BitmartBP2, BitmartBP2V,
         BitmartBP_BinanceAP, BitmartBP_BybitAP, BitmartBP_OKXAP, BitmartBP_UpbitAP, BitmartBP_KucoinAP,
         BitmartBP_BitgetAP, BitmartBP_BitstampAP
         , BitmartBP_GeminiAP, BitmartBP_KrakenAP, BitmartBP_GateioAP, BitmartBP_HTXAP, BitmartBP_MEXCAP,
         BitmartBP_LbankAP, BitmartBP_BitmartAP
         , BitmartBP_DeepcoinAP, BitmartBP_BitfinexAP, BitmartBP_BingXAP, BitmartBP_OrangeXAP, BitmartBP_BitvenusAP,
         BitmartBP_BiconomyAP,
         BitmartBP_XTAP, BitmartBP_BitflyerAP, BitmartBP_CoinWAP, BitmartBP_ToobitAP, BitmartBP_TapBitAP, Bitmart_Status
         ),
        ("Deepcoin",
         DeepcoinLTP,
         DeepcoinAP2, DeepcoinAP2V, DeepcoinBP2, DeepcoinBP2V,
         DeepcoinBP_BinanceAP, DeepcoinBP_BybitAP, DeepcoinBP_OKXAP, DeepcoinBP_UpbitAP, DeepcoinBP_KucoinAP,
         DeepcoinBP_BitgetAP, DeepcoinBP_BitstampAP
         , DeepcoinBP_GeminiAP, DeepcoinBP_KrakenAP, DeepcoinBP_GateioAP, DeepcoinBP_HTXAP, DeepcoinBP_MEXCAP,
         DeepcoinBP_LbankAP, DeepcoinBP_BitmartAP
         , DeepcoinBP_DeepcoinAP, DeepcoinBP_BitfinexAP, DeepcoinBP_BingXAP, DeepcoinBP_OrangeXAP,
         DeepcoinBP_BitvenusAP,
         DeepcoinBP_BiconomyAP,
         DeepcoinBP_XTAP, DeepcoinBP_BitflyerAP, DeepcoinBP_CoinWAP, DeepcoinBP_ToobitAP, DeepcoinBP_TapBitAP,
         Deepcoin_Status
         ),
        ("Bitfinex",
         BitfinexLTP, BitfinexAP2, BitfinexAP2V,
         BitfinexBP2, BitfinexBP2V,
         BitfinexBP_BinanceAP, BitfinexBP_BybitAP, BitfinexBP_OKXAP, BitfinexBP_UpbitAP, BitfinexBP_KucoinAP,
         BitfinexBP_BitgetAP, BitfinexBP_BitstampAP
         , BitfinexBP_GeminiAP, BitfinexBP_KrakenAP, BitfinexBP_GateioAP, BitfinexBP_HTXAP, BitfinexBP_MEXCAP,
         BitfinexBP_LbankAP, BitfinexBP_BitmartAP
         , BitfinexBP_DeepcoinAP, BitfinexBP_BitfinexAP, BitfinexBP_BingXAP, BitfinexBP_OrangeXAP,
         BitfinexBP_BitvenusAP,
         BitfinexBP_BiconomyAP,
         BitfinexBP_XTAP, BitfinexBP_BitflyerAP, BitfinexBP_CoinWAP, BitfinexBP_ToobitAP, BitfinexBP_TapBitAP,
         Bitfinex_Status
         ),
        ("BingX", BingXLTP,
         BingXAP2, BingXAP2V,
         BingXBP2, BingXBP2V,
         BingXBP_BinanceAP, BingXBP_BybitAP, BingXBP_OKXAP, BingXBP_UpbitAP, BingXBP_KucoinAP,
         BingXBP_BitgetAP, BingXBP_BitstampAP
         , BingXBP_GeminiAP, BingXBP_KrakenAP, BingXBP_GateioAP, BingXBP_HTXAP, BingXBP_MEXCAP,
         BingXBP_LbankAP, BingXBP_BitmartAP
         , BingXBP_DeepcoinAP, BingXBP_BitfinexAP, BingXBP_BingXAP, BingXBP_OrangeXAP, BingXBP_BitvenusAP,
         BingXBP_BiconomyAP,
         BingXBP_XTAP, BingXBP_BitflyerAP, BingXBP_CoinWAP, BingXBP_ToobitAP, BingXBP_TapBitAP, BingX_Status
         ),
        ("OrangeX",
         OrangeXLTP, OrangeXAP2, OrangeXAP2V,
         OrangeXBP2, OrangeXBP2V,
         OrangeXBP_BinanceAP, OrangeXBP_BybitAP, OrangeXBP_OKXAP, OrangeXBP_UpbitAP, OrangeXBP_KucoinAP,
         OrangeXBP_BitgetAP, OrangeXBP_BitstampAP
         , OrangeXBP_GeminiAP, OrangeXBP_KrakenAP, OrangeXBP_GateioAP, OrangeXBP_HTXAP, OrangeXBP_MEXCAP,
         OrangeXBP_LbankAP, OrangeXBP_BitmartAP
         , OrangeXBP_DeepcoinAP, OrangeXBP_BitfinexAP, OrangeXBP_BingXAP, OrangeXBP_OrangeXAP, OrangeXBP_BitvenusAP,
         OrangeXBP_BiconomyAP,
         OrangeXBP_XTAP, OrangeXBP_BitflyerAP, OrangeXBP_CoinWAP, OrangeXBP_ToobitAP, OrangeXBP_TapBitAP, OrangeX_Status
         ),
        ("Bitvenus",
         BitvenusLTP, BitvenusAP2, BitvenusAP2V,
         BitvenusBP2, BitvenusBP2V,
         BitvenusBP_BinanceAP, BitvenusBP_BybitAP, BitvenusBP_OKXAP, BitvenusBP_UpbitAP, BitvenusBP_KucoinAP,
         BitvenusBP_BitgetAP, BitvenusBP_BitstampAP
         , BitvenusBP_GeminiAP, BitvenusBP_KrakenAP, BitvenusBP_GateioAP, BitvenusBP_HTXAP, BitvenusBP_MEXCAP,
         BitvenusBP_LbankAP, BitvenusBP_BitmartAP
         , BitvenusBP_DeepcoinAP, BitvenusBP_BitfinexAP, BitvenusBP_BingXAP, BitvenusBP_OrangeXAP,
         BitvenusBP_BitvenusAP,
         BitvenusBP_BiconomyAP,
         BitvenusBP_XTAP, BitvenusBP_BitflyerAP, BitvenusBP_CoinWAP, BitvenusBP_ToobitAP, BitvenusBP_TapBitAP,
         Bitvenus_Status
         ),
        ("Biconomy",
         BiconomyLTP, BiconomyAP2, BiconomyAP2V,
         BiconomyBP2, BiconomyBP2V,
         BiconomyBP_BinanceAP, BiconomyBP_BybitAP, BiconomyBP_OKXAP, BiconomyBP_UpbitAP, BiconomyBP_KucoinAP,
         BiconomyBP_BitgetAP, BiconomyBP_BitstampAP
         , BiconomyBP_GeminiAP, BiconomyBP_KrakenAP, BiconomyBP_GateioAP, BiconomyBP_HTXAP, BiconomyBP_MEXCAP,
         BiconomyBP_LbankAP, BiconomyBP_BitmartAP
         , BiconomyBP_DeepcoinAP, BiconomyBP_BitfinexAP, BiconomyBP_BingXAP, BiconomyBP_OrangeXAP,
         BiconomyBP_BitvenusAP,
         BiconomyBP_BiconomyAP,
         BiconomyBP_XTAP, BiconomyBP_BitflyerAP, BiconomyBP_CoinWAP, BiconomyBP_ToobitAP, BiconomyBP_TapBitAP,
         Biconomy_Status
         ),
        ("Gemini", GeminiLTP,
         GeminiAP2, GeminiAP2V,
         GeminiBP2, GeminiBP2V,
         GeminiBP_BinanceAP, GeminiBP_BybitAP, GeminiBP_OKXAP, GeminiBP_UpbitAP, GeminiBP_KucoinAP,
         GeminiBP_BitgetAP, GeminiBP_BitstampAP
         , GeminiBP_GeminiAP, GeminiBP_KrakenAP, GeminiBP_GateioAP, GeminiBP_HTXAP, GeminiBP_MEXCAP,
         GeminiBP_LbankAP, GeminiBP_BitmartAP
         , GeminiBP_DeepcoinAP, GeminiBP_BitfinexAP, GeminiBP_BingXAP, GeminiBP_OrangeXAP, GeminiBP_BitvenusAP,
         GeminiBP_BiconomyAP,
         GeminiBP_XTAP, GeminiBP_BitflyerAP, GeminiBP_CoinWAP, GeminiBP_ToobitAP, GeminiBP_TapBitAP, Gemini_Status
         ),
        ("XT", XTLTP, XTAP2,
         XTAP2V,
         XTBP2, XTBP2V,
         XTBP_BinanceAP, XTBP_BybitAP, XTBP_OKXAP, XTBP_UpbitAP, XTBP_KucoinAP,
         XTBP_BitgetAP, XTBP_BitstampAP
         , XTBP_GeminiAP, XTBP_KrakenAP, XTBP_GateioAP, XTBP_HTXAP, XTBP_MEXCAP,
         XTBP_LbankAP, XTBP_BitmartAP
         , XTBP_DeepcoinAP, XTBP_BitfinexAP, XTBP_BingXAP, XTBP_OrangeXAP, XTBP_BitvenusAP,
         XTBP_BiconomyAP,
         XTBP_XTAP, XTBP_BitflyerAP, XTBP_CoinWAP, XTBP_ToobitAP, XTBP_TapBitAP, XT_Status
         ),
        ("Bitflyer", BitflyerLTP,
         BitflyerAP2, BitflyerAP2V,
         BitflyerBP2, BitflyerBP2V,
         BitflyerBP_BinanceAP, BitflyerBP_BybitAP, BitflyerBP_OKXAP, BitflyerBP_UpbitAP, BitflyerBP_KucoinAP,
         BitflyerBP_BitgetAP, BitflyerBP_BitstampAP
         , BitflyerBP_GeminiAP, BitflyerBP_KrakenAP, BitflyerBP_GateioAP, BitflyerBP_HTXAP, BitflyerBP_MEXCAP,
         BitflyerBP_LbankAP, BitflyerBP_BitmartAP
         , BitflyerBP_DeepcoinAP, BitflyerBP_BitfinexAP, BitflyerBP_BingXAP, BitflyerBP_OrangeXAP,
         BitflyerBP_BitvenusAP,
         BitflyerBP_BiconomyAP,
         BitflyerBP_XTAP, BitflyerBP_BitflyerAP, BitflyerBP_CoinWAP, BitflyerBP_ToobitAP, BitflyerBP_TapBitAP,
         Bitflyer_Status
         ),
        ("CoinW", CoinWLTP,
         CoinWAP2, CoinWAP2V,
         CoinWBP2, CoinWBP2V,
         CoinWBP_BinanceAP, CoinWBP_BybitAP, CoinWBP_OKXAP, CoinWBP_UpbitAP, CoinWBP_KucoinAP,
         CoinWBP_BitgetAP, CoinWBP_BitstampAP
         , CoinWBP_GeminiAP, CoinWBP_KrakenAP, CoinWBP_GateioAP, CoinWBP_HTXAP, CoinWBP_MEXCAP,
         CoinWBP_LbankAP, CoinWBP_BitmartAP
         , CoinWBP_DeepcoinAP, CoinWBP_BitfinexAP, CoinWBP_BingXAP, CoinWBP_OrangeXAP, CoinWBP_BitvenusAP,
         CoinWBP_BiconomyAP,
         CoinWBP_XTAP, CoinWBP_BitflyerAP, CoinWBP_CoinWAP, CoinWBP_ToobitAP, CoinWBP_TapBitAP, CoinW_Status
         ),
        ("Toobit", ToobitLTP,
         ToobitAP2, ToobitAP2V,
         ToobitBP2, ToobitBP2V,
         ToobitBP_BinanceAP, ToobitBP_BybitAP, ToobitBP_OKXAP, ToobitBP_UpbitAP, ToobitBP_KucoinAP,
         ToobitBP_BitgetAP, ToobitBP_BitstampAP
         , ToobitBP_GeminiAP, ToobitBP_KrakenAP, ToobitBP_GateioAP, ToobitBP_HTXAP, ToobitBP_MEXCAP,
         ToobitBP_LbankAP, ToobitBP_BitmartAP
         , ToobitBP_DeepcoinAP, ToobitBP_BitfinexAP, ToobitBP_BingXAP, ToobitBP_OrangeXAP, ToobitBP_BitvenusAP,
         ToobitBP_BiconomyAP,
         ToobitBP_XTAP, ToobitBP_BitflyerAP, ToobitBP_CoinWAP, ToobitBP_ToobitAP, ToobitBP_TapBitAP, Toobit_Status
         ),
        ("Tapbit", TapbitLTP,
         TapbitAP2, TapbitAP2V,
         TapbitBP2, TapbitBP2V,
         TapBitBP_BinanceAP, TapBitBP_BybitAP, TapBitBP_OKXAP, TapBitBP_UpbitAP, TapBitBP_KucoinAP,
         TapBitBP_BitgetAP, TapBitBP_BitstampAP
         , TapBitBP_GeminiAP, TapBitBP_KrakenAP, TapBitBP_GateioAP, TapBitBP_HTXAP, TapBitBP_MEXCAP,
         TapBitBP_LbankAP, TapBitBP_BitmartAP
         , TapBitBP_DeepcoinAP, TapBitBP_BitfinexAP, TapBitBP_BingXAP, TapBitBP_OrangeXAP, TapBitBP_BitvenusAP,
         TapBitBP_BiconomyAP,
         TapBitBP_XTAP, TapBitBP_BitflyerAP, TapBitBP_CoinWAP, TapBitBP_ToobitAP, TapBitBP_TapBitAP, TapBit_Status
         )

        # Add other exchanges similarly
    ]

    # Create a list to hold the threads
    threads = []

    # Create and start a thread for each PriceDifference function call
    for args in buckets_args:
        thread = threading.Thread(target=Buckets, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



async def Bid_Ask3(results,inital_time):
    start = time.perf_counter_ns()



    # Binance
    BinanceBP3 = results["BinanceBP3"]
    BinanceBP3V = results["BinanceBP3V"]
    BinanceAP3 = results["BinanceAP3"]
    BinanceAP3V = results["BinanceAP3V"]
    BinanceOBT = results["BinanceOBT"]
    BinanceLTP = results["BinanceLTP"]

    # Bybit
    BybitBP3 = results["BybitBP3"]
    BybitBP3V = results["BybitBP3V"]
    BybitAP3 = results["BybitAP3"]
    BybitAP3V = results["BybitAP3V"]
    BybitOBT = results["BybitOBT"]
    BybitLTP = results["BybitLTP"]

    # OKX
    OKXBP3 = results["OKXBP3"]
    OKXBP3V = results["OKXBP3V"]
    OKXAP3 = results["OKXAP3"]
    OKXAP3V = results["OKXAP3V"]
    OKXOBT = results["OKXOBT"]
    OKXLTP = results["OKXLTP"]

    # Upbit
    UpbitBP3 = results["UpbitBP3"]
    UpbitBP3V = results["UpbitBP3V"]
    UpbitAP3 = results["UpbitAP3"]
    UpbitAP3V = results["UpbitAP3V"]
    UpbitOBT = results["UpbitOBT"]
    UpbitLTP = results["UpbitLTP"]

    # Kucoin
    KucoinBP3 = results["KucoinBP3"]
    KucoinBP3V = results["KucoinBP3V"]
    KucoinAP3 = results["KucoinAP3"]
    KucoinAP3V = results["KucoinAP3V"]
    KucoinOBT = results["KucoinOBT"]
    KucoinLTP = results["KucoinLTP"]

    # Bitget
    BitgetBP3 = results["BitgetBP3"]
    BitgetBP3V = results["BitgetBP3V"]
    BitgetAP3 = results["BitgetAP3"]
    BitgetAP3V = results["BitgetAP3V"]
    BitgetOBT = results["BitgetOBT"]
    BitgetLTP = results["BitgetLTP"]

    # Bitstamp
    BitstampBP3 = results["BitstampBP3"]
    BitstampBP3V = results["BitstampBP3V"]
    BitstampAP3 = results["BitstampAP3"]
    BitstampAP3V = results["BitstampAP3V"]
    BitstampOBT = results["BitstampOBT"]
    BitstampLTP = results["BitstampLTP"]

    # Gemini
    GeminiBP3 = results["GeminiBP3"]
    GeminiBP3V = results["GeminiBP3V"]
    GeminiAP3 = results["GeminiAP3"]
    GeminiAP3V = results["GeminiAP3V"]
    GeminiOBT = results["GeminiOBT"]
    GeminiLTP = results["GeminiLTP"]

    # Kraken
    KrakenBP3 = results["KrakenBP3"]
    KrakenBP3V = results["KrakenBP3V"]
    KrakenAP3 = results["KrakenAP3"]
    KrakenAP3V = results["KrakenAP3V"]
    KrakenOBT = results["KrakenOBT"]
    KrakenLTP = results["KrakenLTP"]

    # Gateio
    GateioBP3 = results["GateioBP3"]
    GateioBP3V = results["GateioBP3V"]
    GateioAP3 = results["GateioAP3"]
    GateioAP3V = results["GateioAP3V"]
    GateioOBT = results["GateioOBT"]
    GateioLTP = results["GateioLTP"]

    # HTX
    HTXBP3 = results["HTXBP3"]
    HTXBP3V = results["HTXBP3V"]
    HTXAP3 = results["HTXAP3"]
    HTXAP3V = results["HTXAP3V"]
    HTXOBT = results["HTXOBT"]
    HTXLTP = results["HTXLTP"]

    # MEXC
    MEXCBP3 = results["MEXCBP3"]
    MEXCBP3V = results["MEXCBP3V"]
    MEXCAP3 = results["MEXCAP3"]
    MEXCAP3V = results["MEXCAP3V"]
    MEXCOBT = results["MEXCOBT"]
    MEXCLTP = results["MEXCLTP"]

    # Lbank
    LbankBP3 = results["LbankBP3"]
    LbankBP3V = results["LbankBP3V"]
    LbankAP3 = results["LbankAP3"]
    LbankAP3V = results["LbankAP3V"]
    LbankOBT = results["LbankOBT"]
    LbankLTP = results["LbankLTP"]

    # Bitmart
    BitmartBP3 = results["BitmartBP3"]
    BitmartBP3V = results["BitmartBP3V"]
    BitmartAP3 = results["BitmartAP3"]
    BitmartAP3V = results["BitmartAP3V"]
    BitmartOBT = results["BitmartOBT"]
    BitmartLTP = results["BitmartLTP"]

    # Deepcoin
    DeepcoinBP3 = results["DeepcoinBP3"]
    DeepcoinBP3V = results["DeepcoinBP3V"]
    DeepcoinAP3 = results["DeepcoinAP3"]
    DeepcoinAP3V = results["DeepcoinAP3V"]
    DeepcoinOBT = results["DeepcoinOBT"]
    DeepcoinLTP = results["DeepcoinLTP"]

    # Bitfinex
    BitfinexBP3 = results["BitfinexBP3"]
    BitfinexBP3V = results["BitfinexBP3V"]
    BitfinexAP3 = results["BitfinexAP3"]
    BitfinexAP3V = results["BitfinexAP3V"]
    BitfinexOBT = results["BitfinexOBT"]
    BitfinexLTP = results["BitfinexLTP"]

    # BingX
    BingXBP3 = results["BingXBP3"]
    BingXBP3V = results["BingXBP3V"]
    BingXAP3 = results["BingXAP3"]
    BingXAP3V = results["BingXAP3V"]
    BingXOBT = results["BingXOBT"]
    BingXLTP = results["BingXLTP"]

    # OrangeX
    OrangeXBP3 = results["OrangeXBP3"]
    OrangeXBP3V = results["OrangeXBP3V"]
    OrangeXAP3 = results["OrangeXAP3"]
    OrangeXAP3V = results["OrangeXAP3V"]
    OrangeXOBT = results["OrangeXOBT"]
    OrangeXLTP = results["OrangeXLTP"]

    # Bitvenus
    BitvenusBP3 = results["BitvenusBP3"]
    BitvenusBP3V = results["BitvenusBP3V"]
    BitvenusAP3 = results["BitvenusAP3"]
    BitvenusAP3V = results["BitvenusAP3V"]
    BitvenusOBT = results["BitvenusOBT"]
    BitvenusLTP = results["BitvenusLTP"]

    # Biconomy
    BiconomyBP3 = results["BiconomyBP3"]
    BiconomyBP3V = results["BiconomyBP3V"]
    BiconomyAP3 = results["BiconomyAP3"]
    BiconomyAP3V = results["BiconomyAP3V"]
    BiconomyOBT = results["BiconomyOBT"]
    BiconomyLTP = results["BiconomyLTP"]

    # XT
    XTBP3 = results["XTBP3"]
    XTBP3V = results["XTBP3V"]
    XTAP3 = results["XTAP3"]
    XTAP3V = results["XTAP3V"]
    XTOBT = results["XTOBT"]
    XTLTP = results["XTLTP"]

    # Bitflyer
    BitflyerBP3 = results["BitflyerBP3"]
    BitflyerBP3V = results["BitflyerBP3V"]
    BitflyerAP3 = results["BitflyerAP3"]
    BitflyerAP3V = results["BitflyerAP3V"]
    BitflyerOBT = results["BitflyerOBT"]
    BitflyerLTP = results["BitflyerLTP"]

    # CoinW
    CoinWBP3 = results["CoinWBP3"]
    CoinWBP3V = results["CoinWBP3V"]
    CoinWAP3 = results["CoinWAP3"]
    CoinWAP3V = results["CoinWAP3V"]
    CoinWOBT = results["CoinWOBT"]
    CoinWLTP = results["CoinWLTP"]

    # Toobit
    ToobitBP3 = results["ToobitBP3"]
    ToobitBP3V = results["ToobitBP3V"]
    ToobitAP3 = results["ToobitAP3"]
    ToobitAP3V = results["ToobitAP3V"]
    ToobitOBT = results["ToobitOBT"]
    ToobitLTP = results["ToobitLTP"]

    # TapBit
    TapbitBP3 = results["TapBitBP3"]
    TapbitBP3V = results["TapBitBP3V"]
    TapbitAP3 = results["TapBitAP3"]
    TapbitAP3V = results["TapBitAP3V"]
    TapbitOBT = results["TapBitOBT"]
    TapbitLTP = results["TapBitLTP"]

    Binance_Status = results['Binance_Status']
    BybitStatus = results['Bybit_Status']
    OKX_Status = results['OKX_Status']
    Upbit_Status = results['Upbit_Status']
    Kucoin_Status = results['Kucoin_Status']
    Bitget_Status = results['Bitget_Status']
    Bitstamp_Status = results['Bitstamp_Status']
    Gemini_Status = results['Gemini_Status']
    Kraken_Status = results['Kraken_Status']
    Gateio_Status = results['Gateio_Status']
    HTX_Status = results['HTX_Status']
    MEXC_Status = results['MEXC_Status']
    Lbank_Status = results['Lbank_Status']
    Bitmart_Status = results['Bitmart_Status']
    Deepcoin_Status = results['Deepcoin_Status']
    Bitfinex_Status = results['Bitfinex_Status']
    BingX_Status = results['BingX_Status']
    OrangeX_Status = results['OrangeX_Status']
    Bitvenus_Status = results['Bitvenus_Status']
    Biconomy_Status = results['Biconomy_Status']
    XT_Status = results['XT_Status']
    Bitflyer_Status = results['Bitflyer_Status']
    CoinW_Status = results['CoinW_Status']
    Toobit_Status = results['Toobit_Status']
    TapBit_Status = results['TapBit_Status']

    bid_prices = {
        "Binance": BinanceBP3,
        "Bybit": BybitBP3,
        "OKX": OKXBP3,
        "Upbit": UpbitBP3,
        "Kucoin": KucoinBP3,
        "Bitget": BitgetBP3,
        "Bitstamp": BitstampBP3,
        "Gemini": GeminiBP3,
        "Kraken": KrakenBP3,
        "Gate.io": GateioBP3,
        "HTX": HTXBP3,
        "MEXC": MEXCBP3,
        "Lbank": LbankBP3,
        "Bitmart": BitmartBP3,
        "Deepcoin": DeepcoinBP3,
        "Bitfinex": BitfinexBP3,
        "BingX": BingXBP3,
        "OrangeX": OrangeXBP3,
        "Bitvenus": BitvenusBP3,
        "Biconomy": BiconomyBP3,
        "XT": XTBP3,
        "Bitflyer": BitflyerBP3,
        "CoinW": CoinWBP3,
        "Toobit": ToobitBP3,
        "TapBit": TapbitBP3
    }

    ask_prices = {
        "Binance": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bybit": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "OKX": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Upbit": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Kucoin": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitget": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitstamp": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Gemini": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Kraken": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Gate.io": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "HTX": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "MEXC": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Lbank": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitmart": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Deepcoin": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitfinex": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "BingX": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "OrangeX": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitvenus": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Biconomy": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "XT": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Bitflyer": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "CoinW": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "Toobit": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        },
        "TapBit": {
            "Binance": BinanceAP3,
            "Bybit": BybitAP3,
            "OKX": OKXAP3,
            "Upbit": UpbitAP3,
            "Kucoin": KucoinAP3,
            "Bitget": BitgetAP3,
            "Bitstamp": BitstampAP3,
            "Gemini": GeminiAP3,
            "Kraken": KrakenAP3,
            "Gate.io": GateioAP3,
            "HTX": HTXAP3,
            "MEXC": MEXCAP3,
            "Lbank": LbankAP3,
            "Bitmart": BitmartAP3,
            "Deepcoin": DeepcoinAP3,
            "Bitfinex": BitfinexAP3,
            "BingX": BingXAP3,
            "OrangeX": OrangeXAP3,
            "Bitvenus": BitvenusAP3,
            "Biconomy": BiconomyAP3,
            "XT": XTAP3,
            "Bitflyer": BitflyerAP3,
            "CoinW": CoinWAP3,
            "Toobit": ToobitAP3,
            "TapBit": TapbitAP3
        }
    }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect differences from all exchanges
    all_differences = {}
    for exchange in exchanges:
        all_differences.update(exchange.get_differences())

    results = {}
    for key, value in all_differences.items():
        results[key] = value

    # Print stored variables
    for key in sorted(results.keys()):
        results[key]

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_Gate.ioAP']
    BinanceBP_HTXAP = results['BinanceBP_HTXAP']
    BinanceBP_MEXCAP = results['BinanceBP_MEXCAP']
    BinanceBP_LbankAP = results['BinanceBP_LbankAP']
    BinanceBP_BitmartAP = results['BinanceBP_BitmartAP']
    BinanceBP_DeepcoinAP = results['BinanceBP_DeepcoinAP']
    BinanceBP_BitfinexAP = results['BinanceBP_BitfinexAP']
    BinanceBP_BingXAP = results['BinanceBP_BingXAP']
    BinanceBP_OrangeXAP = results['BinanceBP_OrangeXAP']
    BinanceBP_BitvenusAP = results['BinanceBP_BitvenusAP']
    BinanceBP_BiconomyAP = results['BinanceBP_BiconomyAP']
    BinanceBP_XTAP = results['BinanceBP_XTAP']
    BinanceBP_BitflyerAP = results['BinanceBP_BitflyerAP']
    BinanceBP_CoinWAP = results['BinanceBP_CoinWAP']
    BinanceBP_ToobitAP = results['BinanceBP_ToobitAP']
    BinanceBP_TapBitAP = results['BinanceBP_TapBitAP']

    BybitBP_BinanceAP = results['BybitBP_BinanceAP']
    BybitBP_BybitAP = results['BybitBP_BybitAP']
    BybitBP_OKXAP = results['BybitBP_OKXAP']
    BybitBP_UpbitAP = results['BybitBP_UpbitAP']
    BybitBP_KucoinAP = results['BybitBP_KucoinAP']
    BybitBP_BitgetAP = results['BybitBP_BitgetAP']
    BybitBP_BitstampAP = results['BybitBP_BitstampAP']
    BybitBP_GeminiAP = results['BybitBP_GeminiAP']
    BybitBP_KrakenAP = results['BybitBP_KrakenAP']
    BybitBP_GateioAP = results['BybitBP_Gate.ioAP']
    BybitBP_HTXAP = results['BybitBP_HTXAP']
    BybitBP_MEXCAP = results['BybitBP_MEXCAP']
    BybitBP_LbankAP = results['BybitBP_LbankAP']
    BybitBP_BitmartAP = results['BybitBP_BitmartAP']
    BybitBP_DeepcoinAP = results['BybitBP_DeepcoinAP']
    BybitBP_BitfinexAP = results['BybitBP_BitfinexAP']
    BybitBP_BingXAP = results['BybitBP_BingXAP']
    BybitBP_OrangeXAP = results['BybitBP_OrangeXAP']
    BybitBP_BitvenusAP = results['BybitBP_BitvenusAP']
    BybitBP_BiconomyAP = results['BybitBP_BiconomyAP']
    BybitBP_XTAP = results['BybitBP_XTAP']
    BybitBP_BitflyerAP = results['BybitBP_BitflyerAP']
    BybitBP_CoinWAP = results['BybitBP_CoinWAP']
    BybitBP_ToobitAP = results['BybitBP_ToobitAP']
    BybitBP_TapBitAP = results['BybitBP_TapBitAP']

    OKXBP_BinanceAP = results['OKXBP_BinanceAP']
    OKXBP_BybitAP = results['OKXBP_BybitAP']
    OKXBP_OKXAP = results['OKXBP_OKXAP']
    OKXBP_UpbitAP = results['OKXBP_UpbitAP']
    OKXBP_KucoinAP = results['OKXBP_KucoinAP']
    OKXBP_BitgetAP = results['OKXBP_BitgetAP']
    OKXBP_BitstampAP = results['OKXBP_BitstampAP']
    OKXBP_GeminiAP = results['OKXBP_GeminiAP']
    OKXBP_KrakenAP = results['OKXBP_KrakenAP']
    OKXBP_GateioAP = results['OKXBP_Gate.ioAP']
    OKXBP_HTXAP = results['OKXBP_HTXAP']
    OKXBP_MEXCAP = results['OKXBP_MEXCAP']
    OKXBP_LbankAP = results['OKXBP_LbankAP']
    OKXBP_BitmartAP = results['OKXBP_BitmartAP']
    OKXBP_DeepcoinAP = results['OKXBP_DeepcoinAP']
    OKXBP_BitfinexAP = results['OKXBP_BitfinexAP']
    OKXBP_BingXAP = results['OKXBP_BingXAP']
    OKXBP_OrangeXAP = results['OKXBP_OrangeXAP']
    OKXBP_BitvenusAP = results['OKXBP_BitvenusAP']
    OKXBP_BiconomyAP = results['OKXBP_BiconomyAP']
    OKXBP_XTAP = results['OKXBP_XTAP']
    OKXBP_BitflyerAP = results['OKXBP_BitflyerAP']
    OKXBP_CoinWAP = results['OKXBP_CoinWAP']
    OKXBP_ToobitAP = results['OKXBP_ToobitAP']
    OKXBP_TapBitAP = results['OKXBP_TapBitAP']

    UpbitBP_BinanceAP = results['UpbitBP_BinanceAP']
    UpbitBP_BybitAP = results['UpbitBP_BybitAP']
    UpbitBP_OKXAP = results['UpbitBP_OKXAP']
    UpbitBP_UpbitAP = results['UpbitBP_UpbitAP']
    UpbitBP_KucoinAP = results['UpbitBP_KucoinAP']
    UpbitBP_BitgetAP = results['UpbitBP_BitgetAP']
    UpbitBP_BitstampAP = results['UpbitBP_BitstampAP']
    UpbitBP_GeminiAP = results['UpbitBP_GeminiAP']
    UpbitBP_KrakenAP = results['UpbitBP_KrakenAP']
    UpbitBP_GateioAP = results['UpbitBP_Gate.ioAP']
    UpbitBP_HTXAP = results['UpbitBP_HTXAP']
    UpbitBP_MEXCAP = results['UpbitBP_MEXCAP']
    UpbitBP_LbankAP = results['UpbitBP_LbankAP']
    UpbitBP_BitmartAP = results['UpbitBP_BitmartAP']
    UpbitBP_DeepcoinAP = results['UpbitBP_DeepcoinAP']
    UpbitBP_BitfinexAP = results['UpbitBP_BitfinexAP']
    UpbitBP_BingXAP = results['UpbitBP_BingXAP']
    UpbitBP_OrangeXAP = results['UpbitBP_OrangeXAP']
    UpbitBP_BitvenusAP = results['UpbitBP_BitvenusAP']
    UpbitBP_BiconomyAP = results['UpbitBP_BiconomyAP']
    UpbitBP_XTAP = results['UpbitBP_XTAP']
    UpbitBP_BitflyerAP = results['UpbitBP_BitflyerAP']
    UpbitBP_CoinWAP = results['UpbitBP_CoinWAP']
    UpbitBP_ToobitAP = results['UpbitBP_ToobitAP']
    UpbitBP_TapBitAP = results['UpbitBP_TapBitAP']

    KucoinBP_BinanceAP = results['KucoinBP_BinanceAP']
    KucoinBP_BybitAP = results['KucoinBP_BybitAP']
    KucoinBP_OKXAP = results['KucoinBP_OKXAP']
    KucoinBP_UpbitAP = results['KucoinBP_UpbitAP']
    KucoinBP_KucoinAP = results['KucoinBP_KucoinAP']
    KucoinBP_BitgetAP = results['KucoinBP_BitgetAP']
    KucoinBP_BitstampAP = results['KucoinBP_BitstampAP']
    KucoinBP_GeminiAP = results['KucoinBP_GeminiAP']
    KucoinBP_KrakenAP = results['KucoinBP_KrakenAP']
    KucoinBP_GateioAP = results['KucoinBP_Gate.ioAP']
    KucoinBP_HTXAP = results['KucoinBP_HTXAP']
    KucoinBP_MEXCAP = results['KucoinBP_MEXCAP']
    KucoinBP_LbankAP = results['KucoinBP_LbankAP']
    KucoinBP_BitmartAP = results['KucoinBP_BitmartAP']
    KucoinBP_DeepcoinAP = results['KucoinBP_DeepcoinAP']
    KucoinBP_BitfinexAP = results['KucoinBP_BitfinexAP']
    KucoinBP_BingXAP = results['KucoinBP_BingXAP']
    KucoinBP_OrangeXAP = results['KucoinBP_OrangeXAP']
    KucoinBP_BitvenusAP = results['KucoinBP_BitvenusAP']
    KucoinBP_BiconomyAP = results['KucoinBP_BiconomyAP']
    KucoinBP_XTAP = results['KucoinBP_XTAP']
    KucoinBP_BitflyerAP = results['KucoinBP_BitflyerAP']
    KucoinBP_CoinWAP = results['KucoinBP_CoinWAP']
    KucoinBP_ToobitAP = results['KucoinBP_ToobitAP']
    KucoinBP_TapBitAP = results['KucoinBP_TapBitAP']

    BitgetBP_BinanceAP = results['BitgetBP_BinanceAP']
    BitgetBP_BybitAP = results['BitgetBP_BybitAP']
    BitgetBP_OKXAP = results['BitgetBP_OKXAP']
    BitgetBP_UpbitAP = results['BitgetBP_UpbitAP']
    BitgetBP_KucoinAP = results['BitgetBP_KucoinAP']
    BitgetBP_BitgetAP = results['BitgetBP_BitgetAP']
    BitgetBP_BitstampAP = results['BitgetBP_BitstampAP']
    BitgetBP_GeminiAP = results['BitgetBP_GeminiAP']
    BitgetBP_KrakenAP = results['BitgetBP_KrakenAP']
    BitgetBP_GateioAP = results['BitgetBP_Gate.ioAP']
    BitgetBP_HTXAP = results['BitgetBP_HTXAP']
    BitgetBP_MEXCAP = results['BitgetBP_MEXCAP']
    BitgetBP_LbankAP = results['BitgetBP_LbankAP']
    BitgetBP_BitmartAP = results['BitgetBP_BitmartAP']
    BitgetBP_DeepcoinAP = results['BitgetBP_DeepcoinAP']
    BitgetBP_BitfinexAP = results['BitgetBP_BitfinexAP']
    BitgetBP_BingXAP = results['BitgetBP_BingXAP']
    BitgetBP_OrangeXAP = results['BitgetBP_OrangeXAP']
    BitgetBP_BitvenusAP = results['BitgetBP_BitvenusAP']
    BitgetBP_BiconomyAP = results['BitgetBP_BiconomyAP']
    BitgetBP_XTAP = results['BitgetBP_XTAP']
    BitgetBP_BitflyerAP = results['BitgetBP_BitflyerAP']
    BitgetBP_CoinWAP = results['BitgetBP_CoinWAP']
    BitgetBP_ToobitAP = results['BitgetBP_ToobitAP']
    BitgetBP_TapBitAP = results['BitgetBP_TapBitAP']

    BitstampBP_BinanceAP = results['BitstampBP_BinanceAP']
    BitstampBP_BybitAP = results['BitstampBP_BybitAP']
    BitstampBP_OKXAP = results['BitstampBP_OKXAP']
    BitstampBP_UpbitAP = results['BitstampBP_UpbitAP']
    BitstampBP_KucoinAP = results['BitstampBP_KucoinAP']
    BitstampBP_BitgetAP = results['BitstampBP_BitgetAP']
    BitstampBP_BitstampAP = results['BitstampBP_BitstampAP']
    BitstampBP_GeminiAP = results['BitstampBP_GeminiAP']
    BitstampBP_KrakenAP = results['BitstampBP_KrakenAP']
    BitstampBP_GateioAP = results['BitstampBP_Gate.ioAP']
    BitstampBP_HTXAP = results['BitstampBP_HTXAP']
    BitstampBP_MEXCAP = results['BitstampBP_MEXCAP']
    BitstampBP_LbankAP = results['BitstampBP_LbankAP']
    BitstampBP_BitmartAP = results['BitstampBP_BitmartAP']
    BitstampBP_DeepcoinAP = results['BitstampBP_DeepcoinAP']
    BitstampBP_BitfinexAP = results['BitstampBP_BitfinexAP']
    BitstampBP_BingXAP = results['BitstampBP_BingXAP']
    BitstampBP_OrangeXAP = results['BitstampBP_OrangeXAP']
    BitstampBP_BitvenusAP = results['BitstampBP_BitvenusAP']
    BitstampBP_BiconomyAP = results['BitstampBP_BiconomyAP']
    BitstampBP_XTAP = results['BitstampBP_XTAP']
    BitstampBP_BitflyerAP = results['BitstampBP_BitflyerAP']
    BitstampBP_CoinWAP = results['BitstampBP_CoinWAP']
    BitstampBP_ToobitAP = results['BitstampBP_ToobitAP']
    BitstampBP_TapBitAP = results['BitstampBP_TapBitAP']

    GeminiBP_BinanceAP = results['GeminiBP_BinanceAP']
    GeminiBP_BybitAP = results['GeminiBP_BybitAP']
    GeminiBP_OKXAP = results['GeminiBP_OKXAP']
    GeminiBP_UpbitAP = results['GeminiBP_UpbitAP']
    GeminiBP_KucoinAP = results['GeminiBP_KucoinAP']
    GeminiBP_BitgetAP = results['GeminiBP_BitgetAP']
    GeminiBP_BitstampAP = results['GeminiBP_BitstampAP']
    GeminiBP_GeminiAP = results['GeminiBP_GeminiAP']
    GeminiBP_KrakenAP = results['GeminiBP_KrakenAP']
    GeminiBP_GateioAP = results['GeminiBP_Gate.ioAP']
    GeminiBP_HTXAP = results['GeminiBP_HTXAP']
    GeminiBP_MEXCAP = results['GeminiBP_MEXCAP']
    GeminiBP_LbankAP = results['GeminiBP_LbankAP']
    GeminiBP_BitmartAP = results['GeminiBP_BitmartAP']
    GeminiBP_DeepcoinAP = results['GeminiBP_DeepcoinAP']
    GeminiBP_BitfinexAP = results['GeminiBP_BitfinexAP']
    GeminiBP_BingXAP = results['GeminiBP_BingXAP']
    GeminiBP_OrangeXAP = results['GeminiBP_OrangeXAP']
    GeminiBP_BitvenusAP = results['GeminiBP_BitvenusAP']
    GeminiBP_BiconomyAP = results['GeminiBP_BiconomyAP']
    GeminiBP_XTAP = results['GeminiBP_XTAP']
    GeminiBP_BitflyerAP = results['GeminiBP_BitflyerAP']
    GeminiBP_CoinWAP = results['GeminiBP_CoinWAP']
    GeminiBP_ToobitAP = results['GeminiBP_ToobitAP']
    GeminiBP_TapBitAP = results['GeminiBP_TapBitAP']

    KrakenBP_BinanceAP = results['KrakenBP_BinanceAP']
    KrakenBP_BybitAP = results['KrakenBP_BybitAP']
    KrakenBP_OKXAP = results['KrakenBP_OKXAP']
    KrakenBP_UpbitAP = results['KrakenBP_UpbitAP']
    KrakenBP_KucoinAP = results['KrakenBP_KucoinAP']
    KrakenBP_BitgetAP = results['KrakenBP_BitgetAP']
    KrakenBP_BitstampAP = results['KrakenBP_BitstampAP']
    KrakenBP_GeminiAP = results['KrakenBP_GeminiAP']
    KrakenBP_KrakenAP = results['KrakenBP_KrakenAP']
    KrakenBP_GateioAP = results['KrakenBP_Gate.ioAP']
    KrakenBP_HTXAP = results['KrakenBP_HTXAP']
    KrakenBP_MEXCAP = results['KrakenBP_MEXCAP']
    KrakenBP_LbankAP = results['KrakenBP_LbankAP']
    KrakenBP_BitmartAP = results['KrakenBP_BitmartAP']
    KrakenBP_DeepcoinAP = results['KrakenBP_DeepcoinAP']
    KrakenBP_BitfinexAP = results['KrakenBP_BitfinexAP']
    KrakenBP_BingXAP = results['KrakenBP_BingXAP']
    KrakenBP_OrangeXAP = results['KrakenBP_OrangeXAP']
    KrakenBP_BitvenusAP = results['KrakenBP_BitvenusAP']
    KrakenBP_BiconomyAP = results['KrakenBP_BiconomyAP']
    KrakenBP_XTAP = results['KrakenBP_XTAP']
    KrakenBP_BitflyerAP = results['KrakenBP_BitflyerAP']
    KrakenBP_CoinWAP = results['KrakenBP_CoinWAP']
    KrakenBP_ToobitAP = results['KrakenBP_ToobitAP']
    KrakenBP_TapBitAP = results['KrakenBP_TapBitAP']

    GateioBP_BinanceAP = results['Gate.ioBP_BinanceAP']
    GateioBP_BybitAP = results['Gate.ioBP_BybitAP']
    GateioBP_OKXAP = results['Gate.ioBP_OKXAP']
    GateioBP_UpbitAP = results['Gate.ioBP_UpbitAP']
    GateioBP_KucoinAP = results['Gate.ioBP_KucoinAP']
    GateioBP_BitgetAP = results['Gate.ioBP_BitgetAP']
    GateioBP_BitstampAP = results['Gate.ioBP_BitstampAP']
    GateioBP_GeminiAP = results['Gate.ioBP_GeminiAP']
    GateioBP_KrakenAP = results['Gate.ioBP_KrakenAP']
    GateioBP_GateioAP = results['Gate.ioBP_Gate.ioAP']
    GateioBP_HTXAP = results['Gate.ioBP_HTXAP']
    GateioBP_MEXCAP = results['Gate.ioBP_MEXCAP']
    GateioBP_LbankAP = results['Gate.ioBP_LbankAP']
    GateioBP_BitmartAP = results['Gate.ioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['Gate.ioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['Gate.ioBP_BitfinexAP']
    GateioBP_BingXAP = results['Gate.ioBP_BingXAP']
    GateioBP_OrangeXAP = results['Gate.ioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['Gate.ioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['Gate.ioBP_BiconomyAP']
    GateioBP_XTAP = results['Gate.ioBP_XTAP']
    GateioBP_BitflyerAP = results['Gate.ioBP_BitflyerAP']
    GateioBP_CoinWAP = results['Gate.ioBP_CoinWAP']
    GateioBP_ToobitAP = results['Gate.ioBP_ToobitAP']
    GateioBP_TapBitAP = results['Gate.ioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_Gate.ioAP']
    HTXBP_HTXAP = results['HTXBP_HTXAP']
    HTXBP_MEXCAP = results['HTXBP_MEXCAP']
    HTXBP_LbankAP = results['HTXBP_LbankAP']
    HTXBP_BitmartAP = results['HTXBP_BitmartAP']
    HTXBP_DeepcoinAP = results['HTXBP_DeepcoinAP']
    HTXBP_BitfinexAP = results['HTXBP_BitfinexAP']
    HTXBP_BingXAP = results['HTXBP_BingXAP']
    HTXBP_OrangeXAP = results['HTXBP_OrangeXAP']
    HTXBP_BitvenusAP = results['HTXBP_BitvenusAP']
    HTXBP_BiconomyAP = results['HTXBP_BiconomyAP']
    HTXBP_XTAP = results['HTXBP_XTAP']
    HTXBP_BitflyerAP = results['HTXBP_BitflyerAP']
    HTXBP_CoinWAP = results['HTXBP_CoinWAP']
    HTXBP_ToobitAP = results['HTXBP_ToobitAP']
    HTXBP_TapBitAP = results['HTXBP_TapBitAP']

    MEXCBP_BinanceAP = results['MEXCBP_BinanceAP']
    MEXCBP_BybitAP = results['MEXCBP_BybitAP']
    MEXCBP_OKXAP = results['MEXCBP_OKXAP']
    MEXCBP_UpbitAP = results['MEXCBP_UpbitAP']
    MEXCBP_KucoinAP = results['MEXCBP_KucoinAP']
    MEXCBP_BitgetAP = results['MEXCBP_BitgetAP']
    MEXCBP_BitstampAP = results['MEXCBP_BitstampAP']
    MEXCBP_GeminiAP = results['MEXCBP_GeminiAP']
    MEXCBP_KrakenAP = results['MEXCBP_KrakenAP']
    MEXCBP_GateioAP = results['BinanceBP_Gate.ioAP']
    MEXCBP_HTXAP = results['MEXCBP_HTXAP']
    MEXCBP_MEXCAP = results['MEXCBP_MEXCAP']
    MEXCBP_LbankAP = results['MEXCBP_LbankAP']
    MEXCBP_BitmartAP = results['MEXCBP_BitmartAP']
    MEXCBP_DeepcoinAP = results['MEXCBP_DeepcoinAP']
    MEXCBP_BitfinexAP = results['MEXCBP_BitfinexAP']
    MEXCBP_BingXAP = results['MEXCBP_BingXAP']
    MEXCBP_OrangeXAP = results['MEXCBP_OrangeXAP']
    MEXCBP_BitvenusAP = results['MEXCBP_BitvenusAP']
    MEXCBP_BiconomyAP = results['MEXCBP_BiconomyAP']
    MEXCBP_XTAP = results['MEXCBP_XTAP']
    MEXCBP_BitflyerAP = results['MEXCBP_BitflyerAP']
    MEXCBP_CoinWAP = results['MEXCBP_CoinWAP']
    MEXCBP_ToobitAP = results['MEXCBP_ToobitAP']
    MEXCBP_TapBitAP = results['MEXCBP_TapBitAP']

    LbankBP_BinanceAP = results['LbankBP_BinanceAP']
    LbankBP_BybitAP = results['LbankBP_BybitAP']
    LbankBP_OKXAP = results['LbankBP_OKXAP']
    LbankBP_UpbitAP = results['LbankBP_UpbitAP']
    LbankBP_KucoinAP = results['LbankBP_KucoinAP']
    LbankBP_BitgetAP = results['LbankBP_BitgetAP']
    LbankBP_BitstampAP = results['LbankBP_BitstampAP']
    LbankBP_GeminiAP = results['LbankBP_GeminiAP']
    LbankBP_KrakenAP = results['LbankBP_KrakenAP']
    LbankBP_GateioAP = results['LbankBP_Gate.ioAP']
    LbankBP_HTXAP = results['LbankBP_HTXAP']
    LbankBP_MEXCAP = results['LbankBP_MEXCAP']
    LbankBP_LbankAP = results['LbankBP_LbankAP']
    LbankBP_BitmartAP = results['LbankBP_BitmartAP']
    LbankBP_DeepcoinAP = results['LbankBP_DeepcoinAP']
    LbankBP_BitfinexAP = results['LbankBP_BitfinexAP']
    LbankBP_BingXAP = results['LbankBP_BingXAP']
    LbankBP_OrangeXAP = results['LbankBP_OrangeXAP']
    LbankBP_BitvenusAP = results['LbankBP_BitvenusAP']
    LbankBP_BiconomyAP = results['LbankBP_BiconomyAP']
    LbankBP_XTAP = results['LbankBP_XTAP']
    LbankBP_BitflyerAP = results['LbankBP_BitflyerAP']
    LbankBP_CoinWAP = results['LbankBP_CoinWAP']
    LbankBP_ToobitAP = results['LbankBP_ToobitAP']
    LbankBP_TapBitAP = results['LbankBP_TapBitAP']

    BitmartBP_BinanceAP = results['BitmartBP_BinanceAP']
    BitmartBP_BybitAP = results['BitmartBP_BybitAP']
    BitmartBP_OKXAP = results['BitmartBP_OKXAP']
    BitmartBP_UpbitAP = results['BitmartBP_UpbitAP']
    BitmartBP_KucoinAP = results['BitmartBP_KucoinAP']
    BitmartBP_BitgetAP = results['BitmartBP_BitgetAP']
    BitmartBP_BitstampAP = results['BitmartBP_BitstampAP']
    BitmartBP_GeminiAP = results['BitmartBP_GeminiAP']
    BitmartBP_KrakenAP = results['BitmartBP_KrakenAP']
    BitmartBP_GateioAP = results['BitmartBP_Gate.ioAP']
    BitmartBP_HTXAP = results['BitmartBP_HTXAP']
    BitmartBP_MEXCAP = results['BitmartBP_MEXCAP']
    BitmartBP_LbankAP = results['BitmartBP_LbankAP']
    BitmartBP_BitmartAP = results['BitmartBP_BitmartAP']
    BitmartBP_DeepcoinAP = results['BitmartBP_DeepcoinAP']
    BitmartBP_BitfinexAP = results['BitmartBP_BitfinexAP']
    BitmartBP_BingXAP = results['BitmartBP_BingXAP']
    BitmartBP_OrangeXAP = results['BitmartBP_OrangeXAP']
    BitmartBP_BitvenusAP = results['BitmartBP_BitvenusAP']
    BitmartBP_BiconomyAP = results['BitmartBP_BiconomyAP']
    BitmartBP_XTAP = results['BitmartBP_XTAP']
    BitmartBP_BitflyerAP = results['BitmartBP_BitflyerAP']
    BitmartBP_CoinWAP = results['BitmartBP_CoinWAP']
    BitmartBP_ToobitAP = results['BitmartBP_ToobitAP']
    BitmartBP_TapBitAP = results['BitmartBP_TapBitAP']

    DeepcoinBP_BinanceAP = results['DeepcoinBP_BinanceAP']
    DeepcoinBP_BybitAP = results['DeepcoinBP_BybitAP']
    DeepcoinBP_OKXAP = results['DeepcoinBP_OKXAP']
    DeepcoinBP_UpbitAP = results['DeepcoinBP_UpbitAP']
    DeepcoinBP_KucoinAP = results['DeepcoinBP_KucoinAP']
    DeepcoinBP_BitgetAP = results['DeepcoinBP_BitgetAP']
    DeepcoinBP_BitstampAP = results['DeepcoinBP_BitstampAP']
    DeepcoinBP_GeminiAP = results['DeepcoinBP_GeminiAP']
    DeepcoinBP_KrakenAP = results['DeepcoinBP_KrakenAP']
    DeepcoinBP_GateioAP = results['DeepcoinBP_Gate.ioAP']
    DeepcoinBP_HTXAP = results['DeepcoinBP_HTXAP']
    DeepcoinBP_MEXCAP = results['DeepcoinBP_MEXCAP']
    DeepcoinBP_LbankAP = results['DeepcoinBP_LbankAP']
    DeepcoinBP_BitmartAP = results['DeepcoinBP_BitmartAP']
    DeepcoinBP_DeepcoinAP = results['DeepcoinBP_DeepcoinAP']
    DeepcoinBP_BitfinexAP = results['DeepcoinBP_BitfinexAP']
    DeepcoinBP_BingXAP = results['DeepcoinBP_BingXAP']
    DeepcoinBP_OrangeXAP = results['DeepcoinBP_OrangeXAP']
    DeepcoinBP_BitvenusAP = results['DeepcoinBP_BitvenusAP']
    DeepcoinBP_BiconomyAP = results['DeepcoinBP_BiconomyAP']
    DeepcoinBP_XTAP = results['DeepcoinBP_XTAP']
    DeepcoinBP_BitflyerAP = results['DeepcoinBP_BitflyerAP']
    DeepcoinBP_CoinWAP = results['DeepcoinBP_CoinWAP']
    DeepcoinBP_ToobitAP = results['DeepcoinBP_ToobitAP']
    DeepcoinBP_TapBitAP = results['DeepcoinBP_TapBitAP']

    BitfinexBP_BinanceAP = results['BitfinexBP_BinanceAP']
    BitfinexBP_BybitAP = results['BitfinexBP_BybitAP']
    BitfinexBP_OKXAP = results['BitfinexBP_OKXAP']
    BitfinexBP_UpbitAP = results['BitfinexBP_UpbitAP']
    BitfinexBP_KucoinAP = results['BitfinexBP_KucoinAP']
    BitfinexBP_BitgetAP = results['BitfinexBP_BitgetAP']
    BitfinexBP_BitstampAP = results['BitfinexBP_BitstampAP']
    BitfinexBP_GeminiAP = results['BitfinexBP_GeminiAP']
    BitfinexBP_KrakenAP = results['BitfinexBP_KrakenAP']
    BitfinexBP_GateioAP = results['BitfinexBP_Gate.ioAP']
    BitfinexBP_HTXAP = results['BitfinexBP_HTXAP']
    BitfinexBP_MEXCAP = results['BitfinexBP_MEXCAP']
    BitfinexBP_LbankAP = results['BitfinexBP_LbankAP']
    BitfinexBP_BitmartAP = results['BitfinexBP_BitmartAP']
    BitfinexBP_DeepcoinAP = results['BitfinexBP_DeepcoinAP']
    BitfinexBP_BitfinexAP = results['BitfinexBP_BitfinexAP']
    BitfinexBP_BingXAP = results['BitfinexBP_BingXAP']
    BitfinexBP_OrangeXAP = results['BitfinexBP_OrangeXAP']
    BitfinexBP_BitvenusAP = results['BitfinexBP_BitvenusAP']
    BitfinexBP_BiconomyAP = results['BitfinexBP_BiconomyAP']
    BitfinexBP_XTAP = results['BitfinexBP_XTAP']
    BitfinexBP_BitflyerAP = results['BitfinexBP_BitflyerAP']
    BitfinexBP_CoinWAP = results['BitfinexBP_CoinWAP']
    BitfinexBP_ToobitAP = results['BitfinexBP_ToobitAP']
    BitfinexBP_TapBitAP = results['BitfinexBP_TapBitAP']

    BingXBP_BinanceAP = results['BingXBP_BinanceAP']
    BingXBP_BybitAP = results['BingXBP_BybitAP']
    BingXBP_OKXAP = results['BingXBP_OKXAP']
    BingXBP_UpbitAP = results['BingXBP_UpbitAP']
    BingXBP_KucoinAP = results['BingXBP_KucoinAP']
    BingXBP_BitgetAP = results['BingXBP_BitgetAP']
    BingXBP_BitstampAP = results['BingXBP_BitstampAP']
    BingXBP_GeminiAP = results['BingXBP_GeminiAP']
    BingXBP_KrakenAP = results['BingXBP_KrakenAP']
    BingXBP_GateioAP = results['BingXBP_Gate.ioAP']
    BingXBP_HTXAP = results['BingXBP_HTXAP']
    BingXBP_MEXCAP = results['BingXBP_MEXCAP']
    BingXBP_LbankAP = results['BingXBP_LbankAP']
    BingXBP_BitmartAP = results['BingXBP_BitmartAP']
    BingXBP_DeepcoinAP = results['BingXBP_DeepcoinAP']
    BingXBP_BitfinexAP = results['BingXBP_BitfinexAP']
    BingXBP_BingXAP = results['BingXBP_BingXAP']
    BingXBP_OrangeXAP = results['BingXBP_OrangeXAP']
    BingXBP_BitvenusAP = results['BingXBP_BitvenusAP']
    BingXBP_BiconomyAP = results['BingXBP_BiconomyAP']
    BingXBP_XTAP = results['BingXBP_XTAP']
    BingXBP_BitflyerAP = results['BingXBP_BitflyerAP']
    BingXBP_CoinWAP = results['BingXBP_CoinWAP']
    BingXBP_ToobitAP = results['BingXBP_ToobitAP']
    BingXBP_TapBitAP = results['BingXBP_TapBitAP']

    OrangeXBP_BinanceAP = results['OrangeXBP_BinanceAP']
    OrangeXBP_BybitAP = results['OrangeXBP_BybitAP']
    OrangeXBP_OKXAP = results['OrangeXBP_OKXAP']
    OrangeXBP_UpbitAP = results['OrangeXBP_UpbitAP']
    OrangeXBP_KucoinAP = results['OrangeXBP_KucoinAP']
    OrangeXBP_BitgetAP = results['OrangeXBP_BitgetAP']
    OrangeXBP_BitstampAP = results['OrangeXBP_BitstampAP']
    OrangeXBP_GeminiAP = results['OrangeXBP_GeminiAP']
    OrangeXBP_KrakenAP = results['OrangeXBP_KrakenAP']
    OrangeXBP_GateioAP = results['OrangeXBP_Gate.ioAP']
    OrangeXBP_HTXAP = results['OrangeXBP_HTXAP']
    OrangeXBP_MEXCAP = results['OrangeXBP_MEXCAP']
    OrangeXBP_LbankAP = results['OrangeXBP_LbankAP']
    OrangeXBP_BitmartAP = results['OrangeXBP_BitmartAP']
    OrangeXBP_DeepcoinAP = results['OrangeXBP_DeepcoinAP']
    OrangeXBP_BitfinexAP = results['OrangeXBP_BitfinexAP']
    OrangeXBP_BingXAP = results['OrangeXBP_BingXAP']
    OrangeXBP_OrangeXAP = results['OrangeXBP_OrangeXAP']
    OrangeXBP_BitvenusAP = results['OrangeXBP_BitvenusAP']
    OrangeXBP_BiconomyAP = results['OrangeXBP_BiconomyAP']
    OrangeXBP_XTAP = results['OrangeXBP_XTAP']
    OrangeXBP_BitflyerAP = results['OrangeXBP_BitflyerAP']
    OrangeXBP_CoinWAP = results['OrangeXBP_CoinWAP']
    OrangeXBP_ToobitAP = results['OrangeXBP_ToobitAP']
    OrangeXBP_TapBitAP = results['OrangeXBP_TapBitAP']

    BitvenusBP_BinanceAP = results['BitvenusBP_BinanceAP']
    BitvenusBP_BybitAP = results['BitvenusBP_BybitAP']
    BitvenusBP_OKXAP = results['BitvenusBP_OKXAP']
    BitvenusBP_UpbitAP = results['BitvenusBP_UpbitAP']
    BitvenusBP_KucoinAP = results['BitvenusBP_KucoinAP']
    BitvenusBP_BitgetAP = results['BitvenusBP_BitgetAP']
    BitvenusBP_BitstampAP = results['BitvenusBP_BitstampAP']
    BitvenusBP_GeminiAP = results['BitvenusBP_GeminiAP']
    BitvenusBP_KrakenAP = results['BitvenusBP_KrakenAP']
    BitvenusBP_GateioAP = results['BitvenusBP_Gate.ioAP']
    BitvenusBP_HTXAP = results['BitvenusBP_HTXAP']
    BitvenusBP_MEXCAP = results['BitvenusBP_MEXCAP']
    BitvenusBP_LbankAP = results['BitvenusBP_LbankAP']
    BitvenusBP_BitmartAP = results['BitvenusBP_BitmartAP']
    BitvenusBP_DeepcoinAP = results['BitvenusBP_DeepcoinAP']
    BitvenusBP_BitfinexAP = results['BitvenusBP_BitfinexAP']
    BitvenusBP_BingXAP = results['BitvenusBP_BingXAP']
    BitvenusBP_OrangeXAP = results['BitvenusBP_OrangeXAP']
    BitvenusBP_BitvenusAP = results['BitvenusBP_BitvenusAP']
    BitvenusBP_BiconomyAP = results['BitvenusBP_BiconomyAP']
    BitvenusBP_XTAP = results['BitvenusBP_XTAP']
    BitvenusBP_BitflyerAP = results['BitvenusBP_BitflyerAP']
    BitvenusBP_CoinWAP = results['BitvenusBP_CoinWAP']
    BitvenusBP_ToobitAP = results['BitvenusBP_ToobitAP']
    BitvenusBP_TapBitAP = results['BitvenusBP_TapBitAP']

    BiconomyBP_BinanceAP = results['BiconomyBP_BinanceAP']
    BiconomyBP_BybitAP = results['BiconomyBP_BybitAP']
    BiconomyBP_OKXAP = results['BiconomyBP_OKXAP']
    BiconomyBP_UpbitAP = results['BiconomyBP_UpbitAP']
    BiconomyBP_KucoinAP = results['BiconomyBP_KucoinAP']
    BiconomyBP_BitgetAP = results['BiconomyBP_BitgetAP']
    BiconomyBP_BitstampAP = results['BiconomyBP_BitstampAP']
    BiconomyBP_GeminiAP = results['BiconomyBP_GeminiAP']
    BiconomyBP_KrakenAP = results['BiconomyBP_KrakenAP']
    BiconomyBP_GateioAP = results['BiconomyBP_Gate.ioAP']
    BiconomyBP_HTXAP = results['BiconomyBP_HTXAP']
    BiconomyBP_MEXCAP = results['BiconomyBP_MEXCAP']
    BiconomyBP_LbankAP = results['BiconomyBP_LbankAP']
    BiconomyBP_BitmartAP = results['BiconomyBP_BitmartAP']
    BiconomyBP_DeepcoinAP = results['BiconomyBP_DeepcoinAP']
    BiconomyBP_BitfinexAP = results['BiconomyBP_BitfinexAP']
    BiconomyBP_BingXAP = results['BiconomyBP_BingXAP']
    BiconomyBP_OrangeXAP = results['BiconomyBP_OrangeXAP']
    BiconomyBP_BitvenusAP = results['BiconomyBP_BitvenusAP']
    BiconomyBP_BiconomyAP = results['BiconomyBP_BiconomyAP']
    BiconomyBP_XTAP = results['BiconomyBP_XTAP']
    BiconomyBP_BitflyerAP = results['BiconomyBP_BitflyerAP']
    BiconomyBP_CoinWAP = results['BiconomyBP_CoinWAP']
    BiconomyBP_ToobitAP = results['BiconomyBP_ToobitAP']
    BiconomyBP_TapBitAP = results['BiconomyBP_TapBitAP']

    XTBP_BinanceAP = results['XTBP_BinanceAP']
    XTBP_BybitAP = results['XTBP_BybitAP']
    XTBP_OKXAP = results['XTBP_OKXAP']
    XTBP_UpbitAP = results['XTBP_UpbitAP']
    XTBP_KucoinAP = results['XTBP_KucoinAP']
    XTBP_BitgetAP = results['XTBP_BitgetAP']
    XTBP_BitstampAP = results['XTBP_BitstampAP']
    XTBP_GeminiAP = results['XTBP_GeminiAP']
    XTBP_KrakenAP = results['XTBP_KrakenAP']
    XTBP_GateioAP = results['XTBP_Gate.ioAP']
    XTBP_HTXAP = results['XTBP_HTXAP']
    XTBP_MEXCAP = results['XTBP_MEXCAP']
    XTBP_LbankAP = results['XTBP_LbankAP']
    XTBP_BitmartAP = results['XTBP_BitmartAP']
    XTBP_DeepcoinAP = results['XTBP_DeepcoinAP']
    XTBP_BitfinexAP = results['XTBP_BitfinexAP']
    XTBP_BingXAP = results['XTBP_BingXAP']
    XTBP_OrangeXAP = results['XTBP_OrangeXAP']
    XTBP_BitvenusAP = results['XTBP_BitvenusAP']
    XTBP_BiconomyAP = results['XTBP_BiconomyAP']
    XTBP_XTAP = results['XTBP_XTAP']
    XTBP_BitflyerAP = results['XTBP_BitflyerAP']
    XTBP_CoinWAP = results['XTBP_CoinWAP']
    XTBP_ToobitAP = results['XTBP_ToobitAP']
    XTBP_TapBitAP = results['XTBP_TapBitAP']

    BitflyerBP_BinanceAP = results['BitflyerBP_BinanceAP']
    BitflyerBP_BybitAP = results['BitflyerBP_BybitAP']
    BitflyerBP_OKXAP = results['BitflyerBP_OKXAP']
    BitflyerBP_UpbitAP = results['BitflyerBP_UpbitAP']
    BitflyerBP_KucoinAP = results['BitflyerBP_KucoinAP']
    BitflyerBP_BitgetAP = results['BitflyerBP_BitgetAP']
    BitflyerBP_BitstampAP = results['BitflyerBP_BitstampAP']
    BitflyerBP_GeminiAP = results['BitflyerBP_GeminiAP']
    BitflyerBP_KrakenAP = results['BitflyerBP_KrakenAP']
    BitflyerBP_GateioAP = results['BitflyerBP_Gate.ioAP']
    BitflyerBP_HTXAP = results['BitflyerBP_HTXAP']
    BitflyerBP_MEXCAP = results['BitflyerBP_MEXCAP']
    BitflyerBP_LbankAP = results['BitflyerBP_LbankAP']
    BitflyerBP_BitmartAP = results['BitflyerBP_BitmartAP']
    BitflyerBP_DeepcoinAP = results['BitflyerBP_DeepcoinAP']
    BitflyerBP_BitfinexAP = results['BitflyerBP_BitfinexAP']
    BitflyerBP_BingXAP = results['BitflyerBP_BingXAP']
    BitflyerBP_OrangeXAP = results['BitflyerBP_OrangeXAP']
    BitflyerBP_BitvenusAP = results['BitflyerBP_BitvenusAP']
    BitflyerBP_BiconomyAP = results['BitflyerBP_BiconomyAP']
    BitflyerBP_XTAP = results['BitflyerBP_XTAP']
    BitflyerBP_BitflyerAP = results['BitflyerBP_BitflyerAP']
    BitflyerBP_CoinWAP = results['BitflyerBP_CoinWAP']
    BitflyerBP_ToobitAP = results['BitflyerBP_ToobitAP']
    BitflyerBP_TapBitAP = results['BitflyerBP_TapBitAP']

    CoinWBP_BinanceAP = results['CoinWBP_BinanceAP']
    CoinWBP_BybitAP = results['CoinWBP_BybitAP']
    CoinWBP_OKXAP = results['CoinWBP_OKXAP']
    CoinWBP_UpbitAP = results['CoinWBP_UpbitAP']
    CoinWBP_KucoinAP = results['CoinWBP_KucoinAP']
    CoinWBP_BitgetAP = results['CoinWBP_BitgetAP']
    CoinWBP_BitstampAP = results['CoinWBP_BitstampAP']
    CoinWBP_GeminiAP = results['CoinWBP_GeminiAP']
    CoinWBP_KrakenAP = results['CoinWBP_KrakenAP']
    CoinWBP_GateioAP = results['CoinWBP_Gate.ioAP']
    CoinWBP_HTXAP = results['CoinWBP_HTXAP']
    CoinWBP_MEXCAP = results['CoinWBP_MEXCAP']
    CoinWBP_LbankAP = results['CoinWBP_LbankAP']
    CoinWBP_BitmartAP = results['CoinWBP_BitmartAP']
    CoinWBP_DeepcoinAP = results['CoinWBP_DeepcoinAP']
    CoinWBP_BitfinexAP = results['CoinWBP_BitfinexAP']
    CoinWBP_BingXAP = results['CoinWBP_BingXAP']
    CoinWBP_OrangeXAP = results['CoinWBP_OrangeXAP']
    CoinWBP_BitvenusAP = results['CoinWBP_BitvenusAP']
    CoinWBP_BiconomyAP = results['CoinWBP_BiconomyAP']
    CoinWBP_XTAP = results['CoinWBP_XTAP']
    CoinWBP_BitflyerAP = results['CoinWBP_BitflyerAP']
    CoinWBP_CoinWAP = results['CoinWBP_CoinWAP']
    CoinWBP_ToobitAP = results['CoinWBP_ToobitAP']
    CoinWBP_TapBitAP = results['CoinWBP_TapBitAP']

    ToobitBP_BinanceAP = results['ToobitBP_BinanceAP']
    ToobitBP_BybitAP = results['ToobitBP_BybitAP']
    ToobitBP_OKXAP = results['ToobitBP_OKXAP']
    ToobitBP_UpbitAP = results['ToobitBP_UpbitAP']
    ToobitBP_KucoinAP = results['ToobitBP_KucoinAP']
    ToobitBP_BitgetAP = results['ToobitBP_BitgetAP']
    ToobitBP_BitstampAP = results['ToobitBP_BitstampAP']
    ToobitBP_GeminiAP = results['ToobitBP_GeminiAP']
    ToobitBP_KrakenAP = results['ToobitBP_KrakenAP']
    ToobitBP_GateioAP = results['ToobitBP_Gate.ioAP']
    ToobitBP_HTXAP = results['ToobitBP_HTXAP']
    ToobitBP_MEXCAP = results['ToobitBP_MEXCAP']
    ToobitBP_LbankAP = results['ToobitBP_LbankAP']
    ToobitBP_BitmartAP = results['ToobitBP_BitmartAP']
    ToobitBP_DeepcoinAP = results['ToobitBP_DeepcoinAP']
    ToobitBP_BitfinexAP = results['ToobitBP_BitfinexAP']
    ToobitBP_BingXAP = results['ToobitBP_BingXAP']
    ToobitBP_OrangeXAP = results['ToobitBP_OrangeXAP']
    ToobitBP_BitvenusAP = results['ToobitBP_BitvenusAP']
    ToobitBP_BiconomyAP = results['ToobitBP_BiconomyAP']
    ToobitBP_XTAP = results['ToobitBP_XTAP']
    ToobitBP_BitflyerAP = results['ToobitBP_BitflyerAP']
    ToobitBP_CoinWAP = results['ToobitBP_CoinWAP']
    ToobitBP_ToobitAP = results['ToobitBP_ToobitAP']
    ToobitBP_TapBitAP = results['ToobitBP_TapBitAP']

    TapBitBP_BinanceAP = results['TapBitBP_BinanceAP']
    TapBitBP_BybitAP = results['TapBitBP_BybitAP']
    TapBitBP_OKXAP = results['TapBitBP_OKXAP']
    TapBitBP_UpbitAP = results['TapBitBP_UpbitAP']
    TapBitBP_KucoinAP = results['TapBitBP_KucoinAP']
    TapBitBP_BitgetAP = results['TapBitBP_BitgetAP']
    TapBitBP_BitstampAP = results['TapBitBP_BitstampAP']
    TapBitBP_GeminiAP = results['TapBitBP_GeminiAP']
    TapBitBP_KrakenAP = results['TapBitBP_KrakenAP']
    TapBitBP_GateioAP = results['TapBitBP_Gate.ioAP']
    TapBitBP_HTXAP = results['TapBitBP_HTXAP']
    TapBitBP_MEXCAP = results['TapBitBP_MEXCAP']
    TapBitBP_LbankAP = results['TapBitBP_LbankAP']
    TapBitBP_BitmartAP = results['TapBitBP_BitmartAP']
    TapBitBP_DeepcoinAP = results['TapBitBP_DeepcoinAP']
    TapBitBP_BitfinexAP = results['TapBitBP_BitfinexAP']
    TapBitBP_BingXAP = results['TapBitBP_BingXAP']
    TapBitBP_OrangeXAP = results['TapBitBP_OrangeXAP']
    TapBitBP_BitvenusAP = results['TapBitBP_BitvenusAP']
    TapBitBP_BiconomyAP = results['TapBitBP_BiconomyAP']
    TapBitBP_XTAP = results['TapBitBP_XTAP']
    TapBitBP_BitflyerAP = results['TapBitBP_BitflyerAP']
    TapBitBP_CoinWAP = results['TapBitBP_CoinWAP']
    TapBitBP_ToobitAP = results['TapBitBP_ToobitAP']
    TapBitBP_TapBitAP = results['TapBitBP_TapBitAP']

    end =time.perf_counter_ns()
    processingtime = (end - start)+inital_time


    # "Binance",BinanceLTP,BinanceAP1,BinanceAP1V,BinanceBP1,BinanceBP1V,
    def Buckets(Name, LTP, AP3, AP3V, BP3, BP3V, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11,
                sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19, sub20, sub21, sub22, sub23, sub24, sub25,
                Status):
        tasks = []
        with ThreadPoolExecutor() as executor:
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Binance", BinanceLTP, BinanceAP3,
                                BinanceAP3V, BinanceBP3, BinanceBP3V, processingtime, sub1, Status, Binance_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bybit", BybitLTP, BybitAP3,
                                BybitAP3V, BybitBP3, BybitBP3V, processingtime, sub2, Status, BybitStatus))
            tasks.append(
                executor.submit(checker, OKXOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "OKX", OKXLTP, OKXAP3, OKXAP3V,
                                OKXBP3, OKXBP3V, processingtime, sub3, Binance_Status, OKX_Status))
            tasks.append(
                executor.submit(checker, UpbitOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Upbit", UpbitLTP, UpbitAP3,
                                UpbitAP3V, UpbitBP3, UpbitBP3V, processingtime, sub4, Status, Upbit_Status))
            tasks.append(
                executor.submit(checker, KucoinOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Kucoin", KucoinLTP, KucoinAP3,
                                KucoinAP3V, KucoinBP3, KucoinBP3V, processingtime, sub5, Status, Kucoin_Status))
            tasks.append(
                executor.submit(checker, BitgetOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitget", BitgetLTP, BitgetAP3,
                                BitgetAP3V, BitgetBP3, BitgetBP3V, processingtime, sub6, Status, Bitget_Status))
            tasks.append(executor.submit(checker, BitstampOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitstamp", BitstampLTP,
                                         BitstampAP3, BitstampAP3V, BitstampBP3, BitstampBP3V, processingtime, sub7,
                                         Status, Bitstamp_Status))
            tasks.append(
                executor.submit(checker, KrakenOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Kraken", KrakenLTP, KrakenAP3,
                                KrakenAP3V, KrakenBP3, KrakenBP3V, processingtime, sub8, Status, Kraken_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Gate.io", GateioLTP, GateioAP3,
                                GateioAP3V, GateioBP3, GateioBP3V, processingtime, sub9, Status, Gateio_Status))
            tasks.append(
                executor.submit(checker, HTXOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "HTX", HTXLTP, HTXAP3, HTXAP3V,
                                HTXBP3, HTXBP3V, processingtime, sub10, Status, HTX_Status))
            tasks.append(
                executor.submit(checker, MEXCOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "MEXC", MEXCLTP, MEXCAP3, MEXCAP3V,
                                MEXCBP3, MEXCBP3V, processingtime, sub11, Status, MEXC_Status))
            tasks.append(
                executor.submit(checker, LbankOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Lbank", LbankLTP, LbankAP3,
                                LbankAP3V, LbankBP3, LbankBP3V, processingtime, sub12, Status, Lbank_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitmart", BitmartLTP, BitmartAP3,
                                BitmartAP3V, BitmartBP3, BitmartBP3V, processingtime, sub13, Status, Bitmart_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Deepcoin", DeepcoinLTP,
                                         DeepcoinAP3, DeepcoinAP3V, DeepcoinBP3, DeepcoinBP3V, processingtime, sub14,
                                         Status, Deepcoin_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitfinex", BitfinexLTP,
                                         BitfinexAP3, BitfinexAP3V, BitfinexBP3, BitfinexBP3V, processingtime, sub15,
                                         Status, Bitfinex_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "BingX", BingXLTP, BingXAP3,
                                BingXAP3V, BingXBP3, BingXBP3V, processingtime, sub16, Status, BingX_Status))
            tasks.append(
                executor.submit(checker, OrangeXOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "OrangeX", OrangeXLTP, OrangeXAP3,
                                OrangeXAP3V, OrangeXBP3, OrangeXBP3V, processingtime, sub17, Status, OrangeX_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitvenus", BitvenusLTP,
                                         BitvenusAP3, BitvenusAP3V, BitvenusBP3, BitvenusBP3V, processingtime, sub18,
                                         Status, Bitvenus_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Biconomy", BiconomyLTP,
                                         BiconomyAP3, BiconomyAP3V, BiconomyBP3, BiconomyBP3V, processingtime, sub19,
                                         Status, Biconomy_Status))
            tasks.append(
                executor.submit(checker, GeminiOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Gemini", GeminiLTP, GeminiAP3,
                                GeminiAP3V, GeminiBP3, GeminiBP3V, processingtime, sub20, Status, Gemini_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "XT", XTLTP, XTAP3, XTAP3V, XTBP3,
                                XTBP3V, processingtime, sub21, Binance_Status, XT_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Bitflyer", BitflyerLTP, BitflyerAP3,
                                BitflyerAP3V, BitflyerBP3, BitflyerBP3V, processingtime, sub22, Status,
                                Bitflyer_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "CoinW", CoinWLTP, CoinWAP3, CoinWAP3V,
                                CoinWBP3, CoinWBP3V, processingtime, sub23, Status, CoinW_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Toobit", ToobitLTP, ToobitAP3,
                                ToobitAP3V, ToobitBP3, ToobitBP3V, processingtime, sub24, Status, Toobit_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP3, AP3V, BP3, BP3V, "Tapbit", TapbitLTP, TapbitAP3,
                                TapbitAP3V, TapbitBP3, TapbitBP3V, processingtime, sub25, Status, TapBit_Status))

            # Wait for all tasks to complete
            for task in tasks:
                task.result()
    buckets_args = [
        (
            "Binance", BinanceLTP, BinanceAP3, BinanceAP3V, BinanceBP3, BinanceBP3V, BinanceBP_BinanceAP,
            BinanceBP_BybitAP,
            BinanceBP_OKXAP, BinanceBP_UpbitAP, BinanceBP_KucoinAP, BinanceBP_BitgetAP, BinanceBP_BitstampAP,
            BinanceBP_GeminiAP, BinanceBP_KrakenAP, BinanceBP_GateioAP, BinanceBP_HTXAP, BinanceBP_MEXCAP,
            BinanceBP_LbankAP, BinanceBP_BitmartAP, BinanceBP_DeepcoinAP, BinanceBP_BitfinexAP, BinanceBP_BingXAP,
            BinanceBP_OrangeXAP, BinanceBP_BitvenusAP, BinanceBP_BiconomyAP, BinanceBP_XTAP, BinanceBP_BitflyerAP,
            BinanceBP_CoinWAP, BinanceBP_ToobitAP, BinanceBP_TapBitAP, Binance_Status),
        ("Bybit", BybitLTP, BybitAP3, BybitAP3V, BybitBP3, BybitBP3V, BybitBP_BinanceAP, BybitBP_BybitAP, BybitBP_OKXAP,
         BybitBP_UpbitAP, BybitBP_KucoinAP, BybitBP_BitgetAP, BybitBP_BitstampAP, BybitBP_GeminiAP, BybitBP_KrakenAP,
         BybitBP_GateioAP, BybitBP_HTXAP, BybitBP_MEXCAP, BybitBP_LbankAP, BybitBP_BitmartAP, BybitBP_DeepcoinAP,
         BybitBP_BitfinexAP, BybitBP_BingXAP, BybitBP_OrangeXAP, BybitBP_BitvenusAP, BybitBP_BiconomyAP, BybitBP_XTAP,
         BybitBP_BitflyerAP, BybitBP_CoinWAP, BybitBP_ToobitAP, BybitBP_TapBitAP, BybitStatus),
        ("OKX", OKXLTP, OKXAP3, OKXAP3V, OKXBP3, OKXBP3V, OKXBP_BinanceAP, OKXBP_BybitAP, OKXBP_OKXAP, OKXBP_UpbitAP,
         OKXBP_KucoinAP, OKXBP_BitgetAP, OKXBP_BitstampAP, OKXBP_GeminiAP, OKXBP_KrakenAP, OKXBP_GateioAP, OKXBP_HTXAP,
         OKXBP_MEXCAP, OKXBP_LbankAP, OKXBP_BitmartAP, OKXBP_DeepcoinAP, OKXBP_BitfinexAP, OKXBP_BingXAP,
         OKXBP_OrangeXAP, OKXBP_BitvenusAP, OKXBP_BiconomyAP, OKXBP_XTAP, OKXBP_BitflyerAP, OKXBP_CoinWAP,
         OKXBP_ToobitAP, OKXBP_TapBitAP, OKX_Status),
        ("Upbit", UpbitLTP, UpbitAP3, UpbitAP3V, UpbitBP3, UpbitBP3V, UpbitBP_BinanceAP, UpbitBP_BybitAP, UpbitBP_OKXAP,
         UpbitBP_UpbitAP, UpbitBP_KucoinAP, UpbitBP_BitgetAP, UpbitBP_BitstampAP, UpbitBP_GeminiAP, UpbitBP_KrakenAP,
         UpbitBP_GateioAP, UpbitBP_HTXAP, UpbitBP_MEXCAP, UpbitBP_LbankAP, UpbitBP_BitmartAP, UpbitBP_DeepcoinAP,
         UpbitBP_BitfinexAP, UpbitBP_BingXAP, UpbitBP_OrangeXAP, UpbitBP_BitvenusAP, UpbitBP_BiconomyAP, UpbitBP_XTAP,
         UpbitBP_BitflyerAP, UpbitBP_CoinWAP, UpbitBP_ToobitAP, UpbitBP_TapBitAP, Upbit_Status),
        ("Kucoin", KucoinLTP, KucoinAP3, KucoinAP3V, KucoinBP3, KucoinBP3V, KucoinBP_BinanceAP, KucoinBP_BybitAP,
         KucoinBP_OKXAP, KucoinBP_UpbitAP, KucoinBP_KucoinAP, KucoinBP_BitgetAP, KucoinBP_BitstampAP, KucoinBP_GeminiAP,
         KucoinBP_KrakenAP, KucoinBP_GateioAP, KucoinBP_HTXAP, KucoinBP_MEXCAP, KucoinBP_LbankAP, KucoinBP_BitmartAP,
         KucoinBP_DeepcoinAP, KucoinBP_BitfinexAP, KucoinBP_BingXAP, KucoinBP_OrangeXAP, KucoinBP_BitvenusAP,
         KucoinBP_BiconomyAP, KucoinBP_XTAP, KucoinBP_BitflyerAP, KucoinBP_CoinWAP, KucoinBP_ToobitAP,
         KucoinBP_TapBitAP, Kucoin_Status),
        ("Bitget", BitgetLTP, BitgetAP3, BitgetAP3V, BitgetBP3, BitgetBP3V, BitgetBP_BinanceAP, BitgetBP_BybitAP,
         BitgetBP_OKXAP, BitgetBP_UpbitAP, BitgetBP_KucoinAP, BitgetBP_BitgetAP, BitgetBP_BitstampAP, BitgetBP_GeminiAP,
         BitgetBP_KrakenAP, BitgetBP_GateioAP, BitgetBP_HTXAP, BitgetBP_MEXCAP, BitgetBP_LbankAP, BitgetBP_BitmartAP,
         BitgetBP_DeepcoinAP, BitgetBP_BitfinexAP, BitgetBP_BingXAP, BitgetBP_OrangeXAP, BitgetBP_BitvenusAP,
         BitgetBP_BiconomyAP, BitgetBP_XTAP, BitgetBP_BitflyerAP, BitgetBP_CoinWAP, BitgetBP_ToobitAP,
         BitgetBP_TapBitAP, Bitget_Status),
        ("Bitstamp", BitstampLTP, BitstampAP3, BitstampAP3V, BitstampBP3, BitstampBP3V, BitstampBP_BinanceAP,
         BitstampBP_BybitAP, BitstampBP_OKXAP, BitstampBP_UpbitAP, BitstampBP_KucoinAP, BitstampBP_BitgetAP,
         BitstampBP_BitstampAP, BitstampBP_GeminiAP, BitstampBP_KrakenAP, BitstampBP_GateioAP, BitstampBP_HTXAP,
         BitstampBP_MEXCAP, BitstampBP_LbankAP, BitstampBP_BitmartAP, BitstampBP_DeepcoinAP, BitstampBP_BitfinexAP,
         BitstampBP_BingXAP, BitstampBP_OrangeXAP, BitstampBP_BitvenusAP, BitstampBP_BiconomyAP, BitstampBP_XTAP,
         BitstampBP_BitflyerAP, BitstampBP_CoinWAP, BitstampBP_ToobitAP, BitstampBP_TapBitAP, Bitstamp_Status),
        ("Kraken", KrakenLTP, KrakenAP3, KrakenAP3V, KrakenBP3, KrakenBP3V, KrakenBP_BinanceAP, KrakenBP_BybitAP,
         KrakenBP_OKXAP, KrakenBP_UpbitAP, KrakenBP_KucoinAP, KrakenBP_BitgetAP, KrakenBP_BitstampAP, KrakenBP_GeminiAP,
         KrakenBP_KrakenAP, KrakenBP_GateioAP, KrakenBP_HTXAP, KrakenBP_MEXCAP, KrakenBP_LbankAP, KrakenBP_BitmartAP,
         KrakenBP_DeepcoinAP, KrakenBP_BitfinexAP, KrakenBP_BingXAP, KrakenBP_OrangeXAP, KrakenBP_BitvenusAP,
         KrakenBP_BiconomyAP, KrakenBP_XTAP, KrakenBP_BitflyerAP, KrakenBP_CoinWAP, KrakenBP_ToobitAP,
         KrakenBP_TapBitAP, Kraken_Status),
        ("Gate.io", GateioLTP, GateioAP3, GateioAP3V, GateioBP3, GateioBP3V, GateioBP_BinanceAP, GateioBP_BybitAP,
         GateioBP_OKXAP, GateioBP_UpbitAP, GateioBP_KucoinAP, GateioBP_BitgetAP, GateioBP_BitstampAP, GateioBP_GeminiAP,
         GateioBP_KrakenAP, GateioBP_GateioAP, GateioBP_HTXAP, GateioBP_MEXCAP, GateioBP_LbankAP, GateioBP_BitmartAP,
         GateioBP_DeepcoinAP, GateioBP_BitfinexAP, GateioBP_BingXAP, GateioBP_OrangeXAP, GateioBP_BitvenusAP,
         GateioBP_BiconomyAP, GateioBP_XTAP, GateioBP_BitflyerAP, GateioBP_CoinWAP, GateioBP_ToobitAP,
         GateioBP_TapBitAP, Gateio_Status),
        ("HTX", HTXLTP, HTXAP3,
         HTXAP3V,
         HTXBP3, HTXBP3V,
         HTXBP_BinanceAP, HTXBP_BybitAP, HTXBP_OKXAP, HTXBP_UpbitAP, HTXBP_KucoinAP,
         HTXBP_BitgetAP, HTXBP_BitstampAP
         , HTXBP_GeminiAP, HTXBP_KrakenAP, HTXBP_GateioAP, HTXBP_HTXAP, HTXBP_MEXCAP,
         HTXBP_LbankAP, HTXBP_BitmartAP
         , HTXBP_DeepcoinAP, HTXBP_BitfinexAP, HTXBP_BingXAP, HTXBP_OrangeXAP, HTXBP_BitvenusAP,
         HTXBP_BiconomyAP,
         HTXBP_XTAP, HTXBP_BitflyerAP, HTXBP_CoinWAP, HTXBP_ToobitAP, HTXBP_TapBitAP, HTX_Status
         ),
        ("MEXC", MEXCLTP,
         MEXCAP3, MEXCAP3V,
         MEXCBP3, MEXCBP3V,
         MEXCBP_BinanceAP, MEXCBP_BybitAP, MEXCBP_OKXAP, MEXCBP_UpbitAP, MEXCBP_KucoinAP,
         MEXCBP_BitgetAP, MEXCBP_BitstampAP
         , MEXCBP_GeminiAP, MEXCBP_KrakenAP, MEXCBP_GateioAP, MEXCBP_HTXAP, MEXCBP_MEXCAP,
         MEXCBP_LbankAP, MEXCBP_BitmartAP
         , MEXCBP_DeepcoinAP, MEXCBP_BitfinexAP, MEXCBP_BingXAP, MEXCBP_OrangeXAP, MEXCBP_BitvenusAP,
         MEXCBP_BiconomyAP,
         MEXCBP_XTAP, MEXCBP_BitflyerAP, MEXCBP_CoinWAP, MEXCBP_ToobitAP, MEXCBP_TapBitAP, MEXC_Status
         ),
        ("Lbank", LbankLTP,
         LbankAP3, LbankAP3V,
         LbankBP3, LbankBP3V,
         LbankBP_BinanceAP, LbankBP_BybitAP, LbankBP_OKXAP, LbankBP_UpbitAP, LbankBP_KucoinAP,
         LbankBP_BitgetAP, LbankBP_BitstampAP
         , LbankBP_GeminiAP, LbankBP_KrakenAP, LbankBP_GateioAP, LbankBP_HTXAP, LbankBP_MEXCAP,
         LbankBP_LbankAP, LbankBP_BitmartAP
         , LbankBP_DeepcoinAP, LbankBP_BitfinexAP, LbankBP_BingXAP, LbankBP_OrangeXAP, LbankBP_BitvenusAP,
         LbankBP_BiconomyAP,
         LbankBP_XTAP, LbankBP_BitflyerAP, LbankBP_CoinWAP, LbankBP_ToobitAP, LbankBP_TapBitAP, Lbank_Status
         ),
        ("Bitmart",
         BitmartLTP, BitmartAP3, BitmartAP3V,
         BitmartBP3, BitmartBP3V,
         BitmartBP_BinanceAP, BitmartBP_BybitAP, BitmartBP_OKXAP, BitmartBP_UpbitAP, BitmartBP_KucoinAP,
         BitmartBP_BitgetAP, BitmartBP_BitstampAP
         , BitmartBP_GeminiAP, BitmartBP_KrakenAP, BitmartBP_GateioAP, BitmartBP_HTXAP, BitmartBP_MEXCAP,
         BitmartBP_LbankAP, BitmartBP_BitmartAP
         , BitmartBP_DeepcoinAP, BitmartBP_BitfinexAP, BitmartBP_BingXAP, BitmartBP_OrangeXAP, BitmartBP_BitvenusAP,
         BitmartBP_BiconomyAP,
         BitmartBP_XTAP, BitmartBP_BitflyerAP, BitmartBP_CoinWAP, BitmartBP_ToobitAP, BitmartBP_TapBitAP, Bitmart_Status
         ),
        ("Deepcoin",
         DeepcoinLTP,
         DeepcoinAP3, DeepcoinAP3V, DeepcoinBP3, DeepcoinBP3V,
         DeepcoinBP_BinanceAP, DeepcoinBP_BybitAP, DeepcoinBP_OKXAP, DeepcoinBP_UpbitAP, DeepcoinBP_KucoinAP,
         DeepcoinBP_BitgetAP, DeepcoinBP_BitstampAP
         , DeepcoinBP_GeminiAP, DeepcoinBP_KrakenAP, DeepcoinBP_GateioAP, DeepcoinBP_HTXAP, DeepcoinBP_MEXCAP,
         DeepcoinBP_LbankAP, DeepcoinBP_BitmartAP
         , DeepcoinBP_DeepcoinAP, DeepcoinBP_BitfinexAP, DeepcoinBP_BingXAP, DeepcoinBP_OrangeXAP,
         DeepcoinBP_BitvenusAP,
         DeepcoinBP_BiconomyAP,
         DeepcoinBP_XTAP, DeepcoinBP_BitflyerAP, DeepcoinBP_CoinWAP, DeepcoinBP_ToobitAP, DeepcoinBP_TapBitAP,
         Deepcoin_Status
         ),
        ("Bitfinex",
         BitfinexLTP, BitfinexAP3, BitfinexAP3V,
         BitfinexBP3, BitfinexBP3V,
         BitfinexBP_BinanceAP, BitfinexBP_BybitAP, BitfinexBP_OKXAP, BitfinexBP_UpbitAP, BitfinexBP_KucoinAP,
         BitfinexBP_BitgetAP, BitfinexBP_BitstampAP
         , BitfinexBP_GeminiAP, BitfinexBP_KrakenAP, BitfinexBP_GateioAP, BitfinexBP_HTXAP, BitfinexBP_MEXCAP,
         BitfinexBP_LbankAP, BitfinexBP_BitmartAP
         , BitfinexBP_DeepcoinAP, BitfinexBP_BitfinexAP, BitfinexBP_BingXAP, BitfinexBP_OrangeXAP,
         BitfinexBP_BitvenusAP,
         BitfinexBP_BiconomyAP,
         BitfinexBP_XTAP, BitfinexBP_BitflyerAP, BitfinexBP_CoinWAP, BitfinexBP_ToobitAP, BitfinexBP_TapBitAP,
         Bitfinex_Status
         ),
        ("BingX", BingXLTP,
         BingXAP3, BingXAP3V,
         BingXBP3, BingXBP3V,
         BingXBP_BinanceAP, BingXBP_BybitAP, BingXBP_OKXAP, BingXBP_UpbitAP, BingXBP_KucoinAP,
         BingXBP_BitgetAP, BingXBP_BitstampAP
         , BingXBP_GeminiAP, BingXBP_KrakenAP, BingXBP_GateioAP, BingXBP_HTXAP, BingXBP_MEXCAP,
         BingXBP_LbankAP, BingXBP_BitmartAP
         , BingXBP_DeepcoinAP, BingXBP_BitfinexAP, BingXBP_BingXAP, BingXBP_OrangeXAP, BingXBP_BitvenusAP,
         BingXBP_BiconomyAP,
         BingXBP_XTAP, BingXBP_BitflyerAP, BingXBP_CoinWAP, BingXBP_ToobitAP, BingXBP_TapBitAP, BingX_Status
         ),
        ("OrangeX",
         OrangeXLTP, OrangeXAP3, OrangeXAP3V,
         OrangeXBP3, OrangeXBP3V,
         OrangeXBP_BinanceAP, OrangeXBP_BybitAP, OrangeXBP_OKXAP, OrangeXBP_UpbitAP, OrangeXBP_KucoinAP,
         OrangeXBP_BitgetAP, OrangeXBP_BitstampAP
         , OrangeXBP_GeminiAP, OrangeXBP_KrakenAP, OrangeXBP_GateioAP, OrangeXBP_HTXAP, OrangeXBP_MEXCAP,
         OrangeXBP_LbankAP, OrangeXBP_BitmartAP
         , OrangeXBP_DeepcoinAP, OrangeXBP_BitfinexAP, OrangeXBP_BingXAP, OrangeXBP_OrangeXAP, OrangeXBP_BitvenusAP,
         OrangeXBP_BiconomyAP,
         OrangeXBP_XTAP, OrangeXBP_BitflyerAP, OrangeXBP_CoinWAP, OrangeXBP_ToobitAP, OrangeXBP_TapBitAP, OrangeX_Status
         ),
        ("Bitvenus",
         BitvenusLTP, BitvenusAP3, BitvenusAP3V,
         BitvenusBP3, BitvenusBP3V,
         BitvenusBP_BinanceAP, BitvenusBP_BybitAP, BitvenusBP_OKXAP, BitvenusBP_UpbitAP, BitvenusBP_KucoinAP,
         BitvenusBP_BitgetAP, BitvenusBP_BitstampAP
         , BitvenusBP_GeminiAP, BitvenusBP_KrakenAP, BitvenusBP_GateioAP, BitvenusBP_HTXAP, BitvenusBP_MEXCAP,
         BitvenusBP_LbankAP, BitvenusBP_BitmartAP
         , BitvenusBP_DeepcoinAP, BitvenusBP_BitfinexAP, BitvenusBP_BingXAP, BitvenusBP_OrangeXAP,
         BitvenusBP_BitvenusAP,
         BitvenusBP_BiconomyAP,
         BitvenusBP_XTAP, BitvenusBP_BitflyerAP, BitvenusBP_CoinWAP, BitvenusBP_ToobitAP, BitvenusBP_TapBitAP,
         Bitvenus_Status
         ),
        ("Biconomy",
         BiconomyLTP, BiconomyAP3, BiconomyAP3V,
         BiconomyBP3, BiconomyBP3V,
         BiconomyBP_BinanceAP, BiconomyBP_BybitAP, BiconomyBP_OKXAP, BiconomyBP_UpbitAP, BiconomyBP_KucoinAP,
         BiconomyBP_BitgetAP, BiconomyBP_BitstampAP
         , BiconomyBP_GeminiAP, BiconomyBP_KrakenAP, BiconomyBP_GateioAP, BiconomyBP_HTXAP, BiconomyBP_MEXCAP,
         BiconomyBP_LbankAP, BiconomyBP_BitmartAP
         , BiconomyBP_DeepcoinAP, BiconomyBP_BitfinexAP, BiconomyBP_BingXAP, BiconomyBP_OrangeXAP,
         BiconomyBP_BitvenusAP,
         BiconomyBP_BiconomyAP,
         BiconomyBP_XTAP, BiconomyBP_BitflyerAP, BiconomyBP_CoinWAP, BiconomyBP_ToobitAP, BiconomyBP_TapBitAP,
         Biconomy_Status
         ),
        ("Gemini", GeminiLTP,
         GeminiAP3, GeminiAP3V,
         GeminiBP3, GeminiBP3V,
         GeminiBP_BinanceAP, GeminiBP_BybitAP, GeminiBP_OKXAP, GeminiBP_UpbitAP, GeminiBP_KucoinAP,
         GeminiBP_BitgetAP, GeminiBP_BitstampAP
         , GeminiBP_GeminiAP, GeminiBP_KrakenAP, GeminiBP_GateioAP, GeminiBP_HTXAP, GeminiBP_MEXCAP,
         GeminiBP_LbankAP, GeminiBP_BitmartAP
         , GeminiBP_DeepcoinAP, GeminiBP_BitfinexAP, GeminiBP_BingXAP, GeminiBP_OrangeXAP, GeminiBP_BitvenusAP,
         GeminiBP_BiconomyAP,
         GeminiBP_XTAP, GeminiBP_BitflyerAP, GeminiBP_CoinWAP, GeminiBP_ToobitAP, GeminiBP_TapBitAP, Gemini_Status
         ),
        ("XT", XTLTP, XTAP3,
         XTAP3V,
         XTBP3, XTBP3V,
         XTBP_BinanceAP, XTBP_BybitAP, XTBP_OKXAP, XTBP_UpbitAP, XTBP_KucoinAP,
         XTBP_BitgetAP, XTBP_BitstampAP
         , XTBP_GeminiAP, XTBP_KrakenAP, XTBP_GateioAP, XTBP_HTXAP, XTBP_MEXCAP,
         XTBP_LbankAP, XTBP_BitmartAP
         , XTBP_DeepcoinAP, XTBP_BitfinexAP, XTBP_BingXAP, XTBP_OrangeXAP, XTBP_BitvenusAP,
         XTBP_BiconomyAP,
         XTBP_XTAP, XTBP_BitflyerAP, XTBP_CoinWAP, XTBP_ToobitAP, XTBP_TapBitAP, XT_Status
         ),
        ("Bitflyer", BitflyerLTP,
         BitflyerAP3, BitflyerAP3V,
         BitflyerBP3, BitflyerBP3V,
         BitflyerBP_BinanceAP, BitflyerBP_BybitAP, BitflyerBP_OKXAP, BitflyerBP_UpbitAP, BitflyerBP_KucoinAP,
         BitflyerBP_BitgetAP, BitflyerBP_BitstampAP
         , BitflyerBP_GeminiAP, BitflyerBP_KrakenAP, BitflyerBP_GateioAP, BitflyerBP_HTXAP, BitflyerBP_MEXCAP,
         BitflyerBP_LbankAP, BitflyerBP_BitmartAP
         , BitflyerBP_DeepcoinAP, BitflyerBP_BitfinexAP, BitflyerBP_BingXAP, BitflyerBP_OrangeXAP,
         BitflyerBP_BitvenusAP,
         BitflyerBP_BiconomyAP,
         BitflyerBP_XTAP, BitflyerBP_BitflyerAP, BitflyerBP_CoinWAP, BitflyerBP_ToobitAP, BitflyerBP_TapBitAP,
         Bitflyer_Status
         ),
        ("CoinW", CoinWLTP,
         CoinWAP3, CoinWAP3V,
         CoinWBP3, CoinWBP3V,
         CoinWBP_BinanceAP, CoinWBP_BybitAP, CoinWBP_OKXAP, CoinWBP_UpbitAP, CoinWBP_KucoinAP,
         CoinWBP_BitgetAP, CoinWBP_BitstampAP
         , CoinWBP_GeminiAP, CoinWBP_KrakenAP, CoinWBP_GateioAP, CoinWBP_HTXAP, CoinWBP_MEXCAP,
         CoinWBP_LbankAP, CoinWBP_BitmartAP
         , CoinWBP_DeepcoinAP, CoinWBP_BitfinexAP, CoinWBP_BingXAP, CoinWBP_OrangeXAP, CoinWBP_BitvenusAP,
         CoinWBP_BiconomyAP,
         CoinWBP_XTAP, CoinWBP_BitflyerAP, CoinWBP_CoinWAP, CoinWBP_ToobitAP, CoinWBP_TapBitAP, CoinW_Status
         ),
        ("Toobit", ToobitLTP,
         ToobitAP3, ToobitAP3V,
         ToobitBP3, ToobitBP3V,
         ToobitBP_BinanceAP, ToobitBP_BybitAP, ToobitBP_OKXAP, ToobitBP_UpbitAP, ToobitBP_KucoinAP,
         ToobitBP_BitgetAP, ToobitBP_BitstampAP
         , ToobitBP_GeminiAP, ToobitBP_KrakenAP, ToobitBP_GateioAP, ToobitBP_HTXAP, ToobitBP_MEXCAP,
         ToobitBP_LbankAP, ToobitBP_BitmartAP
         , ToobitBP_DeepcoinAP, ToobitBP_BitfinexAP, ToobitBP_BingXAP, ToobitBP_OrangeXAP, ToobitBP_BitvenusAP,
         ToobitBP_BiconomyAP,
         ToobitBP_XTAP, ToobitBP_BitflyerAP, ToobitBP_CoinWAP, ToobitBP_ToobitAP, ToobitBP_TapBitAP, Toobit_Status
         ),
        ("Tapbit", TapbitLTP,
         TapbitAP3, TapbitAP3V,
         TapbitBP3, TapbitBP3V,
         TapBitBP_BinanceAP, TapBitBP_BybitAP, TapBitBP_OKXAP, TapBitBP_UpbitAP, TapBitBP_KucoinAP,
         TapBitBP_BitgetAP, TapBitBP_BitstampAP
         , TapBitBP_GeminiAP, TapBitBP_KrakenAP, TapBitBP_GateioAP, TapBitBP_HTXAP, TapBitBP_MEXCAP,
         TapBitBP_LbankAP, TapBitBP_BitmartAP
         , TapBitBP_DeepcoinAP, TapBitBP_BitfinexAP, TapBitBP_BingXAP, TapBitBP_OrangeXAP, TapBitBP_BitvenusAP,
         TapBitBP_BiconomyAP,
         TapBitBP_XTAP, TapBitBP_BitflyerAP, TapBitBP_CoinWAP, TapBitBP_ToobitAP, TapBitBP_TapBitAP, TapBit_Status
         )

        # Add other exchanges similarly
    ]

    # Create a list to hold the threads
    threads = []

    # Create and start a thread for each PriceDifference function call
    for args in buckets_args:
        thread = threading.Thread(target=Buckets, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



async def Bid_Ask4(results,inital_time):
    start = time.perf_counter_ns()



    # Binance
    BinanceBP4 = results["BinanceBP4"]
    BinanceBP4V = results["BinanceBP4V"]
    BinanceAP4 = results["BinanceAP4"]
    BinanceAP4V = results["BinanceAP4V"]
    BinanceOBT = results["BinanceOBT"]
    BinanceLTP = results["BinanceLTP"]

    # Bybit
    BybitBP4 = results["BybitBP4"]
    BybitBP4V = results["BybitBP4V"]
    BybitAP4 = results["BybitAP4"]
    BybitAP4V = results["BybitAP4V"]
    BybitOBT = results["BybitOBT"]
    BybitLTP = results["BybitLTP"]

    # OKX
    OKXBP4 = results["OKXBP4"]
    OKXBP4V = results["OKXBP4V"]
    OKXAP4 = results["OKXAP4"]
    OKXAP4V = results["OKXAP4V"]
    OKXOBT = results["OKXOBT"]
    OKXLTP = results["OKXLTP"]

    # Upbit
    UpbitBP4 = results["UpbitBP4"]
    UpbitBP4V = results["UpbitBP4V"]
    UpbitAP4 = results["UpbitAP4"]
    UpbitAP4V = results["UpbitAP4V"]
    UpbitOBT = results["UpbitOBT"]
    UpbitLTP = results["UpbitLTP"]

    # Kucoin
    KucoinBP4 = results["KucoinBP4"]
    KucoinBP4V = results["KucoinBP4V"]
    KucoinAP4 = results["KucoinAP4"]
    KucoinAP4V = results["KucoinAP4V"]
    KucoinOBT = results["KucoinOBT"]
    KucoinLTP = results["KucoinLTP"]

    # Bitget
    BitgetBP4 = results["BitgetBP4"]
    BitgetBP4V = results["BitgetBP4V"]
    BitgetAP4 = results["BitgetAP4"]
    BitgetAP4V = results["BitgetAP4V"]
    BitgetOBT = results["BitgetOBT"]
    BitgetLTP = results["BitgetLTP"]

    # Bitstamp
    BitstampBP4 = results["BitstampBP4"]
    BitstampBP4V = results["BitstampBP4V"]
    BitstampAP4 = results["BitstampAP4"]
    BitstampAP4V = results["BitstampAP4V"]
    BitstampOBT = results["BitstampOBT"]
    BitstampLTP = results["BitstampLTP"]

    # Gemini
    GeminiBP4 = results["GeminiBP4"]
    GeminiBP4V = results["GeminiBP4V"]
    GeminiAP4 = results["GeminiAP4"]
    GeminiAP4V = results["GeminiAP4V"]
    GeminiOBT = results["GeminiOBT"]
    GeminiLTP = results["GeminiLTP"]

    # Kraken
    KrakenBP4 = results["KrakenBP4"]
    KrakenBP4V = results["KrakenBP4V"]
    KrakenAP4 = results["KrakenAP4"]
    KrakenAP4V = results["KrakenAP4V"]
    KrakenOBT = results["KrakenOBT"]
    KrakenLTP = results["KrakenLTP"]

    # Gateio
    GateioBP4 = results["GateioBP4"]
    GateioBP4V = results["GateioBP4V"]
    GateioAP4 = results["GateioAP4"]
    GateioAP4V = results["GateioAP4V"]
    GateioOBT = results["GateioOBT"]
    GateioLTP = results["GateioLTP"]

    # HTX
    HTXBP4 = results["HTXBP4"]
    HTXBP4V = results["HTXBP4V"]
    HTXAP4 = results["HTXAP4"]
    HTXAP4V = results["HTXAP4V"]
    HTXOBT = results["HTXOBT"]
    HTXLTP = results["HTXLTP"]

    # MEXC
    MEXCBP4 = results["MEXCBP4"]
    MEXCBP4V = results["MEXCBP4V"]
    MEXCAP4 = results["MEXCAP4"]
    MEXCAP4V = results["MEXCAP4V"]
    MEXCOBT = results["MEXCOBT"]
    MEXCLTP = results["MEXCLTP"]

    # Lbank
    LbankBP4 = results["LbankBP4"]
    LbankBP4V = results["LbankBP4V"]
    LbankAP4 = results["LbankAP4"]
    LbankAP4V = results["LbankAP4V"]
    LbankOBT = results["LbankOBT"]
    LbankLTP = results["LbankLTP"]

    # Bitmart
    BitmartBP4 = results["BitmartBP4"]
    BitmartBP4V = results["BitmartBP4V"]
    BitmartAP4 = results["BitmartAP4"]
    BitmartAP4V = results["BitmartAP4V"]
    BitmartOBT = results["BitmartOBT"]
    BitmartLTP = results["BitmartLTP"]

    # Deepcoin
    DeepcoinBP4 = results["DeepcoinBP4"]
    DeepcoinBP4V = results["DeepcoinBP4V"]
    DeepcoinAP4 = results["DeepcoinAP4"]
    DeepcoinAP4V = results["DeepcoinAP4V"]
    DeepcoinOBT = results["DeepcoinOBT"]
    DeepcoinLTP = results["DeepcoinLTP"]

    # Bitfinex
    BitfinexBP4 = results["BitfinexBP4"]
    BitfinexBP4V = results["BitfinexBP4V"]
    BitfinexAP4 = results["BitfinexAP4"]
    BitfinexAP4V = results["BitfinexAP4V"]
    BitfinexOBT = results["BitfinexOBT"]
    BitfinexLTP = results["BitfinexLTP"]

    # BingX
    BingXBP4 = results["BingXBP4"]
    BingXBP4V = results["BingXBP4V"]
    BingXAP4 = results["BingXAP4"]
    BingXAP4V = results["BingXAP4V"]
    BingXOBT = results["BingXOBT"]
    BingXLTP = results["BingXLTP"]

    # OrangeX
    OrangeXBP4 = results["OrangeXBP4"]
    OrangeXBP4V = results["OrangeXBP4V"]
    OrangeXAP4 = results["OrangeXAP4"]
    OrangeXAP4V = results["OrangeXAP4V"]
    OrangeXOBT = results["OrangeXOBT"]
    OrangeXLTP = results["OrangeXLTP"]

    # Bitvenus
    BitvenusBP4 = results["BitvenusBP4"]
    BitvenusBP4V = results["BitvenusBP4V"]
    BitvenusAP4 = results["BitvenusAP4"]
    BitvenusAP4V = results["BitvenusAP4V"]
    BitvenusOBT = results["BitvenusOBT"]
    BitvenusLTP = results["BitvenusLTP"]

    # Biconomy
    BiconomyBP4 = results["BiconomyBP4"]
    BiconomyBP4V = results["BiconomyBP4V"]
    BiconomyAP4 = results["BiconomyAP4"]
    BiconomyAP4V = results["BiconomyAP4V"]
    BiconomyOBT = results["BiconomyOBT"]
    BiconomyLTP = results["BiconomyLTP"]

    # XT
    XTBP4 = results["XTBP4"]
    XTBP4V = results["XTBP4V"]
    XTAP4 = results["XTAP4"]
    XTAP4V = results["XTAP4V"]
    XTOBT = results["XTOBT"]
    XTLTP = results["XTLTP"]

    # Bitflyer
    BitflyerBP4 = results["BitflyerBP4"]
    BitflyerBP4V = results["BitflyerBP4V"]
    BitflyerAP4 = results["BitflyerAP4"]
    BitflyerAP4V = results["BitflyerAP4V"]
    BitflyerOBT = results["BitflyerOBT"]
    BitflyerLTP = results["BitflyerLTP"]

    # CoinW
    CoinWBP4 = results["CoinWBP4"]
    CoinWBP4V = results["CoinWBP4V"]
    CoinWAP4 = results["CoinWAP4"]
    CoinWAP4V = results["CoinWAP4V"]
    CoinWOBT = results["CoinWOBT"]
    CoinWLTP = results["CoinWLTP"]

    # Toobit
    ToobitBP4 = results["ToobitBP4"]
    ToobitBP4V = results["ToobitBP4V"]
    ToobitAP4 = results["ToobitAP4"]
    ToobitAP4V = results["ToobitAP4V"]
    ToobitOBT = results["ToobitOBT"]
    ToobitLTP = results["ToobitLTP"]

    # TapBit
    TapbitBP4 = results["TapBitBP4"]
    TapbitBP4V = results["TapBitBP4V"]
    TapbitAP4 = results["TapBitAP4"]
    TapbitAP4V = results["TapBitAP4V"]
    TapbitOBT = results["TapBitOBT"]
    TapbitLTP = results["TapBitLTP"]

    Binance_Status = results['Binance_Status']
    BybitStatus = results['Bybit_Status']
    OKX_Status = results['OKX_Status']
    Upbit_Status = results['Upbit_Status']
    Kucoin_Status = results['Kucoin_Status']
    Bitget_Status = results['Bitget_Status']
    Bitstamp_Status = results['Bitstamp_Status']
    Gemini_Status = results['Gemini_Status']
    Kraken_Status = results['Kraken_Status']
    Gateio_Status = results['Gateio_Status']
    HTX_Status = results['HTX_Status']
    MEXC_Status = results['MEXC_Status']
    Lbank_Status = results['Lbank_Status']
    Bitmart_Status = results['Bitmart_Status']
    Deepcoin_Status = results['Deepcoin_Status']
    Bitfinex_Status = results['Bitfinex_Status']
    BingX_Status = results['BingX_Status']
    OrangeX_Status = results['OrangeX_Status']
    Bitvenus_Status = results['Bitvenus_Status']
    Biconomy_Status = results['Biconomy_Status']
    XT_Status = results['XT_Status']
    Bitflyer_Status = results['Bitflyer_Status']
    CoinW_Status = results['CoinW_Status']
    Toobit_Status = results['Toobit_Status']
    TapBit_Status = results['TapBit_Status']

    bid_prices = {
        "Binance": BinanceBP4,
        "Bybit": BybitBP4,
        "OKX": OKXBP4,
        "Upbit": UpbitBP4,
        "Kucoin": KucoinBP4,
        "Bitget": BitgetBP4,
        "Bitstamp": BitstampBP4,
        "Gemini": GeminiBP4,
        "Kraken": KrakenBP4,
        "Gate.io": GateioBP4,
        "HTX": HTXBP4,
        "MEXC": MEXCBP4,
        "Lbank": LbankBP4,
        "Bitmart": BitmartBP4,
        "Deepcoin": DeepcoinBP4,
        "Bitfinex": BitfinexBP4,
        "BingX": BingXBP4,
        "OrangeX": OrangeXBP4,
        "Bitvenus": BitvenusBP4,
        "Biconomy": BiconomyBP4,
        "XT": XTBP4,
        "Bitflyer": BitflyerBP4,
        "CoinW": CoinWBP4,
        "Toobit": ToobitBP4,
        "TapBit": TapbitBP4
    }

    ask_prices = {
        "Binance": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bybit": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "OKX": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Upbit": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Kucoin": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitget": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitstamp": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Gemini": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Kraken": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Gate.io": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "HTX": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "MEXC": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Lbank": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitmart": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Deepcoin": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitfinex": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "BingX": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "OrangeX": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitvenus": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Biconomy": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "XT": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Bitflyer": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "CoinW": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "Toobit": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        },
        "TapBit": {
            "Binance": BinanceAP4,
            "Bybit": BybitAP4,
            "OKX": OKXAP4,
            "Upbit": UpbitAP4,
            "Kucoin": KucoinAP4,
            "Bitget": BitgetAP4,
            "Bitstamp": BitstampAP4,
            "Gemini": GeminiAP4,
            "Kraken": KrakenAP4,
            "Gate.io": GateioAP4,
            "HTX": HTXAP4,
            "MEXC": MEXCAP4,
            "Lbank": LbankAP4,
            "Bitmart": BitmartAP4,
            "Deepcoin": DeepcoinAP4,
            "Bitfinex": BitfinexAP4,
            "BingX": BingXAP4,
            "OrangeX": OrangeXAP4,
            "Bitvenus": BitvenusAP4,
            "Biconomy": BiconomyAP4,
            "XT": XTAP4,
            "Bitflyer": BitflyerAP4,
            "CoinW": CoinWAP4,
            "Toobit": ToobitAP4,
            "TapBit": TapbitAP4
        }
    }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect differences from all exchanges
    all_differences = {}
    for exchange in exchanges:
        all_differences.update(exchange.get_differences())

    results = {}
    for key, value in all_differences.items():
        results[key] = value

    # Print stored variables
    for key in sorted(results.keys()):
        results[key]

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_Gate.ioAP']
    BinanceBP_HTXAP = results['BinanceBP_HTXAP']
    BinanceBP_MEXCAP = results['BinanceBP_MEXCAP']
    BinanceBP_LbankAP = results['BinanceBP_LbankAP']
    BinanceBP_BitmartAP = results['BinanceBP_BitmartAP']
    BinanceBP_DeepcoinAP = results['BinanceBP_DeepcoinAP']
    BinanceBP_BitfinexAP = results['BinanceBP_BitfinexAP']
    BinanceBP_BingXAP = results['BinanceBP_BingXAP']
    BinanceBP_OrangeXAP = results['BinanceBP_OrangeXAP']
    BinanceBP_BitvenusAP = results['BinanceBP_BitvenusAP']
    BinanceBP_BiconomyAP = results['BinanceBP_BiconomyAP']
    BinanceBP_XTAP = results['BinanceBP_XTAP']
    BinanceBP_BitflyerAP = results['BinanceBP_BitflyerAP']
    BinanceBP_CoinWAP = results['BinanceBP_CoinWAP']
    BinanceBP_ToobitAP = results['BinanceBP_ToobitAP']
    BinanceBP_TapBitAP = results['BinanceBP_TapBitAP']

    BybitBP_BinanceAP = results['BybitBP_BinanceAP']
    BybitBP_BybitAP = results['BybitBP_BybitAP']
    BybitBP_OKXAP = results['BybitBP_OKXAP']
    BybitBP_UpbitAP = results['BybitBP_UpbitAP']
    BybitBP_KucoinAP = results['BybitBP_KucoinAP']
    BybitBP_BitgetAP = results['BybitBP_BitgetAP']
    BybitBP_BitstampAP = results['BybitBP_BitstampAP']
    BybitBP_GeminiAP = results['BybitBP_GeminiAP']
    BybitBP_KrakenAP = results['BybitBP_KrakenAP']
    BybitBP_GateioAP = results['BybitBP_Gate.ioAP']
    BybitBP_HTXAP = results['BybitBP_HTXAP']
    BybitBP_MEXCAP = results['BybitBP_MEXCAP']
    BybitBP_LbankAP = results['BybitBP_LbankAP']
    BybitBP_BitmartAP = results['BybitBP_BitmartAP']
    BybitBP_DeepcoinAP = results['BybitBP_DeepcoinAP']
    BybitBP_BitfinexAP = results['BybitBP_BitfinexAP']
    BybitBP_BingXAP = results['BybitBP_BingXAP']
    BybitBP_OrangeXAP = results['BybitBP_OrangeXAP']
    BybitBP_BitvenusAP = results['BybitBP_BitvenusAP']
    BybitBP_BiconomyAP = results['BybitBP_BiconomyAP']
    BybitBP_XTAP = results['BybitBP_XTAP']
    BybitBP_BitflyerAP = results['BybitBP_BitflyerAP']
    BybitBP_CoinWAP = results['BybitBP_CoinWAP']
    BybitBP_ToobitAP = results['BybitBP_ToobitAP']
    BybitBP_TapBitAP = results['BybitBP_TapBitAP']

    OKXBP_BinanceAP = results['OKXBP_BinanceAP']
    OKXBP_BybitAP = results['OKXBP_BybitAP']
    OKXBP_OKXAP = results['OKXBP_OKXAP']
    OKXBP_UpbitAP = results['OKXBP_UpbitAP']
    OKXBP_KucoinAP = results['OKXBP_KucoinAP']
    OKXBP_BitgetAP = results['OKXBP_BitgetAP']
    OKXBP_BitstampAP = results['OKXBP_BitstampAP']
    OKXBP_GeminiAP = results['OKXBP_GeminiAP']
    OKXBP_KrakenAP = results['OKXBP_KrakenAP']
    OKXBP_GateioAP = results['OKXBP_Gate.ioAP']
    OKXBP_HTXAP = results['OKXBP_HTXAP']
    OKXBP_MEXCAP = results['OKXBP_MEXCAP']
    OKXBP_LbankAP = results['OKXBP_LbankAP']
    OKXBP_BitmartAP = results['OKXBP_BitmartAP']
    OKXBP_DeepcoinAP = results['OKXBP_DeepcoinAP']
    OKXBP_BitfinexAP = results['OKXBP_BitfinexAP']
    OKXBP_BingXAP = results['OKXBP_BingXAP']
    OKXBP_OrangeXAP = results['OKXBP_OrangeXAP']
    OKXBP_BitvenusAP = results['OKXBP_BitvenusAP']
    OKXBP_BiconomyAP = results['OKXBP_BiconomyAP']
    OKXBP_XTAP = results['OKXBP_XTAP']
    OKXBP_BitflyerAP = results['OKXBP_BitflyerAP']
    OKXBP_CoinWAP = results['OKXBP_CoinWAP']
    OKXBP_ToobitAP = results['OKXBP_ToobitAP']
    OKXBP_TapBitAP = results['OKXBP_TapBitAP']

    UpbitBP_BinanceAP = results['UpbitBP_BinanceAP']
    UpbitBP_BybitAP = results['UpbitBP_BybitAP']
    UpbitBP_OKXAP = results['UpbitBP_OKXAP']
    UpbitBP_UpbitAP = results['UpbitBP_UpbitAP']
    UpbitBP_KucoinAP = results['UpbitBP_KucoinAP']
    UpbitBP_BitgetAP = results['UpbitBP_BitgetAP']
    UpbitBP_BitstampAP = results['UpbitBP_BitstampAP']
    UpbitBP_GeminiAP = results['UpbitBP_GeminiAP']
    UpbitBP_KrakenAP = results['UpbitBP_KrakenAP']
    UpbitBP_GateioAP = results['UpbitBP_Gate.ioAP']
    UpbitBP_HTXAP = results['UpbitBP_HTXAP']
    UpbitBP_MEXCAP = results['UpbitBP_MEXCAP']
    UpbitBP_LbankAP = results['UpbitBP_LbankAP']
    UpbitBP_BitmartAP = results['UpbitBP_BitmartAP']
    UpbitBP_DeepcoinAP = results['UpbitBP_DeepcoinAP']
    UpbitBP_BitfinexAP = results['UpbitBP_BitfinexAP']
    UpbitBP_BingXAP = results['UpbitBP_BingXAP']
    UpbitBP_OrangeXAP = results['UpbitBP_OrangeXAP']
    UpbitBP_BitvenusAP = results['UpbitBP_BitvenusAP']
    UpbitBP_BiconomyAP = results['UpbitBP_BiconomyAP']
    UpbitBP_XTAP = results['UpbitBP_XTAP']
    UpbitBP_BitflyerAP = results['UpbitBP_BitflyerAP']
    UpbitBP_CoinWAP = results['UpbitBP_CoinWAP']
    UpbitBP_ToobitAP = results['UpbitBP_ToobitAP']
    UpbitBP_TapBitAP = results['UpbitBP_TapBitAP']

    KucoinBP_BinanceAP = results['KucoinBP_BinanceAP']
    KucoinBP_BybitAP = results['KucoinBP_BybitAP']
    KucoinBP_OKXAP = results['KucoinBP_OKXAP']
    KucoinBP_UpbitAP = results['KucoinBP_UpbitAP']
    KucoinBP_KucoinAP = results['KucoinBP_KucoinAP']
    KucoinBP_BitgetAP = results['KucoinBP_BitgetAP']
    KucoinBP_BitstampAP = results['KucoinBP_BitstampAP']
    KucoinBP_GeminiAP = results['KucoinBP_GeminiAP']
    KucoinBP_KrakenAP = results['KucoinBP_KrakenAP']
    KucoinBP_GateioAP = results['KucoinBP_Gate.ioAP']
    KucoinBP_HTXAP = results['KucoinBP_HTXAP']
    KucoinBP_MEXCAP = results['KucoinBP_MEXCAP']
    KucoinBP_LbankAP = results['KucoinBP_LbankAP']
    KucoinBP_BitmartAP = results['KucoinBP_BitmartAP']
    KucoinBP_DeepcoinAP = results['KucoinBP_DeepcoinAP']
    KucoinBP_BitfinexAP = results['KucoinBP_BitfinexAP']
    KucoinBP_BingXAP = results['KucoinBP_BingXAP']
    KucoinBP_OrangeXAP = results['KucoinBP_OrangeXAP']
    KucoinBP_BitvenusAP = results['KucoinBP_BitvenusAP']
    KucoinBP_BiconomyAP = results['KucoinBP_BiconomyAP']
    KucoinBP_XTAP = results['KucoinBP_XTAP']
    KucoinBP_BitflyerAP = results['KucoinBP_BitflyerAP']
    KucoinBP_CoinWAP = results['KucoinBP_CoinWAP']
    KucoinBP_ToobitAP = results['KucoinBP_ToobitAP']
    KucoinBP_TapBitAP = results['KucoinBP_TapBitAP']

    BitgetBP_BinanceAP = results['BitgetBP_BinanceAP']
    BitgetBP_BybitAP = results['BitgetBP_BybitAP']
    BitgetBP_OKXAP = results['BitgetBP_OKXAP']
    BitgetBP_UpbitAP = results['BitgetBP_UpbitAP']
    BitgetBP_KucoinAP = results['BitgetBP_KucoinAP']
    BitgetBP_BitgetAP = results['BitgetBP_BitgetAP']
    BitgetBP_BitstampAP = results['BitgetBP_BitstampAP']
    BitgetBP_GeminiAP = results['BitgetBP_GeminiAP']
    BitgetBP_KrakenAP = results['BitgetBP_KrakenAP']
    BitgetBP_GateioAP = results['BitgetBP_Gate.ioAP']
    BitgetBP_HTXAP = results['BitgetBP_HTXAP']
    BitgetBP_MEXCAP = results['BitgetBP_MEXCAP']
    BitgetBP_LbankAP = results['BitgetBP_LbankAP']
    BitgetBP_BitmartAP = results['BitgetBP_BitmartAP']
    BitgetBP_DeepcoinAP = results['BitgetBP_DeepcoinAP']
    BitgetBP_BitfinexAP = results['BitgetBP_BitfinexAP']
    BitgetBP_BingXAP = results['BitgetBP_BingXAP']
    BitgetBP_OrangeXAP = results['BitgetBP_OrangeXAP']
    BitgetBP_BitvenusAP = results['BitgetBP_BitvenusAP']
    BitgetBP_BiconomyAP = results['BitgetBP_BiconomyAP']
    BitgetBP_XTAP = results['BitgetBP_XTAP']
    BitgetBP_BitflyerAP = results['BitgetBP_BitflyerAP']
    BitgetBP_CoinWAP = results['BitgetBP_CoinWAP']
    BitgetBP_ToobitAP = results['BitgetBP_ToobitAP']
    BitgetBP_TapBitAP = results['BitgetBP_TapBitAP']

    BitstampBP_BinanceAP = results['BitstampBP_BinanceAP']
    BitstampBP_BybitAP = results['BitstampBP_BybitAP']
    BitstampBP_OKXAP = results['BitstampBP_OKXAP']
    BitstampBP_UpbitAP = results['BitstampBP_UpbitAP']
    BitstampBP_KucoinAP = results['BitstampBP_KucoinAP']
    BitstampBP_BitgetAP = results['BitstampBP_BitgetAP']
    BitstampBP_BitstampAP = results['BitstampBP_BitstampAP']
    BitstampBP_GeminiAP = results['BitstampBP_GeminiAP']
    BitstampBP_KrakenAP = results['BitstampBP_KrakenAP']
    BitstampBP_GateioAP = results['BitstampBP_Gate.ioAP']
    BitstampBP_HTXAP = results['BitstampBP_HTXAP']
    BitstampBP_MEXCAP = results['BitstampBP_MEXCAP']
    BitstampBP_LbankAP = results['BitstampBP_LbankAP']
    BitstampBP_BitmartAP = results['BitstampBP_BitmartAP']
    BitstampBP_DeepcoinAP = results['BitstampBP_DeepcoinAP']
    BitstampBP_BitfinexAP = results['BitstampBP_BitfinexAP']
    BitstampBP_BingXAP = results['BitstampBP_BingXAP']
    BitstampBP_OrangeXAP = results['BitstampBP_OrangeXAP']
    BitstampBP_BitvenusAP = results['BitstampBP_BitvenusAP']
    BitstampBP_BiconomyAP = results['BitstampBP_BiconomyAP']
    BitstampBP_XTAP = results['BitstampBP_XTAP']
    BitstampBP_BitflyerAP = results['BitstampBP_BitflyerAP']
    BitstampBP_CoinWAP = results['BitstampBP_CoinWAP']
    BitstampBP_ToobitAP = results['BitstampBP_ToobitAP']
    BitstampBP_TapBitAP = results['BitstampBP_TapBitAP']

    GeminiBP_BinanceAP = results['GeminiBP_BinanceAP']
    GeminiBP_BybitAP = results['GeminiBP_BybitAP']
    GeminiBP_OKXAP = results['GeminiBP_OKXAP']
    GeminiBP_UpbitAP = results['GeminiBP_UpbitAP']
    GeminiBP_KucoinAP = results['GeminiBP_KucoinAP']
    GeminiBP_BitgetAP = results['GeminiBP_BitgetAP']
    GeminiBP_BitstampAP = results['GeminiBP_BitstampAP']
    GeminiBP_GeminiAP = results['GeminiBP_GeminiAP']
    GeminiBP_KrakenAP = results['GeminiBP_KrakenAP']
    GeminiBP_GateioAP = results['GeminiBP_Gate.ioAP']
    GeminiBP_HTXAP = results['GeminiBP_HTXAP']
    GeminiBP_MEXCAP = results['GeminiBP_MEXCAP']
    GeminiBP_LbankAP = results['GeminiBP_LbankAP']
    GeminiBP_BitmartAP = results['GeminiBP_BitmartAP']
    GeminiBP_DeepcoinAP = results['GeminiBP_DeepcoinAP']
    GeminiBP_BitfinexAP = results['GeminiBP_BitfinexAP']
    GeminiBP_BingXAP = results['GeminiBP_BingXAP']
    GeminiBP_OrangeXAP = results['GeminiBP_OrangeXAP']
    GeminiBP_BitvenusAP = results['GeminiBP_BitvenusAP']
    GeminiBP_BiconomyAP = results['GeminiBP_BiconomyAP']
    GeminiBP_XTAP = results['GeminiBP_XTAP']
    GeminiBP_BitflyerAP = results['GeminiBP_BitflyerAP']
    GeminiBP_CoinWAP = results['GeminiBP_CoinWAP']
    GeminiBP_ToobitAP = results['GeminiBP_ToobitAP']
    GeminiBP_TapBitAP = results['GeminiBP_TapBitAP']

    KrakenBP_BinanceAP = results['KrakenBP_BinanceAP']
    KrakenBP_BybitAP = results['KrakenBP_BybitAP']
    KrakenBP_OKXAP = results['KrakenBP_OKXAP']
    KrakenBP_UpbitAP = results['KrakenBP_UpbitAP']
    KrakenBP_KucoinAP = results['KrakenBP_KucoinAP']
    KrakenBP_BitgetAP = results['KrakenBP_BitgetAP']
    KrakenBP_BitstampAP = results['KrakenBP_BitstampAP']
    KrakenBP_GeminiAP = results['KrakenBP_GeminiAP']
    KrakenBP_KrakenAP = results['KrakenBP_KrakenAP']
    KrakenBP_GateioAP = results['KrakenBP_Gate.ioAP']
    KrakenBP_HTXAP = results['KrakenBP_HTXAP']
    KrakenBP_MEXCAP = results['KrakenBP_MEXCAP']
    KrakenBP_LbankAP = results['KrakenBP_LbankAP']
    KrakenBP_BitmartAP = results['KrakenBP_BitmartAP']
    KrakenBP_DeepcoinAP = results['KrakenBP_DeepcoinAP']
    KrakenBP_BitfinexAP = results['KrakenBP_BitfinexAP']
    KrakenBP_BingXAP = results['KrakenBP_BingXAP']
    KrakenBP_OrangeXAP = results['KrakenBP_OrangeXAP']
    KrakenBP_BitvenusAP = results['KrakenBP_BitvenusAP']
    KrakenBP_BiconomyAP = results['KrakenBP_BiconomyAP']
    KrakenBP_XTAP = results['KrakenBP_XTAP']
    KrakenBP_BitflyerAP = results['KrakenBP_BitflyerAP']
    KrakenBP_CoinWAP = results['KrakenBP_CoinWAP']
    KrakenBP_ToobitAP = results['KrakenBP_ToobitAP']
    KrakenBP_TapBitAP = results['KrakenBP_TapBitAP']

    GateioBP_BinanceAP = results['Gate.ioBP_BinanceAP']
    GateioBP_BybitAP = results['Gate.ioBP_BybitAP']
    GateioBP_OKXAP = results['Gate.ioBP_OKXAP']
    GateioBP_UpbitAP = results['Gate.ioBP_UpbitAP']
    GateioBP_KucoinAP = results['Gate.ioBP_KucoinAP']
    GateioBP_BitgetAP = results['Gate.ioBP_BitgetAP']
    GateioBP_BitstampAP = results['Gate.ioBP_BitstampAP']
    GateioBP_GeminiAP = results['Gate.ioBP_GeminiAP']
    GateioBP_KrakenAP = results['Gate.ioBP_KrakenAP']
    GateioBP_GateioAP = results['Gate.ioBP_Gate.ioAP']
    GateioBP_HTXAP = results['Gate.ioBP_HTXAP']
    GateioBP_MEXCAP = results['Gate.ioBP_MEXCAP']
    GateioBP_LbankAP = results['Gate.ioBP_LbankAP']
    GateioBP_BitmartAP = results['Gate.ioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['Gate.ioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['Gate.ioBP_BitfinexAP']
    GateioBP_BingXAP = results['Gate.ioBP_BingXAP']
    GateioBP_OrangeXAP = results['Gate.ioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['Gate.ioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['Gate.ioBP_BiconomyAP']
    GateioBP_XTAP = results['Gate.ioBP_XTAP']
    GateioBP_BitflyerAP = results['Gate.ioBP_BitflyerAP']
    GateioBP_CoinWAP = results['Gate.ioBP_CoinWAP']
    GateioBP_ToobitAP = results['Gate.ioBP_ToobitAP']
    GateioBP_TapBitAP = results['Gate.ioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_Gate.ioAP']
    HTXBP_HTXAP = results['HTXBP_HTXAP']
    HTXBP_MEXCAP = results['HTXBP_MEXCAP']
    HTXBP_LbankAP = results['HTXBP_LbankAP']
    HTXBP_BitmartAP = results['HTXBP_BitmartAP']
    HTXBP_DeepcoinAP = results['HTXBP_DeepcoinAP']
    HTXBP_BitfinexAP = results['HTXBP_BitfinexAP']
    HTXBP_BingXAP = results['HTXBP_BingXAP']
    HTXBP_OrangeXAP = results['HTXBP_OrangeXAP']
    HTXBP_BitvenusAP = results['HTXBP_BitvenusAP']
    HTXBP_BiconomyAP = results['HTXBP_BiconomyAP']
    HTXBP_XTAP = results['HTXBP_XTAP']
    HTXBP_BitflyerAP = results['HTXBP_BitflyerAP']
    HTXBP_CoinWAP = results['HTXBP_CoinWAP']
    HTXBP_ToobitAP = results['HTXBP_ToobitAP']
    HTXBP_TapBitAP = results['HTXBP_TapBitAP']

    MEXCBP_BinanceAP = results['MEXCBP_BinanceAP']
    MEXCBP_BybitAP = results['MEXCBP_BybitAP']
    MEXCBP_OKXAP = results['MEXCBP_OKXAP']
    MEXCBP_UpbitAP = results['MEXCBP_UpbitAP']
    MEXCBP_KucoinAP = results['MEXCBP_KucoinAP']
    MEXCBP_BitgetAP = results['MEXCBP_BitgetAP']
    MEXCBP_BitstampAP = results['MEXCBP_BitstampAP']
    MEXCBP_GeminiAP = results['MEXCBP_GeminiAP']
    MEXCBP_KrakenAP = results['MEXCBP_KrakenAP']
    MEXCBP_GateioAP = results['BinanceBP_Gate.ioAP']
    MEXCBP_HTXAP = results['MEXCBP_HTXAP']
    MEXCBP_MEXCAP = results['MEXCBP_MEXCAP']
    MEXCBP_LbankAP = results['MEXCBP_LbankAP']
    MEXCBP_BitmartAP = results['MEXCBP_BitmartAP']
    MEXCBP_DeepcoinAP = results['MEXCBP_DeepcoinAP']
    MEXCBP_BitfinexAP = results['MEXCBP_BitfinexAP']
    MEXCBP_BingXAP = results['MEXCBP_BingXAP']
    MEXCBP_OrangeXAP = results['MEXCBP_OrangeXAP']
    MEXCBP_BitvenusAP = results['MEXCBP_BitvenusAP']
    MEXCBP_BiconomyAP = results['MEXCBP_BiconomyAP']
    MEXCBP_XTAP = results['MEXCBP_XTAP']
    MEXCBP_BitflyerAP = results['MEXCBP_BitflyerAP']
    MEXCBP_CoinWAP = results['MEXCBP_CoinWAP']
    MEXCBP_ToobitAP = results['MEXCBP_ToobitAP']
    MEXCBP_TapBitAP = results['MEXCBP_TapBitAP']

    LbankBP_BinanceAP = results['LbankBP_BinanceAP']
    LbankBP_BybitAP = results['LbankBP_BybitAP']
    LbankBP_OKXAP = results['LbankBP_OKXAP']
    LbankBP_UpbitAP = results['LbankBP_UpbitAP']
    LbankBP_KucoinAP = results['LbankBP_KucoinAP']
    LbankBP_BitgetAP = results['LbankBP_BitgetAP']
    LbankBP_BitstampAP = results['LbankBP_BitstampAP']
    LbankBP_GeminiAP = results['LbankBP_GeminiAP']
    LbankBP_KrakenAP = results['LbankBP_KrakenAP']
    LbankBP_GateioAP = results['LbankBP_Gate.ioAP']
    LbankBP_HTXAP = results['LbankBP_HTXAP']
    LbankBP_MEXCAP = results['LbankBP_MEXCAP']
    LbankBP_LbankAP = results['LbankBP_LbankAP']
    LbankBP_BitmartAP = results['LbankBP_BitmartAP']
    LbankBP_DeepcoinAP = results['LbankBP_DeepcoinAP']
    LbankBP_BitfinexAP = results['LbankBP_BitfinexAP']
    LbankBP_BingXAP = results['LbankBP_BingXAP']
    LbankBP_OrangeXAP = results['LbankBP_OrangeXAP']
    LbankBP_BitvenusAP = results['LbankBP_BitvenusAP']
    LbankBP_BiconomyAP = results['LbankBP_BiconomyAP']
    LbankBP_XTAP = results['LbankBP_XTAP']
    LbankBP_BitflyerAP = results['LbankBP_BitflyerAP']
    LbankBP_CoinWAP = results['LbankBP_CoinWAP']
    LbankBP_ToobitAP = results['LbankBP_ToobitAP']
    LbankBP_TapBitAP = results['LbankBP_TapBitAP']

    BitmartBP_BinanceAP = results['BitmartBP_BinanceAP']
    BitmartBP_BybitAP = results['BitmartBP_BybitAP']
    BitmartBP_OKXAP = results['BitmartBP_OKXAP']
    BitmartBP_UpbitAP = results['BitmartBP_UpbitAP']
    BitmartBP_KucoinAP = results['BitmartBP_KucoinAP']
    BitmartBP_BitgetAP = results['BitmartBP_BitgetAP']
    BitmartBP_BitstampAP = results['BitmartBP_BitstampAP']
    BitmartBP_GeminiAP = results['BitmartBP_GeminiAP']
    BitmartBP_KrakenAP = results['BitmartBP_KrakenAP']
    BitmartBP_GateioAP = results['BitmartBP_Gate.ioAP']
    BitmartBP_HTXAP = results['BitmartBP_HTXAP']
    BitmartBP_MEXCAP = results['BitmartBP_MEXCAP']
    BitmartBP_LbankAP = results['BitmartBP_LbankAP']
    BitmartBP_BitmartAP = results['BitmartBP_BitmartAP']
    BitmartBP_DeepcoinAP = results['BitmartBP_DeepcoinAP']
    BitmartBP_BitfinexAP = results['BitmartBP_BitfinexAP']
    BitmartBP_BingXAP = results['BitmartBP_BingXAP']
    BitmartBP_OrangeXAP = results['BitmartBP_OrangeXAP']
    BitmartBP_BitvenusAP = results['BitmartBP_BitvenusAP']
    BitmartBP_BiconomyAP = results['BitmartBP_BiconomyAP']
    BitmartBP_XTAP = results['BitmartBP_XTAP']
    BitmartBP_BitflyerAP = results['BitmartBP_BitflyerAP']
    BitmartBP_CoinWAP = results['BitmartBP_CoinWAP']
    BitmartBP_ToobitAP = results['BitmartBP_ToobitAP']
    BitmartBP_TapBitAP = results['BitmartBP_TapBitAP']

    DeepcoinBP_BinanceAP = results['DeepcoinBP_BinanceAP']
    DeepcoinBP_BybitAP = results['DeepcoinBP_BybitAP']
    DeepcoinBP_OKXAP = results['DeepcoinBP_OKXAP']
    DeepcoinBP_UpbitAP = results['DeepcoinBP_UpbitAP']
    DeepcoinBP_KucoinAP = results['DeepcoinBP_KucoinAP']
    DeepcoinBP_BitgetAP = results['DeepcoinBP_BitgetAP']
    DeepcoinBP_BitstampAP = results['DeepcoinBP_BitstampAP']
    DeepcoinBP_GeminiAP = results['DeepcoinBP_GeminiAP']
    DeepcoinBP_KrakenAP = results['DeepcoinBP_KrakenAP']
    DeepcoinBP_GateioAP = results['DeepcoinBP_Gate.ioAP']
    DeepcoinBP_HTXAP = results['DeepcoinBP_HTXAP']
    DeepcoinBP_MEXCAP = results['DeepcoinBP_MEXCAP']
    DeepcoinBP_LbankAP = results['DeepcoinBP_LbankAP']
    DeepcoinBP_BitmartAP = results['DeepcoinBP_BitmartAP']
    DeepcoinBP_DeepcoinAP = results['DeepcoinBP_DeepcoinAP']
    DeepcoinBP_BitfinexAP = results['DeepcoinBP_BitfinexAP']
    DeepcoinBP_BingXAP = results['DeepcoinBP_BingXAP']
    DeepcoinBP_OrangeXAP = results['DeepcoinBP_OrangeXAP']
    DeepcoinBP_BitvenusAP = results['DeepcoinBP_BitvenusAP']
    DeepcoinBP_BiconomyAP = results['DeepcoinBP_BiconomyAP']
    DeepcoinBP_XTAP = results['DeepcoinBP_XTAP']
    DeepcoinBP_BitflyerAP = results['DeepcoinBP_BitflyerAP']
    DeepcoinBP_CoinWAP = results['DeepcoinBP_CoinWAP']
    DeepcoinBP_ToobitAP = results['DeepcoinBP_ToobitAP']
    DeepcoinBP_TapBitAP = results['DeepcoinBP_TapBitAP']

    BitfinexBP_BinanceAP = results['BitfinexBP_BinanceAP']
    BitfinexBP_BybitAP = results['BitfinexBP_BybitAP']
    BitfinexBP_OKXAP = results['BitfinexBP_OKXAP']
    BitfinexBP_UpbitAP = results['BitfinexBP_UpbitAP']
    BitfinexBP_KucoinAP = results['BitfinexBP_KucoinAP']
    BitfinexBP_BitgetAP = results['BitfinexBP_BitgetAP']
    BitfinexBP_BitstampAP = results['BitfinexBP_BitstampAP']
    BitfinexBP_GeminiAP = results['BitfinexBP_GeminiAP']
    BitfinexBP_KrakenAP = results['BitfinexBP_KrakenAP']
    BitfinexBP_GateioAP = results['BitfinexBP_Gate.ioAP']
    BitfinexBP_HTXAP = results['BitfinexBP_HTXAP']
    BitfinexBP_MEXCAP = results['BitfinexBP_MEXCAP']
    BitfinexBP_LbankAP = results['BitfinexBP_LbankAP']
    BitfinexBP_BitmartAP = results['BitfinexBP_BitmartAP']
    BitfinexBP_DeepcoinAP = results['BitfinexBP_DeepcoinAP']
    BitfinexBP_BitfinexAP = results['BitfinexBP_BitfinexAP']
    BitfinexBP_BingXAP = results['BitfinexBP_BingXAP']
    BitfinexBP_OrangeXAP = results['BitfinexBP_OrangeXAP']
    BitfinexBP_BitvenusAP = results['BitfinexBP_BitvenusAP']
    BitfinexBP_BiconomyAP = results['BitfinexBP_BiconomyAP']
    BitfinexBP_XTAP = results['BitfinexBP_XTAP']
    BitfinexBP_BitflyerAP = results['BitfinexBP_BitflyerAP']
    BitfinexBP_CoinWAP = results['BitfinexBP_CoinWAP']
    BitfinexBP_ToobitAP = results['BitfinexBP_ToobitAP']
    BitfinexBP_TapBitAP = results['BitfinexBP_TapBitAP']

    BingXBP_BinanceAP = results['BingXBP_BinanceAP']
    BingXBP_BybitAP = results['BingXBP_BybitAP']
    BingXBP_OKXAP = results['BingXBP_OKXAP']
    BingXBP_UpbitAP = results['BingXBP_UpbitAP']
    BingXBP_KucoinAP = results['BingXBP_KucoinAP']
    BingXBP_BitgetAP = results['BingXBP_BitgetAP']
    BingXBP_BitstampAP = results['BingXBP_BitstampAP']
    BingXBP_GeminiAP = results['BingXBP_GeminiAP']
    BingXBP_KrakenAP = results['BingXBP_KrakenAP']
    BingXBP_GateioAP = results['BingXBP_Gate.ioAP']
    BingXBP_HTXAP = results['BingXBP_HTXAP']
    BingXBP_MEXCAP = results['BingXBP_MEXCAP']
    BingXBP_LbankAP = results['BingXBP_LbankAP']
    BingXBP_BitmartAP = results['BingXBP_BitmartAP']
    BingXBP_DeepcoinAP = results['BingXBP_DeepcoinAP']
    BingXBP_BitfinexAP = results['BingXBP_BitfinexAP']
    BingXBP_BingXAP = results['BingXBP_BingXAP']
    BingXBP_OrangeXAP = results['BingXBP_OrangeXAP']
    BingXBP_BitvenusAP = results['BingXBP_BitvenusAP']
    BingXBP_BiconomyAP = results['BingXBP_BiconomyAP']
    BingXBP_XTAP = results['BingXBP_XTAP']
    BingXBP_BitflyerAP = results['BingXBP_BitflyerAP']
    BingXBP_CoinWAP = results['BingXBP_CoinWAP']
    BingXBP_ToobitAP = results['BingXBP_ToobitAP']
    BingXBP_TapBitAP = results['BingXBP_TapBitAP']

    OrangeXBP_BinanceAP = results['OrangeXBP_BinanceAP']
    OrangeXBP_BybitAP = results['OrangeXBP_BybitAP']
    OrangeXBP_OKXAP = results['OrangeXBP_OKXAP']
    OrangeXBP_UpbitAP = results['OrangeXBP_UpbitAP']
    OrangeXBP_KucoinAP = results['OrangeXBP_KucoinAP']
    OrangeXBP_BitgetAP = results['OrangeXBP_BitgetAP']
    OrangeXBP_BitstampAP = results['OrangeXBP_BitstampAP']
    OrangeXBP_GeminiAP = results['OrangeXBP_GeminiAP']
    OrangeXBP_KrakenAP = results['OrangeXBP_KrakenAP']
    OrangeXBP_GateioAP = results['OrangeXBP_Gate.ioAP']
    OrangeXBP_HTXAP = results['OrangeXBP_HTXAP']
    OrangeXBP_MEXCAP = results['OrangeXBP_MEXCAP']
    OrangeXBP_LbankAP = results['OrangeXBP_LbankAP']
    OrangeXBP_BitmartAP = results['OrangeXBP_BitmartAP']
    OrangeXBP_DeepcoinAP = results['OrangeXBP_DeepcoinAP']
    OrangeXBP_BitfinexAP = results['OrangeXBP_BitfinexAP']
    OrangeXBP_BingXAP = results['OrangeXBP_BingXAP']
    OrangeXBP_OrangeXAP = results['OrangeXBP_OrangeXAP']
    OrangeXBP_BitvenusAP = results['OrangeXBP_BitvenusAP']
    OrangeXBP_BiconomyAP = results['OrangeXBP_BiconomyAP']
    OrangeXBP_XTAP = results['OrangeXBP_XTAP']
    OrangeXBP_BitflyerAP = results['OrangeXBP_BitflyerAP']
    OrangeXBP_CoinWAP = results['OrangeXBP_CoinWAP']
    OrangeXBP_ToobitAP = results['OrangeXBP_ToobitAP']
    OrangeXBP_TapBitAP = results['OrangeXBP_TapBitAP']

    BitvenusBP_BinanceAP = results['BitvenusBP_BinanceAP']
    BitvenusBP_BybitAP = results['BitvenusBP_BybitAP']
    BitvenusBP_OKXAP = results['BitvenusBP_OKXAP']
    BitvenusBP_UpbitAP = results['BitvenusBP_UpbitAP']
    BitvenusBP_KucoinAP = results['BitvenusBP_KucoinAP']
    BitvenusBP_BitgetAP = results['BitvenusBP_BitgetAP']
    BitvenusBP_BitstampAP = results['BitvenusBP_BitstampAP']
    BitvenusBP_GeminiAP = results['BitvenusBP_GeminiAP']
    BitvenusBP_KrakenAP = results['BitvenusBP_KrakenAP']
    BitvenusBP_GateioAP = results['BitvenusBP_Gate.ioAP']
    BitvenusBP_HTXAP = results['BitvenusBP_HTXAP']
    BitvenusBP_MEXCAP = results['BitvenusBP_MEXCAP']
    BitvenusBP_LbankAP = results['BitvenusBP_LbankAP']
    BitvenusBP_BitmartAP = results['BitvenusBP_BitmartAP']
    BitvenusBP_DeepcoinAP = results['BitvenusBP_DeepcoinAP']
    BitvenusBP_BitfinexAP = results['BitvenusBP_BitfinexAP']
    BitvenusBP_BingXAP = results['BitvenusBP_BingXAP']
    BitvenusBP_OrangeXAP = results['BitvenusBP_OrangeXAP']
    BitvenusBP_BitvenusAP = results['BitvenusBP_BitvenusAP']
    BitvenusBP_BiconomyAP = results['BitvenusBP_BiconomyAP']
    BitvenusBP_XTAP = results['BitvenusBP_XTAP']
    BitvenusBP_BitflyerAP = results['BitvenusBP_BitflyerAP']
    BitvenusBP_CoinWAP = results['BitvenusBP_CoinWAP']
    BitvenusBP_ToobitAP = results['BitvenusBP_ToobitAP']
    BitvenusBP_TapBitAP = results['BitvenusBP_TapBitAP']

    BiconomyBP_BinanceAP = results['BiconomyBP_BinanceAP']
    BiconomyBP_BybitAP = results['BiconomyBP_BybitAP']
    BiconomyBP_OKXAP = results['BiconomyBP_OKXAP']
    BiconomyBP_UpbitAP = results['BiconomyBP_UpbitAP']
    BiconomyBP_KucoinAP = results['BiconomyBP_KucoinAP']
    BiconomyBP_BitgetAP = results['BiconomyBP_BitgetAP']
    BiconomyBP_BitstampAP = results['BiconomyBP_BitstampAP']
    BiconomyBP_GeminiAP = results['BiconomyBP_GeminiAP']
    BiconomyBP_KrakenAP = results['BiconomyBP_KrakenAP']
    BiconomyBP_GateioAP = results['BiconomyBP_Gate.ioAP']
    BiconomyBP_HTXAP = results['BiconomyBP_HTXAP']
    BiconomyBP_MEXCAP = results['BiconomyBP_MEXCAP']
    BiconomyBP_LbankAP = results['BiconomyBP_LbankAP']
    BiconomyBP_BitmartAP = results['BiconomyBP_BitmartAP']
    BiconomyBP_DeepcoinAP = results['BiconomyBP_DeepcoinAP']
    BiconomyBP_BitfinexAP = results['BiconomyBP_BitfinexAP']
    BiconomyBP_BingXAP = results['BiconomyBP_BingXAP']
    BiconomyBP_OrangeXAP = results['BiconomyBP_OrangeXAP']
    BiconomyBP_BitvenusAP = results['BiconomyBP_BitvenusAP']
    BiconomyBP_BiconomyAP = results['BiconomyBP_BiconomyAP']
    BiconomyBP_XTAP = results['BiconomyBP_XTAP']
    BiconomyBP_BitflyerAP = results['BiconomyBP_BitflyerAP']
    BiconomyBP_CoinWAP = results['BiconomyBP_CoinWAP']
    BiconomyBP_ToobitAP = results['BiconomyBP_ToobitAP']
    BiconomyBP_TapBitAP = results['BiconomyBP_TapBitAP']

    XTBP_BinanceAP = results['XTBP_BinanceAP']
    XTBP_BybitAP = results['XTBP_BybitAP']
    XTBP_OKXAP = results['XTBP_OKXAP']
    XTBP_UpbitAP = results['XTBP_UpbitAP']
    XTBP_KucoinAP = results['XTBP_KucoinAP']
    XTBP_BitgetAP = results['XTBP_BitgetAP']
    XTBP_BitstampAP = results['XTBP_BitstampAP']
    XTBP_GeminiAP = results['XTBP_GeminiAP']
    XTBP_KrakenAP = results['XTBP_KrakenAP']
    XTBP_GateioAP = results['XTBP_Gate.ioAP']
    XTBP_HTXAP = results['XTBP_HTXAP']
    XTBP_MEXCAP = results['XTBP_MEXCAP']
    XTBP_LbankAP = results['XTBP_LbankAP']
    XTBP_BitmartAP = results['XTBP_BitmartAP']
    XTBP_DeepcoinAP = results['XTBP_DeepcoinAP']
    XTBP_BitfinexAP = results['XTBP_BitfinexAP']
    XTBP_BingXAP = results['XTBP_BingXAP']
    XTBP_OrangeXAP = results['XTBP_OrangeXAP']
    XTBP_BitvenusAP = results['XTBP_BitvenusAP']
    XTBP_BiconomyAP = results['XTBP_BiconomyAP']
    XTBP_XTAP = results['XTBP_XTAP']
    XTBP_BitflyerAP = results['XTBP_BitflyerAP']
    XTBP_CoinWAP = results['XTBP_CoinWAP']
    XTBP_ToobitAP = results['XTBP_ToobitAP']
    XTBP_TapBitAP = results['XTBP_TapBitAP']

    BitflyerBP_BinanceAP = results['BitflyerBP_BinanceAP']
    BitflyerBP_BybitAP = results['BitflyerBP_BybitAP']
    BitflyerBP_OKXAP = results['BitflyerBP_OKXAP']
    BitflyerBP_UpbitAP = results['BitflyerBP_UpbitAP']
    BitflyerBP_KucoinAP = results['BitflyerBP_KucoinAP']
    BitflyerBP_BitgetAP = results['BitflyerBP_BitgetAP']
    BitflyerBP_BitstampAP = results['BitflyerBP_BitstampAP']
    BitflyerBP_GeminiAP = results['BitflyerBP_GeminiAP']
    BitflyerBP_KrakenAP = results['BitflyerBP_KrakenAP']
    BitflyerBP_GateioAP = results['BitflyerBP_Gate.ioAP']
    BitflyerBP_HTXAP = results['BitflyerBP_HTXAP']
    BitflyerBP_MEXCAP = results['BitflyerBP_MEXCAP']
    BitflyerBP_LbankAP = results['BitflyerBP_LbankAP']
    BitflyerBP_BitmartAP = results['BitflyerBP_BitmartAP']
    BitflyerBP_DeepcoinAP = results['BitflyerBP_DeepcoinAP']
    BitflyerBP_BitfinexAP = results['BitflyerBP_BitfinexAP']
    BitflyerBP_BingXAP = results['BitflyerBP_BingXAP']
    BitflyerBP_OrangeXAP = results['BitflyerBP_OrangeXAP']
    BitflyerBP_BitvenusAP = results['BitflyerBP_BitvenusAP']
    BitflyerBP_BiconomyAP = results['BitflyerBP_BiconomyAP']
    BitflyerBP_XTAP = results['BitflyerBP_XTAP']
    BitflyerBP_BitflyerAP = results['BitflyerBP_BitflyerAP']
    BitflyerBP_CoinWAP = results['BitflyerBP_CoinWAP']
    BitflyerBP_ToobitAP = results['BitflyerBP_ToobitAP']
    BitflyerBP_TapBitAP = results['BitflyerBP_TapBitAP']

    CoinWBP_BinanceAP = results['CoinWBP_BinanceAP']
    CoinWBP_BybitAP = results['CoinWBP_BybitAP']
    CoinWBP_OKXAP = results['CoinWBP_OKXAP']
    CoinWBP_UpbitAP = results['CoinWBP_UpbitAP']
    CoinWBP_KucoinAP = results['CoinWBP_KucoinAP']
    CoinWBP_BitgetAP = results['CoinWBP_BitgetAP']
    CoinWBP_BitstampAP = results['CoinWBP_BitstampAP']
    CoinWBP_GeminiAP = results['CoinWBP_GeminiAP']
    CoinWBP_KrakenAP = results['CoinWBP_KrakenAP']
    CoinWBP_GateioAP = results['CoinWBP_Gate.ioAP']
    CoinWBP_HTXAP = results['CoinWBP_HTXAP']
    CoinWBP_MEXCAP = results['CoinWBP_MEXCAP']
    CoinWBP_LbankAP = results['CoinWBP_LbankAP']
    CoinWBP_BitmartAP = results['CoinWBP_BitmartAP']
    CoinWBP_DeepcoinAP = results['CoinWBP_DeepcoinAP']
    CoinWBP_BitfinexAP = results['CoinWBP_BitfinexAP']
    CoinWBP_BingXAP = results['CoinWBP_BingXAP']
    CoinWBP_OrangeXAP = results['CoinWBP_OrangeXAP']
    CoinWBP_BitvenusAP = results['CoinWBP_BitvenusAP']
    CoinWBP_BiconomyAP = results['CoinWBP_BiconomyAP']
    CoinWBP_XTAP = results['CoinWBP_XTAP']
    CoinWBP_BitflyerAP = results['CoinWBP_BitflyerAP']
    CoinWBP_CoinWAP = results['CoinWBP_CoinWAP']
    CoinWBP_ToobitAP = results['CoinWBP_ToobitAP']
    CoinWBP_TapBitAP = results['CoinWBP_TapBitAP']

    ToobitBP_BinanceAP = results['ToobitBP_BinanceAP']
    ToobitBP_BybitAP = results['ToobitBP_BybitAP']
    ToobitBP_OKXAP = results['ToobitBP_OKXAP']
    ToobitBP_UpbitAP = results['ToobitBP_UpbitAP']
    ToobitBP_KucoinAP = results['ToobitBP_KucoinAP']
    ToobitBP_BitgetAP = results['ToobitBP_BitgetAP']
    ToobitBP_BitstampAP = results['ToobitBP_BitstampAP']
    ToobitBP_GeminiAP = results['ToobitBP_GeminiAP']
    ToobitBP_KrakenAP = results['ToobitBP_KrakenAP']
    ToobitBP_GateioAP = results['ToobitBP_Gate.ioAP']
    ToobitBP_HTXAP = results['ToobitBP_HTXAP']
    ToobitBP_MEXCAP = results['ToobitBP_MEXCAP']
    ToobitBP_LbankAP = results['ToobitBP_LbankAP']
    ToobitBP_BitmartAP = results['ToobitBP_BitmartAP']
    ToobitBP_DeepcoinAP = results['ToobitBP_DeepcoinAP']
    ToobitBP_BitfinexAP = results['ToobitBP_BitfinexAP']
    ToobitBP_BingXAP = results['ToobitBP_BingXAP']
    ToobitBP_OrangeXAP = results['ToobitBP_OrangeXAP']
    ToobitBP_BitvenusAP = results['ToobitBP_BitvenusAP']
    ToobitBP_BiconomyAP = results['ToobitBP_BiconomyAP']
    ToobitBP_XTAP = results['ToobitBP_XTAP']
    ToobitBP_BitflyerAP = results['ToobitBP_BitflyerAP']
    ToobitBP_CoinWAP = results['ToobitBP_CoinWAP']
    ToobitBP_ToobitAP = results['ToobitBP_ToobitAP']
    ToobitBP_TapBitAP = results['ToobitBP_TapBitAP']

    TapBitBP_BinanceAP = results['TapBitBP_BinanceAP']
    TapBitBP_BybitAP = results['TapBitBP_BybitAP']
    TapBitBP_OKXAP = results['TapBitBP_OKXAP']
    TapBitBP_UpbitAP = results['TapBitBP_UpbitAP']
    TapBitBP_KucoinAP = results['TapBitBP_KucoinAP']
    TapBitBP_BitgetAP = results['TapBitBP_BitgetAP']
    TapBitBP_BitstampAP = results['TapBitBP_BitstampAP']
    TapBitBP_GeminiAP = results['TapBitBP_GeminiAP']
    TapBitBP_KrakenAP = results['TapBitBP_KrakenAP']
    TapBitBP_GateioAP = results['TapBitBP_Gate.ioAP']
    TapBitBP_HTXAP = results['TapBitBP_HTXAP']
    TapBitBP_MEXCAP = results['TapBitBP_MEXCAP']
    TapBitBP_LbankAP = results['TapBitBP_LbankAP']
    TapBitBP_BitmartAP = results['TapBitBP_BitmartAP']
    TapBitBP_DeepcoinAP = results['TapBitBP_DeepcoinAP']
    TapBitBP_BitfinexAP = results['TapBitBP_BitfinexAP']
    TapBitBP_BingXAP = results['TapBitBP_BingXAP']
    TapBitBP_OrangeXAP = results['TapBitBP_OrangeXAP']
    TapBitBP_BitvenusAP = results['TapBitBP_BitvenusAP']
    TapBitBP_BiconomyAP = results['TapBitBP_BiconomyAP']
    TapBitBP_XTAP = results['TapBitBP_XTAP']
    TapBitBP_BitflyerAP = results['TapBitBP_BitflyerAP']
    TapBitBP_CoinWAP = results['TapBitBP_CoinWAP']
    TapBitBP_ToobitAP = results['TapBitBP_ToobitAP']
    TapBitBP_TapBitAP = results['TapBitBP_TapBitAP']

    end =time.perf_counter_ns()
    processingtime = (end - start)+inital_time



    # "Binance",BinanceLTP,BinanceAP1,BinanceAP1V,BinanceBP1,BinanceBP1V,
    def Buckets(Name, LTP, AP4, AP4V, BP4, BP4V, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11,
                sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19, sub20, sub21, sub22, sub23, sub24, sub25,
                Status):
        tasks = []
        with ThreadPoolExecutor() as executor:
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Binance", BinanceLTP, BinanceAP4,
                                BinanceAP4V, BinanceBP4, BinanceBP4V, processingtime, sub1, Status, Binance_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bybit", BybitLTP, BybitAP4,
                                BybitAP4V, BybitBP4, BybitBP4V, processingtime, sub2, Status, BybitStatus))
            tasks.append(
                executor.submit(checker, OKXOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "OKX", OKXLTP, OKXAP4, OKXAP4V,
                                OKXBP4, OKXBP4V, processingtime, sub3, Binance_Status, OKX_Status))
            tasks.append(
                executor.submit(checker, UpbitOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Upbit", UpbitLTP, UpbitAP4,
                                UpbitAP4V, UpbitBP4, UpbitBP4V, processingtime, sub4, Status, Upbit_Status))
            tasks.append(
                executor.submit(checker, KucoinOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Kucoin", KucoinLTP, KucoinAP4,
                                KucoinAP4V, KucoinBP4, KucoinBP4V, processingtime, sub5, Status, Kucoin_Status))
            tasks.append(
                executor.submit(checker, BitgetOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitget", BitgetLTP, BitgetAP4,
                                BitgetAP4V, BitgetBP4, BitgetBP4V, processingtime, sub6, Status, Bitget_Status))
            tasks.append(executor.submit(checker, BitstampOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitstamp", BitstampLTP,
                                         BitstampAP4, BitstampAP4V, BitstampBP4, BitstampBP4V, processingtime, sub7,
                                         Status, Bitstamp_Status))
            tasks.append(
                executor.submit(checker, KrakenOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Kraken", KrakenLTP, KrakenAP4,
                                KrakenAP4V, KrakenBP4, KrakenBP4V, processingtime, sub8, Status, Kraken_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Gate.io", GateioLTP, GateioAP4,
                                GateioAP4V, GateioBP4, GateioBP4V, processingtime, sub9, Status, Gateio_Status))
            tasks.append(
                executor.submit(checker, HTXOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "HTX", HTXLTP, HTXAP4, HTXAP4V,
                                HTXBP4, HTXBP4V, processingtime, sub10, Status, HTX_Status))
            tasks.append(
                executor.submit(checker, MEXCOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "MEXC", MEXCLTP, MEXCAP4, MEXCAP4V,
                                MEXCBP4, MEXCBP4V, processingtime, sub11, Status, MEXC_Status))
            tasks.append(
                executor.submit(checker, LbankOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Lbank", LbankLTP, LbankAP4,
                                LbankAP4V, LbankBP4, LbankBP4V, processingtime, sub12, Status, Lbank_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitmart", BitmartLTP, BitmartAP4,
                                BitmartAP4V, BitmartBP4, BitmartBP4V, processingtime, sub13, Status, Bitmart_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Deepcoin", DeepcoinLTP,
                                         DeepcoinAP4, DeepcoinAP4V, DeepcoinBP4, DeepcoinBP4V, processingtime, sub14,
                                         Status, Deepcoin_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitfinex", BitfinexLTP,
                                         BitfinexAP4, BitfinexAP4V, BitfinexBP4, BitfinexBP4V, processingtime, sub15,
                                         Status, Bitfinex_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "BingX", BingXLTP, BingXAP4,
                                BingXAP4V, BingXBP4, BingXBP4V, processingtime, sub16, Status, BingX_Status))
            tasks.append(
                executor.submit(checker, OrangeXOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "OrangeX", OrangeXLTP, OrangeXAP4,
                                OrangeXAP4V, OrangeXBP4, OrangeXBP4V, processingtime, sub17, Status, OrangeX_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitvenus", BitvenusLTP,
                                         BitvenusAP4, BitvenusAP4V, BitvenusBP4, BitvenusBP4V, processingtime, sub18,
                                         Status, Bitvenus_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Biconomy", BiconomyLTP,
                                         BiconomyAP4, BiconomyAP4V, BiconomyBP4, BiconomyBP4V, processingtime, sub19,
                                         Status, Biconomy_Status))
            tasks.append(
                executor.submit(checker, GeminiOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Gemini", GeminiLTP, GeminiAP4,
                                GeminiAP4V, GeminiBP4, GeminiBP4V, processingtime, sub20, Status, Gemini_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "XT", XTLTP, XTAP4, XTAP4V, XTBP4,
                                XTBP4V, processingtime, sub21, Binance_Status, XT_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Bitflyer", BitflyerLTP, BitflyerAP4,
                                BitflyerAP4V, BitflyerBP4, BitflyerBP4V, processingtime, sub22, Status,
                                Bitflyer_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "CoinW", CoinWLTP, CoinWAP4, CoinWAP4V,
                                CoinWBP4, CoinWBP4V, processingtime, sub23, Status, CoinW_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Toobit", ToobitLTP, ToobitAP4,
                                ToobitAP4V, ToobitBP4, ToobitBP4V, processingtime, sub24, Status, Toobit_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP4, AP4V, BP4, BP4V, "Tapbit", TapbitLTP, TapbitAP4,
                                TapbitAP4V, TapbitBP4, TapbitBP4V, processingtime, sub25, Status, TapBit_Status))

            # Wait for all tasks to complete
            for task in tasks:
                task.result()

    buckets_args = [
        (
            "Binance", BinanceLTP, BinanceAP4, BinanceAP4V, BinanceBP4, BinanceBP4V, BinanceBP_BinanceAP,
            BinanceBP_BybitAP,
            BinanceBP_OKXAP, BinanceBP_UpbitAP, BinanceBP_KucoinAP, BinanceBP_BitgetAP, BinanceBP_BitstampAP,
            BinanceBP_GeminiAP, BinanceBP_KrakenAP, BinanceBP_GateioAP, BinanceBP_HTXAP, BinanceBP_MEXCAP,
            BinanceBP_LbankAP, BinanceBP_BitmartAP, BinanceBP_DeepcoinAP, BinanceBP_BitfinexAP, BinanceBP_BingXAP,
            BinanceBP_OrangeXAP, BinanceBP_BitvenusAP, BinanceBP_BiconomyAP, BinanceBP_XTAP, BinanceBP_BitflyerAP,
            BinanceBP_CoinWAP, BinanceBP_ToobitAP, BinanceBP_TapBitAP, Binance_Status),
        ("Bybit", BybitLTP, BybitAP4, BybitAP4V, BybitBP4, BybitBP4V, BybitBP_BinanceAP, BybitBP_BybitAP, BybitBP_OKXAP,
         BybitBP_UpbitAP, BybitBP_KucoinAP, BybitBP_BitgetAP, BybitBP_BitstampAP, BybitBP_GeminiAP, BybitBP_KrakenAP,
         BybitBP_GateioAP, BybitBP_HTXAP, BybitBP_MEXCAP, BybitBP_LbankAP, BybitBP_BitmartAP, BybitBP_DeepcoinAP,
         BybitBP_BitfinexAP, BybitBP_BingXAP, BybitBP_OrangeXAP, BybitBP_BitvenusAP, BybitBP_BiconomyAP, BybitBP_XTAP,
         BybitBP_BitflyerAP, BybitBP_CoinWAP, BybitBP_ToobitAP, BybitBP_TapBitAP, BybitStatus),
        ("OKX", OKXLTP, OKXAP4, OKXAP4V, OKXBP4, OKXBP4V, OKXBP_BinanceAP, OKXBP_BybitAP, OKXBP_OKXAP, OKXBP_UpbitAP,
         OKXBP_KucoinAP, OKXBP_BitgetAP, OKXBP_BitstampAP, OKXBP_GeminiAP, OKXBP_KrakenAP, OKXBP_GateioAP, OKXBP_HTXAP,
         OKXBP_MEXCAP, OKXBP_LbankAP, OKXBP_BitmartAP, OKXBP_DeepcoinAP, OKXBP_BitfinexAP, OKXBP_BingXAP,
         OKXBP_OrangeXAP, OKXBP_BitvenusAP, OKXBP_BiconomyAP, OKXBP_XTAP, OKXBP_BitflyerAP, OKXBP_CoinWAP,
         OKXBP_ToobitAP, OKXBP_TapBitAP, OKX_Status),
        ("Upbit", UpbitLTP, UpbitAP4, UpbitAP4V, UpbitBP4, UpbitBP4V, UpbitBP_BinanceAP, UpbitBP_BybitAP, UpbitBP_OKXAP,
         UpbitBP_UpbitAP, UpbitBP_KucoinAP, UpbitBP_BitgetAP, UpbitBP_BitstampAP, UpbitBP_GeminiAP, UpbitBP_KrakenAP,
         UpbitBP_GateioAP, UpbitBP_HTXAP, UpbitBP_MEXCAP, UpbitBP_LbankAP, UpbitBP_BitmartAP, UpbitBP_DeepcoinAP,
         UpbitBP_BitfinexAP, UpbitBP_BingXAP, UpbitBP_OrangeXAP, UpbitBP_BitvenusAP, UpbitBP_BiconomyAP, UpbitBP_XTAP,
         UpbitBP_BitflyerAP, UpbitBP_CoinWAP, UpbitBP_ToobitAP, UpbitBP_TapBitAP, Upbit_Status),
        ("Kucoin", KucoinLTP, KucoinAP4, KucoinAP4V, KucoinBP4, KucoinBP4V, KucoinBP_BinanceAP, KucoinBP_BybitAP,
         KucoinBP_OKXAP, KucoinBP_UpbitAP, KucoinBP_KucoinAP, KucoinBP_BitgetAP, KucoinBP_BitstampAP, KucoinBP_GeminiAP,
         KucoinBP_KrakenAP, KucoinBP_GateioAP, KucoinBP_HTXAP, KucoinBP_MEXCAP, KucoinBP_LbankAP, KucoinBP_BitmartAP,
         KucoinBP_DeepcoinAP, KucoinBP_BitfinexAP, KucoinBP_BingXAP, KucoinBP_OrangeXAP, KucoinBP_BitvenusAP,
         KucoinBP_BiconomyAP, KucoinBP_XTAP, KucoinBP_BitflyerAP, KucoinBP_CoinWAP, KucoinBP_ToobitAP,
         KucoinBP_TapBitAP, Kucoin_Status),
        ("Bitget", BitgetLTP, BitgetAP4, BitgetAP4V, BitgetBP4, BitgetBP4V, BitgetBP_BinanceAP, BitgetBP_BybitAP,
         BitgetBP_OKXAP, BitgetBP_UpbitAP, BitgetBP_KucoinAP, BitgetBP_BitgetAP, BitgetBP_BitstampAP, BitgetBP_GeminiAP,
         BitgetBP_KrakenAP, BitgetBP_GateioAP, BitgetBP_HTXAP, BitgetBP_MEXCAP, BitgetBP_LbankAP, BitgetBP_BitmartAP,
         BitgetBP_DeepcoinAP, BitgetBP_BitfinexAP, BitgetBP_BingXAP, BitgetBP_OrangeXAP, BitgetBP_BitvenusAP,
         BitgetBP_BiconomyAP, BitgetBP_XTAP, BitgetBP_BitflyerAP, BitgetBP_CoinWAP, BitgetBP_ToobitAP,
         BitgetBP_TapBitAP, Bitget_Status),
        ("Bitstamp", BitstampLTP, BitstampAP4, BitstampAP4V, BitstampBP4, BitstampBP4V, BitstampBP_BinanceAP,
         BitstampBP_BybitAP, BitstampBP_OKXAP, BitstampBP_UpbitAP, BitstampBP_KucoinAP, BitstampBP_BitgetAP,
         BitstampBP_BitstampAP, BitstampBP_GeminiAP, BitstampBP_KrakenAP, BitstampBP_GateioAP, BitstampBP_HTXAP,
         BitstampBP_MEXCAP, BitstampBP_LbankAP, BitstampBP_BitmartAP, BitstampBP_DeepcoinAP, BitstampBP_BitfinexAP,
         BitstampBP_BingXAP, BitstampBP_OrangeXAP, BitstampBP_BitvenusAP, BitstampBP_BiconomyAP, BitstampBP_XTAP,
         BitstampBP_BitflyerAP, BitstampBP_CoinWAP, BitstampBP_ToobitAP, BitstampBP_TapBitAP, Bitstamp_Status),
        ("Kraken", KrakenLTP, KrakenAP4, KrakenAP4V, KrakenBP4, KrakenBP4V, KrakenBP_BinanceAP, KrakenBP_BybitAP,
         KrakenBP_OKXAP, KrakenBP_UpbitAP, KrakenBP_KucoinAP, KrakenBP_BitgetAP, KrakenBP_BitstampAP, KrakenBP_GeminiAP,
         KrakenBP_KrakenAP, KrakenBP_GateioAP, KrakenBP_HTXAP, KrakenBP_MEXCAP, KrakenBP_LbankAP, KrakenBP_BitmartAP,
         KrakenBP_DeepcoinAP, KrakenBP_BitfinexAP, KrakenBP_BingXAP, KrakenBP_OrangeXAP, KrakenBP_BitvenusAP,
         KrakenBP_BiconomyAP, KrakenBP_XTAP, KrakenBP_BitflyerAP, KrakenBP_CoinWAP, KrakenBP_ToobitAP,
         KrakenBP_TapBitAP, Kraken_Status),
        ("Gate.io", GateioLTP, GateioAP4, GateioAP4V, GateioBP4, GateioBP4V, GateioBP_BinanceAP, GateioBP_BybitAP,
         GateioBP_OKXAP, GateioBP_UpbitAP, GateioBP_KucoinAP, GateioBP_BitgetAP, GateioBP_BitstampAP, GateioBP_GeminiAP,
         GateioBP_KrakenAP, GateioBP_GateioAP, GateioBP_HTXAP, GateioBP_MEXCAP, GateioBP_LbankAP, GateioBP_BitmartAP,
         GateioBP_DeepcoinAP, GateioBP_BitfinexAP, GateioBP_BingXAP, GateioBP_OrangeXAP, GateioBP_BitvenusAP,
         GateioBP_BiconomyAP, GateioBP_XTAP, GateioBP_BitflyerAP, GateioBP_CoinWAP, GateioBP_ToobitAP,
         GateioBP_TapBitAP, Gateio_Status),
        ("HTX", HTXLTP, HTXAP4,
         HTXAP4V,
         HTXBP4, HTXBP4V,
         HTXBP_BinanceAP, HTXBP_BybitAP, HTXBP_OKXAP, HTXBP_UpbitAP, HTXBP_KucoinAP,
         HTXBP_BitgetAP, HTXBP_BitstampAP
         , HTXBP_GeminiAP, HTXBP_KrakenAP, HTXBP_GateioAP, HTXBP_HTXAP, HTXBP_MEXCAP,
         HTXBP_LbankAP, HTXBP_BitmartAP
         , HTXBP_DeepcoinAP, HTXBP_BitfinexAP, HTXBP_BingXAP, HTXBP_OrangeXAP, HTXBP_BitvenusAP,
         HTXBP_BiconomyAP,
         HTXBP_XTAP, HTXBP_BitflyerAP, HTXBP_CoinWAP, HTXBP_ToobitAP, HTXBP_TapBitAP, HTX_Status
         ),
        ("MEXC", MEXCLTP,
         MEXCAP4, MEXCAP4V,
         MEXCBP4, MEXCBP4V,
         MEXCBP_BinanceAP, MEXCBP_BybitAP, MEXCBP_OKXAP, MEXCBP_UpbitAP, MEXCBP_KucoinAP,
         MEXCBP_BitgetAP, MEXCBP_BitstampAP
         , MEXCBP_GeminiAP, MEXCBP_KrakenAP, MEXCBP_GateioAP, MEXCBP_HTXAP, MEXCBP_MEXCAP,
         MEXCBP_LbankAP, MEXCBP_BitmartAP
         , MEXCBP_DeepcoinAP, MEXCBP_BitfinexAP, MEXCBP_BingXAP, MEXCBP_OrangeXAP, MEXCBP_BitvenusAP,
         MEXCBP_BiconomyAP,
         MEXCBP_XTAP, MEXCBP_BitflyerAP, MEXCBP_CoinWAP, MEXCBP_ToobitAP, MEXCBP_TapBitAP, MEXC_Status
         ),
        ("Lbank", LbankLTP,
         LbankAP4, LbankAP4V,
         LbankBP4, LbankBP4V,
         LbankBP_BinanceAP, LbankBP_BybitAP, LbankBP_OKXAP, LbankBP_UpbitAP, LbankBP_KucoinAP,
         LbankBP_BitgetAP, LbankBP_BitstampAP
         , LbankBP_GeminiAP, LbankBP_KrakenAP, LbankBP_GateioAP, LbankBP_HTXAP, LbankBP_MEXCAP,
         LbankBP_LbankAP, LbankBP_BitmartAP
         , LbankBP_DeepcoinAP, LbankBP_BitfinexAP, LbankBP_BingXAP, LbankBP_OrangeXAP, LbankBP_BitvenusAP,
         LbankBP_BiconomyAP,
         LbankBP_XTAP, LbankBP_BitflyerAP, LbankBP_CoinWAP, LbankBP_ToobitAP, LbankBP_TapBitAP, Lbank_Status
         ),
        ("Bitmart",
         BitmartLTP, BitmartAP4, BitmartAP4V,
         BitmartBP4, BitmartBP4V,
         BitmartBP_BinanceAP, BitmartBP_BybitAP, BitmartBP_OKXAP, BitmartBP_UpbitAP, BitmartBP_KucoinAP,
         BitmartBP_BitgetAP, BitmartBP_BitstampAP
         , BitmartBP_GeminiAP, BitmartBP_KrakenAP, BitmartBP_GateioAP, BitmartBP_HTXAP, BitmartBP_MEXCAP,
         BitmartBP_LbankAP, BitmartBP_BitmartAP
         , BitmartBP_DeepcoinAP, BitmartBP_BitfinexAP, BitmartBP_BingXAP, BitmartBP_OrangeXAP, BitmartBP_BitvenusAP,
         BitmartBP_BiconomyAP,
         BitmartBP_XTAP, BitmartBP_BitflyerAP, BitmartBP_CoinWAP, BitmartBP_ToobitAP, BitmartBP_TapBitAP, Bitmart_Status
         ),
        ("Deepcoin",
         DeepcoinLTP,
         DeepcoinAP4, DeepcoinAP4V, DeepcoinBP4, DeepcoinBP4V,
         DeepcoinBP_BinanceAP, DeepcoinBP_BybitAP, DeepcoinBP_OKXAP, DeepcoinBP_UpbitAP, DeepcoinBP_KucoinAP,
         DeepcoinBP_BitgetAP, DeepcoinBP_BitstampAP
         , DeepcoinBP_GeminiAP, DeepcoinBP_KrakenAP, DeepcoinBP_GateioAP, DeepcoinBP_HTXAP, DeepcoinBP_MEXCAP,
         DeepcoinBP_LbankAP, DeepcoinBP_BitmartAP
         , DeepcoinBP_DeepcoinAP, DeepcoinBP_BitfinexAP, DeepcoinBP_BingXAP, DeepcoinBP_OrangeXAP,
         DeepcoinBP_BitvenusAP,
         DeepcoinBP_BiconomyAP,
         DeepcoinBP_XTAP, DeepcoinBP_BitflyerAP, DeepcoinBP_CoinWAP, DeepcoinBP_ToobitAP, DeepcoinBP_TapBitAP,
         Deepcoin_Status
         ),
        ("Bitfinex",
         BitfinexLTP, BitfinexAP4, BitfinexAP4V,
         BitfinexBP4, BitfinexBP4V,
         BitfinexBP_BinanceAP, BitfinexBP_BybitAP, BitfinexBP_OKXAP, BitfinexBP_UpbitAP, BitfinexBP_KucoinAP,
         BitfinexBP_BitgetAP, BitfinexBP_BitstampAP
         , BitfinexBP_GeminiAP, BitfinexBP_KrakenAP, BitfinexBP_GateioAP, BitfinexBP_HTXAP, BitfinexBP_MEXCAP,
         BitfinexBP_LbankAP, BitfinexBP_BitmartAP
         , BitfinexBP_DeepcoinAP, BitfinexBP_BitfinexAP, BitfinexBP_BingXAP, BitfinexBP_OrangeXAP,
         BitfinexBP_BitvenusAP,
         BitfinexBP_BiconomyAP,
         BitfinexBP_XTAP, BitfinexBP_BitflyerAP, BitfinexBP_CoinWAP, BitfinexBP_ToobitAP, BitfinexBP_TapBitAP,
         Bitfinex_Status
         ),
        ("BingX", BingXLTP,
         BingXAP4, BingXAP4V,
         BingXBP4, BingXBP4V,
         BingXBP_BinanceAP, BingXBP_BybitAP, BingXBP_OKXAP, BingXBP_UpbitAP, BingXBP_KucoinAP,
         BingXBP_BitgetAP, BingXBP_BitstampAP
         , BingXBP_GeminiAP, BingXBP_KrakenAP, BingXBP_GateioAP, BingXBP_HTXAP, BingXBP_MEXCAP,
         BingXBP_LbankAP, BingXBP_BitmartAP
         , BingXBP_DeepcoinAP, BingXBP_BitfinexAP, BingXBP_BingXAP, BingXBP_OrangeXAP, BingXBP_BitvenusAP,
         BingXBP_BiconomyAP,
         BingXBP_XTAP, BingXBP_BitflyerAP, BingXBP_CoinWAP, BingXBP_ToobitAP, BingXBP_TapBitAP, BingX_Status
         ),
        ("OrangeX",
         OrangeXLTP, OrangeXAP4, OrangeXAP4V,
         OrangeXBP4, OrangeXBP4V,
         OrangeXBP_BinanceAP, OrangeXBP_BybitAP, OrangeXBP_OKXAP, OrangeXBP_UpbitAP, OrangeXBP_KucoinAP,
         OrangeXBP_BitgetAP, OrangeXBP_BitstampAP
         , OrangeXBP_GeminiAP, OrangeXBP_KrakenAP, OrangeXBP_GateioAP, OrangeXBP_HTXAP, OrangeXBP_MEXCAP,
         OrangeXBP_LbankAP, OrangeXBP_BitmartAP
         , OrangeXBP_DeepcoinAP, OrangeXBP_BitfinexAP, OrangeXBP_BingXAP, OrangeXBP_OrangeXAP, OrangeXBP_BitvenusAP,
         OrangeXBP_BiconomyAP,
         OrangeXBP_XTAP, OrangeXBP_BitflyerAP, OrangeXBP_CoinWAP, OrangeXBP_ToobitAP, OrangeXBP_TapBitAP, OrangeX_Status
         ),
        ("Bitvenus",
         BitvenusLTP, BitvenusAP4, BitvenusAP4V,
         BitvenusBP4, BitvenusBP4V,
         BitvenusBP_BinanceAP, BitvenusBP_BybitAP, BitvenusBP_OKXAP, BitvenusBP_UpbitAP, BitvenusBP_KucoinAP,
         BitvenusBP_BitgetAP, BitvenusBP_BitstampAP
         , BitvenusBP_GeminiAP, BitvenusBP_KrakenAP, BitvenusBP_GateioAP, BitvenusBP_HTXAP, BitvenusBP_MEXCAP,
         BitvenusBP_LbankAP, BitvenusBP_BitmartAP
         , BitvenusBP_DeepcoinAP, BitvenusBP_BitfinexAP, BitvenusBP_BingXAP, BitvenusBP_OrangeXAP,
         BitvenusBP_BitvenusAP,
         BitvenusBP_BiconomyAP,
         BitvenusBP_XTAP, BitvenusBP_BitflyerAP, BitvenusBP_CoinWAP, BitvenusBP_ToobitAP, BitvenusBP_TapBitAP,
         Bitvenus_Status
         ),
        ("Biconomy",
         BiconomyLTP, BiconomyAP4, BiconomyAP4V,
         BiconomyBP4, BiconomyBP4V,
         BiconomyBP_BinanceAP, BiconomyBP_BybitAP, BiconomyBP_OKXAP, BiconomyBP_UpbitAP, BiconomyBP_KucoinAP,
         BiconomyBP_BitgetAP, BiconomyBP_BitstampAP
         , BiconomyBP_GeminiAP, BiconomyBP_KrakenAP, BiconomyBP_GateioAP, BiconomyBP_HTXAP, BiconomyBP_MEXCAP,
         BiconomyBP_LbankAP, BiconomyBP_BitmartAP
         , BiconomyBP_DeepcoinAP, BiconomyBP_BitfinexAP, BiconomyBP_BingXAP, BiconomyBP_OrangeXAP,
         BiconomyBP_BitvenusAP,
         BiconomyBP_BiconomyAP,
         BiconomyBP_XTAP, BiconomyBP_BitflyerAP, BiconomyBP_CoinWAP, BiconomyBP_ToobitAP, BiconomyBP_TapBitAP,
         Biconomy_Status
         ),
        ("Gemini", GeminiLTP,
         GeminiAP4, GeminiAP4V,
         GeminiBP4, GeminiBP4V,
         GeminiBP_BinanceAP, GeminiBP_BybitAP, GeminiBP_OKXAP, GeminiBP_UpbitAP, GeminiBP_KucoinAP,
         GeminiBP_BitgetAP, GeminiBP_BitstampAP
         , GeminiBP_GeminiAP, GeminiBP_KrakenAP, GeminiBP_GateioAP, GeminiBP_HTXAP, GeminiBP_MEXCAP,
         GeminiBP_LbankAP, GeminiBP_BitmartAP
         , GeminiBP_DeepcoinAP, GeminiBP_BitfinexAP, GeminiBP_BingXAP, GeminiBP_OrangeXAP, GeminiBP_BitvenusAP,
         GeminiBP_BiconomyAP,
         GeminiBP_XTAP, GeminiBP_BitflyerAP, GeminiBP_CoinWAP, GeminiBP_ToobitAP, GeminiBP_TapBitAP, Gemini_Status
         ),
        ("XT", XTLTP, XTAP4,
         XTAP4V,
         XTBP4, XTBP4V,
         XTBP_BinanceAP, XTBP_BybitAP, XTBP_OKXAP, XTBP_UpbitAP, XTBP_KucoinAP,
         XTBP_BitgetAP, XTBP_BitstampAP
         , XTBP_GeminiAP, XTBP_KrakenAP, XTBP_GateioAP, XTBP_HTXAP, XTBP_MEXCAP,
         XTBP_LbankAP, XTBP_BitmartAP
         , XTBP_DeepcoinAP, XTBP_BitfinexAP, XTBP_BingXAP, XTBP_OrangeXAP, XTBP_BitvenusAP,
         XTBP_BiconomyAP,
         XTBP_XTAP, XTBP_BitflyerAP, XTBP_CoinWAP, XTBP_ToobitAP, XTBP_TapBitAP, XT_Status
         ),
        ("Bitflyer", BitflyerLTP,
         BitflyerAP4, BitflyerAP4V,
         BitflyerBP4, BitflyerBP4V,
         BitflyerBP_BinanceAP, BitflyerBP_BybitAP, BitflyerBP_OKXAP, BitflyerBP_UpbitAP, BitflyerBP_KucoinAP,
         BitflyerBP_BitgetAP, BitflyerBP_BitstampAP
         , BitflyerBP_GeminiAP, BitflyerBP_KrakenAP, BitflyerBP_GateioAP, BitflyerBP_HTXAP, BitflyerBP_MEXCAP,
         BitflyerBP_LbankAP, BitflyerBP_BitmartAP
         , BitflyerBP_DeepcoinAP, BitflyerBP_BitfinexAP, BitflyerBP_BingXAP, BitflyerBP_OrangeXAP,
         BitflyerBP_BitvenusAP,
         BitflyerBP_BiconomyAP,
         BitflyerBP_XTAP, BitflyerBP_BitflyerAP, BitflyerBP_CoinWAP, BitflyerBP_ToobitAP, BitflyerBP_TapBitAP,
         Bitflyer_Status
         ),
        ("CoinW", CoinWLTP,
         CoinWAP4, CoinWAP4V,
         CoinWBP4, CoinWBP4V,
         CoinWBP_BinanceAP, CoinWBP_BybitAP, CoinWBP_OKXAP, CoinWBP_UpbitAP, CoinWBP_KucoinAP,
         CoinWBP_BitgetAP, CoinWBP_BitstampAP
         , CoinWBP_GeminiAP, CoinWBP_KrakenAP, CoinWBP_GateioAP, CoinWBP_HTXAP, CoinWBP_MEXCAP,
         CoinWBP_LbankAP, CoinWBP_BitmartAP
         , CoinWBP_DeepcoinAP, CoinWBP_BitfinexAP, CoinWBP_BingXAP, CoinWBP_OrangeXAP, CoinWBP_BitvenusAP,
         CoinWBP_BiconomyAP,
         CoinWBP_XTAP, CoinWBP_BitflyerAP, CoinWBP_CoinWAP, CoinWBP_ToobitAP, CoinWBP_TapBitAP, CoinW_Status
         ),
        ("Toobit", ToobitLTP,
         ToobitAP4, ToobitAP4V,
         ToobitBP4, ToobitBP4V,
         ToobitBP_BinanceAP, ToobitBP_BybitAP, ToobitBP_OKXAP, ToobitBP_UpbitAP, ToobitBP_KucoinAP,
         ToobitBP_BitgetAP, ToobitBP_BitstampAP
         , ToobitBP_GeminiAP, ToobitBP_KrakenAP, ToobitBP_GateioAP, ToobitBP_HTXAP, ToobitBP_MEXCAP,
         ToobitBP_LbankAP, ToobitBP_BitmartAP
         , ToobitBP_DeepcoinAP, ToobitBP_BitfinexAP, ToobitBP_BingXAP, ToobitBP_OrangeXAP, ToobitBP_BitvenusAP,
         ToobitBP_BiconomyAP,
         ToobitBP_XTAP, ToobitBP_BitflyerAP, ToobitBP_CoinWAP, ToobitBP_ToobitAP, ToobitBP_TapBitAP, Toobit_Status
         ),
        ("Tapbit", TapbitLTP,
         TapbitAP4, TapbitAP4V,
         TapbitBP4, TapbitBP4V,
         TapBitBP_BinanceAP, TapBitBP_BybitAP, TapBitBP_OKXAP, TapBitBP_UpbitAP, TapBitBP_KucoinAP,
         TapBitBP_BitgetAP, TapBitBP_BitstampAP
         , TapBitBP_GeminiAP, TapBitBP_KrakenAP, TapBitBP_GateioAP, TapBitBP_HTXAP, TapBitBP_MEXCAP,
         TapBitBP_LbankAP, TapBitBP_BitmartAP
         , TapBitBP_DeepcoinAP, TapBitBP_BitfinexAP, TapBitBP_BingXAP, TapBitBP_OrangeXAP, TapBitBP_BitvenusAP,
         TapBitBP_BiconomyAP,
         TapBitBP_XTAP, TapBitBP_BitflyerAP, TapBitBP_CoinWAP, TapBitBP_ToobitAP, TapBitBP_TapBitAP, TapBit_Status
         )

        # Add other exchanges similarly
    ]

    # Create a list to hold the threads
    threads = []

    # Create and start a thread for each PriceDifference function call
    for args in buckets_args:
        thread = threading.Thread(target=Buckets, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



async def Bid_Ask5(results,inital_time):
    start = time.perf_counter_ns()



    # Binance
    BinanceBP5 = results["BinanceBP5"]
    BinanceBP5V = results["BinanceBP5V"]
    BinanceAP5 = results["BinanceAP5"]
    BinanceAP5V = results["BinanceAP5V"]
    BinanceOBT = results["BinanceOBT"]
    BinanceLTP = results["BinanceLTP"]

    # Bybit
    BybitBP5 = results["BybitBP5"]
    BybitBP5V = results["BybitBP5V"]
    BybitAP5 = results["BybitAP5"]
    BybitAP5V = results["BybitAP5V"]
    BybitOBT = results["BybitOBT"]
    BybitLTP = results["BybitLTP"]

    # OKX
    OKXBP5 = results["OKXBP5"]
    OKXBP5V = results["OKXBP5V"]
    OKXAP5 = results["OKXAP5"]
    OKXAP5V = results["OKXAP5V"]
    OKXOBT = results["OKXOBT"]
    OKXLTP = results["OKXLTP"]

    # Upbit
    UpbitBP5 = results["UpbitBP5"]
    UpbitBP5V = results["UpbitBP5V"]
    UpbitAP5 = results["UpbitAP5"]
    UpbitAP5V = results["UpbitAP5V"]
    UpbitOBT = results["UpbitOBT"]
    UpbitLTP = results["UpbitLTP"]

    # Kucoin
    KucoinBP5 = results["KucoinBP5"]
    KucoinBP5V = results["KucoinBP5V"]
    KucoinAP5 = results["KucoinAP5"]
    KucoinAP5V = results["KucoinAP5V"]
    KucoinOBT = results["KucoinOBT"]
    KucoinLTP = results["KucoinLTP"]

    # Bitget
    BitgetBP5 = results["BitgetBP5"]
    BitgetBP5V = results["BitgetBP5V"]
    BitgetAP5 = results["BitgetAP5"]
    BitgetAP5V = results["BitgetAP5V"]
    BitgetOBT = results["BitgetOBT"]
    BitgetLTP = results["BitgetLTP"]

    # Bitstamp
    BitstampBP5 = results["BitstampBP5"]
    BitstampBP5V = results["BitstampBP5V"]
    BitstampAP5 = results["BitstampAP5"]
    BitstampAP5V = results["BitstampAP5V"]
    BitstampOBT = results["BitstampOBT"]
    BitstampLTP = results["BitstampLTP"]

    # Gemini
    GeminiBP5 = results["GeminiBP5"]
    GeminiBP5V = results["GeminiBP5V"]
    GeminiAP5 = results["GeminiAP5"]
    GeminiAP5V = results["GeminiAP5V"]
    GeminiOBT = results["GeminiOBT"]
    GeminiLTP = results["GeminiLTP"]

    # Kraken
    KrakenBP5 = results["KrakenBP5"]
    KrakenBPV5 = results["KrakenBP5V"]
    KrakenAP5 = results["KrakenAP5"]
    KrakenAPV5 = results["KrakenAP5V"]
    KrakenOBT = results["KrakenOBT"]
    KrakenLTP = results["KrakenLTP"]

    # Gateio
    GateioBP5 = results["GateioBP5"]
    GateioBPV5 = results["GateioBP5V"]
    GateioAP5 = results["GateioAP5"]
    GateioAPV5 = results["GateioAP5V"]
    GateioOBT = results["GateioOBT"]
    GateioLTP = results["GateioLTP"]

    # HTX
    HTXBP5 = results["HTXBP5"]
    HTXBP5V = results["HTXBP5V"]
    HTXAP5 = results["HTXAP5"]
    HTXAP5V = results["HTXAP5V"]
    HTXOBT = results["HTXOBT"]
    HTXLTP = results["HTXLTP"]

    # MEXC
    MEXCBP5 = results["MEXCBP5"]
    MEXCBP5V = results["MEXCBP5V"]
    MEXCAP5 = results["MEXCAP5"]
    MEXCAP5V = results["MEXCAP5V"]
    MEXCOBT = results["MEXCOBT"]
    MEXCLTP = results["MEXCLTP"]

    # Lbank
    LbankBP5 = results["LbankBP5"]
    LbankBP5V = results["LbankBP5V"]
    LbankAP5 = results["LbankAP5"]
    LbankAP5V = results["LbankAP5V"]
    LbankOBT = results["LbankOBT"]
    LbankLTP = results["LbankLTP"]

    # Bitmart
    BitmartBP5 = results["BitmartBP5"]
    BitmartBP5V = results["BitmartBP5V"]
    BitmartAP5 = results["BitmartAP5"]
    BitmartAP5V = results["BitmartAP5V"]
    BitmartOBT = results["BitmartOBT"]
    BitmartLTP = results["BitmartLTP"]

    # Deepcoin
    DeepcoinBP5 = results["DeepcoinBP5"]
    DeepcoinBP5V = results["DeepcoinBP5V"]
    DeepcoinAP5 = results["DeepcoinAP5"]
    DeepcoinAP5V = results["DeepcoinAP5V"]
    DeepcoinOBT = results["DeepcoinOBT"]
    DeepcoinLTP = results["DeepcoinLTP"]

    # Bitfinex
    BitfinexBP5 = results["BitfinexBP5"]
    BitfinexBP5V = results["BitfinexBP5V"]
    BitfinexAP5 = results["BitfinexAP5"]
    BitfinexAP5V = results["BitfinexAP5V"]
    BitfinexOBT = results["BitfinexOBT"]
    BitfinexLTP = results["BitfinexLTP"]

    # BingX
    BingXBP5 = results["BingXBP5"]
    BingXBP5V = results["BingXBP5V"]
    BingXAP5 = results["BingXAP5"]
    BingXAP5V = results["BingXAP5V"]
    BingXOBT = results["BingXOBT"]
    BingXLTP = results["BingXLTP"]

    # OrangeX
    OrangeXBP5 = results["OrangeXBP5"]
    OrangeXBP5V = results["OrangeXBP5V"]
    OrangeXAP5 = results["OrangeXAP5"]
    OrangeXAP5V = results["OrangeXAP5V"]
    OrangeXOBT = results["OrangeXOBT"]
    OrangeXLTP = results["OrangeXLTP"]

    # Bitvenus
    BitvenusBP5 = results["BitvenusBP5"]
    BitvenusBP5V = results["BitvenusBP5V"]
    BitvenusAP5 = results["BitvenusAP5"]
    BitvenusAP5V = results["BitvenusAP5V"]
    BitvenusOBT = results["BitvenusOBT"]
    BitvenusLTP = results["BitvenusLTP"]

    # Biconomy
    BiconomyBP5 = results["BiconomyBP5"]
    BiconomyBP5V = results["BiconomyBP5V"]
    BiconomyAP5 = results["BiconomyAP5"]
    BiconomyAP5V = results["BiconomyAP5V"]
    BiconomyOBT = results["BiconomyOBT"]
    BiconomyLTP = results["BiconomyLTP"]

    # XT
    XTBP5 = results["XTBP5"]
    XTBP5V = results["XTBP5V"]
    XTAP5 = results["XTAP5"]
    XTAP5V = results["XTAP5V"]
    XTOBT = results["XTOBT"]
    XTLTP = results["XTLTP"]

    # Bitflyer
    BitflyerBP5 = results["BitflyerBP5"]
    BitflyerBP5V = results["BitflyerBP5V"]
    BitflyerAP5 = results["BitflyerAP5"]
    BitflyerAP5V = results["BitflyerAP5V"]
    BitflyerOBT = results["BitflyerOBT"]
    BitflyerLTP = results["BitflyerLTP"]

    # CoinW
    CoinWBP5 = results["CoinWBP5"]
    CoinWBP5V = results["CoinWBP5V"]
    CoinWAP5 = results["CoinWAP5"]
    CoinWAP5V = results["CoinWAP5V"]
    CoinWOBT = results["CoinWOBT"]
    CoinWLTP = results["CoinWLTP"]

    # Toobit
    ToobitBP5 = results["ToobitBP5"]
    ToobitBP5V = results["ToobitBP5V"]
    ToobitAP5 = results["ToobitAP5"]
    ToobitAP5V = results["ToobitAP5V"]
    ToobitOBT = results["ToobitOBT"]
    ToobitLTP = results["ToobitLTP"]

    # TapBit
    TapbitBP5 = results["TapBitBP5"]
    TapbitBP5V = results["TapBitBP5V"]
    TapbitAP5 = results["TapBitAP5"]
    TapbitAP5V = results["TapBitAP5V"]
    TapbitOBT = results["TapBitOBT"]
    TapbitLTP = results["TapBitLTP"]

    Binance_Status = results['Binance_Status']
    BybitStatus = results['Bybit_Status']
    OKX_Status = results['OKX_Status']
    Upbit_Status = results['Upbit_Status']
    Kucoin_Status = results['Kucoin_Status']
    Bitget_Status = results['Bitget_Status']
    Bitstamp_Status = results['Bitstamp_Status']
    Gemini_Status = results['Gemini_Status']
    Kraken_Status = results['Kraken_Status']
    Gateio_Status = results['Gateio_Status']
    HTX_Status = results['HTX_Status']
    MEXC_Status = results['MEXC_Status']
    Lbank_Status = results['Lbank_Status']
    Bitmart_Status = results['Bitmart_Status']
    Deepcoin_Status = results['Deepcoin_Status']
    Bitfinex_Status = results['Bitfinex_Status']
    BingX_Status = results['BingX_Status']
    OrangeX_Status = results['OrangeX_Status']
    Bitvenus_Status = results['Bitvenus_Status']
    Biconomy_Status = results['Biconomy_Status']
    XT_Status = results['XT_Status']
    Bitflyer_Status = results['Bitflyer_Status']
    CoinW_Status = results['CoinW_Status']
    Toobit_Status = results['Toobit_Status']
    TapBit_Status = results['TapBit_Status']

    bid_prices = {
        "Binance": BinanceBP5,
        "Bybit": BybitBP5,
        "OKX": OKXBP5,
        "Upbit": UpbitBP5,
        "Kucoin": KucoinBP5,
        "Bitget": BitgetBP5,
        "Bitstamp": BitstampBP5,
        "Gemini": GeminiBP5,
        "Kraken": KrakenBP5,
        "Gate.io": GateioBP5,
        "HTX": HTXBP5,
        "MEXC": MEXCBP5,
        "Lbank": LbankBP5,
        "Bitmart": BitmartBP5,
        "Deepcoin": DeepcoinBP5,
        "Bitfinex": BitfinexBP5,
        "BingX": BingXBP5,
        "OrangeX": OrangeXBP5,
        "Bitvenus": BitvenusBP5,
        "Biconomy": BiconomyBP5,
        "XT": XTBP5,
        "Bitflyer": BitflyerBP5,
        "CoinW": CoinWBP5,
        "Toobit": ToobitBP5,
        "TapBit": TapbitBP5
    }

    ask_prices = {
        "Binance": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bybit": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "OKX": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Upbit": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Kucoin": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitget": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitstamp": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Gemini": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Kraken": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Gate.io": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "HTX": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "MEXC": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Lbank": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitmart": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Deepcoin": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitfinex": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "BingX": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "OrangeX": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitvenus": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Biconomy": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "XT": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Bitflyer": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "CoinW": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "Toobit": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        },
        "TapBit": {
            "Binance": BinanceAP5,
            "Bybit": BybitAP5,
            "OKX": OKXAP5,
            "Upbit": UpbitAP5,
            "Kucoin": KucoinAP5,
            "Bitget": BitgetAP5,
            "Bitstamp": BitstampAP5,
            "Gemini": GeminiAP5,
            "Kraken": KrakenAP5,
            "Gate.io": GateioAP5,
            "HTX": HTXAP5,
            "MEXC": MEXCAP5,
            "Lbank": LbankAP5,
            "Bitmart": BitmartAP5,
            "Deepcoin": DeepcoinAP5,
            "Bitfinex": BitfinexAP5,
            "BingX": BingXAP5,
            "OrangeX": OrangeXAP5,
            "Bitvenus": BitvenusAP5,
            "Biconomy": BiconomyAP5,
            "XT": XTAP5,
            "Bitflyer": BitflyerAP5,
            "CoinW": CoinWAP5,
            "Toobit": ToobitAP5,
            "TapBit": TapbitAP5
        }
    }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect differences from all exchanges
    all_differences = {}
    for exchange in exchanges:
        all_differences.update(exchange.get_differences())

    results = {}
    for key, value in all_differences.items():
        results[key] = value

    # Print stored variables
    for key in sorted(results.keys()):
        results[key]

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_Gate.ioAP']
    BinanceBP_HTXAP = results['BinanceBP_HTXAP']
    BinanceBP_MEXCAP = results['BinanceBP_MEXCAP']
    BinanceBP_LbankAP = results['BinanceBP_LbankAP']
    BinanceBP_BitmartAP = results['BinanceBP_BitmartAP']
    BinanceBP_DeepcoinAP = results['BinanceBP_DeepcoinAP']
    BinanceBP_BitfinexAP = results['BinanceBP_BitfinexAP']
    BinanceBP_BingXAP = results['BinanceBP_BingXAP']
    BinanceBP_OrangeXAP = results['BinanceBP_OrangeXAP']
    BinanceBP_BitvenusAP = results['BinanceBP_BitvenusAP']
    BinanceBP_BiconomyAP = results['BinanceBP_BiconomyAP']
    BinanceBP_XTAP = results['BinanceBP_XTAP']
    BinanceBP_BitflyerAP = results['BinanceBP_BitflyerAP']
    BinanceBP_CoinWAP = results['BinanceBP_CoinWAP']
    BinanceBP_ToobitAP = results['BinanceBP_ToobitAP']
    BinanceBP_TapBitAP = results['BinanceBP_TapBitAP']

    BybitBP_BinanceAP = results['BybitBP_BinanceAP']
    BybitBP_BybitAP = results['BybitBP_BybitAP']
    BybitBP_OKXAP = results['BybitBP_OKXAP']
    BybitBP_UpbitAP = results['BybitBP_UpbitAP']
    BybitBP_KucoinAP = results['BybitBP_KucoinAP']
    BybitBP_BitgetAP = results['BybitBP_BitgetAP']
    BybitBP_BitstampAP = results['BybitBP_BitstampAP']
    BybitBP_GeminiAP = results['BybitBP_GeminiAP']
    BybitBP_KrakenAP = results['BybitBP_KrakenAP']
    BybitBP_GateioAP = results['BybitBP_Gate.ioAP']
    BybitBP_HTXAP = results['BybitBP_HTXAP']
    BybitBP_MEXCAP = results['BybitBP_MEXCAP']
    BybitBP_LbankAP = results['BybitBP_LbankAP']
    BybitBP_BitmartAP = results['BybitBP_BitmartAP']
    BybitBP_DeepcoinAP = results['BybitBP_DeepcoinAP']
    BybitBP_BitfinexAP = results['BybitBP_BitfinexAP']
    BybitBP_BingXAP = results['BybitBP_BingXAP']
    BybitBP_OrangeXAP = results['BybitBP_OrangeXAP']
    BybitBP_BitvenusAP = results['BybitBP_BitvenusAP']
    BybitBP_BiconomyAP = results['BybitBP_BiconomyAP']
    BybitBP_XTAP = results['BybitBP_XTAP']
    BybitBP_BitflyerAP = results['BybitBP_BitflyerAP']
    BybitBP_CoinWAP = results['BybitBP_CoinWAP']
    BybitBP_ToobitAP = results['BybitBP_ToobitAP']
    BybitBP_TapBitAP = results['BybitBP_TapBitAP']

    OKXBP_BinanceAP = results['OKXBP_BinanceAP']
    OKXBP_BybitAP = results['OKXBP_BybitAP']
    OKXBP_OKXAP = results['OKXBP_OKXAP']
    OKXBP_UpbitAP = results['OKXBP_UpbitAP']
    OKXBP_KucoinAP = results['OKXBP_KucoinAP']
    OKXBP_BitgetAP = results['OKXBP_BitgetAP']
    OKXBP_BitstampAP = results['OKXBP_BitstampAP']
    OKXBP_GeminiAP = results['OKXBP_GeminiAP']
    OKXBP_KrakenAP = results['OKXBP_KrakenAP']
    OKXBP_GateioAP = results['OKXBP_Gate.ioAP']
    OKXBP_HTXAP = results['OKXBP_HTXAP']
    OKXBP_MEXCAP = results['OKXBP_MEXCAP']
    OKXBP_LbankAP = results['OKXBP_LbankAP']
    OKXBP_BitmartAP = results['OKXBP_BitmartAP']
    OKXBP_DeepcoinAP = results['OKXBP_DeepcoinAP']
    OKXBP_BitfinexAP = results['OKXBP_BitfinexAP']
    OKXBP_BingXAP = results['OKXBP_BingXAP']
    OKXBP_OrangeXAP = results['OKXBP_OrangeXAP']
    OKXBP_BitvenusAP = results['OKXBP_BitvenusAP']
    OKXBP_BiconomyAP = results['OKXBP_BiconomyAP']
    OKXBP_XTAP = results['OKXBP_XTAP']
    OKXBP_BitflyerAP = results['OKXBP_BitflyerAP']
    OKXBP_CoinWAP = results['OKXBP_CoinWAP']
    OKXBP_ToobitAP = results['OKXBP_ToobitAP']
    OKXBP_TapBitAP = results['OKXBP_TapBitAP']

    UpbitBP_BinanceAP = results['UpbitBP_BinanceAP']
    UpbitBP_BybitAP = results['UpbitBP_BybitAP']
    UpbitBP_OKXAP = results['UpbitBP_OKXAP']
    UpbitBP_UpbitAP = results['UpbitBP_UpbitAP']
    UpbitBP_KucoinAP = results['UpbitBP_KucoinAP']
    UpbitBP_BitgetAP = results['UpbitBP_BitgetAP']
    UpbitBP_BitstampAP = results['UpbitBP_BitstampAP']
    UpbitBP_GeminiAP = results['UpbitBP_GeminiAP']
    UpbitBP_KrakenAP = results['UpbitBP_KrakenAP']
    UpbitBP_GateioAP = results['UpbitBP_Gate.ioAP']
    UpbitBP_HTXAP = results['UpbitBP_HTXAP']
    UpbitBP_MEXCAP = results['UpbitBP_MEXCAP']
    UpbitBP_LbankAP = results['UpbitBP_LbankAP']
    UpbitBP_BitmartAP = results['UpbitBP_BitmartAP']
    UpbitBP_DeepcoinAP = results['UpbitBP_DeepcoinAP']
    UpbitBP_BitfinexAP = results['UpbitBP_BitfinexAP']
    UpbitBP_BingXAP = results['UpbitBP_BingXAP']
    UpbitBP_OrangeXAP = results['UpbitBP_OrangeXAP']
    UpbitBP_BitvenusAP = results['UpbitBP_BitvenusAP']
    UpbitBP_BiconomyAP = results['UpbitBP_BiconomyAP']
    UpbitBP_XTAP = results['UpbitBP_XTAP']
    UpbitBP_BitflyerAP = results['UpbitBP_BitflyerAP']
    UpbitBP_CoinWAP = results['UpbitBP_CoinWAP']
    UpbitBP_ToobitAP = results['UpbitBP_ToobitAP']
    UpbitBP_TapBitAP = results['UpbitBP_TapBitAP']

    KucoinBP_BinanceAP = results['KucoinBP_BinanceAP']
    KucoinBP_BybitAP = results['KucoinBP_BybitAP']
    KucoinBP_OKXAP = results['KucoinBP_OKXAP']
    KucoinBP_UpbitAP = results['KucoinBP_UpbitAP']
    KucoinBP_KucoinAP = results['KucoinBP_KucoinAP']
    KucoinBP_BitgetAP = results['KucoinBP_BitgetAP']
    KucoinBP_BitstampAP = results['KucoinBP_BitstampAP']
    KucoinBP_GeminiAP = results['KucoinBP_GeminiAP']
    KucoinBP_KrakenAP = results['KucoinBP_KrakenAP']
    KucoinBP_GateioAP = results['KucoinBP_Gate.ioAP']
    KucoinBP_HTXAP = results['KucoinBP_HTXAP']
    KucoinBP_MEXCAP = results['KucoinBP_MEXCAP']
    KucoinBP_LbankAP = results['KucoinBP_LbankAP']
    KucoinBP_BitmartAP = results['KucoinBP_BitmartAP']
    KucoinBP_DeepcoinAP = results['KucoinBP_DeepcoinAP']
    KucoinBP_BitfinexAP = results['KucoinBP_BitfinexAP']
    KucoinBP_BingXAP = results['KucoinBP_BingXAP']
    KucoinBP_OrangeXAP = results['KucoinBP_OrangeXAP']
    KucoinBP_BitvenusAP = results['KucoinBP_BitvenusAP']
    KucoinBP_BiconomyAP = results['KucoinBP_BiconomyAP']
    KucoinBP_XTAP = results['KucoinBP_XTAP']
    KucoinBP_BitflyerAP = results['KucoinBP_BitflyerAP']
    KucoinBP_CoinWAP = results['KucoinBP_CoinWAP']
    KucoinBP_ToobitAP = results['KucoinBP_ToobitAP']
    KucoinBP_TapBitAP = results['KucoinBP_TapBitAP']

    BitgetBP_BinanceAP = results['BitgetBP_BinanceAP']
    BitgetBP_BybitAP = results['BitgetBP_BybitAP']
    BitgetBP_OKXAP = results['BitgetBP_OKXAP']
    BitgetBP_UpbitAP = results['BitgetBP_UpbitAP']
    BitgetBP_KucoinAP = results['BitgetBP_KucoinAP']
    BitgetBP_BitgetAP = results['BitgetBP_BitgetAP']
    BitgetBP_BitstampAP = results['BitgetBP_BitstampAP']
    BitgetBP_GeminiAP = results['BitgetBP_GeminiAP']
    BitgetBP_KrakenAP = results['BitgetBP_KrakenAP']
    BitgetBP_GateioAP = results['BitgetBP_Gate.ioAP']
    BitgetBP_HTXAP = results['BitgetBP_HTXAP']
    BitgetBP_MEXCAP = results['BitgetBP_MEXCAP']
    BitgetBP_LbankAP = results['BitgetBP_LbankAP']
    BitgetBP_BitmartAP = results['BitgetBP_BitmartAP']
    BitgetBP_DeepcoinAP = results['BitgetBP_DeepcoinAP']
    BitgetBP_BitfinexAP = results['BitgetBP_BitfinexAP']
    BitgetBP_BingXAP = results['BitgetBP_BingXAP']
    BitgetBP_OrangeXAP = results['BitgetBP_OrangeXAP']
    BitgetBP_BitvenusAP = results['BitgetBP_BitvenusAP']
    BitgetBP_BiconomyAP = results['BitgetBP_BiconomyAP']
    BitgetBP_XTAP = results['BitgetBP_XTAP']
    BitgetBP_BitflyerAP = results['BitgetBP_BitflyerAP']
    BitgetBP_CoinWAP = results['BitgetBP_CoinWAP']
    BitgetBP_ToobitAP = results['BitgetBP_ToobitAP']
    BitgetBP_TapBitAP = results['BitgetBP_TapBitAP']

    BitstampBP_BinanceAP = results['BitstampBP_BinanceAP']
    BitstampBP_BybitAP = results['BitstampBP_BybitAP']
    BitstampBP_OKXAP = results['BitstampBP_OKXAP']
    BitstampBP_UpbitAP = results['BitstampBP_UpbitAP']
    BitstampBP_KucoinAP = results['BitstampBP_KucoinAP']
    BitstampBP_BitgetAP = results['BitstampBP_BitgetAP']
    BitstampBP_BitstampAP = results['BitstampBP_BitstampAP']
    BitstampBP_GeminiAP = results['BitstampBP_GeminiAP']
    BitstampBP_KrakenAP = results['BitstampBP_KrakenAP']
    BitstampBP_GateioAP = results['BitstampBP_Gate.ioAP']
    BitstampBP_HTXAP = results['BitstampBP_HTXAP']
    BitstampBP_MEXCAP = results['BitstampBP_MEXCAP']
    BitstampBP_LbankAP = results['BitstampBP_LbankAP']
    BitstampBP_BitmartAP = results['BitstampBP_BitmartAP']
    BitstampBP_DeepcoinAP = results['BitstampBP_DeepcoinAP']
    BitstampBP_BitfinexAP = results['BitstampBP_BitfinexAP']
    BitstampBP_BingXAP = results['BitstampBP_BingXAP']
    BitstampBP_OrangeXAP = results['BitstampBP_OrangeXAP']
    BitstampBP_BitvenusAP = results['BitstampBP_BitvenusAP']
    BitstampBP_BiconomyAP = results['BitstampBP_BiconomyAP']
    BitstampBP_XTAP = results['BitstampBP_XTAP']
    BitstampBP_BitflyerAP = results['BitstampBP_BitflyerAP']
    BitstampBP_CoinWAP = results['BitstampBP_CoinWAP']
    BitstampBP_ToobitAP = results['BitstampBP_ToobitAP']
    BitstampBP_TapBitAP = results['BitstampBP_TapBitAP']

    GeminiBP_BinanceAP = results['GeminiBP_BinanceAP']
    GeminiBP_BybitAP = results['GeminiBP_BybitAP']
    GeminiBP_OKXAP = results['GeminiBP_OKXAP']
    GeminiBP_UpbitAP = results['GeminiBP_UpbitAP']
    GeminiBP_KucoinAP = results['GeminiBP_KucoinAP']
    GeminiBP_BitgetAP = results['GeminiBP_BitgetAP']
    GeminiBP_BitstampAP = results['GeminiBP_BitstampAP']
    GeminiBP_GeminiAP = results['GeminiBP_GeminiAP']
    GeminiBP_KrakenAP = results['GeminiBP_KrakenAP']
    GeminiBP_GateioAP = results['GeminiBP_Gate.ioAP']
    GeminiBP_HTXAP = results['GeminiBP_HTXAP']
    GeminiBP_MEXCAP = results['GeminiBP_MEXCAP']
    GeminiBP_LbankAP = results['GeminiBP_LbankAP']
    GeminiBP_BitmartAP = results['GeminiBP_BitmartAP']
    GeminiBP_DeepcoinAP = results['GeminiBP_DeepcoinAP']
    GeminiBP_BitfinexAP = results['GeminiBP_BitfinexAP']
    GeminiBP_BingXAP = results['GeminiBP_BingXAP']
    GeminiBP_OrangeXAP = results['GeminiBP_OrangeXAP']
    GeminiBP_BitvenusAP = results['GeminiBP_BitvenusAP']
    GeminiBP_BiconomyAP = results['GeminiBP_BiconomyAP']
    GeminiBP_XTAP = results['GeminiBP_XTAP']
    GeminiBP_BitflyerAP = results['GeminiBP_BitflyerAP']
    GeminiBP_CoinWAP = results['GeminiBP_CoinWAP']
    GeminiBP_ToobitAP = results['GeminiBP_ToobitAP']
    GeminiBP_TapBitAP = results['GeminiBP_TapBitAP']

    KrakenBP_BinanceAP = results['KrakenBP_BinanceAP']
    KrakenBP_BybitAP = results['KrakenBP_BybitAP']
    KrakenBP_OKXAP = results['KrakenBP_OKXAP']
    KrakenBP_UpbitAP = results['KrakenBP_UpbitAP']
    KrakenBP_KucoinAP = results['KrakenBP_KucoinAP']
    KrakenBP_BitgetAP = results['KrakenBP_BitgetAP']
    KrakenBP_BitstampAP = results['KrakenBP_BitstampAP']
    KrakenBP_GeminiAP = results['KrakenBP_GeminiAP']
    KrakenBP_KrakenAP = results['KrakenBP_KrakenAP']
    KrakenBP_GateioAP = results['KrakenBP_Gate.ioAP']
    KrakenBP_HTXAP = results['KrakenBP_HTXAP']
    KrakenBP_MEXCAP = results['KrakenBP_MEXCAP']
    KrakenBP_LbankAP = results['KrakenBP_LbankAP']
    KrakenBP_BitmartAP = results['KrakenBP_BitmartAP']
    KrakenBP_DeepcoinAP = results['KrakenBP_DeepcoinAP']
    KrakenBP_BitfinexAP = results['KrakenBP_BitfinexAP']
    KrakenBP_BingXAP = results['KrakenBP_BingXAP']
    KrakenBP_OrangeXAP = results['KrakenBP_OrangeXAP']
    KrakenBP_BitvenusAP = results['KrakenBP_BitvenusAP']
    KrakenBP_BiconomyAP = results['KrakenBP_BiconomyAP']
    KrakenBP_XTAP = results['KrakenBP_XTAP']
    KrakenBP_BitflyerAP = results['KrakenBP_BitflyerAP']
    KrakenBP_CoinWAP = results['KrakenBP_CoinWAP']
    KrakenBP_ToobitAP = results['KrakenBP_ToobitAP']
    KrakenBP_TapBitAP = results['KrakenBP_TapBitAP']

    GateioBP_BinanceAP = results['Gate.ioBP_BinanceAP']
    GateioBP_BybitAP = results['Gate.ioBP_BybitAP']
    GateioBP_OKXAP = results['Gate.ioBP_OKXAP']
    GateioBP_UpbitAP = results['Gate.ioBP_UpbitAP']
    GateioBP_KucoinAP = results['Gate.ioBP_KucoinAP']
    GateioBP_BitgetAP = results['Gate.ioBP_BitgetAP']
    GateioBP_BitstampAP = results['Gate.ioBP_BitstampAP']
    GateioBP_GeminiAP = results['Gate.ioBP_GeminiAP']
    GateioBP_KrakenAP = results['Gate.ioBP_KrakenAP']
    GateioBP_GateioAP = results['Gate.ioBP_Gate.ioAP']
    GateioBP_HTXAP = results['Gate.ioBP_HTXAP']
    GateioBP_MEXCAP = results['Gate.ioBP_MEXCAP']
    GateioBP_LbankAP = results['Gate.ioBP_LbankAP']
    GateioBP_BitmartAP = results['Gate.ioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['Gate.ioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['Gate.ioBP_BitfinexAP']
    GateioBP_BingXAP = results['Gate.ioBP_BingXAP']
    GateioBP_OrangeXAP = results['Gate.ioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['Gate.ioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['Gate.ioBP_BiconomyAP']
    GateioBP_XTAP = results['Gate.ioBP_XTAP']
    GateioBP_BitflyerAP = results['Gate.ioBP_BitflyerAP']
    GateioBP_CoinWAP = results['Gate.ioBP_CoinWAP']
    GateioBP_ToobitAP = results['Gate.ioBP_ToobitAP']
    GateioBP_TapBitAP = results['Gate.ioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_Gate.ioAP']
    HTXBP_HTXAP = results['HTXBP_HTXAP']
    HTXBP_MEXCAP = results['HTXBP_MEXCAP']
    HTXBP_LbankAP = results['HTXBP_LbankAP']
    HTXBP_BitmartAP = results['HTXBP_BitmartAP']
    HTXBP_DeepcoinAP = results['HTXBP_DeepcoinAP']
    HTXBP_BitfinexAP = results['HTXBP_BitfinexAP']
    HTXBP_BingXAP = results['HTXBP_BingXAP']
    HTXBP_OrangeXAP = results['HTXBP_OrangeXAP']
    HTXBP_BitvenusAP = results['HTXBP_BitvenusAP']
    HTXBP_BiconomyAP = results['HTXBP_BiconomyAP']
    HTXBP_XTAP = results['HTXBP_XTAP']
    HTXBP_BitflyerAP = results['HTXBP_BitflyerAP']
    HTXBP_CoinWAP = results['HTXBP_CoinWAP']
    HTXBP_ToobitAP = results['HTXBP_ToobitAP']
    HTXBP_TapBitAP = results['HTXBP_TapBitAP']

    MEXCBP_BinanceAP = results['MEXCBP_BinanceAP']
    MEXCBP_BybitAP = results['MEXCBP_BybitAP']
    MEXCBP_OKXAP = results['MEXCBP_OKXAP']
    MEXCBP_UpbitAP = results['MEXCBP_UpbitAP']
    MEXCBP_KucoinAP = results['MEXCBP_KucoinAP']
    MEXCBP_BitgetAP = results['MEXCBP_BitgetAP']
    MEXCBP_BitstampAP = results['MEXCBP_BitstampAP']
    MEXCBP_GeminiAP = results['MEXCBP_GeminiAP']
    MEXCBP_KrakenAP = results['MEXCBP_KrakenAP']
    MEXCBP_GateioAP = results['BinanceBP_Gate.ioAP']
    MEXCBP_HTXAP = results['MEXCBP_HTXAP']
    MEXCBP_MEXCAP = results['MEXCBP_MEXCAP']
    MEXCBP_LbankAP = results['MEXCBP_LbankAP']
    MEXCBP_BitmartAP = results['MEXCBP_BitmartAP']
    MEXCBP_DeepcoinAP = results['MEXCBP_DeepcoinAP']
    MEXCBP_BitfinexAP = results['MEXCBP_BitfinexAP']
    MEXCBP_BingXAP = results['MEXCBP_BingXAP']
    MEXCBP_OrangeXAP = results['MEXCBP_OrangeXAP']
    MEXCBP_BitvenusAP = results['MEXCBP_BitvenusAP']
    MEXCBP_BiconomyAP = results['MEXCBP_BiconomyAP']
    MEXCBP_XTAP = results['MEXCBP_XTAP']
    MEXCBP_BitflyerAP = results['MEXCBP_BitflyerAP']
    MEXCBP_CoinWAP = results['MEXCBP_CoinWAP']
    MEXCBP_ToobitAP = results['MEXCBP_ToobitAP']
    MEXCBP_TapBitAP = results['MEXCBP_TapBitAP']

    LbankBP_BinanceAP = results['LbankBP_BinanceAP']
    LbankBP_BybitAP = results['LbankBP_BybitAP']
    LbankBP_OKXAP = results['LbankBP_OKXAP']
    LbankBP_UpbitAP = results['LbankBP_UpbitAP']
    LbankBP_KucoinAP = results['LbankBP_KucoinAP']
    LbankBP_BitgetAP = results['LbankBP_BitgetAP']
    LbankBP_BitstampAP = results['LbankBP_BitstampAP']
    LbankBP_GeminiAP = results['LbankBP_GeminiAP']
    LbankBP_KrakenAP = results['LbankBP_KrakenAP']
    LbankBP_GateioAP = results['LbankBP_Gate.ioAP']
    LbankBP_HTXAP = results['LbankBP_HTXAP']
    LbankBP_MEXCAP = results['LbankBP_MEXCAP']
    LbankBP_LbankAP = results['LbankBP_LbankAP']
    LbankBP_BitmartAP = results['LbankBP_BitmartAP']
    LbankBP_DeepcoinAP = results['LbankBP_DeepcoinAP']
    LbankBP_BitfinexAP = results['LbankBP_BitfinexAP']
    LbankBP_BingXAP = results['LbankBP_BingXAP']
    LbankBP_OrangeXAP = results['LbankBP_OrangeXAP']
    LbankBP_BitvenusAP = results['LbankBP_BitvenusAP']
    LbankBP_BiconomyAP = results['LbankBP_BiconomyAP']
    LbankBP_XTAP = results['LbankBP_XTAP']
    LbankBP_BitflyerAP = results['LbankBP_BitflyerAP']
    LbankBP_CoinWAP = results['LbankBP_CoinWAP']
    LbankBP_ToobitAP = results['LbankBP_ToobitAP']
    LbankBP_TapBitAP = results['LbankBP_TapBitAP']

    BitmartBP_BinanceAP = results['BitmartBP_BinanceAP']
    BitmartBP_BybitAP = results['BitmartBP_BybitAP']
    BitmartBP_OKXAP = results['BitmartBP_OKXAP']
    BitmartBP_UpbitAP = results['BitmartBP_UpbitAP']
    BitmartBP_KucoinAP = results['BitmartBP_KucoinAP']
    BitmartBP_BitgetAP = results['BitmartBP_BitgetAP']
    BitmartBP_BitstampAP = results['BitmartBP_BitstampAP']
    BitmartBP_GeminiAP = results['BitmartBP_GeminiAP']
    BitmartBP_KrakenAP = results['BitmartBP_KrakenAP']
    BitmartBP_GateioAP = results['BitmartBP_Gate.ioAP']
    BitmartBP_HTXAP = results['BitmartBP_HTXAP']
    BitmartBP_MEXCAP = results['BitmartBP_MEXCAP']
    BitmartBP_LbankAP = results['BitmartBP_LbankAP']
    BitmartBP_BitmartAP = results['BitmartBP_BitmartAP']
    BitmartBP_DeepcoinAP = results['BitmartBP_DeepcoinAP']
    BitmartBP_BitfinexAP = results['BitmartBP_BitfinexAP']
    BitmartBP_BingXAP = results['BitmartBP_BingXAP']
    BitmartBP_OrangeXAP = results['BitmartBP_OrangeXAP']
    BitmartBP_BitvenusAP = results['BitmartBP_BitvenusAP']
    BitmartBP_BiconomyAP = results['BitmartBP_BiconomyAP']
    BitmartBP_XTAP = results['BitmartBP_XTAP']
    BitmartBP_BitflyerAP = results['BitmartBP_BitflyerAP']
    BitmartBP_CoinWAP = results['BitmartBP_CoinWAP']
    BitmartBP_ToobitAP = results['BitmartBP_ToobitAP']
    BitmartBP_TapBitAP = results['BitmartBP_TapBitAP']

    DeepcoinBP_BinanceAP = results['DeepcoinBP_BinanceAP']
    DeepcoinBP_BybitAP = results['DeepcoinBP_BybitAP']
    DeepcoinBP_OKXAP = results['DeepcoinBP_OKXAP']
    DeepcoinBP_UpbitAP = results['DeepcoinBP_UpbitAP']
    DeepcoinBP_KucoinAP = results['DeepcoinBP_KucoinAP']
    DeepcoinBP_BitgetAP = results['DeepcoinBP_BitgetAP']
    DeepcoinBP_BitstampAP = results['DeepcoinBP_BitstampAP']
    DeepcoinBP_GeminiAP = results['DeepcoinBP_GeminiAP']
    DeepcoinBP_KrakenAP = results['DeepcoinBP_KrakenAP']
    DeepcoinBP_GateioAP = results['DeepcoinBP_Gate.ioAP']
    DeepcoinBP_HTXAP = results['DeepcoinBP_HTXAP']
    DeepcoinBP_MEXCAP = results['DeepcoinBP_MEXCAP']
    DeepcoinBP_LbankAP = results['DeepcoinBP_LbankAP']
    DeepcoinBP_BitmartAP = results['DeepcoinBP_BitmartAP']
    DeepcoinBP_DeepcoinAP = results['DeepcoinBP_DeepcoinAP']
    DeepcoinBP_BitfinexAP = results['DeepcoinBP_BitfinexAP']
    DeepcoinBP_BingXAP = results['DeepcoinBP_BingXAP']
    DeepcoinBP_OrangeXAP = results['DeepcoinBP_OrangeXAP']
    DeepcoinBP_BitvenusAP = results['DeepcoinBP_BitvenusAP']
    DeepcoinBP_BiconomyAP = results['DeepcoinBP_BiconomyAP']
    DeepcoinBP_XTAP = results['DeepcoinBP_XTAP']
    DeepcoinBP_BitflyerAP = results['DeepcoinBP_BitflyerAP']
    DeepcoinBP_CoinWAP = results['DeepcoinBP_CoinWAP']
    DeepcoinBP_ToobitAP = results['DeepcoinBP_ToobitAP']
    DeepcoinBP_TapBitAP = results['DeepcoinBP_TapBitAP']

    BitfinexBP_BinanceAP = results['BitfinexBP_BinanceAP']
    BitfinexBP_BybitAP = results['BitfinexBP_BybitAP']
    BitfinexBP_OKXAP = results['BitfinexBP_OKXAP']
    BitfinexBP_UpbitAP = results['BitfinexBP_UpbitAP']
    BitfinexBP_KucoinAP = results['BitfinexBP_KucoinAP']
    BitfinexBP_BitgetAP = results['BitfinexBP_BitgetAP']
    BitfinexBP_BitstampAP = results['BitfinexBP_BitstampAP']
    BitfinexBP_GeminiAP = results['BitfinexBP_GeminiAP']
    BitfinexBP_KrakenAP = results['BitfinexBP_KrakenAP']
    BitfinexBP_GateioAP = results['BitfinexBP_Gate.ioAP']
    BitfinexBP_HTXAP = results['BitfinexBP_HTXAP']
    BitfinexBP_MEXCAP = results['BitfinexBP_MEXCAP']
    BitfinexBP_LbankAP = results['BitfinexBP_LbankAP']
    BitfinexBP_BitmartAP = results['BitfinexBP_BitmartAP']
    BitfinexBP_DeepcoinAP = results['BitfinexBP_DeepcoinAP']
    BitfinexBP_BitfinexAP = results['BitfinexBP_BitfinexAP']
    BitfinexBP_BingXAP = results['BitfinexBP_BingXAP']
    BitfinexBP_OrangeXAP = results['BitfinexBP_OrangeXAP']
    BitfinexBP_BitvenusAP = results['BitfinexBP_BitvenusAP']
    BitfinexBP_BiconomyAP = results['BitfinexBP_BiconomyAP']
    BitfinexBP_XTAP = results['BitfinexBP_XTAP']
    BitfinexBP_BitflyerAP = results['BitfinexBP_BitflyerAP']
    BitfinexBP_CoinWAP = results['BitfinexBP_CoinWAP']
    BitfinexBP_ToobitAP = results['BitfinexBP_ToobitAP']
    BitfinexBP_TapBitAP = results['BitfinexBP_TapBitAP']

    BingXBP_BinanceAP = results['BingXBP_BinanceAP']
    BingXBP_BybitAP = results['BingXBP_BybitAP']
    BingXBP_OKXAP = results['BingXBP_OKXAP']
    BingXBP_UpbitAP = results['BingXBP_UpbitAP']
    BingXBP_KucoinAP = results['BingXBP_KucoinAP']
    BingXBP_BitgetAP = results['BingXBP_BitgetAP']
    BingXBP_BitstampAP = results['BingXBP_BitstampAP']
    BingXBP_GeminiAP = results['BingXBP_GeminiAP']
    BingXBP_KrakenAP = results['BingXBP_KrakenAP']
    BingXBP_GateioAP = results['BingXBP_Gate.ioAP']
    BingXBP_HTXAP = results['BingXBP_HTXAP']
    BingXBP_MEXCAP = results['BingXBP_MEXCAP']
    BingXBP_LbankAP = results['BingXBP_LbankAP']
    BingXBP_BitmartAP = results['BingXBP_BitmartAP']
    BingXBP_DeepcoinAP = results['BingXBP_DeepcoinAP']
    BingXBP_BitfinexAP = results['BingXBP_BitfinexAP']
    BingXBP_BingXAP = results['BingXBP_BingXAP']
    BingXBP_OrangeXAP = results['BingXBP_OrangeXAP']
    BingXBP_BitvenusAP = results['BingXBP_BitvenusAP']
    BingXBP_BiconomyAP = results['BingXBP_BiconomyAP']
    BingXBP_XTAP = results['BingXBP_XTAP']
    BingXBP_BitflyerAP = results['BingXBP_BitflyerAP']
    BingXBP_CoinWAP = results['BingXBP_CoinWAP']
    BingXBP_ToobitAP = results['BingXBP_ToobitAP']
    BingXBP_TapBitAP = results['BingXBP_TapBitAP']

    OrangeXBP_BinanceAP = results['OrangeXBP_BinanceAP']
    OrangeXBP_BybitAP = results['OrangeXBP_BybitAP']
    OrangeXBP_OKXAP = results['OrangeXBP_OKXAP']
    OrangeXBP_UpbitAP = results['OrangeXBP_UpbitAP']
    OrangeXBP_KucoinAP = results['OrangeXBP_KucoinAP']
    OrangeXBP_BitgetAP = results['OrangeXBP_BitgetAP']
    OrangeXBP_BitstampAP = results['OrangeXBP_BitstampAP']
    OrangeXBP_GeminiAP = results['OrangeXBP_GeminiAP']
    OrangeXBP_KrakenAP = results['OrangeXBP_KrakenAP']
    OrangeXBP_GateioAP = results['OrangeXBP_Gate.ioAP']
    OrangeXBP_HTXAP = results['OrangeXBP_HTXAP']
    OrangeXBP_MEXCAP = results['OrangeXBP_MEXCAP']
    OrangeXBP_LbankAP = results['OrangeXBP_LbankAP']
    OrangeXBP_BitmartAP = results['OrangeXBP_BitmartAP']
    OrangeXBP_DeepcoinAP = results['OrangeXBP_DeepcoinAP']
    OrangeXBP_BitfinexAP = results['OrangeXBP_BitfinexAP']
    OrangeXBP_BingXAP = results['OrangeXBP_BingXAP']
    OrangeXBP_OrangeXAP = results['OrangeXBP_OrangeXAP']
    OrangeXBP_BitvenusAP = results['OrangeXBP_BitvenusAP']
    OrangeXBP_BiconomyAP = results['OrangeXBP_BiconomyAP']
    OrangeXBP_XTAP = results['OrangeXBP_XTAP']
    OrangeXBP_BitflyerAP = results['OrangeXBP_BitflyerAP']
    OrangeXBP_CoinWAP = results['OrangeXBP_CoinWAP']
    OrangeXBP_ToobitAP = results['OrangeXBP_ToobitAP']
    OrangeXBP_TapBitAP = results['OrangeXBP_TapBitAP']

    BitvenusBP_BinanceAP = results['BitvenusBP_BinanceAP']
    BitvenusBP_BybitAP = results['BitvenusBP_BybitAP']
    BitvenusBP_OKXAP = results['BitvenusBP_OKXAP']
    BitvenusBP_UpbitAP = results['BitvenusBP_UpbitAP']
    BitvenusBP_KucoinAP = results['BitvenusBP_KucoinAP']
    BitvenusBP_BitgetAP = results['BitvenusBP_BitgetAP']
    BitvenusBP_BitstampAP = results['BitvenusBP_BitstampAP']
    BitvenusBP_GeminiAP = results['BitvenusBP_GeminiAP']
    BitvenusBP_KrakenAP = results['BitvenusBP_KrakenAP']
    BitvenusBP_GateioAP = results['BitvenusBP_Gate.ioAP']
    BitvenusBP_HTXAP = results['BitvenusBP_HTXAP']
    BitvenusBP_MEXCAP = results['BitvenusBP_MEXCAP']
    BitvenusBP_LbankAP = results['BitvenusBP_LbankAP']
    BitvenusBP_BitmartAP = results['BitvenusBP_BitmartAP']
    BitvenusBP_DeepcoinAP = results['BitvenusBP_DeepcoinAP']
    BitvenusBP_BitfinexAP = results['BitvenusBP_BitfinexAP']
    BitvenusBP_BingXAP = results['BitvenusBP_BingXAP']
    BitvenusBP_OrangeXAP = results['BitvenusBP_OrangeXAP']
    BitvenusBP_BitvenusAP = results['BitvenusBP_BitvenusAP']
    BitvenusBP_BiconomyAP = results['BitvenusBP_BiconomyAP']
    BitvenusBP_XTAP = results['BitvenusBP_XTAP']
    BitvenusBP_BitflyerAP = results['BitvenusBP_BitflyerAP']
    BitvenusBP_CoinWAP = results['BitvenusBP_CoinWAP']
    BitvenusBP_ToobitAP = results['BitvenusBP_ToobitAP']
    BitvenusBP_TapBitAP = results['BitvenusBP_TapBitAP']

    BiconomyBP_BinanceAP = results['BiconomyBP_BinanceAP']
    BiconomyBP_BybitAP = results['BiconomyBP_BybitAP']
    BiconomyBP_OKXAP = results['BiconomyBP_OKXAP']
    BiconomyBP_UpbitAP = results['BiconomyBP_UpbitAP']
    BiconomyBP_KucoinAP = results['BiconomyBP_KucoinAP']
    BiconomyBP_BitgetAP = results['BiconomyBP_BitgetAP']
    BiconomyBP_BitstampAP = results['BiconomyBP_BitstampAP']
    BiconomyBP_GeminiAP = results['BiconomyBP_GeminiAP']
    BiconomyBP_KrakenAP = results['BiconomyBP_KrakenAP']
    BiconomyBP_GateioAP = results['BiconomyBP_Gate.ioAP']
    BiconomyBP_HTXAP = results['BiconomyBP_HTXAP']
    BiconomyBP_MEXCAP = results['BiconomyBP_MEXCAP']
    BiconomyBP_LbankAP = results['BiconomyBP_LbankAP']
    BiconomyBP_BitmartAP = results['BiconomyBP_BitmartAP']
    BiconomyBP_DeepcoinAP = results['BiconomyBP_DeepcoinAP']
    BiconomyBP_BitfinexAP = results['BiconomyBP_BitfinexAP']
    BiconomyBP_BingXAP = results['BiconomyBP_BingXAP']
    BiconomyBP_OrangeXAP = results['BiconomyBP_OrangeXAP']
    BiconomyBP_BitvenusAP = results['BiconomyBP_BitvenusAP']
    BiconomyBP_BiconomyAP = results['BiconomyBP_BiconomyAP']
    BiconomyBP_XTAP = results['BiconomyBP_XTAP']
    BiconomyBP_BitflyerAP = results['BiconomyBP_BitflyerAP']
    BiconomyBP_CoinWAP = results['BiconomyBP_CoinWAP']
    BiconomyBP_ToobitAP = results['BiconomyBP_ToobitAP']
    BiconomyBP_TapBitAP = results['BiconomyBP_TapBitAP']

    XTBP_BinanceAP = results['XTBP_BinanceAP']
    XTBP_BybitAP = results['XTBP_BybitAP']
    XTBP_OKXAP = results['XTBP_OKXAP']
    XTBP_UpbitAP = results['XTBP_UpbitAP']
    XTBP_KucoinAP = results['XTBP_KucoinAP']
    XTBP_BitgetAP = results['XTBP_BitgetAP']
    XTBP_BitstampAP = results['XTBP_BitstampAP']
    XTBP_GeminiAP = results['XTBP_GeminiAP']
    XTBP_KrakenAP = results['XTBP_KrakenAP']
    XTBP_GateioAP = results['XTBP_Gate.ioAP']
    XTBP_HTXAP = results['XTBP_HTXAP']
    XTBP_MEXCAP = results['XTBP_MEXCAP']
    XTBP_LbankAP = results['XTBP_LbankAP']
    XTBP_BitmartAP = results['XTBP_BitmartAP']
    XTBP_DeepcoinAP = results['XTBP_DeepcoinAP']
    XTBP_BitfinexAP = results['XTBP_BitfinexAP']
    XTBP_BingXAP = results['XTBP_BingXAP']
    XTBP_OrangeXAP = results['XTBP_OrangeXAP']
    XTBP_BitvenusAP = results['XTBP_BitvenusAP']
    XTBP_BiconomyAP = results['XTBP_BiconomyAP']
    XTBP_XTAP = results['XTBP_XTAP']
    XTBP_BitflyerAP = results['XTBP_BitflyerAP']
    XTBP_CoinWAP = results['XTBP_CoinWAP']
    XTBP_ToobitAP = results['XTBP_ToobitAP']
    XTBP_TapBitAP = results['XTBP_TapBitAP']

    BitflyerBP_BinanceAP = results['BitflyerBP_BinanceAP']
    BitflyerBP_BybitAP = results['BitflyerBP_BybitAP']
    BitflyerBP_OKXAP = results['BitflyerBP_OKXAP']
    BitflyerBP_UpbitAP = results['BitflyerBP_UpbitAP']
    BitflyerBP_KucoinAP = results['BitflyerBP_KucoinAP']
    BitflyerBP_BitgetAP = results['BitflyerBP_BitgetAP']
    BitflyerBP_BitstampAP = results['BitflyerBP_BitstampAP']
    BitflyerBP_GeminiAP = results['BitflyerBP_GeminiAP']
    BitflyerBP_KrakenAP = results['BitflyerBP_KrakenAP']
    BitflyerBP_GateioAP = results['BitflyerBP_Gate.ioAP']
    BitflyerBP_HTXAP = results['BitflyerBP_HTXAP']
    BitflyerBP_MEXCAP = results['BitflyerBP_MEXCAP']
    BitflyerBP_LbankAP = results['BitflyerBP_LbankAP']
    BitflyerBP_BitmartAP = results['BitflyerBP_BitmartAP']
    BitflyerBP_DeepcoinAP = results['BitflyerBP_DeepcoinAP']
    BitflyerBP_BitfinexAP = results['BitflyerBP_BitfinexAP']
    BitflyerBP_BingXAP = results['BitflyerBP_BingXAP']
    BitflyerBP_OrangeXAP = results['BitflyerBP_OrangeXAP']
    BitflyerBP_BitvenusAP = results['BitflyerBP_BitvenusAP']
    BitflyerBP_BiconomyAP = results['BitflyerBP_BiconomyAP']
    BitflyerBP_XTAP = results['BitflyerBP_XTAP']
    BitflyerBP_BitflyerAP = results['BitflyerBP_BitflyerAP']
    BitflyerBP_CoinWAP = results['BitflyerBP_CoinWAP']
    BitflyerBP_ToobitAP = results['BitflyerBP_ToobitAP']
    BitflyerBP_TapBitAP = results['BitflyerBP_TapBitAP']

    CoinWBP_BinanceAP = results['CoinWBP_BinanceAP']
    CoinWBP_BybitAP = results['CoinWBP_BybitAP']
    CoinWBP_OKXAP = results['CoinWBP_OKXAP']
    CoinWBP_UpbitAP = results['CoinWBP_UpbitAP']
    CoinWBP_KucoinAP = results['CoinWBP_KucoinAP']
    CoinWBP_BitgetAP = results['CoinWBP_BitgetAP']
    CoinWBP_BitstampAP = results['CoinWBP_BitstampAP']
    CoinWBP_GeminiAP = results['CoinWBP_GeminiAP']
    CoinWBP_KrakenAP = results['CoinWBP_KrakenAP']
    CoinWBP_GateioAP = results['CoinWBP_Gate.ioAP']
    CoinWBP_HTXAP = results['CoinWBP_HTXAP']
    CoinWBP_MEXCAP = results['CoinWBP_MEXCAP']
    CoinWBP_LbankAP = results['CoinWBP_LbankAP']
    CoinWBP_BitmartAP = results['CoinWBP_BitmartAP']
    CoinWBP_DeepcoinAP = results['CoinWBP_DeepcoinAP']
    CoinWBP_BitfinexAP = results['CoinWBP_BitfinexAP']
    CoinWBP_BingXAP = results['CoinWBP_BingXAP']
    CoinWBP_OrangeXAP = results['CoinWBP_OrangeXAP']
    CoinWBP_BitvenusAP = results['CoinWBP_BitvenusAP']
    CoinWBP_BiconomyAP = results['CoinWBP_BiconomyAP']
    CoinWBP_XTAP = results['CoinWBP_XTAP']
    CoinWBP_BitflyerAP = results['CoinWBP_BitflyerAP']
    CoinWBP_CoinWAP = results['CoinWBP_CoinWAP']
    CoinWBP_ToobitAP = results['CoinWBP_ToobitAP']
    CoinWBP_TapBitAP = results['CoinWBP_TapBitAP']

    ToobitBP_BinanceAP = results['ToobitBP_BinanceAP']
    ToobitBP_BybitAP = results['ToobitBP_BybitAP']
    ToobitBP_OKXAP = results['ToobitBP_OKXAP']
    ToobitBP_UpbitAP = results['ToobitBP_UpbitAP']
    ToobitBP_KucoinAP = results['ToobitBP_KucoinAP']
    ToobitBP_BitgetAP = results['ToobitBP_BitgetAP']
    ToobitBP_BitstampAP = results['ToobitBP_BitstampAP']
    ToobitBP_GeminiAP = results['ToobitBP_GeminiAP']
    ToobitBP_KrakenAP = results['ToobitBP_KrakenAP']
    ToobitBP_GateioAP = results['ToobitBP_Gate.ioAP']
    ToobitBP_HTXAP = results['ToobitBP_HTXAP']
    ToobitBP_MEXCAP = results['ToobitBP_MEXCAP']
    ToobitBP_LbankAP = results['ToobitBP_LbankAP']
    ToobitBP_BitmartAP = results['ToobitBP_BitmartAP']
    ToobitBP_DeepcoinAP = results['ToobitBP_DeepcoinAP']
    ToobitBP_BitfinexAP = results['ToobitBP_BitfinexAP']
    ToobitBP_BingXAP = results['ToobitBP_BingXAP']
    ToobitBP_OrangeXAP = results['ToobitBP_OrangeXAP']
    ToobitBP_BitvenusAP = results['ToobitBP_BitvenusAP']
    ToobitBP_BiconomyAP = results['ToobitBP_BiconomyAP']
    ToobitBP_XTAP = results['ToobitBP_XTAP']
    ToobitBP_BitflyerAP = results['ToobitBP_BitflyerAP']
    ToobitBP_CoinWAP = results['ToobitBP_CoinWAP']
    ToobitBP_ToobitAP = results['ToobitBP_ToobitAP']
    ToobitBP_TapBitAP = results['ToobitBP_TapBitAP']

    TapBitBP_BinanceAP = results['TapBitBP_BinanceAP']
    TapBitBP_BybitAP = results['TapBitBP_BybitAP']
    TapBitBP_OKXAP = results['TapBitBP_OKXAP']
    TapBitBP_UpbitAP = results['TapBitBP_UpbitAP']
    TapBitBP_KucoinAP = results['TapBitBP_KucoinAP']
    TapBitBP_BitgetAP = results['TapBitBP_BitgetAP']
    TapBitBP_BitstampAP = results['TapBitBP_BitstampAP']
    TapBitBP_GeminiAP = results['TapBitBP_GeminiAP']
    TapBitBP_KrakenAP = results['TapBitBP_KrakenAP']
    TapBitBP_GateioAP = results['TapBitBP_Gate.ioAP']
    TapBitBP_HTXAP = results['TapBitBP_HTXAP']
    TapBitBP_MEXCAP = results['TapBitBP_MEXCAP']
    TapBitBP_LbankAP = results['TapBitBP_LbankAP']
    TapBitBP_BitmartAP = results['TapBitBP_BitmartAP']
    TapBitBP_DeepcoinAP = results['TapBitBP_DeepcoinAP']
    TapBitBP_BitfinexAP = results['TapBitBP_BitfinexAP']
    TapBitBP_BingXAP = results['TapBitBP_BingXAP']
    TapBitBP_OrangeXAP = results['TapBitBP_OrangeXAP']
    TapBitBP_BitvenusAP = results['TapBitBP_BitvenusAP']
    TapBitBP_BiconomyAP = results['TapBitBP_BiconomyAP']
    TapBitBP_XTAP = results['TapBitBP_XTAP']
    TapBitBP_BitflyerAP = results['TapBitBP_BitflyerAP']
    TapBitBP_CoinWAP = results['TapBitBP_CoinWAP']
    TapBitBP_ToobitAP = results['TapBitBP_ToobitAP']
    TapBitBP_TapBitAP = results['TapBitBP_TapBitAP']

    end = time.perf_counter_ns()
    processingtime = (end - start)+inital_time




    # "Binance",BinanceLTP,BinanceAP1,BinanceAP1V,BinanceBP1,BinanceBP1V,
    def Buckets(Name, LTP, AP5, AP5V, BP5, BP5V, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11,
                sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19, sub20, sub21, sub22, sub23, sub24, sub25,
                Status):
        tasks = []
        with ThreadPoolExecutor() as executor:
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Binance", BinanceLTP, BinanceAP5,
                                BinanceAP5V, BinanceBP5, BinanceBP5V, processingtime, sub1, Status, Binance_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bybit", BybitLTP, BybitAP5,
                                BybitAP5V, BybitBP5, BybitBP5V, processingtime, sub2, Status, BybitStatus))
            tasks.append(
                executor.submit(checker, OKXOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "OKX", OKXLTP, OKXAP5, OKXAP5V,
                                OKXBP5, OKXBP5V, processingtime, sub3, Binance_Status, OKX_Status))
            tasks.append(
                executor.submit(checker, UpbitOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Upbit", UpbitLTP, UpbitAP5,
                                UpbitAP5V, UpbitBP5, UpbitBP5V, processingtime, sub4, Status, Upbit_Status))
            tasks.append(
                executor.submit(checker, KucoinOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Kucoin", KucoinLTP, KucoinAP5,
                                KucoinAP5V, KucoinBP5, KucoinBP5V, processingtime, sub5, Status, Kucoin_Status))
            tasks.append(
                executor.submit(checker, BitgetOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitget", BitgetLTP, BitgetAP5,
                                BitgetAP5V, BitgetBP5, BitgetBP5V, processingtime, sub6, Status, Bitget_Status))
            tasks.append(executor.submit(checker, BitstampOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitstamp", BitstampLTP,
                                         BitstampAP5, BitstampAP5V, BitstampBP5, BitstampBP5V, processingtime, sub7,
                                         Status, Bitstamp_Status))
            tasks.append(
                executor.submit(checker, KrakenOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Kraken", KrakenLTP, KrakenAP5,
                                KrakenAPV5, KrakenBP5, KrakenBPV5, processingtime, sub8, Status, Kraken_Status))
            tasks.append(
                executor.submit(checker, BybitOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Gate.io", GateioLTP, GateioAP5,
                                GateioAPV5, GateioBP5, GateioBPV5, processingtime, sub9, Status, Gateio_Status))
            tasks.append(
                executor.submit(checker, HTXOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "HTX", HTXLTP, HTXAP5, HTXAP5V,
                                HTXBP5, HTXBP5V, processingtime, sub10, Status, HTX_Status))
            tasks.append(
                executor.submit(checker, MEXCOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "MEXC", MEXCLTP, MEXCAP5, MEXCAP5V,
                                MEXCBP5, MEXCBP5V, processingtime, sub11, Status, MEXC_Status))
            tasks.append(
                executor.submit(checker, LbankOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Lbank", LbankLTP, LbankAP5,
                                LbankAP5V, LbankBP5, LbankBP5V, processingtime, sub12, Status, Lbank_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitmart", BitmartLTP, BitmartAP5,
                                BitmartAP5V, BitmartBP5, BitmartBP5V, processingtime, sub13, Status, Bitmart_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Deepcoin", DeepcoinLTP,
                                         DeepcoinAP5, DeepcoinAP5V, DeepcoinBP5, DeepcoinBP5V, processingtime, sub14,
                                         Status, Deepcoin_Status))
            tasks.append(executor.submit(checker, BitmartOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitfinex", BitfinexLTP,
                                         BitfinexAP5, BitfinexAP5V, BitfinexBP5, BitfinexBP5V, processingtime, sub15,
                                         Status, Bitfinex_Status))
            tasks.append(
                executor.submit(checker, BitmartOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "BingX", BingXLTP, BingXAP5,
                                BingXAP5V, BingXBP5, BingXBP5V, processingtime, sub16, Status, BingX_Status))
            tasks.append(
                executor.submit(checker, OrangeXOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "OrangeX", OrangeXLTP, OrangeXAP5,
                                OrangeXAP5V, OrangeXBP5, OrangeXBP5V, processingtime, sub17, Status, OrangeX_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitvenus", BitvenusLTP,
                                         BitvenusAP5, BitvenusAP5V, BitvenusBP5, BitvenusBP5V, processingtime, sub18,
                                         Status, Bitvenus_Status))
            tasks.append(executor.submit(checker, BitvenusOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Biconomy", BiconomyLTP,
                                         BiconomyAP5, BiconomyAP5V, BiconomyBP5, BiconomyBP5V, processingtime, sub19,
                                         Status, Biconomy_Status))
            tasks.append(
                executor.submit(checker, GeminiOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Gemini", GeminiLTP, GeminiAP5,
                                GeminiAP5V, GeminiBP5, GeminiBP5V, processingtime, sub20, Status, Gemini_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "XT", XTLTP, XTAP5, XTAP5V, XTBP5,
                                XTBP5V, processingtime, sub21, Binance_Status, XT_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Bitflyer", BitflyerLTP, BitflyerAP5,
                                BitflyerAP5V, BitflyerBP5, BitflyerBP5V, processingtime, sub22, Status,
                                Bitflyer_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "CoinW", CoinWLTP, CoinWAP5, CoinWAP5V,
                                CoinWBP5, CoinWBP5V, processingtime, sub23, Status, CoinW_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Toobit", ToobitLTP, ToobitAP5,
                                ToobitAP5V, ToobitBP5, ToobitBP5V, processingtime, sub24, Status, Toobit_Status))
            tasks.append(
                executor.submit(checker, XTOBT, Name, LTP, AP5, AP5V, BP5, BP5V, "Tapbit", TapbitLTP, TapbitAP5,
                                TapbitAP5V, TapbitBP5, TapbitBP5V, processingtime, sub25, Status, TapBit_Status))

    buckets_args = [
        (
            "Binance", BinanceLTP, BinanceAP5, BinanceAP5V, BinanceBP5, BinanceBP5V, BinanceBP_BinanceAP,
            BinanceBP_BybitAP,
            BinanceBP_OKXAP, BinanceBP_UpbitAP, BinanceBP_KucoinAP, BinanceBP_BitgetAP, BinanceBP_BitstampAP,
            BinanceBP_GeminiAP, BinanceBP_KrakenAP, BinanceBP_GateioAP, BinanceBP_HTXAP, BinanceBP_MEXCAP,
            BinanceBP_LbankAP, BinanceBP_BitmartAP, BinanceBP_DeepcoinAP, BinanceBP_BitfinexAP, BinanceBP_BingXAP,
            BinanceBP_OrangeXAP, BinanceBP_BitvenusAP, BinanceBP_BiconomyAP, BinanceBP_XTAP, BinanceBP_BitflyerAP,
            BinanceBP_CoinWAP, BinanceBP_ToobitAP, BinanceBP_TapBitAP, Binance_Status),
        ("Bybit", BybitLTP, BybitAP5, BybitAP5V, BybitBP5, BybitBP5V, BybitBP_BinanceAP, BybitBP_BybitAP, BybitBP_OKXAP,
         BybitBP_UpbitAP, BybitBP_KucoinAP, BybitBP_BitgetAP, BybitBP_BitstampAP, BybitBP_GeminiAP, BybitBP_KrakenAP,
         BybitBP_GateioAP, BybitBP_HTXAP, BybitBP_MEXCAP, BybitBP_LbankAP, BybitBP_BitmartAP, BybitBP_DeepcoinAP,
         BybitBP_BitfinexAP, BybitBP_BingXAP, BybitBP_OrangeXAP, BybitBP_BitvenusAP, BybitBP_BiconomyAP, BybitBP_XTAP,
         BybitBP_BitflyerAP, BybitBP_CoinWAP, BybitBP_ToobitAP, BybitBP_TapBitAP, BybitStatus),
        ("OKX", OKXLTP, OKXAP5, OKXAP5V, OKXBP5, OKXBP5V, OKXBP_BinanceAP, OKXBP_BybitAP, OKXBP_OKXAP, OKXBP_UpbitAP,
         OKXBP_KucoinAP, OKXBP_BitgetAP, OKXBP_BitstampAP, OKXBP_GeminiAP, OKXBP_KrakenAP, OKXBP_GateioAP, OKXBP_HTXAP,
         OKXBP_MEXCAP, OKXBP_LbankAP, OKXBP_BitmartAP, OKXBP_DeepcoinAP, OKXBP_BitfinexAP, OKXBP_BingXAP,
         OKXBP_OrangeXAP, OKXBP_BitvenusAP, OKXBP_BiconomyAP, OKXBP_XTAP, OKXBP_BitflyerAP, OKXBP_CoinWAP,
         OKXBP_ToobitAP, OKXBP_TapBitAP, OKX_Status),
        ("Upbit", UpbitLTP, UpbitAP5, UpbitAP5V, UpbitBP5, UpbitBP5V, UpbitBP_BinanceAP, UpbitBP_BybitAP, UpbitBP_OKXAP,
         UpbitBP_UpbitAP, UpbitBP_KucoinAP, UpbitBP_BitgetAP, UpbitBP_BitstampAP, UpbitBP_GeminiAP, UpbitBP_KrakenAP,
         UpbitBP_GateioAP, UpbitBP_HTXAP, UpbitBP_MEXCAP, UpbitBP_LbankAP, UpbitBP_BitmartAP, UpbitBP_DeepcoinAP,
         UpbitBP_BitfinexAP, UpbitBP_BingXAP, UpbitBP_OrangeXAP, UpbitBP_BitvenusAP, UpbitBP_BiconomyAP, UpbitBP_XTAP,
         UpbitBP_BitflyerAP, UpbitBP_CoinWAP, UpbitBP_ToobitAP, UpbitBP_TapBitAP, Upbit_Status),
        ("Kucoin", KucoinLTP, KucoinAP5, KucoinAP5V, KucoinBP5, KucoinBP5V, KucoinBP_BinanceAP, KucoinBP_BybitAP,
         KucoinBP_OKXAP, KucoinBP_UpbitAP, KucoinBP_KucoinAP, KucoinBP_BitgetAP, KucoinBP_BitstampAP, KucoinBP_GeminiAP,
         KucoinBP_KrakenAP, KucoinBP_GateioAP, KucoinBP_HTXAP, KucoinBP_MEXCAP, KucoinBP_LbankAP, KucoinBP_BitmartAP,
         KucoinBP_DeepcoinAP, KucoinBP_BitfinexAP, KucoinBP_BingXAP, KucoinBP_OrangeXAP, KucoinBP_BitvenusAP,
         KucoinBP_BiconomyAP, KucoinBP_XTAP, KucoinBP_BitflyerAP, KucoinBP_CoinWAP, KucoinBP_ToobitAP,
         KucoinBP_TapBitAP, Kucoin_Status),
        ("Bitget", BitgetLTP, BitgetAP5, BitgetAP5V, BitgetBP5, BitgetBP5V, BitgetBP_BinanceAP, BitgetBP_BybitAP,
         BitgetBP_OKXAP, BitgetBP_UpbitAP, BitgetBP_KucoinAP, BitgetBP_BitgetAP, BitgetBP_BitstampAP, BitgetBP_GeminiAP,
         BitgetBP_KrakenAP, BitgetBP_GateioAP, BitgetBP_HTXAP, BitgetBP_MEXCAP, BitgetBP_LbankAP, BitgetBP_BitmartAP,
         BitgetBP_DeepcoinAP, BitgetBP_BitfinexAP, BitgetBP_BingXAP, BitgetBP_OrangeXAP, BitgetBP_BitvenusAP,
         BitgetBP_BiconomyAP, BitgetBP_XTAP, BitgetBP_BitflyerAP, BitgetBP_CoinWAP, BitgetBP_ToobitAP,
         BitgetBP_TapBitAP, Bitget_Status),
        ("Bitstamp", BitstampLTP, BitstampAP5, BitstampAP5V, BitstampBP5, BitstampBP5V, BitstampBP_BinanceAP,
         BitstampBP_BybitAP, BitstampBP_OKXAP, BitstampBP_UpbitAP, BitstampBP_KucoinAP, BitstampBP_BitgetAP,
         BitstampBP_BitstampAP, BitstampBP_GeminiAP, BitstampBP_KrakenAP, BitstampBP_GateioAP, BitstampBP_HTXAP,
         BitstampBP_MEXCAP, BitstampBP_LbankAP, BitstampBP_BitmartAP, BitstampBP_DeepcoinAP, BitstampBP_BitfinexAP,
         BitstampBP_BingXAP, BitstampBP_OrangeXAP, BitstampBP_BitvenusAP, BitstampBP_BiconomyAP, BitstampBP_XTAP,
         BitstampBP_BitflyerAP, BitstampBP_CoinWAP, BitstampBP_ToobitAP, BitstampBP_TapBitAP, Bitstamp_Status),
        ("Kraken", KrakenLTP, KrakenAP5, KrakenAPV5, KrakenBP5, KrakenBPV5, KrakenBP_BinanceAP, KrakenBP_BybitAP,
         KrakenBP_OKXAP, KrakenBP_UpbitAP, KrakenBP_KucoinAP, KrakenBP_BitgetAP, KrakenBP_BitstampAP, KrakenBP_GeminiAP,
         KrakenBP_KrakenAP, KrakenBP_GateioAP, KrakenBP_HTXAP, KrakenBP_MEXCAP, KrakenBP_LbankAP, KrakenBP_BitmartAP,
         KrakenBP_DeepcoinAP, KrakenBP_BitfinexAP, KrakenBP_BingXAP, KrakenBP_OrangeXAP, KrakenBP_BitvenusAP,
         KrakenBP_BiconomyAP, KrakenBP_XTAP, KrakenBP_BitflyerAP, KrakenBP_CoinWAP, KrakenBP_ToobitAP,
         KrakenBP_TapBitAP, Kraken_Status),
        ("Gate.io", GateioLTP, GateioAP5, GateioAPV5, GateioBP5, GateioBPV5, GateioBP_BinanceAP, GateioBP_BybitAP,
         GateioBP_OKXAP, GateioBP_UpbitAP, GateioBP_KucoinAP, GateioBP_BitgetAP, GateioBP_BitstampAP, GateioBP_GeminiAP,
         GateioBP_KrakenAP, GateioBP_GateioAP, GateioBP_HTXAP, GateioBP_MEXCAP, GateioBP_LbankAP, GateioBP_BitmartAP,
         GateioBP_DeepcoinAP, GateioBP_BitfinexAP, GateioBP_BingXAP, GateioBP_OrangeXAP, GateioBP_BitvenusAP,
         GateioBP_BiconomyAP, GateioBP_XTAP, GateioBP_BitflyerAP, GateioBP_CoinWAP, GateioBP_ToobitAP,
         GateioBP_TapBitAP, Gateio_Status),
        ("HTX", HTXLTP, HTXAP5,
         HTXAP5V,
         HTXBP5, HTXBP5V,
         HTXBP_BinanceAP, HTXBP_BybitAP, HTXBP_OKXAP, HTXBP_UpbitAP, HTXBP_KucoinAP,
         HTXBP_BitgetAP, HTXBP_BitstampAP
         , HTXBP_GeminiAP, HTXBP_KrakenAP, HTXBP_GateioAP, HTXBP_HTXAP, HTXBP_MEXCAP,
         HTXBP_LbankAP, HTXBP_BitmartAP
         , HTXBP_DeepcoinAP, HTXBP_BitfinexAP, HTXBP_BingXAP, HTXBP_OrangeXAP, HTXBP_BitvenusAP,
         HTXBP_BiconomyAP,
         HTXBP_XTAP, HTXBP_BitflyerAP, HTXBP_CoinWAP, HTXBP_ToobitAP, HTXBP_TapBitAP, HTX_Status
         ),
        ("MEXC", MEXCLTP,
         MEXCAP5, MEXCAP5V,
         MEXCBP5, MEXCBP5V,
         MEXCBP_BinanceAP, MEXCBP_BybitAP, MEXCBP_OKXAP, MEXCBP_UpbitAP, MEXCBP_KucoinAP,
         MEXCBP_BitgetAP, MEXCBP_BitstampAP
         , MEXCBP_GeminiAP, MEXCBP_KrakenAP, MEXCBP_GateioAP, MEXCBP_HTXAP, MEXCBP_MEXCAP,
         MEXCBP_LbankAP, MEXCBP_BitmartAP
         , MEXCBP_DeepcoinAP, MEXCBP_BitfinexAP, MEXCBP_BingXAP, MEXCBP_OrangeXAP, MEXCBP_BitvenusAP,
         MEXCBP_BiconomyAP,
         MEXCBP_XTAP, MEXCBP_BitflyerAP, MEXCBP_CoinWAP, MEXCBP_ToobitAP, MEXCBP_TapBitAP, MEXC_Status
         ),
        ("Lbank", LbankLTP,
         LbankAP5, LbankAP5V,
         LbankBP5, LbankBP5V,
         LbankBP_BinanceAP, LbankBP_BybitAP, LbankBP_OKXAP, LbankBP_UpbitAP, LbankBP_KucoinAP,
         LbankBP_BitgetAP, LbankBP_BitstampAP
         , LbankBP_GeminiAP, LbankBP_KrakenAP, LbankBP_GateioAP, LbankBP_HTXAP, LbankBP_MEXCAP,
         LbankBP_LbankAP, LbankBP_BitmartAP
         , LbankBP_DeepcoinAP, LbankBP_BitfinexAP, LbankBP_BingXAP, LbankBP_OrangeXAP, LbankBP_BitvenusAP,
         LbankBP_BiconomyAP,
         LbankBP_XTAP, LbankBP_BitflyerAP, LbankBP_CoinWAP, LbankBP_ToobitAP, LbankBP_TapBitAP, Lbank_Status
         ),
        ("Bitmart",
         BitmartLTP, BitmartAP5, BitmartAP5V,
         BitmartBP5, BitmartBP5V,
         BitmartBP_BinanceAP, BitmartBP_BybitAP, BitmartBP_OKXAP, BitmartBP_UpbitAP, BitmartBP_KucoinAP,
         BitmartBP_BitgetAP, BitmartBP_BitstampAP
         , BitmartBP_GeminiAP, BitmartBP_KrakenAP, BitmartBP_GateioAP, BitmartBP_HTXAP, BitmartBP_MEXCAP,
         BitmartBP_LbankAP, BitmartBP_BitmartAP
         , BitmartBP_DeepcoinAP, BitmartBP_BitfinexAP, BitmartBP_BingXAP, BitmartBP_OrangeXAP, BitmartBP_BitvenusAP,
         BitmartBP_BiconomyAP,
         BitmartBP_XTAP, BitmartBP_BitflyerAP, BitmartBP_CoinWAP, BitmartBP_ToobitAP, BitmartBP_TapBitAP, Bitmart_Status
         ),
        ("Deepcoin",
         DeepcoinLTP,
         DeepcoinAP5, DeepcoinAP5V, DeepcoinBP5, DeepcoinBP5V,
         DeepcoinBP_BinanceAP, DeepcoinBP_BybitAP, DeepcoinBP_OKXAP, DeepcoinBP_UpbitAP, DeepcoinBP_KucoinAP,
         DeepcoinBP_BitgetAP, DeepcoinBP_BitstampAP
         , DeepcoinBP_GeminiAP, DeepcoinBP_KrakenAP, DeepcoinBP_GateioAP, DeepcoinBP_HTXAP, DeepcoinBP_MEXCAP,
         DeepcoinBP_LbankAP, DeepcoinBP_BitmartAP
         , DeepcoinBP_DeepcoinAP, DeepcoinBP_BitfinexAP, DeepcoinBP_BingXAP, DeepcoinBP_OrangeXAP,
         DeepcoinBP_BitvenusAP,
         DeepcoinBP_BiconomyAP,
         DeepcoinBP_XTAP, DeepcoinBP_BitflyerAP, DeepcoinBP_CoinWAP, DeepcoinBP_ToobitAP, DeepcoinBP_TapBitAP,
         Deepcoin_Status
         ),
        ("Bitfinex",
         BitfinexLTP, BitfinexAP5, BitfinexAP5V,
         BitfinexBP5, BitfinexBP5V,
         BitfinexBP_BinanceAP, BitfinexBP_BybitAP, BitfinexBP_OKXAP, BitfinexBP_UpbitAP, BitfinexBP_KucoinAP,
         BitfinexBP_BitgetAP, BitfinexBP_BitstampAP
         , BitfinexBP_GeminiAP, BitfinexBP_KrakenAP, BitfinexBP_GateioAP, BitfinexBP_HTXAP, BitfinexBP_MEXCAP,
         BitfinexBP_LbankAP, BitfinexBP_BitmartAP
         , BitfinexBP_DeepcoinAP, BitfinexBP_BitfinexAP, BitfinexBP_BingXAP, BitfinexBP_OrangeXAP,
         BitfinexBP_BitvenusAP,
         BitfinexBP_BiconomyAP,
         BitfinexBP_XTAP, BitfinexBP_BitflyerAP, BitfinexBP_CoinWAP, BitfinexBP_ToobitAP, BitfinexBP_TapBitAP,
         Bitfinex_Status
         ),
        ("BingX", BingXLTP,
         BingXAP5, BingXAP5V,
         BingXBP5, BingXBP5V,
         BingXBP_BinanceAP, BingXBP_BybitAP, BingXBP_OKXAP, BingXBP_UpbitAP, BingXBP_KucoinAP,
         BingXBP_BitgetAP, BingXBP_BitstampAP
         , BingXBP_GeminiAP, BingXBP_KrakenAP, BingXBP_GateioAP, BingXBP_HTXAP, BingXBP_MEXCAP,
         BingXBP_LbankAP, BingXBP_BitmartAP
         , BingXBP_DeepcoinAP, BingXBP_BitfinexAP, BingXBP_BingXAP, BingXBP_OrangeXAP, BingXBP_BitvenusAP,
         BingXBP_BiconomyAP,
         BingXBP_XTAP, BingXBP_BitflyerAP, BingXBP_CoinWAP, BingXBP_ToobitAP, BingXBP_TapBitAP, BingX_Status
         ),
        ("OrangeX",
         OrangeXLTP, OrangeXAP5, OrangeXAP5V,
         OrangeXBP5, OrangeXBP5V,
         OrangeXBP_BinanceAP, OrangeXBP_BybitAP, OrangeXBP_OKXAP, OrangeXBP_UpbitAP, OrangeXBP_KucoinAP,
         OrangeXBP_BitgetAP, OrangeXBP_BitstampAP
         , OrangeXBP_GeminiAP, OrangeXBP_KrakenAP, OrangeXBP_GateioAP, OrangeXBP_HTXAP, OrangeXBP_MEXCAP,
         OrangeXBP_LbankAP, OrangeXBP_BitmartAP
         , OrangeXBP_DeepcoinAP, OrangeXBP_BitfinexAP, OrangeXBP_BingXAP, OrangeXBP_OrangeXAP, OrangeXBP_BitvenusAP,
         OrangeXBP_BiconomyAP,
         OrangeXBP_XTAP, OrangeXBP_BitflyerAP, OrangeXBP_CoinWAP, OrangeXBP_ToobitAP, OrangeXBP_TapBitAP, OrangeX_Status
         ),
        ("Bitvenus",
         BitvenusLTP, BitvenusAP5, BitvenusAP5V,
         BitvenusBP5, BitvenusBP5V,
         BitvenusBP_BinanceAP, BitvenusBP_BybitAP, BitvenusBP_OKXAP, BitvenusBP_UpbitAP, BitvenusBP_KucoinAP,
         BitvenusBP_BitgetAP, BitvenusBP_BitstampAP
         , BitvenusBP_GeminiAP, BitvenusBP_KrakenAP, BitvenusBP_GateioAP, BitvenusBP_HTXAP, BitvenusBP_MEXCAP,
         BitvenusBP_LbankAP, BitvenusBP_BitmartAP
         , BitvenusBP_DeepcoinAP, BitvenusBP_BitfinexAP, BitvenusBP_BingXAP, BitvenusBP_OrangeXAP,
         BitvenusBP_BitvenusAP,
         BitvenusBP_BiconomyAP,
         BitvenusBP_XTAP, BitvenusBP_BitflyerAP, BitvenusBP_CoinWAP, BitvenusBP_ToobitAP, BitvenusBP_TapBitAP,
         Bitvenus_Status
         ),
        ("Biconomy",
         BiconomyLTP, BiconomyAP5, BiconomyAP5V,
         BiconomyBP5, BiconomyBP5V,
         BiconomyBP_BinanceAP, BiconomyBP_BybitAP, BiconomyBP_OKXAP, BiconomyBP_UpbitAP, BiconomyBP_KucoinAP,
         BiconomyBP_BitgetAP, BiconomyBP_BitstampAP
         , BiconomyBP_GeminiAP, BiconomyBP_KrakenAP, BiconomyBP_GateioAP, BiconomyBP_HTXAP, BiconomyBP_MEXCAP,
         BiconomyBP_LbankAP, BiconomyBP_BitmartAP
         , BiconomyBP_DeepcoinAP, BiconomyBP_BitfinexAP, BiconomyBP_BingXAP, BiconomyBP_OrangeXAP,
         BiconomyBP_BitvenusAP,
         BiconomyBP_BiconomyAP,
         BiconomyBP_XTAP, BiconomyBP_BitflyerAP, BiconomyBP_CoinWAP, BiconomyBP_ToobitAP, BiconomyBP_TapBitAP,
         Biconomy_Status
         ),
        ("Gemini", GeminiLTP,
         GeminiAP5, GeminiAP5V,
         GeminiBP5, GeminiBP5V,
         GeminiBP_BinanceAP, GeminiBP_BybitAP, GeminiBP_OKXAP, GeminiBP_UpbitAP, GeminiBP_KucoinAP,
         GeminiBP_BitgetAP, GeminiBP_BitstampAP
         , GeminiBP_GeminiAP, GeminiBP_KrakenAP, GeminiBP_GateioAP, GeminiBP_HTXAP, GeminiBP_MEXCAP,
         GeminiBP_LbankAP, GeminiBP_BitmartAP
         , GeminiBP_DeepcoinAP, GeminiBP_BitfinexAP, GeminiBP_BingXAP, GeminiBP_OrangeXAP, GeminiBP_BitvenusAP,
         GeminiBP_BiconomyAP,
         GeminiBP_XTAP, GeminiBP_BitflyerAP, GeminiBP_CoinWAP, GeminiBP_ToobitAP, GeminiBP_TapBitAP, Gemini_Status
         ),
        ("XT", XTLTP, XTAP5,
         XTAP5V,
         XTBP5, XTBP5V,
         XTBP_BinanceAP, XTBP_BybitAP, XTBP_OKXAP, XTBP_UpbitAP, XTBP_KucoinAP,
         XTBP_BitgetAP, XTBP_BitstampAP
         , XTBP_GeminiAP, XTBP_KrakenAP, XTBP_GateioAP, XTBP_HTXAP, XTBP_MEXCAP,
         XTBP_LbankAP, XTBP_BitmartAP
         , XTBP_DeepcoinAP, XTBP_BitfinexAP, XTBP_BingXAP, XTBP_OrangeXAP, XTBP_BitvenusAP,
         XTBP_BiconomyAP,
         XTBP_XTAP, XTBP_BitflyerAP, XTBP_CoinWAP, XTBP_ToobitAP, XTBP_TapBitAP, XT_Status
         ),
        ("Bitflyer", BitflyerLTP,
         BitflyerAP5, BitflyerAP5V,
         BitflyerBP5, BitflyerBP5V,
         BitflyerBP_BinanceAP, BitflyerBP_BybitAP, BitflyerBP_OKXAP, BitflyerBP_UpbitAP, BitflyerBP_KucoinAP,
         BitflyerBP_BitgetAP, BitflyerBP_BitstampAP
         , BitflyerBP_GeminiAP, BitflyerBP_KrakenAP, BitflyerBP_GateioAP, BitflyerBP_HTXAP, BitflyerBP_MEXCAP,
         BitflyerBP_LbankAP, BitflyerBP_BitmartAP
         , BitflyerBP_DeepcoinAP, BitflyerBP_BitfinexAP, BitflyerBP_BingXAP, BitflyerBP_OrangeXAP,
         BitflyerBP_BitvenusAP,
         BitflyerBP_BiconomyAP,
         BitflyerBP_XTAP, BitflyerBP_BitflyerAP, BitflyerBP_CoinWAP, BitflyerBP_ToobitAP, BitflyerBP_TapBitAP,
         Bitflyer_Status
         ),
        ("CoinW", CoinWLTP,
         CoinWAP5, CoinWAP5V,
         CoinWBP5, CoinWBP5V,
         CoinWBP_BinanceAP, CoinWBP_BybitAP, CoinWBP_OKXAP, CoinWBP_UpbitAP, CoinWBP_KucoinAP,
         CoinWBP_BitgetAP, CoinWBP_BitstampAP
         , CoinWBP_GeminiAP, CoinWBP_KrakenAP, CoinWBP_GateioAP, CoinWBP_HTXAP, CoinWBP_MEXCAP,
         CoinWBP_LbankAP, CoinWBP_BitmartAP
         , CoinWBP_DeepcoinAP, CoinWBP_BitfinexAP, CoinWBP_BingXAP, CoinWBP_OrangeXAP, CoinWBP_BitvenusAP,
         CoinWBP_BiconomyAP,
         CoinWBP_XTAP, CoinWBP_BitflyerAP, CoinWBP_CoinWAP, CoinWBP_ToobitAP, CoinWBP_TapBitAP, CoinW_Status
         ),
        ("Toobit", ToobitLTP,
         ToobitAP5, ToobitAP5V,
         ToobitBP5, ToobitBP5V,
         ToobitBP_BinanceAP, ToobitBP_BybitAP, ToobitBP_OKXAP, ToobitBP_UpbitAP, ToobitBP_KucoinAP,
         ToobitBP_BitgetAP, ToobitBP_BitstampAP
         , ToobitBP_GeminiAP, ToobitBP_KrakenAP, ToobitBP_GateioAP, ToobitBP_HTXAP, ToobitBP_MEXCAP,
         ToobitBP_LbankAP, ToobitBP_BitmartAP
         , ToobitBP_DeepcoinAP, ToobitBP_BitfinexAP, ToobitBP_BingXAP, ToobitBP_OrangeXAP, ToobitBP_BitvenusAP,
         ToobitBP_BiconomyAP,
         ToobitBP_XTAP, ToobitBP_BitflyerAP, ToobitBP_CoinWAP, ToobitBP_ToobitAP, ToobitBP_TapBitAP, Toobit_Status
         ),
        ("Tapbit", TapbitLTP,
         TapbitAP5, TapbitAP5V,
         TapbitBP5, TapbitBP5V,
         TapBitBP_BinanceAP, TapBitBP_BybitAP, TapBitBP_OKXAP, TapBitBP_UpbitAP, TapBitBP_KucoinAP,
         TapBitBP_BitgetAP, TapBitBP_BitstampAP
         , TapBitBP_GeminiAP, TapBitBP_KrakenAP, TapBitBP_GateioAP, TapBitBP_HTXAP, TapBitBP_MEXCAP,
         TapBitBP_LbankAP, TapBitBP_BitmartAP
         , TapBitBP_DeepcoinAP, TapBitBP_BitfinexAP, TapBitBP_BingXAP, TapBitBP_OrangeXAP, TapBitBP_BitvenusAP,
         TapBitBP_BiconomyAP,
         TapBitBP_XTAP, TapBitBP_BitflyerAP, TapBitBP_CoinWAP, TapBitBP_ToobitAP, TapBitBP_TapBitAP, TapBit_Status
         )

        # Add other exchanges similarly
    ]

    # Create a list to hold the threads
    threads = []

    # Create and start a thread for each PriceDifference function call
    for args in buckets_args:
        thread = threading.Thread(target=Buckets, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



async def fetching():
    return await Data()




async def run_functions_concurrently(data,inital_time):
    with ThreadPoolExecutor() as executor:
        # Create a list of tasks to run concurrently
        tasks = [
            asyncio.create_task(Bid_Ask1(data,inital_time)),
            asyncio.create_task(Bid_Ask2(data,inital_time)),
            asyncio.create_task(Bid_Ask3(data,inital_time)),
            asyncio.create_task(Bid_Ask4(data,inital_time)),
            asyncio.create_task(Bid_Ask5(data,inital_time)),
        ]

        # Run the tasks concurrently
        await asyncio.gather(*tasks)


# Main loop to run the functions
async def main():
    # Infinite loop to keep running
    while True:
        start = time.perf_counter_ns()
        data = await fetching()
        end = time.perf_counter_ns()
        inital_time = end - start

        await (run_functions_concurrently(data,inital_time))



asyncio.run(main())

from warning import error_note

error_note()