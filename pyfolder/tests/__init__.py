
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