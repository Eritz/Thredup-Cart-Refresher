#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

''' This script refreshes items added inside one's Thredup account's
cart. It first collects the links of each of the wanted items, removes the items from the cart,
and re-adds them back.
Note: Firefox MUST BE INSTALLED for this script to function.'''

item_list = []
cart_link = 'https://www.thredup.com/cart/edit'
user_email = str(input('Please enter your Thredup email account. ' ))
user_pass = str(input('Please enter your Thredup password. '))

# This opens up ThredUp's cart detail page and removes all the items.
class Cart:
    def cart_remove(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.thredup.com/login')
        username = self.browser.find_element_by_id('user_session_email')
        username.send_keys(user_email)
        password = self.browser.find_element_by_id('user_session_password')
        password.send_keys(user_pass)
        password.submit()
        self.browser.get(cart_link)
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
        self.browser.get(cart_link)

# This get a list of the links of items to be added into the cart.
def link_to_items():
    number = 1
    print('Please paste the links of the items that \n''you would want added to the cart.\n')
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

link_to_items()
thred = Cart()
thred.cart_remove()
thred.cart_add()