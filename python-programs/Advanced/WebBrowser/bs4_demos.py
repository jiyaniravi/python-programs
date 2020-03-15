import bs4
import requests

response = requests.get('https://www.google.com/')
response.raise_for_status()

formattedHTML = bs4.BeautifulSoup(response.text, 'html.parser')
#print(formattedHTML)

SIvCobValue = formattedHTML.select('#SIvCob')
print(SIvCobValue)