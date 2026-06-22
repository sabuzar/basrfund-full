import threading
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
# from models import checker
from modelsValueDifference import checker
from BCHUSDTAPIRequest import main



async def main1():
    start = time.time()

    results = await main()

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

    BinanceBP_BinanceAP = results['BinanceBP_BinanceAP']
    BinanceBP_BybitAP = results['BinanceBP_BybitAP']
    BinanceBP_OKXAP = results['BinanceBP_OKXAP']
    BinanceBP_UpbitAP = results['BinanceBP_UpbitAP']
    BinanceBP_KucoinAP = results['BinanceBP_KucoinAP']
    BinanceBP_BitgetAP = results['BinanceBP_BitgetAP']
    BinanceBP_BitstampAP = results['BinanceBP_BitstampAP']
    BinanceBP_GeminiAP = results['BinanceBP_GeminiAP']
    BinanceBP_KrakenAP = results['BinanceBP_KrakenAP']
    BinanceBP_GateioAP = results['BinanceBP_GateioAP']
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
    BybitBP_GateioAP = results['BybitBP_GateioAP']
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
    OKXBP_GateioAP = results['BinanceBP_GateioAP']
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
    UpbitBP_GateioAP = results['UpbitBP_GateioAP']
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
    KucoinBP_GateioAP = results['BinanceBP_GateioAP']
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
    BitgetBP_GateioAP = results['BitgetBP_GateioAP']
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
    BitstampBP_GateioAP = results['BitstampBP_GateioAP']
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
    GeminiBP_GateioAP = results['GeminiBP_GateioAP']
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
    KrakenBP_GateioAP = results['KrakenBP_GateioAP']
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

    GateioBP_BinanceAP = results['GateioBP_BinanceAP']
    GateioBP_BybitAP = results['GateioBP_BybitAP']
    GateioBP_OKXAP = results['GateioBP_OKXAP']
    GateioBP_UpbitAP = results['GateioBP_UpbitAP']
    GateioBP_KucoinAP = results['GateioBP_KucoinAP']
    GateioBP_BitgetAP = results['GateioBP_BitgetAP']
    GateioBP_BitstampAP = results['GateioBP_BitstampAP']
    GateioBP_GeminiAP = results['GateioBP_GeminiAP']
    GateioBP_KrakenAP = results['GateioBP_KrakenAP']
    GateioBP_GateioAP = results['GateioBP_GateioAP']
    GateioBP_HTXAP = results['GateioBP_HTXAP']
    GateioBP_MEXCAP = results['GateioBP_MEXCAP']
    GateioBP_LbankAP = results['GateioBP_LbankAP']
    GateioBP_BitmartAP = results['GateioBP_BitmartAP']
    GateioBP_DeepcoinAP = results['GateioBP_DeepcoinAP']
    GateioBP_BitfinexAP = results['GateioBP_BitfinexAP']
    GateioBP_BingXAP = results['GateioBP_BingXAP']
    GateioBP_OrangeXAP = results['GateioBP_OrangeXAP']
    GateioBP_BitvenusAP = results['GateioBP_BitvenusAP']
    GateioBP_BiconomyAP = results['GateioBP_BiconomyAP']
    GateioBP_XTAP = results['GateioBP_XTAP']
    GateioBP_BitflyerAP = results['GateioBP_BitflyerAP']
    GateioBP_CoinWAP = results['GateioBP_CoinWAP']
    GateioBP_ToobitAP = results['GateioBP_ToobitAP']
    GateioBP_TapBitAP = results['GateioBP_TapBitAP']

    HTXBP_BinanceAP = results['HTXBP_BinanceAP']
    HTXBP_BybitAP = results['HTXBP_BybitAP']
    HTXBP_OKXAP = results['HTXBP_OKXAP']
    HTXBP_UpbitAP = results['HTXBP_UpbitAP']
    HTXBP_KucoinAP = results['HTXBP_KucoinAP']
    HTXBP_BitgetAP = results['HTXBP_BitgetAP']
    HTXBP_BitstampAP = results['HTXBP_BitstampAP']
    HTXBP_GeminiAP = results['HTXBP_GeminiAP']
    HTXBP_KrakenAP = results['HTXBP_KrakenAP']
    HTXBP_GateioAP = results['HTXBP_GateioAP']
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
    MEXCBP_GateioAP = results['BinanceBP_GateioAP']
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
    LbankBP_GateioAP = results['LbankBP_GateioAP']
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
    BitmartBP_GateioAP = results['BitmartBP_GateioAP']
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
    DeepcoinBP_GateioAP = results['DeepcoinBP_GateioAP']
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
    BitfinexBP_GateioAP = results['BitfinexBP_GateioAP']
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
    BingXBP_GateioAP = results['BingXBP_GateioAP']
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
    OrangeXBP_GateioAP = results['OrangeXBP_GateioAP']
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
    BitvenusBP_GateioAP = results['BitvenusBP_GateioAP']
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
    BiconomyBP_GateioAP = results['BiconomyBP_GateioAP']
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
    XTBP_GateioAP = results['XTBP_GateioAP']
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
    BitflyerBP_GateioAP = results['BitflyerBP_GateioAP']
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
    CoinWBP_GateioAP = results['CoinWBP_GateioAP']
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
    ToobitBP_GateioAP = results['ToobitBP_GateioAP']
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
    TapBitBP_GateioAP = results['TapBitBP_GateioAP']
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

    end = time.time()
    processingtime = (end - start) * 1_000_000


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

    # table50len=Table_lenchecker('Bucket99BTC')
    # table100to200len = Table_lenchecker('Bucket100to200BTC')
    # table200to300len = Table_lenchecker('Bucket200to300BTC')
    # table300to400len = Table_lenchecker('Bucket300to400BTC')
    # table500pluslen = Table_lenchecker('Bucket500plusBTC')
    # print(table50len,table100to200len,table200to300len,table300to400len,table500pluslen)


while True:

    asyncio.run(main1())
