from tkinter import *
from tkinter.messagebox import *

def mtov():
	mw.withdraw()
	vw.deiconify()
def vtom():
	vw.withdraw()
	mw.deiconify()

def on_entry_click(event, entry):
    if entry.get() == "Feet" or entry.get() == "inch":
        entry.delete(0, "end")
        entry.config(fg="black")

def save():
	age=ent_age.get()
	height=ent_height.get()
	weight=ent_weight.get()
	if age.strip()=="" or height.strip()=="" or weight.strip=="":
		showerror("Issue","Don't leave Blank Spaces")
		ent_age.delete(0,END)
		ent_height.delete(0,END)
		ent_weight.delete(0,END)
		ent_age.focus()
		ent_height.focus()
		ent_weight.focus()
	elif not(age.isdigit()) or not(height.isnumeric()) or not(weight.isdigit()):
		showerror("Issue","You should enter numbers only")
		ent_age.delete(0,END)
		ent_height.delete(0,END)
		ent_weight.delete(0,END)
		ent_age.focus()
		ent_height.focus()
		ent_weight.focus()
	elif int(age)<2 or int(age)>120: 
		showerror("Issue","Wrong Age")
		ent_age.delete(0,END)
		ent_age.focus()
	elif len(weight)>3 or len(height)>3:
		showerror("Issue","Enter proper weight or height values")
		ent_height.delete(0,END)
		ent_weight.delete(0,END)
		ent_height.focus()
		ent_weight.focus()
	else:
		height=float(height)
		weight=int(weight)
		if height<1.0 or weight < 1:
			showerror("Issue","Atleast enter 1 and not less than 1")
			ent_height.delete(0,END)
			ent_weight.delete(0,END)
			ent_height.focus()
			ent_weight.focus()
		else:
			bmi=weight/(height*height*0.01*0.01)
			if bmi<18.5:
				msg="You are Underweight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<=24.9 and bmi>=18.5:
				msg="You have Normal weight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<=29.9 and bmi>=25:
				msg="You are Overweight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<35 and bmi>=30:
				msg="You are Obese and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi>=35:
				msg="You have Morbid Obesity and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			ent_age.delete(0,END)
			ent_height.delete(0,END)
			ent_weight.delete(0,END)
			ent_age.focus()
			ent_height.focus()
			ent_weight.focus()

def submit():
	age=vw_ent_age.get()
	feet=vw_ent_feet.get()
	inch=vw_ent_inch.get()
	weight=vw_ent_weight.get()
	if age.strip()=="" or feet.strip()=="" or weight.strip=="" or inch.strip()=="":
		showerror("Issue","Don't leave Blank Spaces")
		vw_ent_age.delete(0,END)
		vw_ent_feet.delete(0,END)
		vw_ent_inch.delete(0,END)
		vw_ent_weight.delete(0,END)
		vw_ent_age.focus()
		vw_ent_feet.focus()
		vw_ent_inch.focus()
		vw_ent_weight.focus()
	elif not(age.isdigit()) or not(feet.isnumeric()) or not(weight.isdigit()) or not(inch.isnumeric()):
		showerror("Issue","You should enter numbers only")
		vw_ent_age.delete(0,END)
		vw_ent_feet.delete(0,END)
		vw_ent_inch.delete(0,END)
		vw_ent_weight.delete(0,END)
		vw_ent_age.focus()
		vw_ent_feet.focus()
		vw_ent_inch.focus()
		vw_ent_weight.focus()
	elif int(age)<2 or int(age)>120: 
		showerror("Issue","Wrong Age")
		vw_ent_age.delete(0,END)
		vw_ent_age.focus()
	elif len(weight)>3 or len(feet)>1 or len(inch)>2:
		showerror("Issue","Enter proper weight or height values")
		vw_ent_feet.delete(0,END)
		vw_ent_inch.delete(0,END)
		vw_ent_weight.delete(0,END)
		vw_ent_feet.focus()
		vw_ent_inch.focus()
		vw_ent_weight.focus()
	else:
		feet=float(feet)
		inch=float(inch)
		weight=int(weight)
		total_inches = float(feet) * 12 + float(inch)
		if feet<1.0 or weight < 1:
			showerror("Issue","Atleast enter 1 and not less than 1")
			vw_ent_feet.delete(0,END)
			vw_ent_inch.delete(0,END)
			vw_ent_weight.delete(0,END)
			vw_ent_feet.focus()
			vw_ent_inch.focus()
			vw_ent_weight.focus()
		else:
			bmi=(weight*703)/(total_inches*total_inches)
			if bmi<18.5:
				msg="You are Underweight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<=24.9 and bmi>=18.5:
				msg="You have Normal weight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<=29.9 and bmi>=25:
				msg="You are Overweight and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi<35 and bmi>=30:
				msg="You are Obese and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			elif bmi>=35:
				msg="You have Morbid Obesity and your BMI is "+str(round(bmi,2))
				showinfo("BMI",msg)
			vw_ent_age.delete(0,END)
			vw_ent_feet.delete(0,END)
			vw_ent_inch.delete(0,END)
			vw_ent_weight.delete(0,END)
			vw_ent_age.focus()
			vw_ent_feet.focus()
			vw_ent_inch.focus()
			vw_ent_weight.focus()

mw=Tk()
mw.title("BMI Calculator")
mw.geometry("650x650+360+150")
mw.configure(bg="lightblue")

f=("Old English Text MT",30,"bold")
fx=("Arial",25,"bold")

s=IntVar()
s.set(1)
s.set(3)

lab_head=Label(mw,text="BMI Calculator",font=f,bg="lightblue",fg="grey")
lab_head.pack(pady=20)

lab_gender=Label(mw,text="Gender: ",font=fx,bg="lightblue",fg="grey")
ent_male=Radiobutton(mw,text="Male",font=fx,bg="lightblue",fg="grey",variable=s,value=1)
ent_female=Radiobutton(mw,text="Female",font=fx,bg="lightblue",fg="grey",variable=s,value=2)
lab_age=Label(mw,text="Age (Between 2yrs to 120 yrs): ",font=fx,bg="lightblue",fg="grey")
ent_age=Entry(mw,font=fx)
lab_height=Label(mw,text="height(in cm): ",font=fx,bg="lightblue",fg="grey")
ent_height=Entry(mw,font=fx)
lab_weight=Label(mw,text="Weight(in Kg): ",font=fx,bg="lightblue",fg="grey")
ent_weight=Entry(mw,font=fx)
buttonin=Button(mw,text="BMI in International System",font=fx,bg="red",fg="white",command=save)
buttonim=Button(mw,text="BMI in Imperial System",font=fx,bg="red",fg="white",command=mtov)


lab_gender.place(x=100,y=100)
ent_male.place(x=260,y=100)
ent_female.place(x=410,y=100)
lab_age.place(x=100,y=150)
ent_age.place(x=100,y=200)
lab_height.place(x=100,y=250)
ent_height.place(x=100,y=300)
lab_weight.place(x=100,y=360)
ent_weight.place(x=100,y=410)
buttonin.place(x=100,y=470)
buttonim.place(x=140,y=550)

mw.resizable(False, False)

vw=Toplevel(mw)

vw.title("BMI Calculator")
vw.geometry("650x650+360+150")
vw.configure(bg="lightblue")

f=("Old English Text MT",30,"bold")
fx=("Arial",25,"bold")

vw_lab_head=Label(vw,text="BMI Calculator",font=f,bg="lightblue",fg="grey")
vw_lab_head.pack(pady=20)

vw_lab_gender=Label(vw,text="Gender: ",font=fx,bg="lightblue",fg="grey")
vw_ent_male=Radiobutton(vw,text="Male",font=fx,bg="lightblue",fg="grey",variable=s,value=3)
vw_ent_female=Radiobutton(vw,text="Female",font=fx,bg="lightblue",fg="grey",variable=s,value=4)
vw_lab_age=Label(vw,text="Age (Between 2yrs to 120 yrs): ",font=fx,bg="lightblue",fg="grey")
vw_ent_age=Entry(vw,font=fx)
vw_lab_height=Label(vw,text="height(in ft(1st input) and inch(2nd input): ",font=fx,bg="lightblue",fg="grey")
vw_ent_feet=Entry(vw,font=fx,fg="black")
vw_ent_feet.insert(0,"Feet")
vw_ent_feet.bind("<FocusIn>", lambda event, entry=vw_ent_feet: on_entry_click(event, entry))
vw_ent_inch=Entry(vw,font=fx,fg="black")
vw_ent_inch.insert(0,"inch")
vw_ent_inch.bind("<FocusIn>", lambda event, entry=vw_ent_inch: on_entry_click(event, entry))

vw_lab_weight=Label(vw,text="Weight(in lb): ",font=fx,bg="lightblue",fg="grey")
vw_ent_weight=Entry(vw,font=fx)
vw_buttonin=Button(vw,text="BMI in International System",font=fx,bg="red",fg="white",command=vtom)
vw_buttonim=Button(vw,text="BMI in Imperial System",font=fx,bg="red",fg="white",command=submit)


vw_lab_gender.place(x=100,y=100)
vw_ent_male.place(x=260,y=100)
vw_ent_female.place(x=410,y=100)
vw_lab_age.place(x=100,y=150)
vw_ent_age.place(x=100,y=200)
vw_lab_height.place(x=10,y=250)
vw_ent_feet.place(x=100,y=295)
vw_ent_inch.place(x=100,y=345)
vw_lab_weight.place(x=100,y=390)
vw_ent_weight.place(x=100,y=440)
vw_buttonin.place(x=100,y=500)
vw_buttonim.place(x=140,y=580)

vw.resizable(False, False)

vw.withdraw()

mw.mainloop()
