import textwrap
from Conta import ContaCorrente
from Cliente import PessoaFisica
from Transacao import Deposito, Saque

class Banco:
    #cliente:Cliente
    #conta:ContaCorrente
    menu = """
================================
[d]   depositar
[s]   sacar
[e]   extrato
[nc]  nova conta
[lc]  listar contas
[nu]  novo usuario
[q]   sair
================================
"""
    def __init__(self):
        self.clientes = []
        self.contas = []
    
    def filtrar_cliente(self, cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    def recuperar_contaCliente(self, cliente):
        if not cliente.contas:
            print("Erro! Cliente não possui conta!")
            return
        return cliente.contas[0]

    def criar_conta(self, numero_conta, clientes, contas):
        cpf = input("CPF do cliente:")
        cliente = self.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Erro! Cliente Não ENcontrado!\n===> Procedimento Encerrado!")
            return
        
        conta = ContaCorrente(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
    
    def criar_cliente(self, clientes):
        cpf = input("CPF do cliente:")
        cliente = self.filtrar_cliente(cpf, clientes)

        if cliente:
            print("Erro! Cliente já existe!")
            return
        nome = input("Informe seu nome completo:")
        data_nascimento = input("Informe sua data de nascimento:")
        endereco = input("Informe o endereço: logadouro, nro, bairro, cidade/sigla_estado")

        cliente = PessoaFisica(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            endereco=endereco)
        clientes.append(cliente)
        print("Cliente criado com sucesso")

    def listar_contas(self, contas):
        for conta in contas:
            print("*"*100)
            print(textwrap.dedent(str(conta)))

    def sacar(self, clientes): 
        cpf = input("CPF do cliente:")
        cliente = self.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Erro! Cliente Não ENcontrado!")
            return
        valor = float(input("Informe o valor a ser sacado:"))
        transacao = Saque(valor=valor)
        conta = self.recuperar_contaCliente(cliente)
        if not conta:
            return
        
        cliente.realisarTransacao(conta, transacao)

    def depositar(self, clientes): 
        cpf = input("CPF do cliente:")
        cliente = self.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Erro! Cliente Não ENcontrado!")
            return
        valor = float(input("Informe o valor a ser depositado:"))
        transacao = Deposito(valor=valor)
        conta = self.recuperar_contaCliente(cliente)
        if not conta:
            return
        
        cliente.realisarTransacao(conta, transacao)

    def exibir_extrato(self, cliente):
        cpf = input("CPF do cliente:")
        cliente = self.filtrar_cliente(cpf, self.clientes)

        if not cliente:
            print("Erro! Cliente Não ENcontrado!")
            return
        conta = self.recuperar_contaCliente(cliente)
        if not conta:
            return
        transacoes = conta.historico.transacoes
        extrato = "Não foram realizadas transações." if not transacoes else "Obtendo Transações..."
        if extrato == "Obtendo Transações...":
            extrato+="\n"
            for transacao in transacoes:
                extrato += f"\n{transacao['Tipo']}:\n\tR${transacao['Valor']:.2f}"

        print(f'''
=================Extrato===============
{extrato}
Saldo: \tR${conta.saldo:.2f}
======================================= 
              ''')

    def choice(self):
        "Entrando no Banco Sistema 03"
        while True:
            print(self.menu)
            opcao = input("==> ")
            if opcao == "d":
                self.depositar(self.clientes)
            elif opcao == "s":
                self.sacar(self.clientes)
            elif opcao == "e":
                self.exibir_extrato(self.clientes)
            elif opcao == "nu":
                self.criar_cliente(self.clientes)
            elif opcao == "nc":
                numero_conta = len(self.contas) + 1
                self.criar_conta(numero_conta, self.clientes, self.contas)
            elif opcao == "lc":
                self.listar_contas(self.contas)
            elif opcao == "q":
                break
            else:
                print("Erro! Comando Inválido!")