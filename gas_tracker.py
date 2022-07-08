#use API to get the gas price
#create nromal gui to display
#design, make transparent
#add a drop down for widthxheight, font and font size, background,
#figure out how to make it stuck on a different corner of the screen
#make options for where somneone would want to display, bottom right, top right, top left, bottom left
#make an opacity slider or change option
#make executable

#https://www.youtube.com/watch?v=qTiqnV1MaNs
from calendar import c
from tkinter import *
import tkinter.font as font
import tkinter.ttk as ttk
import time

from etherscan import Etherscan
from matplotlib.ft2font import BOLD
from matplotlib.pyplot import text
from sqlalchemy import false

eth = Etherscan("5V75QSVZNG6DNXC7IHZ6ZYAMU9VXB2W4V3")
root = Tk()
font1 = ['Helvetica,Arial,sans-serif', 16, 'normal']
print(font.families())
def main():
    #print(gas_price())
    main_gui()
    root.mainloop()

def gas_price():

    #get_gas_oracle() function call

    gas_oracle = eth.get_gas_oracle()

    safe_gas = gas_oracle["SafeGasPrice"] #low #00c9a7
    propose_gas_price = gas_oracle["ProposeGasPrice"] #average #3498db
    fast_gas_price = gas_oracle["FastGasPrice"] #high brown

    return(safe_gas, propose_gas_price,fast_gas_price)

#Making solid when clicked on
def make_solid(e):
    root.attributes('-alpha', 1.0)
    root.overrideredirect(False)

#Removing window frame when right click is clicked
def remove_frame(e):
    root.overrideredirect(True)
#Changing font family
def my_font_family(type_of_family, low_text, average_text, high_text): 
    print("Default Text: " , font1[0])
    #font1[0] = type_of_family
    # font.Font(family=type_of_family)
    text_labels = [low_text,average_text, high_text]
    for i in text_labels:
        i.config(font=(type_of_family))


    print("Changed Text: ", font1[0])

#Changing font, font-family, and style(bold, italic, underline)
def font_changes(low_text, average_text, high_text):
    menu_bar = Menu(root)

    menu_font = Menu(menu_bar,tearoff=False, 
    background='#fff', fg="#000", activebackground="#afaaaa", 
    activeforeground="#000", font="Helvetica,Arial,sans-serif 8 bold")

    menu_bar.add_cascade(label="Font", menu=menu_font)

    menu_sub_family=Menu(menu_font, tearoff=False, 
    background='pink', fg="#000", activebackground="#00c733", 
    activeforeground="#fff", font="Helvetica,Arial,sans-serif 8 bold")

    menu_font.add_cascade(label="Font Family", menu=menu_sub_family)

    different_fonts = ['Arial', 'Arial Black', 'Calibri', 'Calibri Light', 'Cambria', 'Comic Sans MS', 'Garamond', 'Georgia', 'Helvetica', 'Rockwell', 'Times New Roman']
    menu_sub_family.add_command(label="Times", command=lambda:my_font_family('Terminal', low_text, average_text, high_text))

    root.config(menu=menu_bar)

def main_gui():
    root.title('Ethereum Gas Tracker')
    root.geometry("500x200") #width x height
    root.attributes('-alpha', 0.75)
    
    #Calling make_solid() function when left-mouse is clicked
    root.bind("<Button-1>", make_solid)
    #Calling remove_frame() function when right-mouse is clicked
    root.bind("<Button-3>", remove_frame)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width, " ", screen_height)
    
    low, average, high = gas_price()


    low_text = Label(root, text="Low", fg="#000000", font=("Helvetica,Arial,sans-serif", 16))
    print(type(font))
    print(type(font1))
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

    font_changes(low_text, average_text, high_text)



if __name__ == "__main__":
    main()
