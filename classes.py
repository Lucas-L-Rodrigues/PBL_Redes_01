#from dataclasses import dataclass
from datetime import date

class Passagem:
    def __init__(self, dataCompra, reserva, cidadeSaida, cidadeChegada, poltrona, estaPago, estaCancelado):
        self.dataCompra    = dataCompra
        self.reserva       = reserva
        self.cidadeSaida   = cidadeSaida
        self.cidadeChegada = cidadeChegada
        self.poltrona      = poltrona
        self.estaPago      = estaPago
        self.estaCancelado = estaCancelado
    
    def realizarCompra(self):
        
        return
    def realizarReserva(self):
        
        return
    def realizarPagamento(self):
        
        return
    def realizarCancelamento(self):
        
        return

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.passagens = []


    def adicionarPassagem(self, passagem):
        self.passagens.append(passagem)
