# Lidando com Exceptions no Pytest

# Como solicitado pelo chefe da Dominique, inserimos uma exception no método calcular_bonus. Também desenvolvemos um teste para averiguar o bom funcionamento desse segmento de código, contudo ele contempla apenas o cenário em que o funcionário se enquadra nas regras para recebimento do bônus.

# A seguir, vamos construir um teste que considere a situação em que o funcionário não recebe bônus, isto é, quando ocorrer a exception com a mensagem de erro.

# No arquivo test_bytebank.py, a partir da linha 42, vamos criar o teste test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception. O Pytest tem um recurso que considera que o retorno do teste tem que ser uma exception, para utilizá-lo colocamos with pytest.raises(Exception):

# def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
#     with pytest.raises(Exception):

# Dessa forma, o trecho que estiver dentro do with, no final, deve levar a uma exception. Para que essa ferramenta funcione, é preciso importar o pytest no início do arquivo, com import pytest.

# O teste seguirá a mesma lógica dos que criamos anteriormente:

# def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
#     with pytest.raises(Exception):
#         entrada = 100000000  # given

#         funconario_teste = Funcionario('teste', '11/11/2000', entrada)
#         resultado = funconario_teste.calcular_bonus()  # when

#         assert resultado  # then

# A entrada é o salário de R$100.000.000,00. Não precisamos informar o resultado esperado, porque dentro do pytest.raises(Exception) fica implícito que o esperado é uma exception. Depois, instanciamos um funcionário cujo salário será a entrada e armazenamos o retorno de calcular_bonus na variável resultado — este é o when. Por fim, não compararemos resultado com esperado como antes, visto que este último não existe mais. Em vez disso, apenas vamos conferir se o resultado é uma exception.

# No terminal, executaremos pytest -v e constataremos que todos os testes passam, inclusive o que acabamos de desenvolver. Sendo assim, criamos dois testes para o método calcular_bonus. O primeiro testa a situação em que o bônus é concedido, já o segundo trata do cenário em que o funcionário não recebe o bônus — neste caso, usamos uma exceção.

# Ao desenvolver um segmento de código, é comum gerar diversos testes para a mesma funcionalidade para englobar situações diversas em que o retorno será diferente. No próximo vídeo, aprenderemos a organizar melhor nossos testes, agrupando-os e inserindo indicações para facilitar o entendimento de outros desenvolvedores.

# Exceptions em software

# É muito comum a utilização de exceptions no desenvolvimento de softwares em Python, portanto, é natural que existam ferramentas em testes para lidar com exceptions.

# Sobre exceptions e sua influência na construção de testes:

# A linguagem Python apresenta dois tipos de erros possíveis: Syntax Errors (erros de Sintaxe) e Exceptions (erros de lógica)

# O Pytest possui bibliotecas e métodos capazes de lidar com exceptions. Um exemplo é o método raises(), que traz a possibilidade de assumirmos uma exception como um desfecho do teste.

# Exceptions são o equivalente a erros de lógica em Python e já existem várias exceptions padrão dentro da linguagem. Você pode dar uma olhada na documentação.

# https://docs.python.org/pt-br/3/library/exceptions.html

# Uma forma de criar um teste que leve em consideração uma exception é utilizando o código with pytest.raises(Exception).
# Através do trecho de código acima, podemos lidar com exceptions usando o Pytest.



