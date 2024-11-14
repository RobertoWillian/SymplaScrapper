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
    driver.get('https://www.sympla.com.br/eventos/brasilia-df?s=tecnologia')
    return paginar()  # Retorna o JSON gerado pela função paginar

# Função que coleta os dados da página e os adiciona às listas
def coletar_dados():
    # Coleta os títulos dos eventos dentro da página e insere dentro de uma lista
    for titulo in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventTitle-sc-1rkzctc-7'):
        titulos.append(titulo.text)

    # Coleta a data dos eventos dentro da página e insere dentro de uma lista
    for data in driver.find_elements(By.CLASS_NAME, 'sc-1sp59be-0'):
        datas.append(data.text.replace("\n", " - "))

    # Coleta os endereços dos eventos dentro da página e insere dentro de uma lista
    for endereco in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventLocation-sc-1rkzctc-8'):
        if (endereco.text != "- ,"):
            enderecos.append(endereco.text)
        else:
           enderecos.append("Online")
# Função recursiva para seguir a paginação
def paginar():
    # Coleta dados da página atual
    coletar_dados()

    # Verifica se o botão de "Próxima Página" está presente
    try:
        botao = driver.find_element(By.CLASS_NAME, "hNyJjx")
        driver.execute_script("arguments[0].scrollIntoView();", botao)
        sleep(2)
        driver.execute_script("arguments[0].click();", botao)
        sleep(2)  # Espera 2 segundos para o próximo carregamento
        return paginar()  # Chama a função recursivamente para a próxima página

    except:
        # Caso não haja mais páginas, gera o JSON com os dados coletados
        eventos = [{"Titulo": titulo, "Data": data, "Endereco": endereco} for titulo, data, endereco in zip(titulos, datas, enderecos)]
        titulos.clear()
        datas.clear()
        enderecos.clear()
        with open('eventos.json', 'w', encoding='utf-8') as file:
            json.dump(eventos, file, ensure_ascii=False, indent=4)
        return eventos
