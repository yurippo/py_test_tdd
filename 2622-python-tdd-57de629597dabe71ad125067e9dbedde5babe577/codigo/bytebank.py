from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property

    def salario(self):
        return self._salario

#um metodo que captura a data de nascimento de um funcionario e pega o ano atual
# pra calcular a idade do funcionario que nao esta funcionando bem
#pq data de nascimento tem ano mes e dia nao somente ano set testamos com uma String por exemplo
#'13/03/2000' o codigo quebra e pra resolver isso agora vamos recriar esse metodo e fazer com que ele se torne funcional
#novamente primeiro passo sera quebrar a data de nascimento em 3 uma lista com 3 itens o primerio item sendo o dia
#o segundo item sendo o mes e o terceiro dia sendo o ano o novo metodo sera reescrito abaixo

    # def idade(self):
    #     ano_atual = date.today().year
    #     return ano_atual - int(self._data_nascimento)

    def idade(self):
        #o split e um metodo do Python pra formatar Strings com o metodo vamos quebrar a String em determinados pontos
        #e retornar com isso uma lista com as partes quebradas dessa String vamos passar no split('/') o caracter usado para
        #fazer a quebra no caso '/' e com isso vamos ter uma lista com dia mes e ano
        data_nascimento_quebrada = self._data_nascimento.split('/')
        #agora vamos criar uma nova variavel ano_nascimento e vamos igualar essa variavel ao ultimo item da minha lista
        # que e a data_nascimento_quebrada e abro o colchete e coloco o [-1] que sempre vai pegar o ultimo item da lista
        #no nosso caso o ano
        ano_nascimento = data_nascimento_quebrada[-1]

        ano_atual = date.today().year
        # e no return vamos colocar ano_atual - int(self.ano_quebrado)
        return ano_atual - int(ano_nascimento)
        #essas alteracoes devem fazer a funcao funcionar e fazer rodar o nosso codigo la no main
        #vamos testar  de novo

    

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

#Funcao __str__ que devolve as informacoes completas do objeto quando agente cria

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
        

    #Historia da Dominique

    #A Dominique e uma desenvolvedora iniciante e ela trabalha nessa empresa que e o Bytebank
    #que e uma FinTech um banco digital que foca em technologia mas ao mesmo tempo financas
    #e o chefe dela deu um projetinho para ela desenvolver um projeto que vai fazer parte de um 
    #projeto muito maior ali dentro da empresa

    #O Projeto Dela
    #Desenvolver uma classe que contem as informacoes dos funcionarios do Bytebank algo bem importante
    #e a Dominique ja desenvolveu um codigo agente vai revisar esse codigo daqui a pouco mais antes
    #ela pediu a nossa ajuda ajuda-la a decifrar alguns termos outros devs mais experientes falam
    #sobre testes, TDD, Testes Unitarios o chefe dela fala vamos desenvolver alguma coisa utilizando testes
    #a metodologia do TDD e ela nao sabe o que eh isso e nesse curso vamos ajudar ela, revisar os projetos dela

    #vamos iniciar um ambiente virtual para nao haver conflitos entre nossos projetos Python
    #primerio venv faz mencao ao ambiente virtual e segundo venv e o nome que quero dar ao ambiente virtual
    #Spode ser o que eu quiser e existe essa convencao venv

    #python3 -m venv venv

    #podemos ver agora o nosso novo diretorio venv

    #mas ainda nao ta funcionando entao precisamos ativar esse ambiente virtual
    #source venv/bin/activate para windows apenas activate
    #scripts execution estava desativado tive que run powershell como admin e mudar policy para
    # Set-ExecutionPolicy unrestricted depois A e reolvido
    #ai rodei  venv\Scripts\activate e funcionou venv finalmente ativada
    #agora que ja criamos um ambiente virtual podemos testar o codigo da Dominique
    # ai dentro da pasta codigo vamos criar o arquivo main.py e dentro de main vamos criar 
    # um objeto para testar a class Funcionario de bytebank.py


