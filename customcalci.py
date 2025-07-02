from customtkinter import *
from math import *
import pygame

#sound effects
def sound():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\COMCell_Iphone touch sound 2 (ID 2038)_BSB.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
def sound2():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\decidemp3-14575.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def sound3():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\click-button-140881.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


    


 
 #frame work
root=CTk()
root.config(background="black")
root.title("calculater")
root.geometry("410x500")
root.resizable(False,False)
display=StringVar()
input_var=""
#entrybox
Entrybox=CTkEntry(master=root,textvariable=display,height=70,width=400,corner_radius=30,border_color="black",bg_color="black",fg_color="black",font=("Helvetica",70)).place(x=5,y=0)

#framebox

frame=CTkFrame(master=root,width=400,height=500,border_color="black",corner_radius=30,border_width=3,bg_color="black",fg_color="black")
frame.place(x=0,y=100)


#input function
def input_function(item):
    sound()
    global input_var
    if item==("cbrt("):
        display.set(input_var+"∛")
        input_var = input_var + str(item)
    elif item ==("sqrt(") :
        display.set(input_var+"√")
        input_var=input_var+str(item)

    else:
        input_var = input_var + str(item)
        display.set(input_var)


#equals fucntion
def equal_buut_function():
    sound2()
    global input_var
    result=str(round(eval(input_var),3))
    display.set(result)
    input_var=result

#clearfunction
def clear_button():
    sound()
    global input_var
    input_var=""
    display.set(input_var)

#backspace
def backspace():
    sound()
    global input_var
    
    input_var=input_var[:len(input_var)-1]
    display.set(input_var)


#trignomentryfuntion
is_on=True
def Trignometry():
    sound3()

    global is_on
    if is_on:
        root.geometry("650x500")
        window_button.place(x=600,y=10)
        frame.configure(width=600,height=500)

        sin= CTkButton(master=frame, command=lambda: input_function("sin("), text="sin", height=70, width=10,corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 20,"bold"))
        sin.grid(row=0, column=4, padx=3, pady=3)

        cos = CTkButton(master=frame, command=lambda: input_function("cos("), text="cos", height=70, width=10,corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 20,"bold"))
        cos.grid(row=1, column=4, padx=3, pady=3)

        left_brace = CTkButton(master=frame, command=lambda: input_function("("), text="(", height=70, width=70,corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 30,"bold"))
        left_brace.grid(row=2, column=4, padx=3, pady=3)

        right_brace = CTkButton(master=frame, command=lambda: input_function(")"), text=")", height=70, width=70,corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 30,"bold"))
        right_brace.grid(row=3, column=4, padx=3, pady=3)

        #
        tan= CTkButton(master=frame, command=lambda: input_function("tan("), text="tan", height=70, width=10,
                             corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 20,"bold"))
        tan.grid(row=0, column=5, padx=3, pady=3)
        cbrt = CTkButton(master=frame, command=lambda: input_function("cbrt("), text="∛", height=70, width=10,
                             corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 20,"bold"))
        cbrt.grid(row=1, column=5, padx=3, pady=3)
        sqrt= CTkButton(master=frame, command=lambda: input_function("sqrt("), text="√", height=70, width=70,
                               corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 30,"bold"))
        sqrt.grid(row=2, column=5, padx=3, pady=3)
        log= CTkButton(master=frame, command=lambda: input_function("log("), text="log", height=70, width=70,
                              corner_radius=50, fg_color="orange", border_color="white", font=("Helvetica", 30,"bold"))
        log.grid(row=3, column=5, padx=3, pady=3)

        is_on=False
    else:
        root.geometry("410x500")
        window_button.place(x=370, y=10)
        frame.configure(width=400)

        is_on=True

#advButtons

window_button=CTkButton(master=root,text="adv",
                        height=10,width=10,corner_radius=100,
                        fg_color="gray",bg_color="black",
                        font=("Helvetica",10),
                        command=Trignometry)
window_button.place(x=350,y=10)

#1st row

clear_butt=CTkButton(master=frame,command=lambda:clear_button(),text="AC",height=70,width=10,corner_radius=60,fg_color="gray",border_color="white",font=("Helvetica",20,"bold"))
clear_butt.grid(row=0,column=0,padx=3,pady=3)
back_butt=CTkButton(master=frame,command=lambda:backspace(),text="⌫",height=70,width=40,corner_radius=60,fg_color="gray",border_color="white",font=("Helvetica",25,"bold"))
back_butt.grid(row=0,column=1,padx=3,pady=3)
modulu_butt=CTkButton(master=frame,command=lambda:input_function("%"),text="%",height=70,width=70,corner_radius=60,fg_color="gray",border_color="white",font=("Helvetica",20,"bold"))
modulu_butt.grid(row=0,column=2,padx=3,pady=3)
div_butt=CTkButton(master=frame,command=lambda:input_function("/"),text="/",height=70,width=70,corner_radius=60,fg_color="orange",border_color="white",font=("Helvetica",20,"bold"))
div_butt.grid(row=0,column=3,padx=3,pady=3)

#2nd row

seven_butt=CTkButton(master=frame,command=lambda:input_function("7"),text="7",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
seven_butt.grid(row=1,column=0,padx=3,pady=3)
eight_butt=CTkButton(master=frame,command=lambda:input_function("8"),text="8",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
eight_butt.grid(row=1,column=1,padx=3,pady=3)
nine_butt=CTkButton(master=frame,command=lambda:input_function("9"),text="9",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
nine_butt.grid(row=1,column=2,padx=3,pady=3)
mul_butt=CTkButton(master=frame,command=lambda:input_function("*"),text="*",height=70,width=70,corner_radius=50,fg_color="orange",border_color="white",font=("Helvetica",30,"bold"))
mul_butt.grid(row=1,column=3,padx=3,pady=3)

#3rd row

four_butt=CTkButton(master=frame,command=lambda:input_function("4"),text="4",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
four_butt.grid(row=2,column=0,padx=3,pady=3)
five_butt=CTkButton(master=frame,command=lambda:input_function("5"),text="5",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
five_butt.grid(row=2,column=1,padx=3,pady=3)
six_butt=CTkButton(master=frame,command=lambda:input_function("6"),text="6",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
six_butt.grid(row=2,column=2,padx=3,pady=3)
minus_butt=CTkButton(master=frame,command=lambda:input_function("-"),text="-",height=70,width=70,corner_radius=50,fg_color="orange",border_color="white",font=("Helvetica",30,"bold"))
minus_butt.grid(row=2,column=3,padx=3,pady=3)

#4th row

one_butt=CTkButton(master=frame,command=lambda:input_function("1"),text="1",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
one_butt.grid(row=3,column=0,padx=3,pady=3)
two_butt=CTkButton(master=frame,command=lambda:input_function("2"),text="2",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
two_butt.grid(row=3,column=1,padx=3,pady=3)
three_butt=CTkButton(master=frame,command=lambda:input_function("3"),text="3",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
three_butt.grid(row=3,column=2,padx=3,pady=3)
plus_butt=CTkButton(master=frame,command=lambda:input_function("+"),text="+",height=70,width=70,corner_radius=50,fg_color="orange",border_color="white",font=("Helvetica",30,"bold"))
plus_butt.grid(row=3,column=3,padx=3,pady=3)

#5th row
zero_butt=CTkButton(master=frame,command=lambda:input_function("00"),text="00",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
zero_butt.grid(row=4,column=0,padx=3,pady=3)
Tzero_butt=CTkButton(master=frame,command=lambda:input_function("0"),text="0",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
Tzero_butt.grid(row=4,column=1,padx=3,pady=3)
dot_butt=CTkButton(master=frame,command=lambda:input_function("."),text=".",height=70,width=70,corner_radius=50,fg_color="#3f3f43",border_color="white",font=("Helvetica",30,"bold"))
dot_butt.grid(row=4,column=2,padx=3,pady=3)
equals_butt=CTkButton(master=frame,command=lambda:equal_buut_function(),text="=",height=70,width=70,corner_radius=50,fg_color="orange",border_color="white",font=("Helvetica",30,"bold"))
equals_butt.grid(row=4,column=3,padx=3,pady=3)



root.mainloop()
