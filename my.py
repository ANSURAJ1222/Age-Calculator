# import all functions from the tkinter
from tkinter import *

def calculateAge():
		birthday = int(dayld.get())
		birthmonth = int(monthld.get())
		birthyear = int(yearld.get())

		givenday = int(givendayld.get())
		givenmonth = int(givenMonthld.get())
		givenyear = int(givenYearld.get())
		
		
		month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
		if (birthday > givenday):
			givenmonth = givenmonth - 1
			givenday = givenday + month[birthmonth-1]
					
					
		if (birthmonth > givenmonth):
			givenyear = givenyear - 1
			givenmonth = givenmonth + 12

		calculatedday = givenday - birthday
		calculatedmonth = givenmonth - birthmonth
		calculatedyear = givenyear - birthyear

		
		rdayld.insert(10, str(calculatedday))
		rMonthld.insert(10, str(calculatedmonth))
		ryearld.insert(10, str(calculatedyear))
	

if __name__ == "__main__":
	gui = Tk()

	gui.configure(background = "light yellow")

	gui.title("Age Calculator")
	gui.geometry("550x250")
	dob = Label(gui, text = "Date Of Birth", bg = "blue")

	givenDate = Label(gui, text = "Given Date", bg = "blue")
	day = Label(gui, text = "Day", bg = "light blue")

	month = Label(gui, text = "Month", bg = "light blue")
	year = Label(gui, text = "Year", bg = "light blue")
	givenDay = Label(gui, text = "Given Day", bg = "light blue")
	givenMonth = Label(gui, text = "Given Month", bg = "light blue")
	givenYear = Label(gui, text = "Given Year", bg = "light blue")

	rYear = Label(gui, text = "Years", bg = "light blue")


	rMonth = Label(gui, text = "Months", bg = "light blue")
	rDay = Label(gui, text = "Days", bg = "light blue")


	resultantAge = Button(gui, text = "Resultant Age", fg = "white", bg = "black", command = calculateAge)

	

	dayld = Entry(gui)
	monthld = Entry(gui)
	yearld = Entry(gui)
	
	givendayld = Entry(gui)
	givenMonthld = Entry(gui)
	givenYearld = Entry(gui)
	
	ryearld = Entry(gui)
	rMonthld = Entry(gui)
	rdayld = Entry(gui)


	
	dob.grid(row = 0, column = 1)
	
	day.grid(row = 1, column = 0)
	dayld.grid(row = 1, column = 1)
	
	month.grid(row = 2, column = 0)
	monthld.grid(row = 2, column = 1)
	
	year.grid(row = 3, column = 0)
	yearld.grid(row = 3, column = 1)
	
	givenDate.grid(row = 0, column = 4)
	
	givenDay.grid(row = 1, column = 3)
	givendayld.grid(row = 1, column = 4)
	
	givenMonth.grid(row = 2, column = 3)
	givenMonthld.grid(row = 2, column = 4)
	
	givenYear.grid(row = 3, column = 3)
	givenYearld.grid(row = 3, column = 4)
	
	resultantAge.grid(row = 4, column = 2)
	
	rYear.grid(row = 5, column = 2)
	ryearld.grid(row = 6, column = 2)
	
	rMonth.grid(row = 7, column = 2)
	rMonthld.grid(row = 8, column = 2)
	
	rDay.grid(row = 9, column = 2)
	rdayld.grid(row = 10, column = 2)


	# Start the GUI
	gui.mainloop()
