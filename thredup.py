#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

''' After inputting the account information, the script will request and save the links of all target items. 
It will open Firefox to login, empty out all items in the account's cart, and re-add all linked items.
Note: The script requires Firefox to be installed and a Thredup account.'''

item_list = []

# Obtain Thredup login information.
def thredup_login():
    user_email = str(input('Please enter your Thredup email account. ' ))
    user_pass = str(input('Please enter your Thredup password. '))
    return (user_email, user_pass)

# Create a list for items to be added later.
def link_to_items():
    number = 1
    print('\nPlease paste the links of the items that \n''you would want added to the cart.\n')
    print('When you\'re done adding your items, type \"done\"\n')
    while True:
        add_this = input('Paste item link %d: ' % number)
        if add_this == 'done':
            print('Are you done? Please type "yes" or "no"\n')
            print('Here are your current links:\n')
            print("\n".join(item_list),'\n')
            answer = input('>>> ')
            if answer == 'yes':
                print('\nFinished compiling the list of items.')
                print('Now opening Web browser...\n')
                break
            elif answer == 'no':
                number += 1
                continue
            elif answer != 'yes' or answer != 'no':
                print('\nInvalid command. Please retry again.')
                number += 1
        else:
            item_list.append(add_this)
            number += 1
    return(item_list)
    
# Remove and re-add items to cart
class Cart:
    def cart_remove(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.thredup.com/login')
        username = self.browser.find_element_by_id('user_session_email')
        username.send_keys(user_email)
        password = self.browser.find_element_by_id('user_session_password')
        password.send_keys(user_pass)
        password.submit()
        self.browser.get('https://www.thredup.com/cart/edit')
        while True:
            try:
                remove_item = self.browser.find_element_by_xpath("//input[@class='remove' and @type='submit']")
                remove_item.click()
            except:
                print('Items emptied from cart...')
                print('Now adding items back...\n')
                break
    
    def cart_add(self):
        for link in item_list:
            try:
                self.browser.get(str(link))
                self.browser.implicitly_wait(1)
                add_item = self.browser.find_element_by_class_name('add-to-cart ')
                add_item.click()
            except:
                print('Nothing to be added.')
        print('Finished adding items.')
        self.browser.get('https://www.thredup.com/cart/edit')

def main():
    user_email, user_pass = thredup_login()    
    link_to_items()
    thred = Cart()
    thred.cart_remove()
    thred.cart_add()

if __name__ == '__main__':
    main()