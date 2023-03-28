from bytebank import Funcionario
#acima importamos a Class Funcionario de bytebank.py

#E agora vamos criar/estanciar um objeto da Class Funcionario
#o funcionario Lucas
#Setamos a String 'Lucas Carvalho' como o nome do funcionario, 2000 como o ano de nascimento
#e o salario inicial dele de 1000 reais

lucas = Funcionario('Lucas Carvalho','13/03/2000',1000)

#agora vamos printar para visualizar Lucas
#e funcionou Funcionario(Lucas Carvalho, 2000, 1000)

#Agora iremos testar o metodo idade para isso fazemos
# e funcionou o metodo nos retornou a idade 23
#estamos em 2023 ele nasceu em 2000 logo ele tem 23 anos
# porem a data de nascimento deveria tbm pegar o mes e o dia do nascimento
# se agente pensar bem essa regra de negocio ta meio estranha
#pq o funcionario precisa informar a data de nascimento dele que nao eh so composta pelo ano
#e sim por ano, mes e dia
#entao se aqui em main alterarmos isso colocarmos tudo como uma String '13/03/2000' ao invez de so 2000 e rodar de novo
#boom o codigo quebra gerando o erro abaixo

# , line 21, in idade
#     return ano_atual - int(self._data_nascimento)ValueError: invalid literal for int() with base 10: '13/03/2000'

#tem um erro nesse codigo a regra de negocio ta falha ta quebrada precisamos concertar isso 


#mas se pensarmos bem essa regra de negocios ta meio estranha o que o funcionario
#precisa informar e a data de nascimento dele que nao e composta so pelo ano tem o dia e o mes tambem
#Depois de alterarmos o metodo def idade na classe bytebank.py e retestarmos aqui na main ela funcionou
#retornou a idade de Lucas bacaninha sem problemas

#so que o nosso codigo de teste ta muito jogado e o chefe pediu para nos transformarmos esse codigo 
#em um teste automatizado mesmo vamos trabalhar nisso entao
#Comentando o codigo do teste anterior
# print(lucas)
# print(lucas.idade())
#vamos criar o novo teste agora

#vamos criar o metodo def test_idade() e vou instanciar um novo funcionario dentro do metodo

def teste_idade():
    funcionario_teste = Funcionario('Teste','13/03/2000',1111)
    print(f'Teste = {funcionario_teste.idade()}')

#acabei de criar um teste automatizado logo acima
#e com isso ja temos um teste automatizado que esta dentro do metodo acima como podemos ver
# poderiamos inclusive implementar outras logicas mirabolantes para testar o codigo da Dominique#

teste_idade()
#chamando o teste para testar
#Teste = 23 Funcionou!
    
















#Ambientes virtuais

# A utilização de ambientes virtuais (virtual environments) é algo recorrente no mundo de desenvolvimento
# de projetos com Python. Por quais motivos os ambientes virtuais são uma boa prática no desenvolvimento com a linguagem?

# 1 - A prática da criação do arquivo requirements.txt dentro de ambientes virtuais acaba por dinamizar a replicação de
# um mesmo ambiente de projeto em máquinas diferentes.

# Qualquer pessoa pode replicar um projeto que contém um arquivo requirements.txt, para isso, basta criar um ambiente virtual
# e utilizar o comando pip install -r requirements.txt. Todos os pacotes que constam dentro do arquivo serão instalados.
# Para saber mais sobre ambientes virtuais acesse esse artigo:
# Ambientes virtuais em Python -> https://www.alura.com.br/artigos/ambientes-virtuais-em-python


#2 - O uso de ambientes virtuais acaba evitando conflitos entre versões de pacotes utilizados em diferentes projetos
#O ambiente virtual acaba proporcionando um ambiente isolado de qualquer outro projeto sendo desenvolvido.
# Dessa forma, cada ambiente pode ter uma versão instalado do mesmo pacote/biblioteca/extensão sem haver conflitos.