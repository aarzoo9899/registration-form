from tkinter import*
from tkinter import messagebox
from tkcalendar import*
from tkinter import PhotoImage
Mianscreen=Tk()
Mianscreen.geometry('1000x700')
Mianscreen.configure(background="white")

# image 
bg = PhotoImage(file = "aa.png")
# Create Canvas 
canvas1 = Canvas( Mianscreen, width = 200, 
				height = 250) 

canvas1.pack(fill = "both", expand = True)
# Display image 
canvas1.create_image( -70, 5, image = bg, 
					anchor = "nw") 
# Add Text 
canvas1.create_text( 250, 290, text = " ") 


#celender
def pick_date(event):
	global cal,date_window
	date_window=Toplevel()
	date_window.grab_set()
	date_window.title('Choose Date of Birth')
	date_window.geometry('250x220+590+370')
	cal= Calendar(date_window, selectmode="day",date_pattern="mm/dd/y",bg="blue")
	cal.place(x=0,y=0)

	submit_btn=Button(date_window,text="Submit",command=grap_date)
	submit_btn.place(x=100,y=190)

def grap_date():
	DOB.delete(0,END)
	DOB.insert(0,cal.get_date())
	date_window.destroy()

	#checkbox
def on_checkbox_toggel():
	if checkbox_var.get():
		print("checkbox is checked")
	else:
		print("checkbox is unchecked")

#showerror
input1=StringVar()
input2=StringVar()
input3=StringVar()
input4=StringVar()
input5=StringVar()
def submit():
	Mianscreen.destroy()
	txt=input1.get()
	txt=input2.get()
	txt=input3.get()
	txt=input4.get()
	txt=input5.get()
	


	if txt=='':
		messagebox.showerror("Error","Fill all fields")
	else:
#secondscreen	
		sec=Tk()
		sec.geometry('1000x700')
		sec.configure(background="white")
		title=Label(sec,text="               Registration Done                  ",font=("elephant",45,"normal"),fg="#E0FFFF",bg="darkblue")
		title.place(x=0,y=300)
		sec.mainloop()

#widgets
#title
title=Label(text="      Fill KV Registration Form               ",font=("elephant",45,"normal"),bg="darkblue",fg="white")
title.place(x=0,y=0)
#student
Name=Label(text="Name of Student :-",font=("arial",12,"bold"),fg="darkblue")
Name.place(x=100,y=130)
#student Input
Name=Entry(font=("arial",10,"normal"),textvariable=input1)
Name.place(x=250,y=130)
#DOB
DOB=Label(text="DOB:-",font=("arial",11,"bold"),fg="darkblue")
DOB.place(x=100,y=170)
#DOBInput
DOB=Entry(font=("arial",10,"normal"),textvariable=input2)
DOB.place(x=250,y=170)
DOB.insert(0,"dd/mm/yyyy")
DOB.bind("<1>",pick_date)
#Age
Age=Label(text="Age:-",font=("arial",11,"bold"),fg="darkblue")
Age.place(x=100,y=210)
#AgeInput
Age=Entry(font=("arial",10,"normal"),textvariable=input3)
Age.place(x=250,y=210)
#Gender
Gen=Label(Mianscreen,text="Select Gender:-",width=15,font=("arial",11,"bold"),fg="darkblue")
Gen.place(x=450,y=130)
i=IntVar()
Radiobutton(Mianscreen,text="Male",padx=5,variable=i,value="Male",font=("arial",11,"bold"),fg="darkblue").place(x=450,y=190)
Radiobutton(Mianscreen,text="Female",padx=5,variable=i,value="Female",font=("arial",11,"bold"),fg="darkblue").place(x=590,y=190)
#Level
Lev=Label(text="Level:-",font=("arial",11,"bold"),fg="darkblue")
Lev.place(x=100,y=250)
bignner=Label(text="Beginner:-",font=("arial",11,"bold"),fg="darkblue")
bignner.place(x=240,y=250)
Intermediate=Label(text="Intermediate:-",font=("arial",11,"bold"),fg="darkblue")
Intermediate.place(x=400,y=250)
Advanced=Label(text="Advanced:-",font=("arial",11,"bold"),fg="darkblue")
Advanced.place(x=590,y=250)
#Checkbox
checkbox_var=BooleanVar()
checkbox=Checkbutton(Mianscreen,text=" ",variable=checkbox_var,command=on_checkbox_toggel)
checkbox.place(x=310,y=250)
checkbox_var=BooleanVar()
checkbox=Checkbutton(Mianscreen,text=" ",variable=checkbox_var,command=on_checkbox_toggel)
checkbox.place(x=500,y=250)
checkbox_var=BooleanVar()
checkbox=Checkbutton(Mianscreen,text=" ",variable=checkbox_var,command=on_checkbox_toggel)
checkbox.place(x=670,y=250)
#parents
FName=Label(text="Father's Name :-",font=("arial",12,"bold"),fg="darkblue")
FName.place(x=100,y=300)
MName=Label(text="Mother's Name :-",font=("arial",12,"bold"),fg="darkblue")
MName.place(x=100,y=340)
#parents input
FName=Entry(font=("arial",10,"normal"),textvariable=input4)
FName.place(x=250,y=300)
MName=Entry(font=("arial",10,"normal"))
MName.place(x=250,y=340)
#Address
Address=Label(text="Address:-",font=("arial",12,"bold"),fg="darkblue")
Address.place(x=100,y=380)
#AddressInput
Address=Entry(font=("arial",10,"normal"))
Address.place(x=250,y=380)
#Email
Email=Label(text="Email:-",font=("arial",12,"bold"),fg="darkblue")
Email.place(x=100,y=420)
#EmailInput
Email=Entry(font=("arial",10,"normal"))
Email.place(x=250,y=420)
#Contact
Contact=Label(text="Contact:-",font=("arial",12,"bold"),fg="darkblue")
Contact.place(x=490,y=420)
#Contact Inpute
Contact=Entry(font=("arial",10,"normal"),textvariable=input5)
Contact.place(x=570,y=420)
#Medical
Medical=Label(text="Medical",font=("arial",12,"bold"),fg="darkblue")
Medical.place(x=100,y=460)
Medical=Label(text="conditon(s):-",font=("arial",12,"bold"),fg="darkblue")
Medical.place(x=100,y=480)
#Input
Medical=Entry(font=("arial",10,"normal"))
Medical.place(x=250,y=480)
#button
btn=Button(Mianscreen,text="Submit",font=("algerian",18,"normal"),bg="green",fg="white",command=submit)
btn.place(x=420,y=550)
Mianscreen.mainloop()