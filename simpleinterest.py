from tkinter import *
window = Tk()

window.title("Simple Interest Calculator")
window.geometry("400x500")
window.configure(bg="#FFE5D9")

def calculate_interest():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)
    show_label.destroy() 
    message=Label(result_frame, text="Simple Interest calculated is "+str(interest), bg="#FFE5D9", font=("Calibri", 12), width=42) 
    message.place(x=20,y=40) 
    message.pack()

app_label = Label(window, text="Simple Interest Calculator", fg="black", bg="#FFE5D9", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal = Label(window, text="Enter Prinicipal(₹)", fg="black", bg="#FFE5D9", font=("Calibri", 12),bd=1)
principal.place(x=20, y=90)

principal = Entry(window, text="", fg="black", bg="#FFE5D9", font=("Calibri", 12))
principal.place(x=190, y=92)

rate = Label(window, text="Enter Rate of Interest(%)", fg="black", bg="#FFE5D9", font=("Calibri", 12),bd=1)
rate.place(x=20, y=140)

rate = Entry(window, text="", fg="black", bg="#FFE5D9", font=("Calibri", 12))
rate.place(x=190, y=142)

time = Label(window, text="Enter time(yrs)", fg="black", bg="#FFE5D9", font=("Calibri", 12),bd=1)
time.place(x=20, y=185)

time = Entry(window, text="", fg="black", bg="#FFE5D9", font=("Calibri", 12))
time.place(x=190, y=187)

calculate_button = Button(window, text="Calculate", fg = "black", bg = "#FFE5D9", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "#FFE5D9", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

show_label = Label(result_frame, text="Your result will be displayed here", bg="#FFE5D9", font=("Calibri", 12), width=40)
show_label.place(x=20,y=20)
show_label.pack()

window.mainloop()