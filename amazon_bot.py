#web scraping
from bs4 import BeautifulSoup

#web browser
from selenium import webdriver

#enable to send emails
import smtplib





def send_mail(title):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    #establish a connection between 2 emails
    server.ehlo()

    #encrypt our connections
    server.starttls()

    server.ehlo()

    #username, password or the 2 way authentication
    server.login('email', 'password/2wayAuthentication')

    subject = 'Price fell down!'
    body = title + "\n Check the amazon link : " + str(URL)
    msg = f"Subject: {subject}\n\n{body}".encode('utf-8')


    server.sendmail(
        "email to send",
        "email to receive",
        msg
        )
    print("Hey email has been sent!")

    #close the connection
    server.quit()

def check_price(driver, URL,Price):
    #get the html page
    driver.get(URL)

    #save the source code in the html variable
    html = driver.page_source

    #parse the code with bs4 so we can use bs4 command on it
    soup = BeautifulSoup(html,'html.parser')

    #parse to find the title of the text
    title = soup.find(id="productTitle").get_text().strip()
    print(title)
    #parse the price to string
    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)
    #string price to fload price
    converted_price = float(price[1:])
    print(converted_price)

    #if price is lower than x send an email
    if(converted_price<Price):
        send_mail(title)




#not opening the web browser
options = webdriver.ChromeOptions()
options.headless = True

#get the driver
driver = webdriver.Chrome(executable_path="D:/python project/chromedriver.exe", options=options)

#URL place the amazon URL you want to check the price
URL = "https://www.amazon.com/Zumimall-Doorbell-Wireless-Detection-Waterproof%EF%BC%8CCloud/dp/B08C9QNTCH"

#email you if the price is less than that
Price = 200
check_price(driver,URL,Price)
