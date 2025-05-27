from bs4 import BeautifulSoup as bs
import requests as rs


#TESTING TESTING

def exit_command(): # if the user decides to exit 

    print("Exiting...")
    exit()

def error_msg():  # call this function for bad inputs 
    
    print("Invalid Input.")

def noct():

 #1) grab website htmls
    nocturnal_GA = rs.get('https://nocturnal.frontgatetickets.com/event/0jy7rh4vqbmp83ov').text #grab website link for GA admission
    #print(nocturnal)  # prints out html file 
    soup1 = bs(nocturnal_GA, 'lxml')

    nocturnal_VIP = rs.get('https://nocturnal.frontgatetickets.com/event/d4ekm6gn25yxhav0').text #grab website link for VIP admission
    soup2 = bs(nocturnal_VIP, 'lxml')

    camping = rs.get('https://nocturnal.frontgatetickets.com/event/e2i910hiqcxfo47c').text  #grab the website for the camping passes
    soup3 = bs(camping, 'lxml')

    print("What kind of Tickets? (Select 1 or 2) ")
    print("(1) GA")
    print("(2) VIP")
    print("(3) Camping Options")
   
    # declare some boolean variable for while program running 
    running = True   

    # declare some while loop to keep selecting options 
    while (running): # keep looping until the user decides to exit

        selection = int(input("Press 1 for GA, 2 for VIP, 3 for camping options, or 0 to exit: "))
        
        if (selection == 0): #exit command 

            exit_command()

        elif(selection == 1):  # display GA options and prices 
            
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

        elif(selection ==2): # this takes use VIP options 

            print(selection, "was selected. Directing you to VIP prices...")
            #print (soup2.prettify()) testing purposes 
            prices = []
            tags = soup2.find_all('div', class_='ticket-price-section')
            for y in tags:
                
                price = float(y.get('data-price'))
                prices.append(price)

        # lines below takes the minimuma and maximum of both prices
            VIP_reg = min(prices)
            VIP_magnet = max(prices)

            #print(prices) # prints the list containing the prices for testing purposes

            print("The price for VIP is: ", VIP_reg)
            print("The price of VIP with the magnet is: ", VIP_magnet)
            
        elif(selection ==3): # this is for camping tickets 
            #print("It works")    
            print(selection, "was selected. Directing you to camping prices...")
            tags_title = soup3.find_all('div', class_='ticket-price-section')
            
            # this line is for testing purposes -----------------------
            price = soup3.find_all('div', class_= 'ticket-price-section')

            prices = []
            for p in price:
                price = p.get('data-price')
                prices.append(price)

                #print(price)

            # end more tests ------------------------------------------------

            names = []
            for z in tags_title: 
                name = z.get('data-name')
                names.append(name)
                #print(name.strip())  # strip() trims the whitespace 

            # Match corresponding name with price. Let's use a dictionary (USE ZIP)
            names_prices = dict(zip(names, prices))
            for n, p in names_prices.items():  # loop over the items 
                print(f"{n}:{p}")  # prints pairs of names and prices

        else:
            error_msg()  
        
        # lines below keep looping if the user wants to stay in the same menus 
        back = input("Go Back? Y/N: ")
        back == back.upper()
        if(back == 'Y'): 
            print("Going back...")
            break
        elif(back == 'N'): continue

    # --------------- we would end the while here ------------------

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
    running = True 

    while(running):
        #festival_choice = int(input("Choice: "))
        # Start a while loop to keep selecting stuff 
        user_input = input("Select (0) to exit, (1) for Nocturnal, (2) for HARD Summer: ")
       
        # try -> except for error checking 
        try: 
            
            festival_choice = int(user_input)
        
        except ValueError:  # input was not expected (int)
            
            error_msg()
            continue  # go back to top of the loop 

        if(festival_choice == 0): 
            running = False
            exit_command()
       
        elif(festival_choice == 1):
            noct()
        elif(festival_choice == 2):
            hardSummer()
        else:
            error_msg()
            
    # ----------------- end while loop here  -----------------



main()
