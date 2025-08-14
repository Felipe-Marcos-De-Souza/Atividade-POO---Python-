# Atividade 1: Classe Livro
class Livro:
    def __init__(self): # Aqui terá as váriaveis iniciais da classe livro
        self.titulo = ""
        self.autor = ""
        self.numero_paginas = 0
        self.pagina_atual = 0
    
    def abrir_livro(self): # Método para abrir o livro que começa na página 1
        self.pagina_atual = 1 
    
    def ler_paginas(self): # Método para perguntar quantas páginas o usuário leu
        numero = int(input("Quantas páginas você leu? "))
        if numero == 0:
            print("Você não leu nenhuma página!")
        else:
            self.pagina_atual += numero
            print("Número de páginas salvo!") 

    def exibir_progresso(self): # Ele exibe uma mensagem falando do livro e quantidade de páginas lidas
        print(f"Você leu {self.pagina_atual} páginas do livro '{self.titulo}'")
        
    def informacoes_livro(self): # Extra: Pergunta informações como o título o autor e quantidade de páginas no livro e guarda em váriaveis 
        self.titulo = input("Qual é o título do livro? ")
        self.autor = input("Qual o autor da obra? ")
        self.numero_paginas = int(input("Quantas páginas tem o livro? "))


# Atividade 2: Classe ContaBancaria
class ContaBancaria:
    def __init__(self): # Aqui terá as váriaveis iniciais da classe ContaBancaria
        self.titular = ""
        self.saldo = 0.0
        self.numero_conta = ""
        
    def depositar(self): # Deposita um valor dado pelo usuário e soma ao saldo
        deposito = float(input("Escreva quanto deseja depositar: ")) 
        self.saldo += deposito
        print(f"O valor de R${deposito:.2f} foi depositado na sua conta!")
    
    def sacar(self): # Saca um determinado valor do saldo do usuário
        saque = float(input("Escreva quanto deseja sacar: ")) 
        if saque > self.saldo: # Se o valor pedido pelo cliente for maior que o saldo dá como insuficiente
            print("Saldo insuficiente!")
        else:
            self.saldo -= saque # De resto retira o saque
            print(f"O valor sacado foi de R${saque:.2f}")
        
    def consultar_saldo(self): # Exibe as informações do saldo disponível na conta dele.
        print(f"Há R${self.saldo:.2f} na sua conta")
        
    def exibir_extrato(self): # Mostra as informações da conta
        print("----------------- Conta atual -----------------")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Número da conta: {self.numero_conta}")
        print("----------------------------------------------")
    
    def criar_conta(self): # Cria uma conta para o cliente do banco, depositando as informações.
        self.titular = input("Nome do titular: ")
        self.numero_conta = input("Número da conta: ")
        self.saldo = float(input("Saldo inicial: "))
        


# Menu principal
class Main:
    def __init__(self):
        self.livro = Livro()
        self.conta = ContaBancaria()
        
    def menu_inicial(self): # O menu inicial com a opção da atividade 1 ou 2 
        print("\n----------------- Menu inicial -----------------")
        print("1 - Classe Livro")
        print("2 - Conta Bancária")
        print("------------------------------------------------")
        
        opcao_geral = int(input("Escolha uma opção: ")) # Se o usuário clicar 1 ele vai para o menu do livro e 2 para o menu da Conta bancária
        if opcao_geral == 1:
            self.menu_livro()
        elif opcao_geral == 2:   
            self.menu_conta()
        else:
            print("Opção inválida!")

    def menu_livro(self): # Menu livro tem: Cadastro, Abrir o livro, ler páginas e exibir o progresso
        print("\n----------------- Menu: Livro -----------------")
        print("1 - Cadastrar livro")
        print("2 - Abrir o livro")
        print("3 - Ler páginas")
        print("4 - Exibir progresso")
        print("------------------------------------------------")
        opcao_livro = int(input("Escolha uma opção: "))
        match opcao_livro:
            case 1:
                self.livro.informacoes_livro()
            case 2:
                self.livro.abrir_livro()
            case 3:
                self.livro.ler_paginas()
            case 4:
                self.livro.exibir_progresso()
            case _:
                print("Opção inválida!")

    def menu_conta(self): #Menu Conta tem: Criar conta, depositar e sacar valores, consultar saldo e exibir o extrato do cliente
        print("\n----------- Menu: Conta Bancária -----------")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar saldo")
        print("5 - Exibir extrato")
        print("--------------------------------------------")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                self.conta.criar_conta()
            case 2:
                self.conta.depositar()
            case 3:
                self.conta.sacar()
            case 4:
                self.conta.consultar_saldo()
            case 5:
                self.conta.exibir_extrato()
            case _:
                print("Opção inválida!")

# Ponto de entrada: a forma que a IA deu de fazer rodar a classe menu que eu criei...
if __name__ == "__main__":
    projeto = Main()
    while True:
        projeto.menu_inicial()
        continuar = input("Deseja voltar ao menu? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o programa...")
            break
