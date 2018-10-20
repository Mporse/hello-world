# import libraries
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

# specifiy the url
quote_page = "http://www.biosite.dk/virksomheder/virksomheder.htm"
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page)

f = open(r"C:\Users\Porse\Desktop\biotek-virksomheder_i_DK.txt", "w")

for link in soup.findAll('a', attrs={'href': re.compile("htm$")}):
    if link.get('href').startswith("http:"):
        pass
    else:
        f.write(link.get('href') + ",")

f.close()

f2 = open(r"C:\Users\Porse\Desktop\biotek-virksomheder_i_DK.txt", "r")

company_list = f2.readline().split(",")
print("Antal virksomheder: " + str(len(company_list)))

f_2 = open(r"C:\Users\Porse\Desktop\biotek-virksomheder_i_DK_beskrivelser.txt", "w+")

quote_page2 = "http://www.biosite.dk/virksomheder/"

x = 1

for webpage in company_list:
    quote_page3 = quote_page2 + webpage
    # print(quote_page3)
    page2 = urlopen(quote_page3)
    soup2 = BeautifulSoup(page2)

    for text in soup2.findAll('p'):
        # print(text)
        if not str(text).startswith("<p><strong>Produkter:</strong>"):
            pass
        else:
            f_2.write(str(x) + ": " + company_list[x-1] + " - " + str(text)[len("<strong>Produkter:</strong>")+4:] + "\n")
    x = x + 1

f.close()
f2.close()
f_2.close()
