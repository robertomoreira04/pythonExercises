class Carro:
    numero_rodas = 4
    qtd_passageiros = 5

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def buzinar(self):
        print("Buzinando...")

carro = Carro()
carro.acelerar()
carro.frear()
carro.buzinar()

class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1994

uno = Uno()
uno.acelerar()
uno.frear()
print(uno.marca)