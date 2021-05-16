# Import the libraries
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

# Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
    # Get the URL
    url = 'https://www.coindesk.com/price/'+coin

    # Make requests to the website
    HTML = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')

    # Find the current price
    text = soup.find('div', attrs={'class': 'coin-info-block'}) \
        .find('div', attrs={'class': 'data-definition'}) \
        .find('div', attrs={'class': 'price-large'}).text
    # Return the text

    return text

def main():
    last_price = -1
    # Create a loop to continously get price updates
    while True:
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)
        # Which crypto - make a list
        cryptolist = ['bitcoin', 'ethereum', 'xrp',
                      'dogecoin', 'cardano', 'stellar']
        # Print a heading for each price refresh containing the date and time
        print('Price update ' + dt_string)
        # get the price
        for x in range(len(cryptolist)):
            price = get_crypto_price(cryptolist[x])
            # Check if the price changed
            if price != last_price:
                if len(cryptolist[x]) > 3:
                    # if the crypto name is not listed as 3 chars, make it proper case
                    print(cryptolist[x].title() + ': ', price)
                else:
                    # if the crypto name is 3 chars or less, make it all upper case
                    print(cryptolist[x].upper() + ': ', price)
                last_price = price
            else:
                print('no change...' + dt_string)
        # Check again every hour
        time.sleep(3600)


# Run the main function
main()
