from Conta import *
from abc import ABC, abstractclassmethod, abstractproperty
class Transacao(ABC):
    @property
    @abstractproperty    
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    valor:float
    def __init__(self, valor) -> None:
        super(Transacao, self).__init__()
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionarTransacao(self)

class Deposito(Transacao):
    valor:float
    def __init__(self, valor) -> None:
        super(Transacao, self).__init__()
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionarTransacao(self)