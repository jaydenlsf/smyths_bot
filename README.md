# Smyths Checkout Bot
A simple Python script that uses Selenium to monitor a product. Once the item comes back in stock, the bot will attempt to add it to cart and checkout the basket.
   - Useful for trying to catch a Playstation 5 restock


### Requirements
- Download webdriver from https://chromedriver.chromium.org/downloads
- The script uses Firebox as the default browser
- If you would like to use Chrome instead, change line 9 in smyths_checkout.py to driver = webdriver.Chrome('INSERT THE PATH TO CHROME DRIVER HERE')

Install all dependencies
1. pip3 install selenium
2. pip3 install discordwebhook


### Instructions
1. Download profile.json and smyths_checkout.py and place both files in the same directory
2. Open profile.json using a text editor and insert the details
   - If you do not use discord, comment out line 35 and line 49 - 54 in smyths_checkout.py
   - However, it is highly recommended to setup a discord webhook so you can receive notifications when the desired item comes back in stock
3. Once you have the information filled in you are ready to go and go ahead and run the script
4. When the desired item becomes in stock, keep an eye on the browser until it reaches the last step at checkout, where you are required to manually select the expiry month and year  of your credit card from the drop down. Finally, make sure to hit the 'Place Order' button



### To do
- Figure out a method to automatically select credit card expiry month and year
