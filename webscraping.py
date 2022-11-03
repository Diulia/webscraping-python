import requests
from bs4 import BeautifulSoup

request_url = requests.get('https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude')

print(request_url.url)
print(request_url.status_code)

response = request_url
  
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
  
i = 0
  
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
        response = requests.get(link.get('href'))
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
  
print("All PDF files downloaded")