from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discordwebhook import Discord
import time
import json

driver = webdriver.Firefox()

cart_url = 'https://www.smythstoys.com/cart'
product_url = input('Please insert the product url:\n')

with open('profile.json', 'r') as f:
    profile = json.load(f)
    discord_webhook = profile["discordWebhook"]
    first_name = profile["firstName"]
    surname = profile["lastName"]
    email = profile["email"]
    mobile_number = profile["mobileNumber"]
    postcode = profile["postcode"]
    address1 = profile["address1"]
    city = profile["city"]
    card_number = profile["cardNumber"]
    expiry_month = profile['expiryMonth']
    expiry_year = profile['expiryYear']
    cvv = profile["cvv"]

card_number.strip()
card1 = card_number[:4]
card2 = card_number[4:8]
card3 = card_number[8:12]
card4 = card_number[12:]

webhook = Discord(url=discord_webhook)


def add_to_cart():
    out_of_stock = True
    while out_of_stock:
        driver.get(product_url)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        try:
            driver.find_element_by_name(
                'js-stockStatusCode').get_attribute('innerText') == 'inStock'
            driver.find_element_by_id('addToCartButton').click()
            print(' ----------------- | Item is in stock | ----------------- ')
            print(' ------------- | Attempting to add to cart | ------------- ')
            webhook.post(
                username="Smyths Restock",
                avatar_url="https://pbs.twimg.com/profile_images/1201814536459898880/TC3S7JHH.png",
                embeds=[{"title": "**In-stock Notification**",
                         "description": "___Please head over to browser to checkout.___\n\nSelect your cc's expiry month and year and click 'Place Order'"}]
            )
            out_of_stock = False
        except:
            print(f'[ {current_time} ]   Out of stock. Monitoring...')
            time.sleep(5)


def basket_checkout():
    driver.get(cart_url)
    driver.find_element_by_id('checkoutOnCart').click()
    driver.find_element_by_id('guest.email').send_keys(email)
    driver.find_element_by_id('guest.confirmEmail').send_keys(email)
    driver.find_element_by_class_name('guestCheckoutBtn').click()


def checkout():
    WebDriverWait(driver, 999).until(EC.presence_of_element_located(
        (By. ID, 'firstName'))).send_keys(first_name)
    driver.find_element_by_id('surname').send_keys(surname)
    driver.find_element_by_id('phone').send_keys(mobile_number)
    driver.find_element_by_id('find_address').send_keys(postcode)
    driver.find_element_by_id('addressSubmit').click()
    # wait until the page loads and asks for user to manually input address
    WebDriverWait(driver, 999).until(
        EC.presence_of_element_located((By.ID, 'line1'))).send_keys(address1)
    driver.find_element_by_id('city').send_keys(city)
    driver.find_element_by_id('pincode').send_keys(postcode)
    driver.find_element_by_id('addressSubmit').click()
    # wait until delivery option shows up
    WebDriverWait(driver, 999).until(EC.presence_of_element_located(
        (By.ID, 'deliveryMethodSubmit'))).click()
    # wait until payment form shows up
    WebDriverWait(driver, 999).until(
        EC.presence_of_element_located((By.ID, 'cardNumberPart1'))).send_keys(card1)
    driver.find_element_by_id('cardNumberPart2').send_keys(card2)
    driver.find_element_by_id('cardNumberPart3').send_keys(card3)
    driver.find_element_by_id('cardNumberPart4').send_keys(card4)
    driver.find_element_by_id('cardCvn').send_keys(cvv)
    driver.find_element_by_class_name('control__indicator').click()
    driver.find_element_by_xpath(
        '//*[@id="accordion"]/div/div/div/div[1]/div[3]/div/div/label[1]/div').click()
    print(' ++++++++ | Please manually select the expiry month and year of your card and hit "Place Order" button | ++++++++')


def main():
    add_to_cart()
    basket_checkout()
    checkout()


if __name__ == '__main__':
    main()
