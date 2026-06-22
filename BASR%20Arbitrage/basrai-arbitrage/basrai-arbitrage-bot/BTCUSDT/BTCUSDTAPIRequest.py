import time
import aiohttp
import asyncio
import ssl
import certifi
import config

ssl_context = ssl.create_default_context(cafile=certifi.where())


"""
BTCUSDT API Data Fetcher

This script fetches order book and trade data for the BTC/USDT trading pair from multiple cryptocurrency exchanges. 
It utilizes asynchronous requests with the `aiohttp` library for efficient concurrent API calls. 

Main Features:
- Fetches bid/ask prices and volumes for multiple order book levels.
- Retrieves last traded prices and associated metadata.
- Handles API errors gracefully, ensuring robust data fetching.

Key Functions:
1. fetch_price(session, url): Sends an asynchronous GET request to fetch data from the given URL.
2. Data(): Main function that gathers data from all configured exchange APIs, initializes variables for each exchange, and processes the responses.

Configuration:
- The list of API endpoints is imported from a `config` module, which must define URLs for order book (OB) and last trade price (LTP) endpoints for various exchanges.
- Uses SSL for secure connections, with the certificate handled by the `certifi` package.

Dependencies:
- aiohttp: For making asynchronous HTTP requests.
- asyncio: For managing asynchronous tasks.
- certifi: For providing SSL certificates.
- A `config` module containing the API endpoints.

Usage:
Run this script in an asynchronous event loop to fetch and process data from all supported exchanges.

Error Handling:
- Gracefully catches and logs client and other exceptions.
- Assigns default values to variables in case of errors.

Note:
Ensure that the `config` module is correctly set up with all required API endpoint URLs before executing this script.
"""


async def fetch_price(session, url):
    '''
    Fetches price data from the given URL.
    :param session: aiohttp session for making requests
    :param url: URL to send the request to
    :return: response status and data
    '''
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=0.5)) as response:  # Timeout set to 10 seconds
            response.raise_for_status()
            data = await response.json()
            return response.status, data
    except aiohttp.ClientError as e:
        print(f"Client error fetching data from {url}: {e}")
        return None, None
    except asyncio.TimeoutError:
        print(f"Timeout error fetching data from {url}")
        return None, None
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None, None

async def Data():
    '''
    Orchestrates the fetching of data from multiple URLs concurrently.
    '''
    """
    """
    urls = [
        config.BinanceOBURL, config.BinanceLTPURL,
        config.BybitOBURL, config.BybitLTPURL,
        config.OKXOBBURL, config.OKXLTPURL,
        config.UpbitOBURL, config.UpbitLTPURL,
        config.KucoinOBURL, config.KucoinLTPURL,
        config.BitgetOBURL, config.BitgetLTPURL,
        config.BitstampOBURL, config.BitstampLTPURL,
        config.krakenOBURL, config.krakenLTPURL,
        config.Gateio_url_Orderbook, config.Gateio_url_Last_trade,
        config.HTXOBURL, config.HTXLTPURL,
        config.MEXCOBURL, config.MEXCLTPURL,
        config.LbankOBURL, config.LbankLTPURL,
        config.BitmartOBURL, config.BitmartLTPURL,
        config.DeepcoinOBURL, config.DeepcoinLTPURL,
        config.BitfinexOBURL, config.BitfinexLTPURL,
        config.BingxOBURL, config.BingxLTPURL,
        config.OrangeXOBURL, config.OrangeXLTPURL,
        config.BitvenusOBURL, config.BitvenusLTPURL,
        config.BICONOMYOBURL, config.BICONOMYLTPURL,
        config.GeminiOBURL, config.GeminiLTPURL,
        config.XTOBURL, config.XTLTPURL,
        config.BitflyerOBURL, config.BitflyerLTPURL,
        config.CoinWOBURL, config.CoinWLTPURL,
        config.ToobitOBURL, config.ToobitLTPURL,
        config.TapbitOBURL, config.TapbitLTPURL
    ]

    # Use connection pooling with a connection limit
    connector = aiohttp.TCPConnector(limit=50, ssl=ssl_context)  # Limit concurrent connections to 50

    async with aiohttp.ClientSession(connector=connector) as session:
        # Create tasks for fetching data from URLs
        tasks = [fetch_price(session, url) for url in urls]
        # Await all tasks concurrently
        responses = await asyncio.gather(*tasks, return_exceptions=False)

        # Initialize variables for Binance
        BinanceBP1 = BinanceBP2 = BinanceBP3 = BinanceBP4 = BinanceBP5 = 0
        BinanceBP1V = BinanceBP2V = BinanceBP3V = BinanceBP4V = BinanceBP5V = 0
        BinanceAP1 = BinanceAP2 = BinanceAP3 = BinanceAP4 = BinanceAP5 = 0
        BinanceAP1V = BinanceAP2V = BinanceAP3V = BinanceAP4V = BinanceAP5V = 0
        BinanceLTP = BinanceLTPV = 0
        BinanceLTPTM = 0
        BinanceLTPT = None

        # Initialize variables for Bybit
        BybitBP1 = BybitBP2 = BybitBP3 = BybitBP4 = BybitBP5 = 0
        BybitBP1V = BybitBP2V = BybitBP3V = BybitBP4V = BybitBP5V = 0
        BybitAP1 = BybitAP2 = BybitAP3 = BybitAP4 = BybitAP5 = 0
        BybitAP1V = BybitAP2V = BybitAP3V = BybitAP4V = BybitAP5V = 0
        BybitOBTM = 0
        BybitOBT = None
        BybitLTP = BybitLTPV = 0
        BybitLTPTM = 0
        BybitLTPT = None

        OKXAP1 = OKXAP2 = OKXAP3 = OKXAP4 = OKXAP5 = 0
        OKXAP1V = OKXAP2V = OKXAP3V = OKXAP4V = OKXAP5V = 0
        OKXBP1 = OKXBP2 = OKXBP3 = OKXBP4 = OKXBP5 = 0
        OKXBP1V = OKXBP2V = OKXBP3V = OKXBP4V = OKXBP5V = 0
        OKXOBTM = 0
        OKXOBT = None
        OKXLTP = OKXLTPV = 0
        OKXLTPTM = 0
        OKXLTPT = None

        UpbitOBTM = UpbitAP1 = UpbitBP1 = UpbitAP1V = UpbitBP1V = UpbitAP2 = UpbitBP2 = UpbitAP2V = 0
        UpbitBP2V = UpbitAP3 = UpbitBP3 = UpbitAP3V = UpbitBP3V = UpbitAP4 = UpbitBP4 = UpbitAP4V = UpbitBP4V = 0
        UpbitAP5 = UpbitBP5 = UpbitAP5V = UpbitBP5V = 0
        UpbitOBT = None
        UpbitLTP = UpbitLTPV = 0
        UpbitLTPTM = 0
        UpbitLTPT = None

        KucoinOBTM = 0
        KucoinOBT = None
        KucoinBP1 = KucoinBP2 = KucoinBP3 = KucoinBP4 = KucoinBP5 = 0
        KucoinBP1V = KucoinBP2V = KucoinBP3V = KucoinBP4V = KucoinBP5V = 0
        KucoinAP1 = KucoinAP2 = KucoinAP3 = KucoinAP4 = KucoinAP5 = 0
        KucoinAP1V = KucoinAP2V = KucoinAP3V = KucoinAP4V = KucoinAP5V = 0
        KucoinLTP = 0
        KucoinLTPV = 0
        KucoinLTPTM = 0
        KucoinLTPT = None

        BitgetOBTM = 0
        BitgetOBT = None
        BitgetAP1 = BitgetAP2 = BitgetAP3 = BitgetAP4 = BitgetAP5 = 0
        BitgetAP1V = BitgetAP2V = BitgetAP3V = BitgetAP4V = BitgetAP5V = 0
        BitgetBP1 = BitgetBP2 = BitgetBP3 = BitgetBP4 = BitgetBP5 = 0
        BitgetBP1V = BitgetBP2V = BitgetBP3V = BitgetBP4V = BitgetBP5V = 0
        BitgetLTP = 0
        BitgetLTPTM = 0
        BitgetLTPV = 0
        BitgetLTPT = None

        BitstampOBTM = 0
        BitstampOBT = None
        BitstampBP1 = BitstampBP2 = BitstampBP3 = BitstampBP4 = BitstampBP5 = 0
        BitstampBP1V = BitstampBP2V = BitstampBP3V = BitstampBP4V = BitstampBP5V = 0
        BitstampAP1 = BitstampAP2 = BitstampAP3 = BitstampAP4 = BitstampAP5 = 0
        BitstampAP1V = BitstampAP2V = BitstampAP3V = BitstampAP4V = BitstampAP5V = 0
        BitstampLTP = 0
        BitstampLTPV = 0
        BitstampLTPTM = 0
        BitstampLTPT = None

        GeminiOBTM = 0
        GeminiOBT = None
        GeminiBP1 = GeminiBP2 = GeminiBP3 = GeminiBP4 = GeminiBP5 = 0
        GeminiBP1V = GeminiBP2V = GeminiBP3V = GeminiBP4V = GeminiBP5V = 0
        GeminiAP1 = GeminiAP2 = GeminiAP3 = GeminiAP4 = GeminiAP5 = 0
        GeminiAP1V = GeminiAP2V = GeminiAP3V = GeminiAP4V = GeminiAP5V = 0
        GeminiLTP = 0
        GeminiLTPV = 0
        GeminiLTPTM = 0
        GeminiLTPT = None

        KrakenAP1 = KrakenAP2 = KrakenAP3 = KrakenAP4 = KrakenAP5 = 0
        KrakenAPV1 = KrakenAPV2 = KrakenAPV3 = KrakenAPV4 = KrakenAPV5 = 0
        KrakenBP1 = KrakenBP2 = KrakenBP3 = KrakenBP4 = KrakenBP5 = 0
        KrakenBPV1 = KrakenBPV2 = KrakenBPV3 = KrakenBPV4 = KrakenBPV5 = KrakenOBTM = 0
        KrakenOBT = None
        KrakenLTP = 0
        KrakenLTPV = 0
        KrakenLTPTM = 0
        KrakenLTPT = None

        GateioAP1 = GateioAP2 = GateioAP3 = GateioAP4 = GateioAP5 = 0
        GateioAPV1 = GateioAPV2 = GateioAPV3 = GateioAPV4 = GateioAPV5 = 0
        GateioBP1 = GateioBP2 = GateioBP3 = GateioBP4 = GateioBP5 = 0
        GateioBPV1 = GateioBPV2 = GateioBPV3 = GateioBPV4 = GateioBPV5 = 0
        GateioLTP = 0

        HTXOBTM = 0
        HTXOBT = None
        HTXBP1 = HTXBP2 = HTXBP3 = HTXBP4 = HTXBP5 = 0
        HTXBP1V = HTXBP2V = HTXBP3V = HTXBP4V = HTXBP5V = 0
        HTXAP1 = HTXAP2 = HTXAP3 = HTXAP4 = HTXAP5 = 0
        HTXAP1V = HTXAP2V = HTXAP3V = HTXAP4V = HTXAP5V = 0
        HTXLTPTM = 0
        HTXLTPT = None
        HTXLTP = 0
        HTXLTPV = 0

        MEXCBP1 = MEXCBP2 = MEXCBP3 = MEXCBP4 = MEXCBP5 = 0
        MEXCBP1V = MEXCBP2V = MEXCBP3V = MEXCBP4V = MEXCBP5V = 0
        MEXCAP1 = MEXCAP2 = MEXCAP3 = MEXCAP4 = MEXCAP5 = 0
        MEXCAP1V = MEXCAP2V = MEXCAP3V = MEXCAP4V = MEXCAP5V = 0
        MEXCOBTM = 0
        MEXCOBT = None
        MEXCLTP = 0
        MEXCLTPV = 0
        MEXCLTPTM = 0
        MEXCLTPT = None

        LbankAP1 = LbankAP2 = LbankAP3 = LbankAP4 = LbankAP5 = 0
        LbankAP1V = LbankAP2V = LbankAP3V = LbankAP4V = LbankAP5V = 0
        LbankBP1 = LbankBP2 = LbankBP3 = LbankBP4 = LbankBP5 = 0
        LbankBP1V = LbankBP2V = LbankBP3V = LbankBP4V = LbankBP5V = 0
        LbankOBTM = 0
        LbankOBT = None
        LbankLTP = 0
        LbankLTPTM = 0
        LbankLTPT = None

        BitmartOBTM = 0
        BitmartOBT = None
        BitmartAP1 = BitmartAP2 = BitmartAP3 = BitmartAP4 = BitmartAP5 = 0
        BitmartAP1V = BitmartAP2V = BitmartAP3V = BitmartAP4V = BitmartAP5V = 0
        BitmartBP1 = BitmartBP2 = BitmartBP3 = BitmartBP4 = BitmartBP5 = 0
        BitmartBP1V = BitmartBP2V = BitmartBP3V = BitmartBP4V = BitmartBP5V = 0
        BitmartLTPTM = 0
        BitmartLTPT = None
        BitmartLTP = 0
        BitmartLTPV = 0

        DeepcoinBP1 = DeepcoinBP2 = DeepcoinBP3 = DeepcoinBP4 = DeepcoinBP5 = 0
        DeepcoinBP1V = DeepcoinBP2V = DeepcoinBP3V = DeepcoinBP4V = DeepcoinBP5V = 0
        DeepcoinAP1 = DeepcoinAP2 = DeepcoinAP3 = DeepcoinAP4 = DeepcoinAP5 = 0
        DeepcoinAP1V = DeepcoinAP2V = DeepcoinAP3V = DeepcoinAP4V = DeepcoinAP5V = 0
        DeepcoinLTP = 0
        DeepcoinLTPTM = 0
        DeepcoinLTPT = None

        BitfinexBP1 = BitfinexBP2 = BitfinexBP3 = BitfinexBP4 = BitfinexBP5 = 0
        BitfinexBP1V = BitfinexBP2V = BitfinexBP3V = BitfinexBP4V = BitfinexBP5V = 0
        BitfinexAP1 = BitfinexAP2 = BitfinexAP3 = BitfinexAP4 = BitfinexAP5 = 0
        BitfinexAP1V = BitfinexAP2V = BitfinexAP3V = BitfinexAP4V = BitfinexAP5V = 0
        BitfinexLTP = 0

        BingxOBTM = 0
        BingxOBT = 0
        BingXBP1 = BingXBP2 = BingXBP3 = BingXBP4 = BingXBP5 = 0
        BingXAP1 = BingXAP2 = BingXAP3 = BingXAP4 = BingXAP5 = 0
        BingXBP1V = BingXBP2V = BingXBP3V = BingXBP4V = BingXBP5V = 0
        BingXAP1V = BingXAP2V = BingXAP3V = BingXAP4V = BingXAP5V = 0
        BingXLTPTM = 0
        BingXLTPT = None
        BingXLTP = 0
        BingXLTPV = 0

        OrangeXAP1 = OrangeXAP2 = OrangeXAP3 = OrangeXAP4 = OrangeXAP5 = 0
        OrangeXAP1V = OrangeXAP2V = OrangeXAP3V = OrangeXAP4V = OrangeXAP5V = 0
        OrangeXBP1 = OrangeXBP2 = OrangeXBP3 = OrangeXBP4 = OrangeXBP5 = 0
        OrangeXBP1V = OrangeXBP2V = OrangeXBP3V = OrangeXBP4V = OrangeXBP5V = 0
        OrangeXOBTM = 0
        OrangeXOBT = None
        OrangeXLTP = 0
        OrangeXLTPTM = 0
        OrangeXLTPT = None

        BitvenusOBTM = 0
        BitvenusOBT = None
        BitvenusBP1 = BitvenusBP2 = BitvenusBP3 = BitvenusBP4 = BitvenusBP5 = 0
        BitvenusBP1V = BitvenusBP2V = BitvenusBP3V = BitvenusBP4V = BitvenusBP5V = 0
        BitvenusAP1 = BitvenusAP2 = BitvenusAP3 = BitvenusAP4 = BitvenusAP5 = 0
        BitvenusAP1V = BitvenusAP2V = BitvenusAP3V = BitvenusAP4V = BitvenusAP5V = 0
        BitvenusLTP = 0
        BitvenusLTPV = 0
        BitvenusLTPTM = 0
        BitvenusLTPT = None

        BiconomyAP1 = BiconomyAP2 = BiconomyAP3 = BiconomyAP4 = BiconomyAP5 = 0
        BiconomyAP1V = BiconomyAP2V = BiconomyAP3V = BiconomyAP4V = BiconomyAP5V = 0
        BiconomyBP1 = BiconomyBP2 = BiconomyBP3 = BiconomyBP4 = BiconomyBP5 = 0
        BiconomyBP1V = BiconomyBP2V = BiconomyBP3V = BiconomyBP4V = BiconomyBP5V = 0
        BiconomyLTPV = 0
        BiconomyLTP = 0
        BiconomyLTPTM = 0
        BiconomyLTPT = None

        XTOBTM = 0
        XTOBT = None
        XTBP1 = XTBP2 = XTBP3 = XTBP4 = XTBP5 = 0
        XTBP1V = XTBP2V = XTBP3V = XTBP4V = XTBP5V = 0
        XTAP1 = XTAP2 = XTAP3 = XTAP4 = XTAP5 = 0
        XTAP1V = XTAP2V = XTAP3V = XTAP4V = XTAP5V = 0
        XTLTPTM = 0
        XTLTPT = None
        XTLTP = 0

        BitflyerBP1 = BitflyerBP2 = BitflyerBP3 = BitflyerBP4 = BitflyerBP5 = 0
        BitflyerBP1V = BitflyerBP2V = BitflyerBP3V = BitflyerBP4V = BitflyerBP5V = 0
        BitflyerAP1 = BitflyerAP2 = BitflyerAP3 = BitflyerAP4 = BitflyerAP5 = 0
        BitflyerAP1V = BitflyerAP2V = BitflyerAP3V = BitflyerAP4V = BitflyerAP5V = 0
        BitflyerLTP = 0
        BitflyerLTPV = 0
        BitflyerLTPT = 0

        CoinWAP1 = CoinWAP2 = CoinWAP3 = CoinWAP4 = CoinWAP5 = CoinWBP1 = CoinWBP2 = CoinWBP3 = CoinWBP4 = CoinWBP5 = 0
        CoinWAP1V = CoinWAP2V = CoinWAP3V = CoinWAP4V = CoinWAP5V = CoinWBP1V = CoinWBP2V = CoinWBP3V = CoinWBP4V = CoinWBP5V = 0
        CoinWLTP = 0

        ToobitOBTM = 0
        ToobitBP1 = ToobitBP2 = ToobitBP3 = ToobitBP4 = ToobitBP5 = ToobitAP1 = ToobitAP2 = ToobitAP3 = ToobitAP4 = ToobitAP5 = 0
        ToobitBP1V = ToobitBP2V = ToobitBP3V = ToobitBP4V = ToobitBP5V = ToobitAP1V = ToobitAP2V = ToobitAP3V = ToobitAP4V = ToobitAP5V = 0
        ToobitLTP = 0
        ToobitLTPV = 0
        ToobitLTPTm = 0

        TapbitAP1 = TapbitAP2 = TapbitAP3 = TapbitAP4 = TapbitAP5 = TapbitBP1 = TapbitBP2 = TapbitBP3 = TapbitBP4 = TapbitBP5 = 0
        TapbitAP1V = TapbitAP2V = TapbitAP3V = TapbitAP4V = TapbitAP5V = TapbitBP1V = TapbitBP2V = TapbitBP3V = TapbitBP4V = TapbitBP5V = 0
        TapbitOBTM = 0
        TapbitLTP = 0

        Binance_Status, BinanceOBRes = responses[0]
        BybitStatus, BybitOBURLRes = responses[2]
        OKX_Status, OKXOBBURLRes = responses[4]
        Upbit_Status, UpbitLTPURLRes = responses[7]
        Kucoin_Status, KucoinOBURLRes = responses[8]
        Bitget_Status, BitgetOBURLRes = responses[10]
        Bitstamp_Status, BitstampOBURLRes = responses[12]
        Gemini_Status, GeminiOBURLRes = responses[38]
        Kraken_Status, KrakenOBURL_Res = responses[14]
        Gateio_Status, Gateio_url_Orderbook_res = responses[16]
        HTX_Status, HTXOBRes = responses[18]
        MEXC_Status, MEXCOBRes = responses[20]
        Lbank_Status, LbankOBRes = responses[22]
        Bitmart_Status, BitmartOBRes = responses[24]
        Deepcoin_Status, DeepcoinOBRes = responses[26]
        Bitfinex_Status, BitfinexOBRes = responses[28]
        BingX_Status, BingxOBRes = responses[30]
        OrangeX_Status, OrangeXOBRes = responses[32]
        Bitvenus_Status, BitvinusOBRes = responses[34]
        Biconomy_Status, BiconomyOBRes = responses[36]
        XT_Status, XTOBRes = responses[40]
        Bitflyer_Status, BitflyerOBURLRes = responses[42]
        CoinW_Status, CoinWOBRes = responses[44]
        Toobit_Status, ToobitOBRes = responses[46]
        TapBit_Status, TapbitOBRes = responses[48]

        # print(Binance_Status,BybitStatus,OKX_Status,Upbit_Status,Kucoin_Status,Bitget_Status,Bitstamp_Status,Gemini_Status,
        #       Kraken_Status,Gateio_Status,HTX_Status,MEXC_Status,Lbank_Status,Bitmart_Status,Deepcoin_Status, Bitfinex_Status,
        #       BingX_Status,OrangeX_Status,Bitvenus_Status,Biconomy_Status,XT_Status,Bitflyer_Status,CoinW_Status, Toobit_Status,
        #       TapBit_Status
        # )

        _, BinanceLTPURLRes = responses[1]
        _, BybitLTPURLRes = responses[3]
        _, OKXLTPURLRes = responses[5]
        _, UpbitOBURLRes = responses[6]
        _, KucoinLTPURLRes = responses[9]
        _, BitgetLTPURLRes = responses[11]
        _, BitstampLTPURLRes = responses[13]
        _, GeminiLTPURLRes = responses[39]
        _, KrakenLTP_Res = responses[15]
        _, Gateio_url_Last_trade_res = responses[17]
        _, HTXLTPURL_Res = responses[19]
        _, MEXCLTPURL_Res = responses[21]
        _, LbankLTPURL_Res = responses[23]
        _, BitmartLTPURL_Res = responses[25]
        _, DeepcoinLTPURL_Res = responses[27]
        _, BitfinexLTPURL_Res = responses[29]
        _, BingxLTPURL_Res = responses[31]
        _, OrangeXLTPURL_Res = responses[33]
        _, BitvenusLTPURL_Res = responses[35]
        _, BICONOMYLTPURL_Res = responses[37]
        _, XTLTPURL_Res = responses[41]
        _, BitflyerLTPURLRes = responses[43]
        _, CoinWLTPURL_Res = responses[45]
        _, ToobitLTPURL_Res = responses[47]
        _, TapbitLTPURL_Res = responses[49]


        try:
            if BinanceOBRes:
                BinanceBP1 = float(BinanceOBRes['bids'][0][0])
                BinanceBP2 = float(BinanceOBRes['bids'][1][0])
                BinanceBP3 = float(BinanceOBRes['bids'][2][0])
                BinanceBP4 = float(BinanceOBRes['bids'][3][0])
                BinanceBP5 = float(BinanceOBRes['bids'][4][0])
                BinanceBP1V = (float(BinanceOBRes['bids'][0][1]))
                BinanceBP2V = float(BinanceOBRes['bids'][1][1])
                BinanceBP3V = float(BinanceOBRes['bids'][2][1])
                BinanceBP4V = float(BinanceOBRes['bids'][3][1])
                BinanceBP5V = float(BinanceOBRes['bids'][4][1])
                BinanceAP1 = float(BinanceOBRes['asks'][0][0])
                BinanceAP2 = float(BinanceOBRes['asks'][1][0])
                BinanceAP3 = float(BinanceOBRes['asks'][2][0])
                BinanceAP4 = float(BinanceOBRes['asks'][3][0])
                BinanceAP5 = float(BinanceOBRes['asks'][4][0])
                BinanceAP1V = (float(BinanceOBRes['asks'][0][1]))
                BinanceAP2V = float(BinanceOBRes['asks'][1][1])
                BinanceAP3V = float(BinanceOBRes['asks'][2][1])
                BinanceAP4V = float(BinanceOBRes['asks'][3][1])
                BinanceAP5V = float(BinanceOBRes['asks'][4][1])

                if BinanceLTPURLRes:
                    BinanceLTP = float(BinanceLTPURLRes['lastPrice'])
                    BinanceLTPV = BinanceLTPURLRes['lastQty']
                    BinanceLTPTM = int(BinanceLTPURLRes['closeTime'])
                    BinanceLTPT = (BinanceLTPTM)
        except Exception as e:

            Binance_Status = 400
        try:

            if BybitOBURLRes:
                BybitBP1 = float(BybitOBURLRes['result'][0]['price'])
                BybitBP2 = float(BybitOBURLRes['result'][1]['price'])
                BybitBP3 = float(BybitOBURLRes['result'][2]['price'])
                BybitBP4 = float(BybitOBURLRes['result'][3]['price'])
                BybitBP5 = float(BybitOBURLRes['result'][4]['price'])
                BybitBP1V = (float(BybitOBURLRes['result'][0]['size']))
                BybitBP2V = float(BybitOBURLRes['result'][1]['size'])
                BybitBP3V = float(BybitOBURLRes['result'][2]['size'])
                BybitBP4V = float(BybitOBURLRes['result'][3]['size'])
                BybitBP5V = float(BybitOBURLRes['result'][4]['size'])
                BybitAP1 = float(BybitOBURLRes['result'][5]['price'])
                BybitAP2 = float(BybitOBURLRes['result'][6]['price'])
                BybitAP3 = float(BybitOBURLRes['result'][7]['price'])
                BybitAP4 = float(BybitOBURLRes['result'][8]['price'])
                BybitAP5 = float(BybitOBURLRes['result'][9]['price'])
                BybitAP1V = (float(BybitOBURLRes['result'][5]['size']))
                BybitAP2V = float(BybitOBURLRes['result'][6]['size'])
                BybitAP3V = float(BybitOBURLRes['result'][7]['size'])
                BybitAP4V = float(BybitOBURLRes['result'][8]['size'])
                BybitAP5V = float(BybitOBURLRes['result'][9]['size'])
                BybitOBTM = float(BybitOBURLRes['time_now'])
                BybitOBT = (BybitOBTM)

                if BybitLTPURLRes:
                    BybitLTP = float(BybitLTPURLRes['result'][0]['last_price'])
                    BybitLTPV = 0
                    BybitLTPTM = float(BybitLTPURLRes['time_now'])
                    BybitLTPT = (BybitLTPTM)
        except Exception as e:

            BybitStatus = 400
        try:

            if OKXOBBURLRes:
                OKXAP1 = float(OKXOBBURLRes['data'][0]['asks'][0][0])
                OKXAP2 = float(OKXOBBURLRes['data'][0]['asks'][1][0])
                OKXAP3 = float(OKXOBBURLRes['data'][0]['asks'][2][0])
                OKXAP4 = float(OKXOBBURLRes['data'][0]['asks'][3][0])
                OKXAP5 = float(OKXOBBURLRes['data'][0]['asks'][4][0])
                OKXAP1V = (float(OKXOBBURLRes['data'][0]['asks'][0][1]))
                OKXAP2V = float(OKXOBBURLRes['data'][0]['asks'][1][1])
                OKXAP3V = float(OKXOBBURLRes['data'][0]['asks'][2][1])
                OKXAP4V = float(OKXOBBURLRes['data'][0]['asks'][3][1])
                OKXAP5V = float(OKXOBBURLRes['data'][0]['asks'][4][1])
                OKXBP1 = float(OKXOBBURLRes['data'][0]['bids'][0][0])
                OKXBP2 = float(OKXOBBURLRes['data'][0]['bids'][1][0])
                OKXBP3 = float(OKXOBBURLRes['data'][0]['bids'][2][0])
                OKXBP4 = float(OKXOBBURLRes['data'][0]['bids'][3][0])
                OKXBP5 = float(OKXOBBURLRes['data'][0]['bids'][4][0])
                OKXBP1V = (float(OKXOBBURLRes['data'][0]['bids'][0][1]))
                OKXBP2V = float(OKXOBBURLRes['data'][0]['bids'][1][1])
                OKXBP3V = float(OKXOBBURLRes['data'][0]['bids'][2][1])
                OKXBP4V = float(OKXOBBURLRes['data'][0]['bids'][3][1])
                OKXBP5V = float(OKXOBBURLRes['data'][0]['bids'][4][1])
                OKXOBTM = int(OKXOBBURLRes['data'][0]['ts'])
                OKXOBT = (OKXOBTM)

                if OKXLTPURLRes:
                    OKXLTP = float(OKXLTPURLRes['data'][0]['last'])
                    OKXLTPV = OKXLTPURLRes['data'][0]['lastSz']
                    OKXLTPTM = int(OKXLTPURLRes['data'][0]['ts'])
                    OKXLTPT = (OKXLTPTM)
        except Exception as e:

            OKX_Status = 400
        try:

            if UpbitOBURLRes:
                UpbitOBTM = int(UpbitOBURLRes[0]['timestamp'])
                UpbitOBT = (UpbitOBTM)
                UpbitAP1 = float(UpbitOBURLRes[0]['orderbook_units'][0]['ask_price'])
                UpbitBP1 = float(UpbitOBURLRes[0]['orderbook_units'][0]['bid_price'])
                UpbitAP1V = (float(UpbitOBURLRes[0]['orderbook_units'][0]['ask_size']))
                UpbitBP1V = (float(UpbitOBURLRes[0]['orderbook_units'][0]['bid_size']))
                UpbitAP2 = float(UpbitOBURLRes[0]['orderbook_units'][1]['ask_price'])
                UpbitBP2 = float(UpbitOBURLRes[0]['orderbook_units'][1]['bid_price'])
                UpbitAP2V = float(UpbitOBURLRes[0]['orderbook_units'][1]['ask_size'])
                UpbitBP2V = float(UpbitOBURLRes[0]['orderbook_units'][1]['bid_size'])
                UpbitAP3 = float(UpbitOBURLRes[0]['orderbook_units'][2]['ask_price'])
                UpbitBP3 = float(UpbitOBURLRes[0]['orderbook_units'][2]['bid_price'])
                UpbitAP3V = float(UpbitOBURLRes[0]['orderbook_units'][2]['ask_size'])
                UpbitBP3V = float(UpbitOBURLRes[0]['orderbook_units'][2]['bid_size'])
                UpbitAP4 = float(UpbitOBURLRes[0]['orderbook_units'][3]['ask_price'])
                UpbitBP4 = float(UpbitOBURLRes[0]['orderbook_units'][3]['bid_price'])
                UpbitAP4V = float(UpbitOBURLRes[0]['orderbook_units'][3]['ask_size'])
                UpbitBP4V = float(UpbitOBURLRes[0]['orderbook_units'][3]['bid_size'])
                UpbitAP5 = float(UpbitOBURLRes[0]['orderbook_units'][4]['ask_price'])
                UpbitBP5 = float(UpbitOBURLRes[0]['orderbook_units'][4]['bid_price'])
                UpbitAP5V = float(UpbitOBURLRes[0]['orderbook_units'][4]['ask_size'])
                UpbitBP5V = float(UpbitOBURLRes[0]['orderbook_units'][4]['bid_size'])

                UpbitLTP = float(UpbitLTPURLRes[0]['trade_price'])
                UpbitLTPV = UpbitLTPURLRes[0]['trade_volume']
                UpbitLTPTM = UpbitLTPURLRes[0]['trade_timestamp']
                UpbitLTPT = (UpbitLTPTM)
        except Exception as e:

            Upbit_Status = 400
        try:

            if KucoinOBURLRes:
                KucoinOBTM = KucoinOBURLRes['data']['time']
                KucoinOBT = (KucoinOBTM)
                KucoinBP1 = float(KucoinOBURLRes['data']['bids'][0][0])
                KucoinBP2 = float(KucoinOBURLRes['data']['bids'][1][0])
                KucoinBP3 = float(KucoinOBURLRes['data']['bids'][2][0])
                KucoinBP4 = float(KucoinOBURLRes['data']['bids'][3][0])
                KucoinBP5 = float(KucoinOBURLRes['data']['bids'][4][0])
                KucoinBP1V = (float(KucoinOBURLRes['data']['bids'][0][1]))
                KucoinBP2V = float(KucoinOBURLRes['data']['bids'][1][1])
                KucoinBP3V = float(KucoinOBURLRes['data']['bids'][2][1])
                KucoinBP4V = float(KucoinOBURLRes['data']['bids'][3][1])
                KucoinBP5V = float(KucoinOBURLRes['data']['bids'][4][1])
                KucoinAP1 = float(KucoinOBURLRes['data']['asks'][0][0])
                KucoinAP2 = float(KucoinOBURLRes['data']['asks'][1][0])
                KucoinAP3 = float(KucoinOBURLRes['data']['asks'][2][0])
                KucoinAP4 = float(KucoinOBURLRes['data']['asks'][3][0])
                KucoinAP5 = float(KucoinOBURLRes['data']['asks'][4][0])
                KucoinAP1V = (float(KucoinOBURLRes['data']['asks'][0][1]))
                KucoinAP2V = float(KucoinOBURLRes['data']['asks'][1][1])
                KucoinAP3V = float(KucoinOBURLRes['data']['asks'][2][1])
                KucoinAP4V = float(KucoinOBURLRes['data']['asks'][3][1])
                KucoinAP5V = float(KucoinOBURLRes['data']['asks'][4][1])

                KucoinLTP = float(KucoinLTPURLRes['data']['last'])
                KucoinLTPV = 0
                KucoinLTPTM = KucoinLTPURLRes['data']['time']
                KucoinLTPT = (KucoinLTPTM)
        except Exception as e:

            Kucoin_Status = 400
        try:

            if BitgetOBURLRes:
                BitgetOBTM = BitgetOBURLRes['requestTime']
                BitgetOBT = (BitgetOBTM)
                BitgetAP1 = float(BitgetOBURLRes['data']['asks'][0][0])
                BitgetAP2 = float(BitgetOBURLRes['data']['asks'][1][0])
                BitgetAP3 = float(BitgetOBURLRes['data']['asks'][2][0])
                BitgetAP4 = float(BitgetOBURLRes['data']['asks'][3][0])
                BitgetAP5 = float(BitgetOBURLRes['data']['asks'][4][0])
                BitgetAP1V = (float(BitgetOBURLRes['data']['asks'][0][1]))
                BitgetAP2V = float(BitgetOBURLRes['data']['asks'][1][1])
                BitgetAP3V = float(BitgetOBURLRes['data']['asks'][2][1])
                BitgetAP4V = float(BitgetOBURLRes['data']['asks'][3][1])
                BitgetAP5V = float(BitgetOBURLRes['data']['asks'][4][1])
                BitgetBP1 = float(BitgetOBURLRes['data']['bids'][0][0])
                BitgetBP2 = float(BitgetOBURLRes['data']['bids'][1][0])
                BitgetBP3 = float(BitgetOBURLRes['data']['bids'][2][0])
                BitgetBP4 = float(BitgetOBURLRes['data']['bids'][3][0])
                BitgetBP5 = float(BitgetOBURLRes['data']['bids'][4][0])
                BitgetBP1V = (float(BitgetOBURLRes['data']['bids'][0][1]))
                BitgetBP2V = float(BitgetOBURLRes['data']['bids'][1][1])
                BitgetBP3V = float(BitgetOBURLRes['data']['bids'][2][1])
                BitgetBP4V = float(BitgetOBURLRes['data']['bids'][3][1])
                BitgetBP5V = float(BitgetOBURLRes['data']['bids'][4][1])

                BitgetLTP = float(BitgetLTPURLRes['data'][0]['lastPr'])
                BitgetLTPTM = int(BitgetLTPURLRes['data'][0]['ts'])
                BitgetLTPV = 0
                BitgetLTPT = (BitgetLTPTM)
        except Exception as e:

            Bitget_Status = 400
        try:

            if BitstampOBURLRes:
                BitstampOBTM = int(BitstampOBURLRes['timestamp'])
                BitstampOBT = (BitstampOBTM)
                BitstampBP1 = float(BitstampOBURLRes['bids'][0][0])
                BitstampBP2 = float(BitstampOBURLRes['bids'][1][0])
                BitstampBP3 = float(BitstampOBURLRes['bids'][2][0])
                BitstampBP4 = float(BitstampOBURLRes['bids'][3][0])
                BitstampBP5 = float(BitstampOBURLRes['bids'][4][0])
                BitstampBP1V = (float(BitstampOBURLRes['bids'][0][1]))
                BitstampBP2V = float(BitstampOBURLRes['bids'][1][1])
                BitstampBP3V = float(BitstampOBURLRes['bids'][2][1])
                BitstampBP4V = float(BitstampOBURLRes['bids'][3][1])
                BitstampBP5V = float(BitstampOBURLRes['bids'][4][1])
                BitstampAP1 = float(BitstampOBURLRes['asks'][0][0])
                BitstampAP2 = float(BitstampOBURLRes['asks'][1][0])
                BitstampAP3 = float(BitstampOBURLRes['asks'][2][0])
                BitstampAP4 = float(BitstampOBURLRes['asks'][3][0])
                BitstampAP5 = float(BitstampOBURLRes['asks'][4][0])
                BitstampAP1V = (float(BitstampOBURLRes['asks'][0][1]))
                BitstampAP2V = float(BitstampOBURLRes['asks'][1][1])
                BitstampAP3V = float(BitstampOBURLRes['asks'][2][1])
                BitstampAP4V = float(BitstampOBURLRes['asks'][3][1])
                BitstampAP5V = float(BitstampOBURLRes['asks'][4][1])

                BitstampLTP = float(BitstampLTPURLRes['last'])
                BitstampLTPV = BitstampLTPURLRes['volume']
                BitstampLTPTM = int(BitstampLTPURLRes['timestamp'])
                BitstampLTPT = (BitstampLTPTM)
        except Exception as e:

            Bitstamp_Status = 400
        try:

            if GeminiOBURLRes:
                GeminiOBTM = int(GeminiOBURLRes['bids'][0]['timestamp'])
                GeminiOBT = (GeminiOBTM)
                GeminiBP1 = float(GeminiOBURLRes['bids'][0]['price'])
                GeminiBP2 = float(GeminiOBURLRes['bids'][1]['price'])
                GeminiBP3 = float(GeminiOBURLRes['bids'][2]['price'])
                GeminiBP4 = float(GeminiOBURLRes['bids'][3]['price'])
                GeminiBP5 = float(GeminiOBURLRes['bids'][4]['price'])
                GeminiBP1V = (float(GeminiOBURLRes['bids'][0]['amount']))
                GeminiBP2V = float(GeminiOBURLRes['bids'][1]['amount'])
                GeminiBP3V = float(GeminiOBURLRes['bids'][2]['amount'])
                GeminiBP4V = float(GeminiOBURLRes['bids'][3]['amount'])
                GeminiBP5V = float(GeminiOBURLRes['bids'][4]['amount'])
                GeminiAP1 = float(GeminiOBURLRes['asks'][0]['price'])
                GeminiAP2 = float(GeminiOBURLRes['asks'][1]['price'])
                GeminiAP3 = float(GeminiOBURLRes['asks'][2]['price'])
                GeminiAP4 = float(GeminiOBURLRes['asks'][3]['price'])
                GeminiAP5 = float(GeminiOBURLRes['asks'][4]['price'])
                GeminiAP1V = (float(GeminiOBURLRes['asks'][0]['amount']))
                GeminiAP2V = float(GeminiOBURLRes['asks'][1]['amount'])
                GeminiAP3V = float(GeminiOBURLRes['asks'][2]['amount'])
                GeminiAP4V = float(GeminiOBURLRes['asks'][3]['amount'])
                GeminiAP5V = float(GeminiOBURLRes['asks'][4]['amount'])

                GeminiLTP = float(GeminiLTPURLRes['last'])
                GeminiLTPV = GeminiLTPURLRes['volume']['BTC']
                GeminiLTPTM = GeminiLTPURLRes['volume']['timestamp']
                GeminiLTPT = (GeminiLTPTM)
        except Exception as e:

            Gemini_Status = 400
        try:

            if KrakenOBURL_Res:
                KrakenAP1 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][0])
                KrakenAP2 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][1][0])
                KrakenAP3 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][2][0])
                KrakenAP4 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][3][0])
                KrakenAP5 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][4][0])
                KrakenAPV1 = (KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][1])
                KrakenAPV2 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][1][1]
                KrakenAPV3 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][2][1]
                KrakenAPV4 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][3][1]
                KrakenAPV5 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][4][1]
                KrakenBP1 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][0][0])
                KrakenBP2 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][1][0])
                KrakenBP3 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][2][0])
                KrakenBP4 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][3][0])
                KrakenBP5 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][4][0])
                KrakenBPV1 = (KrakenOBURL_Res['result']['XBTUSDT']['bids'][0][1])
                KrakenBPV2 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][1][1]
                KrakenBPV3 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][2][1]
                KrakenBPV4 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][3][1]
                KrakenBPV5 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][4][1]
                KrakenOBTM = KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][2]
                KrakenOBT = (KrakenOBTM)

                KrakenLTP = float(KrakenLTP_Res['result']['XBTUSDT'][0][0])
                KrakenLTPV = KrakenLTP_Res['result']['XBTUSDT'][0][1]
                KrakenLTPTM = int(KrakenLTP_Res['result']['XBTUSDT'][0][2])
                KrakenLTPT = (KrakenLTPTM)
        except Exception as e:

            Kraken_Status = 400
        try:

            if Gateio_url_Orderbook_res:
                GateioAP1 = float(Gateio_url_Orderbook_res['asks'][0][0])
                GateioAP2 = float(Gateio_url_Orderbook_res['asks'][1][0])
                GateioAP3 = float(Gateio_url_Orderbook_res['asks'][2][0])
                GateioAP4 = float(Gateio_url_Orderbook_res['asks'][3][0])
                GateioAP5 = float(Gateio_url_Orderbook_res['asks'][4][0])
                GateioAPV1 = (float(Gateio_url_Orderbook_res['asks'][0][1]))
                GateioAPV2 = float(Gateio_url_Orderbook_res['asks'][1][1])
                GateioAPV3 = float(Gateio_url_Orderbook_res['asks'][2][1])
                GateioAPV4 = float(Gateio_url_Orderbook_res['asks'][3][1])
                GateioAPV5 = float(Gateio_url_Orderbook_res['asks'][4][1])
                GateioBP1 = float(Gateio_url_Orderbook_res['bids'][0][0])
                GateioBP2 = float(Gateio_url_Orderbook_res['bids'][1][0])
                GateioBP3 = float(Gateio_url_Orderbook_res['bids'][2][0])
                GateioBP4 = float(Gateio_url_Orderbook_res['bids'][3][0])
                GateioBP5 = float(Gateio_url_Orderbook_res['bids'][4][0])
                GateioBPV1 = (float(Gateio_url_Orderbook_res['bids'][0][1]))
                GateioBPV2 = float(Gateio_url_Orderbook_res['bids'][1][1])
                GateioBPV3 = float(Gateio_url_Orderbook_res['bids'][2][1])
                GateioBPV4 = float(Gateio_url_Orderbook_res['bids'][3][1])
                GateioBPV5 = float(Gateio_url_Orderbook_res['bids'][4][1])

                GateioLTP = float(Gateio_url_Last_trade_res['last'])
        except Exception as e:

            Gateio_Status = 400
        try:

            if HTXOBRes:
                HTXOBTM = int(HTXOBRes['ts'])
                HTXOBT = HTXOBTM
                HTXBP1 = float(HTXOBRes['tick']['bids'][0][0])
                HTXBP2 = float(HTXOBRes['tick']['bids'][1][0])
                HTXBP3 = float(HTXOBRes['tick']['bids'][2][0])
                HTXBP4 = float(HTXOBRes['tick']['bids'][3][0])
                HTXBP5 = float(HTXOBRes['tick']['bids'][4][0])
                HTXBP1V = (float(HTXOBRes['tick']['bids'][0][1]))
                HTXBP2V = float(HTXOBRes['tick']['bids'][1][1])
                HTXBP3V = float(HTXOBRes['tick']['bids'][2][1])
                HTXBP4V = float(HTXOBRes['tick']['bids'][3][1])
                HTXBP5V = float(HTXOBRes['tick']['bids'][4][1])
                HTXAP1 = float(HTXOBRes['tick']['asks'][0][0])
                HTXAP2 = float(HTXOBRes['tick']['asks'][1][0])
                HTXAP3 = float(HTXOBRes['tick']['asks'][2][0])
                HTXAP4 = float(HTXOBRes['tick']['asks'][3][0])
                HTXAP5 = float(HTXOBRes['tick']['asks'][4][0])
                HTXAP1V = (float(HTXOBRes['tick']['asks'][0][1]))
                HTXAP2V = float(HTXOBRes['tick']['asks'][1][1])
                HTXAP3V = float(HTXOBRes['tick']['asks'][2][1])
                HTXAP4V = float(HTXOBRes['tick']['asks'][3][1])
                HTXAP5V = float(HTXOBRes['tick']['asks'][4][1])

                HTXLTPTM = int(HTXLTPURL_Res['tick']['ts'])
                HTXLTPT = HTXLTPTM
                HTXLTP = float(HTXLTPURL_Res['tick']['data'][0]['price'])
                HTXLTPV = HTXLTPURL_Res['tick']['data'][0]['amount']
        except Exception as e:

            HTX_Status = 400
        try:

            if MEXCOBRes:
                MEXCBP1 = float(MEXCOBRes['bids'][0][0])
                MEXCBP2 = float(MEXCOBRes['bids'][1][0])
                MEXCBP3 = float(MEXCOBRes['bids'][2][0])
                MEXCBP4 = float(MEXCOBRes['bids'][3][0])
                MEXCBP5 = float(MEXCOBRes['bids'][4][0])
                MEXCBP1V = (float(MEXCOBRes['bids'][0][1]))
                MEXCBP2V = float(MEXCOBRes['bids'][1][1])
                MEXCBP3V = float(MEXCOBRes['bids'][2][1])
                MEXCBP4V = float(MEXCOBRes['bids'][3][1])
                MEXCBP5V = float(MEXCOBRes['bids'][4][1])
                MEXCAP1 = float(MEXCOBRes['asks'][0][0])
                MEXCAP2 = float(MEXCOBRes['asks'][1][0])
                MEXCAP3 = float(MEXCOBRes['asks'][2][0])
                MEXCAP4 = float(MEXCOBRes['asks'][3][0])
                MEXCAP5 = float(MEXCOBRes['asks'][4][0])
                MEXCAP1V = (float(MEXCOBRes['asks'][0][1]))
                MEXCAP2V = float(MEXCOBRes['asks'][1][1])
                MEXCAP3V = float(MEXCOBRes['asks'][2][1])
                MEXCAP4V = float(MEXCOBRes['asks'][3][1])
                MEXCAP5V = float(MEXCOBRes['asks'][4][1])
                MEXCOBTM = int(MEXCOBRes['timestamp'])
                MEXCOBT = MEXCOBTM

                MEXCLTP = float(MEXCLTPURL_Res[0]['price'])
                MEXCLTPV = MEXCLTPURL_Res[0]['qty']
                MEXCLTPTM = int(MEXCLTPURL_Res[0]['time'])
                MEXCLTPT = MEXCLTPTM
        except Exception as e:

            MEXC_Status = 400
        try:

            if LbankOBRes:
                LbankAP1 = float(LbankOBRes['data']['asks'][0][0])
                LbankAP2 = LbankOBRes['data']['asks'][1][0]
                LbankAP3 = LbankOBRes['data']['asks'][2][0]
                LbankAP4 = LbankOBRes['data']['asks'][3][0]
                LbankAP5 = LbankOBRes['data']['asks'][4][0]
                LbankAP1V = (LbankOBRes['data']['asks'][0][1])
                LbankAP2V = LbankOBRes['data']['asks'][1][1]
                LbankAP3V = LbankOBRes['data']['asks'][2][1]
                LbankAP4V = LbankOBRes['data']['asks'][3][1]
                LbankAP5V = LbankOBRes['data']['asks'][4][1]
                LbankBP1 = float(LbankOBRes['data']['bids'][0][0])
                LbankBP2 = LbankOBRes['data']['bids'][1][0]
                LbankBP3 = LbankOBRes['data']['bids'][2][0]
                LbankBP4 = LbankOBRes['data']['bids'][3][0]
                LbankBP5 = LbankOBRes['data']['bids'][4][0]
                LbankBP1V = (LbankOBRes['data']['bids'][0][1])
                LbankBP2V = LbankOBRes['data']['bids'][1][1]
                LbankBP3V = LbankOBRes['data']['bids'][2][1]
                LbankBP4V = LbankOBRes['data']['bids'][3][1]
                LbankBP5V = LbankOBRes['data']['bids'][4][1]
                LbankOBTM = int(LbankOBRes['data']['timestamp'])
                LbankOBT = LbankOBTM

                LbankLTP = float(LbankLTPURL_Res['data'][0]['ticker']['latest'])
                LbankLTPTM = LbankLTPURL_Res['data'][0]['timestamp']
                LbankLTPT = LbankLTPTM
        except Exception as e:

            Lbank_Status = 400
        try:

            if BitmartOBRes:
                BitmartOBTM = int(BitmartOBRes['data']['ts'])
                BitmartOBT = BitmartOBTM
                BitmartAP1 = float(BitmartOBRes['data']['asks'][0][0])
                BitmartAP2 = BitmartOBRes['data']['asks'][1][0]
                BitmartAP3 = BitmartOBRes['data']['asks'][2][0]
                BitmartAP4 = BitmartOBRes['data']['asks'][3][0]
                BitmartAP5 = BitmartOBRes['data']['asks'][4][0]
                BitmartAP1V = (BitmartOBRes['data']['asks'][0][1])
                BitmartAP2V = BitmartOBRes['data']['asks'][1][1]
                BitmartAP3V = BitmartOBRes['data']['asks'][2][1]
                BitmartAP4V = BitmartOBRes['data']['asks'][3][1]
                BitmartAP5V = BitmartOBRes['data']['asks'][4][1]
                BitmartBP1 = float(BitmartOBRes['data']['bids'][0][0])
                BitmartBP2 = BitmartOBRes['data']['bids'][1][0]
                BitmartBP3 = BitmartOBRes['data']['bids'][2][0]
                BitmartBP4 = BitmartOBRes['data']['bids'][3][0]
                BitmartBP5 = BitmartOBRes['data']['bids'][4][0]
                BitmartBP1V = (BitmartOBRes['data']['bids'][0][1])
                BitmartBP2V = BitmartOBRes['data']['bids'][1][1]
                BitmartBP3V = BitmartOBRes['data']['bids'][2][1]
                BitmartBP4V = BitmartOBRes['data']['bids'][3][1]
                BitmartBP5V = BitmartOBRes['data']['bids'][4][1]

                BitmartLTPTM = int(BitmartLTPURL_Res['data'][0][1])
                BitmartLTPT = BitmartLTPTM
                BitmartLTP = float(BitmartLTPURL_Res['data'][0][2])
                BitmartLTPV = BitmartLTPURL_Res['data'][0][3]
        except Exception as e:

            Bitmart_Status = 400
        try:

            if DeepcoinOBRes:
                DeepcoinBP1 = float(DeepcoinOBRes['data']['bids'][0][0])
                DeepcoinBP2 = DeepcoinOBRes['data']['bids'][1][0]
                DeepcoinBP3 = DeepcoinOBRes['data']['bids'][2][0]
                DeepcoinBP4 = DeepcoinOBRes['data']['bids'][3][0]
                DeepcoinBP5 = DeepcoinOBRes['data']['bids'][4][0]
                DeepcoinBP1V = (DeepcoinOBRes['data']['bids'][0][1])
                DeepcoinBP2V = DeepcoinOBRes['data']['bids'][1][1]
                DeepcoinBP3V = DeepcoinOBRes['data']['bids'][2][1]
                DeepcoinBP4V = DeepcoinOBRes['data']['bids'][3][1]
                DeepcoinBP5V = DeepcoinOBRes['data']['bids'][4][1]
                DeepcoinAP1 = float(DeepcoinOBRes['data']['asks'][0][0])
                DeepcoinAP2 = DeepcoinOBRes['data']['asks'][1][0]
                DeepcoinAP3 = DeepcoinOBRes['data']['asks'][2][0]
                DeepcoinAP4 = DeepcoinOBRes['data']['asks'][3][0]
                DeepcoinAP5 = DeepcoinOBRes['data']['asks'][4][0]
                DeepcoinAP1V = (DeepcoinOBRes['data']['asks'][0][1])
                DeepcoinAP2V = DeepcoinOBRes['data']['asks'][1][1]
                DeepcoinAP3V = DeepcoinOBRes['data']['asks'][2][1]
                DeepcoinAP4V = DeepcoinOBRes['data']['asks'][3][1]
                DeepcoinAP5V = DeepcoinOBRes['data']['asks'][4][1]

                DeepcoinLTP = float(DeepcoinLTPURL_Res['data'][30]['last'])
                DeepcoinLTPTM = int(DeepcoinLTPURL_Res['data'][30]['ts'])
                DeepcoinLTPT = DeepcoinLTPTM
        except Exception as e:

            Deepcoin_Status = 400
        try:

            if BitfinexOBRes:
                BitfinexBP1 = float(BitfinexOBRes[0][0])
                BitfinexBP2 = BitfinexOBRes[1][0]
                BitfinexBP3 = BitfinexOBRes[2][0]
                BitfinexBP4 = BitfinexOBRes[3][0]
                BitfinexBP5 = BitfinexOBRes[4][0]
                BitfinexBP1V = (BitfinexOBRes[0][2])
                BitfinexBP2V = BitfinexOBRes[1][2]
                BitfinexBP3V = BitfinexOBRes[2][2]
                BitfinexBP4V = BitfinexOBRes[3][2]
                BitfinexBP5V = BitfinexOBRes[4][2]
                BitfinexAP1 = float(BitfinexOBRes[25][0])
                BitfinexAP2 = BitfinexOBRes[26][0]
                BitfinexAP3 = BitfinexOBRes[27][0]
                BitfinexAP4 = BitfinexOBRes[28][0]
                BitfinexAP5 = BitfinexOBRes[29][0]
                BitfinexAP1V = (BitfinexOBRes[25][2])
                BitfinexAP2V = BitfinexOBRes[26][2]
                BitfinexAP3V = BitfinexOBRes[27][2]
                BitfinexAP4V = BitfinexOBRes[28][2]
                BitfinexAP5V = BitfinexOBRes[29][2]

                BitfinexLTP = float(BitfinexLTPURL_Res[0][7])
        except Exception as e:

            Bitfinex_Status = 400
        try:

            if BingxOBRes:
                BingxOBTM = int(BingxOBRes['data']['T'])
                BingxOBT = BingxOBTM
                BingXBP1 = float(BingxOBRes['data']['bidsCoin'][0][0])
                BingXBP2 = BingxOBRes['data']['bidsCoin'][1][0]
                BingXBP3 = BingxOBRes['data']['bidsCoin'][2][0]
                BingXBP4 = BingxOBRes['data']['bidsCoin'][3][0]
                BingXBP5 = BingxOBRes['data']['bidsCoin'][4][0]
                BingXAP1 = float(BingxOBRes['data']['asksCoin'][0][0])
                BingXAP2 = BingxOBRes['data']['asksCoin'][1][0]
                BingXAP3 = BingxOBRes['data']['asksCoin'][2][0]
                BingXAP4 = BingxOBRes['data']['asksCoin'][3][0]
                BingXAP5 = BingxOBRes['data']['asksCoin'][4][0]
                BingXBP1V = (BingxOBRes['data']['bidsCoin'][0][1])
                BingXBP2V = BingxOBRes['data']['bidsCoin'][1][1]
                BingXBP3V = BingxOBRes['data']['bidsCoin'][2][1]
                BingXBP4V = BingxOBRes['data']['bidsCoin'][3][1]
                BingXBP5V = BingxOBRes['data']['bidsCoin'][4][1]
                BingXAP1V = (BingxOBRes['data']['asksCoin'][0][1])
                BingXAP2V = BingxOBRes['data']['asksCoin'][1][1]
                BingXAP3V = BingxOBRes['data']['asksCoin'][2][1]
                BingXAP4V = BingxOBRes['data']['asksCoin'][3][1]
                BingXAP5V = BingxOBRes['data']['asksCoin'][4][1]

                BingXLTPTM = int(BingxLTPURL_Res['data'][0]['time'])
                BingXLTPT = BingXLTPTM
                BingXLTP = float(BingxLTPURL_Res['data'][0]['price'])
                BingXLTPV = BingxLTPURL_Res['data'][0]['qty']
        except Exception as e:

            BingX_Status = 400
        try:

            if OrangeXOBRes:
                OrangeXAP1 = float(OrangeXOBRes['result']['asks'][0][0])
                OrangeXAP2 = OrangeXOBRes['result']['asks'][1][0]
                OrangeXAP3 = OrangeXOBRes['result']['asks'][2][0]
                OrangeXAP4 = OrangeXOBRes['result']['asks'][3][0]
                OrangeXAP5 = OrangeXOBRes['result']['asks'][4][0]
                OrangeXAP1V = (OrangeXOBRes['result']['asks'][0][1])
                OrangeXAP2V = OrangeXOBRes['result']['asks'][1][1]
                OrangeXAP3V = OrangeXOBRes['result']['asks'][2][1]
                OrangeXAP4V = OrangeXOBRes['result']['asks'][3][1]
                OrangeXAP5V = OrangeXOBRes['result']['asks'][4][1]
                OrangeXBP1 = float(OrangeXOBRes['result']['bids'][0][0])
                OrangeXBP2 = OrangeXOBRes['result']['bids'][1][0]
                OrangeXBP3 = OrangeXOBRes['result']['bids'][2][0]
                OrangeXBP4 = OrangeXOBRes['result']['bids'][3][0]
                OrangeXBP5 = OrangeXOBRes['result']['bids'][4][0]
                OrangeXBP1V = (OrangeXOBRes['result']['bids'][0][1])
                OrangeXBP2V = OrangeXOBRes['result']['bids'][1][1]
                OrangeXBP3V = OrangeXOBRes['result']['bids'][2][1]
                OrangeXBP4V = OrangeXOBRes['result']['bids'][3][1]
                OrangeXBP5V = OrangeXOBRes['result']['bids'][4][1]
                OrangeXOBTM = int(OrangeXOBRes['result']['timestamp'])
                OrangeXOBT = OrangeXOBTM

                OrangeXLTP = float(OrangeXLTPURL_Res['result'][0]['last_price'])
                OrangeXLTPTM = int(OrangeXLTPURL_Res['result'][0]['timestamp'])
                OrangeXLTPT = OrangeXLTPTM
        except Exception as e:

            OrangeX_Status = 400
        try:

            if BitvinusOBRes:
                BitvenusOBTM = int(BitvinusOBRes['time'])
                BitvenusOBT = BitvenusOBTM
                BitvenusBP1 = float(BitvinusOBRes['bids'][0][0])
                BitvenusBP2 = BitvinusOBRes['bids'][1][0]
                BitvenusBP3 = BitvinusOBRes['bids'][2][0]
                BitvenusBP4 = BitvinusOBRes['bids'][3][0]
                BitvenusBP5 = BitvinusOBRes['bids'][4][0]
                BitvenusBP1V = (BitvinusOBRes['bids'][0][1])
                BitvenusBP2V = BitvinusOBRes['bids'][1][1]
                BitvenusBP3V = BitvinusOBRes['bids'][2][1]
                BitvenusBP4V = BitvinusOBRes['bids'][3][1]
                BitvenusBP5V = BitvinusOBRes['bids'][4][1]
                BitvenusAP1 = float(BitvinusOBRes['asks'][0][0])
                BitvenusAP2 = BitvinusOBRes['asks'][1][0]
                BitvenusAP3 = BitvinusOBRes['asks'][2][0]
                BitvenusAP4 = BitvinusOBRes['asks'][3][0]
                BitvenusAP5 = BitvinusOBRes['asks'][4][0]
                BitvenusAP1V = (BitvinusOBRes['asks'][0][1])
                BitvenusAP2V = BitvinusOBRes['asks'][1][1]
                BitvenusAP3V = BitvinusOBRes['asks'][2][1]
                BitvenusAP4V = BitvinusOBRes['asks'][3][1]
                BitvenusAP5V = BitvinusOBRes['asks'][4][1]

                BitvenusLTP = float(BitvenusLTPURL_Res[0]['price'])
                BitvenusLTPV = float(BitvenusLTPURL_Res[0]['qty'])
                BitvenusLTPTM = int(BitvenusLTPURL_Res[0]['time'])
                BitvenusLTPT = BitvenusLTPTM
        except Exception as e:

            Bitvenus_Status = 400

        try:

            if BiconomyOBRes:
                BiconomyAP1 = float(BiconomyOBRes['asks'][0][0])
                BiconomyAP2 = BiconomyOBRes['asks'][1][0]
                BiconomyAP3 = BiconomyOBRes['asks'][2][0]
                BiconomyAP4 = BiconomyOBRes['asks'][3][0]
                BiconomyAP5 = BiconomyOBRes['asks'][4][0]
                BiconomyAP1V = (BiconomyOBRes['asks'][0][1])
                BiconomyAP2V = BiconomyOBRes['asks'][1][1]
                BiconomyAP3V = BiconomyOBRes['asks'][2][1]
                BiconomyAP4V = BiconomyOBRes['asks'][3][1]
                BiconomyAP5V = BiconomyOBRes['asks'][4][1]
                BiconomyBP1 = float(BiconomyOBRes['bids'][0][0])
                BiconomyBP2 = BiconomyOBRes['bids'][1][0]
                BiconomyBP3 = BiconomyOBRes['bids'][2][0]
                BiconomyBP4 = BiconomyOBRes['bids'][3][0]
                BiconomyBP5 = BiconomyOBRes['bids'][4][0]
                BiconomyBP1V = (BiconomyOBRes['bids'][0][1])
                BiconomyBP2V = BiconomyOBRes['bids'][1][1]
                BiconomyBP3V = BiconomyOBRes['bids'][2][1]
                BiconomyBP4V = BiconomyOBRes['bids'][3][1]
                BiconomyBP5V = BiconomyOBRes['bids'][4][1]

                BiconomyLTPV = BICONOMYLTPURL_Res[0]['amount']
                BiconomyLTP = float(BICONOMYLTPURL_Res[0]['price'])
                BiconomyLTPTM = int(BICONOMYLTPURL_Res[0]['timestamp'])
                BiconomyLTPT = BiconomyLTPTM
        except Exception as e:

            Biconomy_Status = 400
        try:

            if XTOBRes:
                XTOBTM = int(XTOBRes['result']['timestamp'])
                XTOBT = (XTOBTM)
                XTBP1 = float(XTOBRes['result']['bids'][0][0])
                XTBP2 = XTOBRes['result']['bids'][1][0]
                XTBP3 = XTOBRes['result']['bids'][2][0]
                XTBP4 = XTOBRes['result']['bids'][3][0]
                XTBP5 = XTOBRes['result']['bids'][4][0]
                XTBP1V = (XTOBRes['result']['bids'][0][1])
                XTBP2V = XTOBRes['result']['bids'][1][1]
                XTBP3V = XTOBRes['result']['bids'][2][1]
                XTBP4V = XTOBRes['result']['bids'][3][1]
                XTBP5V = XTOBRes['result']['bids'][4][1]
                XTAP1 = float(XTOBRes['result']['asks'][0][0])
                XTAP2 = XTOBRes['result']['asks'][1][0]
                XTAP3 = XTOBRes['result']['asks'][2][0]
                XTAP4 = XTOBRes['result']['asks'][3][0]
                XTAP5 = XTOBRes['result']['asks'][4][0]
                XTAP1V = (XTOBRes['result']['asks'][0][1])
                XTAP2V = XTOBRes['result']['asks'][1][1]
                XTAP3V = XTOBRes['result']['asks'][2][1]
                XTAP4V = XTOBRes['result']['asks'][3][1]
                XTAP5V = XTOBRes['result']['asks'][4][1]

                XTLTPTM = int(XTLTPURL_Res['result'][0]['t'])
                XTLTPT = (XTLTPTM)
                XTLTP = XTLTPURL_Res['result'][0]['c']

        except Exception as e:

            XT_Status = 400

        try:

            if BitflyerOBURLRes:
                BitflyerBP1 = float(BitflyerOBURLRes['bids'][0]['price'])
                BitflyerBP2 = float(BitflyerOBURLRes['bids'][1]['price'])
                BitflyerBP3 = float(BitflyerOBURLRes['bids'][2]['price'])
                BitflyerBP4 = float(BitflyerOBURLRes['bids'][3]['price'])
                BitflyerBP5 = float(BitflyerOBURLRes['bids'][4]['price'])
                BitflyerBP1V = (float(BitflyerOBURLRes['bids'][0]['size']))
                BitflyerBP2V = float(BitflyerOBURLRes['bids'][1]['size'])
                BitflyerBP3V = float(BitflyerOBURLRes['bids'][2]['size'])
                BitflyerBP4V = float(BitflyerOBURLRes['bids'][3]['size'])
                BitflyerBP5V = float(BitflyerOBURLRes['bids'][4]['size'])
                BitflyerAP1 = float(BitflyerOBURLRes['asks'][0]['price'])
                BitflyerAP2 = float(BitflyerOBURLRes['asks'][1]['price'])
                BitflyerAP3 = float(BitflyerOBURLRes['asks'][2]['price'])
                BitflyerAP4 = float(BitflyerOBURLRes['asks'][3]['price'])
                BitflyerAP5 = float(BitflyerOBURLRes['asks'][4]['price'])
                BitflyerAP1V = (float(BitflyerOBURLRes['asks'][0]['size']))
                BitflyerAP2V = float(BitflyerOBURLRes['asks'][1]['size'])
                BitflyerAP3V = float(BitflyerOBURLRes['asks'][2]['size'])
                BitflyerAP4V = float(BitflyerOBURLRes['asks'][3]['size'])
                BitflyerAP5V = float(BitflyerOBURLRes['asks'][4]['size'])

                BitflyerLTP = float(BitflyerLTPURLRes['ltp'])
                BitflyerLTPV = BitflyerLTPURLRes['volume']
                BitflyerLTPT = BitflyerLTPURLRes['timestamp']
        except Exception as e:

            Bitflyer_Status = 400
        try:

            if CoinWOBRes:
                CoinWAP1 = float(CoinWOBRes['data']['asks'][0][0])
                CoinWAP2 = CoinWOBRes['data']['asks'][1][0]
                CoinWAP3 = CoinWOBRes['data']['asks'][2][0]
                CoinWAP4 = CoinWOBRes['data']['asks'][3][0]
                CoinWAP5 = CoinWOBRes['data']['asks'][4][0]
                CoinWBP1 = float(CoinWOBRes['data']['bids'][0][0])
                CoinWBP2 = CoinWOBRes['data']['bids'][1][0]
                CoinWBP3 = CoinWOBRes['data']['bids'][2][0]
                CoinWBP4 = CoinWOBRes['data']['bids'][3][0]
                CoinWBP5 = CoinWOBRes['data']['bids'][4][0]
                CoinWAP1V = (CoinWOBRes['data']['asks'][0][1])
                CoinWAP2V = CoinWOBRes['data']['asks'][1][1]
                CoinWAP3V = CoinWOBRes['data']['asks'][2][1]
                CoinWAP4V = CoinWOBRes['data']['asks'][3][1]
                CoinWAP5V = CoinWOBRes['data']['asks'][4][1]
                CoinWBP1V = (CoinWOBRes['data']['bids'][0][1])
                CoinWBP2V = CoinWOBRes['data']['bids'][1][1]
                CoinWBP3V = CoinWOBRes['data']['bids'][2][1]
                CoinWBP4V = CoinWOBRes['data']['bids'][3][1]
                CoinWBP5V = CoinWOBRes['data']['bids'][4][1]

                CoinWLTP = CoinWLTPURL_Res['data']['last']
        except Exception as e:

            CoinW_Status = 400
        try:

            if ToobitOBRes:
                ToobitOBTM = ToobitOBRes['t']
                ToobitBP1 = float(ToobitOBRes['b'][0][0])
                ToobitBP2 = ToobitOBRes['b'][1][0]
                ToobitBP3 = ToobitOBRes['b'][2][0]
                ToobitBP4 = ToobitOBRes['b'][3][0]
                ToobitBP5 = ToobitOBRes['b'][4][0]
                ToobitAP1 = float(ToobitOBRes['a'][0][0])
                ToobitAP2 = ToobitOBRes['a'][1][0]
                ToobitAP3 = ToobitOBRes['a'][2][0]
                ToobitAP4 = ToobitOBRes['a'][3][0]
                ToobitAP5 = ToobitOBRes['a'][4][0]
                ToobitBP1V = (ToobitOBRes['b'][0][1])
                ToobitBP2V = ToobitOBRes['b'][1][1]
                ToobitBP3V = ToobitOBRes['b'][2][1]
                ToobitBP4V = ToobitOBRes['b'][3][1]
                ToobitBP5V = ToobitOBRes['b'][4][1]
                ToobitAP1V = (ToobitOBRes['a'][0][1])
                ToobitAP2V = ToobitOBRes['a'][1][1]
                ToobitAP3V = ToobitOBRes['a'][2][1]
                ToobitAP4V = ToobitOBRes['a'][3][1]
                ToobitAP5V = ToobitOBRes['a'][4][1]

                ToobitLTP = ToobitLTPURL_Res[0]['p']
                ToobitLTPV = ToobitLTPURL_Res[0]['q']
                ToobitLTPTm = ToobitLTPURL_Res[0]['t']
        except Exception as e:

            Toobit_Status = 400

        try:

            if TapbitOBRes:
                TapbitAP1 = float(TapbitOBRes['data']['asks'][0][0])
                TapbitAP2 = TapbitOBRes['data']['asks'][1][0]
                TapbitAP3 = TapbitOBRes['data']['asks'][2][0]
                TapbitAP4 = TapbitOBRes['data']['asks'][3][0]
                TapbitAP5 = TapbitOBRes['data']['asks'][4][0]
                TapbitBP1 = float(TapbitOBRes['data']['bids'][0][0])
                TapbitBP2 = TapbitOBRes['data']['bids'][1][0]
                TapbitBP3 = TapbitOBRes['data']['bids'][2][0]
                TapbitBP4 = TapbitOBRes['data']['bids'][3][0]
                TapbitBP5 = TapbitOBRes['data']['bids'][4][0]
                TapbitAP1V = (TapbitOBRes['data']['asks'][0][1])
                TapbitAP2V = TapbitOBRes['data']['asks'][1][1]
                TapbitAP3V = TapbitOBRes['data']['asks'][2][1]
                TapbitAP4V = TapbitOBRes['data']['asks'][3][1]
                TapbitAP5V = TapbitOBRes['data']['asks'][4][1]
                TapbitBP1V = (TapbitOBRes['data']['bids'][0][1])
                TapbitBP2V = TapbitOBRes['data']['bids'][1][1]
                TapbitBP3V = TapbitOBRes['data']['bids'][2][1]
                TapbitBP4V = TapbitOBRes['data']['bids'][3][1]
                TapbitBP5V = TapbitOBRes['data']['bids'][4][1]
                TapbitOBTM = TapbitOBRes['data']['timestamp']

                TapbitLTP = TapbitLTPURL_Res['data']['last_price']

        except Exception as e:

            TapBit_Status = 400








    return {


        "BinanceBP1": BinanceBP1,
        "BinanceBP1V": BinanceBP1V,
        "BinanceAP1": BinanceAP1,
        "BinanceAP1V": BinanceAP1V,
        "BinanceOBT": BybitOBT,
        "BinanceLTP": BinanceLTP,
        "BybitBP1": BybitBP1,
        "BybitBP1V": BybitBP1V,
        "BybitAP1": BybitAP1,
        "BybitAP1V": BybitAP1V,
        "BybitOBT": BybitOBT,
        "BybitLTP": BybitLTP,
        "OKXBP1": OKXBP1,
        "OKXBP1V": OKXBP1V,
        "OKXAP1": OKXAP1,
        "OKXAP1V": OKXAP1V,
        "OKXOBT": OKXOBT,
        "OKXLTP": OKXLTP,
        "UpbitBP1": UpbitBP1,
        "UpbitBP1V": UpbitBP1V,
        "UpbitAP1": UpbitAP1,
        "UpbitAP1V": UpbitAP1V,
        "UpbitOBT": UpbitOBT,
        "UpbitLTP": UpbitLTP,
        "KucoinBP1": KucoinBP1,
        "KucoinBP1V": KucoinBP1V,
        "KucoinAP1": KucoinAP1,
        "KucoinAP1V": KucoinAP1V,
        "KucoinOBT": KucoinOBT,
        "KucoinLTP": KucoinLTP,
        "BitgetBP1": BitgetBP1,
        "BitgetBP1V": BitgetBP1V,
        "BitgetAP1": BitgetAP1,
        "BitgetAP1V": BitgetAP1V,
        "BitgetOBT": BitgetOBT,
        "BitgetLTP": BitgetLTP,
        "BitstampBP1": BitstampBP1,
        "BitstampBP1V": BitstampBP1V,
        "BitstampAP1": BitstampAP1,
        "BitstampAP1V": BitstampAP1V,
        "BitstampOBT": BitstampOBT,
        "BitstampLTP": BitstampLTP,
        "GeminiBP1": GeminiBP1,
        "GeminiBP1V": GeminiBP1V,
        "GeminiAP1": GeminiAP1,
        "GeminiAP1V": GeminiAP1V,
        "GeminiOBT": GeminiOBT,
        "GeminiLTP": GeminiLTP,
        "KrakenBP1": KrakenBP1,
        "KrakenBP1V": KrakenBPV1,
        "KrakenAP1": KrakenAP1,
        "KrakenAP1V": KrakenAPV1,
        "KrakenOBT": KrakenOBT,
        "KrakenLTP": KrakenLTP,
        "GateioBP1": GateioBP1,
        "GateioBP1V": GateioBPV1,
        "GateioAP1": GateioAP1,
        "GateioAP1V": GateioAPV1,
        "GateioOBT": BybitOBT,
        "GateioLTP": GateioLTP,
        "HTXBP1": HTXBP1,
        "HTXBP1V": HTXBP1V,
        "HTXAP1": HTXAP1,
        "HTXAP1V": HTXAP1V,
        "HTXOBT": HTXOBT,
        "HTXLTP": HTXLTP,
        "MEXCBP1": MEXCBP1,
        "MEXCBP1V": MEXCBP1V,
        "MEXCAP1": MEXCAP1,
        "MEXCAP1V": MEXCAP1V,
        "MEXCOBT": MEXCOBT,
        "MEXCLTP": MEXCLTP,
        "LbankBP1": LbankBP1,
        "LbankBP1V": LbankBP1V,
        "LbankAP1": LbankAP1,
        "LbankAP1V": LbankAP1V,
        "LbankOBT": LbankOBT,
        "LbankLTP": LbankLTP,
        "BitmartBP1": BitmartBP1,
        "BitmartBP1V": BitmartBP1V,
        "BitmartAP1": BitmartAP1,
        "BitmartAP1V": BitmartAP1V,
        "BitmartOBT": BitmartOBT,
        "BitmartLTP": BitmartLTP,
        "DeepcoinBP1": DeepcoinBP1,
        "DeepcoinBP1V": DeepcoinBP1V,
        "DeepcoinAP1": DeepcoinAP1,
        "DeepcoinAP1V": DeepcoinAP1V,
        "DeepcoinOBT": BybitOBT,
        "DeepcoinLTP": DeepcoinLTP,
        "BitfinexBP1": BitfinexBP1,
        "BitfinexBP1V": BitfinexBP1V,
        "BitfinexAP1": BitfinexAP1,
        "BitfinexAP1V": BitfinexAP1V,
        "BitfinexOBT": BybitOBT,
        "BitfinexLTP": BitfinexLTP,
        "BingXBP1": BingXBP1,
        "BingXBP1V": BingXBP1V,
        "BingXAP1": BingXAP1,
        "BingXAP1V": BingXAP1V,
        "BingXOBT": BybitOBT,
        "BingXLTP": BingXLTP,
        "OrangeXBP1": OrangeXBP1,
        "OrangeXBP1V": OrangeXBP1V,
        "OrangeXAP1": OrangeXAP1,
        "OrangeXAP1V": OrangeXAP1V,
        "OrangeXOBT": OrangeXOBT,
        "OrangeXLTP": OrangeXLTP,
        "BitvenusBP1": BitvenusBP1,
        "BitvenusBP1V": BitvenusBP1V,
        "BitvenusAP1": BitvenusAP1,
        "BitvenusAP1V": BitvenusAP1V,
        "BitvenusOBT": BitvenusOBT,
        "BitvenusLTP": BitvenusLTP,
        "BiconomyBP1": BiconomyBP1,
        "BiconomyBP1V": BiconomyBP1V,
        "BiconomyAP1": BiconomyAP1,
        "BiconomyAP1V": BiconomyAP1V,
        "BiconomyOBT": BybitOBT,
        "BiconomyLTP": BiconomyLTP,
        "XTBP1": XTBP1,
        "XTBP1V": XTBP1V,
        "XTAP1": XTAP1,
        "XTAP1V": XTAP1V,
        "XTOBT": XTOBT,
        "XTLTP": XTLTP,
        "BitflyerBP1": BitflyerBP1,
        "BitflyerBP1V": BitflyerBP1V,
        "BitflyerAP1": BitflyerAP1,
        "BitflyerAP1V": BitflyerAP1V,
        "BitflyerOBT": BybitOBT,
        "BitflyerLTP": BitflyerLTP,
        "CoinWBP1": CoinWBP1,
        "CoinWBP1V": CoinWBP1V,
        "CoinWAP1": CoinWAP1,
        "CoinWAP1V": CoinWAP1V,
        "CoinWOBT": BybitOBT,
        "CoinWLTP": CoinWLTP,
        "ToobitBP1": ToobitBP1,
        "ToobitBP1V": ToobitBP1V,
        "ToobitAP1": ToobitAP1,
        "ToobitAP1V": ToobitAP1V,
        "ToobitOBT": BybitOBT,
        "ToobitLTP": ToobitLTP,
        "TapBitBP1": TapbitBP1,
        "TapBitBP1V": TapbitBP1V,
        "TapBitAP1": TapbitAP1,
        "TapBitAP1V": TapbitAP1V,
        "TapBitOBT": BybitOBT,
        "TapBitLTP": TapbitLTP,

        "BinanceBP2": float(BinanceBP2),
        "BinanceBP2V": float(BinanceBP2V),
        "BinanceAP2": float(BinanceAP2),
        "BinanceAP2V": float(BinanceAP2V),
        "BybitBP2": float(BybitBP2),
        "BybitBP2V": float(BybitBP2V),
        "BybitAP2": float(BybitAP2),
        "BybitAP2V": float(BybitAP2V),
        "OKXBP2": float(OKXBP2),
        "OKXBP2V": float(OKXBP2V),
        "OKXAP2": float(OKXAP2),
        "OKXAP2V": float(OKXAP2V),
        "UpbitBP2": float(UpbitBP2),
        "UpbitBP2V": float(UpbitBP2V),
        "UpbitAP2": float(UpbitAP2),
        "UpbitAP2V": float(UpbitAP2V),
        "KucoinBP2": float(KucoinBP2),
        "KucoinBP2V": float(KucoinBP2V),
        "KucoinAP2": float(KucoinAP2),
        "KucoinAP2V": float(KucoinAP2V),
        "BitgetBP2": float(BitgetBP2),
        "BitgetBP2V": float(BitgetBP2V),
        "BitgetAP2": float(BitgetAP2),
        "BitgetAP2V": float(BitgetAP2V),
        "BitstampBP2": float(BitstampBP2),
        "BitstampBP2V": float(BitstampBP2V),
        "BitstampAP2": float(BitstampAP2),
        "BitstampAP2V": float(BitstampAP2V),
        "GeminiBP2": float(GeminiBP2),
        "GeminiBP2V": float(GeminiBP2V),
        "GeminiAP2": float(GeminiAP2),
        "GeminiAP2V": float(GeminiAP2V),
        "KrakenBP2": float(KrakenBP2),
        "KrakenBP2V": float(KrakenBPV2),
        "KrakenAP2": float(KrakenAP2),
        "KrakenAP2V": float(KrakenAPV2),
        "GateioBP2": float(GateioBP2),
        "GateioBP2V": float(GateioBPV2),
        "GateioAP2": float(GateioAP2),
        "GateioAP2V": float(GateioAPV2),
        "HTXBP2": float(HTXBP2),
        "HTXBP2V": float(HTXBP2V),
        "HTXAP2": float(HTXAP2),
        "HTXAP2V": float(HTXAP2V),
        "MEXCBP2": float(MEXCBP2),
        "MEXCBP2V": float(MEXCBP2V),
        "MEXCAP2": float(MEXCAP2),
        "MEXCAP2V": float(MEXCAP2V),
        "LbankBP2": float(LbankBP2),
        "LbankBP2V": float(LbankBP2V),
        "LbankAP2": float(LbankAP2),
        "LbankAP2V": float(LbankAP2V),
        "BitmartBP2": float(BitmartBP2),
        "BitmartBP2V": float(BitmartBP2V),
        "BitmartAP2": float(BitmartAP2),
        "BitmartAP2V": float(BitmartAP2V),
        "DeepcoinBP2": float(DeepcoinBP2),
        "DeepcoinBP2V": float(DeepcoinBP2V),
        "DeepcoinAP2": float(DeepcoinAP2),
        "DeepcoinAP2V": float(DeepcoinAP2V),
        "BitfinexBP2": float(BitfinexBP2),
        "BitfinexBP2V": float(BitfinexBP2V),
        "BitfinexAP2": float(BitfinexAP2),
        "BitfinexAP2V": float(BitfinexAP2V),
        "BingXBP2": float(BingXBP2),
        "BingXBP2V": float(BingXBP2V),
        "BingXAP2": float(BingXAP2),
        "BingXAP2V": float(BingXAP2V),
        "OrangeXBP2": float(OrangeXBP2),
        "OrangeXBP2V": float(OrangeXBP2V),
        "OrangeXAP2": float(OrangeXAP2),
        "OrangeXAP2V": float(OrangeXAP2V),
        "BitvenusBP2": float(BitvenusBP2),
        "BitvenusBP2V": float(BitvenusBP2V),
        "BitvenusAP2": float(BitvenusAP2),
        "BitvenusAP2V": float(BitvenusAP2V),
        "BiconomyBP2": float(BiconomyBP2),
        "BiconomyBP2V": float(BiconomyBP2V),
        "BiconomyAP2": float(BiconomyAP2),
        "BiconomyAP2V": float(BiconomyAP2V),
        "XTBP2": float(XTBP2),
        "XTBP2V": float(XTBP2V),
        "XTAP2": float(XTAP2),
        "XTAP2V": float(XTAP2V),
        "BitflyerBP2": float(BitflyerBP2),
        "BitflyerBP2V": float(BitflyerBP2V),
        "BitflyerAP2": float(BitflyerAP2),
        "BitflyerAP2V": float(BitflyerAP2V),
        "CoinWBP2": float(CoinWBP2),
        "CoinWBP2V": float(CoinWBP2V),
        "CoinWAP2": float(CoinWAP2),
        "CoinWAP2V": float(CoinWAP2V),
        "ToobitBP2": float(ToobitBP2),
        "ToobitBP2V": float(ToobitBP2V),
        "ToobitAP2": float(ToobitAP2),
        "ToobitAP2V": float(ToobitAP2V),
        "TapBitBP2": float(TapbitBP2),
        "TapBitBP2V": float(TapbitBP2V),
        "TapBitAP2": float(TapbitAP2),
        "TapBitAP2V": float(TapbitAP2V),

        "BinanceBP3": float(BinanceBP3),
        "BinanceBP3V": float(BinanceBP3V),
        "BinanceAP3": float(BinanceAP3),
        "BinanceAP3V": float(BinanceAP3V),
        "BybitBP3": float(BybitBP3),
        "BybitBP3V": float(BybitBP3V),
        "BybitAP3": float(BybitAP3),
        "BybitAP3V": float(BybitAP3V),
        "OKXBP3": float(OKXBP3),
        "OKXBP3V": float(OKXBP3V),
        "OKXAP3": float(OKXAP3),
        "OKXAP3V": float(OKXAP3V),
        "UpbitBP3": float(UpbitBP3),
        "UpbitBP3V": float(UpbitBP3V),
        "UpbitAP3": float(UpbitAP3),
        "UpbitAP3V": float(UpbitAP3V),
        "KucoinBP3": float(KucoinBP3),
        "KucoinBP3V": float(KucoinBP3V),
        "KucoinAP3": float(KucoinAP3),
        "KucoinAP3V": float(KucoinAP3V),
        "BitgetBP3": float(BitgetBP3),
        "BitgetBP3V": float(BitgetBP3V),
        "BitgetAP3": float(BitgetAP3),
        "BitgetAP3V": float(BitgetAP3V),
        "BitstampBP3": float(BitstampBP3),
        "BitstampBP3V": float(BitstampBP3V),
        "BitstampAP3": float(BitstampAP3),
        "BitstampAP3V": float(BitstampAP3V),
        "GeminiBP3": float(GeminiBP3),
        "GeminiBP3V": float(GeminiBP3V),
        "GeminiAP3": float(GeminiAP3),
        "GeminiAP3V": float(GeminiAP3V),
        "KrakenBP3": float(KrakenBP3),
        "KrakenBP3V": float(KrakenBPV3),
        "KrakenAP3": float(KrakenAP3),
        "KrakenAP3V": float(KrakenAPV3),
        "GateioBP3": float(GateioBP3),
        "GateioBP3V": float(GateioBPV3),
        "GateioAP3": float(GateioAP3),
        "GateioAP3V": float(GateioAPV3),
        "HTXBP3": float(HTXBP3),
        "HTXBP3V": float(HTXBP3V),
        "HTXAP3": float(HTXAP3),
        "HTXAP3V": float(HTXAP3V),
        "MEXCBP3": float(MEXCBP3),
        "MEXCBP3V": float(MEXCBP3V),
        "MEXCAP3": float(MEXCAP3),
        "MEXCAP3V": float(MEXCAP3V),
        "LbankBP3": float(LbankBP3),
        "LbankBP3V": float(LbankBP3V),
        "LbankAP3": float(LbankAP3),
        "LbankAP3V": float(LbankAP3V),
        "BitmartBP3": float(BitmartBP3),
        "BitmartBP3V": float(BitmartBP3V),
        "BitmartAP3": float(BitmartAP3),
        "BitmartAP3V": float(BitmartAP1V),
        "DeepcoinBP3": float(DeepcoinBP3),
        "DeepcoinBP3V": float(DeepcoinBP3V),
        "DeepcoinAP3": float(DeepcoinAP3),
        "DeepcoinAP3V": float(DeepcoinAP3V),
        "BitfinexBP3": float(BitfinexBP3),
        "BitfinexBP3V": float(BitfinexBP3V),
        "BitfinexAP3": float(BitfinexAP3),
        "BitfinexAP3V": float(BitfinexAP3V),
        "BingXBP3": float(BingXBP3),
        "BingXBP3V": float(BingXBP3V),
        "BingXAP3": float(BingXAP3),
        "BingXAP3V": float(BingXAP3V),
        "OrangeXBP3": float(OrangeXBP3),
        "OrangeXBP3V": float(OrangeXBP3V),
        "OrangeXAP3": float(OrangeXAP3),
        "OrangeXAP3V": float(OrangeXAP3V),
        "BitvenusBP3": float(BitvenusBP3),
        "BitvenusBP3V": float(BitvenusBP3V),
        "BitvenusAP3": float(BitvenusAP3),
        "BitvenusAP3V": float(BitvenusAP3V),
        "BiconomyBP3": float(BiconomyBP3),
        "BiconomyBP3V": float(BiconomyBP3V),
        "BiconomyAP3": float(BiconomyAP3),
        "BiconomyAP3V": float(BiconomyAP3V),
        "XTBP3": float(XTBP3),
        "XTBP3V": float(XTBP3V),
        "XTAP3": float(XTAP3),
        "XTAP3V": float(XTAP3V),
        "BitflyerBP3": float(BitflyerBP3),
        "BitflyerBP3V": float(BitflyerBP3V),
        "BitflyerAP3": float(BitflyerAP3),
        "BitflyerAP3V": float(BitflyerAP3V),
        "CoinWBP3": float(CoinWBP3),
        "CoinWBP3V": float(CoinWBP3V),
        "CoinWAP3": float(CoinWAP3),
        "CoinWAP3V": float(CoinWAP3V),
        "ToobitBP3": float(ToobitBP3),
        "ToobitBP3V": float(ToobitBP3V),
        "ToobitAP3": float(ToobitAP3),
        "ToobitAP3V": float(ToobitAP3V),
        "TapBitBP3": float(TapbitBP3),
        "TapBitBP3V": float(TapbitBP3V),
        "TapBitAP3": float(TapbitAP3),
        "TapBitAP3V": float(TapbitAP3V),

        "BinanceBP4": float(BinanceBP4),
        "BinanceBP4V": float(BinanceBP4V),
        "BinanceAP4": float(BinanceAP4),
        "BinanceAP4V": float(BinanceAP4V),
        "BybitBP4": float(BybitBP4),
        "BybitBP4V": float(BybitBP4V),
        "BybitAP4": float(BybitAP4),
        "BybitAP4V": float(BybitAP4V),
        "OKXBP4": float(OKXBP4),
        "OKXBP4V": float(OKXBP4V),
        "OKXAP4": float(OKXAP4),
        "OKXAP4V": float(OKXAP4V),
        "UpbitBP4": float(UpbitBP4),
        "UpbitBP4V": float(UpbitBP4V),
        "UpbitAP4": float(UpbitAP4),
        "UpbitAP4V": float(UpbitAP4V),
        "KucoinBP4": float(KucoinBP4),
        "KucoinBP4V": float(KucoinBP4V),
        "KucoinAP4": float(KucoinAP4),
        "KucoinAP4V": float(KucoinAP4V),
        "BitgetBP4": float(BitgetBP4),
        "BitgetBP4V": float(BitgetBP4V),
        "BitgetAP4": float(BitgetAP4),
        "BitgetAP4V": float(BitgetAP4V),
        "BitstampBP4": float(BitstampBP4),
        "BitstampBP4V": float(BitstampBP4V),
        "BitstampAP4": float(BitstampAP4),
        "BitstampAP4V": float(BitstampAP4V),
        "GeminiBP4": float(GeminiBP4),
        "GeminiBP4V": float(GeminiBP4V),
        "GeminiAP4": float(GeminiAP4),
        "GeminiAP4V": float(GeminiAP4V),
        "KrakenBP4": float(KrakenBP4),
        "KrakenBP4V": float(KrakenBPV4),
        "KrakenAP4": float(KrakenAP4),
        "KrakenAP4V": float(KrakenAPV4),
        "GateioBP4": float(GateioBP4),
        "GateioBP4V": float(GateioBPV4),
        "GateioAP4": float(GateioAP4),
        "GateioAP4V": float(GateioAPV4),
        "HTXBP4": float(HTXBP4),
        "HTXBP4V": float(HTXBP4V),
        "HTXAP4": float(HTXAP4),
        "HTXAP4V": float(HTXAP4V),
        "MEXCBP4": float(MEXCBP4),
        "MEXCBP4V": float(MEXCBP4V),
        "MEXCAP4": float(MEXCAP4),
        "MEXCAP4V": float(MEXCAP4V),
        "LbankBP4": float(LbankBP4),
        "LbankBP4V": float(LbankBP4V),
        "LbankAP4": float(LbankAP4),
        "LbankAP4V": float(LbankAP4V),
        "BitmartBP4": float(BitmartBP4),
        "BitmartBP4V": float(BitmartBP4V),
        "BitmartAP4": float(BitmartAP4),
        "BitmartAP4V": float(BitmartAP4V),
        "DeepcoinBP4": float(DeepcoinBP4),
        "DeepcoinBP4V": float(DeepcoinBP4V),
        "DeepcoinAP4": float(DeepcoinAP4),
        "DeepcoinAP4V": float(DeepcoinAP4V),
        "BitfinexBP4": float(BitfinexBP4),
        "BitfinexBP4V": float(BitfinexBP4V),
        "BitfinexAP4": float(BitfinexAP4),
        "BitfinexAP4V": float(BitfinexAP4V),
        "BingXBP4": float(BingXBP4),
        "BingXBP4V": float(BingXBP4V),
        "BingXAP4": float(BingXAP4),
        "BingXAP4V": float(BingXAP4V),
        "OrangeXBP4": float(OrangeXBP4),
        "OrangeXBP4V": float(OrangeXBP4V),
        "OrangeXAP4": float(OrangeXAP4),
        "OrangeXAP4V": float(OrangeXAP4V),
        "BitvenusBP4": float(BitvenusBP4),
        "BitvenusBP4V": float(BitvenusBP4V),
        "BitvenusAP4": float(BitvenusAP4),
        "BitvenusAP4V": float(BitvenusAP4V),
        "BiconomyBP4": float(BiconomyBP4),
        "BiconomyBP4V": float(BiconomyBP4V),
        "BiconomyAP4": float(BiconomyAP4),
        "BiconomyAP4V": float(BiconomyAP4V),
        "XTBP4": float(XTBP4),
        "XTBP4V": float(XTBP4V),
        "XTAP4": float(XTAP4),
        "XTAP4V": float(XTAP4V),
        "BitflyerBP4": float(BitflyerBP4),
        "BitflyerBP4V": float(BitflyerBP4V),
        "BitflyerAP4": float(BitflyerAP4),
        "BitflyerAP4V": float(BitflyerAP4V),
        "CoinWBP4": float(CoinWBP4),
        "CoinWBP4V": float(CoinWBP4V),
        "CoinWAP4": float(CoinWAP4),
        "CoinWAP4V": float(CoinWAP4V),
        "ToobitBP4": float(ToobitBP4),
        "ToobitBP4V": float(ToobitBP4V),
        "ToobitAP4": float(ToobitAP4),
        "ToobitAP4V": float(ToobitAP4V),
        "TapBitBP4": float(TapbitBP4),
        "TapBitBP4V": float(TapbitBP4V),
        "TapBitAP4": float(TapbitAP4),
        "TapBitAP4V": float(TapbitAP4V),

        "BinanceBP5": float(BinanceBP5),
        "BinanceBP5V": float(BinanceBP5V),
        "BinanceAP5": float(BinanceAP5),
        "BinanceAP5V": float(BinanceAP5V),
        "BybitBP5": float(BybitBP5),
        "BybitBP5V": float(BybitBP5V),
        "BybitAP5": float(BybitAP5),
        "BybitAP5V": float(BybitAP5V),
        "OKXBP5": float(OKXBP5),
        "OKXBP5V": float(OKXBP5V),
        "OKXAP5": float(OKXAP5),
        "OKXAP5V": float(OKXAP5V),
        "UpbitBP5": float(UpbitBP5),
        "UpbitBP5V": float(UpbitBP5V),
        "UpbitAP5": float(UpbitAP5),
        "UpbitAP5V": float(UpbitAP5V),
        "KucoinBP5": float(KucoinBP5),
        "KucoinBP5V": float(KucoinBP5V),
        "KucoinAP5": float(KucoinAP5),
        "KucoinAP5V": float(KucoinAP5V),
        "BitgetBP5": float(BitgetBP5),
        "BitgetBP5V": float(BitgetBP5V),
        "BitgetAP5": float(BitgetAP5),
        "BitgetAP5V": float(BitgetAP5V),
        "BitstampBP5": float(BitstampBP5),
        "BitstampBP5V": float(BitstampBP5V),
        "BitstampAP5": float(BitstampAP5),
        "BitstampAP5V": float(BitstampAP5V),
        "GeminiBP5": float(GeminiBP5),
        "GeminiBP5V": float(GeminiBP5V),
        "GeminiAP5": float(GeminiAP5),
        "GeminiAP5V": float(GeminiAP5V),
        "KrakenBP5": float(KrakenBP5),
        "KrakenBP5V": float(KrakenBPV5),
        "KrakenAP5": float(KrakenAP5),
        "KrakenAP5V": float(KrakenAPV5),
        "GateioBP5": float(GateioBP5),
        "GateioBP5V": float(GateioBPV5),
        "GateioAP5": float(GateioAP5),
        "GateioAP5V": float(GateioAPV5),
        "HTXBP5": float(HTXBP5),
        "HTXBP5V": float(HTXBP5V),
        "HTXAP5": float(HTXAP5),
        "HTXAP5V": float(HTXAP5V),
        "MEXCBP5": float(MEXCBP5),
        "MEXCBP5V": float(MEXCBP5V),
        "MEXCAP5": float(MEXCAP5),
        "MEXCAP5V": float(MEXCAP5V),
        "LbankBP5": float(LbankBP5),
        "LbankBP5V": float(LbankBP5V),
        "LbankAP5": float(LbankAP5),
        "LbankAP5V": float(LbankAP5V),
        "BitmartBP5": float(BitmartBP5),
        "BitmartBP5V": float(BitmartBP5V),
        "BitmartAP5": float(BitmartAP5),
        "BitmartAP5V": float(BitmartAP1V),
        "DeepcoinBP5": float(DeepcoinBP5),
        "DeepcoinBP5V": float(DeepcoinBP5V),
        "DeepcoinAP5": float(DeepcoinAP5),
        "DeepcoinAP5V": float(DeepcoinAP5V),
        "BitfinexBP5": float(BitfinexBP5),
        "BitfinexBP5V": float(BitfinexBP5V),
        "BitfinexAP5": float(BitfinexAP5),
        "BitfinexAP5V": float(BitfinexAP5V),
        "BingXBP5": float(BingXBP5),
        "BingXBP5V": float(BingXBP5V),
        "BingXAP5": float(BingXAP5),
        "BingXAP5V": float(BingXAP5V),
        "OrangeXBP5": float(OrangeXBP5),
        "OrangeXBP5V": float(OrangeXBP5V),
        "OrangeXAP5": float(OrangeXAP5),
        "OrangeXAP5V": float(OrangeXAP5V),
        "BitvenusBP5": float(BitvenusBP5),
        "BitvenusBP5V": float(BitvenusBP5V),
        "BitvenusAP5": float(BitvenusAP5),
        "BitvenusAP5V": float(BitvenusAP5V),
        "BiconomyBP5": float(BiconomyBP5),
        "BiconomyBP5V": float(BiconomyBP5V),
        "BiconomyAP5": float(BiconomyAP5),
        "BiconomyAP5V": float(BiconomyAP5V),
        "XTBP5": float(XTBP5),
        "XTBP5V": float(XTBP5V),
        "XTAP5": float(XTAP5),
        "XTAP5V": float(XTAP5V),
        "BitflyerBP5": float(BitflyerBP5),
        "BitflyerBP5V": float(BitflyerBP5V),
        "BitflyerAP5": float(BitflyerAP5),
        "BitflyerAP5V": float(BitflyerAP5V),
        "CoinWBP5": float(CoinWBP5),
        "CoinWBP5V": float(CoinWBP5V),
        "CoinWAP5": float(CoinWAP5),
        "CoinWAP5V": float(CoinWAP5V),
        "ToobitBP5": float(ToobitBP5),
        "ToobitBP5V": float(ToobitBP5V),
        "ToobitAP5": float(ToobitAP5),
        "ToobitAP5V": float(ToobitAP5V),
        "TapBitBP5": float(TapbitBP5),
        "TapBitBP5V": float(TapbitBP5V),
        "TapBitAP5": float(TapbitAP5),
        "TapBitAP5V": float(TapbitAP5V),

        "Binance_Status": Binance_Status,
        "Bybit_Status": BybitStatus,
        "OKX_Status": OKX_Status,
        "Upbit_Status": Upbit_Status,
        "Kucoin_Status": Kucoin_Status,
        "Bitget_Status": Bitget_Status,
        "Bitstamp_Status": Bitstamp_Status,
        "Gemini_Status": Gemini_Status,
        "Kraken_Status": Kraken_Status,
        "Gateio_Status": Gateio_Status,
        "HTX_Status": HTX_Status,
        "MEXC_Status": MEXC_Status,
        "Lbank_Status":Lbank_Status,
        "Bitmart_Status": Bitmart_Status,
        "Deepcoin_Status": Deepcoin_Status,
        "Bitfinex_Status": Bitfinex_Status,
        "BingX_Status": BingX_Status,
        "OrangeX_Status": OrangeX_Status,
        "Bitvenus_Status": Bitvenus_Status,
        "Biconomy_Status": Biconomy_Status,
        "XT_Status": XT_Status,
        "Bitflyer_Status": Bitflyer_Status,
        "CoinW_Status": CoinW_Status,
        "Toobit_Status": Toobit_Status,
        "TapBit_Status": TapBit_Status,}



    # end=time.time()
    # processingtime=end-start
    # print(processingtime)

