import requests
from bs4 import BeautifulSoup

url = 'https://portalrapmais.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    for texto in soup.find_all('h1'):
        print(texto.text)
        title = soup.title.text
        print(title)
else:
    print(f"Falha ao acessar a página. Status code: {response.status_code}")
    
    
    
