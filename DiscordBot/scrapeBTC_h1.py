import ccxt
from datetime import datetime, timedelta


exchange = ccxt.binance({
    'enableRateLimit': True,
    "apiKey": 'JGBGxWzxiLq6rFS9CJV5ObTyxigtgEyE9WCswxdAHIjPxJJMOi3X8xSCRIXb4sDc',
    "secret": 'TRNJGZz0vfhfASh1KjqZEbc6kb5DxfNwt0PGfecx4p8vuzl3b8sgcXrRiB28rUEm',
})

def getBTC():
    # datetime object containing current date and time
    now = datetime.now() - timedelta(minutes=1)
    timeNow = now.strftime("%d/%m/%Y %H:%M:%S")
    timestampNow = int(datetime.strptime(timeNow, "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
    responseNow = exchange.fetch_ohlcv('BTC/USDT', '1m', timestampNow, 1)

    oneHour = datetime.now() - timedelta(hours=1)
    timeOne = oneHour.strftime("%d/%m/%Y %H:%M:%S")
    timestampOne = int(datetime.strptime(timeOne, "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
    responseOne = exchange.fetch_ohlcv('BTC/USDT', '1h', timestampOne, 1)
    
    twoHours = datetime.now() - timedelta(hours=2)
    timeTwo = twoHours.strftime("%d/%m/%Y %H:%M:%S")
    timestampTwo = int(datetime.strptime(timeTwo, "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
    resposeTwo = exchange.fetch_ohlcv('BTC/USDT', '1h', timestampTwo, 1)

    return [responseNow[0][4], responseOne[0][4], resposeTwo[0][4]]


def calcChange(close, closeBefore):
    increase = float(close) - float(closeBefore)
    change = increase / (float(closeBefore) * 100)   #Calculate change
    return change

def calcTendency(close, closeBefore):
    tendency = int()
    if float(close) - float(closeBefore) > 0:
        tendency = 1
    else:
        tendency = 0
        
    return tendency

def returnFeatures():
    change = calcChange(getBTC()[0], getBTC()[1])
    tendency = calcTendency(getBTC()[0], getBTC()[2])
    return [change, tendency]