#Gaberiela Almeida e Nicolly Moura


class Moto:
    def __init__(self,modelo,cor):
        self.__modelo = modelo
        self.__cor = cor 

    def get_modelo (self):
        return self.__modelo
    
    def set_modelo(self,modelo):
        self.__modelo = modelo
    
    def exibir_infoemaçõe(self):
        print(f"modelo: {self.__modelo}, cor: {self.__cor}")
    print("1:Pipeline: e uma sequencia de etapas organizdas para processar dados, executar tarefas, 2:encapsulado é ucultar, quando tem dois _ na frente da variavel, não encapsulado é visivel, 3: nesse modelo, nós devemos seguir passo a passo sem pular nada, tudo tem que ser documentado ")

#class sem encapsulamento

class Pessoa: 
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def exibir_informações(self):
        print (f"nome: {self.nome}, idade: {self.idade}")

    def main():
        modelo_Moto = input("digite o modelo da moto:")
        cor_Moto = input("digite a cor da moto:")

        Moto.set_modelo(f"novo_modelo")
        Moto.exibir_informação()

        nome_pessoa = input("digite seu nome:")

        idade_pessoa = (nome_pessoa, idade_pessoa)

        Pessoa.exibir_informações()
        
    main()




         

        





