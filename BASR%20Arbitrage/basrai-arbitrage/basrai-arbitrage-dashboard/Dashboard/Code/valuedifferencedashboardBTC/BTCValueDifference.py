import time
import asyncio
import aiohttp
import asyncio
import ssl
import certifi
async def converting_decimalPoints(number):
    try:
        # Check if the value is a string and can be converted to float
        if isinstance(number, str):
            number = float(number)

        # Convert the float or string (now float) to an integer
        return int(number)

    except ValueError:
        # Handle the case where conversion is not possible
        print(f"Cannot convert '{number}' to an integer.")
        return None
async def convert_to_gmt5_async(x):
    return x



ssl_context = ssl.create_default_context(cafile=certifi.where())


class Exchange:
    def __init__(self, name, bid_price, ask_prices, bid_volume, ask_volumes):
        self.name = name
        self.bid_price = float(bid_price)
        self.ask_prices = {k: float(v) for k, v in ask_prices.items()}
        self.bid_volume = float(bid_volume)
        self.ask_volumes = {k: float(v) for k, v in ask_volumes.items()}
        self.volume_adjusted_differences = {}

    def calculate_differences(self):
        for exchange, ask_price in self.ask_prices.items():
            # Get the corresponding ask volume
            ask_volume = self.ask_volumes.get(exchange, 0)

            # Determine the smaller volume
            min_volume = min(self.bid_volume, ask_volume)

            # Multiply smaller volume with ask and bid prices and subtract them
            volume_price_difference = (self.bid_price * min_volume) - (ask_price * min_volume)

            # Store the volume-adjusted difference in results
            self.volume_adjusted_differences[f"{self.name}BP_{exchange}AP"] = volume_price_difference

    def get_volume_adjusted_differences(self):
        return self.volume_adjusted_differences

async def fetch_price(session, url):
    try:
        async with session.get(url) as response:
            return await response.json()
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None




async def mainvalue():
    start=time.time()
    BinanceOBURL = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=5'
    BinanceLTPURL = 'https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT'
    BybitOBURL = 'https://api.bybit.com/v2/public/orderBook/L2?symbol=BTCUSDT&depth=5'
    BybitLTPURL = 'https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT'
    OKXOBBURL = 'https://www.okx.com/api/v5/market/books?instId=BTC-USDT&sz=5'
    OKXLTPURL = 'https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT&sz=5'
    UpbitOBURL = 'https://api.upbit.com/v1/orderbook?markets=USDT-BTC'
    UpbitLTPURL = 'https://api.upbit.com/v1/ticker?markets=USDT-BTC'
    KucoinOBURL = 'https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT'
    KucoinLTPURL = 'https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT'
    BitgetOBURL = 'https://api.bitget.com/api/v2/spot/market/orderbook?symbol=BTCUSDT&type=step0&limit=5'
    BitgetLTPURL = 'https://api.bitget.com/api/v2/spot/market/tickers?symbol=BTCUSDT'
    BitstampOBURL = 'https://www.bitstamp.net/api/v2/order_book/btcusdt/'
    BitstampLTPURL = 'https://www.bitstamp.net/api/v2/ticker/btcusdt/'
    GeminiOBURL = 'https://api.gemini.com/v1/book/btcusdt'
    GeminiLTPURL = 'https://api.gemini.com/v1/pubticker/btcusdt'
    krakenOBURL = 'https://api.kraken.com/0/public/Depth?pair=BTCUSDT&count=5'
    krakenLTPURL = 'https://api.kraken.com/0/public/Trades?pair=BTCUSDt&count=1'
    Gateio_url_Orderbook = 'https://api.gate.io/api2/1/orderBook/BTC_USDT'
    Gateio_url_Last_trade = 'https://api.gate.io/api2/1/ticker/BTC_USDT'
    HTXOBURL = 'https://api-aws.huobi.pro/market/depth?symbol=btcusdt&type=step0'
    HTXLTPURL = 'https://api.huobi.pro/market/trade?symbol=btcusdt'
    MEXCOBURL = 'https://api.mexc.com/api/v3/depth?symbol=BTCUSDT&limit=5'
    MEXCLTPURL = 'https://api.mexc.com/api/v3/trades?symbol=BTCUSDT&limit=1'
    LbankOBURL = 'https://api.lbkex.com/v2/depth.do?symbol=btc_usdt&size=5'
    LbankLTPURL = 'https://api.lbkex.com/v2/ticker/24hr.do?symbol=btc_usdt'
    BitmartOBURL = 'https://api-cloud.bitmart.com/spot/quotation/v3/books?symbol=BTC_USDT&limit=5'
    BitmartLTPURL = 'https://api-cloud.bitmart.com/spot/quotation/v3/trades?symbol=BTC_USDT&limit=1'
    DeepcoinOBURL = 'https://api.deepcoin.com/deepcoin/market/books?instId=BTC-USDT&size=5'
    DeepcoinLTPURL = 'https://api.deepcoin.com/deepcoin/market/tickers?instType=SPOT&instId=BTCUSDT'
    BitfinexOBURL = 'https://api-pub.bitfinex.com/v2/book/tBTCUSD/P0?len=25'
    BitfinexLTPURL = 'https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD'
    BingxOBURL = 'https://open-api.bingx.com/openApi/swap/v2/quote/depth?symbol=BTC-USDT&limit=5'
    BingxLTPURL = 'https://open-api.bingx.com/openApi/swap/v2/quote/trades?symbol=BTC-USDT&limit=1'
    OrangeXOBURL = 'https://api.orangex.com/api/v1/public/get_order_book?instrument_name=BTC-USDT&depth=5'
    OrangeXLTPURL = 'https://api.orangex.com/api/v1/public/tickers?instrument_name=BTC-USDT'
    BitvenusOBURL = 'https://api.bitvenus.me/openapi/quote/v1/depth?symbol=BTCUSDT&limit=5'
    BitvenusLTPURL = 'https://api.bitvenus.me/openapi/quote/v1/trades?symbol=BTCUSDT&limit=1'
    BICONOMYOBURL = 'https://www.biconomy.com/api/v1/depth?symbol=BTC_USDT&size=5'
    BICONOMYLTPURL = 'https://www.biconomy.com/api/v1/trades?symbol=BTC_USDT&size=1'
    XTOBURL = 'https://sapi.xt.com/v4/public/depth?symbol=btc_usdt&limit=1'
    XTLTPURL = 'https://sapi.xt.com/v4/public/ticker?symbol=btc_usdt'
    BitflyerOBURL = 'https://api.bitflyer.com/v1/board?product_code=BTC_USD&count=5'
    BitflyerLTPURL = 'https://api.bitflyer.com/v1/getticker?product_code=BTC_USD'
    CoinWOBURL = 'https://api.coinw.com/api/v1/public?command=returnOrderBook&symbol=BTC_USDT&size=5'
    CoinWLTPURL = 'https://api.coinw.com/api/v1/public?command=returnTickerInfo&symbol=BTC_USDT'
    ToobitOBURL = 'https://api.toobit.com/quote/v1/depth?symbol=BTCUSDT&limit=5'
    ToobitLTPURL = 'https://api.toobit.com/quote/v1/trades?symbol=BTCUSDT&limit=1'
    TapbitOBURL = 'https://openapi.tapbit.com/spot/api/spot/instruments/depth?instrument_id=BTC/USDT&depth=5'
    TapbitLTPURL = 'https://openapi.tapbit.com/spot/api/spot/instruments/ticker_one?instrument_id=BTC/USDT'

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = [
            fetch_price(session, BinanceOBURL),  # 0
            fetch_price(session, BinanceLTPURL),  # 1
            fetch_price(session, BybitOBURL),  # 2
            fetch_price(session, BybitLTPURL),  # 3
            fetch_price(session, OKXOBBURL),  # 4
            fetch_price(session, OKXLTPURL),  # 5
            fetch_price(session, UpbitOBURL),  # 6
            fetch_price(session, UpbitLTPURL),  # 7
            fetch_price(session, KucoinOBURL),  # 8
            fetch_price(session, KucoinLTPURL),  # 9
            fetch_price(session, BitgetOBURL),  # 10
            fetch_price(session, BitgetLTPURL),  # 11
            fetch_price(session, BitstampOBURL),  # 12
            fetch_price(session, BitstampLTPURL),  # 13
            fetch_price(session, krakenOBURL),  # 14
            fetch_price(session, krakenLTPURL),  # 15
            fetch_price(session, Gateio_url_Orderbook),  # 16
            fetch_price(session, Gateio_url_Last_trade),  # 17
            fetch_price(session, HTXOBURL),  # 18
            fetch_price(session, HTXLTPURL),  # 19
            fetch_price(session, MEXCOBURL),  # 20
            fetch_price(session, MEXCLTPURL),  # 21
            fetch_price(session, LbankOBURL),  # 22
            fetch_price(session, LbankLTPURL),  # 23
            fetch_price(session, BitmartOBURL),  # 24
            fetch_price(session, BitmartLTPURL),  # 25
            fetch_price(session, DeepcoinOBURL),  # 26
            fetch_price(session, DeepcoinLTPURL),  # 27
            fetch_price(session, BitfinexOBURL),  # 28
            fetch_price(session, BitfinexLTPURL),  # 29
            fetch_price(session, BingxOBURL),  # 30
            fetch_price(session, BingxLTPURL),  # 31
            fetch_price(session, OrangeXOBURL),  # 32
            fetch_price(session, OrangeXLTPURL),  # 33
            fetch_price(session, BitvenusOBURL),  # 34
            fetch_price(session, BitvenusLTPURL),  # 35
            fetch_price(session, BICONOMYOBURL),  # 36
            fetch_price(session, BICONOMYLTPURL),  # 37
            fetch_price(session, GeminiOBURL),  # 38
            fetch_price(session, GeminiLTPURL),  # 39
            fetch_price(session, XTOBURL),  # 40
            fetch_price(session, XTLTPURL),  # 41
            fetch_price(session, BitflyerOBURL),  # 42
            fetch_price(session, BitflyerLTPURL),  # 43
            fetch_price(session, CoinWOBURL),  # 44
            fetch_price(session, CoinWLTPURL),  # 45
            fetch_price(session, ToobitOBURL),  # 46
            fetch_price(session, ToobitLTPURL),  # 47
            fetch_price(session, TapbitOBURL),  # 48
            fetch_price(session, TapbitLTPURL),  # 49

        ]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

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

        Binance_Status = 'OK'
        BybitStatus = 'OK'
        OKX_Status = 'OK'
        Upbit_Status = 'NOT OK'
        Kucoin_Status = 'OK'
        Bitget_Status = 'OK'
        Bitstamp_Status = 'OK'
        Gemini_Status = 'OK'
        Kraken_Status = 'OK'
        Gateio_Status = 'OK'
        HTX_Status = 'OK'
        MEXC_Status = 'OK'
        Lbank_Status = 'OK'
        Bitmart_Status = 'OK'
        Deepcoin_Status = 'OK'
        Bitfinex_Status = 'OK'
        BingX_Status = 'OK'
        OrangeX_Status = 'OK'
        Bitvenus_Status = 'OK'
        Biconomy_Status = 'OK'
        XT_Status = 'OK'
        Bitflyer_Status = 'OK'
        CoinW_Status = 'OK'
        Toobit_Status = 'OK'
        TapBit_Status = 'OK'

        if responses[0] == None:
            Binance_Status = 'NOT OK'
        if responses[2] == None:
            BybitStatus = 'NOT OK'
        if responses[4] == None:
            OKX_Status = 'NOT OK'
        if responses[6] == None:
            Upbit_Status = 'NOT OK'
        if responses[8] == None:
            Kucoin_Status = 'NOT OK'
        if responses[10] == None:
            Bitget_Status = 'NOT OK'
        if responses[12] == None:
            Bitstamp_Status = 'NOT OK'

        if responses[14] == None:
            Kraken_Status = 'NOT OK'
        if responses[16] == None:
            Gateio_Status = 'NOT OK'
        if responses[18] == None:
            HTX_Status = 'NOT OK'
        if responses[20] == None:
            MEXC_Status = 'NOT OK'
        if responses[22] == None:
            Lbank_Status = 'NOT OK'
        if responses[24] == None:
            Bitmart_Status = 'NOT OK'
        if responses[26] == None:
            Deepcoin_Status = 'NOT OK'

        if responses[28] == None:
            Bitfinex_Status = 'NOT OK'
        if responses[30] == None:
            BingX_Status = 'NOT OK'
        if responses[32] == None:
            OrangeX_Status = 'NOT OK'
        if responses[34] == None:
            Bitvenus_Status = 'NOT OK'
        if responses[36] == None:
            Biconomy_Status = 'NOT OK'
        if responses[38] == None:
            Gemini_Status = 'NOT OK'
        if responses[40] == None:
            XT_Status = 'NOT OK'

        if responses[42] == None:
            Bitflyer_Status = 'NOT OK'
        if responses[44] == None:
            CoinW_Status = 'NOT OK'
        if responses[46] == None:
            Toobit_Status = 'NOT OK'
        if responses[48] == None:
            TapBit_Status = 'NOT OK'

        try:
            BinanceOBRes = responses[0]
            if BinanceOBRes:
                BinanceBP1 = float(BinanceOBRes['bids'][0][0])
                BinanceBP2 = float(BinanceOBRes['bids'][1][0])
                BinanceBP3 = float(BinanceOBRes['bids'][2][0])
                BinanceBP4 = float(BinanceOBRes['bids'][3][0])
                BinanceBP5 = float(BinanceOBRes['bids'][4][0])
                BinanceBP1V = float(BinanceOBRes['bids'][0][1])
                BinanceBP2V = float(BinanceOBRes['bids'][1][1])
                BinanceBP3V = float(BinanceOBRes['bids'][2][1])
                BinanceBP4V = float(BinanceOBRes['bids'][3][1])
                BinanceBP5V = float(BinanceOBRes['bids'][4][1])
                BinanceAP1 = float(BinanceOBRes['asks'][0][0])
                BinanceAP2 = float(BinanceOBRes['asks'][1][0])
                BinanceAP3 = float(BinanceOBRes['asks'][2][0])
                BinanceAP4 = float(BinanceOBRes['asks'][3][0])
                BinanceAP5 = float(BinanceOBRes['asks'][4][0])
                BinanceAP1V = float(BinanceOBRes['asks'][0][1])
                BinanceAP2V = float(BinanceOBRes['asks'][1][1])
                BinanceAP3V = float(BinanceOBRes['asks'][2][1])
                BinanceAP4V = float(BinanceOBRes['asks'][3][1])
                BinanceAP5V = float(BinanceOBRes['asks'][4][1])
                BinanceLTPURLRes = responses[1]
                if BinanceLTPURLRes:
                    BinanceLTP = float(BinanceLTPURLRes['lastPrice'])
                    BinanceLTPV = BinanceLTPURLRes['lastQty']
                    BinanceLTPTM = int(BinanceLTPURLRes['closeTime'])
                    BinanceLTPT = await convert_to_gmt5_async(BinanceLTPTM)
        except Exception as e:
            print(f"Error processing Binance order book data: {e}")
            Binance_Status = 'NOT OK'
        try:
            BybitOBURLRes = responses[2]
            if BybitOBURLRes:
                BybitBP1 = float(BybitOBURLRes['result'][0]['price'])
                BybitBP2 = float(BybitOBURLRes['result'][1]['price'])
                BybitBP3 = float(BybitOBURLRes['result'][2]['price'])
                BybitBP4 = float(BybitOBURLRes['result'][3]['price'])
                BybitBP5 = float(BybitOBURLRes['result'][4]['price'])
                BybitBP1V = float(BybitOBURLRes['result'][0]['size'])
                BybitBP2V = float(BybitOBURLRes['result'][1]['size'])
                BybitBP3V = float(BybitOBURLRes['result'][2]['size'])
                BybitBP4V = float(BybitOBURLRes['result'][3]['size'])
                BybitBP5V = float(BybitOBURLRes['result'][4]['size'])
                BybitAP1 = float(BybitOBURLRes['result'][5]['price'])
                BybitAP2 = float(BybitOBURLRes['result'][6]['price'])
                BybitAP3 = float(BybitOBURLRes['result'][7]['price'])
                BybitAP4 = float(BybitOBURLRes['result'][8]['price'])
                BybitAP5 = float(BybitOBURLRes['result'][9]['price'])
                BybitAP1V = float(BybitOBURLRes['result'][5]['size'])
                BybitAP2V = float(BybitOBURLRes['result'][6]['size'])
                BybitAP3V = float(BybitOBURLRes['result'][7]['size'])
                BybitAP4V = float(BybitOBURLRes['result'][8]['size'])
                BybitAP5V = float(BybitOBURLRes['result'][9]['size'])
                BybitOBTM = float(BybitOBURLRes['time_now'])
                BybitOBT = await convert_to_gmt5_async(BybitOBTM)
                BybitLTPURLRes = responses[3]
                if BybitLTPURLRes:
                    BybitLTP = float(BybitLTPURLRes['result'][0]['last_price'])
                    BybitLTPV = 0
                    BybitLTPTM = float(BybitLTPURLRes['time_now'])
                    BybitLTPT = await convert_to_gmt5_async(BybitLTPTM)
        except Exception as e:
            print(f"Error processing Bybit order book data: {e}")
            BybitStatus = 'NOT OK'
        try:
            OKXOBBURLRes = responses[4]
            if OKXOBBURLRes:
                OKXAP1 = float(OKXOBBURLRes['data'][0]['asks'][0][0])
                OKXAP2 = float(OKXOBBURLRes['data'][0]['asks'][1][0])
                OKXAP3 = float(OKXOBBURLRes['data'][0]['asks'][2][0])
                OKXAP4 = float(OKXOBBURLRes['data'][0]['asks'][3][0])
                OKXAP5 = float(OKXOBBURLRes['data'][0]['asks'][4][0])
                OKXAP1V = float(OKXOBBURLRes['data'][0]['asks'][0][1])
                OKXAP2V = float(OKXOBBURLRes['data'][0]['asks'][1][1])
                OKXAP3V = float(OKXOBBURLRes['data'][0]['asks'][2][1])
                OKXAP4V = float(OKXOBBURLRes['data'][0]['asks'][3][1])
                OKXAP5V = float(OKXOBBURLRes['data'][0]['asks'][4][1])
                OKXBP1 = float(OKXOBBURLRes['data'][0]['bids'][0][0])
                OKXBP2 = float(OKXOBBURLRes['data'][0]['bids'][1][0])
                OKXBP3 = float(OKXOBBURLRes['data'][0]['bids'][2][0])
                OKXBP4 = float(OKXOBBURLRes['data'][0]['bids'][3][0])
                OKXBP5 = float(OKXOBBURLRes['data'][0]['bids'][4][0])
                OKXBP1V = float(OKXOBBURLRes['data'][0]['bids'][0][1])
                OKXBP2V = float(OKXOBBURLRes['data'][0]['bids'][1][1])
                OKXBP3V = float(OKXOBBURLRes['data'][0]['bids'][2][1])
                OKXBP4V = float(OKXOBBURLRes['data'][0]['bids'][3][1])
                OKXBP5V = float(OKXOBBURLRes['data'][0]['bids'][4][1])
                OKXOBTM = int(OKXOBBURLRes['data'][0]['ts'])
                OKXOBT = await convert_to_gmt5_async(OKXOBTM)
                OKXLTPURLRes = responses[5]
                if OKXLTPURLRes:
                    OKXLTP = float(OKXLTPURLRes['data'][0]['last'])
                    OKXLTPV = OKXLTPURLRes['data'][0]['lastSz']
                    OKXLTPTM = int(OKXLTPURLRes['data'][0]['ts'])
                    OKXLTPT = await convert_to_gmt5_async(OKXLTPTM)
        except Exception as e:
            print(f"Error processing OKX order book data: {e}")
            OKX_Status = 'NOT OK'
        try:
            UpbitOBURLRes = responses[6]
            if UpbitOBURLRes:
                UpbitOBTM = int(UpbitOBURLRes[0]['timestamp'])
                UpbitOBT = await convert_to_gmt5_async(UpbitOBTM)
                UpbitAP1 = float(UpbitOBURLRes[0]['orderbook_units'][0]['ask_price'])
                UpbitBP1 = float(UpbitOBURLRes[0]['orderbook_units'][0]['bid_price'])
                UpbitAP1V = float(UpbitOBURLRes[0]['orderbook_units'][0]['ask_size'])
                UpbitBP1V = float(UpbitOBURLRes[0]['orderbook_units'][0]['bid_size'])
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
                UpbitLTPURLRes = responses[7]
                UpbitLTP = float(UpbitLTPURLRes[0]['trade_price'])
                UpbitLTPV = UpbitLTPURLRes[0]['trade_volume']
                UpbitLTPTM = UpbitLTPURLRes[0]['trade_timestamp']
                UpbitLTPT = await convert_to_gmt5_async(UpbitLTPTM)
        except Exception as e:
            print(f"Error processing Upbit order book data: {e}")
            Upbit_Status = 'NOT OK'
        try:
            KucoinOBURLRes = responses[8]
            if KucoinOBURLRes:
                KucoinOBTM = KucoinOBURLRes['data']['time']
                KucoinOBT = await convert_to_gmt5_async(KucoinOBTM)
                KucoinBP1 = float(KucoinOBURLRes['data']['bids'][0][0])
                KucoinBP2 = float(KucoinOBURLRes['data']['bids'][1][0])
                KucoinBP3 = float(KucoinOBURLRes['data']['bids'][2][0])
                KucoinBP4 = float(KucoinOBURLRes['data']['bids'][3][0])
                KucoinBP5 = float(KucoinOBURLRes['data']['bids'][4][0])
                KucoinBP1V = float(KucoinOBURLRes['data']['bids'][0][1])
                KucoinBP2V = float(KucoinOBURLRes['data']['bids'][1][1])
                KucoinBP3V = float(KucoinOBURLRes['data']['bids'][2][1])
                KucoinBP4V = float(KucoinOBURLRes['data']['bids'][3][1])
                KucoinBP5V = float(KucoinOBURLRes['data']['bids'][4][1])
                KucoinAP1 = float(KucoinOBURLRes['data']['asks'][0][0])
                KucoinAP2 = float(KucoinOBURLRes['data']['asks'][1][0])
                KucoinAP3 = float(KucoinOBURLRes['data']['asks'][2][0])
                KucoinAP4 = float(KucoinOBURLRes['data']['asks'][3][0])
                KucoinAP5 = float(KucoinOBURLRes['data']['asks'][4][0])
                KucoinAP1V = float(KucoinOBURLRes['data']['asks'][0][1])
                KucoinAP2V = float(KucoinOBURLRes['data']['asks'][1][1])
                KucoinAP3V = float(KucoinOBURLRes['data']['asks'][2][1])
                KucoinAP4V = float(KucoinOBURLRes['data']['asks'][3][1])
                KucoinAP5V = float(KucoinOBURLRes['data']['asks'][4][1])
                KucoinLTPURLRes = responses[9]
                KucoinLTP = float(KucoinLTPURLRes['data']['last'])
                KucoinLTPV = 0
                KucoinLTPTM = KucoinLTPURLRes['data']['time']
                KucoinLTPT = await convert_to_gmt5_async(KucoinLTPTM)
        except Exception as e:
            print(f"Error processing Kucoin order book data: {e}")
            Kucoin_Status = 'NOT OK'
        try:
            BitgetOBURLRes = responses[10]
            if BitgetOBURLRes:
                BitgetOBTM = BitgetOBURLRes['requestTime']
                BitgetOBT = await convert_to_gmt5_async(BitgetOBTM)
                BitgetAP1 = float(BitgetOBURLRes['data']['asks'][0][0])
                BitgetAP2 = float(BitgetOBURLRes['data']['asks'][1][0])
                BitgetAP3 = float(BitgetOBURLRes['data']['asks'][2][0])
                BitgetAP4 = float(BitgetOBURLRes['data']['asks'][3][0])
                BitgetAP5 = float(BitgetOBURLRes['data']['asks'][4][0])
                BitgetAP1V = float(BitgetOBURLRes['data']['asks'][0][1])
                BitgetAP2V = float(BitgetOBURLRes['data']['asks'][1][1])
                BitgetAP3V = float(BitgetOBURLRes['data']['asks'][2][1])
                BitgetAP4V = float(BitgetOBURLRes['data']['asks'][3][1])
                BitgetAP5V = float(BitgetOBURLRes['data']['asks'][4][1])
                BitgetBP1 = float(BitgetOBURLRes['data']['bids'][0][0])
                BitgetBP2 = float(BitgetOBURLRes['data']['bids'][1][0])
                BitgetBP3 = float(BitgetOBURLRes['data']['bids'][2][0])
                BitgetBP4 = float(BitgetOBURLRes['data']['bids'][3][0])
                BitgetBP5 = float(BitgetOBURLRes['data']['bids'][4][0])
                BitgetBP1V = float(BitgetOBURLRes['data']['bids'][0][1])
                BitgetBP2V = float(BitgetOBURLRes['data']['bids'][1][1])
                BitgetBP3V = float(BitgetOBURLRes['data']['bids'][2][1])
                BitgetBP4V = float(BitgetOBURLRes['data']['bids'][3][1])
                BitgetBP5V = float(BitgetOBURLRes['data']['bids'][4][1])
                BitgetLTPURLRes = responses[11]
                BitgetLTP = float(BitgetLTPURLRes['data'][0]['lastPr'])
                BitgetLTPTM = int(BitgetLTPURLRes['data'][0]['ts'])
                BitgetLTPV = 0
                BitgetLTPT = await convert_to_gmt5_async(BitgetLTPTM)
        except Exception as e:
            print(f"Error processing Bitget order book data: {e}")
            Bitget_Status = 'NOT OK'
        try:
            BitstampOBURLRes = responses[12]
            if BitstampOBURLRes:
                BitstampOBTM = int(BitstampOBURLRes['timestamp'])
                BitstampOBT = await convert_to_gmt5_async(BitstampOBTM)
                BitstampBP1 = float(BitstampOBURLRes['bids'][0][0])
                BitstampBP2 = float(BitstampOBURLRes['bids'][1][0])
                BitstampBP3 = float(BitstampOBURLRes['bids'][2][0])
                BitstampBP4 = float(BitstampOBURLRes['bids'][3][0])
                BitstampBP5 = float(BitstampOBURLRes['bids'][4][0])
                BitstampBP1V = float(BitstampOBURLRes['bids'][0][1])
                BitstampBP2V = float(BitstampOBURLRes['bids'][1][1])
                BitstampBP3V = float(BitstampOBURLRes['bids'][2][1])
                BitstampBP4V = float(BitstampOBURLRes['bids'][3][1])
                BitstampBP5V = float(BitstampOBURLRes['bids'][4][1])
                BitstampAP1 = float(BitstampOBURLRes['asks'][0][0])
                BitstampAP2 = float(BitstampOBURLRes['asks'][1][0])
                BitstampAP3 = float(BitstampOBURLRes['asks'][2][0])
                BitstampAP4 = float(BitstampOBURLRes['asks'][3][0])
                BitstampAP5 = float(BitstampOBURLRes['asks'][4][0])
                BitstampAP1V = float(BitstampOBURLRes['asks'][0][1])
                BitstampAP2V = float(BitstampOBURLRes['asks'][1][1])
                BitstampAP3V = float(BitstampOBURLRes['asks'][2][1])
                BitstampAP4V = float(BitstampOBURLRes['asks'][3][1])
                BitstampAP5V = float(BitstampOBURLRes['asks'][4][1])
                BitstampLTPURLRes = responses[13]
                BitstampLTP = float(BitstampLTPURLRes['last'])
                BitstampLTPV = BitstampLTPURLRes['volume']
                BitstampLTPTM = int(BitstampLTPURLRes['timestamp'])
                BitstampLTPT = await convert_to_gmt5_async(BitstampLTPTM)
        except Exception as e:
            print(f"Error processing Bitstamp order book data: {e}")
            Bitstamp_Status = 'NOT OK'
        try:
            GeminiOBURLRes = responses[38]
            if GeminiOBURLRes:
                GeminiOBTM = int(GeminiOBURLRes['bids'][0]['timestamp'])
                GeminiOBT = await convert_to_gmt5_async(GeminiOBTM)
                GeminiBP1 = float(GeminiOBURLRes['bids'][0]['price'])
                GeminiBP2 = float(GeminiOBURLRes['bids'][1]['price'])
                GeminiBP3 = float(GeminiOBURLRes['bids'][2]['price'])
                GeminiBP4 = float(GeminiOBURLRes['bids'][3]['price'])
                GeminiBP5 = float(GeminiOBURLRes['bids'][4]['price'])
                GeminiBP1V = float(GeminiOBURLRes['bids'][0]['amount'])
                GeminiBP2V = float(GeminiOBURLRes['bids'][1]['amount'])
                GeminiBP3V = float(GeminiOBURLRes['bids'][2]['amount'])
                GeminiBP4V = float(GeminiOBURLRes['bids'][3]['amount'])
                GeminiBP5V = float(GeminiOBURLRes['bids'][4]['amount'])
                GeminiAP1 = float(GeminiOBURLRes['asks'][0]['price'])
                GeminiAP2 = float(GeminiOBURLRes['asks'][1]['price'])
                GeminiAP3 = float(GeminiOBURLRes['asks'][2]['price'])
                GeminiAP4 = float(GeminiOBURLRes['asks'][3]['price'])
                GeminiAP5 = float(GeminiOBURLRes['asks'][4]['price'])
                GeminiAP1V = float(GeminiOBURLRes['asks'][0]['amount'])
                GeminiAP2V = float(GeminiOBURLRes['asks'][1]['amount'])
                GeminiAP3V = float(GeminiOBURLRes['asks'][2]['amount'])
                GeminiAP4V = float(GeminiOBURLRes['asks'][3]['amount'])
                GeminiAP5V = float(GeminiOBURLRes['asks'][4]['amount'])
                GeminiLTPURLRes = responses[39]
                GeminiLTP = float(GeminiLTPURLRes['last'])
                GeminiLTPV = GeminiLTPURLRes['volume']['BTC']
                GeminiLTPTM = GeminiLTPURLRes['volume']['timestamp']
                GeminiLTPT = await convert_to_gmt5_async(GeminiLTPTM)
        except Exception as e:
            print(f"Error processing Gemini order book data: {e}")
            Gemini_Status = "NOT OK"
        try:
            KrakenOBURL_Res = responses[14]
            if KrakenOBURL_Res:
                KrakenAP1 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][0])
                KrakenAP2 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][1][0])
                KrakenAP3 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][2][0])
                KrakenAP4 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][3][0])
                KrakenAP5 = float(KrakenOBURL_Res['result']['XBTUSDT']['asks'][4][0])
                KrakenAPV1 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][1]
                KrakenAPV2 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][1][1]
                KrakenAPV3 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][2][1]
                KrakenAPV4 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][3][1]
                KrakenAPV5 = KrakenOBURL_Res['result']['XBTUSDT']['asks'][4][1]
                KrakenBP1 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][0][0])
                KrakenBP2 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][1][0])
                KrakenBP3 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][2][0])
                KrakenBP4 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][3][0])
                KrakenBP5 = float(KrakenOBURL_Res['result']['XBTUSDT']['bids'][4][0])
                KrakenBPV1 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][0][1]
                KrakenBPV2 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][1][1]
                KrakenBPV3 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][2][1]
                KrakenBPV4 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][3][1]
                KrakenBPV5 = KrakenOBURL_Res['result']['XBTUSDT']['bids'][4][1]
                KrakenOBTM = KrakenOBURL_Res['result']['XBTUSDT']['asks'][0][2]
                KrakenOBT = await convert_to_gmt5_async(KrakenOBTM)
                KrakenLTP_Res = responses[15]
                KrakenLTP = float(KrakenLTP_Res['result']['XBTUSDT'][0][0])
                KrakenLTPV = KrakenLTP_Res['result']['XBTUSDT'][0][1]
                KrakenLTPTM = int(KrakenLTP_Res['result']['XBTUSDT'][0][2])
                KrakenLTPT = await convert_to_gmt5_async(KrakenLTPTM)

        except Exception as e:
            print(f"Error processing Kraken order book data: {e}")
            Kraken_Status = 'NOT OK'

        try:
            Gateio_url_Orderbook_res = responses[16]
            if Gateio_url_Orderbook_res:
                GateioAP1 = float(Gateio_url_Orderbook_res['asks'][0][0])
                GateioAP2 = float(Gateio_url_Orderbook_res['asks'][1][0])
                GateioAP3 = float(Gateio_url_Orderbook_res['asks'][2][0])
                GateioAP4 = float(Gateio_url_Orderbook_res['asks'][3][0])
                GateioAP5 = float(Gateio_url_Orderbook_res['asks'][4][0])
                GateioAPV1 = float(Gateio_url_Orderbook_res['asks'][0][1])
                GateioAPV2 = float(Gateio_url_Orderbook_res['asks'][1][1])
                GateioAPV3 = float(Gateio_url_Orderbook_res['asks'][2][1])
                GateioAPV4 = float(Gateio_url_Orderbook_res['asks'][3][1])
                GateioAPV5 = float(Gateio_url_Orderbook_res['asks'][4][1])
                GateioBP1 = float(Gateio_url_Orderbook_res['bids'][0][0])
                GateioBP2 = float(Gateio_url_Orderbook_res['bids'][1][0])
                GateioBP3 = float(Gateio_url_Orderbook_res['bids'][2][0])
                GateioBP4 = float(Gateio_url_Orderbook_res['bids'][3][0])
                GateioBP5 = float(Gateio_url_Orderbook_res['bids'][4][0])
                GateioBPV1 = float(Gateio_url_Orderbook_res['bids'][0][1])
                GateioBPV2 = float(Gateio_url_Orderbook_res['bids'][1][1])
                GateioBPV3 = float(Gateio_url_Orderbook_res['bids'][2][1])
                GateioBPV4 = float(Gateio_url_Orderbook_res['bids'][3][1])
                GateioBPV5 = float(Gateio_url_Orderbook_res['bids'][4][1])
                Gateio_url_Last_trade_res = responses[17]
                GateioLTP = float(Gateio_url_Last_trade_res['last'])
        except Exception as e:
            print(f"Error processing Gate.io order book data: {e}")
            Gateio_Status = 'NOT OK'

        try:
            HTXOBRes = responses[18]
            if HTXOBRes:
                HTXOBTM = int(HTXOBRes['ts'])
                HTXOBT = HTXOBTM
                HTXBP1 = float(HTXOBRes['tick']['bids'][0][0])
                HTXBP2 = float(HTXOBRes['tick']['bids'][1][0])
                HTXBP3 = float(HTXOBRes['tick']['bids'][2][0])
                HTXBP4 = float(HTXOBRes['tick']['bids'][3][0])
                HTXBP5 = float(HTXOBRes['tick']['bids'][4][0])
                HTXBP1V = float(HTXOBRes['tick']['bids'][0][1])
                HTXBP2V = float(HTXOBRes['tick']['bids'][1][1])
                HTXBP3V = float(HTXOBRes['tick']['bids'][2][1])
                HTXBP4V = float(HTXOBRes['tick']['bids'][3][1])
                HTXBP5V = float(HTXOBRes['tick']['bids'][4][1])
                HTXAP1 = float(HTXOBRes['tick']['asks'][0][0])
                HTXAP2 = float(HTXOBRes['tick']['asks'][1][0])
                HTXAP3 = float(HTXOBRes['tick']['asks'][2][0])
                HTXAP4 = float(HTXOBRes['tick']['asks'][3][0])
                HTXAP5 = float(HTXOBRes['tick']['asks'][4][0])
                HTXAP1V = float(HTXOBRes['tick']['asks'][0][1])
                HTXAP2V = float(HTXOBRes['tick']['asks'][1][1])
                HTXAP3V = float(HTXOBRes['tick']['asks'][2][1])
                HTXAP4V = float(HTXOBRes['tick']['asks'][3][1])
                HTXAP5V = float(HTXOBRes['tick']['asks'][4][1])
                HTXLTPURL_Res = responses[19]
                HTXLTPTM = int(HTXLTPURL_Res['tick']['ts'])
                HTXLTPT = HTXLTPTM
                HTXLTP = float(HTXLTPURL_Res['tick']['data'][0]['price'])
                HTXLTPV = HTXLTPURL_Res['tick']['data'][0]['amount']
        except Exception as e:
            print(f"Error processing HXT order book data: {e}")
            HTX_Status = 'NOT OK'

        try:
            MEXCOBRes = responses[20]
            if MEXCOBRes:
                MEXCBP1 = float(MEXCOBRes['bids'][0][0])
                MEXCBP2 = float(MEXCOBRes['bids'][1][0])
                MEXCBP3 = float(MEXCOBRes['bids'][2][0])
                MEXCBP4 = float(MEXCOBRes['bids'][3][0])
                MEXCBP5 = float(MEXCOBRes['bids'][4][0])
                MEXCBP1V = float(MEXCOBRes['bids'][0][1])
                MEXCBP2V = float(MEXCOBRes['bids'][1][1])
                MEXCBP3V = float(MEXCOBRes['bids'][2][1])
                MEXCBP4V = float(MEXCOBRes['bids'][3][1])
                MEXCBP5V = float(MEXCOBRes['bids'][4][1])
                MEXCAP1 = float(MEXCOBRes['asks'][0][0])
                MEXCAP2 = float(MEXCOBRes['asks'][1][0])
                MEXCAP3 = float(MEXCOBRes['asks'][2][0])
                MEXCAP4 = float(MEXCOBRes['asks'][3][0])
                MEXCAP5 = float(MEXCOBRes['asks'][4][0])
                MEXCAP1V = float(MEXCOBRes['asks'][0][1])
                MEXCAP2V = float(MEXCOBRes['asks'][1][1])
                MEXCAP3V = float(MEXCOBRes['asks'][2][1])
                MEXCAP4V = float(MEXCOBRes['asks'][3][1])
                MEXCAP5V = float(MEXCOBRes['asks'][4][1])
                MEXCOBTM = int(MEXCOBRes['timestamp'])
                MEXCOBT = MEXCOBTM
                MEXCLTPURL_Res = responses[21]
                MEXCLTP = float(MEXCLTPURL_Res[0]['price'])
                MEXCLTPV = MEXCLTPURL_Res[0]['qty']
                MEXCLTPTM = int(MEXCLTPURL_Res[0]['time'])
                MEXCLTPT = MEXCLTPTM
        except Exception as e:
            print(f"Error processing MEXC order book data: {e}")
            MEXC_Status = 'NOT OK'
        try:
            LbankOBRes = responses[22]
            if LbankOBRes:
                LbankAP1 = float(LbankOBRes['data']['asks'][0][0])
                LbankAP2 = LbankOBRes['data']['asks'][1][0]
                LbankAP3 = LbankOBRes['data']['asks'][2][0]
                LbankAP4 = LbankOBRes['data']['asks'][3][0]
                LbankAP5 = LbankOBRes['data']['asks'][4][0]
                LbankAP1V = LbankOBRes['data']['asks'][0][1]
                LbankAP2V = LbankOBRes['data']['asks'][1][1]
                LbankAP3V = LbankOBRes['data']['asks'][2][1]
                LbankAP4V = LbankOBRes['data']['asks'][3][1]
                LbankAP5V = LbankOBRes['data']['asks'][4][1]
                LbankBP1 = float(LbankOBRes['data']['bids'][0][0])
                LbankBP2 = LbankOBRes['data']['bids'][1][0]
                LbankBP3 = LbankOBRes['data']['bids'][2][0]
                LbankBP4 = LbankOBRes['data']['bids'][3][0]
                LbankBP5 = LbankOBRes['data']['bids'][4][0]
                LbankBP1V = LbankOBRes['data']['bids'][0][1]
                LbankBP2V = LbankOBRes['data']['bids'][1][1]
                LbankBP3V = LbankOBRes['data']['bids'][2][1]
                LbankBP4V = LbankOBRes['data']['bids'][3][1]
                LbankBP5V = LbankOBRes['data']['bids'][4][1]
                LbankOBTM = int(LbankOBRes['data']['timestamp'])
                LbankOBT = LbankOBTM
                LbankLTPURL_Res = responses[23]
                LbankLTP = float(LbankLTPURL_Res['data'][0]['ticker']['latest'])
                LbankLTPTM = LbankLTPURL_Res['data'][0]['timestamp']
                LbankLTPT = LbankLTPTM
        except Exception as e:
            print(f"Error processing Lbank order book data: {e}")
            Lbank_Status = 'NOT OK'
        try:
            BitmartOBRes = responses[24]
            if BitmartOBRes:
                BitmartOBTM = int(BitmartOBRes['data']['ts'])
                BitmartOBT = BitmartOBTM
                BitmartAP1 = float(BitmartOBRes['data']['asks'][0][0])
                BitmartAP2 = BitmartOBRes['data']['asks'][1][0]
                BitmartAP3 = BitmartOBRes['data']['asks'][2][0]
                BitmartAP4 = BitmartOBRes['data']['asks'][3][0]
                BitmartAP5 = BitmartOBRes['data']['asks'][4][0]
                BitmartAP1V = BitmartOBRes['data']['asks'][0][1]
                BitmartAP2V = BitmartOBRes['data']['asks'][1][1]
                BitmartAP3V = BitmartOBRes['data']['asks'][2][1]
                BitmartAP4V = BitmartOBRes['data']['asks'][3][1]
                BitmartAP5V = BitmartOBRes['data']['asks'][4][1]
                BitmartBP1 = float(BitmartOBRes['data']['bids'][0][0])
                BitmartBP2 = BitmartOBRes['data']['bids'][1][0]
                BitmartBP3 = BitmartOBRes['data']['bids'][2][0]
                BitmartBP4 = BitmartOBRes['data']['bids'][3][0]
                BitmartBP5 = BitmartOBRes['data']['bids'][4][0]
                BitmartBP1V = BitmartOBRes['data']['bids'][0][1]
                BitmartBP2V = BitmartOBRes['data']['bids'][1][1]
                BitmartBP3V = BitmartOBRes['data']['bids'][2][1]
                BitmartBP4V = BitmartOBRes['data']['bids'][3][1]
                BitmartBP5V = BitmartOBRes['data']['bids'][4][1]
                BitmartLTPURL_Res = responses[25]
                BitmartLTPTM = int(BitmartLTPURL_Res['data'][0][1])
                BitmartLTPT = BitmartLTPTM
                BitmartLTP = float(BitmartLTPURL_Res['data'][0][2])
                BitmartLTPV = BitmartLTPURL_Res['data'][0][3]
        except Exception as e:
            print(f"Error processing BitMart order book data: {e}")
            Bitmart_Status = 'NOT OK'
        try:
            DeepcoinOBRes = responses[26]
            if DeepcoinOBRes:
                DeepcoinBP1 = float(DeepcoinOBRes['data']['bids'][0][0])
                DeepcoinBP2 = DeepcoinOBRes['data']['bids'][1][0]
                DeepcoinBP3 = DeepcoinOBRes['data']['bids'][2][0]
                DeepcoinBP4 = DeepcoinOBRes['data']['bids'][3][0]
                DeepcoinBP5 = DeepcoinOBRes['data']['bids'][4][0]
                DeepcoinBP1V = DeepcoinOBRes['data']['bids'][0][1]
                DeepcoinBP2V = DeepcoinOBRes['data']['bids'][1][1]
                DeepcoinBP3V = DeepcoinOBRes['data']['bids'][2][1]
                DeepcoinBP4V = DeepcoinOBRes['data']['bids'][3][1]
                DeepcoinBP5V = DeepcoinOBRes['data']['bids'][4][1]
                DeepcoinAP1 = float(DeepcoinOBRes['data']['asks'][0][0])
                DeepcoinAP2 = DeepcoinOBRes['data']['asks'][1][0]
                DeepcoinAP3 = DeepcoinOBRes['data']['asks'][2][0]
                DeepcoinAP4 = DeepcoinOBRes['data']['asks'][3][0]
                DeepcoinAP5 = DeepcoinOBRes['data']['asks'][4][0]
                DeepcoinAP1V = DeepcoinOBRes['data']['asks'][0][1]
                DeepcoinAP2V = DeepcoinOBRes['data']['asks'][1][1]
                DeepcoinAP3V = DeepcoinOBRes['data']['asks'][2][1]
                DeepcoinAP4V = DeepcoinOBRes['data']['asks'][3][1]
                DeepcoinAP5V = DeepcoinOBRes['data']['asks'][4][1]
                DeepcoinLTPURL_Res = responses[27]
                DeepcoinLTP = float(DeepcoinLTPURL_Res['data'][30]['last'])
                DeepcoinLTPTM = int(DeepcoinLTPURL_Res['data'][30]['ts'])
                DeepcoinLTPT = DeepcoinLTPTM
        except Exception as e:
            print(f"Error processing DeepCOin order book data: {e}")
            Deepcoin_Status = 'NOT OK'
        try:
            BitfinexOBRes = responses[28]
            if BitfinexOBRes:
                BitfinexBP1 = float(BitfinexOBRes[0][0])
                BitfinexBP2 = BitfinexOBRes[1][0]
                BitfinexBP3 = BitfinexOBRes[2][0]
                BitfinexBP4 = BitfinexOBRes[3][0]
                BitfinexBP5 = BitfinexOBRes[4][0]
                BitfinexBP1V = BitfinexOBRes[0][2]
                BitfinexBP2V = BitfinexOBRes[1][2]
                BitfinexBP3V = BitfinexOBRes[2][2]
                BitfinexBP4V = BitfinexOBRes[3][2]
                BitfinexBP5V = BitfinexOBRes[4][2]
                BitfinexAP1 = float(BitfinexOBRes[25][0])
                BitfinexAP2 = BitfinexOBRes[26][0]
                BitfinexAP3 = BitfinexOBRes[27][0]
                BitfinexAP4 = BitfinexOBRes[28][0]
                BitfinexAP5 = BitfinexOBRes[29][0]
                BitfinexAP1V = BitfinexOBRes[25][2]
                BitfinexAP2V = BitfinexOBRes[26][2]
                BitfinexAP3V = BitfinexOBRes[27][2]
                BitfinexAP4V = BitfinexOBRes[28][2]
                BitfinexAP5V = BitfinexOBRes[29][2]
                BitfinexLTPURL_Res = responses[29]
                BitfinexLTP = float(BitfinexLTPURL_Res[0][7])
        except Exception as e:
            print(f"Error processing Bitfinex order book data: {e}")
            Bitfinex_Status = 'NOT OK'
        try:
            BingxOBRes = responses[30]
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
                BingXBP1V = BingxOBRes['data']['bidsCoin'][0][1]
                BingXBP2V = BingxOBRes['data']['bidsCoin'][1][1]
                BingXBP3V = BingxOBRes['data']['bidsCoin'][2][1]
                BingXBP4V = BingxOBRes['data']['bidsCoin'][3][1]
                BingXBP5V = BingxOBRes['data']['bidsCoin'][4][1]
                BingXAP1V = BingxOBRes['data']['asksCoin'][0][1]
                BingXAP2V = BingxOBRes['data']['asksCoin'][1][1]
                BingXAP3V = BingxOBRes['data']['asksCoin'][2][1]
                BingXAP4V = BingxOBRes['data']['asksCoin'][3][1]
                BingXAP5V = BingxOBRes['data']['asksCoin'][4][1]
                BingxLTPURL_Res = responses[31]
                BingXLTPTM = int(BingxLTPURL_Res['data'][0]['time'])
                BingXLTPT = BingXLTPTM
                BingXLTP = float(BingxLTPURL_Res['data'][0]['price'])
                BingXLTPV = BingxLTPURL_Res['data'][0]['qty']
        except Exception as e:
            print(f"Error processing BingX order book data: {e}")
            BingX_Status = 'NOT OK'
        try:
            OrangeXOBRes = responses[32]
            if OrangeXOBRes:
                OrangeXAP1 = float(OrangeXOBRes['result']['asks'][0][0])
                OrangeXAP2 = OrangeXOBRes['result']['asks'][1][0]
                OrangeXAP3 = OrangeXOBRes['result']['asks'][2][0]
                OrangeXAP4 = OrangeXOBRes['result']['asks'][3][0]
                OrangeXAP5 = OrangeXOBRes['result']['asks'][4][0]
                OrangeXAP1V = OrangeXOBRes['result']['asks'][0][1]
                OrangeXAP2V = OrangeXOBRes['result']['asks'][1][1]
                OrangeXAP3V = OrangeXOBRes['result']['asks'][2][1]
                OrangeXAP4V = OrangeXOBRes['result']['asks'][3][1]
                OrangeXAP5V = OrangeXOBRes['result']['asks'][4][1]
                OrangeXBP1 = float(OrangeXOBRes['result']['bids'][0][0])
                OrangeXBP2 = OrangeXOBRes['result']['bids'][1][0]
                OrangeXBP3 = OrangeXOBRes['result']['bids'][2][0]
                OrangeXBP4 = OrangeXOBRes['result']['bids'][3][0]
                OrangeXBP5 = OrangeXOBRes['result']['bids'][4][0]
                OrangeXBP1V = OrangeXOBRes['result']['bids'][0][1]
                OrangeXBP2V = OrangeXOBRes['result']['bids'][1][1]
                OrangeXBP3V = OrangeXOBRes['result']['bids'][2][1]
                OrangeXBP4V = OrangeXOBRes['result']['bids'][3][1]
                OrangeXBP5V = OrangeXOBRes['result']['bids'][4][1]
                OrangeXOBTM = int(OrangeXOBRes['result']['timestamp'])
                OrangeXOBT = OrangeXOBTM
                OrangeXLTPURL_Res = responses[33]
                OrangeXLTP = float(OrangeXLTPURL_Res['result'][0]['last_price'])
                OrangeXLTPTM = int(OrangeXLTPURL_Res['result'][0]['timestamp'])
                OrangeXLTPT = OrangeXLTPTM
        except Exception as e:
            print(f"Error processing OrangeX order book data: {e}")
            OrangeX_ = 'NOT OK'
        try:
            BitvinusOBRes = responses[34]
            if BitvinusOBRes:
                BitvenusOBTM = int(BitvinusOBRes['time'])
                BitvenusOBT = BitvenusOBTM
                BitvenusBP1 = float(BitvinusOBRes['bids'][0][0])
                BitvenusBP2 = BitvinusOBRes['bids'][1][0]
                BitvenusBP3 = BitvinusOBRes['bids'][2][0]
                BitvenusBP4 = BitvinusOBRes['bids'][3][0]
                BitvenusBP5 = BitvinusOBRes['bids'][4][0]
                BitvenusBP1V = BitvinusOBRes['bids'][0][1]
                BitvenusBP2V = BitvinusOBRes['bids'][1][1]
                BitvenusBP3V = BitvinusOBRes['bids'][2][1]
                BitvenusBP4V = BitvinusOBRes['bids'][3][1]
                BitvenusBP5V = BitvinusOBRes['bids'][4][1]
                BitvenusAP1 = float(BitvinusOBRes['asks'][0][0])
                BitvenusAP2 = BitvinusOBRes['asks'][1][0]
                BitvenusAP3 = BitvinusOBRes['asks'][2][0]
                BitvenusAP4 = BitvinusOBRes['asks'][3][0]
                BitvenusAP5 = BitvinusOBRes['asks'][4][0]
                BitvenusAP1V = BitvinusOBRes['asks'][0][1]
                BitvenusAP2V = BitvinusOBRes['asks'][1][1]
                BitvenusAP3V = BitvinusOBRes['asks'][2][1]
                BitvenusAP4V = BitvinusOBRes['asks'][3][1]
                BitvenusAP5V = BitvinusOBRes['asks'][4][1]
                BitvenusLTPURL_Res = responses[35]
                BitvenusLTP = float(BitvenusLTPURL_Res[0]['price'])
                BitvenusLTPV = float(BitvenusLTPURL_Res[0]['qty'])
                BitvenusLTPTM = int(BitvenusLTPURL_Res[0]['time'])
                BitvenusLTPT = BitvenusLTPTM
        except Exception as e:
            print(f"Error processing Bitvenus order book data: {e}")
            Bitvenus_Status = 'NOT OK'

        try:
            BiconomyOBRes = responses[36]
            if BiconomyOBRes:
                BiconomyAP1 = float(BiconomyOBRes['asks'][0][0])
                BiconomyAP2 = BiconomyOBRes['asks'][1][0]
                BiconomyAP3 = BiconomyOBRes['asks'][2][0]
                BiconomyAP4 = BiconomyOBRes['asks'][3][0]
                BiconomyAP5 = BiconomyOBRes['asks'][4][0]
                BiconomyAP1V = BiconomyOBRes['asks'][0][1]
                BiconomyAP2V = BiconomyOBRes['asks'][1][1]
                BiconomyAP3V = BiconomyOBRes['asks'][2][1]
                BiconomyAP4V = BiconomyOBRes['asks'][3][1]
                BiconomyAP5V = BiconomyOBRes['asks'][4][1]
                BiconomyBP1 = float(BiconomyOBRes['bids'][0][0])
                BiconomyBP2 = BiconomyOBRes['bids'][1][0]
                BiconomyBP3 = BiconomyOBRes['bids'][2][0]
                BiconomyBP4 = BiconomyOBRes['bids'][3][0]
                BiconomyBP5 = BiconomyOBRes['bids'][4][0]
                BiconomyBP1V = BiconomyOBRes['bids'][0][1]
                BiconomyBP2V = BiconomyOBRes['bids'][1][1]
                BiconomyBP3V = BiconomyOBRes['bids'][2][1]
                BiconomyBP4V = BiconomyOBRes['bids'][3][1]
                BiconomyBP5V = BiconomyOBRes['bids'][4][1]
                BICONOMYLTPURL_Res = responses[37]
                BiconomyLTPV = BICONOMYLTPURL_Res[0]['amount']
                BiconomyLTP = float(BICONOMYLTPURL_Res[0]['price'])
                BiconomyLTPTM = int(BICONOMYLTPURL_Res[0]['timestamp'])
                BiconomyLTPT = BiconomyLTPTM
        except Exception as e:
            print(f"Error processing Biconomy order book data: {e}")
            Biconomy_Status = "NOT OK"
        try:
            XTOBRes = responses[40]
            if XTOBRes:
                XTOBTM = int(XTOBRes['result']['timestamp'])
                XTOBT = await convert_to_gmt5_async(XTOBTM)
                XTBP1 = float(XTOBRes['result']['bids'][0][0])
                XTBP2 = XTOBRes['result']['bids'][1][0]
                XTBP3 = XTOBRes['result']['bids'][2][0]
                XTBP4 = XTOBRes['result']['bids'][3][0]
                XTBP5 = XTOBRes['result']['bids'][4][0]
                XTBP1V = XTOBRes['result']['bids'][0][1]
                XTBP2V = XTOBRes['result']['bids'][1][1]
                XTBP3V = XTOBRes['result']['bids'][2][1]
                XTBP4V = XTOBRes['result']['bids'][3][1]
                XTBP5V = XTOBRes['result']['bids'][4][1]
                XTAP1 = float(XTOBRes['result']['asks'][0][0])
                XTAP2 = XTOBRes['result']['asks'][1][0]
                XTAP3 = XTOBRes['result']['asks'][2][0]
                XTAP4 = XTOBRes['result']['asks'][3][0]
                XTAP5 = XTOBRes['result']['asks'][4][0]
                XTAP1V = XTOBRes['result']['asks'][0][1]
                XTAP2V = XTOBRes['result']['asks'][1][1]
                XTAP3V = XTOBRes['result']['asks'][2][1]
                XTAP4V = XTOBRes['result']['asks'][3][1]
                XTAP5V = XTOBRes['result']['asks'][4][1]
                XTLTPURL_Res = responses[41]
                XTLTPTM = int(XTLTPURL_Res['result'][0]['t'])
                XTLTPT = await convert_to_gmt5_async(XTLTPTM)
                XTLTP = XTLTPURL_Res['result'][0]['c']

        except Exception as e:
            print(f"Error processing XT order book data: {e}")
            XT_Status = 'NOT OK'

        try:
            BitflyerOBURLRes = responses[42]
            if BitflyerOBURLRes:
                BitflyerBP1 = float(BitflyerOBURLRes['bids'][0]['price'])
                BitflyerBP2 = float(BitflyerOBURLRes['bids'][1]['price'])
                BitflyerBP3 = float(BitflyerOBURLRes['bids'][2]['price'])
                BitflyerBP4 = float(BitflyerOBURLRes['bids'][3]['price'])
                BitflyerBP5 = float(BitflyerOBURLRes['bids'][4]['price'])
                BitflyerBP1V = float(BitflyerOBURLRes['bids'][0]['size'])
                BitflyerBP2V = float(BitflyerOBURLRes['bids'][1]['size'])
                BitflyerBP3V = float(BitflyerOBURLRes['bids'][2]['size'])
                BitflyerBP4V = float(BitflyerOBURLRes['bids'][3]['size'])
                BitflyerBP5V = float(BitflyerOBURLRes['bids'][4]['size'])
                BitflyerAP1 = float(BitflyerOBURLRes['asks'][0]['price'])
                BitflyerAP2 = float(BitflyerOBURLRes['asks'][1]['price'])
                BitflyerAP3 = float(BitflyerOBURLRes['asks'][2]['price'])
                BitflyerAP4 = float(BitflyerOBURLRes['asks'][3]['price'])
                BitflyerAP5 = float(BitflyerOBURLRes['asks'][4]['price'])
                BitflyerAP1V = float(BitflyerOBURLRes['asks'][0]['size'])
                BitflyerAP2V = float(BitflyerOBURLRes['asks'][1]['size'])
                BitflyerAP3V = float(BitflyerOBURLRes['asks'][2]['size'])
                BitflyerAP4V = float(BitflyerOBURLRes['asks'][3]['size'])
                BitflyerAP5V = float(BitflyerOBURLRes['asks'][4]['size'])
                BitflyerLTPURLRes = responses[43]
                BitflyerLTP = float(BitflyerLTPURLRes['ltp'])
                BitflyerLTPV = BitflyerLTPURLRes['volume']
                BitflyerLTPT = BitflyerLTPURLRes['timestamp']
        except Exception as e:
            print(f"Error processing Bitflyer order book data: {e}")
            Bitflyer_Status = 'NOT OK'
        try:
            CoinWOBRes = responses[44]
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
                CoinWAP1V = CoinWOBRes['data']['asks'][0][1]
                CoinWAP2V = CoinWOBRes['data']['asks'][1][1]
                CoinWAP3V = CoinWOBRes['data']['asks'][2][1]
                CoinWAP4V = CoinWOBRes['data']['asks'][3][1]
                CoinWAP5V = CoinWOBRes['data']['asks'][4][1]
                CoinWBP1V = CoinWOBRes['data']['bids'][0][1]
                CoinWBP2V = CoinWOBRes['data']['bids'][1][1]
                CoinWBP3V = CoinWOBRes['data']['bids'][2][1]
                CoinWBP4V = CoinWOBRes['data']['bids'][3][1]
                CoinWBP5V = CoinWOBRes['data']['bids'][4][1]
                CoinWLTPURL_Res = responses[45]
                CoinWLTP = CoinWLTPURL_Res['data']['last']
        except Exception as e:
            print(f"Error processing CoinW order book data: {e}")
            CoinW_Status = 'NOT OK'
        try:
            ToobitOBRes = responses[46]
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
                ToobitBP1V = ToobitOBRes['b'][0][1]
                ToobitBP2V = ToobitOBRes['b'][1][1]
                ToobitBP3V = ToobitOBRes['b'][2][1]
                ToobitBP4V = ToobitOBRes['b'][3][1]
                ToobitBP5V = ToobitOBRes['b'][4][1]
                ToobitAP1V = ToobitOBRes['a'][0][1]
                ToobitAP2V = ToobitOBRes['a'][1][1]
                ToobitAP3V = ToobitOBRes['a'][2][1]
                ToobitAP4V = ToobitOBRes['a'][3][1]
                ToobitAP5V = ToobitOBRes['a'][4][1]
                ToobitLTPURL_Res = responses[47]
                ToobitLTP = ToobitLTPURL_Res[0]['p']
                ToobitLTPV = ToobitLTPURL_Res[0]['q']
                ToobitLTPTm = ToobitLTPURL_Res[0]['t']
        except Exception as e:
            print(f"Error processing Toobit order book data: {e}")
            Toobit_Status = 'NOT OK'

        try:
            TapbitOBRes = responses[48]
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
                TapbitAP1V = TapbitOBRes['data']['asks'][0][1]
                TapbitAP2V = TapbitOBRes['data']['asks'][1][1]
                TapbitAP3V = TapbitOBRes['data']['asks'][2][1]
                TapbitAP4V = TapbitOBRes['data']['asks'][3][1]
                TapbitAP5V = TapbitOBRes['data']['asks'][4][1]
                TapbitBP1V = TapbitOBRes['data']['bids'][0][1]
                TapbitBP2V = TapbitOBRes['data']['bids'][1][1]
                TapbitBP3V = TapbitOBRes['data']['bids'][2][1]
                TapbitBP4V = TapbitOBRes['data']['bids'][3][1]
                TapbitBP5V = TapbitOBRes['data']['bids'][4][1]
                TapbitOBTM = TapbitOBRes['data']['timestamp']
                TapbitLTPURL_Res = responses[49]
                TapbitLTP = TapbitLTPURL_Res['data']['last_price']

        except Exception as e:
            print(f"Error processing TapBit order book data: {e}")
            TapBit_Status = 'NOT OK'


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

        bid_volumes = {
            "Binance": BinanceBP1V,
            "Bybit": BybitBP1V,
            "OKX": OKXBP1V,
            "Upbit": UpbitBP1V,
            "Kucoin": KucoinBP1V,
            "Bitget": BitgetBP1V,
            "Bitstamp": BitstampBP1V,
            "Gemini": GeminiBP1V,
            "Kraken": KrakenBPV1,
            "Gate.io": GateioBPV1,
            "HTX": HTXBP1V,
            "MEXC": MEXCBP1V,
            "Lbank": LbankBP1V,
            "Bitmart": BitmartBP1V,
            "Deepcoin": DeepcoinBP1V,
            "Bitfinex": BitfinexBP1V,
            "BingX": BingXBP1V,
            "OrangeX": OrangeXBP1V,
            "Bitvenus": BitvenusBP1V,
            "Biconomy": BiconomyBP1V,
            "XT": XTBP1V,
            "Bitflyer": BitflyerBP1V,
            "CoinW": CoinWBP1V,
            "Toobit": ToobitBP1V,
            "TapBit": TapbitBP1V
            # Continue with other exchanges...
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
        ask_volumes = {
            "Binance": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bybit": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "OKX": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Upbit": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Kucoin": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitget": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitstamp": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Gemini": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Kraken": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Gate.io": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "HTX": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "MEXC": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Lbank": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitmart": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Deepcoin": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitfinex": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "BingX": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "OrangeX": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitvenus": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Biconomy": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "XT": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Bitflyer": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "CoinW": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "Toobit": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            },
            "TapBit": {
                "Binance": BinanceAP1V,
                "Bybit": BybitAP1V,
                "OKX": OKXAP1V,
                "Upbit": UpbitAP1V,
                "Kucoin": KucoinAP1V,
                "Bitget": BitgetAP1V,
                "Bitstamp": BitstampAP1V,
                "Gemini": GeminiAP1V,
                "Kraken": KrakenAPV1,
                "Gate.io": GateioAPV1,
                "HTX": HTXAP1V,
                "MEXC": MEXCAP1V,
                "Lbank": LbankAP1V,
                "Bitmart": BitmartAP1V,
                "Deepcoin": DeepcoinAP1V,
                "Bitfinex": BitfinexAP1V,
                "BingX": BingXAP1V,
                "OrangeX": OrangeXAP1V,
                "Bitvenus": BitvenusAP1V,
                "Biconomy": BiconomyAP1V,
                "XT": XTAP1V,
                "Bitflyer": BitflyerAP1V,
                "CoinW": CoinWAP1V,
                "Toobit": ToobitAP1V,
                "TapBit": TapbitAP1V
            }
        }

    exchanges = []
    for exchange_name, bid_price in bid_prices.items():
        exchange = Exchange(exchange_name, bid_price, ask_prices[exchange_name], bid_volumes[exchange_name],
                            ask_volumes[exchange_name])
        exchange.calculate_differences()
        exchanges.append(exchange)

    # Collect only the volume-adjusted differences from all exchanges
    results = {}
    for exchange in exchanges:
        results.update(exchange.get_volume_adjusted_differences())

    # Print the volume-adjusted differences
    for key in sorted(results.keys()):
        print(f"{key}: {results[key]}")

    print(HTXBP1,HTXBP1V,HTXAP1,HTXAP1V)


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
    MEXCBP_GateioAP = results['MEXCBP_Gate.ioAP']
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

    end=time.time()
    processing_time=end-start

    data = {
            'Binance_LTP': await converting_decimalPoints(BinanceLTP),
            'BybitLTP': await converting_decimalPoints(BybitLTP),
            'OKX_LTP': await converting_decimalPoints(OKXLTP),
            'Upbit_LTP': await converting_decimalPoints(UpbitLTP),
            'Kucoin_LTP': await converting_decimalPoints(KucoinLTP),
            'Bitget_LTP': await converting_decimalPoints(BitgetLTP),
            'Bybit_LTP': await converting_decimalPoints(BybitLTP),
            'Bitstamp_LTP': await converting_decimalPoints(BitstampLTP),
            'Gemini_LTP': await converting_decimalPoints(GeminiLTP),
            'Kraken_Ltp': await converting_decimalPoints(KrakenLTP),
            'Gateio_LTP': await converting_decimalPoints(GateioLTP),
            'HTX_LTP': await converting_decimalPoints(HTXLTP),
            'MEXC_LTP': await converting_decimalPoints(MEXCLTP),
            'Lbank_LTP': await converting_decimalPoints(LbankLTP),
            'Bitmart_LTP': await converting_decimalPoints(BitmartLTP),
            'Deepcoin_LTP': await converting_decimalPoints(DeepcoinLTP),
            'Bitfinex_LTP': await converting_decimalPoints(BitfinexLTP),
            'BingX_LTP': await converting_decimalPoints(BingXLTP),
            'OrangeX_LTP': await converting_decimalPoints(OrangeXLTP),
            'Bitvenus_LTP': await converting_decimalPoints(BitvenusLTP),
            'Biconomy_LTP': await converting_decimalPoints(BiconomyLTP),
            'XT_LTP': await converting_decimalPoints(XTLTP),
            'Bitflyer_LTP': await converting_decimalPoints(BitflyerLTP),
            'CoinW_LTP': await converting_decimalPoints(CoinWLTP),
            'Toobit_LTP': await converting_decimalPoints(ToobitLTP),
            'TapBit_LTP': await converting_decimalPoints(TapbitLTP),

            'Binance_Status': Binance_Status,
            'BybitStatus': BybitStatus,
            'OKX_Status': OKX_Status,
            'Upbit_Status': Upbit_Status,
            'Kucoin_Status': Kucoin_Status,
            'Bitget_Status': Bitget_Status,
            'Bitstamp_Status': Bitstamp_Status,
            'Gemini_Status': Gemini_Status,
            'Kraken_Status': Kraken_Status,
            'Gateio_Status': Gateio_Status,
            'HTX_Status': HTX_Status,
            'MEXC_Status': MEXC_Status,
            'Lbank_Status': Lbank_Status,
            'Bitmart_Status': Bitmart_Status,
            'Deepcoin_Status': Deepcoin_Status,
            'Bitfinex_Status': Bitfinex_Status,
            'BingX_Status': BingX_Status,
            'OrangeX_Status': OrangeX_Status,
            'Bitvenus_Status': Bitvenus_Status,
            'Biconomy_Status': Biconomy_Status,
            'XT_Status': XT_Status,
            'Bitflyer_Status': Bitflyer_Status,
            'CoinW_Status': CoinW_Status,
            'Toobit_Status': Toobit_Status,
            'TapBit_Status': TapBit_Status,

            'BinanceBP_BinanceAP': await converting_decimalPoints(BinanceBP_BinanceAP),
            'BinanceBP_BybitAP': await converting_decimalPoints(BinanceBP_BybitAP),
            'BinanceBP_OKXAP': await converting_decimalPoints(BinanceBP_OKXAP),
            'BinanceBP_UpbitAP': await converting_decimalPoints(BinanceBP_UpbitAP),
            'BinanceBP_KucoinAP': await converting_decimalPoints(BinanceBP_KucoinAP),
            'BinanceBP_BitgetAP': await converting_decimalPoints(BinanceBP_BitgetAP),
            'BinanceBP_BitstampAP': await converting_decimalPoints(BinanceBP_BitstampAP),
            'BinanceBP_GeminiAP': await converting_decimalPoints(BinanceBP_GeminiAP),
            'BinanceBP_KrakenAP': await converting_decimalPoints(BinanceBP_KrakenAP),
            'BinanceBP_GateioAP': await converting_decimalPoints(BinanceBP_GateioAP),
            'BinanceBP_HTXAP': await converting_decimalPoints(BinanceBP_HTXAP),
            'BinanceBP_MEXCAP': await converting_decimalPoints(BinanceBP_MEXCAP),
            'BinanceBP_LbankAP': await converting_decimalPoints(BinanceBP_LbankAP),
            'BinanceBP_BitmartAP': await converting_decimalPoints(BinanceBP_BitmartAP),
            'BinanceBP_DeepcoinAP': await converting_decimalPoints(BinanceBP_DeepcoinAP),
            'BinanceBP_BitfinexAP': await converting_decimalPoints(BinanceBP_BitfinexAP),
            'BinanceBP_BingXAP': await converting_decimalPoints(BinanceBP_BingXAP),
            'BinanceBP_OrangeXAP': await converting_decimalPoints(BinanceBP_OrangeXAP),
            'BinanceBP_BitvenusAP': await converting_decimalPoints(BinanceBP_BitvenusAP),
            'BinanceBP_BiconomyAP': await converting_decimalPoints(BinanceBP_BiconomyAP),
            'BinanceBP_XTAP': await converting_decimalPoints(BinanceBP_XTAP),
            'BinanceBP_BitflyerAP': await converting_decimalPoints(BinanceBP_BitflyerAP),
            'BinanceBP_CoinWAP': await converting_decimalPoints(BinanceBP_CoinWAP),
            'BinanceBP_ToobitAP': await converting_decimalPoints(BinanceBP_ToobitAP),
            'BinanceBP_TapBitAP': await converting_decimalPoints(BinanceBP_TapBitAP),

            'BybitBP_BinanceAP': await converting_decimalPoints(BybitBP_BinanceAP),
            'BybitBP_BybitAP': await converting_decimalPoints(BybitBP_BybitAP),
            'BybitBP_OKXAP': await converting_decimalPoints(BybitBP_OKXAP),
            'BybitBP_UpbitAP': await converting_decimalPoints(BybitBP_UpbitAP),
            'BybitBP_KucoinAP': await converting_decimalPoints(BybitBP_KucoinAP),
            'BybitBP_BitgetAP': await converting_decimalPoints(BybitBP_BitgetAP),
            'BybitBP_BitstampAP': await converting_decimalPoints(BybitBP_BitstampAP),
            'BybitBP_GeminiAP': await converting_decimalPoints(BybitBP_GeminiAP),
            'BybitBP_KrakenAP': await converting_decimalPoints(BybitBP_KrakenAP),
            'BybitBP_GateioAP': await converting_decimalPoints(BybitBP_GateioAP),
            'BybitBP_HTXAP': await converting_decimalPoints(BybitBP_HTXAP),
            'BybitBP_MEXCAP': await converting_decimalPoints(BybitBP_MEXCAP),
            'BybitBP_LbankAP': await converting_decimalPoints(BybitBP_LbankAP),
            'BybitBP_BitmartAP': await converting_decimalPoints(BybitBP_BitmartAP),
            'BybitBP_DeepcoinAP': await converting_decimalPoints(BybitBP_DeepcoinAP),
            'BybitBP_BitfinexAP': await converting_decimalPoints(BybitBP_BitfinexAP),
            'BybitBP_BingXAP': await converting_decimalPoints(BybitBP_BingXAP),
            'BybitBP_OrangeXAP': await converting_decimalPoints(BybitBP_OrangeXAP),
            'BybitBP_BitvenusAP': await converting_decimalPoints(BybitBP_BitvenusAP),
            'BybitBP_BiconomyAP': await converting_decimalPoints(BybitBP_BiconomyAP),
            'BybitBP_XTAP': await converting_decimalPoints(BybitBP_XTAP),
            'BybitBP_BitflyerAP': await converting_decimalPoints(BybitBP_BitflyerAP),
            'BybitBP_CoinWAP': await converting_decimalPoints(BybitBP_CoinWAP),
            'BybitBP_ToobitAP': await converting_decimalPoints(BybitBP_ToobitAP),
            'BybitBP_TapBitAP': await converting_decimalPoints(BybitBP_TapBitAP),

            'OKXBP_BinanceAP': await converting_decimalPoints(OKXBP_BinanceAP),
            'OKXBP_BybitAP': await converting_decimalPoints(OKXBP_BybitAP),
            'OKXBP_OKXAP': await converting_decimalPoints(OKXBP_OKXAP),
            'OKXBP_UpbitAP': await converting_decimalPoints(OKXBP_UpbitAP),
            'OKXBP_KucoinAP': await converting_decimalPoints(OKXBP_KucoinAP),
            'OKXBP_BitgetAP': await converting_decimalPoints(OKXBP_BitgetAP),
            'OKXBP_BitstampAP': await converting_decimalPoints(OKXBP_BitstampAP),
            'OKXBP_GeminiAP': await converting_decimalPoints(OKXBP_GeminiAP),
            'OKXBP_KrakenAP': await converting_decimalPoints(OKXBP_KrakenAP),
            'OKXBP_GateioAP': await converting_decimalPoints(OKXBP_GateioAP),
            'OKXBP_HTXAP': await converting_decimalPoints(OKXBP_HTXAP),
            'OKXBP_MEXCAP': await converting_decimalPoints(OKXBP_MEXCAP),
            'OKXBP_LbankAP': await converting_decimalPoints(OKXBP_LbankAP),
            'OKXBP_BitmartAP': await converting_decimalPoints(OKXBP_BitmartAP),
            'OKXBP_DeepcoinAP': await converting_decimalPoints(OKXBP_DeepcoinAP),
            'OKXBP_BitfinexAP': await converting_decimalPoints(OKXBP_BitfinexAP),
            'OKXBP_BingXAP': await converting_decimalPoints(OKXBP_BingXAP),
            'OKXBP_OrangeXAP': await converting_decimalPoints(OKXBP_OrangeXAP),
            'OKXBP_BitvenusAP': await converting_decimalPoints(OKXBP_BitvenusAP),
            'OKXBP_BiconomyAP': await converting_decimalPoints(OKXBP_BiconomyAP),
            'OKXBP_XTAP': await converting_decimalPoints(OKXBP_XTAP),
            'OKXBP_BitflyerAP': await converting_decimalPoints(OKXBP_BitflyerAP),
            'OKXBP_CoinWAP': await converting_decimalPoints(OKXBP_CoinWAP),
            'OKXBP_ToobitAP': await converting_decimalPoints(OKXBP_ToobitAP),
            'OKXBP_TapBitAP': await converting_decimalPoints(OKXBP_TapBitAP),

            'UpbitBP_BinanceAP': await converting_decimalPoints(UpbitBP_BinanceAP),
            'UpbitBP_BybitAP': await converting_decimalPoints(UpbitBP_BybitAP),
            'UpbitBP_OKXAP': await converting_decimalPoints(UpbitBP_OKXAP),
            'UpbitBP_UpbitAP': await converting_decimalPoints(UpbitBP_UpbitAP),
            'UpbitBP_KucoinAP': await converting_decimalPoints(UpbitBP_KucoinAP),
            'UpbitBP_BitgetAP': await converting_decimalPoints(UpbitBP_BitgetAP),
            'UpbitBP_BitstampAP': await converting_decimalPoints(UpbitBP_BitstampAP),
            'UpbitBP_GeminiAP': await converting_decimalPoints(UpbitBP_GeminiAP),
            'UpbitBP_KrakenAP': await converting_decimalPoints(UpbitBP_KrakenAP),
            'UpbitBP_GateioAP': await converting_decimalPoints(UpbitBP_GateioAP),
            'UpbitBP_HTXAP': await converting_decimalPoints(UpbitBP_HTXAP),
            'UpbitBP_MEXCAP': await converting_decimalPoints(UpbitBP_MEXCAP),
            'UpbitBP_LbankAP': await converting_decimalPoints(UpbitBP_LbankAP),
            'UpbitBP_BitmartAP': await converting_decimalPoints(UpbitBP_BitmartAP),
            'UpbitBP_DeepcoinAP': await converting_decimalPoints(UpbitBP_DeepcoinAP),
            'UpbitBP_BitfinexAP': await converting_decimalPoints(UpbitBP_BitfinexAP),
            'UpbitBP_BingXAP': await converting_decimalPoints(UpbitBP_BingXAP),
            'UpbitBP_OrangeXAP': await converting_decimalPoints(UpbitBP_OrangeXAP),
            'UpbitBP_BitvenusAP': await converting_decimalPoints(UpbitBP_BitvenusAP),
            'UpbitBP_BiconomyAP': await converting_decimalPoints(UpbitBP_BiconomyAP),
            'UpbitBP_XTAP': await converting_decimalPoints(UpbitBP_XTAP),
            'UpbitBP_BitflyerAP': await converting_decimalPoints(UpbitBP_BitflyerAP),
            'UpbitBP_CoinWAP': await converting_decimalPoints(UpbitBP_CoinWAP),
            'UpbitBP_ToobitAP': await converting_decimalPoints(UpbitBP_ToobitAP),
            'UpbitBP_TapBitAP': await converting_decimalPoints(UpbitBP_TapBitAP),

            'KucoinBP_BinanceAP': await  converting_decimalPoints(KucoinBP_BinanceAP),
            'KucoinBP_BybitAP': await  converting_decimalPoints(KucoinBP_BybitAP),
            'KucoinBP_OKXAP': await  converting_decimalPoints(KucoinBP_OKXAP),
            'KucoinBP_UpbitAP': await  converting_decimalPoints(KucoinBP_UpbitAP),
            'KucoinBP_KucoinAP': await  converting_decimalPoints(KucoinBP_KucoinAP),
            'KucoinBP_BitgetAP': await  converting_decimalPoints(KucoinBP_BitgetAP),
            'KucoinBP_BitstampAP': await  converting_decimalPoints(KucoinBP_BitstampAP),
            'KucoinBP_GeminiAP': await  converting_decimalPoints(KucoinBP_GeminiAP),
            'KucoinBP_KrakenAP': await  converting_decimalPoints(KucoinBP_KrakenAP),
            'KucoinBP_GateioAP': await  converting_decimalPoints(KucoinBP_GateioAP),
            'KucoinBP_HTXAP': await  converting_decimalPoints(KucoinBP_HTXAP),
            'KucoinBP_MEXCAP': await  converting_decimalPoints(KucoinBP_MEXCAP),
            'KucoinBP_LbankAP': await  converting_decimalPoints(KucoinBP_LbankAP),
            'KucoinBP_BitmartAP': await  converting_decimalPoints(KucoinBP_BitmartAP),
            'KucoinBP_DeepcoinAP': await  converting_decimalPoints(KucoinBP_DeepcoinAP),
            'KucoinBP_BitfinexAP': await  converting_decimalPoints(KucoinBP_BitfinexAP),
            'KucoinBP_BingXAP': await  converting_decimalPoints(KucoinBP_BingXAP),
            'KucoinBP_OrangeXAP': await  converting_decimalPoints(KucoinBP_OrangeXAP),
            'KucoinBP_BitvenusAP': await  converting_decimalPoints(KucoinBP_BitvenusAP),
            'KucoinBP_BiconomyAP': await  converting_decimalPoints(KucoinBP_BiconomyAP),
            'KucoinBP_XTAP': await  converting_decimalPoints(KucoinBP_XTAP),
            'KucoinBP_BitflyerAP': await  converting_decimalPoints(KucoinBP_BitflyerAP),
            'KucoinBP_CoinWAP': await  converting_decimalPoints(KucoinBP_CoinWAP),
            'KucoinBP_ToobitAP': await  converting_decimalPoints(KucoinBP_ToobitAP),
            'KucoinBP_TapBitAP': await  converting_decimalPoints(KucoinBP_TapBitAP),

            'BitgetBP_BinanceAP': await converting_decimalPoints(BitgetBP_BinanceAP),
            'BitgetBP_BybitAP': await converting_decimalPoints(BitgetBP_BybitAP),
            'BitgetBP_OKXAP': await converting_decimalPoints(BitgetBP_OKXAP),
            'BitgetBP_UpbitAP': await converting_decimalPoints(BitgetBP_UpbitAP),
            'BitgetBP_KucoinAP': await converting_decimalPoints(BitgetBP_KucoinAP),
            'BitgetBP_BitgetAP': await converting_decimalPoints(BitgetBP_BitgetAP),
            'BitgetBP_BitstampAP': await converting_decimalPoints(BitgetBP_BitstampAP),
            'BitgetBP_GeminiAP': await converting_decimalPoints(BitgetBP_GeminiAP),
            'BitgetBP_KrakenAP': await converting_decimalPoints(BitgetBP_KrakenAP),
            'BitgetBP_GateioAP': await converting_decimalPoints(BitgetBP_GateioAP),
            'BitgetBP_HTXAP': await converting_decimalPoints(BitgetBP_HTXAP),
            'BitgetBP_MEXCAP': await converting_decimalPoints(BitgetBP_MEXCAP),
            'BitgetBP_LbankAP': await converting_decimalPoints(BitgetBP_LbankAP),
            'BitgetBP_BitmartAP': await converting_decimalPoints(BitgetBP_BitmartAP),
            'BitgetBP_DeepcoinAP': await converting_decimalPoints(BitgetBP_DeepcoinAP),
            'BitgetBP_BitfinexAP': await converting_decimalPoints(BitgetBP_BitfinexAP),
            'BitgetBP_BingXAP': await converting_decimalPoints(BitgetBP_BingXAP),
            'BitgetBP_OrangeXAP': await converting_decimalPoints(BitgetBP_OrangeXAP),
            'BitgetBP_BitvenusAP': await converting_decimalPoints(BitgetBP_BitvenusAP),
            'BitgetBP_BiconomyAP': await converting_decimalPoints(BitgetBP_BiconomyAP),
            'BitgetBP_XTAP': await converting_decimalPoints(BitgetBP_XTAP),
            'BitgetBP_BitflyerAP': await converting_decimalPoints(BitgetBP_BitflyerAP),
            'BitgetBP_CoinWAP': await converting_decimalPoints(BitgetBP_CoinWAP),
            'BitgetBP_ToobitAP': await converting_decimalPoints(BitgetBP_ToobitAP),
            'BitgetBP_TapBitAP': await converting_decimalPoints(BitgetBP_TapBitAP),

            'BitstampBP_BinanceAP': await converting_decimalPoints(BitstampBP_BinanceAP),
            'BitstampBP_BybitAP': await converting_decimalPoints(BitstampBP_BybitAP),
            'BitstampBP_OKXAP': await converting_decimalPoints(BitstampBP_OKXAP),
            'BitstampBP_UpbitAP': await converting_decimalPoints(BitstampBP_UpbitAP),
            'BitstampBP_KucoinAP': await converting_decimalPoints(BitstampBP_KucoinAP),
            'BitstampBP_BitgetAP': await converting_decimalPoints(BitstampBP_BitgetAP),
            'BitstampBP_BitstampAP': await converting_decimalPoints(BitstampBP_BitstampAP),
            'BitstampBP_GeminiAP': await converting_decimalPoints(BitstampBP_GeminiAP),
            'BitstampBP_KrakenAP': await converting_decimalPoints(BitstampBP_KrakenAP),
            'BitstampBP_GateioAP': await converting_decimalPoints(BitstampBP_GateioAP),
            'BitstampBP_HTXAP': await converting_decimalPoints(BitstampBP_HTXAP),
            'BitstampBP_MEXCAP': await converting_decimalPoints(BitstampBP_MEXCAP),
            'BitstampBP_LbankAP': await converting_decimalPoints(BitstampBP_LbankAP),
            'BitstampBP_BitmartAP': await converting_decimalPoints(BitstampBP_BitmartAP),
            'BitstampBP_DeepcoinAP': await converting_decimalPoints(BitstampBP_DeepcoinAP),
            'BitstampBP_BitfinexAP': await converting_decimalPoints(BitstampBP_BitfinexAP),
            'BitstampBP_BingXAP': await converting_decimalPoints(BitstampBP_BingXAP),
            'BitstampBP_OrangeXAP': await converting_decimalPoints(BitstampBP_OrangeXAP),
            'BitstampBP_BitvenusAP': await converting_decimalPoints(BitstampBP_BitvenusAP),
            'BitstampBP_BiconomyAP': await converting_decimalPoints(BitstampBP_BitvenusAP),
            'BitstampBP_XTAP': await converting_decimalPoints(BitstampBP_XTAP),
            'BitstampBP_BitflyerAP': await converting_decimalPoints(BitstampBP_BitflyerAP),
            'BitstampBP_CoinWAP': await converting_decimalPoints(BitstampBP_CoinWAP),
            'BitstampBP_ToobitAP': await converting_decimalPoints(BitstampBP_ToobitAP),
            'BitstampBP_TapBitAP': await converting_decimalPoints(BitstampBP_TapBitAP),

            'GeminiBP_BinanceAP': await converting_decimalPoints(GeminiBP_BinanceAP),
            'GeminiBP_BybitAP': await converting_decimalPoints(GeminiBP_BybitAP),
            'GeminiBP_OKXAP': await converting_decimalPoints(GeminiBP_OKXAP),
            'GeminiBP_UpbitAP': await converting_decimalPoints(GeminiBP_UpbitAP),
            'GeminiBP_KucoinAP': await converting_decimalPoints(GeminiBP_KucoinAP),
            'GeminiBP_BitgetAP': await converting_decimalPoints(GeminiBP_BitgetAP),
            'GeminiBP_BitstampAP': await converting_decimalPoints(GeminiBP_BitstampAP),
            'GeminiBP_GeminiAP': await converting_decimalPoints(GeminiBP_GeminiAP),
            'GeminiBP_KrakenAP': await converting_decimalPoints(GeminiBP_KrakenAP),
            'GeminiBP_GateioAP': await converting_decimalPoints(GeminiBP_GateioAP),
            'GeminiBP_HTXAP': await converting_decimalPoints(GeminiBP_HTXAP),
            'GeminiBP_MEXCAP': await converting_decimalPoints(GeminiBP_MEXCAP),
            'GeminiBP_LbankAP': await converting_decimalPoints(GeminiBP_LbankAP),
            'GeminiBP_BitmartAP': await converting_decimalPoints(GeminiBP_BitmartAP),
            'GeminiBP_DeepcoinAP': await converting_decimalPoints(GeminiBP_DeepcoinAP),
            'GeminiBP_BitfinexAP': await converting_decimalPoints(GeminiBP_BitfinexAP),
            'GeminiBP_BingXAP': await converting_decimalPoints(GeminiBP_BingXAP),
            'GeminiBP_OrangeXAP': await converting_decimalPoints(GeminiBP_OrangeXAP),
            'GeminiBP_BitvenusAP': await converting_decimalPoints(GeminiBP_BitvenusAP),
            'GeminiBP_BiconomyAP': await converting_decimalPoints(GeminiBP_BiconomyAP),
            'GeminiBP_XTAP': await converting_decimalPoints(GeminiBP_XTAP),
            'GeminiBP_BitflyerAP': await converting_decimalPoints(GeminiBP_BitflyerAP),
            'GeminiBP_CoinWAP': await converting_decimalPoints(GeminiBP_CoinWAP),
            'GeminiBP_ToobitAP': await converting_decimalPoints(GeminiBP_ToobitAP),
            'GeminiBP_TapBitAP': await converting_decimalPoints(GeminiBP_TapBitAP),

            'KrakenBP_BinanceAP': await converting_decimalPoints(KrakenBP_BinanceAP),
            'KrakenBP_BybitAP': await converting_decimalPoints(KrakenBP_BybitAP),
            'KrakenBP_OKXAP': await converting_decimalPoints(KrakenBP_OKXAP),
            'KrakenBP_UpbitAP': await converting_decimalPoints(KrakenBP_UpbitAP),
            'KrakenBP_KucoinAP': await converting_decimalPoints(KrakenBP_KucoinAP),
            'KrakenBP_BitgetAP': await converting_decimalPoints(KrakenBP_BitgetAP),
            'KrakenBP_BitstampAP': await converting_decimalPoints(KrakenBP_BitstampAP),
            'KrakenBP_GeminiAP': await converting_decimalPoints(KrakenBP_GeminiAP),
            'KrakenBP_KrakenAP': await converting_decimalPoints(KrakenBP_KrakenAP),
            'KrakenBP_GateioAP': await converting_decimalPoints(KrakenBP_GateioAP),
            'KrakenBP_HTXAP': await converting_decimalPoints(KrakenBP_HTXAP),
            'KrakenBP_MEXCAP': await converting_decimalPoints(KrakenBP_MEXCAP),
            'KrakenBP_LbankAP': await converting_decimalPoints(KrakenBP_LbankAP),
            'KrakenBP_BitmartAP': await converting_decimalPoints(KrakenBP_BitmartAP),
            'KrakenBP_DeepcoinAP': await converting_decimalPoints(KrakenBP_DeepcoinAP),
            'KrakenBP_BitfinexAP': await converting_decimalPoints(KrakenBP_BitfinexAP),
            'KrakenBP_BingXAP': await converting_decimalPoints(KrakenBP_BingXAP),
            'KrakenBP_OrangeXAP': await converting_decimalPoints(KrakenBP_OrangeXAP),
            'KrakenBP_BitvenusAP': await converting_decimalPoints(KrakenBP_BitvenusAP),
            'KrakenBP_BiconomyAP': await converting_decimalPoints(KrakenBP_BiconomyAP),
            'KrakenBP_XTAP': await converting_decimalPoints(KrakenBP_XTAP),
            'KrakenBP_BitflyerAP': await converting_decimalPoints(KrakenBP_BitflyerAP),
            'KrakenBP_CoinWAP': await converting_decimalPoints(KrakenBP_CoinWAP),
            'KrakenBP_ToobitAP': await converting_decimalPoints(KrakenBP_ToobitAP),
            'KrakenBP_TapBitAP': await converting_decimalPoints(KrakenBP_TapBitAP),

            'GateiotBP_BinanceAP': await converting_decimalPoints(GateioBP_BinanceAP),
            'GateiotBP_BybitAP': await converting_decimalPoints(GateioBP_BybitAP),
            'GateiotBP_OKXAP': await converting_decimalPoints(GateioBP_OKXAP),
            'GateiotBP_UpbitAP': await converting_decimalPoints(GateioBP_UpbitAP),
            'GateiotBP_KucoinAP': await converting_decimalPoints(GateioBP_KucoinAP),
            'GateiotBP_BitgetAP': await converting_decimalPoints(GateioBP_BitgetAP),
            'GateiotBP_BitstampAP': await converting_decimalPoints(GateioBP_BitstampAP),
            'GateiotBP_GeminiAP': await converting_decimalPoints(GateioBP_GeminiAP),
            'GateiotBP_KrakenAP': await converting_decimalPoints(GateioBP_KrakenAP),
            'GateiotBP_GateioAP': await converting_decimalPoints(GateioBP_GateioAP),
            'GateiotBP_HTXAP': await converting_decimalPoints(GateioBP_HTXAP),
            'GateiotBP_MEXCAP': await converting_decimalPoints(GateioBP_MEXCAP),
            'GateiotBP_LbankAP': await converting_decimalPoints(GateioBP_LbankAP),
            'GateiotBP_BitmartAP': await converting_decimalPoints(GateioBP_BitmartAP),
            'GateiotBP_DeepcoinAP': await converting_decimalPoints(GateioBP_DeepcoinAP),
            'GateiotBP_BitfinexAP': await converting_decimalPoints(GateioBP_BitfinexAP),
            'GateiotBP_BingXAP': await converting_decimalPoints(GateioBP_BingXAP),
            'GateiotBP_OrangeXAP': await converting_decimalPoints(GateioBP_OrangeXAP),
            'GateiotBP_BitvenusAP': await converting_decimalPoints(GateioBP_BitvenusAP),
            'GateiotBP_BiconomyAP': await converting_decimalPoints(GateioBP_BiconomyAP),
            'GateiotBP_XTAP': await converting_decimalPoints(GateioBP_XTAP),
            'GateiotBP_BitflyerAP': await converting_decimalPoints(GateioBP_BitflyerAP),
            'GateiotBP_CoinWAP': await converting_decimalPoints(GateioBP_CoinWAP),
            'GateiotBP_ToobitAP': await converting_decimalPoints(GateioBP_ToobitAP),
            'GateiotBP_TapBitAP': await converting_decimalPoints(GateioBP_TapBitAP),

            'HTXBP_BinanceAP': await converting_decimalPoints(HTXBP_BinanceAP),
            'HTXBP_BybitAP': await converting_decimalPoints(HTXBP_BybitAP),
            'HTXBP_OKXAP': await converting_decimalPoints(HTXBP_OKXAP),
            'HTXBP_UpbitAP': await converting_decimalPoints(HTXBP_UpbitAP),
            'HTXBP_KucoinAP': await converting_decimalPoints(HTXBP_KucoinAP),
            'HTXBP_BitgetAP': await converting_decimalPoints(HTXBP_BitgetAP),
            'HTXBP_BitstampAP': await converting_decimalPoints(HTXBP_BitstampAP),
            'HTXBP_GeminiAP': await converting_decimalPoints(HTXBP_GeminiAP),
            'HTXBP_KrakenAP': await converting_decimalPoints(HTXBP_KrakenAP),
            'HTXBP_GateioAP': await converting_decimalPoints(HTXBP_GateioAP),
            'HTXBP_HTXAP': await converting_decimalPoints(HTXBP_HTXAP),
            'HTXBP_MEXCAP': await converting_decimalPoints(HTXBP_MEXCAP),
            'HTXBP_LbankAP': await converting_decimalPoints(HTXBP_LbankAP),
            'HTXBP_BitmartAP': await converting_decimalPoints(HTXBP_BitmartAP),
            'HTXBP_DeepcoinAP': await converting_decimalPoints(HTXBP_DeepcoinAP),
            'HTXBP_BitfinexAP': await converting_decimalPoints(HTXBP_BitfinexAP),
            'HTXBP_BingXAP': await converting_decimalPoints(HTXBP_BingXAP),
            'HTXBP_OrangeXAP': await converting_decimalPoints(HTXBP_OrangeXAP),
            'HTXBP_BitvenusAP': await converting_decimalPoints(HTXBP_BitvenusAP),
            'HTXBP_BiconomyAP': await converting_decimalPoints(HTXBP_BiconomyAP),
            'HTXBP_XTAP': await converting_decimalPoints(HTXBP_XTAP),
            'HTXBP_BitflyerAP': await converting_decimalPoints(HTXBP_BitflyerAP),
            'HTXBP_CoinWAP': await converting_decimalPoints(HTXBP_CoinWAP),
            'HTXBP_ToobitAP': await converting_decimalPoints(HTXBP_ToobitAP),
            'HTXBP_TapBitAP': await converting_decimalPoints(HTXBP_TapBitAP),

            'MEXCBP_BinanceAP': await converting_decimalPoints(MEXCBP_BinanceAP),
            'MEXCBP_BybitAP': await converting_decimalPoints(MEXCBP_BybitAP),
            'MEXCBP_OKXAP': await converting_decimalPoints(MEXCBP_OKXAP),
            'MEXCBP_UpbitAP': await converting_decimalPoints(MEXCBP_UpbitAP),
            'MEXCBP_KucoinAP': await converting_decimalPoints(MEXCBP_KucoinAP),
            'MEXCBP_BitgetAP': await converting_decimalPoints(MEXCBP_BitgetAP),
            'MEXCBP_BitstampAP': await converting_decimalPoints(MEXCBP_BitstampAP),
            'MEXCBP_GeminiAP': await converting_decimalPoints(MEXCBP_GeminiAP),
            'MEXCBP_KrakenAP': await converting_decimalPoints(MEXCBP_KrakenAP),
            'MEXCBP_GateioAP': await converting_decimalPoints(MEXCBP_GateioAP),
            'MEXCBP_HTXAP': await converting_decimalPoints(MEXCBP_HTXAP),
            'MEXCBP_MEXCAP': await converting_decimalPoints(MEXCBP_MEXCAP),
            'MEXCBP_LbankAP': await converting_decimalPoints(MEXCBP_LbankAP),
            'MEXCBP_BitmartAP': await converting_decimalPoints(MEXCBP_BitmartAP),
            'MEXCBP_DeepcoinAP': await converting_decimalPoints(MEXCBP_DeepcoinAP),
            'MEXCBP_BitfinexAP': await converting_decimalPoints(MEXCBP_BitfinexAP),
            'MEXCBP_BingXAP': await converting_decimalPoints(MEXCBP_BingXAP),
            'MEXCBP_OrangeXAP': await converting_decimalPoints(MEXCBP_OrangeXAP),
            'MEXCBP_BitvenusAP': await converting_decimalPoints(MEXCBP_BitvenusAP),
            'MEXCBP_BiconomyAP': await converting_decimalPoints(MEXCBP_BiconomyAP),
            'MEXCBP_XTAP': await converting_decimalPoints(MEXCBP_XTAP),
            'MEXCBP_BitflyerAP': await converting_decimalPoints(MEXCBP_BitflyerAP),
            'MEXCBP_CoinWAP': await converting_decimalPoints(MEXCBP_CoinWAP),
            'MEXCBP_ToobitAP': await converting_decimalPoints(MEXCBP_ToobitAP),
            'MEXCBP_TapBitAP': await converting_decimalPoints(MEXCBP_TapBitAP),

            'LbankBP_BinanceAP': await converting_decimalPoints(LbankBP_BinanceAP),
            'LbankBP_BybitAP': await converting_decimalPoints(LbankBP_BybitAP),
            'LbankBP_OKXAP': await converting_decimalPoints(LbankBP_OKXAP),
            'LbankBP_UpbitAP': await converting_decimalPoints(LbankBP_UpbitAP),
            'LbankBP_KucoinAP': await converting_decimalPoints(LbankBP_KucoinAP),
            'LbankBP_BitgetAP': await converting_decimalPoints(LbankBP_BitgetAP),
            'LbankBP_BitstampAP': await converting_decimalPoints(LbankBP_BitstampAP),
            'LbankBP_GeminiAP': await converting_decimalPoints(LbankBP_GeminiAP),
            'LbankBP_KrakenAP': await converting_decimalPoints(LbankBP_KrakenAP),
            'LbankBP_GateioAP': await converting_decimalPoints(LbankBP_GateioAP),
            'LbankBP_HTXAP': await converting_decimalPoints(LbankBP_HTXAP),
            'LbankBP_MEXCAP': await converting_decimalPoints(LbankBP_MEXCAP),
            'LbankBP_LbankAP': await converting_decimalPoints(LbankBP_LbankAP),
            'LbankBP_BitmartAP': await converting_decimalPoints(LbankBP_BitmartAP),
            'LbankBP_DeepcoinAP': await converting_decimalPoints(LbankBP_DeepcoinAP),
            'LbankBP_BitfinexAP': await converting_decimalPoints(LbankBP_BitfinexAP),
            'LbankBP_BingXAP': await converting_decimalPoints(LbankBP_BingXAP),
            'LbankBP_OrangeXAP': await converting_decimalPoints(LbankBP_OrangeXAP),
            'LbankBP_BitvenusAP': await converting_decimalPoints(LbankBP_BitvenusAP),
            'LbankBP_BiconomyAP': await converting_decimalPoints(LbankBP_BiconomyAP),
            'LbankBP_XTAP': await converting_decimalPoints(LbankBP_XTAP),
            'LbankBP_BitflyerAP': await converting_decimalPoints(LbankBP_BitflyerAP),
            'LbankBP_CoinWAP': await converting_decimalPoints(LbankBP_CoinWAP),
            'LbankBP_ToobitAP': await converting_decimalPoints(LbankBP_ToobitAP),
            'LbankBP_TapBitAP': await converting_decimalPoints(LbankBP_TapBitAP),

            'BitmartBP_BinanceAP': await converting_decimalPoints(BitmartBP_BinanceAP),
            'BitmartBP_BybitAP': await converting_decimalPoints(BitmartBP_BybitAP),
            'BitmartBP_OKXAP': await converting_decimalPoints(BitmartBP_OKXAP),
            'BitmartBP_UpbitAP': await converting_decimalPoints(BitmartBP_UpbitAP),
            'BitmartBP_KucoinAP': await converting_decimalPoints(BitmartBP_KucoinAP),
            'BitmartBP_BitgetAP': await converting_decimalPoints(BitmartBP_BitgetAP),
            'BitmartBP_BitstampAP': await converting_decimalPoints(BitmartBP_BitstampAP),
            'BitmartBP_GeminiAP': await converting_decimalPoints(BitmartBP_GeminiAP),
            'BitmartBP_KrakenAP': await converting_decimalPoints(BitmartBP_KrakenAP),
            'BitmartBP_GateioAP': await converting_decimalPoints(BitmartBP_GateioAP),
            'BitmartBP_HTXAP': await converting_decimalPoints(BitmartBP_HTXAP),
            'BitmartBP_MEXCAP': await converting_decimalPoints(BitmartBP_MEXCAP),
            'BitmartBP_LbankAP': await converting_decimalPoints(BitmartBP_LbankAP),
            'BitmartBP_BitmartAP': await converting_decimalPoints(BitmartBP_BitmartAP),
            'BitmartBP_DeepcoinAP': await converting_decimalPoints(BitmartBP_DeepcoinAP),
            'BitmartBP_BitfinexAP': await converting_decimalPoints(BitmartBP_BitfinexAP),
            'BitmartBP_BingXAP': await converting_decimalPoints(BitmartBP_BingXAP),
            'BitmartBP_OrangeXAP': await converting_decimalPoints(BitmartBP_OrangeXAP),
            'BitmartBP_BitvenusAP': await converting_decimalPoints(BitmartBP_BitvenusAP),
            'BitmartBP_BiconomyAP': await converting_decimalPoints(BitmartBP_BiconomyAP),
            'BitmartBP_XTAP': await converting_decimalPoints(BitmartBP_XTAP),
            'BitmartBP_BitflyerAP': await converting_decimalPoints(BitmartBP_BitflyerAP),
            'BitmartBP_CoinWAP': await converting_decimalPoints(BitmartBP_CoinWAP),
            'BitmartBP_ToobitAP': await converting_decimalPoints(BitmartBP_ToobitAP),
            'BitmartBP_TapBitAP': await converting_decimalPoints(BitmartBP_TapBitAP),

            'DeepcoinBP_BinanceAP': await converting_decimalPoints(DeepcoinBP_BinanceAP),
            'DeepcoinBP_BybitAP': await converting_decimalPoints(DeepcoinBP_BybitAP),
            'DeepcoinBP_OKXAP': await converting_decimalPoints(DeepcoinBP_OKXAP),
            'DeepcoinBP_UpbitAP': await converting_decimalPoints(DeepcoinBP_UpbitAP),
            'DeepcoinBP_KucoinAP': await converting_decimalPoints(DeepcoinBP_KucoinAP),
            'DeepcoinBP_BitgetAP': await converting_decimalPoints(DeepcoinBP_BitgetAP),
            'DeepcoinBP_BitstampAP': await converting_decimalPoints(DeepcoinBP_BitstampAP),
            'DeepcoinBP_GeminiAP': await converting_decimalPoints(DeepcoinBP_GeminiAP),
            'DeepcoinBP_KrakenAP': await converting_decimalPoints(DeepcoinBP_KrakenAP),
            'DeepcoinBP_GateioAP': await converting_decimalPoints(DeepcoinBP_GateioAP),
            'DeepcoinBP_HTXAP': await converting_decimalPoints(DeepcoinBP_HTXAP),
            'DeepcoinBP_MEXCAP': await converting_decimalPoints(DeepcoinBP_MEXCAP),
            'DeepcoinBP_LbankAP': await converting_decimalPoints(DeepcoinBP_LbankAP),
            'DeepcoinBP_BitmartAP': await converting_decimalPoints(DeepcoinBP_BitmartAP),
            'DeepcoinBP_DeepcoinAP': await converting_decimalPoints(DeepcoinBP_DeepcoinAP),
            'DeepcoinBP_BitfinexAP': await converting_decimalPoints(DeepcoinBP_BitfinexAP),
            'DeepcoinBP_BingXAP': await converting_decimalPoints(DeepcoinBP_BingXAP),
            'DeepcoinBP_OrangeXAP': await converting_decimalPoints(DeepcoinBP_OrangeXAP),
            'DeepcoinBP_BitvenusAP': await converting_decimalPoints(DeepcoinBP_BitvenusAP),
            'DeepcoinBP_BiconomyAP': await converting_decimalPoints(DeepcoinBP_BiconomyAP),
            'DeepcoinBP_XTAP': await converting_decimalPoints(DeepcoinBP_XTAP),
            'DeepcoinBP_BitflyerAP': await converting_decimalPoints(DeepcoinBP_BitflyerAP),
            'DeepcoinBP_CoinWAP': await converting_decimalPoints(DeepcoinBP_CoinWAP),
            'DeepcoinBP_ToobitAP': await converting_decimalPoints(DeepcoinBP_ToobitAP),
            'DeepcoinBP_TapBitAP': await converting_decimalPoints(DeepcoinBP_TapBitAP),

            'BitfinexBP_BinanceAP': await converting_decimalPoints(BitfinexBP_BinanceAP),
            'BitfinexBP_BybitAP': await converting_decimalPoints(BitfinexBP_BybitAP),
            'BitfinexBP_OKXAP': await converting_decimalPoints(BitfinexBP_OKXAP),
            'BitfinexBP_UpbitAP': await converting_decimalPoints(BitfinexBP_UpbitAP),
            'BitfinexBP_KucoinAP': await converting_decimalPoints(BitfinexBP_KucoinAP),
            'BitfinexBP_BitgetAP': await converting_decimalPoints(BitfinexBP_BitgetAP),
            'BitfinexBP_BitstampAP': await converting_decimalPoints(BitfinexBP_BitstampAP),
            'BitfinexBP_GeminiAP': await converting_decimalPoints(BitfinexBP_GeminiAP),
            'BitfinexBP_KrakenAP': await converting_decimalPoints(BitfinexBP_KrakenAP),
            'BitfinexBP_GateioAP': await converting_decimalPoints(BitfinexBP_GateioAP),
            'BitfinexBP_HTXAP': await converting_decimalPoints(BitfinexBP_HTXAP),
            'BitfinexBP_MEXCAP': await converting_decimalPoints(BitfinexBP_MEXCAP),
            'BitfinexBP_LbankAP': await converting_decimalPoints(BitfinexBP_LbankAP),
            'BitfinexBP_BitmartAP': await converting_decimalPoints(BitfinexBP_BitmartAP),
            'BitfinexBP_DeepcoinAP': await converting_decimalPoints(BitfinexBP_DeepcoinAP),
            'BitfinexBP_BitfinexAP': await converting_decimalPoints(BitfinexBP_BitfinexAP),
            'BitfinexBP_BingXAP': await converting_decimalPoints(BitfinexBP_BingXAP),
            'BitfinexBP_OrangeXAP': await converting_decimalPoints(BitfinexBP_OrangeXAP),
            'BitfinexBP_BitvenusAP': await converting_decimalPoints(BitfinexBP_BitvenusAP),
            'BitfinexBP_BiconomyAP': await converting_decimalPoints(BitfinexBP_BiconomyAP),
            'BitfinexBP_XTAP': await converting_decimalPoints(BitfinexBP_XTAP),
            'BitfinexBP_BitflyerAP': await converting_decimalPoints(BitfinexBP_BitflyerAP),
            'BitfinexBP_CoinWAP': await converting_decimalPoints(BitfinexBP_CoinWAP),
            'BitfinexBP_ToobitAP': await converting_decimalPoints(BitfinexBP_ToobitAP),
            'BitfinexBP_TapBitAP': await converting_decimalPoints(BitfinexBP_TapBitAP),

            'BingXtBP_BinanceAP': await converting_decimalPoints(BingXBP_BinanceAP),
            'BingXtBP_BybitAP': await converting_decimalPoints(BingXBP_BybitAP),
            'BingXtBP_OKXAP': await converting_decimalPoints(BingXBP_OKXAP),
            'BingXtBP_UpbitAP': await converting_decimalPoints(BingXBP_UpbitAP),
            'BingXtBP_KucoinAP': await converting_decimalPoints(BingXBP_KucoinAP),
            'BingXtBP_BitgetAP': await converting_decimalPoints(BingXBP_BitgetAP),
            'BingXtBP_BitstampAP': await converting_decimalPoints(BingXBP_BitstampAP),
            'BingXtBP_GeminiAP': await converting_decimalPoints(BingXBP_GeminiAP),
            'BingXtBP_KrakenAP': await converting_decimalPoints(BingXBP_KrakenAP),
            'BingXtBP_GateioAP': await converting_decimalPoints(BingXBP_GateioAP),
            'BingXtBP_HTXAP': await converting_decimalPoints(BingXBP_HTXAP),
            'BingXtBP_MEXCAP': await converting_decimalPoints(BingXBP_MEXCAP),
            'BingXtBP_LbankAP': await converting_decimalPoints(BingXBP_LbankAP),
            'BingXtBP_BitmartAP': await converting_decimalPoints(BingXBP_BitmartAP),
            'BingXtBP_DeepcoinAP': await converting_decimalPoints(BingXBP_DeepcoinAP),
            'BingXtBP_BitfinexAP': await converting_decimalPoints(BingXBP_BitfinexAP),
            'BingXtBP_BingXAP': await converting_decimalPoints(BingXBP_BingXAP),
            'BingXtBP_OrangeXAP': await converting_decimalPoints(BingXBP_OrangeXAP),
            'BingXtBP_BitvenusAP': await converting_decimalPoints(BingXBP_BitvenusAP),
            'BingXtBP_BiconomyAP': await converting_decimalPoints(BingXBP_BiconomyAP),
            'BingXtBP_XTAP': await converting_decimalPoints(BingXBP_XTAP),
            'BingXtBP_BitflyerAP': await converting_decimalPoints(BingXBP_BitflyerAP),
            'BingXtBP_CoinWAP': await converting_decimalPoints(BingXBP_CoinWAP),
            'BingXtBP_ToobitAP': await converting_decimalPoints(BingXBP_ToobitAP),
            'BingXtBP_TapBitAP': await converting_decimalPoints(BingXBP_TapBitAP),

            'OrangeXBP_BinanceAP': await converting_decimalPoints(OrangeXBP_BinanceAP),
            'OrangeXBP_BybitAP': await converting_decimalPoints(OrangeXBP_BybitAP),
            'OrangeXBP_OKXAP': await converting_decimalPoints(OrangeXBP_OKXAP),
            'OrangeXBP_UpbitAP': await converting_decimalPoints(OrangeXBP_UpbitAP),
            'OrangeXBP_KucoinAP': await converting_decimalPoints(OrangeXBP_KucoinAP),
            'OrangeXBP_BitgetAP': await converting_decimalPoints(OrangeXBP_BitgetAP),
            'OrangeXBP_BitstampAP': await converting_decimalPoints(OrangeXBP_BitstampAP),
            'OrangeXBP_GeminiAP': await converting_decimalPoints(OrangeXBP_GeminiAP),
            'OrangeXBP_KrakenAP': await converting_decimalPoints(OrangeXBP_KrakenAP),
            'OrangeXBP_GateioAP': await converting_decimalPoints(OrangeXBP_GateioAP),
            'OrangeXBP_HTXAP': await converting_decimalPoints(OrangeXBP_HTXAP),
            'OrangeXBP_MEXCAP': await converting_decimalPoints(OrangeXBP_MEXCAP),
            'OrangeXBP_LbankAP': await converting_decimalPoints(OrangeXBP_LbankAP),
            'OrangeXBP_BitmartAP': await converting_decimalPoints(OrangeXBP_BitmartAP),
            'OrangeXBP_DeepcoinAP': await converting_decimalPoints(OrangeXBP_DeepcoinAP),
            'OrangeXBP_BitfinexAP': await converting_decimalPoints(OrangeXBP_BitfinexAP),
            'OrangeXBP_BingXAP': await converting_decimalPoints(OrangeXBP_BingXAP),
            'OrangeXBP_OrangeXAP': await converting_decimalPoints(OrangeXBP_OrangeXAP),
            'OrangeXBP_BitvenusAP': await converting_decimalPoints(OrangeXBP_BitvenusAP),
            'OrangeXBP_BiconomyAP': await converting_decimalPoints(OrangeXBP_BiconomyAP),
            'OrangeXBP_XTAP': await converting_decimalPoints(OrangeXBP_XTAP),
            'OrangeXBP_BitflyerAP': await converting_decimalPoints(OrangeXBP_BitflyerAP),
            'OrangeXBP_CoinWAP': await converting_decimalPoints(OrangeXBP_CoinWAP),
            'OrangeXBP_ToobitAP': await converting_decimalPoints(OrangeXBP_ToobitAP),
            'OrangeXBP_TapBitAP': await converting_decimalPoints(OrangeXBP_TapBitAP),

            'BitvenusBP_BinanceAP': await converting_decimalPoints(BitvenusBP_BinanceAP),
            'BitvenusBP_BybitAP': await converting_decimalPoints(BitvenusBP_BybitAP),
            'BitvenusBP_OKXAP': await converting_decimalPoints(BitvenusBP_OKXAP),
            'BitvenusBP_UpbitAP': await converting_decimalPoints(BitvenusBP_UpbitAP),
            'BitvenusBP_KucoinAP': await converting_decimalPoints(BitvenusBP_KucoinAP),
            'BitvenusBP_BitgetAP': await converting_decimalPoints(BitvenusBP_BitgetAP),
            'BitvenusBP_BitstampAP': await converting_decimalPoints(BitvenusBP_BitstampAP),
            'BitvenusBP_GeminiAP': await converting_decimalPoints(BitvenusBP_GeminiAP),
            'BitvenusBP_KrakenAP': await converting_decimalPoints(BitvenusBP_KrakenAP),
            'BitvenusBP_GateioAP': await converting_decimalPoints(BitvenusBP_GateioAP),
            'BitvenusBP_HTXAP': await converting_decimalPoints(BitvenusBP_HTXAP),
            'BitvenusBP_MEXCAP': await converting_decimalPoints(BitvenusBP_MEXCAP),
            'BitvenusBP_LbankAP': await converting_decimalPoints(BitvenusBP_LbankAP),
            'BitvenusBP_BitmartAP': await converting_decimalPoints(BitvenusBP_BitmartAP),
            'BitvenusBP_DeepcoinAP': await converting_decimalPoints(BitvenusBP_DeepcoinAP),
            'BitvenusBP_BitfinexAP': await converting_decimalPoints(BitvenusBP_BitfinexAP),
            'BitvenusBP_BingXAP': await converting_decimalPoints(BitvenusBP_BingXAP),
            'BitvenusBP_OrangeXAP': await converting_decimalPoints(BitvenusBP_OrangeXAP),
            'BitvenusBP_BitvenusAP': await converting_decimalPoints(BitvenusBP_BitvenusAP),
            'BitvenusBP_BiconomyAP': await converting_decimalPoints(BitvenusBP_BiconomyAP),
            'BitvenusBP_XTAP': await converting_decimalPoints(BitvenusBP_XTAP),
            'BitvenusBP_BitflyerAP': await converting_decimalPoints(BitvenusBP_BitflyerAP),
            'BitvenusBP_CoinWAP': await converting_decimalPoints(BitvenusBP_CoinWAP),
            'BitvenusBP_ToobitAP': await converting_decimalPoints(BitvenusBP_ToobitAP),
            'BitvenusBP_TapBitAP': await converting_decimalPoints(BitvenusBP_TapBitAP),

            'BiconomyBP_BinanceAP': await converting_decimalPoints(BiconomyBP_BinanceAP),
            'BiconomyBP_BybitAP': await converting_decimalPoints(BiconomyBP_BybitAP),
            'BiconomyBP_OKXAP': await converting_decimalPoints(BiconomyBP_OKXAP),
            'BiconomyBP_UpbitAP': await converting_decimalPoints(BiconomyBP_UpbitAP),
            'BiconomyBP_KucoinAP': await converting_decimalPoints(BiconomyBP_KucoinAP),
            'BiconomyBP_BitgetAP': await converting_decimalPoints(BiconomyBP_BitgetAP),
            'BiconomyBP_BitstampAP': await converting_decimalPoints(BiconomyBP_BitstampAP),
            'BiconomyBP_GeminiAP': await converting_decimalPoints(BiconomyBP_GeminiAP),
            'BiconomyBP_KrakenAP': await converting_decimalPoints(BiconomyBP_KrakenAP),
            'BiconomyBP_GateioAP': await converting_decimalPoints(BiconomyBP_GateioAP),
            'BiconomyBP_HTXAP': await converting_decimalPoints(BiconomyBP_HTXAP),
            'BiconomyBP_MEXCAP': await converting_decimalPoints(BiconomyBP_MEXCAP),
            'BiconomyBP_LbankAP': await converting_decimalPoints(BiconomyBP_LbankAP),
            'BiconomyBP_BitmartAP': await converting_decimalPoints(BiconomyBP_BitmartAP),
            'BiconomyBP_DeepcoinAP': await converting_decimalPoints(BiconomyBP_DeepcoinAP),
            'BiconomyBP_BitfinexAP': await converting_decimalPoints(BiconomyBP_BitfinexAP),
            'BiconomyBP_BingXAP': await converting_decimalPoints(BiconomyBP_BingXAP),
            'BiconomyBP_OrangeXAP': await converting_decimalPoints(BiconomyBP_OrangeXAP),
            'BiconomyBP_BitvenusAP': await converting_decimalPoints(BiconomyBP_BitvenusAP),
            'BiconomyBP_BiconomyAP': await converting_decimalPoints(BiconomyBP_BiconomyAP),
            'BiconomyBP_XTAP': await converting_decimalPoints(BiconomyBP_XTAP),
            'BiconomyBP_BitflyerAP': await converting_decimalPoints(BiconomyBP_BitflyerAP),
            'BiconomyBP_CoinWAP': await converting_decimalPoints(BiconomyBP_CoinWAP),
            'BiconomyBP_ToobitAP': await converting_decimalPoints(BiconomyBP_ToobitAP),
            'BiconomyBP_TapBitAP': await converting_decimalPoints(BiconomyBP_TapBitAP),

            'XTBP_BinanceAP': await converting_decimalPoints(XTBP_BinanceAP),
            'XTBP_BybitAP': await converting_decimalPoints(XTBP_BybitAP),
            'XTBP_OKXAP': await converting_decimalPoints(XTBP_OKXAP),
            'XTBP_UpbitAP': await converting_decimalPoints(XTBP_UpbitAP),
            'XTBP_KucoinAP': await converting_decimalPoints(XTBP_KucoinAP),
            'XTBP_BitgetAP': await converting_decimalPoints(XTBP_BitgetAP),
            'XTBP_BitstampAP': await converting_decimalPoints(XTBP_BitstampAP),
            'XTBP_GeminiAP': await converting_decimalPoints(XTBP_GeminiAP),
            'XTBP_KrakenAP': await converting_decimalPoints(XTBP_KrakenAP),
            'XTBP_GateioAP': await converting_decimalPoints(XTBP_GateioAP),
            'XTBP_HTXAP': await converting_decimalPoints(XTBP_HTXAP),
            'XTBP_MEXCAP': await converting_decimalPoints(XTBP_MEXCAP),
            'XTBP_LbankAP': await converting_decimalPoints(XTBP_LbankAP),
            'XTBP_BitmartAP': await converting_decimalPoints(XTBP_BitmartAP),
            'XTBP_DeepcoinAP': await converting_decimalPoints(XTBP_DeepcoinAP),
            'XTBP_BitfinexAP': await converting_decimalPoints(XTBP_BitfinexAP),
            'XTBP_BingXAP': await converting_decimalPoints(XTBP_BingXAP),
            'XTBP_OrangeXAP': await converting_decimalPoints(XTBP_OrangeXAP),
            'XTBP_BitvenusAP': await converting_decimalPoints(XTBP_BitvenusAP),
            'XTBP_BiconomyAP': await converting_decimalPoints(XTBP_BiconomyAP),
            'XTBP_XTAP': await converting_decimalPoints(XTBP_XTAP),
            'XTBP_BitflyerAP': await converting_decimalPoints(XTBP_BitflyerAP),
            'XTBP_CoinWAP': await converting_decimalPoints(XTBP_CoinWAP),
            'XTBP_ToobitAP': await converting_decimalPoints(XTBP_ToobitAP),
            'XTBP_TapBitAP': await converting_decimalPoints(XTBP_TapBitAP),

            'BitflyerBP_BinanceAP': await converting_decimalPoints(BitflyerBP_BinanceAP),
            'BitflyerBP_BybitAP': await converting_decimalPoints(BitflyerBP_BybitAP),
            'BitflyerBP_OKXAP': await converting_decimalPoints(BitflyerBP_OKXAP),
            'BitflyerBP_UpbitAP': await converting_decimalPoints(BitflyerBP_UpbitAP),
            'BitflyerBP_KucoinAP': await converting_decimalPoints(BitflyerBP_KucoinAP),
            'BitflyerBP_BitgetAP': await converting_decimalPoints(BitflyerBP_BitgetAP),
            'BitflyerBP_BitstampAP': await converting_decimalPoints(BitflyerBP_BitstampAP),
            'BitflyerBP_GeminiAP': await converting_decimalPoints(BitflyerBP_GeminiAP),
            'BitflyerBP_KrakenAP': await converting_decimalPoints(BitflyerBP_KrakenAP),
            'BitflyerBP_GateioAP': await converting_decimalPoints(BitflyerBP_GateioAP),
            'BitflyerBP_HTXAP': await converting_decimalPoints(BitflyerBP_HTXAP),
            'BitflyerBP_MEXCAP': await converting_decimalPoints(BitflyerBP_MEXCAP),
            'BitflyerBP_LbankAP': await converting_decimalPoints(BitflyerBP_LbankAP),
            'BitflyerBP_BitmartAP': await converting_decimalPoints(BitflyerBP_BitmartAP),
            'BitflyerBP_DeepcoinAP': await converting_decimalPoints(BitflyerBP_DeepcoinAP),
            'BitflyerBP_BitfinexAP': await converting_decimalPoints(BitflyerBP_BitfinexAP),
            'BitflyerBP_BingXAP': await converting_decimalPoints(BitflyerBP_BingXAP),
            'BitflyerBP_OrangeXAP': await converting_decimalPoints(BitflyerBP_OrangeXAP),
            'BitflyerBP_BitvenusAP': await converting_decimalPoints(BitflyerBP_BitvenusAP),
            'BitflyerBP_BiconomyAP': await converting_decimalPoints(BitflyerBP_BiconomyAP),
            'BitflyerBP_XTAP': await converting_decimalPoints(BitflyerBP_XTAP),
            'BitflyerBP_BitflyerAP': await converting_decimalPoints(BitflyerBP_BitflyerAP),
            'BitflyerBP_CoinWAP': await converting_decimalPoints(BitflyerBP_CoinWAP),
            'BitflyerBP_ToobitAP': await converting_decimalPoints(BitflyerBP_ToobitAP),
            'BitflyerBP_TapBitAP': await converting_decimalPoints(BitflyerBP_TapBitAP),

            'CoinWBP_BinanceAP': await converting_decimalPoints(CoinWBP_BinanceAP),
            'CoinWBP_BybitAP': await converting_decimalPoints(CoinWBP_BybitAP),
            'CoinWBP_OKXAP': await converting_decimalPoints(CoinWBP_OKXAP),
            'CoinWBP_UpbitAP': await converting_decimalPoints(CoinWBP_UpbitAP),
            'CoinWBP_KucoinAP': await converting_decimalPoints(CoinWBP_KucoinAP),
            'CoinWBP_BitgetAP': await converting_decimalPoints(CoinWBP_BitgetAP),
            'CoinWBP_BitstampAP': await converting_decimalPoints(CoinWBP_BitstampAP),
            'CoinWBP_GeminiAP': await converting_decimalPoints(CoinWBP_GeminiAP),
            'CoinWBP_KrakenAP': await converting_decimalPoints(CoinWBP_KrakenAP),
            'CoinWBP_GateioAP': await converting_decimalPoints(CoinWBP_GateioAP),
            'CoinWBP_HTXAP': await converting_decimalPoints(CoinWBP_HTXAP),
            'CoinWBP_MEXCAP': await converting_decimalPoints(CoinWBP_MEXCAP),
            'CoinWBP_LbankAP': await converting_decimalPoints(CoinWBP_LbankAP),
            'CoinWBP_BitmartAP': await converting_decimalPoints(CoinWBP_BitmartAP),
            'CoinWBP_DeepcoinAP': await converting_decimalPoints(CoinWBP_DeepcoinAP),
            'CoinWBP_BitfinexAP': await converting_decimalPoints(CoinWBP_BitfinexAP),
            'CoinWBP_BingXAP': await converting_decimalPoints(CoinWBP_BingXAP),
            'CoinWBP_OrangeXAP': await converting_decimalPoints(CoinWBP_OrangeXAP),
            'CoinWBP_BitvenusAP': await converting_decimalPoints(CoinWBP_BitvenusAP),
            'CoinWBP_BiconomyAP': await converting_decimalPoints(CoinWBP_BiconomyAP),
            'CoinWBP_XTAP': await converting_decimalPoints(CoinWBP_XTAP),
            'CoinWBP_BitflyerAP': await converting_decimalPoints(CoinWBP_BitflyerAP),
            'CoinWBP_CoinWAP': await converting_decimalPoints(CoinWBP_CoinWAP),
            'CoinWBP_ToobitAP': await converting_decimalPoints(CoinWBP_ToobitAP),
            'CoinWBP_TapBitAP': await converting_decimalPoints(CoinWBP_TapBitAP),

            'ToobitBP_BinanceAP': await converting_decimalPoints(ToobitBP_BinanceAP),
            'ToobitBP_BybitAP': await converting_decimalPoints(ToobitBP_BybitAP),
            'ToobitBP_OKXAP': await converting_decimalPoints(ToobitBP_OKXAP),
            'ToobitBP_UpbitAP': await converting_decimalPoints(ToobitBP_UpbitAP),
            'ToobitBP_KucoinAP': await converting_decimalPoints(ToobitBP_KucoinAP),
            'ToobitBP_BitgetAP': await converting_decimalPoints(ToobitBP_BitgetAP),
            'ToobitBP_BitstampAP': await converting_decimalPoints(ToobitBP_BitstampAP),
            'ToobitBP_GeminiAP': await converting_decimalPoints(ToobitBP_GeminiAP),
            'ToobitBP_KrakenAP': await converting_decimalPoints(ToobitBP_KrakenAP),
            'ToobitBP_GateioAP': await converting_decimalPoints(ToobitBP_GateioAP),
            'ToobitBP_HTXAP': await converting_decimalPoints(ToobitBP_HTXAP),
            'ToobitBP_MEXCAP': await converting_decimalPoints(ToobitBP_MEXCAP),
            'ToobitBP_LbankAP': await converting_decimalPoints(ToobitBP_LbankAP),
            'ToobitBP_BitmartAP': await converting_decimalPoints(ToobitBP_BitmartAP),
            'ToobitBP_DeepcoinAP': await converting_decimalPoints(ToobitBP_DeepcoinAP),
            'ToobitBP_BitfinexAP': await converting_decimalPoints(ToobitBP_BitfinexAP),
            'ToobitBP_BingXAP': await converting_decimalPoints(ToobitBP_BingXAP),
            'ToobitBP_OrangeXAP': await converting_decimalPoints(ToobitBP_OrangeXAP),
            'ToobitBP_BitvenusAP': await converting_decimalPoints(ToobitBP_BitvenusAP),
            'ToobitBP_BiconomyAP': await converting_decimalPoints(ToobitBP_BiconomyAP),
            'ToobitBP_XTAP': await converting_decimalPoints(ToobitBP_XTAP),
            'ToobitBP_BitflyerAP': await converting_decimalPoints(ToobitBP_BitflyerAP),
            'ToobitBP_CoinWAP': await converting_decimalPoints(ToobitBP_CoinWAP),
            'ToobitBP_ToobitAP': await converting_decimalPoints(ToobitBP_ToobitAP),
            'ToobitBP_TapBitAP': await converting_decimalPoints(ToobitBP_TapBitAP),

            'TapBitBP_BinanceAP': await converting_decimalPoints(TapBitBP_BinanceAP),
            'TapBitBP_BybitAP': await converting_decimalPoints(TapBitBP_BybitAP),
            'TapBitBP_OKXAP': await converting_decimalPoints(TapBitBP_OKXAP),
            'TapBitBP_UpbitAP': await converting_decimalPoints(TapBitBP_UpbitAP),
            'TapBitBP_KucoinAP': await converting_decimalPoints(TapBitBP_KucoinAP),
            'TapBitBP_BitgetAP': await converting_decimalPoints(TapBitBP_BitgetAP),
            'TapBitBP_BitstampAP': await converting_decimalPoints(TapBitBP_BitstampAP),
            'TapBitBP_GeminiAP': await converting_decimalPoints(TapBitBP_GeminiAP),
            'TapBitBP_KrakenAP': await converting_decimalPoints(TapBitBP_KrakenAP),
            'TapBitBP_GateioAP': await converting_decimalPoints(TapBitBP_GateioAP),
            'TapBitBP_HTXAP': await converting_decimalPoints(TapBitBP_HTXAP),
            'TapBitBP_MEXCAP': await converting_decimalPoints(TapBitBP_MEXCAP),
            'TapBitBP_LbankAP': await converting_decimalPoints(TapBitBP_LbankAP),
            'TapBitBP_BitmartAP': await converting_decimalPoints(TapBitBP_BitmartAP),
            'TapBitBP_DeepcoinAP': await converting_decimalPoints(TapBitBP_DeepcoinAP),
            'TapBitBP_BitfinexAP': await converting_decimalPoints(TapBitBP_BitfinexAP),
            'TapBitBP_BingXAP': await converting_decimalPoints(TapBitBP_BingXAP),
            'TapBitBP_OrangeXAP': await converting_decimalPoints(TapBitBP_OrangeXAP),
            'TapBitBP_BitvenusAP': await converting_decimalPoints(TapBitBP_BitvenusAP),
            'TapBitBP_BiconomyAP': await converting_decimalPoints(TapBitBP_BiconomyAP),
            'TapBitBP_XTAP': await converting_decimalPoints(TapBitBP_XTAP),
            'TapBitBP_BitflyerAP': await converting_decimalPoints(TapBitBP_BitflyerAP),
            'TapBitBP_CoinWAP': await converting_decimalPoints(TapBitBP_CoinWAP),
            'TapBitBP_ToobitAP': await converting_decimalPoints(TapBitBP_ToobitAP),
            'TapBitBP_TapBitAP': await converting_decimalPoints(TapBitBP_TapBitAP),

            # You can continue adding more data here as needed
        }

    # Return the updated data
    return data





