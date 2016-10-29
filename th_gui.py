import re
import tkinter as tk
import tkinter.scrolledtext
from tkinter import ttk

class ThredApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="givemeanimage.ico")
        tk.Tk.wm_title(self, "Thredup Cart Auto Refresher")
        
        self.t_links = []
        self.user_id = ''
        self.pass_id = ''
      
        container = tk.Frame(self) #Frame is the window. The container houses everything        
        container.pack(fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1) #0 is minimum size
        container.grid_columnconfigure(0, weight=1) #weight tells how much pixel to expand by
        
        self.frames = {}
        
        for element in (MainPage, RunPage, FirePage, ChromePage, ListPage, TextLinkField, SavePage):       
            frame = element(container, self)           
            self.frames[element] = frame #Create a key with the mainpage in the dict
            frame.grid(row=0, column=0, sticky = "nsew") # Allow the frame to be stretched
        
        self.show_frame(MainPage) # Run the below method to show it up

    def show_frame(self, cont):
        show_this = self.frames[cont]        
        show_this.tkraise() #from tk.Tk, pop it up
    
    def pop_up(self, text_title, text_message):
        popup = tk.Tk()
        popup.wm_title(text_title)
        message = ttk.Label(popup, text = text_message)
        message.pack(side='top', pady=10)
        message2 = ttk.Button(popup, text='Okay', command=popup.destroy)
        message2.pack(pady=10)
        #popup.mainloop()

            
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_menu = tk.Label(self, text="Main Menu")
        main_menu.pack(pady = 5, padx = 10)
        
        dl_button = ttk.Button(self, text="Start", width=23, command=lambda:controller.show_frame(RunPage))
        dl_button.pack(padx=10, pady=15)
        
        list_button = ttk.Button(self, text="Set Thredup Links", width=23, command=lambda:controller.show_frame(ListPage))
        list_button.pack(padx=10, pady=15)
        
        save_button = ttk.Button(self, text="Account Info", width=23, command=lambda:controller.show_frame(SavePage))
        save_button.pack(padx=10, pady=15)
        
        quit_button = ttk.Button(self, text="Quit", width=23, command=quit)
        quit_button.pack(padx=10, pady=15)

class RunPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        download_label = tk.Label(self, text="Choose a browser")
        download_label.pack(padx = 10, pady = 15)
        
        fire_button = ttk.Button(self, text="Firefox", width=23, command=lambda:controller.show_frame(FirePage))
        fire_button.pack(padx=10, pady=15)
        
        chrome_button = ttk.Button(self, text="Chrome", width=23, command=lambda:controller.show_frame(ChromePage))
        chrome_button.pack(padx=10, pady=15)
                
        back_button = ttk.Button(self, text="Back to main menu", width=23, command=lambda:controller.show_frame(MainPage))
        back_button.pack(padx=10, pady=15)

class FirePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        inst = tk.Label(self, text='Press Execute and complete the CAPTCHA. You\'ll be redirected to the homepage. Then press Okay on the box to let the program do the rest.')
        inst.pack(padx=10, pady=15)
        
        login_button = ttk.Button(self, text='Execute', width=23, command=lambda:self.begin(controller))
        login_button.pack(padx=10, pady=15)
        
        back_button = ttk.Button(self, text="Back", width=23, command=lambda:controller.show_frame(RunPage))
        back_button.pack(padx=10, pady=15)
    
    def begin(self, controller): #b/c controller.user):
        from th_web import Firefox
        shop = Firefox(controller.user_id,controller.pass_id, controller.t_links,1)
        temp = tk.Tk()
        temp.wm_title('Captcha')
        messaget = ttk.Label(temp, text = 'Press Okay after finishing the CAPTCHA')
        messaget.pack(side='top', pady=10)
        messaget2 = ttk.Button(temp, text='Okay', command=temp.destroy)
        messaget2.pack(pady=10)
        temp.wait_window(temp)

        self.action(shop, controller)
        temp2 = tk.Tk()
        temp2.wm_title('Done')
        messaget3 = ttk.Label(temp2, text = 'Finished renewing links! Press Okay (not X) to terminate the browser.')
        messaget3.pack(side='top', pady=15)
        messaget4 = ttk.Button(temp2, text='Okay', command=temp2.destroy)
        messaget4.pack(pady=10)
        temp2.wait_window(temp2)
        
        shop.close()
        
    def action(self, browser, controller):
            browser.cart()
            browser.renew(controller.t_links)
            
class ChromePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        inst = tk.Label(self, text='Press Execute and complete the CAPTCHA. You\'ll be redirected to the homepage. Then press Okay on the box to let the program do the rest.')
        inst.pack(padx=10, pady=15)
        
        login_button = ttk.Button(self, text='Execute', width=23, command=lambda:self.begin(controller))
        login_button.pack(padx=10, pady=15)
        
        back_button = ttk.Button(self, text="Back", width=23, command=lambda:controller.show_frame(RunPage))
        back_button.pack(padx=10, pady=15)
    
    def begin(self, controller): 
        from th_web import Chrome
        shop = Chrome(controller.user_id,controller.pass_id, controller.t_links,2)
        temp = tk.Tk()
        temp.wm_title('Captcha')
        messaget = ttk.Label(temp, text = 'Press Okay after finishing the CAPTCHA')
        messaget.pack(side='top', pady=10)
        messaget2 = ttk.Button(temp, text='Okay', command=temp.destroy)
        messaget2.pack(pady=10)
        temp.wait_window(temp)

        self.action(shop, controller)
        temp2 = tk.Tk()
        temp2.wm_title('Done')
        messaget3 = ttk.Label(temp2, text = 'Finished renewing links! Press Okay (not X) to terminate the browser.')
        messaget3.pack(side='top', pady=10)
        messaget4 = ttk.Button(temp2, text='Okay', command=temp2.destroy)
        messaget4.pack(pady=10)
        temp2.wait_window(temp2)
        
        shop.close()
        
    def action(self, browser, controller):
            browser.cart()
            browser.renew(controller.t_links)

class ListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        download_label = tk.Label(self, text="Insert your links. Example of link format is https://www.thredup.com/product/14619380")
        download_label.pack(padx = 10, pady = 15)
        
        textlink_button = ttk.Button(self, text="Enter links", width=23, command=lambda:controller.show_frame(TextLinkField))
        textlink_button.pack(padx = 10, pady = 15)           
        
        popout_links = ttk.Button(self, text="Currently saved links", width=23, command=lambda:self.listoflinks(controller))
        popout_links.pack(padx = 10, pady = 15)
        
        export_button = ttk.Button(self, text="Export current links to .txt", width=23, command=lambda:self.export(controller))
        export_button.pack(padx = 10, pady = 15)
        
        import_button = ttk.Button(self, text="Import links from .txt", width=23, command=lambda:self.imp(controller))
        import_button.pack(padx = 10, pady = 15)
          
        back_button = ttk.Button(self, text="Back to main menu", width=23, command=lambda:controller.show_frame(MainPage))
        back_button.pack(padx = 10, pady = 15)
        
    def listoflinks(self, controller):
        listbox = tk.Tk()
        listpopout = tk.Text(listbox)
        for num, x in enumerate(controller.t_links):
            listpopout.insert('end',str(num+1) + ' - ' + x + '\n')
        listpopout.pack()
        listpopout.mainloop()
        
    def export(self, controller):
        exported_file = open('exported_links.txt', 'w')
        for link in controller.t_links:
            exported_file.write(link + '\n')
        exported_file.close()
        controller.pop_up('Done', 'Finished Exporting to .txt file')
    
    def imp(self, controller):
        imported_file = open('exported_links.txt', 'r')
        check1 = re.compile(r'thredup.com')
        for line in imported_file:
            if line != '' and check1.search(line) != None:
                    controller.t_links.append(line.rstrip('\n'))
        imported_file.close()
        controller.pop_up('Done', 'Finished Importing from .txt file')
               
class TextLinkField(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        textbox = tkinter.scrolledtext.ScrolledText(self, borderwidth=3, relief="sunken")
        textbox.config(font=("consolas", 12), undo=True, wrap='word')
        textbox.grid(row=0, column=0, padx=2, pady=2)     
        
        getlinks_button = ttk.Button(self, text='Save input', command=lambda:self.retrieve_input(textbox, controller))
        getlinks_button.grid(row=2, column = 0, pady=5)
        
        back_linkpage = ttk.Button(self, text='Back', command=lambda:controller.show_frame(ListPage))
        back_linkpage.grid(row=2, column = 1)
    
    def retrieve_input(self,box,store):
        lines = box.get("1.0", tk.END).splitlines()
        check1 = re.compile(r'thredup.com')
        if '' in lines:
            del lines[lines.index('')]
        for i in list(set(lines)):
            i = i.strip()
            if check1.search(i) != None:
                store.t_links.append(i)
        store.pop_up('Saved', 'Finished Saving! Press "Okay" and "Back".')
        
class SavePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        download_label = tk.Label(self, text="This will temporarily save User Name and Password")
        download_label.pack(pady = 5, padx = 10)
        
        savedir_button = ttk.Button(self, text='Enter information', width=23, command=lambda:self.save_screen(controller))
        savedir_button.pack(padx=10, pady=15)        
        
        currentset_button = ttk.Button(self, text='Currently saved information', width=23, command=lambda:self.show_save(controller))
        currentset_button.pack(padx=10, pady=15)
                         
        back_button = ttk.Button(self, text="Back to main menu", width=23, command=lambda:controller.show_frame(MainPage))
        back_button.pack(padx=10, pady=15)
    
    def show_save(self, controller):
        acct_pop = tk.Tk()
        acct_pop.wm_title('Currently stored')
        info = tk.Text(acct_pop)
        info.insert('end', 'User: ' + controller.user_id + '\n' + 'Password: ' + controller.pass_id)
        info.pack()
        info.mainloop()
    
    def save_screen(self, controller):
        prompt = tk.Tk()
        prompt.wm_title('User Settings')
        tk.Label(prompt, text='User ID', width=10).grid(row=0)
        tk.Label(prompt, text='Password', width=10).grid(row=1)
             
        ent1 = ttk.Entry(prompt)
        ent2 = ttk.Entry(prompt, show='*')
        ent1.grid(row=0, column=1, pady=2)
        ent2.grid(row=1, column=1)
        
        saveset_button = ttk.Button(prompt, text='Save', command=lambda:self.save_info(ent1, ent2, controller))
        saveset_button.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, sticky='nsew')
        
        prompt.mainloop()
    
    def save_info(self, e1, e2, controller):
        controller.user_id = e1.get()
        controller.pass_id = e2.get()
        controller.pop_up('Done', 'Finished Saving!')
        
app = ThredApplication()
app.mainloop()