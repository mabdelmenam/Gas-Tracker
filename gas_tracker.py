#use API to get the gas price
#create nromal gui to display
#design, make transparent
#figure out how to make it stuck on a different corner of the screen
#make options for where somneone would want to display, bottom right, top right, top left, bottom left
#make an opacity slider or change option
#make executable
from calendar import c
from tkinter import *
import tkinter.ttk as ttk
import time

from etherscan import Etherscan

eth = Etherscan("5V75QSVZNG6DNXC7IHZ6ZYAMU9VXB2W4V3")
root = Tk()

def main():
    print(gas_price())
    main_gui()
    root.mainloop()

def gas_price():

    #get_gas_oracle() function call

    gas_oracle = eth.get_gas_oracle()

    safe_gas = gas_oracle["SafeGasPrice"] #low #00c9a7
    propose_gas_price = gas_oracle["ProposeGasPrice"] #average #3498db
    fast_gas_price = gas_oracle["FastGasPrice"] #high brown

    return(safe_gas, propose_gas_price,fast_gas_price)

def main_gui():
    root.title('Ethereum Gas Tracker')
    root.geometry("400x250")
    root.attributes('-alpha', 0.75)

    #Making solid when clicked on
    def make_solid(e):
        root.attributes('-alpha', 1.0)
        root.overrideredirect(False)
    #Removing window frame when right click is clicked
    def remove_frame(e):
        root.overrideredirect(True)
    
    root.bind("<Button-1>", make_solid)
    root.bind("<Button-3>", remove_frame)
    
    low, average, high = gas_price()


    low_text = Label(root, text="Low", fg="#000000", font=("Helvetica,Arial,sans-serif", 16))
    low_gas_label = Label(root, text=low, fg="#00c9a7", font=("Helvetica,Arial,sans-serif", 20))
    low_text.place(relx=0.25, rely=0.2,anchor=W)
    low_gas_label.place(relx = 0.25, rely = 0.4, anchor=W)

    average_text = Label(root, text="Average", fg="#000000", font=("Helvetica,Arial,sans-serif", 16))
    average_gas_label = Label(root, text=average, fg="#3498db", font=("Helvetica,Arial,sans-serif", 20))
    average_text.place(relx=0.5, rely=0.2,anchor=CENTER)
    average_gas_label.place(relx=0.5,rely=0.4, anchor=CENTER)

    high_text = Label(root, text="High", fg="#000000", font=("Helvetica,Arial,sans-serif", 16))
    high_gas_label = Label(root, text=high, fg="#a52a2a", font=("Helvetica,Arial,sans-serif", 20))
    high_text.place(relx=0.75, rely=0.2, anchor=E)
    high_gas_label.place(relx=0.75, rely=0.4, anchor=E)

    #Slide Function
    def slide(x):
        root.attributes('-alpha', my_slider.get()) #my_silder.get() gets what the current slider value is from my_slider variable
        slide_label.config(text=str(round(my_slider.get(), 2))) #gets value from my_slider variable

    #Slider
    my_slider = ttk.Scale(root, from_=0.1,to=1.0, value=1.0, orient=HORIZONTAL, command=slide)
    my_slider.place(relx=0.5, rely=0.65, anchor=CENTER)

    #Creates a Label that will be used to dispaly the value of the slider
    slide_label = Label(root, text='')
    slide_label.place(relx=0.5, rely=0.75)



if __name__ == "__main__":
    main()
