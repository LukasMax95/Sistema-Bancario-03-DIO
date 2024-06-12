from Cliente import Cliente
from Historico import Historico


class Conta:
    saldo:float
    numaro:int
    agencia:str
    cliente:Cliente
    historico:Historico
    def __init__(self, numero:int, cliente:Cliente) -> None:
        self._saldo = 0
        self._numaro = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numaro
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    @classmethod
    def nova_conta(self, cliente: Cliente, numero:int):
        return cls(numero, cliente)
    
    def sacar(self, valor:float):
        saldo = self._saldo
        excedeuSaldo = valor > saldo
        valorNegativo = valor < 0
        if excedeuSaldo:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Saldo Insuficiente")
        elif valorNegativo:
            for i in range(0,3):
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                      + "Valor Inválido! por favor, digite um valor positivo!")
                print(f"Tentativa {(i+1)}")
                try:
                    valor = float(input())
                    if valor > 0:
                        return self.sacar(valor)
                except:
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                          "Erro! Valor Inválido! por favor, digite um número!")
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Valor Inválido! Três tentativas malsucedidas!")
        else:
            print("\nOperação Bem-Sucedida\n")
            self._saldo -= valor
            print("\nSaque Realizado com Sucesso!\n")
            return True
        return False

    def depositar(self, valor:float):
        valorNegativo = valor < 0

        if valorNegativo:
            for i in range(0,3):
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                      + "Valor Inválido! por favor, digite um valor positivo!")
                print(f"Tentativa {(i+1)}")
                try:
                    valor = float(input())
                    if valor > 0:
                        return self.sacar(valor)
                except:
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                          "Erro! Valor Inválido! por favor, digite um número!")
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Valor Inválido! Três tentativas malsucedidas!")
        else:
            print("\nOperação Bem-Sucedida\n")
            self._saldo += valor
            print("\nSaque Realizado com Sucesso!\n")
            return True
        return False

class ContaCorrente(Conta):
    linite:float
    limite_saques:int
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def novoDia(self, limite = 500, limite_saques = 3):
        self.limite = limite
        self.limite_saques = limite_saques
    
    
    def sacar(self, valor: float):
        #numero_saques = len[transacao for transacao in self.historico.transacoes 
        #                    if transacao["Tipo"] == Saque.__name__]
        saldo = self._saldo
        excedeuSaldo = valor > saldo
        valorNegativo = valor < 0
        if self.limite_saques == 0:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Limite diário de Saques excedido!")
        elif excedeuSaldo:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Saldo Insuficiente")
        elif valorNegativo:
            for i in range(0,3):
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                      + "Valor Inválido! por favor, digite um valor positivo!")
                print(f"Tentativa {(i+1)}")
                try:
                    valor = float(input())
                    if valor > 0:
                        return self.sacar(valor)
                except:
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                          "Erro! Valor Inválido! por favor, digite um número!")
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" 
                  + "Falha na Operação!\n"
                  + "Erro! Valor Inválido! Três tentativas malsucedidas!")
        else:
            print("\nOperação Bem-Sucedida\n")
            super().sacar(valor)
            self.limite_saques -= 1
            print("\nSaque Realizado com Sucesso!\n")
            return True
        return False

    def __str__(self) -> str:
        return f'''\
        Agência:\t{self.agencia}
        C/C:\t\t{self._numaro}
        Conta:\t{self.cliente.nome}
        '''