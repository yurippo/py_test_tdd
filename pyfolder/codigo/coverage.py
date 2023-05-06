# Configurando ferramenta de cobertura

# O chefe da Dominique entrou em contato para elogiá-la e falar que ela está avançando muito bem nos seus aprendizados sobre desenvolvimento de projetos. Ela entendeu o que são testes automatizados, testes unitários e como utilizar o TDD para criar funcionalidades seguindo as regras de negócio.

# Durante essa conversa, o chefe dela comentou sobre cobertura de testes e a Dominique pediu nossa ajuda para entender esse conceito. Ao comparar lado a lado os arquivos bytebank.py e test_bytebank.py, o chefe da Dominique concluiu que existem vários testes para vários segmentos do projeto, contudo não há garantia de que todas as linhas de código estão cobertas por algum teste. Quando trabalhamos com testes, a intenção é ter 100% de cobertura por testes.

# A Dominique ficou um pouco confusa: "Como assim não tem garantia?". Comparando os dois arquivos e examinando os nomes verbosos dos testes, ela sabe que o primeiro teste verifica o funcionamento do método idade, o segundo teste refere-se ao método sobrenome e assim por diante. Segundo a análise dela, cobrimos todas as partes do código.

# Mas existe um problema em fazer essa análise manualmente. Conforme um projeto se torna mais extenso e complexo, fica cada vez mais difícil nos certificarmos de que cobrimos todos os cenários possíveis de todos os segmentos de código. Por isso, existem ferramentas para nos ajudar a verificar a cobertura de testes! O Pytest tem uma extensão chamada pytest-cov. "Cov" é uma abreviação de coverage — "cobertura", em inglês.

# Vamos instalar a versão 3.0.0 dessa extensão pelo terminal com o pip, usando o comando pip install pytest-cov==3.0.0. Em seguida, executaremos pip freeze > requeriments.txt para atualizar o nosso arquivo requirements.txt que contém a lista com todos os pacotes instalados no ambiente virtual. Depois, podemos abrir o arquivo requirements.txt e checar que o pytest-cov==3.0.0 está listado também.

# Para rodar a extensão e verificarmos qual é a cobertura do código da Dominique, vamos executar o comando pytest --cov no terminal. Assim, o pytest-cov procurará todos os testes para checar a cobertura. Na sequência, vamos examinar o resultado.

# Primeiramente, o Pytest foi executado normalmente e obtemos tests/test_bytebank.py ..... — os cinco pontos indicam que os cinco testes passaram. Em seguida, temos uma tabela que explica cada parte em que o coverage rodou:

# Name	Stmts	Miss	Cover
# codigo/bytebank.py	35	1	97%
# tests/_init_.py	0	0	100%
# tests/test_bytebank.py	38	1	97%
# TOTAL	73	2	97%

# Na coluna "Name", temos o nome dos arquivos em que foi feita a leitura da cobertura. O primeiro deles é o bytebank.py, onde realmente queremos que ele rode. Depois, temos o dunder init e o próprio arquivo de testes (test-bytebank.py).

# Na segunda coluna, temos os statements (a quantidade de linhas do código). No bytebank.py, por exemplo, temos 35 statements. Depois, temos a coluna "Miss", que indica a quantidade de statements que não estão sendo testados! Ou seja, no arquivo bytebank.py, perdemos uma linha na cobertura de testes.

# Por fim, temos a coluna "Cover" que exibe a porcentagem de cobertura de testes de cada arquivo. No bytebank.py, temos 97% de cobertura.

# No momento, temos interesse em examinar apenas a cobertura de testes do arquivo bytebank.py. Então, vamos executar novamente o pytest-cov, dessa vez definindo o diretório onde queremos realizar o teste (no caso, codigo). Depois, precisamos indicar o nome da pasta de testes, que é tests:

# pytest --cov=codigo tests/

# Executando o comando, o pytest-cov selecionará apenas o arquivo que especificamos e fará os testes só no bytebank.py:

# Name	Stmts	Miss	Cover
# codigo/bytebank.py	35	1	97%
# TOTAL	35	1	97%

# Sendo assim, conseguimos rodar pela primeira vez a ferramenta de cobertura de testes. Temos 97% de cobertura, o que significa que tem alguma linha do bytebank.py que não está sendo coberta, não há um teste para ela.

# Vamos descobrir que linha é essa e o que podemos mudar para alcançar os 100% de cobertura!

# Excluindo código para a cobertura

#  reparamos que existem certas questões intrínsecas da linguagem para as quais não vale a pena criar testes. Como pessoas programadoras, assumimos que a linguagem funciona como deveria e nos resguardamos para gerar testes voltados para códigos que nós criamos — seja para verificar a lógica de programação ou regras de negócio, por exemplo.

# Logo, concluímos ser desnecessário testar o método __str__, então vamos apagar o teste test_retorno_str do arquivo test_bytebank.py. Se executarmos o comando pytest --cov=codigo tests/ --cov-report term-missing novamente, voltaremos a ter apenas 97% de cobertura.

# Com essa tabela, sabemos o número da linha em que falta cobertura, porém há outro método de relatório em que é possível arranjar esse resultado de forma mais visual. Basta executar o comando pytest --cov=codigo tests/ --cov-report html.

# O coverage será executado e salvo em um arquivo HTML. Abrindo a estrutura de diretórios à esquerda da IDE, há uma nova pasta chamada htmlcov. Nela, temos um novo arquivo de nome index.html. Vamos clicar sobre ele com o botão direito, selecionar "Open in > Browser" e escolher o navegador de nossa preferência. No meu caso, abrirei no Firefox.

# No navegador, a princípio, teremos a mesma tabela que obtivemos anteriormente, apenas com uma interface mais bonita. Ao clicar no ícone de teclado no canto direito superior da tela, teremos uma lista de atalhos de teclados. Com as teclas "n", "s", "m", "x" e "c" é possível alterar a ordem das colunas da tabela. Com as teclas de colchetes, podemos ir para outros arquivos. Vamos pressionar a tecla "]" (colchete direito ou "fecha colchete") para ir ao próximo arquivo, onde serão mostradas todas as linhas de código do bytebank.py.

# No topo da página, temos escrito "35 statements". À direita desse texto, há três retângulos. Clicando no primeiro (em que está escrito "34 run"), destacaremos em verde todas as linhas de código que estão cobertas por algum teste. Pressionando o segundo retângulo (em que está escrito "1 missing"), ressaltamos em vermelho a linha que não tem teste. No terceiro retângulo, está escrito "0 excluded".

# Comparado ao relatório que obtivemos na linha de comando, esta é uma representação mais visual da cobertura dos testes.

# Agora, vamos voltar à IDE e especificar ao pytest-cov que não precisamos cobrir o método __str__. Dentro do diretório bytebank.tdd, criaremos um arquivo chamado .coveragerc. Assim como o pytest.ini, o .coveragerc também precederá as configurações básicas, dessa vez para a extensão do coverage do Pytest.

# Neste arquivo, vamos definir algumas configurações para nosso relatório (report), indicando linhas que queremos que sejam excluídas do escaneamento:

# [run]
# source = ./codigo

# [report]
# exclude_lines =
#     def __str__

# Em seguida, vamos executar pytest --cov=codigo tests/ --cov-report term-missing novamente no terminal. Desta vez, teremos 33 statements e 100% de cobertura. Ou seja, conseguimos desconsiderar o trecho sobre o qual não precisamos ter testes.

# No próximo vídeo, estudaremos outras funcionalidades interessantes do pytext-cov, como a geração de outros relatórios e configurações para o .coveragerc que nos ajudarão na execução do Pytest.


# Contexto de cobertura

# O conceito de cobertura de código é muito utilizado no mercado de desenvolvimento de software com Python em conjunto com a prática de testes e TDD. Uma ferramenta de cobertura como a extensão Pytest-cov é muito útil para verificar a presença de testes sobre o código de uma aplicação.

# Sobre o conceito de cobertura de testes:

# Quanto maior é a cobertura de código em um projeto, menores são as chances de acontecerem erros no desenvolvimento de novas funcionalidades que obedecem regras de negócio específicas.

# Quanto maior é a porcentagem de cobertura indicada pela ferramenta de cobertura, maiores são as chances da aplicação ter sido exaustivamente testada por testes unitários e funcionar como esperado.

# O objetivo do Pytest-cov é mostrar a quantidade de código que está coberta por testes. Não necessariamente existe uma verificação de qualidade de código.

# Existem certos trechos de código que não precisam ser testados por serem funcionalidades intrínsecas da linguagem. Observe o exemplo a seguir:

# @property
# def nome(self):
#         return self._nome

# Esse código desempenha a função de retornar o atributo nome sem que ele seja acessado como método. Isso é uma característica do funcionamento da linguagem Python e portanto, não precisa ser testado.

# Gerando relatórios

# Já aprendemos que, para executar o pytest-cov e mostrar um relatório de coverage, basta rodar o comando pytest --cov=codigo tests/ --cov-report term-missing. Como retorno, temos uma tabela com todas as informações que precisamos. Alternativamente, há o comando pytest --cov=codigo tests/ --cov-report html, que criará um diretório com arquivos HTML para visualizarmos os códigos compreendidos ou não por testes, bem como os trechos excluídos do escaneamento (como no caso do método __str__).

# Essas são duas opções viáveis para consultar a cobertura de testes, porém são comandos longos e seria trabalhoso utilizar constantemente essa nomenclatura. Felizmente, temos uma maneira de diminuí-la. De início, vamos focar na tag --cov=codigo tests/, que define o diretório em que os testes serão realizados. No arquivo .coveragerc, vamos personalizar o source:

# [run]
# source = ./codigo

# [report]
# exclude_lines =
#     def __str__

# Anteriormente, quando executamos pytest --cov, o Pytest realizava os testes em todas as pastas do nosso projeto. Agora que definimos o source, ao rodar pytest --cov, apenas o diretório codigo será compreendido. Assim, já conseguimos reduzir parte do comando.

# Por enquanto, o relatório HTML é gerado numa pasta de nome htmlcov, mas gostaríamos de guardá-lo em uma pasta própria. No arquivo .coveragerc, vamos personalizar esse local de armazenamento:

# [run]
# source = ./codigo

# [report]
# exclude_lines =
#     def __str__

# [html]
# directory = coverage_relatorio_html

# Dessa forma, guardaremos os relatórios HTML no diretório chamado coverage_relatorio_html. Para testar, vamos apagar a pasta htmlcov. Após rodar novamente o comando pytest --cov=codigo tests/ --cov-report html, consultaremos a estrutura de diretórios do projeto e teremos o novo diretório coverage_relatorio_html, onde encontraremos o index.html que podemos abrir no navegador.

# Para executar o coverage, ainda precisamos inserir a tag --cov. Antes de entregar o relatório, o Pytest sempre executa todos os testes, então podemos definir todas essas tags de uma única vez, no arquivo pytest.ini:

# [pytest]
# addopts = -v --cov=codigo tests/ --cov-report term-missing
# markers =
#     calcular_bonus: Teste para o metodo calcular_bonus

# Assim, toda vez que executarmos pytest serão adotadas as tags -v, --cov=codigo e --cov-report term-missing. Em outras palavras, o retorno sempre será verboso, os testes sempre serão executados no diretório codigo e sempre geraremos um relatório term-missing. Outra opção seria configurar para recebermos um relatório HTML.

# Após salvar, podemos rodar pytest no terminal para nos certificar de que o resultado aparecerá conforme o esperado.

# Por fim, vamos aprender como gerar relatórios em formato XML, um padrão do mercado, estabelecido em diversas linguagens de programação e bastante útil para enviar a outras pessoas. Basta executar o comando pytest --junitxml report.xml. O JUnit é a ferramenta de testes do Java, linguagem que estabeleceu esse padrão. Já report.xml é o nome que escolhemos para nosso arquivo.

# Todos os testes serão executados novamente e geraremos o arquivo report.xml na estrutura de diretórios do projeto. Posteriormente, podemos fazer um parsing de dados para visualizar essas informações de uma forma melhor.

# O report.xml é um relatório dos testes do Pytest. De forma complementar, podemos gerar um relatório do coverage, executando o comando pytest --cov-report xml. Na estrutura de diretório à esquerda, teremos o novo arquivo coverage.xml.

# Então, conseguimos ensinar o que são testes, como funciona o Pytest e as funções do coverage para a Dominique. Agora, ela está apta para mostrar inúmeros relatórios para o chefe dela e avançar em seu projeto do Bytebank.

#Ferramenta do Coverage

# 1) Começamos instalando a ferramenta de coverage do Pytest, o Pytest-cov, através do terminal/prompt de comando;

# pip install pytest-cov==3.0.0

# 2) Atualizamos o arquivo requirements.txt com o seguinte comando no terminal/prompt de comando;

# pip freeze > requirements.txt

# 3) Rodamos a ferramenta de cobertura de testes pela primeira vez com o seguinte código:

# pytest –cov=codigo tests/ 

# 4) Percebemos que alguns trechos de código do arquivo bytebank.py não estão sendo cobertos. Para localizar quais trechos são esses, utilizamos o seguinte comando:

# pytest –cov=codigo tests/ –cov-report term-missing

# 5) Aprendemos também, uma forma de gerar um relatório de cobertura de testes em HTML através do seguinte comando:

# pytest –cov=codigo tests/ –cov-report html

# 6) Pudemos visualizar que o trecho que não possui teste é aquele que possui o método __str__();

# 7) Para obter 100% de cobertura de testes, criamos um teste para o método __str__();

# def test_retorno_str(self):
#        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000  # given
#        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

#         funconario_teste = Funcionario(nome, data_nascimento, salario)
#         resultado = funconario_teste.__str__() # when

#         assert resultado == esperado  # then


# 8) Contudo, aprendemos que existem certos trechos de código que executam funcionalidades intrínsecas da linguagem Python e que não faz sentido testá-los, já que como pessoas desenvolvedoras, assumimos que a linguagem funciona como deveria.

# 9) Tendo isso em mente, apagamos o teste feito sobre o método __str__() e criamos o arquivo .coveragerc, que possui um propósito similar ao pytest.ini e possibilita a mudança de algumas configurações padrão do pytest-cov;

# 10) O arquivo .coveragerc dá a possibilidade de excluirmos linhas de código do bytebabank.py, cuja cobertura de teste não queremos verificar;

# [run]

# [report]
# exclude_lines =
#    def __str__


# 11) Melhoramos a execução da ferramenta de cobertura definindo no arquivo pytest.ini que sempre que digitarmos o código pytest no terminal, deve ser feita não apenas a execução dos testes, mas o relatório de cobertura de código;

#     [pytest]
# addopts = -v --cov=codigo tests/ --cov-report term-missing
# markers =
#     calcular_bonus: Teste para o metodo calcular_bonus

# 12) Também alteramos o arquivo .coveragerc para que sempre que executarmos o comando pytest –cov a análise de cobertura de testes seja feita apenas no arquivo bytebank.py, bem como, definimos que sempre que um relatório em HTML for gerado, ele deve ficar dentro de um diretório chamado coverage_relatorio_html.

#     [run]
# source = ./codigo

# [report]
# exclude_lines =
#     def __str__

# [html]
# directory = coverage_relatorio_html

# 13) Para criarmos um relatório de testes no padrão xml, basta utilizar o seguinte comando no terminal/prompt de comando:

#     pytest –junitxml report.xml

# 14) Para criar um relatório de cobertura no padrão xml, basta utilizar o seguinte comando no terminal/prompt de comando:

# pytest –cov-report xml

# A cobertura de testes é uma das formas de garantir a qualidade do software através da constatação de existência de testes nas principais funcionalidades da aplicação;
# Utilizar a ferramenta de cobertura de testes do Pytest, o pytest-cov;
# Criação de relatórios em formatos diferentes, como HTML e XML.

# Primeiramente, conhecemos a história da Dominique, uma pessoa desenvolvedora iniciante na empresa Bytebank. Ela recebeu um projeto para desenvolver, mas não tinha muita familiaridade com testes — um conceito exigido por seu chefe.

# Então, de início, aprendemos o que são testes, quais tipos de testes existem, para que eles servem e por que são importantes no desenvolvimento de projetos. Em seguida, criamos nosso primeiro teste automatizado no arquivo main.py para começar a entender esse assunto na prática.

# Logo, descobrimos ser interessante usar um framework para testes. Toda linguagem de programação com foco em desenvolvimento de projetos conta com uma biblioteca dedicada a testes. No caso do Python, temos o Pytest, ferramenta que usamos para transpor nossos testes. Configuramos o ambiente, criamos o diretório para testes e atentamos às nomenclaturas corretas aceitas pelo Pytest, bem como aos padrões e às boas práticas na criação de testes (como nomes verbosos).

# Na sequência, entendemos o que é TDD — Test-driven development, uma metodologia alternativa à criação do código antes dos testes. No TDD, invertemos a ordem: criamos os testes primeiro, depois, a implementação — e, por fim, refatoramos o código. Essa metodologia coloca em evidência as regras de negócio e traz maior segurança para alterar e atualizar o código.

# Aprendemos a aplicar o TDD, na prática, ajudando a Dominique a implementar funcionalidades na classe Funcionario em que ela estava trabalhando. Entendemos qual era a regra de negócio do método, depois o criamos e refatoramos o código.

# Em seguida, aprendemos sobre as exceptions, erros personalizados que serão exibidos na tela quando determinado problema ocorrer no projeto. Adicionalmente, aprendemos a criar testes que incluem exceptions, já que são estruturas recorrentes.

# Depois, descobrimos como utilizar os markers, um recurso do Pytest para organizar os testes com tags, mudando a execução dos testes. Por exemplo, conseguimos "pular" alguns deles, se necessário.

# Mais adiante, entendemos o conceito e a importância do coverage. A cobertura de testes é uma forma de nos certificar de que temos 100% do código coberto por testes. Inclusive, levantamos o questionamento se segmentos intrínsecos da linguagem precisam de testes e concluímos que não é uma prática tão interessante, podemos assumir que funcionarão. Para fazer esse escaneamento da cobertura, utilizamos o pytest-cov, uma extensão do Pytest.

# Por fim, aprendemos a gerar relatórios para apresentar para outras pessoas e indicar que nossos projetos estão funcionando dentro dos padrões de TDD. Nosso estudo valeu a pena e agora temos um bom entendimento de testes com Python!

# Como próximo passo, você pode personalizar o projeto da Dominique, modificando e aplicando mais teste ou incluindo mais funcionalidades, por exemplo. Outra opção é inserir testes em seus projetos pessoais, ou implementar o TDD em códigos que você já testou anteriormente.

# Além disso, você pode compartilhar nas redes sociais o projeto finalizado deste curso. Isso contribui para o fortalecimento de uma comunidade focada em tecnologia, que ama o Python, testes unitários automatizados e metodologia do TDD! Principalmente se você estiver no começo de carreira, participar nas redes sociais é uma ótima maneira de aumentar a sua visibilidade para grandes empresas ávidas por novos programadores com conhecimento em testes.

# Não deixe de interagir nas comunidades da Alura também, como o Discord. Compartilhe o seu código, como foi sua experiência ao longo deste treinamento e troque ideias com seus colegas