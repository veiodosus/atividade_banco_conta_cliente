class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def contas(self):
        return self.__contas
    
    def adicionar(self, conta):
        if type(conta) == Conta:
            self.__contas.append(conta)
            print('Conta adicionada!')
        else:
            print('Erro, o parâmetro deve ser da classe Conta!')
    
    def remover(self, numero):
        for n in self.__contas:
            if numero == n.numero:
                self.__contas.remove(n)
                return 'Conta removida!'
        else:
            print('Numero não consta nos registros!')
        
    def saldo_total(self):
        saldo = 0
        for n in self.__contas:
            saldo += n.saldo
        return f'{saldo:.2f}'
    
    def __str__(self):
        return f'Banco {self.__nome}. Saldo total: {self.saldo_total()}.'

class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'{valor} reais depositados na conta!')

    def sacar(self, valor):
        if not valor > self.__saldo:
            self.__saldo -= valor
            print(f'{valor} reais sacados da conta!')
    
    def __str__(self) -> str:
        return f'N: {self.__numero}. Saldo: {self.__saldo}.'

class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    def __str__(self) -> str:
        return f'CPF: {self.__cpf}. NOME: {self.__nome}.'
    

banco1 = Banco('Santander')
banco2 = Banco('Bradesco')
banco3 = Banco('Brasil')

cliente1 = Cliente(12312312312, 'Vinícius Silva Ribeiro')
cliente2 = Cliente(32132132132, 'Murilo da Silva')
cliente3 = Cliente(45645645645, 'Guilherme Ribeiro')

conta1 = Conta(123, cliente1)
conta2 = Conta(321, cliente1)
conta3 = Conta(456, cliente2)
conta4 = Conta(654, cliente2)
conta5 = Conta(789, cliente3)
conta6 = Conta(987, cliente3)

banco1.adicionar(conta1)
banco1.adicionar(conta2)
banco2.adicionar(conta3)
banco2.adicionar(conta4)
banco3.adicionar(conta5)
banco3.adicionar(conta6)
print('')
conta1.depositar(123)
conta2.depositar(123)
conta3.depositar(123)
conta4.depositar(123)
conta5.depositar(123)
conta6.depositar(123)
print('')
print(conta1)
print(conta2)
print(conta3)
print(conta4)
print(conta5)
print(conta6)
print('')
conta1.sacar(10)
conta2.sacar(10)
conta3.sacar(10)
conta4.sacar(10)
conta5.sacar(10)
conta6.sacar(10)
print('')
print(conta1)
print(conta2)
print(conta3)
print(conta4)
print(conta5)
print(conta6)
print('')
print(banco1.saldo_total())
print(banco2.saldo_total())
print(banco3.saldo_total())
print('')
print(banco1)
print(banco2)
print(banco3)