import sqlite3

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def adicionar_clientes(self):
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()        
        
        cur.execute('''CREATE TABLE IF NOT EXISTS clientes
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL)''')
        
        # Insere o cliente
        cur.execute('INSERT INTO clientes (nome, telefone) VALUES (?, ?)', 
                    (self.nome, self.telefone))
        con.commit()
        con.close()
        
    @staticmethod
    def listar_clientes():
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM clientes')
        nomes = cur.fetchall()
        for nome in nomes:
            print(nome)

    @staticmethod            
    def atualizar_cliente():
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()
        Cliente.listar_clientes()
        nome_antigo = input("Digite o nome do cliente que deseja atualizar: ")
        novo_telefone = input("Digite o novo telefone: ")
        cur.execute('UPDATE clientes SET telefone = ? WHERE nome = ?', 
        (novo_telefone, nome_antigo))
        con.commit()
        con.close()
        
    @staticmethod
    def remover_cliente():
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()
        Cliente.listar_clientes()
        nome_remover = input("Digite o nome do cliente que deseja remover: ")
        cur.execute('DELETE FROM clientes WHERE nome = ?', (nome_remover,))
        print('Cliente removido com sucesso!')       
        con.commit()
        con.close()       

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def adicionar_produto(self):
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()        
        
        cur.execute('''CREATE TABLE IF NOT EXISTS produtos
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco TEXT NOT NULL)''')
        
        # Insere o cliente
        cur.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', 
                    (self.nome, self.preco))
        con.commit()
        con.close()
        
    @staticmethod
    def listar_produtos():
        con = sqlite3.connect('projeto_1.db')
        cur= con.cursor()
        cur.execute('SELECT * FROM produtos')
        nomes = cur.fetchall()
        for nome in nomes:
            print(nome)
        con.close()

    @staticmethod
    def atualizar_produto():
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()
        Produto.listar_produtos()
        nome_antigo = input("Digite o nome do produto que deseja atualizar: ")
        novo_nome = input("Digite o novo nome: ")
        novo_preco = input('Digite o novo preço: ')
        cur.execute('UPDATE produtos SET nome = ?, preco = ? WHERE nome = ?', 
            (novo_nome, novo_preco, nome_antigo))
        con.commit()
        con.close()

    @staticmethod
    def remover_produto():
        con = sqlite3.connect('projeto_1.db')
        cur = con.cursor()
        Produto.listar_produtos()
        nome_remover = input("Digite o nome do produto que deseja remover: ")
        cur.execute('DELETE FROM produtos WHERE nome = ?', (nome_remover,))
        print(f'Produto removido com sucesso!')      
        con.commit()
        con.close()

        
def menu():
    while True:
        print("Cliente | Produto | Sair")
        escolha = input("Escolha: ").strip().capitalize()

        if escolha == "Cliente":
            print('Adicionar | Listar | Atualizar | Remover | Voltar')
            escolha_produto = input("Escolha: ").strip().capitalize()
            if escolha_produto == 'Adicionar':
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                cliente = Cliente(nome, telefone)
                cliente.adicionar_clientes()
            elif escolha_produto == 'Listar':
                Cliente.listar_clientes()
            elif escolha_produto == 'Atualizar':
                Cliente.atualizar_cliente()
            elif escolha_produto == 'Remover':
                Cliente.remover_cliente()
            elif escolha_produto == 'Voltar':
                continue
        
        elif escolha == "Produto":
            print ('Adicionar | Listar | Atualizar | Remover | Voltar')            
            escolha_produto = input("Escolha: ").strip().capitalize()
            if escolha_produto == 'Adicionar':
                nome = input("Nome: ")
                preco = input("Preço: ")
                produto = Produto(nome, preco)
                produto.adicionar_produto()
            elif escolha_produto == 'Listar':
                Produto.listar_produtos()
            elif escolha_produto == 'Atualizar':
                Produto.atualizar_produto()
            elif escolha_produto == 'Remover':
                Produto.remover_produto()
            elif escolha_produto == 'Voltar':
                continue
        
        elif escolha == "Sair":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")           
    
if __name__ == "__main__":
    menu()

    
    
    

     
    