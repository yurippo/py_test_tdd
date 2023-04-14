# O que são testes?

# Afinal de contas, por que testes existem? Vamos usar o exemplo da 

# Dominique para analisar essa questão.

# A Dominique é uma pessoa desenvolvedora e, ao longo de sua carreira, ela desenvolverá muitos códigos.
#Grande parte desses códigos serão funcionalidades de uma aplicação maior — haverá um grande projeto e cada trecho desenvolvido
# será uma nova funcionalidade a ser adicionada nele.

# Cada funcionalidade deve respeitar certas regras de negócio do projeto, recebendo determinadas informações e
# retornando determinados dados.

# No início do desenvolvimento, enquanto o projeto ainda está pequeno, é fácil julgar se o código respeita
# ou não as regras de negócio. Porém, conforme o projeto crescer, a hierarquia do projeto aumentar, existir mais módulos,
# classes e métodos, e surgir mais regras de negócio, logo cada funcionalidade terá que respeitar inúmeras regras!
# É neste ponto que entra o processo de testes

# O teste verifica se cada funcionalidade está se comportando como deveria, garantindo um desempenho de maior
# qualidade dos códigos. Inclusive, há pessoas que são contratadas para se dedicarem em tempo integral apenas
# a esses procedimentos! Os testers são responsáveis por aplicar testes em códigos de outras pessoas desenvolvedoras,
# executando os famosos testes manuais.

# O teste manual apresenta algumas desvantagens em relação ao automático. Primeiramente, ele é um processo mais lento e
# trabalhoso, visto que é uma pessoa quem o realizará. Ela precisa visualizar e interpretar o código, analisar as regras
# de negócio e elaborar algoritmos que testarão a funcionalidade específica. Por conta desse fator humano, os testes manuais
# também estão sujeitos a falhas.

# Por outro lado, um tester é capaz de observar a especificidade de cada projeto em particular. Este é o grande
# mérito dos testes manuais: uma pessoa encarregada exclusivamente de testes examinará minuciosamente os processos envolvidos no código.

# Ademais, construir testes manuais pode ser bastante inconveniente. Uma vez que a pessoa dev está desenvolvendo um projeto,
# é inoportuno interromper esse avanço para produzir testes manuais para todas as funcionalidades existentes. 
#Ainda mais se já soubermos que o código está funcionando.

# Em contrapartida, o teste automatizado possui várias características interessantes. A primeira vantagem
# é ser automatizado. Uma vez desenvolvido, é necessário apenas informar o valor que a função receberá e o valor
# esperado como retorno. O restante do processo é automático, não será preciso alocar tanta atenção a ele.

# Além disso, o feedback é rápido. Com a execução dos testes, obtemos rapidamente o retorno com os pontos de melhorias do código.

# Outra vantagem é a segurança na alteração do código. Como os testes automatizados definem as regras de negócio que o
# projeto deve obedecer, há maior segurança ao trabalhar com um código que nunca vimos antes e
# modificá-lo (fazendo uma migração de um padrão de projeto para outro, por exemplo). Contanto que o novo código continue
# obedecendo às mesmas regras do código antigo, temos maior liberdade para alterá-lo sem problemas.

# Dessa forma, os testes automatizados influenciam a cultura da refatoração (refactoring), incentivando a melhoria contínua de código.

# A seguir, vamos comentar sobre os tipos de testes.

# Os testes unitários são responsáveis por averiguar o funcionamento de pequenas partes da
# aplicação (as menores unidades de um código), como um método ou uma classe.

# Os testes de integração, como o nome sugere, verificam a integração entre essas unidades menores que
# compõem o projeto, isto é, os trechos que testamos individualmente nos testes unitários.

# Os testes de ponta a ponta (End-to-End — E2E) aferem o bom funcionamento da aplicação inteira, desde o início até o final.
# Muitas vezes, esse teste simula o usuário da aplicação e o ambiente de produção em que o produto será colocado. 
#Trata-se de um teste mais abrangente, que compreende todo o processo da aplicação.

# Esses são os tipos de testes mais relevantes. Teremos mais conteúdos sobre esse tema no decorrer do curso e
# poderemos tirar dúvidas relacionadas aos tipos de testes. No caso, focaremos nos testes unitários.

# Voltando ao arquivo main.py, notaremos que o código que desenvolvemos é um teste unitário automatizado, visto
# que estamos analisando o funcionamento do método idade — uma pequena parte do código da Dominique.

# Contudo, nosso código testa um único cenário. Para testar outras situações, poderíamos incrementar o código
# com funcionario_teste1 e funcionario_teste2 com datas de nascimentos diferentes, por exemplo:

# from codigo.bytebank import Funcionario

# def teste_idade():
#     funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
#     print(f'Teste = {funcionario_teste.idade()}')

#     funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
#     print(f'Teste = {funcionario_teste1.idade()}')

#     funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
#     print(f'Teste = {funcionario_teste2.idade()}')

# teste_idade()

# Ao executar o arquivo, vamos obter o resultado esperado, porém o código ficou extenso e seria inconveniente incluir
# mais trechos diretamente no código a cada novo cenário que quiséssemos testar. Para melhorar a construção dos nossos testes,
# usaremos uma ferramenta chamada Pytest. Vamos conhecê-la 

#Teste Manual vs. Automatizado

# Existem profissionais de qualidade e analistas dedicados exclusivamente ao ramo de testes manuais.
# Mesmo assim, em alguns casos particulares, o uso de testes automatizados se faz mais relevante.

# Eis algumas das principais vantagens no uso de testes automatizados:

#Testes automatizados são mais rápidos
# Uma vez que já estão escritos, basta que sejam executados e,
# poucos segundos depois, já se tem o resultado positivo ou negativo daquilo que se está testando

#Testes automatizados são mais confiáveis
# Uma vez que são criados através de ferramentas e scripts que impõem um padrão de construção específico
# para todos, bem como, não ficam sujeitos a erro humano, já que não é necessária a supervisão humana em
# cada etapa do processo de execução do teste

#Testes automatizados são mais baratos?
# Nem sempre isso é uma realidade e, na maioria das vezes, testes automatizados são mais caros.
# Já que os testes dependem de níveis de automatização, isso pode levar à utilização de ferramentas
# mais específicas de criação de scripts e testes. Gerando mais custos.

#Testes automatizados são adaptáveis a contextos de produção?
# Esse é um dos escopos em que o teste manual obtém vantagem sobre o teste automatizado.
# Por serem realizados por um profissional que está a todo tempo supervisionando o ambiente de produção,
# os testes manuais acabam sendo mais elegíveis a se adaptarem às variáveis que possam surgir na utilização
# do projeto pelo usuário

#Para saber mais: mais sobre testes
#O conceito da utilização de testes no mundo de desenvolvimento de software é
# explorado extensivamente no mercado de trabalho de diversas linguagens de programação.
# Temos dois artigos que se estendem no conteúdo de testes em software

# Tipos de testes: quais os principais e por que utilizá-los?
# https://www.alura.com.br/artigos/tipos-de-testes-principais-por-que-utiliza-los

# Por que e o que é possível testar?
# https://www.alura.com.br/artigos/por-que-e-o-que-e-possivel-testar

