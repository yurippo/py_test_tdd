# Organizando testes com Markers

# vamos estudar algumas das funcionalidades do Pytest que nos permitem explorar a execução dos testes.

# Sabemos que o comando pytest -v roda todos os testes, no entanto, a Dominique gostaria de verificar o resultado de apenas um teste específico. Anteriormente, reparamos que há uma seta verde à esquerda do nome de cada teste. Ao clicar sobre ela com o botão direito, podemos selecionar "Run" para executar o teste individualmente (com uma interface diferente), porém essa solução dependente da IDE. Seria interessante ter um recurso que podemos executar em qualquer tipo de ambiente, pelo terminal.

# Uma opção para selecionar determinado teste e executá-lo é usar a flag -k, que realizará a filtragem a partir de uma palavra do nome do método. Por exemplo, para executar apenas o teste test_quando_idade_recebe_13_03_2000_deve_retornar_22, vamos rodar o comando pytest -k idade, pois este é o único teste com a palavra "idade".

# No resultado, seremos informados que 1 teste passou e 4 foram desselecionados. Isto é, eles não falharam, apenas não os executamos. Para obter o retorno de modo verboso, podemos usar mais de uma flag ao mesmo tempo: pytest -v -k idade.

# Por enquanto, nosso projeto tem poucos testes, então conseguimos lembrar os nomes de cada um deles, mas a tendência é que esse arquivo fique mais extenso. Dependendo do tamanho do projeto, talvez até tenhamos mais de um arquivo de testes. Com o tempo, filtrar testes pelo nome se tornará uma prática inviável, pois não teremos certeza se uma palavra está presente apenas em um teste. Como os nomes devem ser verbosos e explicativos, é provável que muitas palavras se repitam. No nosso caso, todos os testes repetem "quando" e "deve", por exemplo.

#mark

# Então, outra opção para selecionar a execução de testes específicos é por meio dos marks! Para entendermos o que são os marks, primeiramente vamos importá-los no início do arquivo:

# from codigo.bytebank import Funcionario
# import pytest
# from pytest import mark

# Vamos supor que queremos executar apenas os testes referentes ao método calcular_bonus — no caso, os dois últimos testes que desenvolvemos neste curso. Para filtrá-los, criaremos um decorator chamado calcular_bonus, que será um mark:

# @mark.calcular_bonus
# def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
#     entrada = 1000  # given
#     esperado = 100

#     funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
#     resultado = funcionario_teste.calcular_bonus() # when

#     assert resultado == esperado  # then

# Em resumo, o mark é uma tag que associamos a determinados testes. Ele tem o formato de um decorator do Python: inicia-se com o símbolo de arroba, seguido da nomenclatura mark, um ponto e o nome.

# Na segunda linha do arquivo, estamos importando o pytest. Na linha seguinte, importamos o mark de pytest. Poderíamos usar o mark com `@pytest.mark.calcular_bonus`, mas optamos pela segunda importação para manter o código mais organizado.

# Vamos usar a mesma tag no outro teste referente ao calcular_bonus:

# @mark.calcular_bonus
# def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
#     entrada = 1000  # given
#     esperado = 100

#     funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
#     resultado = funcionario_teste.calcular_bonus() # when

#     assert resultado == esperado  # then

# @mark.calcular_bonus
# def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
#     with pytest.raises(Exception):
#         entrada = 100000000  # given

#         funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
#         resultado = funcionario_teste.calcular_bonus()  # when

#             assert resultado  # then
        

# Para executar apenas esses dois testes, basta chamar a tag calcular_bonus com a flag -m (de mark):

# pytest -v -m calcular_bonus

# Analisando o resultado no terminal, notaremos que 2 testes foram executados e passaram; e 3 testes foram desselecionados, como esperado.

# Além disso, teremos dois warnings (avisos), indicando que pytest.mark.calcular_bonus é um mark fora dos padrões. O Pytest não sabe distinguir se é um erro de digitação (typo) ou um mark personalizado.

# Os marks não são apenas tags que podemos utilizar como referências para certos testes, eles têm outras utilidades e seguem alguns padrões. Para verificar quais tipos de marks existem no Pytest, vamos executar pytest --markers no terminal. Dessa forma, teremos a documentação de todos os markers que podemos utilizar. Por exemplo, ao colocar `@pytest.mark.skip` antes de um teste, executaremos todos os testes e "pularemos" apenas este. Vamos testá-lo.

# Primeiramente, vamos comentar os markers `@mark.calcular_bonusque inserimos nas linhas 35 e 45. Em seguida, vamos incluir@mark.skipna linha imediatamente antes do teste de decréscimo de salário. No terminal, rodaremospytest -v` para executar todos os testes. Como resultado, notaremos que foram executados 4 testes e 1 foi ignorado ou "pulado" (skipped).

# Portanto, os marks oferecem a possibilidade de organizarmos melhor quais testes queremos executar ou até mesmo a forma como queremos executá-los. Vamos estudar mais alguns exemplos, executando pytest --markers novamente.

# Além do `@pytest.mark.skipque "pula" um teste, temos o@pytest.mark.skipifque "pulará" o teste se uma condição for obedecida. Existe também o@pytest.mark.xfail` que determina que um teste deve falhar, caso certa condição seja atendida. São diversos markers à disposição, é interessante consultarmos a documentação do Pytest para encontrar formas de personalizar nossos códigos conforme nossas necessidades.

# Por ora, vamos voltar ao projeto da Dominique. Removeremos o `@mark.skipque incluímos na linha 24 e descomentar os@mark.calcular_bonus` das linhas 35 e 45.

# Constatamos que, ao rodar pytest -v -m calcular_bonus, receberemos 2 warnings. Para retirar esses avisos, precisamos gerar um arquivo, onde incluiremos esses marks personalizados. Clicaremos com o botão direito sobre a pasta bytebank-tdd no painel à esquerda, selecionaremos "New > File" e nomearemos o novo arquivo pytest.ini.

# Este é um arquivo de configuração do Pytest e ele precede a configuração original do Pytest. É preciso tomar cuidado com o que colocamos nele, pois, uma vez o Pytest é executado, ele dará prioridade ao que está neste arquivo e, depois, considerará a configuração padrão do Pytest.

# Na primeira linha, digitaremos [pytest]. A seguir, vamos incluir o nome do nosso marker personalizado, bem como uma descrição:

# [pytest]
# markers =
#     calcular_bonus: Teste para o metodo calcular_bonus

# Vamos salvar. Em seguida, executaremos pytest -v -m calcular_bonus no terminal mais uma vez, para rodar apenas os testes marcados com a tag calcular_bonus. Dessa vez, 2 testes passarão, 3 serão desselecionados e não teremos warnings, pois acrescentamos os markers personalizados no arquivo pytest.ini.

# Para saber mais: Markers

# Parte da razão pela qual o Pytest é conhecido como framework de testes, não uma simples biblioteca, está no fato do Pytest possuir uma vasta gama de ferramentas direcionadas a melhorar a eficiência e organização dos testes desenvolvidos.

# Os markers ou marcadores são uma dessas ferramentas incríveis do Pytest e oferecem não somente uma forma de organizar melhor os testes com tags personalizadas, mas colaboram para definir como determinados testes irão funcionar ou ser executados.

# skip

# @pytest.mark.skip(reason="não quero executar isso agora")
# def test_aleatorio():
#     ...

# Através do uso do marker skip podemos pular um teste, caso a execução dele não seja necessária naquele instante.

# skipif

# import sys


# @pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
# def test_funcao():
#     ...

# Acima, o teste não é executado caso sys.version_info < (3, 10) seja verdadeiro, ou seja, caso a versão do Python esteja abaixo da versão 3.10.

# Através do uso do marker skipif podemos pular um teste caso ele se encaixe em determinada situação definida por uma condicional.

# xfail

# @pytest.mark.xfail
# def test_funcao():
#     ...
# Através do uso do marker xfail especificamos que o teste deve retornar uma falha, em vez de passar.

# Essas e muitas outras possibilidades de uso de markers para modificar a mecânica de uso dos testes podem ser vistas na documentação oficial do Pytest.

# How to mark test functions with attributes

# https://docs.pytest.org/en/7.1.x/how-to/mark.html