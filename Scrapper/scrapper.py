import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Listas para armazenar os dados
titulos = []
datas = []
enderecos = []

def get_eventos_scrapper():
    # Abre a URL da página
    driver.get('https://www.sympla.com.br/eventos?s=Tecnologia')
    return paginar(1)  # Retorna o JSON gerado pela função paginar

# Função que coleta os dados da página e os adiciona às listas
def coletar_dados():
    # Coleta os títulos dos eventos dentro da página e insere dentro de uma lista
    for titulo in driver.find_elements(By.CLASS_NAME, 'pn67h18'):
        titulos.append(titulo.text)

    # Coleta a data dos eventos dentro da página e insere dentro de uma lista
    for data in driver.find_elements(By.CLASS_NAME, 'qtfy414'):
        print(data.text)
        datas.append(data.text.replace("\n", " - "))

    # Coleta os endereços dos eventos dentro da página e insere dentro de uma lista
    for endereco in driver.find_elements(By.CLASS_NAME, 'pn67h1a'):
        if (endereco.text != "- ,"):
            enderecos.append(endereco.text)
        else:
           enderecos.append("Online")
# Função recursiva para seguir a paginação
def paginar(IsPrimeiraPagina : bool):
    # Coleta dados da página atual
    coletar_dados()

    botoes = driver.find_elements(By.CLASS_NAME, "swraze2")

    if len(botoes) > 1:
        botao = botoes[1]  # Seleciona o segundo botão (Equivalente ao botão "Próximo no Sympla")
    elif (len(botoes) == 1) and (IsPrimeiraPagina == 1):
        botao = botoes[0]  # Seleciona o único botão disponível na primeira página
        IsPrimeiraPagina = 0 #Define que o navegador não está mais na primeira pagina
    else:
        # Caso não haja mais páginas, gera o JSON com os dados coletados
        eventos = [{"Titulo": titulo, "Data": data, "Endereco": endereco} for titulo, data, endereco in zip(titulos, datas, enderecos)]
        titulos.clear()
        datas.clear()
        enderecos.clear()
        with open('eventos.json', 'w', encoding='utf-8') as file:
            json.dump(eventos, file, ensure_ascii=False, indent=4)
        return eventos  
         
    driver.execute_script("arguments[0].scrollIntoView();", botao)
    sleep(2)
    driver.execute_script("arguments[0].click();", botao)
    sleep(2)  # Espera 2 segundos para o próximo carregamento
    return paginar(IsPrimeiraPagina)  # Chama a função recursivamente para a próxima página


