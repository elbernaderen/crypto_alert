from messenger_d import mensajero
import time

class Valores_alerta:
    def __init__(self,simbolo,valor,rsi,macd,value_valor,value_rsi,value_macd):
        self.simbolo = simbolo
        self.valor = [valor,value_valor]
        self.rsi = [rsi,value_rsi]
        self.macd = [macd,value_macd]

    def elemento(self,valores_real):
        self.valor.append(valores_real.valor)
        self.rsi.append(valores_real.rsi)
        self.macd.append(valores_real.macd)

        return self.valor,self.rsi, self.macd

    def quita_elemento(self):
        self.valor.pop()
        self.rsi.pop()
        self.macd.pop()



def enviar_datos(alert):
    global running
    running = False
    alert = alert
    while True:
        mensajero(alert)
        
        for i in range (60*5):
            time.sleep(1)
            
            if running:
                print("detenido")
                return


def detener():
    global running
    running = True
    print("detener")