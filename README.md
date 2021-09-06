# Dados Livres: plataforma livre de dados abertos

A ideia de desenvolver o Dados Livres surgiu em 2018, mas o seu desenvolvimento
iniciou em 2019 como um projeto de pesquisa no IFRN. Assim, o projeto foi
idealizado e desenvolvido pela estudante
[Carolina Soares](https://gitlab.com/mariacarolinass) e orientado pelo professor
[Pedro Baesse](https://gitlab.com/pbaesse).

O Dados Livres é um ambiente web para catalogação de fontes de dados abertos
e aplicações cívicas por meio de colaboração coletiva. Além disso, o código do
projeto está disponibilizado no GitLab para contribuições gerais com o seu
software livre.

Alguns diferenciais do projeto é a praticidade, pois suas fontes e aplicações
são facilmente cadastradas na plataforma sem exigir nenhum conhecimento de
código. Outro diferencial é a ligação de fontes de dados abertos com as
aplicações cívicas, na sua página de perfil, e vice-versa.

Entre os planejamentos futuros do projeto é pretendido permitir cadastrar
artigos científicos e notícias que utilizam de dados abertos. Por fim, será
esperado que o Dados Livres possa criar um ambiente que facilite a
participação da população no controle social e difusão de dados abertos
para os mais diversos fins.

# Problemas conhecidos e possíveis melhorias

# Como instalar

Primeiro faça um fork do projeto!

Em seguida clone o repositório que você fez o fork:

```sh
$ git clone https://gitlab.com/seu-usuario/dados-livres
$ cd dados-livres
```

Instale o ambiente virtual venv:

```sh
$ sudo apt-get install python3-venv
```

Utilize o comando abaixo para criar o ambiente virtual de nome venv:

```sh
$ python3 -m venv venv
```

Para entrar no ambiente virtual:

```sh
$ source venv/bin/activate       (Linux)
$ source venv\Script\activate    (Windows)
```

Agora, instale a lista de bibliotecas no arquivo requirements.txt:

```sh
$ pip install -r requirements.txt
```

## Configurando o projeto

Inicie o banco de dados:

```sh
$ flask db init
$ flask db migrate -m "criando banco de dados"
$ flask db upgrade
```

Para rodar a aplicação utilize o comando:

```sh
$ flask run
```

Acesse no seu navegador o seguinte endereço abaixo:

```sh
http://localhost:5000/
```

Para contribuir com o projeto use:

```sh
$ git checkout -b "nome_da_branch"
$ git add
$ git commit
$ git push
```

# Lista de autores

Carolina Soares --> GitLab: [@mariacarolinass](https://gitlab.com/mariacarolinass) |
GitHub: [@mariacarolinass](https://github.com/mariacarolinass) | Telegram:
[@carols0](https://t.me/carols0)

Pedro Baesse --> GitLab: [@pbaesse](https://gitlab.com/pbaesse) |
GitHub: [@pbaesse](https://github.com/pbaesse) | Telegram:
[@pbaesse](https://t.me/pbaesse)

# Licença
Dados Livres é Licenciado sob Licença GPL-3.0.

# Contato

Entre em contato conosco [preenchendo o formulário neste link](https://dadoslivres.pythonanywhere.com/contact)
ou mande uma mensagem no [grupo do Dados Livres no Telegram](https://t.me/dadoslivres).
