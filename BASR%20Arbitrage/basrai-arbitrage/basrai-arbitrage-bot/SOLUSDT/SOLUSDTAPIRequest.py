import threading
import time
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import asyncio
import ssl
import certifi

from BaseAlgorithm import Exchange
import config

ssl_context = ssl.create_default_context(cafile=certifi.where())


async def fetch_price(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return response.status, data
    except aiohttp.ClientError as e:
        print(f"Client error fetching data from {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None, None


async def main():
    start = time.time()

    # URLs for fetching data, stored in the config file
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

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = [fetch_price(session, url) for url in urls]
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
                GeminiLTPV = GeminiLTPURLRes['volume']['SOL']
                GeminiLTPTM = GeminiLTPURLRes['volume']['timestamp']
                GeminiLTPT = (GeminiLTPTM)
        except Exception as e:

            Gemini_Status = 400
        try:

            if KrakenOBURL_Res:
                KrakenAP1 = float(KrakenOBURL_Res['result']['SOLUSDT']['asks'][0][0])
                KrakenAP2 = float(KrakenOBURL_Res['result']['SOLUSDT']['asks'][1][0])
                KrakenAP3 = float(KrakenOBURL_Res['result']['SOLUSDT']['asks'][2][0])
                KrakenAP4 = float(KrakenOBURL_Res['result']['SOLUSDT']['asks'][3][0])
                KrakenAP5 = float(KrakenOBURL_Res['result']['SOLUSDT']['asks'][4][0])
                KrakenAPV1 = (KrakenOBURL_Res['result']['SOLUSDT']['asks'][0][1])
                KrakenAPV2 = KrakenOBURL_Res['result']['SOLUSDT']['asks'][1][1]
                KrakenAPV3 = KrakenOBURL_Res['result']['SOLUSDT']['asks'][2][1]
                KrakenAPV4 = KrakenOBURL_Res['result']['SOLUSDT']['asks'][3][1]
                KrakenAPV5 = KrakenOBURL_Res['result']['SOLUSDT']['asks'][4][1]
                KrakenBP1 = float(KrakenOBURL_Res['result']['SOLUSDT']['bids'][0][0])
                KrakenBP2 = float(KrakenOBURL_Res['result']['SOLUSDT']['bids'][1][0])
                KrakenBP3 = float(KrakenOBURL_Res['result']['SOLUSDT']['bids'][2][0])
                KrakenBP4 = float(KrakenOBURL_Res['result']['SOLUSDT']['bids'][3][0])
                KrakenBP5 = float(KrakenOBURL_Res['result']['SOLUSDT']['bids'][4][0])
                KrakenBPV1 = (KrakenOBURL_Res['result']['SOLUSDT']['bids'][0][1])
                KrakenBPV2 = KrakenOBURL_Res['result']['SOLUSDT']['bids'][1][1]
                KrakenBPV3 = KrakenOBURL_Res['result']['SOLUSDT']['bids'][2][1]
                KrakenBPV4 = KrakenOBURL_Res['result']['SOLUSDT']['bids'][3][1]
                KrakenBPV5 = KrakenOBURL_Res['result']['SOLUSDT']['bids'][4][1]
                KrakenOBTM = KrakenOBURL_Res['result']['SOLUSDT']['asks'][0][2]
                KrakenOBT = (KrakenOBTM)

                KrakenLTP = float(KrakenLTP_Res['result']['SOLUSDT'][0][0])
                KrakenLTPV = KrakenLTP_Res['result']['SOLUSDT'][0][1]
                KrakenLTPTM = int(KrakenLTP_Res['result']['SOLUSDT'][0][2])
                KrakenLTPT = (KrakenLTPTM)
        except Exception as e:
            print(f"Error processing Kraken order book data: {e}")
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



    end = time.time()
    processingtime = (end - start) * 1_000_000

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
        "TapBit_Status": TapBit_Status,

        "BinanceBP_BinanceAP": results['BinanceBP_BinanceAP'],
        "BinanceBP_BybitAP": results['BinanceBP_BybitAP'],
        "BinanceBP_OKXAP": results['BinanceBP_OKXAP'],
        "BinanceBP_UpbitAP": results['BinanceBP_UpbitAP'],
        "BinanceBP_KucoinAP": results['BinanceBP_KucoinAP'],
        "BinanceBP_BitgetAP": results['BinanceBP_BitgetAP'],
        "BinanceBP_BitstampAP": results['BinanceBP_BitstampAP'],
        "BinanceBP_GeminiAP": results['BinanceBP_GeminiAP'],
        "BinanceBP_KrakenAP": results['BinanceBP_KrakenAP'],
        "BinanceBP_GateioAP": results['BinanceBP_Gate.ioAP'],
        "BinanceBP_HTXAP": results['BinanceBP_HTXAP'],
        "BinanceBP_MEXCAP": results['BinanceBP_MEXCAP'],
        "BinanceBP_LbankAP": results['BinanceBP_LbankAP'],
        "BinanceBP_BitmartAP": results['BinanceBP_BitmartAP'],
        "BinanceBP_DeepcoinAP": results['BinanceBP_DeepcoinAP'],
        "BinanceBP_BitfinexAP": results['BinanceBP_BitfinexAP'],
        "BinanceBP_BingXAP": results['BinanceBP_BingXAP'],
        "BinanceBP_OrangeXAP": results['BinanceBP_OrangeXAP'],
        "BinanceBP_BitvenusAP": results['BinanceBP_BitvenusAP'],
        "BinanceBP_BiconomyAP": results['BinanceBP_BiconomyAP'],
        "BinanceBP_XTAP": results['BinanceBP_XTAP'],
        "BinanceBP_BitflyerAP": results['BinanceBP_BitflyerAP'],
        "BinanceBP_CoinWAP": results['BinanceBP_CoinWAP'],
        "BinanceBP_ToobitAP": results['BinanceBP_ToobitAP'],
        "BinanceBP_TapBitAP": results['BinanceBP_TapBitAP'],

        "BybitBP_BinanceAP": results['BybitBP_BinanceAP'],
        "BybitBP_BybitAP": results['BybitBP_BybitAP'],
        "BybitBP_OKXAP": results['BybitBP_OKXAP'],
        "BybitBP_UpbitAP": results['BybitBP_UpbitAP'],
        "BybitBP_KucoinAP": results['BybitBP_KucoinAP'],
        "BybitBP_BitgetAP": results['BybitBP_BitgetAP'],
        "BybitBP_BitstampAP": results['BybitBP_BitstampAP'],
        "BybitBP_GeminiAP": results['BybitBP_GeminiAP'],
        "BybitBP_KrakenAP": results['BybitBP_KrakenAP'],
        "BybitBP_GateioAP": results['BybitBP_Gate.ioAP'],
        "BybitBP_HTXAP": results['BybitBP_HTXAP'],
        "BybitBP_MEXCAP": results['BybitBP_MEXCAP'],
        "BybitBP_LbankAP": results['BybitBP_LbankAP'],
        "BybitBP_BitmartAP": results['BybitBP_BitmartAP'],
        "BybitBP_DeepcoinAP": results['BybitBP_DeepcoinAP'],
        "BybitBP_BitfinexAP": results['BybitBP_BitfinexAP'],
        "BybitBP_BingXAP": results['BybitBP_BingXAP'],
        "BybitBP_OrangeXAP": results['BybitBP_OrangeXAP'],
        "BybitBP_BitvenusAP": results['BybitBP_BitvenusAP'],
        "BybitBP_BiconomyAP": results['BybitBP_BiconomyAP'],
        "BybitBP_XTAP": results['BybitBP_XTAP'],
        "BybitBP_BitflyerAP": results['BybitBP_BitflyerAP'],
        "BybitBP_CoinWAP": results['BybitBP_CoinWAP'],
        "BybitBP_ToobitAP": results['BybitBP_ToobitAP'],
        "BybitBP_TapBitAP": results['BybitBP_TapBitAP'],

        "OKXBP_BinanceAP": results['OKXBP_BinanceAP'],
        "OKXBP_BybitAP": results['OKXBP_BybitAP'],
        "OKXBP_OKXAP": results['OKXBP_OKXAP'],
        "OKXBP_UpbitAP": results['OKXBP_UpbitAP'],
        "OKXBP_KucoinAP": results['OKXBP_KucoinAP'],
        "OKXBP_BitgetAP": results['OKXBP_BitgetAP'],
        "OKXBP_BitstampAP": results['OKXBP_BitstampAP'],
        "OKXBP_GeminiAP": results['OKXBP_GeminiAP'],
        "OKXBP_KrakenAP": results['OKXBP_KrakenAP'],
        "OKXBP_GateioAP": results['BinanceBP_Gate.ioAP'],
        "OKXBP_HTXAP": results['OKXBP_HTXAP'],
        "OKXBP_MEXCAP": results['OKXBP_MEXCAP'],
        "OKXBP_LbankAP": results['OKXBP_LbankAP'],
        "OKXBP_BitmartAP": results['OKXBP_BitmartAP'],
        "OKXBP_DeepcoinAP": results['OKXBP_DeepcoinAP'],
        "OKXBP_BitfinexAP": results['OKXBP_BitfinexAP'],
        "OKXBP_BingXAP": results['OKXBP_BingXAP'],
        "OKXBP_OrangeXAP": results['OKXBP_OrangeXAP'],
        "OKXBP_BitvenusAP": results['OKXBP_BitvenusAP'],
        "OKXBP_BiconomyAP": results['OKXBP_BiconomyAP'],
        "OKXBP_XTAP": results['OKXBP_XTAP'],
        "OKXBP_BitflyerAP": results['OKXBP_BitflyerAP'],
        "OKXBP_CoinWAP": results['OKXBP_CoinWAP'],
        "OKXBP_ToobitAP": results['OKXBP_ToobitAP'],
        "OKXBP_TapBitAP": results['OKXBP_TapBitAP'],

        "UpbitBP_BinanceAP": results['UpbitBP_BinanceAP'],
        "UpbitBP_BybitAP": results['UpbitBP_BybitAP'],
        "UpbitBP_OKXAP": results['UpbitBP_OKXAP'],
        "UpbitBP_UpbitAP": results['UpbitBP_UpbitAP'],
        "UpbitBP_KucoinAP": results['UpbitBP_KucoinAP'],
        "UpbitBP_BitgetAP": results['UpbitBP_BitgetAP'],
        "UpbitBP_BitstampAP": results['UpbitBP_BitstampAP'],
        "UpbitBP_GeminiAP": results['UpbitBP_GeminiAP'],
        "UpbitBP_KrakenAP": results['UpbitBP_KrakenAP'],
        "UpbitBP_GateioAP": results['UpbitBP_Gate.ioAP'],
        "UpbitBP_HTXAP": results['UpbitBP_HTXAP'],
        "UpbitBP_MEXCAP": results['UpbitBP_MEXCAP'],
        "UpbitBP_LbankAP": results['UpbitBP_LbankAP'],
        "UpbitBP_BitmartAP": results['UpbitBP_BitmartAP'],
        "UpbitBP_DeepcoinAP": results['UpbitBP_DeepcoinAP'],
        "UpbitBP_BitfinexAP": results['UpbitBP_BitfinexAP'],
        "UpbitBP_BingXAP": results['UpbitBP_BingXAP'],
        "UpbitBP_OrangeXAP": results['UpbitBP_OrangeXAP'],
        "UpbitBP_BitvenusAP": results['UpbitBP_BitvenusAP'],
        "UpbitBP_BiconomyAP": results['UpbitBP_BiconomyAP'],
        "UpbitBP_XTAP": results['UpbitBP_XTAP'],
        "UpbitBP_BitflyerAP": results['UpbitBP_BitflyerAP'],
        "UpbitBP_CoinWAP": results['UpbitBP_CoinWAP'],
        "UpbitBP_ToobitAP": results['UpbitBP_ToobitAP'],
        "UpbitBP_TapBitAP": results['UpbitBP_TapBitAP'],

        "KucoinBP_BinanceAP": results['KucoinBP_BinanceAP'],
        "KucoinBP_BybitAP": results['KucoinBP_BybitAP'],
        "KucoinBP_OKXAP": results['KucoinBP_OKXAP'],
        "KucoinBP_UpbitAP": results['KucoinBP_UpbitAP'],
        "KucoinBP_KucoinAP": results['KucoinBP_KucoinAP'],
        "KucoinBP_BitgetAP": results['KucoinBP_BitgetAP'],
        "KucoinBP_BitstampAP": results['KucoinBP_BitstampAP'],
        "KucoinBP_GeminiAP": results['KucoinBP_GeminiAP'],
        "KucoinBP_KrakenAP": results['KucoinBP_KrakenAP'],
        "KucoinBP_GateioAP": results['KucoinBP_Gate.ioAP'],
        "KucoinBP_HTXAP": results['KucoinBP_HTXAP'],
        "KucoinBP_MEXCAP": results['KucoinBP_MEXCAP'],
        "KucoinBP_LbankAP": results['KucoinBP_LbankAP'],
        "KucoinBP_BitmartAP": results['KucoinBP_BitmartAP'],
        "KucoinBP_DeepcoinAP": results['KucoinBP_DeepcoinAP'],
        "KucoinBP_BitfinexAP": results['KucoinBP_BitfinexAP'],
        "KucoinBP_BingXAP": results['KucoinBP_BingXAP'],
        "KucoinBP_OrangeXAP": results['KucoinBP_OrangeXAP'],
        "KucoinBP_BitvenusAP": results['KucoinBP_BitvenusAP'],
        "KucoinBP_BiconomyAP": results['KucoinBP_BiconomyAP'],
        "KucoinBP_XTAP": results['KucoinBP_XTAP'],
        "KucoinBP_BitflyerAP": results['KucoinBP_BitflyerAP'],
        "KucoinBP_CoinWAP": results['KucoinBP_CoinWAP'],
        "KucoinBP_ToobitAP": results['KucoinBP_ToobitAP'],
        "KucoinBP_TapBitAP": results['KucoinBP_TapBitAP'],

        "BitgetBP_BinanceAP": results['BitgetBP_BinanceAP'],
        "BitgetBP_BybitAP": results['BitgetBP_BybitAP'],
        "BitgetBP_OKXAP": results['BitgetBP_OKXAP'],
        "BitgetBP_UpbitAP": results['BitgetBP_UpbitAP'],
        "BitgetBP_KucoinAP": results['BitgetBP_KucoinAP'],
        "BitgetBP_BitgetAP": results['BitgetBP_BitgetAP'],
        "BitgetBP_BitstampAP": results['BitgetBP_BitstampAP'],
        "BitgetBP_GeminiAP": results['BitgetBP_GeminiAP'],
        "BitgetBP_KrakenAP": results['BitgetBP_KrakenAP'],
        "BitgetBP_GateioAP": results['BitgetBP_Gate.ioAP'],
        "BitgetBP_HTXAP": results['BitgetBP_HTXAP'],
        "BitgetBP_MEXCAP": results['BitgetBP_MEXCAP'],
        "BitgetBP_LbankAP": results['BitgetBP_LbankAP'],
        "BitgetBP_BitmartAP": results['BitgetBP_BitmartAP'],
        "BitgetBP_DeepcoinAP": results['BitgetBP_DeepcoinAP'],
        "BitgetBP_BitfinexAP": results['BitgetBP_BitfinexAP'],
        "BitgetBP_BingXAP": results['BitgetBP_BingXAP'],
        "BitgetBP_OrangeXAP": results['BitgetBP_OrangeXAP'],
        "BitgetBP_BitvenusAP": results['BitgetBP_BitvenusAP'],
        "BitgetBP_BiconomyAP": results['BitgetBP_BiconomyAP'],
        "BitgetBP_XTAP": results['BitgetBP_XTAP'],
        "BitgetBP_BitflyerAP": results['BitgetBP_BitflyerAP'],
        "BitgetBP_CoinWAP": results['BitgetBP_CoinWAP'],
        "BitgetBP_ToobitAP": results['BitgetBP_ToobitAP'],
        "BitgetBP_TapBitAP": results['BitgetBP_TapBitAP'],

        "BitstampBP_BinanceAP": results['BitstampBP_BinanceAP'],
        "BitstampBP_BybitAP": results['BitstampBP_BybitAP'],
        "BitstampBP_OKXAP": results['BitstampBP_OKXAP'],
        "BitstampBP_UpbitAP": results['BitstampBP_UpbitAP'],
        "BitstampBP_KucoinAP": results['BitstampBP_KucoinAP'],
        "BitstampBP_BitgetAP": results['BitstampBP_BitgetAP'],
        "BitstampBP_BitstampAP": results['BitstampBP_BitstampAP'],
        "BitstampBP_GeminiAP": results['BitstampBP_GeminiAP'],
        "BitstampBP_KrakenAP": results['BitstampBP_KrakenAP'],
        "BitstampBP_GateioAP": results['BitstampBP_Gate.ioAP'],
        "BitstampBP_HTXAP": results['BitstampBP_HTXAP'],
        "BitstampBP_MEXCAP": results['BitstampBP_MEXCAP'],
        "BitstampBP_LbankAP": results['BitstampBP_LbankAP'],
        "BitstampBP_BitmartAP": results['BitstampBP_BitmartAP'],
        "BitstampBP_DeepcoinAP": results['BitstampBP_DeepcoinAP'],
        "BitstampBP_BitfinexAP": results['BitstampBP_BitfinexAP'],
        "BitstampBP_BingXAP": results['BitstampBP_BingXAP'],
        "BitstampBP_OrangeXAP": results['BitstampBP_OrangeXAP'],
        "BitstampBP_BitvenusAP": results['BitstampBP_BitvenusAP'],
        "BitstampBP_BiconomyAP": results['BitstampBP_BiconomyAP'],
        "BitstampBP_XTAP": results['BitstampBP_XTAP'],
        "BitstampBP_BitflyerAP": results['BitstampBP_BitflyerAP'],
        "BitstampBP_CoinWAP": results['BitstampBP_CoinWAP'],
        "BitstampBP_ToobitAP": results['BitstampBP_ToobitAP'],
        "BitstampBP_TapBitAP": results['BitstampBP_TapBitAP'],

        "GeminiBP_BinanceAP": results['GeminiBP_BinanceAP'],
        "GeminiBP_BybitAP": results['GeminiBP_BybitAP'],
        "GeminiBP_OKXAP": results['GeminiBP_OKXAP'],
        "GeminiBP_UpbitAP": results['GeminiBP_UpbitAP'],
        "GeminiBP_KucoinAP": results['GeminiBP_KucoinAP'],
        "GeminiBP_BitgetAP": results['GeminiBP_BitgetAP'],
        "GeminiBP_BitstampAP": results['GeminiBP_BitstampAP'],
        "GeminiBP_GeminiAP": results['GeminiBP_GeminiAP'],
        "GeminiBP_KrakenAP": results['GeminiBP_KrakenAP'],
        "GeminiBP_GateioAP": results['GeminiBP_Gate.ioAP'],
        "GeminiBP_HTXAP": results['GeminiBP_HTXAP'],
        "GeminiBP_MEXCAP": results['GeminiBP_MEXCAP'],
        "GeminiBP_LbankAP": results['GeminiBP_LbankAP'],
        "GeminiBP_BitmartAP": results['GeminiBP_BitmartAP'],
        "GeminiBP_DeepcoinAP": results['GeminiBP_DeepcoinAP'],
        "GeminiBP_BitfinexAP": results['GeminiBP_BitfinexAP'],
        "GeminiBP_BingXAP": results['GeminiBP_BingXAP'],
        "GeminiBP_OrangeXAP": results['GeminiBP_OrangeXAP'],
        "GeminiBP_BitvenusAP": results['GeminiBP_BitvenusAP'],
        "GeminiBP_BiconomyAP": results['GeminiBP_BiconomyAP'],
        "GeminiBP_XTAP": results['GeminiBP_XTAP'],
        "GeminiBP_BitflyerAP": results['GeminiBP_BitflyerAP'],
        "GeminiBP_CoinWAP": results['GeminiBP_CoinWAP'],
        "GeminiBP_ToobitAP": results['GeminiBP_ToobitAP'],
        "GeminiBP_TapBitAP": results['GeminiBP_TapBitAP'],

        "KrakenBP_BinanceAP": results['KrakenBP_BinanceAP'],
        "KrakenBP_BybitAP": results['KrakenBP_BybitAP'],
        "KrakenBP_OKXAP": results['KrakenBP_OKXAP'],
        "KrakenBP_UpbitAP": results['KrakenBP_UpbitAP'],
        "KrakenBP_KucoinAP": results['KrakenBP_KucoinAP'],
        "KrakenBP_BitgetAP": results['KrakenBP_BitgetAP'],
        "KrakenBP_BitstampAP": results['KrakenBP_BitstampAP'],
        "KrakenBP_GeminiAP": results['KrakenBP_GeminiAP'],
        "KrakenBP_KrakenAP": results['KrakenBP_KrakenAP'],
        "KrakenBP_GateioAP": results['KrakenBP_Gate.ioAP'],
        "KrakenBP_HTXAP": results['KrakenBP_HTXAP'],
        "KrakenBP_MEXCAP": results['KrakenBP_MEXCAP'],
        "KrakenBP_LbankAP": results['KrakenBP_LbankAP'],
        "KrakenBP_BitmartAP": results['KrakenBP_BitmartAP'],
        "KrakenBP_DeepcoinAP": results['KrakenBP_DeepcoinAP'],
        "KrakenBP_BitfinexAP": results['KrakenBP_BitfinexAP'],
        "KrakenBP_BingXAP": results['KrakenBP_BingXAP'],
        "KrakenBP_OrangeXAP": results['KrakenBP_OrangeXAP'],
        "KrakenBP_BitvenusAP": results['KrakenBP_BitvenusAP'],
        "KrakenBP_BiconomyAP": results['KrakenBP_BiconomyAP'],
        "KrakenBP_XTAP": results['KrakenBP_XTAP'],
        "KrakenBP_BitflyerAP": results['KrakenBP_BitflyerAP'],
        "KrakenBP_CoinWAP": results['KrakenBP_CoinWAP'],
        "KrakenBP_ToobitAP": results['KrakenBP_ToobitAP'],
        "KrakenBP_TapBitAP": results['KrakenBP_TapBitAP'],

        "GateioBP_BinanceAP": results['Gate.ioBP_BinanceAP'],
        "GateioBP_BybitAP": results['Gate.ioBP_BybitAP'],
        "GateioBP_OKXAP": results['Gate.ioBP_OKXAP'],
        "GateioBP_UpbitAP": results['Gate.ioBP_UpbitAP'],
        "GateioBP_KucoinAP": results['Gate.ioBP_KucoinAP'],
        "GateioBP_BitgetAP": results['Gate.ioBP_BitgetAP'],
        "GateioBP_BitstampAP": results['Gate.ioBP_BitstampAP'],
        "GateioBP_GeminiAP": results['Gate.ioBP_GeminiAP'],
        "GateioBP_KrakenAP": results['Gate.ioBP_KrakenAP'],
        "GateioBP_GateioAP": results['BinanceBP_Gate.ioAP'],
        "GateioBP_HTXAP": results['Gate.ioBP_HTXAP'],
        "GateioBP_MEXCAP": results['Gate.ioBP_MEXCAP'],
        "GateioBP_LbankAP": results['Gate.ioBP_LbankAP'],
        "GateioBP_BitmartAP": results['Gate.ioBP_BitmartAP'],
        "GateioBP_DeepcoinAP": results['Gate.ioBP_DeepcoinAP'],
        "GateioBP_BitfinexAP": results['Gate.ioBP_BitfinexAP'],
        "GateioBP_BingXAP": results['Gate.ioBP_BingXAP'],
        "GateioBP_OrangeXAP": results['Gate.ioBP_OrangeXAP'],
        "GateioBP_BitvenusAP": results['Gate.ioBP_BitvenusAP'],
        "GateioBP_BiconomyAP": results['Gate.ioBP_BiconomyAP'],
        "GateioBP_XTAP": results['Gate.ioBP_XTAP'],
        "GateioBP_BitflyerAP": results['Gate.ioBP_BitflyerAP'],
        "GateioBP_CoinWAP": results['Gate.ioBP_CoinWAP'],
        "GateioBP_ToobitAP": results['Gate.ioBP_ToobitAP'],
        "GateioBP_TapBitAP": results['Gate.ioBP_TapBitAP'],

        "HTXBP_BinanceAP": results['HTXBP_BinanceAP'],
        "HTXBP_BybitAP": results['HTXBP_BybitAP'],
        "HTXBP_OKXAP": results['HTXBP_OKXAP'],
        "HTXBP_UpbitAP": results['HTXBP_UpbitAP'],
        "HTXBP_KucoinAP": results['HTXBP_KucoinAP'],
        "HTXBP_BitgetAP": results['HTXBP_BitgetAP'],
        "HTXBP_BitstampAP": results['HTXBP_BitstampAP'],
        "HTXBP_GeminiAP": results['HTXBP_GeminiAP'],
        "HTXBP_KrakenAP": results['HTXBP_KrakenAP'],
        "HTXBP_GateioAP": results['HTXBP_Gate.ioAP'],
        "HTXBP_HTXAP": results['HTXBP_HTXAP'],
        "HTXBP_MEXCAP": results['HTXBP_MEXCAP'],
        "HTXBP_LbankAP": results['HTXBP_LbankAP'],
        "HTXBP_BitmartAP": results['HTXBP_BitmartAP'],
        "HTXBP_DeepcoinAP": results['HTXBP_DeepcoinAP'],
        "HTXBP_BitfinexAP": results['HTXBP_BitfinexAP'],
        "HTXBP_BingXAP": results['HTXBP_BingXAP'],
        "HTXBP_OrangeXAP": results['HTXBP_OrangeXAP'],
        "HTXBP_BitvenusAP": results['HTXBP_BitvenusAP'],
        "HTXBP_BiconomyAP": results['HTXBP_BiconomyAP'],
        "HTXBP_XTAP": results['HTXBP_XTAP'],
        "HTXBP_BitflyerAP": results['HTXBP_BitflyerAP'],
        "HTXBP_CoinWAP": results['HTXBP_CoinWAP'],
        "HTXBP_ToobitAP": results['HTXBP_ToobitAP'],
        "HTXBP_TapBitAP": results['HTXBP_TapBitAP'],

        "MEXCBP_BinanceAP": results['MEXCBP_BinanceAP'],
        "MEXCBP_BybitAP": results['MEXCBP_BybitAP'],
        "MEXCBP_OKXAP": results['MEXCBP_OKXAP'],
        "MEXCBP_UpbitAP": results['MEXCBP_UpbitAP'],
        "MEXCBP_KucoinAP": results['MEXCBP_KucoinAP'],
        "MEXCBP_BitgetAP": results['MEXCBP_BitgetAP'],
        "MEXCBP_BitstampAP": results['MEXCBP_BitstampAP'],
        "MEXCBP_GeminiAP": results['MEXCBP_GeminiAP'],
        "MEXCBP_KrakenAP": results['MEXCBP_KrakenAP'],
        "MEXCBP_GateioAP": results['BinanceBP_Gate.ioAP'],
        "MEXCBP_HTXAP": results['MEXCBP_HTXAP'],
        "MEXCBP_MEXCAP": results['MEXCBP_MEXCAP'],
        "MEXCBP_LbankAP": results['MEXCBP_LbankAP'],
        "MEXCBP_BitmartAP": results['MEXCBP_BitmartAP'],
        "MEXCBP_DeepcoinAP": results['MEXCBP_DeepcoinAP'],
        "MEXCBP_BitfinexAP": results['MEXCBP_BitfinexAP'],
        "MEXCBP_BingXAP": results['MEXCBP_BingXAP'],
        "MEXCBP_OrangeXAP": results['MEXCBP_OrangeXAP'],
        "MEXCBP_BitvenusAP": results['MEXCBP_BitvenusAP'],
        "MEXCBP_BiconomyAP": results['MEXCBP_BiconomyAP'],
        "MEXCBP_XTAP": results['MEXCBP_XTAP'],
        "MEXCBP_BitflyerAP": results['MEXCBP_BitflyerAP'],
        "MEXCBP_CoinWAP": results['MEXCBP_CoinWAP'],
        "MEXCBP_ToobitAP": results['MEXCBP_ToobitAP'],
        "MEXCBP_TapBitAP": results['MEXCBP_TapBitAP'],

        "LbankBP_BinanceAP": results['LbankBP_BinanceAP'],
        "LbankBP_BybitAP": results['LbankBP_BybitAP'],
        "LbankBP_OKXAP": results['LbankBP_OKXAP'],
        "LbankBP_UpbitAP": results['LbankBP_UpbitAP'],
        "LbankBP_KucoinAP": results['LbankBP_KucoinAP'],
        "LbankBP_BitgetAP": results['LbankBP_BitgetAP'],
        "LbankBP_BitstampAP": results['LbankBP_BitstampAP'],
        "LbankBP_GeminiAP": results['LbankBP_GeminiAP'],
        "LbankBP_KrakenAP": results['LbankBP_KrakenAP'],
        "LbankBP_GateioAP": results['LbankBP_Gate.ioAP'],
        "LbankBP_HTXAP": results['LbankBP_HTXAP'],
        "LbankBP_MEXCAP": results['LbankBP_MEXCAP'],
        "LbankBP_LbankAP": results['LbankBP_LbankAP'],
        "LbankBP_BitmartAP": results['LbankBP_BitmartAP'],
        "LbankBP_DeepcoinAP": results['LbankBP_DeepcoinAP'],
        "LbankBP_BitfinexAP": results['LbankBP_BitfinexAP'],
        "LbankBP_BingXAP": results['LbankBP_BingXAP'],
        "LbankBP_OrangeXAP": results['LbankBP_OrangeXAP'],
        "LbankBP_BitvenusAP": results['LbankBP_BitvenusAP'],
        "LbankBP_BiconomyAP": results['LbankBP_BiconomyAP'],
        "LbankBP_XTAP": results['LbankBP_XTAP'],
        "LbankBP_BitflyerAP": results['LbankBP_BitflyerAP'],
        "LbankBP_CoinWAP": results['LbankBP_CoinWAP'],
        "LbankBP_ToobitAP": results['LbankBP_ToobitAP'],
        "LbankBP_TapBitAP": results['LbankBP_TapBitAP'],

        "BitmartBP_BinanceAP": results['BitmartBP_BinanceAP'],
        "BitmartBP_BybitAP": results['BitmartBP_BybitAP'],
        "BitmartBP_OKXAP": results['BitmartBP_OKXAP'],
        "BitmartBP_UpbitAP": results['BitmartBP_UpbitAP'],
        "BitmartBP_KucoinAP": results['BitmartBP_KucoinAP'],
        "BitmartBP_BitgetAP": results['BitmartBP_BitgetAP'],
        "BitmartBP_BitstampAP": results['BitmartBP_BitstampAP'],
        "BitmartBP_GeminiAP": results['BitmartBP_GeminiAP'],
        "BitmartBP_KrakenAP": results['BitmartBP_KrakenAP'],
        "BitmartBP_GateioAP": results['BitmartBP_Gate.ioAP'],
        "BitmartBP_HTXAP": results['BitmartBP_HTXAP'],
        "BitmartBP_MEXCAP": results['BitmartBP_MEXCAP'],
        "BitmartBP_LbankAP": results['BitmartBP_LbankAP'],
        "BitmartBP_BitmartAP": results['BitmartBP_BitmartAP'],
        "BitmartBP_DeepcoinAP": results['BitmartBP_DeepcoinAP'],
        "BitmartBP_BitfinexAP": results['BitmartBP_BitfinexAP'],
        "BitmartBP_BingXAP": results['BitmartBP_BingXAP'],
        "BitmartBP_OrangeXAP": results['BitmartBP_OrangeXAP'],
        "BitmartBP_BitvenusAP": results['BitmartBP_BitvenusAP'],
        "BitmartBP_BiconomyAP": results['BitmartBP_BiconomyAP'],
        "BitmartBP_XTAP": results['BitmartBP_XTAP'],
        "BitmartBP_BitflyerAP": results['BitmartBP_BitflyerAP'],
        "BitmartBP_CoinWAP": results['BitmartBP_CoinWAP'],
        "BitmartBP_ToobitAP": results['BitmartBP_ToobitAP'],
        "BitmartBP_TapBitAP": results['BitmartBP_TapBitAP'],

        "DeepcoinBP_BinanceAP": results['DeepcoinBP_BinanceAP'],
        "DeepcoinBP_BybitAP": results['DeepcoinBP_BybitAP'],
        "DeepcoinBP_OKXAP": results['DeepcoinBP_OKXAP'],
        "DeepcoinBP_UpbitAP": results['DeepcoinBP_UpbitAP'],
        "DeepcoinBP_KucoinAP": results['DeepcoinBP_KucoinAP'],
        "DeepcoinBP_BitgetAP": results['DeepcoinBP_BitgetAP'],
        "DeepcoinBP_BitstampAP": results['DeepcoinBP_BitstampAP'],
        "DeepcoinBP_GeminiAP": results['DeepcoinBP_GeminiAP'],
        "DeepcoinBP_KrakenAP": results['DeepcoinBP_KrakenAP'],
        "DeepcoinBP_GateioAP": results['DeepcoinBP_Gate.ioAP'],
        "DeepcoinBP_HTXAP": results['DeepcoinBP_HTXAP'],
        "DeepcoinBP_MEXCAP": results['DeepcoinBP_MEXCAP'],
        "DeepcoinBP_LbankAP": results['DeepcoinBP_LbankAP'],
        "DeepcoinBP_BitmartAP": results['DeepcoinBP_BitmartAP'],
        "DeepcoinBP_DeepcoinAP": results['DeepcoinBP_DeepcoinAP'],
        "DeepcoinBP_BitfinexAP": results['DeepcoinBP_BitfinexAP'],
        "DeepcoinBP_BingXAP": results['DeepcoinBP_BingXAP'],
        "DeepcoinBP_OrangeXAP": results['DeepcoinBP_OrangeXAP'],
        "DeepcoinBP_BitvenusAP": results['DeepcoinBP_BitvenusAP'],
        "DeepcoinBP_BiconomyAP": results['DeepcoinBP_BiconomyAP'],
        "DeepcoinBP_XTAP": results['DeepcoinBP_XTAP'],
        "DeepcoinBP_BitflyerAP": results['DeepcoinBP_BitflyerAP'],
        "DeepcoinBP_CoinWAP": results['DeepcoinBP_CoinWAP'],
        "DeepcoinBP_ToobitAP": results['DeepcoinBP_ToobitAP'],
        "DeepcoinBP_TapBitAP": results['DeepcoinBP_TapBitAP'],

        "BitfinexBP_BinanceAP": results['BitfinexBP_BinanceAP'],
        "BitfinexBP_BybitAP": results['BitfinexBP_BybitAP'],
        "BitfinexBP_OKXAP": results['BitfinexBP_OKXAP'],
        "BitfinexBP_UpbitAP": results['BitfinexBP_UpbitAP'],
        "BitfinexBP_KucoinAP": results['BitfinexBP_KucoinAP'],
        "BitfinexBP_BitgetAP": results['BitfinexBP_BitgetAP'],
        "BitfinexBP_BitstampAP": results['BitfinexBP_BitstampAP'],
        "BitfinexBP_GeminiAP": results['BitfinexBP_GeminiAP'],
        "BitfinexBP_KrakenAP": results['BitfinexBP_KrakenAP'],
        "BitfinexBP_GateioAP": results['BitfinexBP_Gate.ioAP'],
        "BitfinexBP_HTXAP": results['BitfinexBP_HTXAP'],
        "BitfinexBP_MEXCAP": results['BitfinexBP_MEXCAP'],
        "BitfinexBP_LbankAP": results['BitfinexBP_LbankAP'],
        "BitfinexBP_BitmartAP": results['BitfinexBP_BitmartAP'],
        "BitfinexBP_DeepcoinAP": results['BitfinexBP_DeepcoinAP'],
        "BitfinexBP_BitfinexAP": results['BitfinexBP_BitfinexAP'],
        "BitfinexBP_BingXAP": results['BitfinexBP_BingXAP'],
        "BitfinexBP_OrangeXAP": results['BitfinexBP_OrangeXAP'],
        "BitfinexBP_BitvenusAP": results['BitfinexBP_BitvenusAP'],
        "BitfinexBP_BiconomyAP": results['BitfinexBP_BiconomyAP'],
        "BitfinexBP_XTAP": results['BitfinexBP_XTAP'],
        "BitfinexBP_BitflyerAP": results['BitfinexBP_BitflyerAP'],
        "BitfinexBP_CoinWAP": results['BitfinexBP_CoinWAP'],
        "BitfinexBP_ToobitAP": results['BitfinexBP_ToobitAP'],
        "BitfinexBP_TapBitAP": results['BitfinexBP_TapBitAP'],

        "BingXBP_BinanceAP": results['BingXBP_BinanceAP'],
        "BingXBP_BybitAP": results['BingXBP_BybitAP'],
        "BingXBP_OKXAP": results['BingXBP_OKXAP'],
        "BingXBP_UpbitAP": results['BingXBP_UpbitAP'],
        "BingXBP_KucoinAP": results['BingXBP_KucoinAP'],
        "BingXBP_BitgetAP": results['BingXBP_BitgetAP'],
        "BingXBP_BitstampAP": results['BingXBP_BitstampAP'],
        "BingXBP_GeminiAP": results['BingXBP_GeminiAP'],
        "BingXBP_KrakenAP": results['BingXBP_KrakenAP'],
        "BingXBP_GateioAP": results['BingXBP_Gate.ioAP'],
        "BingXBP_HTXAP": results['BingXBP_HTXAP'],
        "BingXBP_MEXCAP": results['BingXBP_MEXCAP'],
        "BingXBP_LbankAP": results['BingXBP_LbankAP'],
        "BingXBP_BitmartAP": results['BingXBP_BitmartAP'],
        "BingXBP_DeepcoinAP": results['BingXBP_DeepcoinAP'],
        "BingXBP_BitfinexAP": results['BingXBP_BitfinexAP'],
        "BingXBP_BingXAP": results['BingXBP_BingXAP'],
        "BingXBP_OrangeXAP": results['BingXBP_OrangeXAP'],
        "BingXBP_BitvenusAP": results['BingXBP_BitvenusAP'],
        "BingXBP_BiconomyAP": results['BingXBP_BiconomyAP'],
        "BingXBP_XTAP": results['BingXBP_XTAP'],
        "BingXBP_BitflyerAP": results['BingXBP_BitflyerAP'],
        "BingXBP_CoinWAP": results['BingXBP_CoinWAP'],
        "BingXBP_ToobitAP": results['BingXBP_ToobitAP'],
        "BingXBP_TapBitAP": results['BingXBP_TapBitAP'],

        "OrangeXBP_BinanceAP": results['OrangeXBP_BinanceAP'],
        "OrangeXBP_BybitAP": results['OrangeXBP_BybitAP'],
        "OrangeXBP_OKXAP": results['OrangeXBP_OKXAP'],
        "OrangeXBP_UpbitAP": results['OrangeXBP_UpbitAP'],
        "OrangeXBP_KucoinAP": results['OrangeXBP_KucoinAP'],
        "OrangeXBP_BitgetAP": results['OrangeXBP_BitgetAP'],
        "OrangeXBP_BitstampAP": results['OrangeXBP_BitstampAP'],
        "OrangeXBP_GeminiAP": results['OrangeXBP_GeminiAP'],
        "OrangeXBP_KrakenAP": results['OrangeXBP_KrakenAP'],
        "OrangeXBP_GateioAP": results['OrangeXBP_Gate.ioAP'],
        "OrangeXBP_HTXAP": results['OrangeXBP_HTXAP'],
        "OrangeXBP_MEXCAP": results['OrangeXBP_MEXCAP'],
        "OrangeXBP_LbankAP": results['OrangeXBP_LbankAP'],
        "OrangeXBP_BitmartAP": results['OrangeXBP_BitmartAP'],
        "OrangeXBP_DeepcoinAP": results['OrangeXBP_DeepcoinAP'],
        "OrangeXBP_BitfinexAP": results['OrangeXBP_BitfinexAP'],
        "OrangeXBP_BingXAP": results['OrangeXBP_BingXAP'],
        "OrangeXBP_OrangeXAP": results['OrangeXBP_OrangeXAP'],
        "OrangeXBP_BitvenusAP": results['OrangeXBP_BitvenusAP'],
        "OrangeXBP_BiconomyAP": results['OrangeXBP_BiconomyAP'],
        "OrangeXBP_XTAP": results['OrangeXBP_XTAP'],
        "OrangeXBP_BitflyerAP": results['OrangeXBP_BitflyerAP'],
        "OrangeXBP_CoinWAP": results['OrangeXBP_CoinWAP'],
        "OrangeXBP_ToobitAP": results['OrangeXBP_ToobitAP'],
        "OrangeXBP_TapBitAP": results['OrangeXBP_TapBitAP'],

        "BitvenusBP_BinanceAP": results['BitvenusBP_BinanceAP'],
        "BitvenusBP_BybitAP": results['BitvenusBP_BybitAP'],
        "BitvenusBP_OKXAP": results['BitvenusBP_OKXAP'],
        "BitvenusBP_UpbitAP": results['BitvenusBP_UpbitAP'],
        "BitvenusBP_KucoinAP": results['BitvenusBP_KucoinAP'],
        "BitvenusBP_BitgetAP": results['BitvenusBP_BitgetAP'],
        "BitvenusBP_BitstampAP": results['BitvenusBP_BitstampAP'],
        "BitvenusBP_GeminiAP": results['BitvenusBP_GeminiAP'],
        "BitvenusBP_KrakenAP": results['BitvenusBP_KrakenAP'],
        "BitvenusBP_GateioAP": results['BitvenusBP_Gate.ioAP'],
        "BitvenusBP_HTXAP": results['BitvenusBP_HTXAP'],
        "BitvenusBP_MEXCAP": results['BitvenusBP_MEXCAP'],
        "BitvenusBP_LbankAP": results['BitvenusBP_LbankAP'],
        "BitvenusBP_BitmartAP": results['BitvenusBP_BitmartAP'],
        "BitvenusBP_DeepcoinAP": results['BitvenusBP_DeepcoinAP'],
        "BitvenusBP_BitfinexAP": results['BitvenusBP_BitfinexAP'],
        "BitvenusBP_BingXAP": results['BitvenusBP_BingXAP'],
        "BitvenusBP_OrangeXAP": results['BitvenusBP_OrangeXAP'],
        "BitvenusBP_BitvenusAP": results['BitvenusBP_BitvenusAP'],
        "BitvenusBP_BiconomyAP": results['BitvenusBP_BiconomyAP'],
        "BitvenusBP_XTAP": results['BitvenusBP_XTAP'],
        "BitvenusBP_BitflyerAP": results['BitvenusBP_BitflyerAP'],
        "BitvenusBP_CoinWAP": results['BitvenusBP_CoinWAP'],
        "BitvenusBP_ToobitAP": results['BitvenusBP_ToobitAP'],
        "BitvenusBP_TapBitAP": results['BitvenusBP_TapBitAP'],

        "BiconomyBP_BinanceAP": results['BiconomyBP_BinanceAP'],
        "BiconomyBP_BybitAP": results['BiconomyBP_BybitAP'],
        "BiconomyBP_OKXAP": results['BiconomyBP_OKXAP'],
        "BiconomyBP_UpbitAP": results['BiconomyBP_UpbitAP'],
        "BiconomyBP_KucoinAP": results['BiconomyBP_KucoinAP'],
        "BiconomyBP_BitgetAP": results['BiconomyBP_BitgetAP'],
        "BiconomyBP_BitstampAP": results['BiconomyBP_BitstampAP'],
        "BiconomyBP_GeminiAP": results['BiconomyBP_GeminiAP'],
        "BiconomyBP_KrakenAP": results['BiconomyBP_KrakenAP'],
        "BiconomyBP_GateioAP": results['BiconomyBP_Gate.ioAP'],
        "BiconomyBP_HTXAP": results['BiconomyBP_HTXAP'],
        "BiconomyBP_MEXCAP": results['BiconomyBP_MEXCAP'],
        "BiconomyBP_LbankAP": results['BiconomyBP_LbankAP'],
        "BiconomyBP_BitmartAP": results['BiconomyBP_BitmartAP'],
        "BiconomyBP_DeepcoinAP": results['BiconomyBP_DeepcoinAP'],
        "BiconomyBP_BitfinexAP": results['BiconomyBP_BitfinexAP'],
        "BiconomyBP_BingXAP": results['BiconomyBP_BingXAP'],
        "BiconomyBP_OrangeXAP": results['BiconomyBP_OrangeXAP'],
        "BiconomyBP_BitvenusAP": results['BiconomyBP_BitvenusAP'],
        "BiconomyBP_BiconomyAP": results['BiconomyBP_BiconomyAP'],
        "BiconomyBP_XTAP": results['BiconomyBP_XTAP'],
        "BiconomyBP_BitflyerAP": results['BiconomyBP_BitflyerAP'],
        "BiconomyBP_CoinWAP": results['BiconomyBP_CoinWAP'],
        "BiconomyBP_ToobitAP": results['BiconomyBP_ToobitAP'],
        "BiconomyBP_TapBitAP": results['BiconomyBP_TapBitAP'],

        "XTBP_BinanceAP": results['XTBP_BinanceAP'],
        "XTBP_BybitAP": results['XTBP_BybitAP'],
        "XTBP_OKXAP": results['XTBP_OKXAP'],
        "XTBP_UpbitAP": results['XTBP_UpbitAP'],
        "XTBP_KucoinAP": results['XTBP_KucoinAP'],
        "XTBP_BitgetAP": results['XTBP_BitgetAP'],
        "XTBP_BitstampAP": results['XTBP_BitstampAP'],
        "XTBP_GeminiAP": results['XTBP_GeminiAP'],
        "XTBP_KrakenAP": results['XTBP_KrakenAP'],
        "XTBP_GateioAP": results['XTBP_Gate.ioAP'],
        "XTBP_HTXAP": results['XTBP_HTXAP'],
        "XTBP_MEXCAP": results['XTBP_MEXCAP'],
        "XTBP_LbankAP": results['XTBP_LbankAP'],
        "XTBP_BitmartAP": results['XTBP_BitmartAP'],
        "XTBP_DeepcoinAP": results['XTBP_DeepcoinAP'],
        "XTBP_BitfinexAP": results['XTBP_BitfinexAP'],
        "XTBP_BingXAP": results['XTBP_BingXAP'],
        "XTBP_OrangeXAP": results['XTBP_OrangeXAP'],
        "XTBP_BitvenusAP": results['XTBP_BitvenusAP'],
        "XTBP_BiconomyAP": results['XTBP_BiconomyAP'],
        "XTBP_XTAP": results['XTBP_XTAP'],
        "XTBP_BitflyerAP": results['XTBP_BitflyerAP'],
        "XTBP_CoinWAP": results['XTBP_CoinWAP'],
        "XTBP_ToobitAP": results['XTBP_ToobitAP'],
        "XTBP_TapBitAP": results['XTBP_TapBitAP'],

        "BitflyerBP_BinanceAP": results['BitflyerBP_BinanceAP'],
        "BitflyerBP_BybitAP": results['BitflyerBP_BybitAP'],
        "BitflyerBP_OKXAP": results['BitflyerBP_OKXAP'],
        "BitflyerBP_UpbitAP": results['BitflyerBP_UpbitAP'],
        "BitflyerBP_KucoinAP": results['BitflyerBP_KucoinAP'],
        "BitflyerBP_BitgetAP": results['BitflyerBP_BitgetAP'],
        "BitflyerBP_BitstampAP": results['BitflyerBP_BitstampAP'],
        "BitflyerBP_GeminiAP": results['BitflyerBP_GeminiAP'],
        "BitflyerBP_KrakenAP": results['BitflyerBP_KrakenAP'],
        "BitflyerBP_GateioAP": results['BitflyerBP_Gate.ioAP'],
        "BitflyerBP_HTXAP": results['BitflyerBP_HTXAP'],
        "BitflyerBP_MEXCAP": results['BitflyerBP_MEXCAP'],
        "BitflyerBP_LbankAP": results['BitflyerBP_LbankAP'],
        "BitflyerBP_BitmartAP": results['BitflyerBP_BitmartAP'],
        "BitflyerBP_DeepcoinAP": results['BitflyerBP_DeepcoinAP'],
        "BitflyerBP_BitfinexAP": results['BitflyerBP_BitfinexAP'],
        "BitflyerBP_BingXAP": results['BitflyerBP_BingXAP'],
        "BitflyerBP_OrangeXAP": results['BitflyerBP_OrangeXAP'],
        "BitflyerBP_BitvenusAP": results['BitflyerBP_BitvenusAP'],
        "BitflyerBP_BiconomyAP": results['BitflyerBP_BiconomyAP'],
        "BitflyerBP_XTAP": results['BitflyerBP_XTAP'],
        "BitflyerBP_BitflyerAP": results['BitflyerBP_BitflyerAP'],
        "BitflyerBP_CoinWAP": results['BitflyerBP_CoinWAP'],
        "BitflyerBP_ToobitAP": results['BitflyerBP_ToobitAP'],
        "BitflyerBP_TapBitAP": results['BitflyerBP_TapBitAP'],

        # CoinWBP
        "CoinWBP_BinanceAP": results['CoinWBP_BinanceAP'],
        "CoinWBP_BybitAP": results['CoinWBP_BybitAP'],
        "CoinWBP_OKXAP": results['CoinWBP_OKXAP'],
        "CoinWBP_UpbitAP": results['CoinWBP_UpbitAP'],
        "CoinWBP_KucoinAP": results['CoinWBP_KucoinAP'],
        "CoinWBP_BitgetAP": results['CoinWBP_BitgetAP'],
        "CoinWBP_BitstampAP": results['CoinWBP_BitstampAP'],
        "CoinWBP_GeminiAP": results['CoinWBP_GeminiAP'],
        "CoinWBP_KrakenAP": results['CoinWBP_KrakenAP'],
        "CoinWBP_GateioAP": results['CoinWBP_Gate.ioAP'],
        "CoinWBP_HTXAP": results['CoinWBP_HTXAP'],
        "CoinWBP_MEXCAP": results['CoinWBP_MEXCAP'],
        "CoinWBP_LbankAP": results['CoinWBP_LbankAP'],
        "CoinWBP_BitmartAP": results['CoinWBP_BitmartAP'],
        "CoinWBP_DeepcoinAP": results['CoinWBP_DeepcoinAP'],
        "CoinWBP_BitfinexAP": results['CoinWBP_BitfinexAP'],
        "CoinWBP_BingXAP": results['CoinWBP_BingXAP'],
        "CoinWBP_OrangeXAP": results['CoinWBP_OrangeXAP'],
        "CoinWBP_BitvenusAP": results['CoinWBP_BitvenusAP'],
        "CoinWBP_BiconomyAP": results['CoinWBP_BiconomyAP'],
        "CoinWBP_XTAP": results['CoinWBP_XTAP'],
        "CoinWBP_BitflyerAP": results['CoinWBP_BitflyerAP'],
        "CoinWBP_CoinWAP": results['CoinWBP_CoinWAP'],
        "CoinWBP_ToobitAP": results['CoinWBP_ToobitAP'],
        "CoinWBP_TapBitAP": results['CoinWBP_TapBitAP'],

        # ToobitBP
        "ToobitBP_BinanceAP": results['ToobitBP_BinanceAP'],
        "ToobitBP_BybitAP": results['ToobitBP_BybitAP'],
        "ToobitBP_OKXAP": results['ToobitBP_OKXAP'],
        "ToobitBP_UpbitAP": results['ToobitBP_UpbitAP'],
        "ToobitBP_KucoinAP": results['ToobitBP_KucoinAP'],
        "ToobitBP_BitgetAP": results['ToobitBP_BitgetAP'],
        "ToobitBP_BitstampAP": results['ToobitBP_BitstampAP'],
        "ToobitBP_GeminiAP": results['ToobitBP_GeminiAP'],
        "ToobitBP_KrakenAP": results['ToobitBP_KrakenAP'],
        "ToobitBP_GateioAP": results['ToobitBP_Gate.ioAP'],
        "ToobitBP_HTXAP": results['ToobitBP_HTXAP'],
        "ToobitBP_MEXCAP": results['ToobitBP_MEXCAP'],
        "ToobitBP_LbankAP": results['ToobitBP_LbankAP'],
        "ToobitBP_BitmartAP": results['ToobitBP_BitmartAP'],
        "ToobitBP_DeepcoinAP": results['ToobitBP_DeepcoinAP'],
        "ToobitBP_BitfinexAP": results['ToobitBP_BitfinexAP'],
        "ToobitBP_BingXAP": results['ToobitBP_BingXAP'],
        "ToobitBP_OrangeXAP": results['ToobitBP_OrangeXAP'],
        "ToobitBP_BitvenusAP": results['ToobitBP_BitvenusAP'],
        "ToobitBP_BiconomyAP": results['ToobitBP_BiconomyAP'],
        "ToobitBP_XTAP": results['ToobitBP_XTAP'],
        "ToobitBP_BitflyerAP": results['ToobitBP_BitflyerAP'],
        "ToobitBP_CoinWAP": results['ToobitBP_CoinWAP'],
        "ToobitBP_ToobitAP": results['ToobitBP_ToobitAP'],
        "ToobitBP_TapBitAP": results['ToobitBP_TapBitAP'],

        # TapBitBP
        "TapBitBP_BinanceAP": results['TapBitBP_BinanceAP'],
        "TapBitBP_BybitAP": results['TapBitBP_BybitAP'],
        "TapBitBP_OKXAP": results['TapBitBP_OKXAP'],
        "TapBitBP_UpbitAP": results['TapBitBP_UpbitAP'],
        "TapBitBP_KucoinAP": results['TapBitBP_KucoinAP'],
        "TapBitBP_BitgetAP": results['TapBitBP_BitgetAP'],
        "TapBitBP_BitstampAP": results['TapBitBP_BitstampAP'],
        "TapBitBP_GeminiAP": results['TapBitBP_GeminiAP'],
        "TapBitBP_KrakenAP": results['TapBitBP_KrakenAP'],
        "TapBitBP_GateioAP": results['TapBitBP_Gate.ioAP'],
        "TapBitBP_HTXAP": results['TapBitBP_HTXAP'],
        "TapBitBP_MEXCAP": results['TapBitBP_MEXCAP'],
        "TapBitBP_LbankAP": results['TapBitBP_LbankAP'],
        "TapBitBP_BitmartAP": results['TapBitBP_BitmartAP'],
        "TapBitBP_DeepcoinAP": results['TapBitBP_DeepcoinAP'],
        "TapBitBP_BitfinexAP": results['TapBitBP_BitfinexAP'],
        "TapBitBP_BingXAP": results['TapBitBP_BingXAP'],
        "TapBitBP_OrangeXAP": results['TapBitBP_OrangeXAP'],
        "TapBitBP_BitvenusAP": results['TapBitBP_BitvenusAP'],
        "TapBitBP_BiconomyAP": results['TapBitBP_BiconomyAP'],
        "TapBitBP_XTAP": results['TapBitBP_XTAP'],
        "TapBitBP_BitflyerAP": results['TapBitBP_BitflyerAP'],
        "TapBitBP_CoinWAP": results['TapBitBP_CoinWAP'],
        "TapBitBP_ToobitAP": results['TapBitBP_ToobitAP'],
        "TapBitBP_TapBitAP": results['TapBitBP_TapBitAP'],
    }



    # end=time.time()
    # processingtime=end-start
    # print(processingtime)