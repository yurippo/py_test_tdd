from bytebank import Funcionario

#Segundo teste a ser realizado testando o metodo calcular_bonus()

ana = Funcionario('Ana','12/03/1997',100000000)

print(ana.calcular_bonus())

#Rodamos o novo metodo calcular_bonus() com a exception que nos criamos e ele nos retornou ela

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> & "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/venv/Scripts/python.exe" "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/pyfolder/codigo/main.py"
# Traceback (most recent call last):
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\pyfolder\codigo\main.py", line 7, in <module>
#     print(ana.calcular_bonus())
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\pyfolder\codigo\bytebank.py", line 68, in calcular_bonus
#     raise Exception('O salario e muito alto para receber um bonus') #here we created our exception
# Exception: O salario e muito alto para receber um bonus





#esse print aqui vai nos indicar um syntax error que e mostrado abaixo
#quando agente erra na propria linguagem

# print('evfvf'))

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> & "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/venv/Scripts/python.exe" "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/pyfolder/codigo/main.py"
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\pyfolder\codigo\main.py", line 9
#     print('evfvf'))
#                   ^
# SyntaxError: unmatched ')'

# um outro tipo de error que tambem podemos ter e por exemplo

#print(0/0)

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> & "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/venv/Scripts/python.exe" "c:/Users/marci/OneDrive/AREA DE TRABALHO 2022-01-10/py_test_tdd/pyfolder/codigo/main.py"
# Traceback (most recent call last):
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\pyfolder\codigo\main.py", line 22, in <module>
#     print(0/0)
# ZeroDivisionError: division by zero

# ZeroDivisionError: division by zero e um runtime error quando acontece um erro na logica do que agente ta fazendo
#uma exception um erro na logica de uma excecao alguma coisa que ta acontecendo e existe tambem uma forma
#da gente criar exceptions personalizadas que agente mesmo impoe e agente faz isso em varias linguagens de programacao
#e no python tbm nao eh diferente e existe muitas vantagens em fazer isso uma delas eh explicar o pq nao se pode fazer isso
# que esta se tentando fazer o famoso raise Exception















#Primeiro teste realizado

#acima importamos a Class Funcionario de bytebank.py

#E agora vamos criar/estanciar um objeto da Class Funcionario
#o funcionario Lucas
#Setamos a String 'Lucas Carvalho' como o nome do funcionario, 2000 como o ano de nascimento
#e o salario inicial dele de 1000 reais

# lucas = Funcionario('Lucas Carvalho','13/03/2000',1000)

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

# def teste_idade():
#     funcionario_teste = Funcionario('Teste','13/03/2000',1111)
#     print(f'Teste = {funcionario_teste.idade()}')
# #inclusive poderia testar outros cenarios tbm
#     funcionario_teste1 = Funcionario('Teste','13/03/1999',1111)
#     print(f'Teste = {funcionario_teste1.idade()}')
# #e agora vou criar uma outra situacao em que nao apenas o ano muda mas o mes tbm
#     funcionario_teste2 = Funcionario('Teste','01/12/1999',1111)
#     print(f'Teste = {funcionario_teste2.idade()}')
#Beleza os testes funcionaram o Python mostrou os resultados para nos mas o problema e que isso acaba ficando muito extenso
#quando nos queremos testar muitos scenarios fica estranho colocar isso direto em um arquivo para isso existe uma ferramenta que vai
#melhorar a construcoes dos nossos testes e essa ferramenta no caso se chama Pytest e vamos comecar ver isso mais a fundo

# Teste = 23
# Teste = 24
# Teste = 24




#acabei de criar um teste automatizado logo acima, um teste unitario ou unit test
#pq ele ta testando uma pequena parte do codigo da Dominique
#e com isso ja temos um teste automatizado que esta dentro do metodo acima como podemos ver
# poderiamos inclusive implementar outras logicas mirabolantes para testar o codigo da Dominique#

# teste_idade()
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

#Vamos instalar o Pytest para usa-lo no projeto

#pip install pytest==7.2.2

#Tambem rodamos o python.exe -m pip install --upgrade pip para atualizar o nosso pip

#agora vamos  rodar o comando pip freeze que e uma boa pratica esse comando retorna a lista de todos os pacotes
#que agente tem instalado no nosso ambiente virtual e no caso nos retornou

# attrs==22.2.0
# colorama==0.4.6
# exceptiongroup==1.1.1
# iniconfig==2.0.0
# packaging==23.0
# pluggy==1.0.0
# pytest==7.2.2
# tomli==2.0.1

#e tbm eh uma boa pratica agente criar uma pasta e um arquivo txt e ir colocando todas as coisas 
#que agente ta instalando
#e depois se uma pessoa quiser pegar o nosso projeto e reproduzir basta que ela pegue os pacotes desse txt
#entao rodamos  pip freeze > requirements.txt para criar o nosso arquivo txt com os pacotes que temos ate entao

#agora iremos organizar onde iremos colocar os nossos testes no nosso projeto que eh
#criado como tests para o pytest identificar como diretorio de testes e dentro
#do diretorio de testes famos criar o arquivo dunder init __init__.py (dunder significa usar underline underline no mundo python)
#precisamos disso pq esse diretorio de test eh um modulo e pra gente ter um modulo em python agente precisa de uma pasta
# ou seja um diretorio e dentro desse diretorio o arquivo dunder init __init__.py e isso vai fazer o Pytest reconhecer
#que aqui dentro vamos ter testes
#e o arquivo dunder init pode permanecer vazio por exemplo
#ai entao vamos criar o arquivo tests_bytebank.py no diretorio tests
#e finalmente dentro desse arquivo temos a nossa area que podemos comecar a fazer os nossos testes
#ai entao vamos levar o primeiro teste que criamos e traduzilo como ele ficara no Pytest


#Descricao da Instalacao do Pytest 

# Na última aula, criamos o arquivo main.py e desenvolvemos nosso primeiro teste automatizado,
#  elaborando alguns cenários para testar o método idade da classe Funcionario criada pela Dominique.
#  Os códigos funcionaram como esperado, entretanto, não é uma boa prática criarmos testes dessa forma.

# A maioria das linguagens de programação tem ferramentas e bibliotecas destinadas à criação de testes.
#  Para o Python, temos o Pytest, um framework especializado em testes. Antigamente, usava-se mais o unittest
#  para essa finalidade, mas o Pytest chegou para oferecer uma alternativa mais "pythônica". O primeiro release
#  dele foi em 2019 e até hoje ele é um dos principais frameworks de testes para Python.

# Uma das vantagens do Pytest é possuir múltiplos plugins, extensões. Temos um pacote de ferramentas inclusas
#  no Pytest para realizar testes dos mais variados tipos e personalizar nossa interação com o código.

# Além disso, esse framework é altamente escalável, comportando desde aplicações pequenas até projetos maiores,
#  com hierarquias complexas, diversos módulos e muitos diretórios.

# Não bastasse, a utilização do Pytest é muito simples. Com poucos comandos no terminal, conseguimos executar
#  todos os testes que queremos.

# Neste vídeo, prepararemos o ambiente para usar esse recuso. O primeiro passo é instalar o Pytest.
#  Abrindo o terminal, caso não estejamos no ambiente virtual, vamos ativá-lo com o comando source venv/bin/activate.
#  Em seguida, por meio do instalador de pacotes pip, instalaremos o Pytest na versão atual (7.1.2):

# pip install pytest==7.1.2COPIAR CÓDIGO
# Executando o comando pip freeze no terminal, receberemos uma lista de todos os pacotes instalados no nosso ambiente virtual.
#  É uma boa prática criarmos um arquivo .txt para reunir as informações de tudo que estamos instalando, para manter a organização
#  do nosso projeto. Posteriormente, se outra pessoa quiser reproduzi-lo, basta consultar esse documento.

# Portanto, vamos rodar o comando pip freeze > requirements.txt para gerar esse arquivo. Na sequência, podemos consultá-lo
#  na estrutura de pastas, no painel à esquerda, e verificar que o pytest==7.1.2 que instalamos há pouco já consta nessa lista.
#  À medida que instalarmos mais pacotes, atualizaremos esse documento.

# Com o Pytest instalado, vamos organizar o local onde colocaremos os testes. No painel à esquerda,
#  dentro do projeto bytebank-tdd, criaremos um diretório chamado tests. É essencial usar o nome tests
#  (com letras minúsculas, no plural e em inglês); do contrário, o Pytest pode não reconhecer que este é o diretório de testes!

# Dentro do diretório tests, criaremos um arquivo chamado __init__.py. No Python, quando colocamos um elemento
#  entre underlines (dois underlines no início e dois no final), chamamos de dunder. No caso do nosso arquivo, falamos "dunder init".

# O arquivo __init__.py é necessário porque o diretório tests é um módulo. Para considerarmos um módulo no Python,
#  é preciso ter um diretório e, dentro dele, um arquivo dunder init. É assim que o Pytest reconhece que esta é a pasta de testes. O arquivo __init__.py pode permanecer vazio.

# Dentro do diretório tests (nosso módulo de testes), criaremos outro arquivo, chamado tests_bytebank.py — este
#  será o documento em que faremos os testes.

# O ambiente está pronto! No próximo vídeo, vamos "traduzir" os testes que desenvolvemos no main.py para o
#  formato que ele teria com o Pytest.




