#Implementando uma funcionalidade

# O chefe da Dominique pediu para ela adicionar mais uma funcionalidade à classe Funcionario, então chegou a hora de aplicarmos nosso conhecimento de TDD.

# A Bytebank está passando por um período financeiramente instável, por isso os sócios e os diretores da empresa concordaram em fazer um decréscimo de 10% em seus próprios salários para ajudar nessa situação, visto que todos eles ganham um salário mínimo de R$100.000,00. Então, a Dominique será responsável por implementar o método que identificará os diretores e fará esse decréscimo.

# Seguindo a metodologia do TDD, a primeira etapa são os testes. Vamos abrir o arquivo test_bytebank.py e começar a codar o teste para essa nova funcionalidade.

# Primeiramente, escolheremos o nome do método, lembrando que ele deve começar com test_ e ser o mais verboso possível. Mantendo o padrão usado anteriormente, o nomearemos test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000 — pois, ao tirar 10% de um salário de R$100.000,00, o resultado é R$90.000,00.

# Em seguida, escreveremos o código aplicando a metodologia Given-When-Then. A entrada do salário será 100000 e o resultado esperado é 90000:

#  def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
#     entrada_salario = 100000 #given
#     esperado = 90000

# Ou seja, o Given é a entrada do salário. Depois, vamos instanciar o funcionário:

# def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
#     entrada_salario = 100000 #given
#     esperado = 90000

#     funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)

# Na sequência, chamaremos o método responsável pelo decréscimo e o resultado deve ser igual ao salário do funcionário:

# def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
#     entrada_salario = 100000 #given
#     esperado = 90000

#     funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
#     funcionario_teste.decrescimo_salario() # when
#     resultado = funcionario_teste.salario

# Em outras palavras, o When é a chamada do método decrescimo_salario. Por fim, com o assert, verificaremos se o resultado é igual ao esperado — este será o Then:

# def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
#     entrada_salario = 100000 #given
#     esperado = 90000

#     funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
#     funcionario_teste.decrescimo_salario() # when
#     resultado = funcionario_teste.salario

#     assert resultado == esperado  # then

# É possível que haja outros funcionários na Bytebank que ganhem R$100.000,00 e não sejam diretores. Então, para garantir que apenas o salário dos diretores será afetado, vamos incluir mais uma entrada, com o nome de um diretor:

# def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
#     entrada_salario = 100000 #given
#     entrada_nome = 'Paulo Bragança'
#     esperado = 90000

#     funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
#     funcionario_teste.decrescimo_salario() # when
#     resultado = funcionario_teste.salario

#     assert resultado == esperado  # then

# Note que também modificamos a instanciação do funcionario_teste, passando entrada_nome para o parâmetro nome.

# Com o teste pronto, vamos rodá-lo usando o comando pytest -v no terminal. Ele falhará, porque ainda não chegamos na parte de codar. Seguindo as etapas do ciclo do TDD, primeiro desenvolvemos o teste e eles falharão, então faremos a implementação.

# A seguir, ajudaremos a Dominique a implementar esse método. Já conhecemos as regras de negócio, respeitadas pelo teste: se temos um salário de R$100.000,00 e o nome de um dos diretores, o método deve ser chamado e haverá um decréscimo de 10% no salário desse funcionário. Agora, temos que codar um método que faça o teste passar.

# No arquivo bytebank.py, após o método sobrenome, criaremos o método decrescimo_salario:

# def decrescimo_salario(self):
#     if self._salario >= 100000:
#         decrescimo = self._salario * 0.1
#         self._salario = self._salario - decrescimo

# De início, incluímos uma condicional: se o salário do funcionário for maior ou igual a R$100.000,00, o decréscimo deve ocorrer. Em seguida, declaramos a variável decrescimo, que será igual a 10% desse salário. Por fim, subtraímos o valor do decréscimo.

# Além de verificar se a pessoa ganha R$100.000,00 ou mais, é preciso checar se ela também está na lista de diretores e sócios. A Dominique possui uma lista dos sobrenomes deles, então vamos inseri-la no código:

# def decrescimo_salario(self):
#     sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
#     if self._salario >= 100000:
#         decrescimo = self._salario * 0.1
#         self._salario = self._salario - decrescimo

# Na sequência, adicionaremos mais uma condição. Para que o decréscimo aconteça, além de ganhar mais de R$100.000,00, o sobrenome do funcionário deve estar na lista sobrenomes:

# def decrescimo_salario(self):
#     sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
#     if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
#         decrescimo = self._salario * 0.1
#         self._salario = self._salario - decrescimo

# Perceba que, para selecionar o sobrenome do funcionário, usamos o método sobrenome que desenvolvemos anteriormente. Dessa forma, geramos o método que fará nosso teste passar. Vamos chamar o pytest -v no terminal novamente.

# Todos os testes passarão! Quer dizer que completamos a segunda etapa do ciclo do TDD. Elaboramos os testes e eles falharam, depois desenvolvemos o código e os testes passaram. Podemos partir para a refatoração.

# Analisando o decrescimo_salario, é importante nos questionarmos se essa é a melhor forma de desenvolver esse método, se há formas de melhorá-lo. Atualmente, estamos verificando se o funcionário é diretor, se seu salário é maior que R$100.000,00 e realizando o decréscimo de salário —
# são muitos processos acontecendo no mesmo método. Num cenário ideal, cada método tem uma única função.


#TDD e sua utilização

# O Test-Driven Development (Desenvolvimento Guiado por Testes) é um método de desenvolvimento de software amplamente utilizado
# no mercado de trabalho voltado a Python.

# A respeito do TDD:

# O TDD trabalha com o conceito de que os testes são uma representação das regras de negócio que o software deve obedecer.
# Ao final do desenvolvimento de um software funcional utilizando o TDD, teremos uma série de arquivos de testes que expõem de
# forma direta o que cada porção do código da aplicação deve desempenhar. Assim, as funcionalidades estarão de acordo com as
# regras de negócio.

# É normal que ao longo do desenvolvimento do software usando o TDD, algum trecho de código que anteriormente havia sido desenvolvido
# e que passava em todos os testes deixe de passar.. Isso faz parte da filosofia de refatoração do TDD, será comum que trechos de
# códigos parem de funcionar à medida que outros sejam criados e a intenção é sempre consertá-los conforme surjam.

#A etapa da implementação deve ser feita com o pensamento de que o código a ser desenvolvido deve garantir que os testes feitos passem.

# Uma vez que o teste foi criado e que ele expressa de forma correta a regra de negócio e como o código deve responder, basta que a
# implementação siga o raciocínio desenvolvido pelo teste, ou seja, o teste deve passar.

# É normal que alguns testes tenham que ser reformulados à medida que o desenvolvimento da aplicação avança,
# seja por motivos de mudança na regra de negócio ou simples reestruturação do arquivo de testes.

# A refatoração é um dos grandes trunfos do TDD, pois encoraja que o código do software sempre seja revisado pelas
# pessoas desenvolvedoras, de forma que esteja em constante melhoria.