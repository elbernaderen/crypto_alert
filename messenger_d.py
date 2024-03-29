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

    name = dato.simbolo

    interval = dato.intervalo

        # The signal finder is activated, and it will keep working
        # according to the interval choosed

    hour = datetime.timedelta(hours = 400)
    hour_ = datetime.datetime.utcnow()
    tt = hour_ - hour
    
    try:
        store_ohlcv(
            symbol = name, 
            interval = interval,
            start_date = tt, 
            name = "messenger"
            )
    except ConnectionError:

            # If the internet is gone, we'll wait 60 seconds, and'll try again

        time.sleep(60)

        print("check your internet connection\n")

        store_ohlcv(
            symbol = name, 
            interval = interval,
            start_date = tt, 
            name = "messenger"
            )
        # Every time that pass the interval of established time,
        #  the csv file with the data is download in the "messenger" directory, 
        # and this last file will replace the previous one and a DataFrame will be created

    file = pd.read_csv(f"messenger/{name}_{interval}_messenger.csv")
    file = file_edit(file)

        

    valores_real = Valores_reales(file)

    t = f'{name} \n Valor: {valores_real.valor[2]} \n RSI: {valores_real.rsi[0]} \n Macd: {valores_real.macd[0]} \n {datetime.datetime.now()} '
    print(t)

    if itera_valores(dato, valores_real):

        bot.send_message(chat_id = user_id, text = t)

    else:

        t = f"{name}  \n Sin alertas, esperar 5 minutos"
        print(t)

    return
######################################################################################################

######################################################################################################

class Valores_reales:
    def __init__(self,row):

        self.valor = [row["high"].iloc[-1], row["low"].iloc[-1],row["close"].iloc[-1]]

        # agregué lista para poder usar  max y min en compare

        self.rsi = [row["rsi"].iloc[-1], row["rsi"].iloc[-1]]

        self.macd = [row["macd"].iloc[-1], row["macd"].iloc[-1]]



def compare(signo , e_alerta, e_real):
    if signo == ">=":
        return max(e_real) >= e_alerta
    else:
        return min(e_real) < e_alerta

def itera_valores(dato, valores_real):

    for i in dato.agrega_elemento(valores_real):

        if len(i[0]) > 0:

            if compare(i[1],float(i[0]),i[2]):

                continue

            else:

                dato.quita_elemento()

                return False

    dato.quita_elemento()

    return True

def file_edit(file):

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
    
    return file
