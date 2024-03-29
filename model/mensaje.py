from messenger_d import mensajero
import time

class Valores_alerta:
    def __init__(self,simbolo,valor,rsi,macd,value_valor,value_rsi,value_macd,value_intervalo):
        self.simbolo = simbolo.upper()
        self.valor = [valor,value_valor]
        self.rsi = [rsi,value_rsi]
        self.macd = [macd,value_macd]
        self.intervalo = value_intervalo

    def agrega_elemento(self,valores_real):
        self.valor.append(valores_real.valor)
        self.rsi.append(valores_real.rsi)
        self.macd.append(valores_real.macd)

        return self.valor, self.rsi, self.macd

    def quita_elemento(self):
        self.valor.pop()
        self.rsi.pop()
        self.macd.pop()



def enviar_datos(alert):
    global running
    running = False

    while True:
        mensajero(alert)
        
        for i in range (60*5):
            time.sleep(1)
            
            if running:
                return


def detener():
    global running
    running = True
