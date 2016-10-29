from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Example of link format: https://www.thredup.com/product/14634388  '''

class Webpage(object):
    def __init__(self, username, password, links):
        self.username = username
        self.password = password
        self.links = links
        
    def browsertype(self, choice=1):
        if choice == 1:
            self.firefox = webdriver.Firefox()
            return self.firefox
        elif choice != 1:
            self.chrome = webdriver.Chrome(r'.\chromedriver_win32\chromedriver.exe')
            return self.chrome
            
    def login(self, browser, username, password):
        browser.get(r'https://www.thredup.com/login')
        browser.find_element_by_id('user_session_email').send_keys(username)
        browser.find_element_by_id('user_session_password').send_keys(password) #Can't use .submit() because of captcha
        
    def cart(self):
        '''Go to the cart url.'''
        pass
    
    def renew(self):
        '''Click remove, obtain the removed item's url, go to its url, then add it back in the cart. Delete from the list of links '''
        pass
    
    def close(self):
        '''End the browser session.'''
        pass

class Firefox(Webpage):
    def __init__(self, username, password, links, choice):
        Webpage.__init__(self, username, password, links)
        self.firefox = self.browsertype(choice)
        self.firefox.set_window_size(800, 700)
        self.login(self.firefox, username, password)
    
    def cart(self):
        self.firefox.get('http://www.thredup.com/p/cart')
    
    def renew(self, links):
        for link in links[:]:
            WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex']//a[@class='flex' and @href=\'" + link[23:] + '\']')))
            target = self.firefox.find_element_by_xpath("//div[@class='flex']//a[@class='flex' and @href=\'" + link[23:] + '\']') #thredup.com(/gettheresthere)
            target.find_element_by_xpath("../div[@data-radium='true']//span[text()='Remove']").click()
            self.firefox.get(link) # Go to url and add it back
            WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='twelve columns right-pane']//div[text()='Add To Cart']")))
            self.firefox.find_element_by_xpath("//div[@class='twelve columns right-pane']//div[text()='Add To Cart']").click()
            self.cart()
            links.remove(link)
        #Add a quit button
    def close(self):
        self.firefox.close()

class Chrome(Webpage):
    def __init__(self, username, password, links, choice):
        Webpage.__init__(self, username, password, links)
        self.chrome = self.browsertype(choice)
        self.chrome.set_window_size(800, 700)
        self.login(self.chrome, username, password)
    
    def cart(self):
        self.chrome.get('http://www.thredup.com/cart/edit')
        
    def renew(self, links):
        for link in links[:]:
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex']//a[@class='flex' and @href=\'" + link[23:] + '\']')))
            target = self.chrome.find_element_by_xpath("//div[@class='flex']//a[@class='flex' and @href=\'" + link[23:] + '\']') #thredup.com(/gettheresthere)
            target.find_element_by_xpath("../div[@data-radium='true']//span[text()='Remove']").click()
            self.chrome.get(link) # Go to url and add it back
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='twelve columns right-pane']//div[text()='Add To Cart']")))
            self.chrome.find_element_by_xpath("//div[@class='twelve columns right-pane']//div[text()='Add To Cart']").click()
            self.cart()
            links.remove(link)
    def close(self):
        self.chrome.close()
