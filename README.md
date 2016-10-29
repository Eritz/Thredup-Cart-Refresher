# Thredup Cart Refresher

## Description

The idea behind Thredup is that items purchased are a first-come-first-served basis. Customers may want their items to remain in their carts until they decide to buy the products on a later date. Unfortunately, items placed inside the carts are automatically emptied out after 24 hours. To circumvent the 24 hour limit, customers manually remove the product, and quickly adds them back in. Now, imagine a customer having over 50 items of interest. It's tiring and bothersome to add each individual item. The Thredup Cart Refresher helps these troubled customers through automation.  


The Thredup Cart Refresher provides an easy to navigate GUI to help refresh items placed in an account's cart. The user only has to supply each Thredup product's link once. The program opens a browser, logins, and then begins automating the rest. It'll remove the product from the cart, go back to its link, and then adds it back. 

Working as of October 29, 2016. The program supports Firefox and Chrome browsers.

##Prerequisite

The program is built using Python 3.X. It operates only on Windows and requires the following library installed:
- selenium

## How to Use

1. Run th_gui.py
2. Enter login information (not saved)
3. Enter product links so the program can save them
4. Press the Start button, and follow any of the program's instruction
5. Rejoice that you saved time

## Notes to keep in mind
- All files must be in the same directory
- This program assumes the account already has items inside the cart
- The program does NOT save your email or password
- This program will NOT help with any purchases, and will NOT steal any of your personal information
- For periodic usage, it's recommended to export the inputted links using the GUI's export. To reuse the links, simply press the import button
- Results may vary based on connection speed. If so, tweak the delay parameter for WebdriverWait(browser, delay).

## Changelog

*v2.0.0*
- Complete code revamp with working tkinter GUI
  - Unfortunately, the code for running through the list of links and deleting that finished link follows a complexity of O(n^2). 
  - If the list gets freakishly long, say 500, then expect major delays.  

*v1.0.0*
- Code cleanup
