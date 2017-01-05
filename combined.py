import requests
from bs4 import BeautifulSoup



def retrieval(url):
    page = requests.get(url)
    souped = BeautifulSoup(page.text)
    tag = souped.find_all(class_='carbrandpage')[0].find_all(class_='clearfix')
    cars = {}

    for tags in tag:
        name = tags.find_all('h3')[0].text.strip()
        price = tags.find_all(class_='price')[0].text

        if name in cars.keys():
            pass
        else:
            print "Name of the car is %s and the cost is %s" %(name, price)

def main():

    input = int(raw_input("""Which brand ? \n Press 0 for Hyundai \n Press 1 for Maruti
                           \n Press 2 for Skoda \n Press 3 for BMW \n Press 4 for Tata
                          \n Press 5 for Honda"""))
#    url = ["https://www.cardekho.com/cars/Hyundai","https://www.cardekho.com/cars/Maruti",
#          "https://www.cardekho.com/cars/Skoda","https://www.cardekho.com/cars/bmw",
#           "https://www.cardekho.com/cars/tata","https://www.cardekho.com/cars/honda"]
    base = "https://www.cardekho.com/cars/"
    url = ["hyundai","maruti","skoda","bmw","tata","honda"]
    x = base+url[input]
    if input == 0:
        retrieval(x)
    if input == 1:
        retrieval(x)
    if input == 2:
        retrieval(x)
    if input == 3:
        retrieval(x)
    if input == 4:
        retrieval(x)
    if input == 5:
        retrieval(x)



main()
