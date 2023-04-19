# descobrimos como criar testes utilizando o Pytest, o framework de testes do Python.
# Aprendemos sobre a metodologia ágil Given-When-Then e algumas boas práticas na criação
# de nomes de testes — que devem ser o mais verbosos possível. Ou seja, já sabemos como criar um teste, na prática.

# Vamos relembrar como essa demanda chegou até nós. O chefe da Dominique havia solicitado uma nova funcionalidade no
# projeto, então implementamos o novo método sobrenome e, depois, geramos um teste para ele. A princípio, essa parece
# a forma mais lógica de trabalhar — se estamos criando um teste, queremos testar algo que já existe.

# No entanto, existe uma escola de pensamento que dita que é interessante desenvolvermos os testes para o código antes
# e a implementação depois. De início, esse raciocínio parece não fazer sentido, mas vamos procurar entendê-lo a seguir.

# Essa escola de pensamento é o Test-Driven Development (TDD) — em português, "desenvolvimento guiado por testes".
# No TDD, primeiro criamos um teste e depois seguimos para a implementação, para a criação do código ao qual o teste faz referência.

# Após desenvolvermos o código e ele passar no teste, avançamos para a refatoração. Esta etapa é importante porque,
# quando criamos um código para passar em um teste, o resultado pode não ser muito legível para outras pessoas desenvolvedoras
# ou não incluir boas práticas. Então, é interessante melhorar o código por meio da refatoração.

# Depois, voltamos a criar mais testes e completamos o ciclo do TDD — criar testes, implementar os códigos e refatorar.

# Vamos investigar esse ciclo mais a fundo a partir de uma narrativa.

# O chefe da Dominique pediu uma nova funcionalidade para o projeto. Utilizando o TDD, nosso primeiro
# passo é criar um teste, pois já sabemos o que a nova funcionalidade deve receber e o que ela deve
# retornar — essas informações estão nas regras de negócio que o chefe da Dominique nos explicou.

# É possível criar um teste apenas considerando a regra de negócio. Inclusive, essa é uma das vantagens
# do TDD: os testes acabam se tornando a espinha dorsal do projeto, uma base que tem ligação direta com as
# regras de negócio. Através deles, fica mais claro a quais regras de negócio o nosso código deve obedecer.

# Criados os testes, vamos executá-los. Em um primeiro momento, eles vão falhar, porque o código ainda não existe.
# Então, a próxima etapa é desenvolvê-lo e a nossa única meta é fazer com que os testes passem. Com esse objeto em mente,
# criaremos um código que faz o mínimo esforço necessário, dispensando estruturas extensas e complexas, de modo a simplificar o projeto.

# Uma vez que os testes passem, partimos para o estágio de refatoração. Já elaboramos os testes e o código que passa nesses
# testes, contudo é possível que o código não esteja muito bom, não esteja condizente com boas práticas de desenvolvimento
# ou não seja muito legível para outras pessoas da sua equipe, por exemplo. A refatoração é momento de melhorar o código,
# por exemplo, separá-lo em partes menores ou corrigir indentações.

# O TDD existe em muitas linguagens. No caso do Python, a indentação correta é imprescindível para que o código funcione.
# Em outras linguagens, ela pode não ser tão crucial, então pode ser ajustada apenas na refatoração, para aprimorar a
# estrutura do projeto.

# Realizada a refatoração, voltamos para a fase de testes. Por vezes, uma única funcionalidade requer vários testes,
# visto que pode ser aplicada em diversos contextos.

# Dessa forma, continuamos no ciclo de TDD: desenvolvemos um teste para um determinado segmento do projeto,
# elaboramos um código que passará nesse teste que dita as regras de negócio e refatoramos.

# Esse processo promove segurança para modificar códigos alheios, pois o essencial é que os testem passem,
# visto que eles definem as regras de negócio. Ou seja, o TDD melhora o trabalho em equipe de desenvolvedores.