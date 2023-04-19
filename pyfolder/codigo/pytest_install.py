# Instalação do Pytest -> Framework Especializado em Testes (o unitest tbm e usado mas o pytest e mais pythonico)
#Vantagens
#Multiplos Plugins
#Altamente Escalavel
#Utilizacao Muito Simples somentes alguns comandos no terminal consigo executar todos os codigos que eu quero

# Na última aula, criamos o arquivo main.py e desenvolvemos nosso primeiro teste automatizado,
# elaborando alguns cenários para testar o método idade da classe Funcionario criada pela Dominique.
# Os códigos funcionaram como esperado, entretanto, não é uma boa prática criarmos testes dessa forma.

# A maioria das linguagens de programação tem ferramentas e bibliotecas destinadas à criação de testes.
#  Para o Python, temos o Pytest, um framework especializado em testes. Antigamente, usava-se mais o unittest
#  para essa finalidade, mas o Pytest chegou para oferecer uma alternativa mais "pythônica". O primeiro release
#  dele foi em 2019 e até hoje ele é um dos principais frameworks de testes para Python.

# Uma das vantagens do Pytest é possuir múltiplos plugins, extensões. Temos um pacote de ferramentas inclusas
#  no Pytest para realizar testes dos mais variados tipos e personalizar nossa interação com o código.

# Além disso, esse framework é altamente escalável, comportando desde aplicações pequenas até projetos maiores,
#  com hierarquias complexas, diversos módulos e muitos diretórios.

# Não bastasse, a utilização do Pytest é muito simples. Com poucos comandos no terminal, conseguimos executar
# todos os testes que queremos.

# Neste vídeo, prepararemos o ambiente para usar esse recuso. O primeiro passo é instalar o Pytest.
#  Abrindo o terminal, caso não estejamos no ambiente virtual, vamos ativá-lo com o comando source venv/bin/activate.
#  Em seguida, por meio do instalador de pacotes pip, instalaremos o Pytest na versão atual (7.1.2):

# # pip install pytest==7.1.2

# Executando o comando pip freeze no terminal, receberemos uma lista de todos os pacotes instalados
# no nosso ambiente virtual. É uma boa prática criarmos um arquivo .txt para reunir as informações de
# tudo que estamos instalando, para manter a organização do nosso projeto. Posteriormente, se outra pessoa
# quiser reproduzi-lo, basta consultar esse documento.

# Portanto, vamos rodar o comando pip freeze > requirements.txt para gerar esse arquivo.
# Na sequência, podemos consultá-lo na estrutura de pastas, no painel à esquerda, e verificar
# que o pytest==7.1.2 que instalamos há pouco já consta nessa lista. À medida que instalarmos mais
# pacotes, atualizaremos esse documento.

# Com o Pytest instalado, vamos organizar o local onde colocaremos os testes. No painel à esquerda,
# dentro do projeto bytebank-tdd, criaremos um diretório chamado tests. É essencial usar o nome
# tests (com letras minúsculas, no plural e em inglês); do contrário, o Pytest pode não reconhecer
# que este é o diretório de testes!

# Dentro do diretório tests, criaremos um arquivo chamado __init__.py. No Python, quando colocamos
# um elemento entre underlines (dois underlines no início e dois no final), chamamos de dunder.
# No caso do nosso arquivo, falamos "dunder init".

# O arquivo __init__.py é necessário porque o diretório tests é um módulo.
# Para considerarmos um módulo no Python, é preciso ter um diretório e, dentro dele,
# um arquivo dunder init. É assim que o Pytest reconhece que esta é a pasta de testes.
# O arquivo __init__.py pode permanecer vazio.

# Dentro do diretório tests (nosso módulo de testes), criaremos outro arquivo,
# chamado tests_bytebank.py — este será o documento em que faremos os testes.

# O ambiente está pronto! No próximo vídeo, vamos "traduzir" os testes que desenvolvemos
# no main.py para o formato que ele teria com o Pytest.