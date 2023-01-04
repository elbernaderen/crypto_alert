import sys
import pandas as pd
import datetime
import time
from bina.bina import store_ohlcv
import telegram
from tools.tools import RSI, macd
import yaml

######################################################################################################



def mensajero(dato):

    config = yaml.load(open("ignore/telconfig.yml"), Loader = yaml.FullLoader)

    api_key = config["api_key"]
    user_id = config["user_id"]

    bot = telegram.Bot(token = api_key)
    t = f'Bot on'
    bot.send_message(chat_id = user_id, text = t)

    # The relative strength index (RSI) is a momentum indicator
    # used in technical analysis that measures the magnitude 
    # of recent price changes to evaluate overbought or oversold 
    # conditions in the price of a stock or other asset 

    rsi_compare = int(dato.rsi)

    # a will allow us know if the volume of the candels is "a" times bigger than the mean volume
    # of the previus candels

    # name of the Crypto-currency to analyze

    name = dato.simbolo

    macdAlerta = dato.macd

    valorAlerta = dato.valor



    # The time interval must be seconds, so here we convert hour, day or minutes in seconds

    inter_ = 60 * 5
    hours = 150

    # interval_ will save the interval value, and inter_ will be changing in the while loop.

    interval_ = inter_  

    # Generate the  x-axis list to analize the slope with linear regression from cero to rows

    

    while True: 
        # The signal finder is activated, and it will keep working
        # according to the interval choosed

        inter_ = interval_

        # To make an analysis and determine if we have to buy or just wait, 
        # we need to download several seconds before the last candle, 
        # so the variable tt will be the start date of the data to download


        hour = datetime.timedelta(hours = hours)
        hour_ = datetime.datetime.utcnow()
        tt = hour_ - hour
    
        # If at the moment of download the historical data, 
        # the internet is gone, the program will fail. 
        # So we add an Exception 

        try:
            kk = store_ohlcv(
                symbol = name, 
                interval = "5m",
                start_date = tt, 
                name = "messenger"
            )
        except ConnectionError:

            # If the internet is gone, we'll wait 60 seconds, and'll try again

            time.sleep(60)

            inter_ -= 60

            print("check your internet connection\n")

            kk = store_ohlcv(
                symbol = name, 
                interval = "5m",
                start_date = tt, 
                name = "messenger"
            )

        # wait to download the csv file

        time.sleep(30)
        inter_ -= 30
        # Every time that pass the interval of established time,
        #  the csv file with the data is download in the "messenger" directory, 
        # and this last file will replace the previous one and a DataFrame will be created

        file = pd.read_csv(f"messenger/{name}_5m_messenger.csv")

        # Then, the df must be edited and the RSI and macd columns must be appended

        # rsi is a list with each candel RSI value

        rsi = RSI(file["close"])

        # Here the RSI list is added to the dataframe file

        file["rsi"] = rsi

        # The macd function receives a DataFrame and add to it the
        # macd, macd_h and macd_s columns

        file = macd(file)

        # Here we delete the first 95 columns because the firts RSI values are 
        # erroneous

        file.drop(index=file.index[:95], axis=0, inplace=True)

        # Reset the index after the first 95 rows are been deleted

        file = file.reset_index()

        # Generate a list to analize the slope with linear regression whit the close values



        # The slope of the candels is calculated



        # generate a list with every volume value of the rows



        # calculate the mean value of the volume list


        # Here we call the function make_prediction that receive a DataFrame
        #  and return a one row df with the technical indicators of n = rows candles.

        # Here we calculate the prediction using the model rfc_1 and the one row DataFrame new,
        # where the columns date and close are dropped

    
        
        # Here we apply the filter diffined before. 
        # Then, if the data fit the filter and 
        # the response of the predictor is bigger than 0,
        #  the bot sends a message by Telegram with:
        #  PRICE 
        # TAKEPROFIT 
        # STOPLOSS 
        # ZERO LOSS PRICE 
        # DATE

        if (
            coef_1 > 0
            and slope < -0.01
            and (
                file["volume"][len(file) - 1] > vol_prom * a
                or file["volume"][len(file) - 2] > vol_prom * a
            )
            and file["rsi"][len(file) - 1] < rsi_compare
        ):
            coef = coef_1
            t = f'{name} \n BUY: {float(new["close"])} \n TAKEPROFIT: {float(new["close"])*(1+coef)} \n STOPLOSS: {float(new["close"])*(1-.005)} \n cero: {float(new["close"])*(1+0.0015)} \n {datetime.datetime.now()} '
            print(t)
            bot.send_message(chat_id=user_id, text=t)

        # If the price or the values don't fit the filter, 
        # a message is sent through Telegram to wait until the next analysis
        else:
            t = f"{name}  \n don't buy, wait {inter_}"
            print(t)

        time.sleep(inter_)

######################################################################################################

######################################################################################################

