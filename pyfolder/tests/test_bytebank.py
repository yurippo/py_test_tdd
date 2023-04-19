from codigo.bytebank import Funcionario
class TestClass:
    #a good practice for the tests names is it be as much verdose as possible that means explaining everything
    #and now we're going to use a test methodology called GIVEN-WHEN-THEN and Agile Methodology to develop tests
    #Given(Context)...
    #When(Action)...
    #Then(End)...


    def test_when_age_receives_13_03_2000_should_return_23(self):        
        entry = '13/03/2000' #Given - Context
        expected = 23

        funcionario_teste = Funcionario('Test',entry,1111)
        
        result = funcionario_teste.idade() #When-action that will be to invoke the method

        assert result == expected #Then - that's the outcome of the test the end and result now my test is ready
         # the method assert from Pytest will determine if What I'm saying here is right or not


    def test_when_lastname__receives_Lucas_Carvalho_should_return_Carvalho(self):
        entry = 'Lucas Carvalho' #Given - Context
        expected = 'Carvalho'

        lucas = Funcionario(entry, '11/11/2000', 1111)
        result = lucas.sobrenome() #When-action that will be to invoke the method

        assert result == expected

#Agora vamos rodar o test com o comando pytest -v no terminal que nos retornou o resultado os 2 testes passaram

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> pytest -v
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.10.11, pytest-7.2.2, pluggy-1.0.0 -- C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd
# collected 2 items

# 2622-python-tdd-57de629597dabe71ad125067e9dbedde5babe577/tests/test_bytebank.py::TestClass::test_when_age_receives_13_03_2000_should_return_23 PASSED         [ 50%]
# 2622-python-tdd-57de629597dabe71ad125067e9dbedde5babe577/tests/test_bytebank.py::TestClass::test_when_lastname__receives_Lucas_Carvalho_should_return_Carvalho PASSED [100%]

# ======================================================================== 2 passed in 0.02s =========================================================================
# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> 


    def test_when_salary_reduction_receives_1000000_should_return_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

        #Now let's run the test on the terminal with pytest -v and see what happens

        # The test failed of course the method wasn't implemented yet result:

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> pytest -v
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.10.11, pytest-7.2.2, pluggy-1.0.0 -- C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd
# collected 3 items

# pyfolder/tests/test_bytebank.py::TestClass::test_when_age_receives_13_03_2000_should_return_23 PASSED                                                         [ 33%]
# pyfolder/tests/test_bytebank.py::TestClass::test_when_lastname__receives_Lucas_Carvalho_should_return_Carvalho PASSED                                         [ 66%]
# pyfolder/tests/test_bytebank.py::TestClass::test_when_salary_reduction_receives_1000000_should_return_90000 FAILED                                            [100%]

# ============================================================================= FAILURES =============================================================================
# ____________________________________________ TestClass.test_when_salary_reduction_receives_1000000_should_return_90000 _____________________________________________

# self = <tests.test_bytebank.TestClass object at 0x000001ED6889F880>

#     def test_when_salary_reduction_receives_1000000_should_return_90000(self):
#         entry_salary = 100000 #Given - Context
#         entry_name = 'Paulo Braganca'
#         expected = 90000

# >       funcionario_teste = Funcionario(entry_name,'Teste','11/11/2000',entry_salary)
# E       TypeError: Funcionario.__init__() takes 4 positional arguments but 5 were given

# pyfolder\tests\test_bytebank.py:52: TypeError
# ===================================================================== short test summary info ====================================================================== 
# FAILED pyfolder/tests/test_bytebank.py::TestClass::test_when_salary_reduction_receives_1000000_should_return_90000 - TypeError: Funcionario.__init__() takes 4 positional arguments but 5 were given
# =================================================================== 1 failed, 2 passed in 0.17s ==================================================================== 
# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> 


#Now let's test again after the new method was implemented in bytebank.py

# def decrescimo_salario(self):
#         sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
#         if self._salario >= 100000 and (self.sobrenome() in sobrenomes): #to verify if salary >= 100000 and lastname included in the lastname list
#             decrescimo = self._salario * 0.1
#             self._salario = self._salario - decrescimo


#Now let's run the test on the terminal again with pytest -v and see what happens after the method implementation (the tests finaly passed)

# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> pytest -v
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.10.11, pytest-7.2.2, pluggy-1.0.0 -- C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd\venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd
# collected 3 items

# pyfolder/tests/test_bytebank.py::TestClass::test_when_age_receives_13_03_2000_should_return_23 PASSED                                                         [ 33%] 
# pyfolder/tests/test_bytebank.py::TestClass::test_when_lastname__receives_Lucas_Carvalho_should_return_Carvalho PASSED                                         [ 66%] 
# pyfolder/tests/test_bytebank.py::TestClass::test_when_salary_reduction_receives_1000000_should_return_90000 PASSED                                            [100%] 

# ======================================================================== 3 passed in 0.05s ========================================================================= 
# (venv) PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_test_tdd> 









# Antes de "traduzir" o teste do main.py para como ele ficaria quando utilizamos o Pytest (o framework de testes do Python), vamos relembrar qual é o contexto de teste_idade e qual sua finalidade.

# Nosso objetivo é averiguar o bom funcionamento do método idade, que deve calcular a idade de um funcionario_teste, isto é, um objeto já instanciado com a data de nascimento igual a 13/03/2000.

# Vamos elaborar nosso teste no arquivo tests_bytebank.py, conforme o raciocínio demandado pelo Pytest. Primeiramente, vamos criar uma classe chamada TestClass. Essa é uma boa prática, pois mantém o projeto organizado. Imaginando que dispomos de um código extenso e que queremos testar diferentes partes dele, é interessante termos uma classe de testes para cada trecho específico a ser testado.

# Em seguida, daremos um nome ao método. Há dois pontos importantíssimos na criação de nomes de testes! O primeiro ponto é que, para o Pytest reconhecer o teste, a primeira palavra do nome do método deve ser test_.

# O segundo ponto diz respeito a uma boa prática: nomes de testes devem ser o mais verbosos possível. Na programação, "verboso" (ou verbose) significa explícito e minuciosamente explicado. Então, nosso método se chamará test_quando_idade_recebe_13_03_2000_deve_retornar_22:

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):COPIAR CÓDIGO
# Assim, o nome do nosso teste segue o padrão necessário: tem a palavra test_ no início e é extremamente verboso. Mais adiante, entenderemos por que esse nome explícito é tão importante.

# Agora, podemos começar efetivamente a escrever o nosso teste. Sabemos que vamos testar o método idade quando a data de nascimento é 13/03/2000, mas como começamos? Qual é o primeiro passo? O que devemos digitar na primeira linha do teste? Essas não são dúvidas triviais, elas ocorreram diversas vezes ao longo da história de testes e desenvolvimento de softwares. São perguntas tão comuns que, inclusive, foram criadas metodologias de como criar testes! A seguir, aprenderemos sobre uma delas.

# A Given-When-Then é uma metodologia ágil para desenvolvimento de testes. Given pode ser traduzido como "dado" (o verbo "dar" no particípio), no sentido de "Dado determinado contexto...". When significa "quando" e definirá a ação a ser testada. Then significa "então" e indicará o desfecho.

# Em resumo: dado determinado contexto, quando uma ação específica ocorrer, então acontecerá certo desfecho. Para elucidar esses conceitos, vejamos um exemplo.

# Vamos supor que guardei dinheiro na minha conta-corrente — este o contexto. Certo dia, precisei comprar uma blusa nova — esta é a ação. Como tenho dinheiro guardado, eu consigo comprar a blusa nova — este é o desfecho. Dado o contexto em que eu tenho dinheiro guardado, quando tento comprar uma blusa nova, (então) consigo realizar a transação.

# Na sequência, colocaremos essa metologia em prática no tests_bytebank.py!

# O nosso contexto é que temos um funcionário e precisamos inserir sua data de nascimento, que será a entrada:

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
#         entrada = '13/03/2000' # Given-Contexto

# Note que deixamos um comentário para nos guiar. Em seguida, colocaremos o resultado que esperamos receber:

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
#         entrada = '13/03/2000' # Given-Contexto
#         esperado = 22

# Antes de determinar a ação (when), vamos instanciar o objeto funcionario_teste. Seu nome será 'Teste'; 
# sua data de nascimento, entrada; e o salário, 1111. 
# Vale ressaltar que precisaremos importar a classe Funcionario no início do arquivo:

# from codigo.bytebank import Funcionario

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
#         entrada = '13/03/2000' # Given-Contexto
#         esperado = 22

#         funcionario_teste = Funcionario('Teste', entrada, 1111)

# O próximo passo é definir a ação que, no caso, será a invocação do método idade.
# Salvaremos o retorno em uma variável chamada resultado:

# from codigo.bytebank import Funcionario

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
#         entrada = '13/03/2000' # Given-Contexto
#         esperado = 22

#         funcionario_teste = Funcionario('Teste', entrada, 1111)
#         resultado = funcionario_teste.idade() # When-ação

# Por fim, definiremos o desfecho. 
# O método assert verificará se a expressão passada é verdadeira ou não,
# se resultado é igual ao valor esperado ou não:

# from codigo.bytebank import Funcionario

# class TestClass:
#     def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
#         entrada = '13/03/2000' # Given-Contexto
#         esperado = 22

#         funcionario_teste = Funcionario('Teste', entrada, 1111)
#         resultado = funcionario_teste.idade() # When-ação

#         assert resultado == esperado  # Then-desfecho

# Recapitulando:

# GIVEN — Contexto: entrada da data de nascimento
# WHEN — Ação: chamada do método idade
# THEN — Desfecho: verificação se resultado é igual ao esperado
# O teste está pronto!

# À esquerda do código, há uma seta verde ao lado de class TestClass, na linha 3. Vamos clicar nela e selecionar "Run" (ou usar o atalho "Ctrl + Shift + F10") para executar o teste.

# No terminal, leremos tests_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve retornar_22 PASSED [100% ] e saberemos que o teste passou. Também notaremos como é importante o nome do teste ser verboso, porque agora é fácil interpretar o resultado e discernir os acontecimentos.

# Existe outra forma de rodar o teste, basta abrir o terminal e executar pytest. No nosso caso, ao rodar esse comando, ocorrerá um problema e nenhum teste será rodado, porque deixamos passar propositalmente um erro. Aprendemos anteriormente que o nome do nosso diretório deve necessariamente ser tests. Da mesma maneria, também há um padrão para o nome do arquivo: ele deve começar com test_ (e não tests_, no plural). Esse erro serve para mostrar o quão importante são alguns detalhes, quando trabalhamos com Pytest.

# No painel à esquerda, clicaremos com o botão direito sobre o arquivo tests_bytebank.py e selecionaremos "Refactor > Rename...". Outra opção é selecionar o arquivo e usar o atalho "Ctrl + F6". Em seguida, vamos renomeá-lo para test_bytebank.py e pressionar o botão "Refactor", na parte inferior da caixa de diálogo.

# Uma vez renomeado, podemos executar o comando pytest novamente no terminal. Dessa vez, o teste será realizado com sucesso. No retorno, teremos tests/test_bytebank.py . — este ponto no final da linha significa que o teste passou.

# Outra alternativa é acrescentar a flag -v, de verbose, logo: pytest -v. Assim, receberemos um retorno mais detalhado sobre o resultado, parecido com o teste que executamos anteriormente, ao clicar na seta verde.

# Conseguimos transpor o teste de main.py para um formato que o Pytest compreende. Será que podemos utilizar a metodologia do Given-When-Then em outros contextos? Veremos mais sobre o assunto

# O Pytest é o framework de testes mais utilizado do mercado de desenvolvimento de software com Python.
# Ele facilita a construção de testes unitários, sendo altamente escalável e detentor de múltiplas ferramentas
# para facilitar o uso de metodologias de desenvolvimento de software voltadas a testes.

# Um outro nome muito utilizado ao se referir ao Pytest é Unittest, já que esse era o seu nome até a nova versão de 2009.

# A escrita verbosa de nomes para teste é um padrão que ultrapassa o próprio Python.
# Muitas linguagens de programação seguem essa boa prática, que diz que o nome do teste deve
# explicar da forma mais clara possível para que ele serve.

# Uma boa prática na utilização do Pytest é a criação de um módulo específico para testes, ou seja,
# um diretório denominado tests contendo um arquivo __init__.py

# Esse diretório irá conter todos os arquivos referentes aos testes da aplicação,
# sendo que a nomenclatura dos arquivos sempre deverá conter o prefixo test_.

# Arrange-Act-Assert
# Existe uma outra metodologia muito utilizada para a construção do raciocínio
# de funcionamento de testes chamada Arrange-Act-Assert ou simplesmente AAA.
# Essa metodologia também consiste em 3 etapas para a construção de um teste,
# análogas às etapas do Given-When-Then.

# Arrange: A tradução não literal seria algo como organizar.
# A organização, nesse caso, seria focada nos passos preliminares
# necessários para montar o contexto inicial do teste;
# Act: A tradução não literal seria algo como agir. Nesse caso seria a ação
# que parte dos passos organizados na primeira etapa e leva ao que vamos averiguar no final;
# Assert: A tradução não literal seria algo como averiguar. Nesse caso, averiguarmos que o desfecho
# trazido pela ação é realmente aquele que esperamos.

# Outro cenário para testar

# Já desenvolvemos nosso primeiro teste utilizando Pytest e, dessa maneira,
# esclarecemos algumas dúvidas mais cruciais da Dominique sobre como realizar testes no projeto dela por meio do PyCharm.

# Agora, o chefe dela anunciou uma nova feature que ele gostaria de implementar na classe Funcionario:
# um método que retorne o sobrenome dos funcionários. Então, vamos ajudar a Dominique. No arquivo bytebank.py,
# a partir da linha 23 (abaixo do método idade), criaremos um método chamado sobrenome.

# # código anterior omitido

# def sobrenome(self):
#     nome_completo = self.nome.strip()

# código posterior omitido

# Dessa forma, armazenaremos o nome completo da pessoa na variável nome_completo,
# sem espaços excedentes. Em seguida, vamos usar a mesma lógica que empregamos no método idade.
# Com o split, geraremos uma lista com todos os nomes da pessoa, pois queremos selecionar apenas o último:

# código anterior omitido

# def sobrenome(self):
#     nome_completo = self.nome.strip()
#     nome_quebrado = nome_completo.split(' ')

# # código posterior omitido

# Diferentemente do que fizemos em idade, agora o caractere de referência do método split
# será um espaço em branco, pois as pessoas sempre colocam um espaço entre um nome e outro.
# Por fim, vamos retornar o último item da lista nome_quebrado:

# # código anterior omitido

# def sobrenome(self):
#     nome_completo = self.nome.strip()
#     nome_quebrado = nome_completo.split(' ')
#     return nome_quebrado[-1]

# # código posterior omitido

# Pronto! Seguindo a demanda do chefe da Dominique, criamos o método sobrenome que retornará o último nome de um funcionário.

# A seguir, vamos abrir o arquivo test_bytebank.py novamente e codar um teste para esse novo método. Após o código do primeiro teste,
# criaremos outro chamado test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho. Depois, aplicaremos a metodologia
# Given-When-Then.

# O contexto será a entrada do nome do Lucas Carvalho. Para testar, vamos incluir um espaço antes e outro depois do nome:

# def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
#     entrada = ' Lucas Carvalho ' # Given

# Em seguida, vamos definir o resultado esperado e instanciar o objeto. O nome será a entrada;
# a data de nascimento, 11/11/2000; e o salário, R$1111,00:

# def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
#     entrada = ' Lucas Carvalho ' # Given
#     esperado = 'Carvalho'

#     lucas = Funcionario(entrada, '11/11/2000', 1111)

# A ação que será testada é a chamada do método sobrenome. Semelhante ao primeiro teste,
# vamos armazenar o retorno numa variável chamada resultado:

# def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
#     entrada = ' Lucas Carvalho ' # Given
#     esperado = 'Carvalho'

#     lucas = Funcionario(entrada, '11/11/2000', 1111)
#     resultado = lucas.sobrenome() # When

# No desfecho, temos o assert que verificará se o resultado é igual ao esperado:

# def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
#     entrada = ' Lucas Carvalho ' # Given
#     esperado = 'Carvalho'

#     lucas = Funcionario(entrada, '11/11/2000', 1111)
#     resultado = lucas.sobrenome() # When

#     assert resultado == esperado

# Para rodar o teste, acionaremos o terminal e executaremos pytest -v. 
# Assim, vamos obter o resultado do primeiro teste (relativo ao método idade),
# seguido do resultado do segundo teste (relativo ao sobrenome). Ambos retornarão como verdadeiro, então ambos passarão.

# Se executássemos apenas pytest (sem a flag -v), como resultado teríamos tests/test_bytebank.py ...
# A quantidade de pontos ao final da linha é igual à quantidade de testes que passaram.

# Vale relembrar que outra forma de rodar todos os testes é clicar na seta verde, logo à
# esquerda de class TestClass e selecionar "Run" — ou usar o atalho "Ctrl + Shift + F10".

# Também temos a opção de rodar um único teste, clicando na seta verde à esquerda do
# nome do método desejado, por exemplo, o test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho.
# Assim, teremos apenas o resultado desse teste específico.

# Sendo assim, acabamos de desenvolver outro teste com uma situação diferente.

# Quando o chefe da Dominique solicitou a inclusão dessa nova funcionalidade,
# primeiro criamos o método sobrenome e, depois, o teste referente a ele. 
# Será que poderíamos fazer esse processo de forma invertida: gerar
# o teste e depois o método? Essa questão dialoga com o conceito de TDD. Na próxima aula, vamos estudar esse assunto.

#Para saber mais: mais sobre o Pytest

# O Pytest possui diversas ferramentas que facilitam e otimizam a criação de testes automatizados.
# Confira o artigo a seguir e explore diferentes cenários de teste com o Pytest:

# https://www.alura.com.br/artigos/montando-cenarios-de-testes-com-o-pytest


#Nesse projeto aprendemos que

# O Pytest é o mais utilizado framework de Python dedicado a testes do mercado,
# sendo altamente escalável e repleto de plugins e extensões;
# Criar um teste utilizando o Pytest e entendendo que os nomes de cada cada arquivo
# de testes devem conter prefixos específicos para que sejam levados em consideração pelo Pytest;
# Testes devem possuir o nome mais verboso o possível;
# Utilizar o método ágil Given-When-Then para a construção de testes.


