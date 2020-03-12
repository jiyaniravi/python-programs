import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(response.status_code)
print(len(response.text))

response = requests.get('https://automatetheboringstuff.com/files/ahdabdjbsd.txt')
response.raise_for_status()

