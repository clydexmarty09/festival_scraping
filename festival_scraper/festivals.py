from bs4 import BeautifulSoup as bs
import requests as rs


#TESTING TESTING
def error_msg():
    print("Invalid Input.")
    exit()

def noct():

 #1) grab website htmls
    nocturnal_GA = rs.get('https://nocturnal.frontgatetickets.com/event/0jy7rh4vqbmp83ov').text #grab website link for GA admission
    #print(nocturnal)  # prints out html file 
    soup1 = bs(nocturnal_GA, 'lxml')

    nocturnal_VIP = rs.get('https://nocturnal.frontgatetickets.com/event/d4ekm6gn25yxhav0').text #grab website link for VIP admission
    soup2 = bs(nocturnal_VIP, 'lxml')

    print("What kind of Tickets? (Select 1 or 2) ")
    print("1) GA")
    print("2) VIP")
    print("3 Camping Options")
    selection = int(input("Selection: "))

    if(selection == 1):  # display GA options and prices 
        print(selection, "was selected. Directing to GA options...")
      
        #print(soup.prettify())
        tags1 = soup1.find_all('div', class_='ticket-price-section')
        
        prices = []

        # loop over tags in GA section 
        for x in tags1:
            #name = x.get('data-eventname') we don't really need this 
            price = float(x.get('data-price'))

            prices.append(price)

        GA_reg = min(prices)
        GA_sticker = max(prices)

        print("The current price for GA is: ", GA_reg)
        print("The current price for GA with the magnet is: ", GA_sticker)
    elif(selection ==2):
        print(selection, "was selected. Directing you to VIP prices...")
        #print (soup2.prettify()) testing purposes 
        prices = []
        tags = soup2.find_all('div', class_='ticket-price-section')
        for y in tags:
            
            price = float(y.get('data-price'))
            prices.append(price)

        VIP_reg = min(prices)
        VIP_magnet = max(prices)

        print("The price for VIP is: ", VIP_reg)
        print("The price of VIP with the magnet is: ", VIP_magnet)

    elif(selection ==3):
        print("It works")    
    else:
        error_msg()

   


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
    #hardSummer()
    noct()



main()
