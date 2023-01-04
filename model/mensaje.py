from messenger_d import mensajero

class Valores_alerta:
    def __init__(self,simbolo,valor,rsi,macd,value_valor,value_rsi,value_macd):
        self.simbolo = simbolo
        self.valor = float(valor)
        self.rsi = float(rsi)
        self.macd = float(macd)
        self.value_valor = value_valor
        self.value_rsi = value_rsi
        self.value_macd = value_macd

def enviar_datos(alert):
    alert = alert
    print(alert.macd)
    mensajero(alert)