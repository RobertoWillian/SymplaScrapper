# Web Scraping de Eventos com Python

""Web Scraping" é a prática de coletar dados por qualquer meio que não seja um programa interagindo com uma API (ou, obviamente, por um ser humano usando um navegador web). Isso é comumente feito escrevendo um programa automatizado que consulta um servidor web, requisita dados (em geral, na forma de HTML e de outros arquivos que compõem as páginas web) e então faz parse desses dados para extrair as informações necessárias." (Fonte: MITCHELL, Ryan. Web Scraping com Python. 2ed. São Paulo: Novatec, 2019.).

Neste projeto, alunos da matéria "Projeto de Linguagens de Programação", lecionada no curso de Ciência da Computação da UDF, tem como objetivo fazer um web scraping da plataforma de eventos "Sympla", captando os eventos de tecnologia e os listando em uma plataforma própria, que servirá como um HUB. 

HUB este que centralizará algumas propostas e temas (feitos por outros alunos da matéria) para auxiliar os demais alunos dos cursos de tecnologia a ter um melhor desempenho acadêmico, profissional e auxiliar a aumentar o networking.

## ☕ Funcionalidades da Solução e Requisitos Funcionais:
1. Extração de Dados dos Eventos:
* A aplicação deve ser capaz de acessar eventos por meio de plataformas como Sympla ou Google Eventos, realizando consultas periódicas e enviando as informações à aplicação principal. Para isso, será utilizada a biblioteca Selenium do Python, extraindo dados essenciais como nome do evento, local, data e hora.
* É necessário realizar uma higienização dos dados obtidos, garantindo que sejam consistentes e úteis.
* Os dados brutos devem ser transformados em informações estruturadas, que podem ser armazenadas em um banco de dados ou planilhas para posterior análise.

2. Acesso aos Eventos
* As informações devem ser exibidas de forma clara e acessível ao usuário.

3. Filtragem dos Dados
* O usuário deve ter a capacidade de filtrar os dados de maneira dinâmica e intuitiva, podendo selecionar quais informações deseja visualizar e como elas serão apresentadas.


## 💻 Ajustes e melhorias

O projeto está na sua primeira versão e possui como sugestões de melhorias:

- [x] Capturar todas as páginas disponíveis ao filtrar por "tecnologia" no sympla
- [ ] Filtrar os eventos por tecnologia, como: java, python, eventos acadêmicos, feiras, amostras..
- [ ] Capturar eventos de outros sites relevantes para a área da tecnologia
- [ ] Possuir um link de redirecionamento para o evento na nossa página web


## 🛠️ Tecnologias utilizadas

* [Python](https://www.python.org/) - A linguagem utilizada
* [Angular](https://angular.dev/) - Framework web


## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

-- Python 3

Bibliotecas Python:
* Selenium
* FastAPI
* Uvicorn
  
-- Angular (v18)


## 🚀 Como utilizar

Como rodar o aplicativo:
  
1. Clone este repositório `$ git clone <https://github.com/RobertoWillian/SymplaScrapper.git>`
2. Acesse a pasta do projeto no terminal/cmd `$ cd Scrapper`
3. Garanta que as bibliotecas do python estejam baixadas: Selenium, FastAPI e Uvicorn
4. Acesse a pasta do projeto no terminal/cmd `$ python -m uvicorn main:app --reload`
5. Acesse a pasta do projeto no terminal/cmd `$ cd FrontEnd`
6. Instale as dependências `$ npm Scrapper`
7. Execute a aplicação em modo de desenvolvimento `$ npm start`
8. O servidor iniciará na porta: 4200 - acesse <http://localhost:4200>


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.

## ✒️ Autores

* **Ana Carolina Barbosa de Souza** - [github](https://github.com/anacarolbs) e [linkedin](https://www.linkedin.com/in/anacarolbs/)
* **Guilherme Rodrigues Bastos** - [github](https://github.com/EGG1203) e [linkedin](https://www.linkedin.com/in/guilhermebastosgg)
* **Leonardo Ferreira Rodrigues** - [github](https://github.com/leonxrdofr) e [linkedin](https://www.linkedin.com/in/leonardo-ferreira-rodrigues-8247ab239)
* **Marcus Vinicius Portela da Costa** - [github](https://github.com/marcusportela) e [linkedin](https://www.linkedin.com/in/marcusportelamp/)
* **Robert Willian Costa Silva** - [github](https://github.com/RobertoWillian) e [linkedin](https://www.linkedin.com/in/robert-willian-costa-silva)


