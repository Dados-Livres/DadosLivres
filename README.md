# Dados Livres - Plataforma de dados abertos

Dados Livres é uma plataforma livre que permite a catalogação de fontes de dados abertos e aplicações que fazem uso dessas informações por meio de colaboração coletiva. Além disso, Dados Livres, é um Software Livre licenciado sob Licença GNU General Public License Version 3 e seu código-fonte está dísponivel aqui no GitLab.

O projeto deu início no ano de 2019, foi quando começou o desenvolvimento e planejamento do Dados Livres pela estudante [Carolina Soares](https://gitlab.com/mariacarolinass) como um projeto de pesquisa, sendo realizado em uma das instituições do IFRN e orientado pelo Prof. Mr. [Pedro Baesse](https://gitlab.com/pbaesse). Um dos diferenciais do Dados Livres é a praticidade, pois suas fontes e aplicações podem ser facilmente cadastradas sem exigir nenhum conhecimento de código dos seus usuários, facilitando encontrar vários possíveis colaboradores, entretanto, o principal difirencial da plataforma é a suas bases de dados que podem ser ligadas as aplicações criadas e vice-versa. Além disso, entre o nosso planejamento de projeto pretendemos permitir cadastrar artigos científicos e notícias que utilizam dados abertos. 

A plataforma de dados abertos, visa disponibilizar informações abertas direcionadas a sociedade civil, gerando benefícios como o controle social, transparência pública, democracia, inovação cívica, combate a corrupção e vários outros.

# Problemas conhecidos e possíveis melhorias

# Como instalar

Faça um fork do projeto Dados Livres e em seguida clone o repositório Forkado por você:
```sh
$ git clone https://gitlab.com/pbaesse/dados-livres.git
$ cd dados-livres       (entre na pasta clonada)
```
Use um ambiente virtual para fazer as instalações utilizadas na aplicação - Virtualenv:
```sh
$ virtualenv venv
```
Para criar o ambiente virtual:
```sh
$ python3 -m venv venv
```
Para ativar o ambiente virtual:
```sh
$ source venv/bin/activate       (Linux)
$ source venv\Script\activate    (Windows)
```
E finalmente, instale a lista de pacotes da aplicação:
```sh
$ pip install -r requirements.txt
```
Criando o banco de dados:
```sh
$ flask db stamp head
$ flask db migrate -m "criei o banco de dados"
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
E-mail para contato: pbaesse@gmail.com

Outros meios de contato:
- Telegram: [carols0](https://t.me/carols0) ou [pbaesse](https://t.me/pbaesse)
