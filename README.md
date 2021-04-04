# AmazonBot
Check the amazon Price of an item and email you if the price is bellow a certain level
# Pre-Requirements
- You should have chrome installed in your computer   
- You should downlaod chrome driver matching the version of chrome you have installed on your computer   
# Change to do in the code
- First you should write the email you will be using to send an email from with the password or the 2 way authentication in the following line `server.login('email', 'password/2wayAuthentication')`
- You should write the email you will be using the send an email and the one you will be using to receive an email from in the following line `server.sendmail("email to send","email to receive",msg)`
- Change the path of the chrome driver and add the path of it location in the following line `driver = webdriver.Chrome(executable_path="D:/python project/chromedriver.exe", options=options)`
- You should add the URL of the item you want to track in the following line `URL = ""`
- Change the price limit to be notify with in the following line `Price = 200` 

# Acknowledge
Mario Khoury, Beirut Lebanon
