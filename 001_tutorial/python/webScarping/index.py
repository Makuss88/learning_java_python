from bs4 import BeautifulSoup
import requests

url = 'https://kalbi.pl'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

table = doc.find('section', class_="calCard-ententa")

day = table.find_all('a')

arr = []

for i in range(len(day)):
  arr.append(day[i].string)

print(arr)