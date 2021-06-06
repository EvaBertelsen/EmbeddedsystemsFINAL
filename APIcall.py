import tkinter as tk #for gui creation all the visuals
import requests #for the apicall 
import json # formatting the api response so its easy to work with
from time import sleep # not used here but if we want to make it sleep its a good libray 
import os #finds the localy stored apikey
import threading

# creating a calss using tk.frame so that we have everything inside put into out frame
class weatherGui(tk.Frame):
    # making a root with the pack, grid, place and create_widget so that they are all at out command inside
    # we make the master = root as we can se at the bottom of the script so everything is rooted in the tk.Frame
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.grid()
        self.place()
        self.create_widgets()

# the function where we make all our widgets in
    def create_widgets(self):

        root.geometry("800x500")#sets the tkinter window to 800x500 when starting.
        root.title("weatherGui")#renames the window from tkinter to WeatherGui
        
        self.background_img = tk.PhotoImage(file="C:/Users/Michal/Desktop/Dania edukacja/IoT/IoT project/Iot project/kod/800x500weahter.png")#finds the image specifed and stores it in a variable
        self.background_label = tk.Label(image=self.background_img)# making it into a label that can be showed on the tkinter interface
        #inorder to not have any ugly background I went with this method. making a canvas and stroing everything in there,
        #makes the backgrounds nice and smooth
        # I fill it out and expand it so it fits the 800x500
        # and give it the image variable to use so we have an image background 
        self.my_canvas = tk.Canvas(self, width=800, height=500)
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0,0, image=self.background_img, anchor="nw")

        self.input_field = tk.Entry(self, width=30, relief="solid")# This is the input field where we add the cities.
        self.input_field_window = self.my_canvas.create_window(600,100, anchor="nw", window=self.input_field)# we creat the entry bar in the canvas this is like pack() but in canvas

        # Making the button that triggers the apicall.
        self.update_button = tk.Button(self)
        self.update_button["text"] = "show me the weather \n (click me)"# Text on the button
        self.update_button["command"] = lambda: self.piapicall(self.input_field.get())# Here we trigger the call. Lambda makes it so we can start the gui without having a value on self.input_field.get()
                                                                                      # we also read the input that the user types in the entry box and sends that to the apicall function
        self.update_button["bg"] = "black" #bg = background
        self.update_button["fg"] = "white"#fg = foregorund
        self.update_button_window = self.my_canvas.create_window(600, 125, anchor="nw", window=self.update_button)# Adding it to the canvas
        
        # Creating a label that shows us the output from the api call
        self.little_label = tk.Label(self)
        self.little_label = tk.Label(self,bg="white", width=50, height=20, anchor="center", relief="solid")# visuals
        self.little_label_window = self.my_canvas.create_window(225,100, anchor="nw", window=self.little_label)# putting it in the canvas

        
        # Making a quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)# giving it the master.destroy= close the running gui
        self.quit_window = self.my_canvas.create_window(10,450, anchor="nw", window=self.quit)# adding it to the canvas
        
        
        self.home_label = tk.Label(self)
        self.home_label = tk.Label(self,bg="white", width=25, height=20, anchor="center", relief="solid")# visuals
        self.home_label_window = self.my_canvas.create_window(25,100, anchor="nw", window=self.home_label)# putting it in the canvas
        back_home_loop = threading.Thread(name='background', target=self.homeApicall)
        back_home_loop.start()
    
    def homeApicall(self):
        while True:
            home_url = "http://10.0.100.213"

            home_res = requests.get(home_url).json()
        
            self.home_label['text'] = home_call_format(home_res)
            sleep(5)

    def piapicall(self, city):
        apikey = ('82592f29172c2cb9e948abb6f67c6c4b') # Here i have hidden my Apikey in a variable that i store locally so that it wont send out in clear text
        url = "http://api.openweathermap.org/data/2.5/weather?" # we need  to use the url that is created by the wemos for the api call ( here i used the openweahter api)
        params = {'appid' : apikey,
                  'q': city,
                  'units' : 'metric'}# This is the parameters here we use the variables that we have defiend earlier
        res = requests.get(url, params=params).json()# Here we make the api call with the params that were specified above
        call = res #putting the call in a new variable, it dosent do much just makes it eaiser for me. 

        self.little_label['text'] = call_format(call)# alters the text in the label to fit with the formatted apicall. 


# Here we format our api call so that we get the desired information how we want it.
def call_format(call):
    name = (call['name']) # Here we take the name of the city we are searching.
    desc = (call['weather'][0]['description']) # This gives us an description of the weather.
    temp =(call['main']['temp'])#This gives us the temprature.
    feels_like = (call['main']['feels_like'])#This tells us what it feels like outside.
    
    if temp < 10. : #We format our response if the temprature is below 10 degress or if it feels like under 10 degress the program asks us to bring a jacket.
            return (f"You are in {str(name)}\n its : {str(desc)} today.\n the temprature is: {str(temp)}degrees\n it feels like {str(feels_like)}degrees\n you should bring a jacket")
    elif feels_like < 10. :
            return (f"You are in {str(name)}\n its : {str(desc)} today.\n the temprature is: {str(temp)}degrees\n it feels like {str(feels_like)}degrees\n you should bring a jacket")
    else:
            return (f"You are in {str(name)}\n its : {str(desc)} today.\n the temprature is: {str(temp)}degrees\n it feels like {str(feels_like)}degrees")


def home_call_format(home_res):
    home_temp = (home_res['variables']['temperature'])
    home_hum = (home_res['variables']['humidity'])

    if home_temp < 10. :
        return (f"{home_temp} C° \n {home_hum} Humidity \n  Pull out some flip flops it's great weather")
    else:
        return (f"{home_hum} Humidity \n {home_temp} Temperature \n Don't bring jacket")


#starting the mainloop and creating the root, making the weatherapp function
root = tk.Tk()
app = weatherGui(master=root)
app.mainloop()
