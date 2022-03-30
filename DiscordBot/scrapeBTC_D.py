import investpy
from datetime import datetime, timedelta


def get_today():
    today = datetime.strftime(datetime.now(), '%d/%m/%Y')
    yesterday = datetime.strftime(datetime.now() - timedelta(2), '%d/%m/%Y')

  
    data = investpy.get_crypto_historical_data(crypto='bitcoin',
                                            from_date=str(yesterday),
                                            to_date=str(today))
   
 
 
    #Calculate change
    increase = data["Close"][2] - data["Close"][1]

    change = increase / (data["Close"][0] * 100)
    change = "".join(list(str(change))[0:5])

    #Calculate tendency
    tendency = int()
    if data["Close"][2] - data["Close"][1] > 0:
        tendency = 1
    else:
        tendency = 0
        
    return [change, tendency]

