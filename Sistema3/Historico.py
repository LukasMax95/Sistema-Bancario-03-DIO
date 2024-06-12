import Transacao
from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionarTransacao(self, transacao:Transacao):
        self._transacoes.append({
            "Tipo": transacao.__class__.__name__,
            "Valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })