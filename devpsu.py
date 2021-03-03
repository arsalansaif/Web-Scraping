import requests
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/Pennsylvania_State_University"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_="infobox vcard")
data = []
tag_exclude = 'sup'
for tr in table.find_all('tr'):
	row={}
	table_header=[]
	for th in tr.find_all('th'):
		table_header.append(th.get_text())
	for index, info in enumerate(tr.find_all('td')):
			if info(tag_exclude):
				info.find(tag_exclude).decompose()
			if table_header!=[]:
				row["header"] =table_header[0]
				row["row"] = info.get_text()
	if row!={}:
		data.append(row)
for a in data:
	print(a)
with open('Campus.csv', 'w', newline='') as csvfile:
	writer = csv.DictWriter (csvfile, {"header","row"})
	writer.writeheader()
	for i in data:
		writer.writerow(i)