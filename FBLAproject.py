import tkinter as tk #Allows for quicker coding
from tkinter import ttk, filedialog #toolkit for uploading file 

TITLEFONT =("Arial", 40) #Keeps a consistent title font that is used multiple times

class tkinterApp(tk.Tk):

	# __init__ function for class tkinterApp 
	def __init__(self): 

	# __init__ function for class Tk
		tk.Tk.__init__(self)

		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		for F in (HomePage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# HomePage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, stick ="nsew")

		self.show_frame(HomePage)
		# to display the current frame passed as
		# parameter

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame HomePage

class HomePage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		# label of frame Layout 2
		HOMETITLE = tk.Label(self, text ="Home Page", font = TITLEFONT)
		HOMETITLE.pack()

		Directions1 = tk.Label(self, text="Select GPA Type", font=('Arial', 20)) ######
		Directions1.pack() ######

		UnweighPath = tk.Button(self, text ="Unweighted", font=('Comic Sans', 36),
		command = lambda : controller.show_frame(Page1))

		# putting the button in its place by using pack
		UnweighPath.pack(padx = 40, pady = 10, fill = 'both', expand=True)

		# button to show frame 2 with text layout2
		WeighPath = tk.Button(self, text ="Weighted", font=('Comic Sans', 36),
		command = lambda : controller.show_frame(Page2))

		# putting the button in its place by using pack
		WeighPath.pack(padx = 40, pady = 10, fill = 'both', expand=True)




# second window frame page1 
class Page1(tk.Frame):
	def __init__(self, parent, controller):
		self.grade_entered=tk.StringVar()
		self.grade_count = 0
		self.total_grade = 0.0
		self.valid_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D", "D-", "F"] #prompt says to use scale from school, we don't use A+

		tk.Frame.__init__(self, parent)

		TITLE1 = tk.Label(self, text ="Unweighted", font = TITLEFONT)
		TITLE1.pack()

		back = tk.Button(self, text ="< Back", font=('Comic Sans', 20),
				   command = lambda : [controller.show_frame(HomePage), self.clear_entries()])
		back.place(x=0,y=0)
	
		organizer = tk.Frame(self)
		for i in range(4):
			organizer.rowconfigure(i, weight=1, pad = 15)
			organizer.columnconfigure(i, weight=1, pad = 75)

		defineUnweighted = tk.Label(organizer, font =('Arial', 20), 
							  text = "Unweighted GPA is your grade ignoring "
							  "\ncourse rigor, how difficult the course you "
							  "\nare taking is. Each letter grade has a "
							  "\ncoressponding grade value that is assigned to "
							  "\nit which is then used to calculate your GPA.")
		defineUnweighted.grid(row = 0, column = 0, rowspan = 4)

		Directions2 = tk.Label(organizer, text="Enter letter grades one at a time:", font=('Arial', 15)) ######
		Directions2.grid(row = 0, column = 1)

		self.GPAentry = tk.Entry(organizer, textvariable = self.grade_entered, font=('Arial',20), justify = 'center')
		self.GPAentry.grid(row = 1, column = 1)

		submit = tk.Button(organizer, text="submit", font=('Arial', 16), command = self.GPAsubmit)
		submit.grid(row = 2, column = 1)

		self.outputGPA = tk.Entry(organizer, font=('Arial', 20), width=50, justify = 'center')
		self.outputGPA.grid(row = 3, column = 1)
		self.outputGPA.configure(state = 'disabled')

		clear_button = tk.Button(organizer, text="Clear entries", font=('Arial', 12), command = self.clear_entries)
		clear_button.grid(row = 4, column = 1)

		Directions3 = tk.Label(organizer, text="Enter student ID:", font=('Arial', 15)) ######
		Directions3.grid(row = 1, column = 2, columnspan=2)

		self.enterID = tk.Entry(organizer, textvariable=tk.StringVar(), font=('Arial', 20)) ######
		self.enterID.grid(row = 2, column = 2, columnspan=2)

		loadStudent = tk.Button(organizer, text="Load Student", font=('Arial', 12), command=self.open_file) ######
		loadStudent.grid(row = 3, column = 2)

		saveStudent = tk.Button(organizer, text="Save Student", font=('Arial', 12), command=self.save_file) ######
		saveStudent.grid(row = 3, column = 3)

		organizer.pack()

		self.list_container = tk.Frame(self)
		self.list_container.columnconfigure(0, weight=1)
		self.list_container.columnconfigure(1, weight=1)
		self.list_container.columnconfigure(2, weight=1)
		self.list_container.columnconfigure(3, weight=1)
		self.list_container.columnconfigure(4, weight=1)
		self.list_container.columnconfigure(5, weight=1)
		self.list_container.columnconfigure(6, weight=1)

		self.value_list = []#Used to delete all the outputs

		self.grade_holder = "" #Used to save the letter grades that the user inputs

		self.GPAlist = [] ######

		self.list_container.pack(side="top",fill="both", expand=True)

	def GPAsubmit(self):
		grade = self.grade_entered.get()
		grade = grade.upper() ######
		self.GPAentry.delete('0', 'end')
		if grade not in self.valid_grades:
			self.outputGPA.configure(state = 'normal')
			self.outputGPA.delete('0', 'end')
			self.outputGPA.insert('0', "That is not a valid grade. Please try again.")
			self.outputGPA.configure(state = 'disabled')
		else:
			match grade:
				case "A": self.total_grade += 4.0
				case "A-": self.total_grade += 3.66

				case "B+": self.total_grade += 3.33
				case "B": self.total_grade += 3.0
				case "B-": self.total_grade += 2.66

				case "C+": self.total_grade += 2.33
				case "C": self.total_grade += 2.0
				case "C-": self.total_grade += 1.66

				case "D+": self.total_grade += 1.33
				case "D": self.total_grade += 1.0
				case "D-": self.total_grade += 0.67

				case "F": self.total_grade += 0.0 #Doesn't have functional purpose but makes it look nicer

			self.grade_count += 1
			finalGPA = self.total_grade/self.grade_count

			self.outputs = tk.Text(self.list_container, width=15, height=1, font=('Arial', 16))
			self.outputs.grid(row=(self.grade_count - 1)//5, column=(self.grade_count - 1)%5, stick="WE", pady= 20, padx= 45)

			self.value_list.append(self.outputs)#Allows program to store more than one text box at a time allowing for them all to be deleted with the clear button

			self.GPAlist.append(finalGPA) ######

			if self.grade_count == 1:#If statements just to make it look nicer,
				self.outputGPA.configure(state = 'normal')#Makes it editable for the text to be inserted
				self.outputGPA.delete('0', 'end')
				self.grade_holder = grade
				self.outputGPA.insert('end', self.grade_holder)
				self.outputGPA.configure(state = 'disabled')
			else:
				self.outputGPA.configure(state = 'normal')
				self.outputGPA.delete('0', 'end')
				self.grade_holder += ", " + grade
				self.outputGPA.insert('end', self.grade_holder)
				self.outputGPA.configure(state = 'disabled')

			#Center aligned with tags for looks
			self.outputs.tag_configure('tag_name', justify= 'center')
			self.outputs.insert('1.0', finalGPA)
			self.outputs.tag_add("tag_name", "1.0", "end")
			self.outputs.configure(state = 'disabled')#Makes it so the user can't edit the outputs

	def clear_entries(self):
		self.grade_count = 0 #Reset the count for average
		self.total_grade = 0 #Also reset for average

		#clears their entries in input box
		self.GPAentry.delete('0', 'end')

		#clears the results in the output box
		self.outputGPA.configure(state = 'normal')
		self.outputGPA.delete('0', 'end')
		self.outputGPA.configure(state = 'disabled')

		#clears entry box for student ID
		self.enterID.delete('0', 'end')

		#clears all the textboxes holding the finalGPA
		for i in range (len(self.value_list)):
			self.value_list[i].destroy()

	def save_file(self): ######
		id = self.enterID.get() ######
		if id != "": #input validation
			file1 = open(id + ".txt", "w") ######
			for i in self.GPAlist: ######
				i = str(i) ######
				file1.write(i + " ") ######
			file1.close() ######
		else: ######
			self.enterID.insert('0', "That is not a valid ID. Please try again.") ######

	def open_file(self): ######
		self.enterID.delete('0', 'end')
		file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')]) ######
		if file: ######
			content = file.read() ######
			file.close() ######
			for i in content.split(): ######
				i = float(i.strip(" ")) ######
				self.total_grade += i ######

				self.grade_count += 1 ######
				finalGPA = self.total_grade / self.grade_count ######

				GPAstring = self.outputGPA.get() ######
				output_length = len(GPAstring) ######

				self.outputs = tk.Text(self.list_container, width=15, height=1, font=('Arial', 16)) ######
				self.outputs.grid(row=(self.grade_count - 1) // 5, column=(self.grade_count - 1) % 5, stick="WE", ######
									pady=20, padx=45) ######

				self.value_list.append( ######
				self.outputs)	 ######

				self.outputGPA.delete(first=0, last=output_length) ######
				self.outputGPA.insert('0', finalGPA) ######
				self.outputs.tag_configure('tag_name', justify='center') ######
				self.outputs.insert('1.0', finalGPA) ######
				self.outputs.tag_add("tag_name", "1.0", "end") ######


# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		self.grade_entered=tk.StringVar()
		self.grade_count = 0
		self.total_grade = 0.0
		self.valid_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D", "D-", "F"] #prompt says to use scale from school, Hillcrest don't use A+
		self.scaleError = False

		tk.Frame.__init__(self, parent)

		self.outputs = tk.Text(self, width=15, height=1, font=('Arial', 16)) #So there is a defined outputs box for slideUpdater and GPAsubmit to check

		TITLE1 = tk.Label(self, text ="Weighted", font = TITLEFONT)
		TITLE1.pack()

		back = tk.Button(self, text ="< Back", font=('Comic Sans', 20),
				   command = lambda : [controller.show_frame(HomePage), self.clear_entries()])
		back.place(x=0,y=0)

		organizer = tk.Frame(self)
		for i in range(7):
			organizer.rowconfigure(i, weight=1, pad = 15)
		for i in range(4):
			organizer.columnconfigure(i, weight=1, pad = 75)

		defineWeighted = tk.Label(organizer, font =('Arial', 20), 
							text = "Weighted GPA gives a more holistic view of "
							"\nyour GPA, accounting for courses that you "
							"\ntake that are above the standard level. "
							"\nAP or IB courses are college level and give "
							"\nyou an additional 1 point to the "
							"\nstandard letter grade value that you "
							"\nearn, while an honors course will "
							"\ngive you 0.5 additional points.")
		defineWeighted.grid(row = 0, column = 0, rowspan = 4)

		Directions2 = tk.Label(organizer, text="Enter letter grades one at a time:", font=('Arial', 15)) ######
		Directions2.grid(row = 0, column = 1)

		self.GPAentry = tk.Entry(organizer, textvariable = self.grade_entered, font=('Arial',20), justify = 'center')
		self.GPAentry.grid(row = 1, column = 1)

		submit = tk.Button(organizer, text="submit", font=('Arial', 16), command = self.GPAsubmit)
		submit.grid(row = 2, column = 1)

		self.outputGPA = tk.Entry(organizer, font=('Arial', 20), width=50, justify = 'center')
		self.outputGPA.grid(row = 3, column = 1)
		self.outputGPA.configure(state = 'disabled')

		clear_button = tk.Button(organizer, text="Clear entries", font=('Arial', 12), command = self.clear_entries)
		clear_button.grid(row = 4, column = 1)

		self.honorsScale = tk.Scale(organizer, label = "Slide to select how many Honors classes you are taking",
							  from_=0, to=8, length=500, tickinterval=1, orient='horizontal', command = self.slideUpdater)
		self.honorsScale.set(0)
		self.honorsScale.grid(row = 5, column = 1)

		self.APscale = tk.Scale(organizer, label = "Slide to select how many AP/IB classes you are taking",
						  from_=0, to=8, length=500, tickinterval=1, orient='horizontal', command = self.slideUpdater)
		self.APscale.set(0)
		self.APscale.grid(row = 6, column = 1)

		Directions3 = tk.Label(organizer, text="Enter student ID:", font=('Arial', 15)) ######
		Directions3.grid(row = 1, column = 2, columnspan=2)

		self.enterID = tk.Entry(organizer, textvariable=tk.StringVar(), font=('Arial', 20)) ######
		self.enterID.grid(row = 2, column = 2, columnspan=2)

		loadStudent = tk.Button(organizer, text="Load Student", font=('Arial', 12), command=self.open_file) ######
		loadStudent.grid(row = 3, column = 2)

		saveStudent = tk.Button(organizer, text="Save Student", font=('Arial', 12), command=self.save_file) ######
		saveStudent.grid(row = 3, column = 3)

		organizer.pack()

		self.list_container = tk.Frame(self)
		self.list_container.columnconfigure(0, weight=1)
		self.list_container.columnconfigure(1, weight=1)
		self.list_container.columnconfigure(2, weight=1)
		self.list_container.columnconfigure(3, weight=1)
		self.list_container.columnconfigure(4, weight=1)
		self.list_container.columnconfigure(5, weight=1)
		self.list_container.columnconfigure(6, weight=1)

		self.value_list = [] #Used to delete all the outputs

		self.grade_holder = tk.StringVar #Used to save the letter grades that the user inputs

		self.GPAlist = [] #Used to save the outputs to a file

		self.list_container.pack(side = 'top', fill = 'both', expand = True)

	def GPAsubmit(self):
		grade = self.grade_entered.get()
		grade = grade.upper() #Allows inputs to be in undercase, ie. entering "a" works the same as entering "A"
		self.AP_points = self.APscale.get()
		self.honors_points = self.honorsScale.get()/2
		self.GPAentry.delete('0', 'end')

		if grade not in self.valid_grades:
			self.outputGPA.configure(state = 'normal')
			self.outputGPA.delete('0', 'end')
			self.outputGPA.insert('0', "That is not a valid grade. Please try again.")
			self.outputGPA.configure(state = 'disabled')
		else:
			match grade:
				case "A": self.total_grade += 4.0
				case "A-": self.total_grade += 3.66

				case "B+": self.total_grade += 3.33
				case "B": self.total_grade += 3.0
				case "B-": self.total_grade += 2.66

				case "C+": self.total_grade += 2.33
				case "C": self.total_grade += 2.0
				case "C-": self.total_grade += 1.66

				case "D+": self.total_grade += 1.33
				case "D": self.total_grade += 1.0
				case "D-": self.total_grade += 0.67

				case "F": self.total_grade += 0.0 #Doesn't have functional purpose but makes it look nicer

			self.grade_count += 1
			finalGPA = (self.total_grade + self.AP_points + self.honors_points)/self.grade_count

			self.outputs = tk.Text(self.list_container, width=15, height=1, font=('Arial', 16))

			self.outputs.grid(row=(self.grade_count - 1)//5, column=(self.grade_count - 1)%5, stick="WE", pady= 20, padx= 45)

			self.value_list.append(self.outputs)#Allows program to store more than one text box at a time allowing for them all to be deleted with the clear button

			self.GPAlist.append(finalGPA)

			if self.grade_count == 1:#If statements just to make it look nicer,
				self.outputGPA.configure(state = 'normal')#Makes it editable for the text to be inserted
				self.outputGPA.delete('0', 'end')
				self.grade_holder = grade
				self.outputGPA.insert('end', self.grade_holder)
				self.outputGPA.configure(state = 'disabled')
			else:
				self.outputGPA.configure(state = 'normal')
				self.outputGPA.delete('0', 'end')
				self.grade_holder += ", " + grade
				self.outputGPA.insert('end', self.grade_holder)
				self.outputGPA.configure(state = 'disabled')

			self.outputs.tag_configure('tag_name', justify= 'center')
			self.outputs.insert('1.0', finalGPA)
			self.outputs.tag_add("tag_name", "1.0", "end")
			self.outputs.configure(state='disabled')#Makes it so the user can't edit the output

	def clear_entries(self):
		self.grade_count = 0 #Reset the count for average
		self.total_grade = 0 #Also reset for average
	
		#Resetting sliders
		self.scaleError = False
		self.APscale.set(0)
		self.honorsScale.set(0)

		#clears their entries in input box
		self.GPAentry.delete('0', 'end')

		#clears the results in the output box
		self.outputGPA.configure(state = 'normal')
		self.outputGPA.delete('0', 'end')
		self.outputGPA.configure(state = 'disabled')

		#clears entry box for student ID
		self.enterID.delete('0', 'end')

		#clears all the textboxes holding the finalGPA
		for i in range (len(self.value_list)):
			self.value_list[i].destroy()

	def slideUpdater(self, extraparam): #extraparam to accept all the arguments given, prevents error
		self.outputs.configure(state = 'normal')
		self.outputGPA.configure(state = 'normal')
		self.AP_points = self.APscale.get() #Gets the updated value from the AP/IB scale
		self.honors_points = self.honorsScale.get() #Gets the updated value from the honors scale, not going to half it yet because of validation
		if  self.grade_count == 0:
			self.outputGPA.delete('0', 'end')
			self.outputGPA.insert('0', "You have no courses entered that can be AP/IB or honors")
			self.scaleError = True
		elif self.grade_count < self.AP_points + self.honors_points:
			self.outputGPA.delete('0', 'end')
			self.outputGPA.insert('0', "You have no courses entered that can be AP/IB or honors")
			self.scaleError = True
		else:
			if self.scaleError == True:
				self.outputGPA.delete('0', 'end')
				self.scaleError = False
				self.outputGPA.insert('0', self.grade_holder)
			finalGPA = (self.total_grade + self.AP_points + self.honors_points/2)/self.grade_count

			self.outputs.delete('1.0', 'end')

			self.outputs.tag_configure('tag_name', justify= 'center')
			self.outputs.insert('1.0', finalGPA)
			self.outputs.tag_add("tag_name", '1.0', 'end')
		self.outputs.configure(state = 'disabled')
		self.outputGPA.configure(state = 'disabled')

	def save_file(self): ######
		id = self.enterID.get() ######
		if id != "":
			file1 = open(id + ".txt", "w") ######
			for i in self.GPAlist: ######
				i = str(i) ######
				file1.write(i + " ") ######
			file1.close() ######
		else: ######
			self.enterID.insert('0', "That is not a valid ID. Please try again.") ######

	def open_file(self): ######
		file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')]) ######
		if file: ######
			content = file.read() ######
			file.close() ######
			for i in content.split(): ######
				i = float(i.strip(" ")) ######
				self.total_grade += i ######

				self.grade_count += 1 ######
				finalGPA = self.total_grade / self.grade_count ######

				GPAstring = self.outputGPA.get() ######
				output_length = len(GPAstring) ######

				self.outputs = tk.Text(self.list_container, width=15, height=1, font=('Arial', 16)) ######
				self.outputs.grid(row=(self.grade_count - 1) // 5, column=(self.grade_count - 1) % 5, stick="WE", ######
									pady=20, padx=45) ######

				self.value_list.append(self.outputs)	 ######

				self.outputGPA.delete(first=0, last=output_length) ######
				self.outputGPA.insert('0', finalGPA) ######
				self.outputs.tag_configure('tag_name', justify='center') ######
				self.outputs.insert('1.0', finalGPA) ######
				self.outputs.tag_add("tag_name", "1.0", "end") ######

# Driver Code
app = tkinterApp()
width= app.winfo_screenwidth() 
height= app.winfo_screenheight()
#setting tkinter window size
app.geometry("%dx%d" % (width, height))
# Execute tkinter 
app.title("GPA Calculator")
app.mainloop()