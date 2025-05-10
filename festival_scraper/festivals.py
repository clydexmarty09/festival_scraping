from bs4 import BeautifulSoup as bs
import requests as rs


#TESTING TESTING

def noct():

 #1) grab website html
    nocturnal = rs.get('https://nocturnal.frontgatetickets.com/event/0jy7rh4vqbmp83ov').text
    #print(nocturnal)  # prints out html file 

    soup = bs(nocturnal, 'lxml')
    #print(soup.prettify())
    tags = soup.find_all('div', class_='ticket-price-section')
    
    prices = []

    for x in tags:
        name = x.get('data-eventname')
        price = float(x.get('data-price'))

        prices.append(price)

    GA_reg = min(prices)
    GA_sticker = max(prices)

    print("The current price for GA is: ", GA_reg)
    print("The current price for GA with the magnet is: ", GA_sticker)


def hardSummer():


    hard_summer = rs.get('https://hardsummer.frontgatetickets.com/event/nk2gp605pj48u9hw?utm_source=hsmf&utm_medium=saturday_ga&_gl=1*130yp9t*_gcl_au*ODM4MTY2OTY4LjE3NDY4NDExNjQ.*_ga*MTE5MDIxOTIxMC4xNzQ2ODQxMTY1*_ga_J0N9LSSK1L*czE3NDY4NDExNjQkbzEkZzEkdDE3NDY4NDEyNDMkajYwJGwwJGgw').text
    #print(hard_summer)
    soup = bs(hard_summer, 'lxml')
    #print(soup.prettify())
    
    sample_tag = soup.find_all('div', class_='ticket-price-section')
    #print(sample_tag.prettify())

    prices = []  # keep prices in here 

    for x in sample_tag:
        price = float(x.get('data-price'))
        prices.append(price)

    print("The price for Saturday GA is: ", min(prices))
    print("The price for Saturday GA with the sticker is: ", max(prices))
        

def main():

    print("It's alive!!")
    hardSummer()



main()
