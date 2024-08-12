from models import Pessoa

def menu():
    while True:
        print("1. Adicionar Pessoa")
        print("2. Listar Pessoas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            idade = input("Idade: ")
            pessoa = Pessoa(nome, idade)
            pessoa.save()
            print("Pessoa adicionada com sucesso!")
        elif escolha == '2':
            pessoas = Pessoa.get_all()
            for pessoa in pessoas:
                print(f"Nome: {pessoa[1]}, Idade: {pessoa[2]}")
        elif escolha == '3':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
