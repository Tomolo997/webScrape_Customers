import requests
from bs4 import BeautifulSoup
import csv

f = open("naloga.txt", "a")
#requestamo in gremo na naslednjo spletno stran
r = requests.get("https://retool.com/customers/")
#poberemo content iz splente strani 
soup = BeautifulSoup(r.content,"lxml")

#inicializiramo data, katera bo predstavljana podatke, ki jih bomo vpisovali v CSV file.
data = []
#najdemo slike na splenti strani glede na njihov class.
for img in soup.find_all('img', class_='customerLogos__CustomerLogoItem-sc-1e2rx4q-4 cdMMEN'):
    #razdelimo src glede na "/"
    x = img['src'].split("/")
    #Izberemo zadnji element 
    lastElement = x[len(x)-1]
    #company name dobimo tako, da splitamo string glede na "." in vzamemo prvi element.
    companyName = lastElement.split(".")[0]
    #link dobimo tako postavimo companyName med https:// in .com 
    link = "https://" + companyName + ".com"
    #link do logotipa pa je enak trenutni domeni + srcju imegaja
    srcLink = "https://retool.com/" + img['src']
    #Objekt customer vstavimo v data.
    customer = {
        "domena":link,
        "logotipLink":srcLink,
        "companyName":companyName
    }
    data.append(customer)
fieldnames = ['domena', 'logotipLink', 'companyName']

#odpremo csv file in v njega vpisemo podatke
with open('customers.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
