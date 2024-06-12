from Conta import *
from Transacao import *
from datetime import datetime

class Cliente:
    endereco:str
    contas:list
    def __init__(self, endereco:str):
        self.endereco = endereco
        self.contas = []
    def realisarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionarConta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    cpf:str
    nome:str
    data_nascimento:datetime.date
    def __init__(self, nome, data_nascimento, cpf, endereco) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf