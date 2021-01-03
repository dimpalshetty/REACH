from tkinter import * 
from tkinter import messagebox
import datetime
import time
import sqlite3
from PIL import Image, ImageTk


root = Tk()
root.state('zoomed') 
root['bg'] = 'white'
bg1=PhotoImage(file='bg1.png')
submit_path = Image.open('icons\submit.png')
submit = ImageTk.PhotoImage(submit_path)
# submit = PhotoImage(file='submit.png')

# bg_img=Image.open('bg1.png')
# text = Label(root, text='Welcome to Reach',background="#0A79DF",fg="white",width=50,padx=10,pady=10)
# text.config(font=("Bold",30))
# text.grid(row=3,column=0,columnspan=8,padx=5,pady=5)

add_customer_frame = Frame(root, bg='blue', borderwidth=5, padx=20, pady=20)
add_customer_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

login_frame = Frame(root)
login_frame.grid(row=0, column=0)

donate_window = Frame(root)
donate_window.grid(row=0, column=0)

def sample():
    reg_btn['state'] = 'disabled'
    login_btn['state'] = 'normal'
    return_btn['state'] = 'normal'

    text.grid_forget()
    login_frame.grid_forget()
    add_customer_frame.grid_forget()

    global donate_window

    donate_window = Frame(root, bg='blue', borderwidth=5, padx=20, pady=20)
    donate_window.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #first name widget
    first_name_label = Label(donate_window,text="Food name/type", padx=5, pady=5, width=20
    , anchor=W)
    first_name_label.config(font=("Bold",15))
    first_name_label.grid(row=0,column=0, padx=15, pady=15, sticky=W)

    first_name_entry = Entry(donate_window,borderwidth=3,width=15)
    first_name_entry.config(font=8)
    first_name_entry.grid(row=0,column=1, padx=15,sticky=E)

    #last name widget
    last_name_label = Label(donate_window,text="Quantity", padx=5, pady=5, width=15, anchor=W)
    last_name_label.config(font=("Bold",15))
    last_name_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    last_name_entry = Entry(donate_window,borderwidth=3,width=15)
    last_name_entry.config(font=8)
    last_name_entry.grid(row=1,column=1, padx=15,sticky=E)

    #age widget
    age_label = Label(donate_window,text="Age",padx=5, pady=5, width=15, anchor=W)
    age_label.config(font=("Bold",15))
    age_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    age_entry = Entry(donate_window,borderwidth=3,width=15)
 
    age_entry.config(font=8)
    age_entry.grid(row=2,column=1, padx=15,sticky=E)

    #phone number widget
    phone_no_label = Label(donate_window,text="Phone No", padx=5, pady=5, width=15, anchor=W)
    phone_no_label.config(font=("Bold",15))
    phone_no_label.grid(row=3,column=0, padx=15, pady=15, sticky=W)

    phone_entry = Entry(donate_window,borderwidth=3,width=15)
    phone_entry.config(font=8)
    phone_entry.grid(row=3,column=1, padx=15,sticky=E)

    # DL number widget
    dl_no_label = Label(add_customer_frame,text="DL Number", padx=5, pady=5, width=15, anchor=W)
    dl_no_label.config(font=("Bold",15))
    dl_no_label.grid(row=4,column=0, padx=15, pady=15, sticky=W)

    dl_no_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    dl_no_entry.config(font=8)
    dl_no_entry.grid(row=4,column=1, padx=15,sticky=E)

    #gender number widget
    gender_label = Label(add_customer_frame,text="Gender", padx=5, pady=5, width=12, anchor=W)
    gender_label.config(font=("Bold",15))
    gender_label.grid(row=5,column=0, padx=15, pady=15, sticky=W)

    frame_2 = LabelFrame(add_customer_frame)
    frame_2.grid(row=5, column=1, columnspan=3)

    r = StringVar()

    Radiobutton(add_customer_frame, text="Male", variable=r, value="M", font=("Bold",12)).place(x=200, y=350)
    Radiobutton(add_customer_frame, text="Female", variable=r, value="F", font=("Bold",12)).place(x=265, y=350)
    Radiobutton(add_customer_frame, text="Others", variable=r, value="Other", font=("Bold",12)).place(x=350, y=350)

    button_submit = Button(donate_window,image=submit,padx=32,pady=9,fg="white",background="blue",borderwidth=2,relief=FLAT, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get()))
    button_submit.config(font=("Helvetica", 15))
    button_submit.grid(row=6, column=0, columnspan=3, padx=20, pady=20)

def register():
    register_win=Toplevel(root)
    # reg_btn['state'] = 'disabled'
    # login_btn['state'] = 'normal'
    # # return_btn['state'] = 'normal'

    # text.grid_forget()
    # login_frame.grid_forget()
    # # return_frame.grid_forget()

    global register_frame

    register_frame = Frame(register_win, bg='blue', borderwidth=5, padx=20, pady=20)
    register_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #selection widget
    selection_donate=Radiobutton(register_frame, text="Donate", value="M", font=("Bold",12))
    selection_donate.grid(row=0,column=0)

    selection_volunteer=Radiobutton(register_frame, text="Volunteer", value="M", font=("Bold",12))
    selection_volunteer.grid(row=0,column=1)

    #first name widget
    first_name_label = Label(register_frame,text="First Name", padx=5, pady=5, width=15, anchor=W)
    first_name_label.config(font=("Bold",15))
    first_name_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    first_name_entry = Entry(register_frame,borderwidth=3,width=15)
    first_name_entry.config(font=8)
    first_name_entry.grid(row=1,column=1, padx=15,sticky=E)

    #last name widget
    last_name_label = Label(register_frame,text="Last Name", padx=5, pady=5, width=15, anchor=W)
    last_name_label.config(font=("Bold",15))
    last_name_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    last_name_entry = Entry(register_frame,borderwidth=3,width=15)
    last_name_entry.config(font=8)
    last_name_entry.grid(row=2,column=1, padx=15,sticky=E)

    # #age widget
    # age_label = Label(register_frame,text="Age",padx=5, pady=5, width=15, anchor=W)
    # age_label.config(font=("Bold",15))
    # age_label.grid(row=3,column=0, padx=15, pady=15, sticky=W)

    # age_entry = Entry(register_frame,borderwidth=3,width=15)
    # age_entry.config(font=8)
    # age_entry.grid(row=3,column=1, padx=15,sticky=E)

    #phone number widget
    phone_no_label = Label(register_frame,text="Phone No", padx=5, pady=5, width=15, anchor=W)
    phone_no_label.config(font=("Bold",15))
    phone_no_label.grid(row=4,column=0, padx=15, pady=15, sticky=W)

    phone_entry = Entry(register_frame,borderwidth=3,width=15)
    phone_entry.config(font=8)
    phone_entry.grid(row=4,column=1, padx=15,sticky=E)

    # #DL number widget
    # dl_no_label = Label(register_frame,text="DL Number", padx=5, pady=5, width=15, anchor=W)
    # dl_no_label.config(font=("Bold",15))
    # dl_no_label.grid(row=5,column=0, padx=15, pady=15, sticky=W)

    # dl_no_entry = Entry(register_frame,borderwidth=3,width=15)
    # dl_no_entry.config(font=8)
    # dl_no_entry.grid(row=5,column=1, padx=15,sticky=E)

    # #gender number widget
    # gender_label = Label(register_frame,text="Gender", padx=5, pady=5, width=12, anchor=W)
    # gender_label.config(font=("Bold",15))
    # gender_label.grid(row=6,column=0, padx=15, pady=15, sticky=W)

    # frame_2 = LabelFrame(register_frame)
    # frame_2.grid(row=6, column=1, columnspan=3)

    # r = StringVar()

    # Radiobutton(register_frame, text="Male", variable=r, value="M", font=("Bold",12)).place(x=200, y=350)
    # Radiobutton(register_frame, text="Female", variable=r, value="F", font=("Bold",12)).place(x=265, y=350)
    # Radiobutton(register_frame, text="Others", variable=r, value="Other", font=("Bold",12)).place(x=350, y=350)

    #  button_submit = Button(register_frame,text="Submit",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get()))

    button_submit = Button(register_frame,text="Submit",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED, command=donor)
    button_submit.config(font=("Helvetica", 15))
    button_submit.grid(row=7, column=0, columnspan=3, padx=20, pady=20)

# login frame
def login():
    login_win=Toplevel(root)
    # reg_btn['state'] = 'normal'
    # login_btn['state'] = 'disable'

    # text.grid_forget()
    # add_customer_frame.grid_forget()

    login_frame = Frame(login_win, bg='blue', borderwidth=5, padx=20, pady=20)
    login_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=NSEW)

    #first name widget
    first_name_label = Label(login_frame,text="First Name", padx=5, pady=5, width=15, anchor=W)
    first_name_label.config(font=("Bold",15))
    first_name_label.grid(row=0,column=0, padx=15, pady=15, sticky=W)

    first_name_entry = Entry(login_frame,borderwidth=3,width=15)
    first_name_entry.config(font=8)
    first_name_entry.grid(row=0,column=1, padx=15,sticky=E)

    #last name widget
    last_name_label = Label(login_frame,text="Last Name", padx=5, pady=5, width=15, anchor=W)
    last_name_label.config(font=("Bold",15))
    last_name_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    last_name_entry = Entry(login_frame,borderwidth=3,width=15)
    last_name_entry.config(font=8)
    last_name_entry.grid(row=1,column=1, padx=15,sticky=E)

    button_submit = Button(login_frame,text="Submit",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED)
    button_submit.config(font=("Helvetica", 15))
    button_submit.grid(row=6, column=0, columnspan=3, padx=20, pady=20)


head_label = Label(root, text="Reach",background="#0A79DF",fg="white",width=65,padx=14,pady=10,anchor=W)
head_label.config(font=("Bold",30))


head_label.grid(row=0,column=0,columnspan=5,padx=5,pady=5,sticky=W)

# def clock():
#     hour = time.strftime("%I")
#     min = time.strftime("%M")
#     sec = time.strftime("%S")
#     am_pm = time.strftime("%p")

#     dayNum = time.strftime("%d")
#     month = time.strftime("%b")
#     year = time.strftime("%Y")
#     day = time.strftime("%A")

#     date_label.config(text= dayNum +' '+ month +' '+ year +'   '+ day)

#     time_label.config(text= hour +':'+ min +':'+ sec +' '+ am_pm)
#     time_label.after(1000, clock)

# #time frame
# topframe = Frame(root, bg="#00b894", padx=90)
# topframe.grid(row=1, column=0, columnspan=8, padx=0)

# date_label = Label(topframe, text='', font=("bold", 18), fg="#6D214F", bg="#00b894", pady=5, relief=FLAT)
# date_label.pack(side="left", padx=(0,200), anchor=W)

# # title = Label(topframe, text='RENT-IT', font=("helvetica", 18), fg="white", bg="#00b894", pady=5, relief=FLAT)
# # title.pack(side="left", padx=200, anchor=W)

# time_label = Label(topframe, text='', font=("bold", 18), fg="#6D214F", bg="#00b894", pady=5, relief=FLAT)
# time_label.pack(side="left", padx=(200,0), anchor=E)

# clock()

# topframe = Frame(root, bg="#2ecc72")
# topframe.grid(row=2, column=0, columnspan=8, pady=5,sticky=N)

def donor():
    donor_win=Toplevel(root)
    # reg_btn['state'] = 'disabled'
    # login_btn['state'] = 'normal'
    # # return_btn['state'] = 'normal'

    # text.grid_forget()
    # login_frame.grid_forget()
    # # return_frame.grid_forget()

    global donor_frame

    donor_frame = Frame(donor_win, bg='blue', borderwidth=5, padx=20, pady=20)
    donor_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #Food type widget
    food_type_label = Label(donor_frame,text="Food Type", padx=5, pady=5, width=15, anchor=W)
    food_type_label.config(font=("Bold",15))
    food_type_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    food_type_entry = Entry(donor_frame,borderwidth=3,width=15)
    food_type_entry.config(font=8)
    food_type_entry.grid(row=1,column=1, padx=15,sticky=E)

    #food name widget
    food_name_label = Label(donor_frame,text="Food Name/Category", padx=5, pady=5, width=15, anchor=W)
    food_name_label.config(font=("Bold",15))
    food_name_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    food_name_entry = Entry(donor_frame,borderwidth=3,width=15)
    food_name_entry.config(font=8)
    food_name_entry.grid(row=2,column=1, padx=15,sticky=E)

    # #age widget
    # age_label = Label(register_frame,text="Age",padx=5, pady=5, width=15, anchor=W)
    # age_label.config(font=("Bold",15))
    # age_label.grid(row=3,column=0, padx=15, pady=15, sticky=W)

    # age_entry = Entry(register_frame,borderwidth=3,width=15)
    # age_entry.config(font=8)
    # age_entry.grid(row=3,column=1, padx=15,sticky=E)

    #food quantity widget
    quantity_label = Label(donor_frame,text="Phone No", padx=5, pady=5, width=15, anchor=W)
    quantity_label.config(font=("Bold",15))
    quantity_label.grid(row=4,column=0, padx=15, pady=15, sticky=W)

    quantity_entry = Entry(donor_frame,borderwidth=3,width=15)
    quantity_entry.config(font=8)
    quantity_entry.grid(row=4,column=1, padx=15,sticky=E)

    #city widget
    city_label = Label(donor_frame,text="City", padx=5, pady=5, width=15, anchor=W)
    city_label.config(font=("Bold",15))
    city_label.grid(row=5,column=0, padx=15, pady=15, sticky=W)

    city__entry = Entry(donor_frame,borderwidth=3,width=15)
    city__entry.config(font=8)
    city__entry.grid(row=5,column=1, padx=15,sticky=E)

    #pin code widget
    pin_code_label = Label(donor_frame,text="Pin code", padx=5, pady=5, width=15, anchor=W)
    pin_code_label.config(font=("Bold",15))
    pin_code_label.grid(row=5,column=0, padx=15, pady=15, sticky=W)

    pin_code__entry = Entry(donor_frame,borderwidth=3,width=15)
    pin_code__entry.config(font=8)
    pin_code__entry.grid(row=5,column=1, padx=15,sticky=E)
    
    # #gender number widget
    # gender_label = Label(donor_frame,text="Gender", padx=5, pady=5, width=12, anchor=W)
    # gender_label.config(font=("Bold",15))
    # gender_label.grid(row=6,column=0, padx=15, pady=15, sticky=W)

    # frame_2 = LabelFrame(donor_frame)
    # frame_2.grid(row=6, column=1, columnspan=3)

    # r = StringVar()

    # Radiobutton(donor_frame, text="Male", variable=r, value="M", font=("Bold",12)).place(x=200, y=350)
    # Radiobutton(donor_frame, text="Female", variable=r, value="F", font=("Bold",12)).place(x=265, y=350)
    # Radiobutton(donor_frame, text="Others", variable=r, value="Other", font=("Bold",12)).place(x=350, y=350)

    donor_submit = Button(donor_frame,text="Submit",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get()))
    donor_submit.config(font=("Helvetica", 15))
    donor_submit.grid(row=7, column=0, columnspan=3, padx=20, pady=20)


#Landing page
landing_frame=Frame(root)
landing_frame.grid(row=2,column=0,columnspan=8)
label=Label(landing_frame,image=bg1)
label.pack(anchor=NW)

login_btn = Button(landing_frame, text="Login", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT,padx=60,pady=60, command=login)
login_btn.place(x=300,y=450)

reg_btn = Button(landing_frame, text="Register", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT,padx=60,pady=60, command=register)
reg_btn.place(x=700,y=450)

quote = Label(landing_frame, text='Welcome to Reach',fg="orange")
quote.config(font=("Bold",30))
quote.place(x=50,y=200)


# donate_btn = Button(landing_frame, text="Donate", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT,padx=30,pady=30, command=donate)
# donate_btn.place(x=300,y=450)

# volunteer_btn = Button(landing_frame, text="Volunteer", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT,padx=60,pady=60)
# volunteer_btn.place(x=700,y=450)





root.mainloop()