#libary imports
import tkinter
import datetime
#checking for csv
csv_notfound = False
csv_found = False
try:
    f=open("Appointment ID.csv","r")
    csv_found = True
except:
    csv_notfound = True
if csv_found == True:
    f=open("Appointment ID.csv","r")
    Appointment_Data=[]
    counter = 0
    for line in f:
        line = line.strip('\n')
        Appointment_ID,Appointment_Surname,Appointment_Forename,Appointment_Date,Appointment_Time,Appointment_Treatment  = line.split(",")
        Appointment_Data.append([])
        Appointment_Data[counter].append(Appointment_ID)
        Appointment_Data[counter].append(Appointment_Surname)
        Appointment_Data[counter].append(Appointment_Forename)
        Appointment_Data[counter].append(Appointment_Date)
        Appointment_Data[counter].append(Appointment_Time)
        Appointment_Data[counter].append(Appointment_Treatment)
        counter = counter + 1
    f.close()
def Unique_val_calc():
    #finds the most recently used entry
    length = len(Appointment_Data)
    #increases unique value by 1 to create a new unique ID
    Unique_Value = int(Appointment_Data[length-1][0]) + 1
    Unique_Value_Text = "Unique Value is = " + str(Unique_Value)
    return Unique_Value, Unique_Value_Text
Unique_Value,Unique_Value_Text = Unique_val_calc()
#functions to withdraw and update windows (traversing windows)
def MainMenu_Window():
    AdminPage.withdraw()
    AppWindow.withdraw()
    MainMenu.deiconify()
    MainMenu.update()
def AdminMenu_Window():
    MainMenu.withdraw()
    AdminPage.deiconify()
    AdminPage.update()
def AppMenu_Window():
    BookApp.withdraw()
    MainMenu.withdraw()
    ViewApp.withdraw()
    EditApp.withdraw()
    AppWindow.deiconify()
    AppWindow.update()
def BookApp_Window():
    AppWindow.withdraw()
    BookApp.deiconify()
    BookApp.update()
def ViewApp_Window():
    AppWindow.withdraw()
    ViewAppSur.withdraw()
    ViewApp.deiconify()
    ViewApp.update()
def ViewApp_Window_Surname():
    ViewApp.withdraw()
    ViewAppSur.deiconify()
    ViewAppSur.update()
def EditApp_Window():
    AppWindow.withdraw()
    CancelApp.withdraw()
    EditApp.deiconify()
    EditApp.update()
def CancelApp_Window():
    EditApp.withdraw()
    CancelApp.deiconify()
    CancelApp.update()
def Quit():
    quit()
#creating main menu within python tkinter
MainMenu = tkinter.Tk()
MainMenu.title("Main Menu")
MainMenu.geometry("500x400")
MainMenu.configure(bg="lightblue")
#MainMenu.attributes('-fullscreen', True)
#creating the frames for the menu
frame1=tkinter.Frame(MainMenu)
frame1.configure(bg="lightblue")
frame1.pack()
frame2=tkinter.Frame(MainMenu)
frame2.configure(bg="lightblue")
frame2.pack()
frame3=tkinter.Frame(MainMenu)
frame3.configure(bg="lightblue")
frame3.pack()
frame4=tkinter.Frame(MainMenu)
frame4.configure(bg="lightblue")
frame4.pack()
#creating title label within main menu
MainMenu_Space = tkinter.Label(frame1, text="Nails By Katie" ,bg = "lightblue",fg="lightblue", font="calibri 20 bold")
MainMenu_Space.pack()#seperation from top of window

MainMenu_Title_Lbl = tkinter.Label(frame1, text="Nails By Katie", bg="#EC927F",fg="black",font="calibri 25")
MainMenu_Title_Lbl.pack()#title label

MainMenu_Space = tkinter.Label(frame1, text="Nails By Katie" ,bg = "lightblue",fg="lightblue", font="calibri 35 bold")
MainMenu_Space.pack()#larger space between title and 1st button
#creating error label for if the csv is not found
Csv_Appointment_NotFound = tkinter.Label(frame2,text="Appointment Csv not found and wont be functional",bg="red",fg="black",font="calibri 17")
if csv_notfound == True:
    Csv_Appointment_NotFound.pack()
else:
    MainMenu_Admin_bttn=tkinter.Button(frame2, text="Admin Log On", bg = "yellow",fg="black",font="calibri 15", command=AdminMenu_Window)
    MainMenu_Admin_bttn.pack()#first button for admin page

    MainMenu_Space = tkinter.Label(frame2, text="Nails By Katie" ,bg = "lightblue",fg="lightblue", font="calibri 20 bold")
    MainMenu_Space.pack()#smaller space between both buttons 

    MainMenu_App_bttn=tkinter.Button(frame3, text="Book An Appointment",bg="yellow",fg="black",font="calibri 15", command=AppMenu_Window)
    MainMenu_App_bttn.pack()#2nd button for appointment page

    MainMenu_Space = tkinter.Label(frame4, text="Nails By Katie" ,bg = "lightblue",fg="lightblue", font="calibri 20 bold")
    MainMenu_Space.pack()#space between appointment menu and quit button

    MainMenu_Quit_bttn=tkinter.Button(frame4, text="Quit",bg="yellow",fg="black",font="calibri 15", command=Quit)
    MainMenu_Quit_bttn.pack()#quit button
#creating appointment window and its geometry
AppWindow=tkinter.Toplevel(MainMenu)
AppWindow.title("Appointment Window")
AppWindow.geometry("500x405")
AppWindow.configure(bg="lightblue")
AppWindow.withdraw()
#AppWindow.attributes('-fullscreen', True)
#creating frames within the appointment window
frame1=tkinter.Frame(AppWindow)
frame1.configure(bg="lightblue")
frame1.pack()
frame2=tkinter.Frame(AppWindow)
frame2.configure(bg="lightblue")
frame2.pack()
frame3=tkinter.Frame(AppWindow)
frame3.configure(bg="lightblue")
frame3.pack()
frame4=tkinter.Frame(AppWindow)
frame4.configure(bg="lightblue")
frame4.pack()
frame5=tkinter.Frame(AppWindow)
frame5.configure(bg="lightblue")
frame5.pack()
#creating labels and buttons for the Appointment page 
AppPage_Space = tkinter.Label(frame1,text="Nails By Katie - Appointment Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AppPage_Space.pack()#create space between the top of the page page and the title
AppMenu_Title_lbl=tkinter.Label(frame1, text="Nails By Katie - Appointment Page", bg="#EC927F",fg="black",font="calibri 25")
AppMenu_Title_lbl.pack()#title label
AppPage_Space = tkinter.Label(frame1,text="Nails By Katie - Appointment Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AppPage_Space.pack()#create space between the title and the 1st button
AppMenu_book_bttn = tkinter.Button(frame2, text="Book your Appointment", bg="yellow",fg="black",font="calibri 15", command=BookApp_Window)
AppMenu_book_bttn.pack()#creating the button which will take the user to another page to book an appointment
AppPage_Space = tkinter.Label(frame2,text="Nails By Katie - Appointment Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AppPage_Space.pack()#creating the space between the book appointment button and the view appointment button
AppMenu_view_bttn=tkinter.Button(frame3, text="View your Appointment",bg="yellow",fg="black",font="calibri 15", command=ViewApp_Window)
AppMenu_view_bttn.pack()#creating the button which would take the user to a page to view their appointment specifically
AppPage_Space = tkinter.Label(frame3,text="Nails By Katie - Appointment Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AppPage_Space.pack()#space between view appointment button and ammend appointment button
AppMenu_edit_bttn=tkinter.Button(frame4,text="Edit your Appointment",bg="yellow",fg="black",font="calibri 15",command = EditApp_Window)
AppMenu_edit_bttn.pack()#button to allow users to ammend an appointment
AppPage_Space = tkinter.Label(frame5,text="Nails By Katie - Appointment Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AppPage_Space.pack()#space between ammend appointment button and return to main menu button
AppMenu_return_bttn = tkinter.Button(frame5,text="Return to Main Menu",bg="yellow",fg="black",font="calibri 15",command=MainMenu_Window)
AppMenu_return_bttn.pack()#button to re-open the main menu from the appointment page
#creating admin window and its corresponding geometry
AdminPage=tkinter.Toplevel(MainMenu)
AdminPage.title("Admin Page")
AdminPage.geometry("500x405")
AdminPage.configure(bg="lightblue")
AdminPage.withdraw()
#AdminPage.attributes('-fullscreen', True)
#creating frames for the the admin page
frame1=tkinter.Frame(AdminPage)
frame1.configure(bg="lightblue")
frame1.pack()
frame2=tkinter.Frame(AdminPage)
frame2.configure(bg="lightblue")
frame2.pack()
frame3=tkinter.Frame(AdminPage)
frame3.configure(bg="lightblue")
frame3.pack()
frame4=tkinter.Frame(AdminPage)
frame4.configure(bg="lightblue")
frame4.pack()
frame5=tkinter.Frame(AdminPage)
frame5.configure(bg="lightblue")
frame5.pack()
#creating the labels and buttons within the admin menu
AdminPage_Space = tkinter.Label(frame1,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AdminPage_Space.pack()#create space between the top of the page page and the title
AdminPage_Title_lbl=tkinter.Label(frame1, text="Nails By Katie - Admin Page", bg="#EC927F",fg="black",font="calibri 25")
AdminPage_Title_lbl.pack()#title label
AdminPage_Space = tkinter.Label(frame1,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AdminPage_Space.pack()#create space between the title and the 1st button
Admin_app_bttn = tkinter.Button(frame2, text="View Appointments", bg="yellow",fg="black",font="calibri 15")
Admin_app_bttn.pack()#creating the button which will take the user to another page to view appointments of various clients 
AdminPage_Space = tkinter.Label(frame2,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AdminPage_Space.pack()#creating the space between the view appointments button and the view stock levels button
Admin_stock_bttn=tkinter.Button(frame3, text="View Stock Levels",bg="yellow",fg="black",font="calibri 15")
Admin_stock_bttn.pack()#creating the button which would take the user to a page to view stock levels of products
AdminPage_Space = tkinter.Label(frame3,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AdminPage_Space.pack()#space between stock levels button and view analytics of the business button
Admin_analytics_bttn=tkinter.Button(frame4,text="View Analytics",bg="yellow",fg="black",font="calibri 15")
Admin_analytics_bttn.pack()
#button to allow the user to view various analytics in the form of graphs using matplotlib libary
#also can show analytics using labels 
AdminPage_Space = tkinter.Label(frame5,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 20 bold")
AdminPage_Space.pack()#space between view analytics button and return to main menu button
Admin_return_bttn = tkinter.Button(frame5,text="Return to Main Menu",bg="yellow",fg="black",font="calibri 15",command=MainMenu_Window)
Admin_return_bttn.pack()#button to re-open the main menu from the appointment page
#creating book appointment window
BookApp=tkinter.Toplevel(AppWindow)
BookApp.title("Book an Appointment")
BookApp.geometry("630x650")
BookApp.configure(bg="lightblue")
BookApp.withdraw()
#BookApp.attributes('-fullscreen', True)
#creating frames for the book appointment page
frame1=tkinter.Frame(BookApp)
frame1.configure(bg="lightblue")
frame1.pack()
frame2=tkinter.Frame(BookApp)
frame2.configure(bg="lightblue")
frame2.pack()
frame3=tkinter.Frame(BookApp)
frame3.configure(bg="lightblue")
frame3.pack()
frame4=tkinter.Frame(BookApp)
frame4.configure(bg="lightblue")
frame4.pack()
frame5=tkinter.Frame(BookApp)
frame5.configure(bg="lightblue")
frame5.pack()
frame6=tkinter.Frame(BookApp)
frame6.configure(bg="lightblue")
frame6.pack()
frame7=tkinter.Frame(BookApp)
frame7.configure(bg="lightblue")
frame7.pack()
#creating space from top of the window to the title label
BookApp_Space = tkinter.Label(frame1,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 20 bold")
BookApp_Space.pack()
BookApp_Title_Lbl=tkinter.Label(frame1, text="Nails By Katie - Book an Appointment", bg="#EC927F",fg="black",font="calibri 25")
BookApp_Title_Lbl.pack()#creating title label for booking appointment page 
BookApp_Space = tkinter.Label(frame2,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between title and a surname label and entry box
BookApp_surname_Lbl=tkinter.Label(frame2,text="Surname:",bg="#EC927F",fg="black",font="calibri 15")
BookApp_surname_Lbl.pack(side=tkinter.LEFT)#surname label
BookApp_Space = tkinter.Label(frame3,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between surname and forename
BookApp_forename_Lbl=tkinter.Label(frame3,text="Forename:",bg="#EC927F",fg="black",font="calibri 15")
BookApp_forename_Lbl.pack(side=tkinter.LEFT)#forename label
BookApp_Space = tkinter.Label(frame4,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between forename and date
BookApp_Data_Lbl=tkinter.Label(frame4,text="Date (dd/mm/yyyy):",bg="#EC927F",fg="black",font="calibri 15")
BookApp_Data_Lbl.pack(side=tkinter.LEFT)#date label
BookApp_Space = tkinter.Label(frame5,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between date and time
BookApp_Time_Lbl=tkinter.Label(frame5,text="Time:",bg="#EC927F",fg="black", font="calibri 15")
BookApp_Time_Lbl.pack(side=tkinter.LEFT)#time label
#drop down menu for times on the book appointment pag
times = ["09:00 AM","10:30 AM","12:00 PM","01:30 PM","03:00 PM"]
variable_times=tkinter.StringVar()
variable_times.set(times[0])
BookApp_Time_dropdown=tkinter.OptionMenu(
    frame5,
    variable_times,
    *times)
BookApp_Time_dropdown.pack(side=tkinter.RIGHT)

BookApp_Space = tkinter.Label(frame6,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between time and drop down

services = ['Pedicure','Manicure','Gel Polish','Acrylics','Nail Art']#list to hold different available services
variable_services=tkinter.StringVar()
variable_services.set(services[0])
BookApp_Type_DropDown=tkinter.OptionMenu(
    frame6,
    variable_services,
    *services)#drop down menu 
BookApp_Type_DropDown.pack(side=tkinter.LEFT)
BookApp_Space = tkinter.Label(frame7,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
BookApp_Space.pack()#space between the drop down menu and the return to main menu button
BookApp_Return_Bttn=tkinter.Button(frame7, text="Return to Main Menu", bg="yellow",fg="black",font="calibri 15", command=AppMenu_Window)
BookApp_Return_Bttn.pack(side=tkinter.LEFT)
#creating error messages for surname 
Surname_NoEnt=tkinter.Label(frame6, text="surname has no entry", bg="red", font="15")
Surname_Double=tkinter.Label(frame6, text="surname contains repeated hyphen", bg="red", font="15")
Surname_Space=tkinter.Label(frame6, text="surname contains a space(s)", bg="red", font="15")
Surname_Digit=tkinter.Label(frame6, text="surname contains a digit", bg="red", font="15")
Surname_Char=tkinter.Label(frame6, text="surname contains an invalid character", bg="red", font="15")
#creating error messages for forename
Forename_NoEnt=tkinter.Label(frame6, text="forename has no entry", bg="red", font="15")
Forename_Double=tkinter.Label(frame6, text="forename contains repeated hyphen", bg="red", font="15")
Forename_Space=tkinter.Label(frame6, text="forename contains a space(s)", bg="red", font="15")
Forename_Digit=tkinter.Label(frame6, text="forename contains a digit", bg="red", font="15")
Forename_Char=tkinter.Label(frame6, text="forename contains an invalid character", bg="red", font="15")
#error messages for date
Date_WrongLen=tkinter.Label(frame6, text="date is not a valid length", bg="red", font="15")
Date_Year=tkinter.Label(frame6, text="must be 2022", bg="red", font="15")
Date_Char6=tkinter.Label(frame6, text="character 6 is not a /", bg="red", font="15")
Date_Month=tkinter.Label(frame6, text="month entered is not valid", bg="red", font="15")
Date_Char3=tkinter.Label(frame6, text="charcter 3 is not a /", bg="red", font="15")
Date_Day=tkinter.Label(frame6, text="day entered is not valid", bg="red", font="15")
d1_Great = tkinter.Label(frame6, text="date entered has already happened", bg="red", font="15")
Date_invalid = tkinter.Label(frame6, text="date contains something invalid e.g. day or month" , bg="red",font="15")
#error message when data and time entered has already been booked
Space_taken = tkinter.Label(frame6, text="data and time entered is already taken", bg="red", font ="15")
def validate_name(name, entry):
    if name == "surname":
        Surname_Error = True
        Forename_Error = False
        ViewSur_Error = False
    elif name == "forename":
        Forename_Error = True
        Surname_Error = False
        ViewSur_Error = False
    else:
        ViewSur_Error = True
        Surname_Error = False
        Forename_Error = False
    BookApp_Valid = False
    counter_name = 0
    if entry == "":
        if Surname_Error == True:
            Surname_NoEnt.pack(anchor = 'e')
        elif Forename_Error == True:
            Forename_NoEnt.pack(anchor = 'e')
        elif ViewSur_Error == True:
            ForSurname_NoEnt.pack()
    elif "--" in entry:
        if Surname_Error == True:
            Surname_Double.pack(anchor = 'e')
        elif Forename_Error == True:
            Forename_Double.pack(anchor = 'e')
        elif ViewSur_Error == True:
            ForSurname_Double.pack()
    elif " " in entry:
        if Surname_Error == True:
            Surname_Space.pack(anchor = 'e')
        elif Forename_Error == True:
            Forename_Space.pack(anchor = 'e')
        elif ViewSur_Error == True:
            ForSurname_Space.pack()
    else:
        for i in range(len(entry)):
            if entry[i].isdigit():
                if Surname_Error == True:
                    Surname_Digit.pack(anchor = 'e')
                    break
                elif Forename_Error == True:
                    Forename_Digit.pack(anchor = 'e')
                    break
                elif ViewSur_Error == True:
                    ForSurname_Digit.pack()
                    break
            if entry[i].isalpha() or entry[i] == "-":
                counter_name = counter_name + 1
            else:
                if Surname_Error == True:
                    Surname_Char.pack(anchor = 'e')
                elif Forename_Error == True:
                    Forename_Char.pack(anchor = 'e')
                elif ViewSur_Error == True:
                    ForSurname_Char.pack()
            if counter_name == len(entry):
                BookApp_Valid = True
                return BookApp_Valid
    return False
def validate_date(Type,entry):
    date_valid = False
    counter_date = 0
    if len(entry) != 10:
        if Type == 'Save':
            Date_WrongLen.pack(anchor='e')
        elif Type == 'Edit':
            Date_WrongLen2.pack(anchor = 'e')
    else:
        if entry[6:9].isdigit():
            if int(entry[6]) == 2 and int(entry[7]) == 0 and int(entry[8]) == 2 and int(entry[9]) == 1 or int(entry[9]) == 2:
                counter_date = counter_date + 1
                pass
            else:
                if Type == 'Save':
                    Date_Year.pack(anchor='e')
                elif Type == 'Edit':
                    Date_Year2.pack(anchor = 'e')
        else:
            if Type == 'Save':
                Date_Year.pack(anchor='e')
            elif Type == 'Edit':
                Date_Year2.pack(anchor = 'e')
        if entry[5] == "/":
            counter_date = counter_date + 1
            pass
        else:
            if Type == 'Save':
                Date_Char6.pack(anchor='e')
            elif Type == 'Edit':
                Date_Char62.pack(anchor = 'e')
        if entry[3].isdigit():
            counter_date = counter_date + 1
            pass
        else:
            if Type == 'Save':
                Date_Month.pack(anchor='e')
            elif Type == 'Edit':
                Date_Month2.pack(anchor = 'e')
        if entry[2] == "/":
            counter_date = counter_date + 1
            pass
        else:
            if Type == 'Save':
                Date_Char3.pack(anchor='e')
            elif Type == 'Edit':
                Date_Char32.pack(anchor = 'e')
        if entry[0].isdigit():
            counter_date = counter_date + 1
            pass
        else:
            if Type == 'Save':
                Date_Day.pack(anchor='e')
            elif Type == 'Edit':
                Date_Day2.pack(anchor = 'e')
        if entry[1].isdigit():
            counter_date=counter_date+1
            pass
        else:
            if Type == 'Save':
                Date_Day.pack(anchor='e')
            elif Type == 'Edit':
                Date_Day2.pack(anchor = 'e')
        if counter_date == 6:
            d1 = entry[0] + entry[1]
            m1 = entry[3] + entry[4]
            y1 = entry[6] + entry[7] + entry[8] + entry[9]
            d = int(d1)
            m = int(m1)
            y = int(y1)
            # date in yyyy/mm/dd format
            d1 = datetime.datetime.now()
            try:
                d2 = datetime.datetime(y, m, d)
                # Comparing the dates will return
                # either True or False
                if d1 > d2:
                    if Type == 'Save':
                        d1_Great.pack(anchor='e')
                    elif Type == 'Edit':
                        d1_Great2.pack(anchor = 'e')
                elif d1 < d2:
                    date_valid = True
            except:
                if Type == 'Save':
                    Date_invalid.pack(anchor='e')
                elif Type == 'Edit':
                    Date_invalid2.pack(anchor = 'e')
            return date_valid
def check_data_repeat(Type,entry, time_entry):
    repeat = False
    taken = False
    appointment_data_repeat = []
    for i in range (len(Appointment_Data)):
        if entry == Appointment_Data[i][3]:
            appointment_data_repeat.append(i)
            repeat = True
    if repeat == True:
        for i in range (len(appointment_data_repeat)):
            if time_entry == Appointment_Data[appointment_data_repeat[i]][4]:
                taken = True
    if taken == True:
        if Type == 'Save':
            Space_taken.pack()
        elif Type == 'Edit':
            Space_taken2.pack(side=tkinter.RIGHT)
    return repeat, taken 
#labels to show the user the status of the booking
Unique_ID=tkinter.Label(frame6,text=Unique_Value_Text,bg="#EC927F",fg="white",font="15")           
Data_Saved=tkinter.Label(frame6,text="Data has been saved",bg="green",font="15")    
Data_NotSaved=tkinter.Label(frame6,text="Data has not been saved",bg="red",font="15")
#label to show the user that the csv is open
Csv_open=tkinter.Label(frame6,text="Csv is open, close csv and click save again", bg= "red",font="15")
def Save():
    global counter
    Unique_Value,Unique_Value_Text = Unique_val_calc()
    Clear_Errors()
    Surname_BookApp_Valid = validate_name("surname", BookApp_surname_Ent.get())
    Forename_BookApp_Valid = validate_name("forename", BookApp_forename_Ent.get())
    Data_BookApp_Valid = validate_date("Save",BookApp_Date_Ent.get())
    repeat , taken = check_data_repeat("Save",BookApp_Date_Ent.get(),variable_times.get())
    if taken == False:
        Time_BookApp = variable_times.get()
        Type_BookApp = variable_services.get()
        Surname_BookApp = BookApp_surname_Ent.get().lower()
        Forename_BookApp = BookApp_forename_Ent.get().lower()
        Date_BookApp = BookApp_Date_Ent.get()
        if Surname_BookApp_Valid == True and Forename_BookApp_Valid == True and Data_BookApp_Valid == True:
            try:
                f=open("Appointment ID.csv","a")
                Appointment_info = str(Unique_Value) + "," + Surname_BookApp + "," + Forename_BookApp + "," + Date_BookApp + "," + Time_BookApp + "," + Type_BookApp + "\n"
                f.write(Appointment_info)
                f.close()
                Unique_ID.configure(text=Unique_Value_Text)
                Unique_ID.pack(anchor="e")
                Data_Saved.pack(anchor="e")
                Appointment_Data.append([])
                Appointment_Data[counter].append(str(Unique_Value))
                Appointment_Data[counter].append(Surname_BookApp)
                Appointment_Data[counter].append(Forename_BookApp)
                Appointment_Data[counter].append(Date_BookApp)
                Appointment_Data[counter].append(Time_BookApp)
                Appointment_Data[counter].append(Type_BookApp)
                counter = counter + 1
            except:
                Csv_open.pack()
        else:
            Data_NotSaved.pack(anchor='e')
    if Surname_BookApp_Valid == False or Forename_BookApp_Valid == False or Data_BookApp_Valid == False or repeat == True or taken == True:
        BookApp_Clear_Bttn.configure(text="Click to remove error and data")
#buttons
BookApp_Save_Bttn=tkinter.Button(frame7, text="Save Appointment", bg = "yellow", font = "calibri 15", command= Save)
BookApp_Save_Bttn.pack(side=tkinter.RIGHT)#save button to save data to a csv
BookApp_surname_Ent=tkinter.Entry(frame2,width=20,background="lightgrey")
BookApp_surname_Ent.pack(side=tkinter.RIGHT)#entry box for surname
BookApp_forename_Ent=tkinter.Entry(frame3, width=20,background="lightgrey")
BookApp_forename_Ent.pack(side=tkinter.RIGHT)#entry box for forename
BookApp_Date_Ent=tkinter.Entry(frame4,width=20,background="lightgrey")
BookApp_Date_Ent.pack(side=tkinter.RIGHT)#entry box for date
def Clear_Data():
    BookApp_surname_Ent.delete(0,100)
    BookApp_forename_Ent.delete(0,100)
    BookApp_Date_Ent.delete(0,100)
    variable_services.set(services[0])
    variable_times.set(times[0])
def Clear_Errors():
    Surname_NoEnt.pack_forget()
    Surname_Double.pack_forget()
    Surname_Space.pack_forget()
    Surname_Digit.pack_forget()
    Surname_Char.pack_forget()
    Forename_NoEnt.pack_forget()
    Forename_Double.pack_forget()
    Forename_Space.pack_forget()
    Forename_Digit.pack_forget()
    Forename_Char.pack_forget()
    Date_WrongLen.pack_forget()
    Date_Year.pack_forget()
    Date_Char6.pack_forget()
    Date_Month.pack_forget()
    Date_Char3.pack_forget()
    Date_Day.pack_forget()
    Data_Saved.pack_forget()
    Data_NotSaved.pack_forget()
    Unique_ID.pack_forget()
    Csv_open.pack_forget()
    d1_Great.pack_forget()
    Date_invalid.pack_forget()
    Space_taken.pack_forget()
def Clear_Button():
    Clear_Data()
    Clear_Errors()
    BookApp_Clear_Bttn.configure(text="Clear Data")
#button to clear data from booking page   
BookApp_Clear_Bttn=tkinter.Button(frame7, text="Clear Data", bg="yellow",fg="black", font="calibri 15", command=Clear_Button)
BookApp_Clear_Bttn.pack()
#view appointment
ViewApp=tkinter.Toplevel(AppWindow)
ViewApp.title("View your Appointment")
ViewApp.geometry("600x550")
ViewApp.configure(bg="lightblue")
ViewApp.withdraw()
#ViewApp.attributes('-fullscreen', True)
#viewapp frames
ViewAppframe1=tkinter.Frame(ViewApp)
ViewAppframe1.configure(bg="lightblue")
ViewAppframe1.pack()
ViewAppframe2=tkinter.Frame(ViewApp)
ViewAppframe2.configure(bg="lightblue")
ViewAppframe2.pack()
ViewAppframe3=tkinter.Frame(ViewApp)
ViewAppframe3.configure(bg="lightblue")
ViewAppframe3.pack()
ViewAppframe4=tkinter.Frame(ViewApp)
ViewAppframe4.configure(bg="lightblue")
ViewAppframe4.pack()
ViewAppframe5=tkinter.Frame(ViewApp)
ViewAppframe5.configure(bg="lightblue")
ViewAppframe5.pack()
#title label
ViewApp_Space = tkinter.Label(ViewAppframe1,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 20 bold")
ViewApp_Space.pack()
ViewApp_Title_Lbl=tkinter.Label(ViewAppframe1, text="Nails By Katie - View your Appointment", bg="#EC927F",fg="black",font="calibri 25")
ViewApp_Title_Lbl.pack()
#unique id label and entry box
ViewApp_Space = tkinter.Label(ViewAppframe2,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
ViewApp_Space.pack()
ViewApp_UniID_Lbl=tkinter.Label(ViewAppframe2,text="Unique ID for Appointment",bg="#EC927F",fg="black",font="calibri 15")
ViewApp_UniID_Lbl.pack(side=tkinter.LEFT)
ViewApp_UniID_Ent=tkinter.Entry(ViewAppframe2,width=20,background="lightgrey")
ViewApp_UniID_Ent.pack(side=tkinter.RIGHT)
#placeholder for space to display information
ViewApp_SpaceMd = tkinter.Label(ViewAppframe3,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 30 bold")
ViewApp_SpaceMd.pack()
ViewApp_SpaceMd2= tkinter.Label(ViewAppframe3,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 30 bold")
ViewApp_SpaceMd2.pack()
ViewApp_SpaceMd3 = tkinter.Label(ViewAppframe3,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 30 bold")
ViewApp_SpaceMd3.pack()
#search id button
ViewApp_Space = tkinter.Label(ViewAppframe4,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
ViewApp_Space.pack()
ViewApp_Forgot_Bttn=tkinter.Button(ViewAppframe4,text="Forgotten ID",bg="yellow",fg="black",font="calibri 15",command=ViewApp_Window_Surname)
ViewApp_Forgot_Bttn.pack()
#create error messages
ID_NoEnt=tkinter.Label(ViewAppframe3, text="ID has no entry", bg="red", font="15")
ID_Space=tkinter.Label(ViewAppframe3, text="ID contains a space(s)", bg="red", font="15")
ID_Char=tkinter.Label(ViewAppframe3, text="ID contains an invalid character", bg="red", font="15")
#Appointment not found label
Appointment_NotFound=tkinter.Label(ViewAppframe3,text="A corresponding appointment could not be found",bg="red",font="15")
#takes first position in list to declare variables
Appointment_UniID = Appointment_Data[0][0]
Appointment_Surname = Appointment_Data[0][1]
Appointment_Forename = Appointment_Data[0][2]
Appointment_Date = Appointment_Data[0][3]
Appointment_Time = Appointment_Data[0][4]
Appointment_Type = Appointment_Data[0][5]
#function to set data
def set_data(Appointment_UniID,Appointment_Surname,Appointment_Forename,Appointment_Date,Appointment_Time,Appointment_Type):
    Uni_ID_Str="Unique ID: " + str(Appointment_UniID)
    Surname_Str="Surname: " + str(Appointment_Surname)
    Forename_Str="Forename: " + str(Appointment_Forename)
    Date_Str="Date: " + str(Appointment_Date)
    Time_Str="Time: " + str(Appointment_Time)
    Type_Str="Type of Appointment: " + str(Appointment_Type)
    return Uni_ID_Str,Surname_Str,Forename_Str,Date_Str,Time_Str,Type_Str
#call function to set up data
Uni_ID_Str,Surname_Str,Forename_Str,Date_Str,Time_Str,Type_Str = set_data(Appointment_UniID,Appointment_Surname,Appointment_Forename,Appointment_Date,Appointment_Time,Appointment_Type)
#labels to display information
Appointment_UniqueID_Label=tkinter.Label(ViewAppframe3,text=Uni_ID_Str,bg="#EC927F",fg="white",font="15")
Appointment_Surname_Label=tkinter.Label(ViewAppframe3,text=Surname_Str,bg="#EC927F",fg="white",font="15")
Appointment_Forename_Label=tkinter.Label(ViewAppframe3,text=Forename_Str,bg="#EC927F",fg="white",font="15")
Appointment_Date_Label=tkinter.Label(ViewAppframe3,text=Date_Str,bg="#EC927F",fg="white",font="15")
Appointment_Time_Label=tkinter.Label(ViewAppframe3,text=Time_Str,bg="#EC927F",fg="white",font="15")
Appointment_Type_Label=tkinter.Label(ViewAppframe3,text=Type_Str,bg="#EC927F",fg="white",font="15")
#function to find the appointment position within list
def find_app(ID_ent):
    position = 0
    for i in range (len(Appointment_Data)):
        if Appointment_Data[i][0] == ID_ent:
            Appointment_Position = i
            Appointment_Found = True
            break
        else:
            position = position + 1
        if position == len(Appointment_Data) - 1:
            Appointment_Found = False
            Appointment_Position = 0
    return Appointment_Found, Appointment_Position
#command to search the id
def search_ID():
    clear_ID_Error()
    valid_ID,ID_ent = validate_ID('Search')
    if valid_ID == True:
        Appointment_Found, Appointment_Position = find_app(ID_ent)
        if Appointment_Found ==True:
            Appointment_UniID = Appointment_Data[Appointment_Position][0]
            Appointment_Surname = Appointment_Data[Appointment_Position][1]
            Appointment_Forename = Appointment_Data[Appointment_Position][2]
            Appointment_Date = Appointment_Data[Appointment_Position][3]
            Appointment_Time = Appointment_Data[Appointment_Position][4]
            Appointment_Type = Appointment_Data[Appointment_Position][5]
            Uni_ID_Str,Surname_Str,Forename_Str,Date_Str,Time_Str,Type_Str = set_data(Appointment_UniID,Appointment_Surname,Appointment_Forename,Appointment_Date,Appointment_Time,Appointment_Type)
            Appointment_UniqueID_Label.configure(text=Uni_ID_Str)
            Appointment_Surname_Label.configure(text=Surname_Str)
            Appointment_Forename_Label.configure(text=Forename_Str)
            Appointment_Date_Label.configure(text=Date_Str)
            Appointment_Time_Label.configure(text=Time_Str)
            Appointment_Type_Label.configure(text=Type_Str)
            ViewApp_SpaceMd.pack_forget()
            ViewApp_SpaceMd2.pack_forget()
            Appointment_UniqueID_Label.pack()
            Appointment_Surname_Label.pack()
            Appointment_Forename_Label.pack()
            Appointment_Date_Label.pack()
            Appointment_Time_Label.pack()
            Appointment_Type_Label.pack()
        elif Appointment_Found == False:
            Appointment_NotFound.pack()
#validation function for the ID entry
def validate_ID(Type):
    if Type == 'Search':
        ID_ent = ViewApp_UniID_Ent.get()
        valid_ID=False
        if ID_ent.isalpha():
            ID_Char.pack()
        elif ID_ent == "":
            ID_NoEnt.pack()
        elif " " in ID_ent:
            ID_Space.pack()
        else:
            if ID_ent.isdigit():
                valid_ID=True
            else:
                ID_Char.pack()
    elif Type == 'Edit':
        ID_ent  = EditApp_UniID_Ent.get()
        valid_ID=False
        if ID_ent.isalpha():
            ID_Char2.pack(anchor = 'e')
        elif ID_ent == "":
            ID_NoEnt2.pack(anchor = 'e')
        elif " " in ID_ent:
            ID_Space2.pack(anchor = 'e')
        else:
            if ID_ent.isdigit():
                valid_ID=True
            else:
                ID_Char2.pack(anchor = 'e')
    return valid_ID,ID_ent
def clear_ID_Error():
    ID_NoEnt.pack_forget()
    ID_Char.pack_forget()
    ID_Space.pack_forget()
    Appointment_NotFound.pack_forget()
    ViewApp_SpaceMd.pack()
    ViewApp_SpaceMd2.pack()
    Appointment_UniqueID_Label.pack_forget()
    Appointment_Surname_Label.pack_forget()
    Appointment_Forename_Label.pack_forget()
    Appointment_Date_Label.pack_forget()
    Appointment_Time_Label.pack_forget()
    Appointment_Type_Label.pack_forget()
#button to return to main menu
ViewApp_Return_Bttn=tkinter.Button(ViewAppframe5,text="Return to previous menu",bg="yellow",fg="black",font="calibri 15",command=AppMenu_Window)
ViewApp_Return_Bttn.pack(side=tkinter.LEFT)
#search button
ViewApp_Srch_Bttn=tkinter.Button(ViewAppframe5,text="Search ID for appointment",bg="yellow",fg="black",font="calibri 15",command=search_ID)
ViewApp_Srch_Bttn.pack(side=tkinter.RIGHT)
#creating the branch window where the user can input their surname
ViewAppSur=tkinter.Toplevel(ViewApp)
ViewAppSur.title("Forgot ID")
ViewAppSur.geometry("650x450")
ViewAppSur.configure(bg="lightblue")
ViewAppSur.withdraw()
#creating frames for the window
frame1=tkinter.Frame(ViewAppSur)
frame1.configure(bg="lightblue")
frame1.pack()
frame2=tkinter.Frame(ViewAppSur)
frame2.configure(bg="lightblue")
frame2.pack()
frame3=tkinter.Frame(ViewAppSur)
frame3.configure(bg="lightblue")
frame3.pack()
frame4=tkinter.Frame(ViewAppSur)
frame4.configure(bg="lightblue")
frame4.pack()
#title label
ViewAppSur_Space = tkinter.Label(frame1,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 20 bold")
ViewAppSur_Space.pack()
ViewAppSur_Title_Lbl=tkinter.Label(frame1, text="Nails By Katie - Forgot ID", bg="#EC927F",fg="black",font="calibri 25")
ViewAppSur_Title_Lbl.pack()
#surname label and entry box
ViewAppSur_Space = tkinter.Label(frame2,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
ViewAppSur_Space.pack()
ViewAppSur_Surname_Lbl=tkinter.Label(frame2,text="Surname for Appointment",bg="#EC927F",fg="black",font="calibri 15")
ViewAppSur_Surname_Lbl.pack(side=tkinter.LEFT)
ViewAppSur_Surname_Ent=tkinter.Entry(frame2,width=20,background="lightgrey")
ViewAppSur_Surname_Ent.pack(side=tkinter.RIGHT)
#reserve space between entry and buttons at the bottom of the page
ViewAppSur_Space = tkinter.Label(frame3,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 15 bold")
ViewAppSur_Space.pack()
ViewAppSur_Space = tkinter.Label(frame3,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 30 bold")
ViewAppSur_Space.pack()
#return to previous menu button
ViewAppSur_Space = tkinter.Label(frame4,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
ViewAppSur_Space.pack()
ViewAppSur_Return_Bttn=tkinter.Button(frame4,text="Return to previous menu",bg="yellow",fg="black",font="calibri 15",command=ViewApp_Window)
ViewAppSur_Return_Bttn.pack(side=tkinter.LEFT)
#error message labels
ForSurname_NoEnt=tkinter.Label(frame3, text="surname has no entry", bg="red", font="15")
ForSurname_Double=tkinter.Label(frame3, text="surname contains repeated hyphen", bg="red", font="15")
ForSurname_Space=tkinter.Label(frame3, text="surname contains a space(s)", bg="red", font="15")
ForSurname_Digit=tkinter.Label(frame3, text="surname contains a digit", bg="red", font="15")
ForSurname_Char=tkinter.Label(frame3, text="surname contains an invalid character", bg="red", font="15")
#error message when the user has no future appointments
ViewAppSur_pastapp=tkinter.Label(frame3, text="no future appointments", bg="red", font="15")
#error message for no appointment found
ForSurname_SurnameNotFound=tkinter.Label(frame3,text="surname has no corresponding appointment(s)",bg="red",font="15")
#search button
appointment_surname_position = []
appointment_surname_position_past = []
appointment_surname_dates = []
def search_surname():
    appointment_surname_position.clear()#clears list when the function is run
    position = 0
    surname_tosearch = ViewAppSur_Surname_Ent.get().lower()
    for i in range(len(Appointment_Data)):
        if Appointment_Data[i][1] == surname_tosearch:
            appointment_surname_position.append(i)
            Appointment_Found = True
        else:
            position = position + 1
        if position == len(Appointment_Data):
            Appointment_Found = False
    return Appointment_Found,surname_tosearch
def compareDate():
    pastapp = False
    appointment_surname_position_past.clear()
    appointment_surname_dates.clear()
    for i in range(len(appointment_surname_position)):
        CurrentAppDate = Appointment_Data[appointment_surname_position[i]][3]
        d1 = CurrentAppDate[0] + CurrentAppDate[1]
        m1 = CurrentAppDate[3] + CurrentAppDate[4]
        y1 = CurrentAppDate[6] + CurrentAppDate[7] + CurrentAppDate[8] + CurrentAppDate[9]
        d = int(d1)
        m = int(m1)
        y = int(y1)
        # date in yyyy/mm/dd format
        d1 = datetime.datetime.now()
        d2 = datetime.datetime(y, m, d)
        if d2 > d1:
            appointment_surname_position_past.append(appointment_surname_position[i])
    if appointment_surname_position_past == []:
        pastapp = True
    return pastapp
def orderDate(appointment_surname_dates,surname_tosearch,distance_date,temp_position):
    temp_dates = []
    new_date_order = []
    for i in range (len(appointment_surname_position_past)):
        appointment_surname_dates.append(Appointment_Data[appointment_surname_position_past[i]][3])
    #order the dates based on their distances, pass the list back of ordered dates and use same i and y range loops
    date_current = datetime.datetime.now()
    for i in range(len(appointment_surname_dates)):
        CurrentAppDate = appointment_surname_dates[i]
        d1 = CurrentAppDate[0] + CurrentAppDate[1]
        m1 = CurrentAppDate[3] + CurrentAppDate[4]
        y1 = CurrentAppDate[6] + CurrentAppDate[7] + CurrentAppDate[8] + CurrentAppDate[9]
        d = int(d1)
        m = int(m1)
        y = int(y1)
        d2 = datetime.datetime(y, m, d)
        temp_dates.append(d2)
        distance = d2 - date_current
        distance = distance.days
        distance_date.append(distance)
    distance_date = sorted(distance_date)
    for i in range (len(appointment_surname_dates)):
        order = False
        pointer = 0
        while order == False:
            value = temp_dates[pointer] - date_current
            if distance_date[i] == value.days:
                new_date_order.append(appointment_surname_dates[pointer])
                order = True
            else:
                pointer = pointer + 1
    for i in range(len(appointment_surname_dates)):
        for y in range(len(Appointment_Data)):
            if new_date_order[i] == Appointment_Data[y][3] and surname_tosearch == Appointment_Data[y][1]:
                temp_position.append(y)
    return temp_position,distance_date
#creating strings for appointment display labels
SearchSurname_AppInfo_Str = "0"
#label to display information
SearchSurname_AppInfo_Lbl_1=tkinter.Label(frame3,text=SearchSurname_AppInfo_Str,bg="#EC927F",fg="white",font="calibri 9")
SearchSurname_AppInfo_Lbl_2=tkinter.Label(frame3,text=SearchSurname_AppInfo_Str,bg="#EC927F",fg="white",font="calibri 9")
SearchSurname_AppInfo_Lbl_3=tkinter.Label(frame3,text=SearchSurname_AppInfo_Str,bg="#EC927F",fg="white",font="calibri 9")
def app_SearchSurname_variables(i,temp_position,date_distance):
    #the function will now create variables based on the position and back them using a different function
    UniqueID_SearchSurname = Appointment_Data[temp_position[i]][0]
    Surname_SearchSurname = Appointment_Data[temp_position[i]][1]
    Forename_SearchSurname = Appointment_Data[temp_position[i]][2]
    Date_SearchSurname = Appointment_Data[temp_position[i]][3]
    Time_SearchSurname = Appointment_Data[temp_position[i]][4]
    Type_SearchSurname = Appointment_Data[temp_position[i]][5]
    UniqueID_SearchSurname_Str="Unique ID: " + str(UniqueID_SearchSurname)
    Surname_SearchSurname_Str=" Surname: " + str(Surname_SearchSurname)
    Forename_SearchSurname_Str=" Forename: " + str(Forename_SearchSurname)
    Date_SearchSurname_Str=" Date: " + str(Date_SearchSurname)
    Time_SearchSurname_Str=" Time: " + str(Time_SearchSurname)
    Type_SearchSurname_Str=" Type of Appointment: " + str(Type_SearchSurname)
    SearchSurname_AppInfo_Str = UniqueID_SearchSurname_Str + Surname_SearchSurname_Str + Forename_SearchSurname_Str + Date_SearchSurname_Str + Time_SearchSurname_Str + Type_SearchSurname_Str
    return SearchSurname_AppInfo_Str
def packlabels(SearchSurname_AppInfo_Str,pointer):
    if pointer == 1:
        SearchSurname_AppInfo_Lbl_1.configure(text = SearchSurname_AppInfo_Str)
        SearchSurname_AppInfo_Lbl_1.pack()
    elif pointer == 2:
        SearchSurname_AppInfo_Lbl_2.configure(text=SearchSurname_AppInfo_Str)
        SearchSurname_AppInfo_Lbl_2.pack()
    elif pointer == 3:
        SearchSurname_AppInfo_Lbl_3.configure(text=SearchSurname_AppInfo_Str)
        SearchSurname_AppInfo_Lbl_3.pack()
def clearErrors():
    SearchSurname_AppInfo_Lbl_1.pack_forget()
    SearchSurname_AppInfo_Lbl_2.pack_forget()
    SearchSurname_AppInfo_Lbl_3.pack_forget()
    ForSurname_NoEnt.pack_forget()
    ForSurname_Double.pack_forget()
    ForSurname_Space.pack_forget()
    ForSurname_Digit.pack_forget()
    ForSurname_Char.pack_forget()
    ViewAppSur_pastapp.pack_forget()
def SearchSurname():
    temp_position = []
    distance_date = []
    pointer = 1
    clearErrors()
    ForSurname_valid = validate_name("forgot-surname", ViewAppSur_Surname_Ent.get())
    if ForSurname_valid == True:
        Appointment_Found,surname_tosearch = search_surname()
        if Appointment_Found == True:
            pastapp = compareDate()
            if pastapp == True:
                ViewAppSur_pastapp.pack()
            else:
                pass
            temp_position,distance_date = orderDate(appointment_surname_dates,surname_tosearch,distance_date,temp_position)
            if len(appointment_surname_position_past) <= 3:
                for i in range (len(appointment_surname_position_past)):
                    SearchSurname_AppInfo_Str = app_SearchSurname_variables(i,temp_position,distance_date)
                    packlabels(SearchSurname_AppInfo_Str,pointer)
                    pointer = pointer + 1
            else:
                for i in range (3):
                    SearchSurname_AppInfo_Str = app_SearchSurname_variables(i)
                    packlabels(SearchSurname_AppInfo_Str,pointer)
                    pointer = pointer + 1
        if Appointment_Found == False:
            ForSurname_SurnameNotFound.pack()
#search button for surname 
ViewAppSur_Srch_Bttn=tkinter.Button(frame4,text="Search surname for appointment(s)",bg="yellow",fg="black",font="calibri 15",command=SearchSurname)
ViewAppSur_Srch_Bttn.pack(side=tkinter.RIGHT)

#edit appointment window
EditApp=tkinter.Toplevel(AppWindow)
EditApp.title("Edit your Appointment")
EditApp.geometry("550x450")
EditApp.configure(bg="lightblue")
EditApp.withdraw()
#frame creation 
EditAppframe1=tkinter.Frame(EditApp)
EditAppframe1.configure(bg="lightblue")
EditAppframe1.pack()
EditAppframe2=tkinter.Frame(EditApp)
EditAppframe2.configure(bg="lightblue")
EditAppframe2.pack()
EditAppframe3=tkinter.Frame(EditApp)
EditAppframe3.configure(bg="lightblue")
EditAppframe3.pack()
EditAppframe4=tkinter.Frame(EditApp)
EditAppframe4.configure(bg="lightblue")
EditAppframe4.pack()
EditAppframe5=tkinter.Frame(EditApp)
EditAppframe5.configure(bg="lightblue")
EditAppframe5.pack()
#space and title of the window
EditApp_Space = tkinter.Label(EditAppframe1,text="Nails By Katie - Book an Appointment",bg="lightblue",fg="lightblue",font="calibri 20 bold")
EditApp_Space.pack()
EditApp_Title_Lbl=tkinter.Label(EditAppframe1, text="Nails By Katie - Edit your Appointment", bg="#EC927F",fg="black",font="calibri 25")
EditApp_Title_Lbl.pack()
#space, entry box and label
EditApp_Space = tkinter.Label(EditAppframe2,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
EditApp_Space.pack()
EditApp_UniID_Lbl = tkinter.Label(EditAppframe2,text="Unique ID:",bg="#EC927F",fg="black",font="calibri 15")
EditApp_UniID_Lbl.pack(side=tkinter.LEFT)
EditApp_UniID_Ent = tkinter.Entry(EditAppframe2,width=20,background="lightgrey")
EditApp_UniID_Ent.pack(side=tkinter.RIGHT)
#space between unique ID and drop down menus
EditApp_Space = tkinter.Label(EditAppframe3,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
EditApp_Space.pack()
#create lists for drop down to choose field to change
field_change = ["Date","Time","Type"]
variable_field=tkinter.StringVar()
variable_field.set(field_change[0])
EditApp_field_dropdown=tkinter.OptionMenu(
    EditAppframe3,
    variable_field,
    *field_change)
EditApp_field_dropdown.pack(side=tkinter.LEFT)
#times drop down menu
#already declared on line 260
EditApp_Time_dropdown=tkinter.OptionMenu(
    EditAppframe3,
    variable_times,
    *times)
#entry box to change date
EditApp_Date_Ent = tkinter.Entry(EditAppframe3,width = 20, background = "lightgrey")
EditApp_Date_Ent.pack(side=tkinter.RIGHT)
#type drop down menu
#declared line 272
BookApp_Type_DropDown=tkinter.OptionMenu(
    EditAppframe3,
    variable_services,
    *services)

#loop to look at field_change option and pack accordingly
def check_choice():
    global choice
    choice = variable_field.get()
    if choice == "Time":
        BookApp_Type_DropDown.pack_forget()
        EditApp_Date_Ent.pack_forget()
        EditApp_Time_dropdown.pack(side=tkinter.RIGHT)
    if choice == "Type":
        BookApp_Type_DropDown.pack(side=tkinter.RIGHT)
        EditApp_Date_Ent.pack_forget()
        EditApp_Time_dropdown.pack_forget()
    if choice == "Date":
        BookApp_Type_DropDown.pack_forget()
        EditApp_Date_Ent.pack(side=tkinter.RIGHT)
        EditApp_Time_dropdown.pack_forget()
    EditApp.after(500,check_choice)
#validating entries
def write_csv():
    try:
        f=open("Appointment ID.csv","w")
        for i in range (len(Appointment_Data)):
            line=""
            line=Appointment_Data[i][0]+","+Appointment_Data[i][1]+","+Appointment_Data[i][2]+","+Appointment_Data[i][3]+","+Appointment_Data[i][4]+","+Appointment_Data[i][5]+"\n"
            f.write(line)
        f.close()
        Edit_success.pack(side=tkinter.RIGHT)
    except:
        Csv_open2.pack(side=tkinter.RIGHT)
def save_edit():
    clear_edit_errors()
    valid_ID,ID_ent = validate_ID('Edit')
    if choice == "Date":
        date_valid = validate_date('Edit',EditApp_Date_Ent.get())
        if valid_ID == True and date_valid == True:
            Appointment_Found, Appointment_Position = find_app(ID_ent)
            if Appointment_Found == True:
                if choice == 'Date':
                    repeat , taken = check_data_repeat("Edit",EditApp_Date_Ent.get(),Appointment_Data[Appointment_Position][4])
                    if taken == False:
                        #save edit
                        Appointment_Data[Appointment_Position][3] = EditApp_Date_Ent.get()
                        write_csv()
            elif Appointment_Found == False:
                Appointment_NotFound2.pack(side=tkinter.RIGHT)
    else:
        if valid_ID == True:
            Appointment_Found, Appointment_Position = find_app(ID_ent)
            if Appointment_Found == False:
                Appointment_NotFound2.pack(side=tkinter.RIGHT)
            else:
                if choice == 'Time':
                    repeat = False
                    taken = False
                    appointment_data_repeat = []
                    for i in range (len(Appointment_Data)):
                        if Appointment_Data[Appointment_Position][3] == Appointment_Data[i][3]:
                            appointment_data_repeat.append(i)
                            repeat = True
                    if repeat == True:
                        for i in range (len(appointment_data_repeat)):
                            if Appointment_Data[appointment_data_repeat[i]][4] == variable_times.get():
                                taken = True
                                Space_taken2.pack(side=tkinter.RIGHT)
                    if taken == False:
                        #save edit
                        Appointment_Data[Appointment_Position][4] = variable_times.get()
                        write_csv()
                elif choice == 'Type':
                    Appointment_Data[Appointment_Position][5] = variable_services.get()
                    write_csv()
                    #save edit
EditApp.after(0,check_choice)
#function to clear entry boxes and remove errors.
def clear_edit_entries():
    EditApp_UniID_Ent.delete(0,100)
    EditApp_Date_Ent.delete(0,100)
    variable_field.set(field_change[0])
    variable_times.set(times[0])
    variable_services.set(services[0])
    clear_edit_errors()
#function to clear error messages
def clear_edit_errors():
    ID_NoEnt2.pack_forget()
    ID_Char2.pack_forget()
    ID_Space2.pack_forget()
    Date_WrongLen2.pack_forget()
    Date_Year2.pack_forget()
    Date_Char62.pack_forget()
    Date_Month2.pack_forget()
    Date_Char32.pack_forget()
    Date_Day2.pack_forget()
    d1_Great2.pack_forget()
    Date_invalid2.pack_forget()
    Appointment_NotFound2.pack_forget()
    Space_taken2.pack_forget()
    Edit_success.pack_forget()
    Csv_open2.pack_forget()
#space between field choice and cancel button
EditApp_Space = tkinter.Label(EditAppframe4,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
EditApp_Space.pack()
#creating cancel appointment button
EditApp_Cancel_Bttn=tkinter.Button(EditAppframe4,text="Cancel Appointment",bg="red",fg="black",font="calibri 14",command=CancelApp_Window)
EditApp_Cancel_Bttn.pack(side=tkinter.LEFT)
#space between cancel button and return buttons
EditApp_Space = tkinter.Label(EditAppframe5,text="Nails By Katie - Admin Page",bg="lightblue",fg="lightblue",font="calibri 25 bold")
EditApp_Space.pack()
#return button
EditApp_Return_Bttn=tkinter.Button(EditAppframe5,text="Return to Menu",bg="yellow",fg="black",font="calibri 15",command=AppMenu_Window)
EditApp_Return_Bttn.pack(side=tkinter.LEFT)
#clear button
EditApp_Clear_Bttn=tkinter.Button(EditAppframe5,text="Clear Entries",bg="yellow",fg="black",font="calibri 15",command=clear_edit_entries)
EditApp_Clear_Bttn.pack(side=tkinter.LEFT)
#save button
EditApp_Save_Bttn=tkinter.Button(EditAppframe5,text="Save Changes",bg="yellow",fg="black",font="calibri 15",command=save_edit)
EditApp_Save_Bttn.pack(side=tkinter.RIGHT)
#id error messages
ID_NoEnt2=tkinter.Label(EditAppframe4, text="ID has no entry", bg="red", font="15")
ID_Space2=tkinter.Label(EditAppframe4, text="ID contains a space(s)", bg="red", font="15")
ID_Char2=tkinter.Label(EditAppframe4, text="ID contains an invalid character", bg="red", font="15")
#date error messages
Date_WrongLen2=tkinter.Label(EditAppframe4, text="Date is not a valid length", bg="red", font="15")
Date_Year2=tkinter.Label(EditAppframe4, text="Must be 2022", bg="red", font="15")
Date_Char62=tkinter.Label(EditAppframe4, text="Character 6 is not a /", bg="red", font="15")
Date_Month2=tkinter.Label(EditAppframe4, text="Month entered is not valid", bg="red", font="15")
Date_Char32=tkinter.Label(EditAppframe4, text="Charcter 3 is not a /", bg="red", font="15")
Date_Day2=tkinter.Label(EditAppframe4, text="Day entered is not valid", bg="red", font="15")
d1_Great2 = tkinter.Label(EditAppframe4, text="Date entered has already happened", bg="red", font="15")
Date_invalid2 = tkinter.Label(EditAppframe4, text="Date contains something invalid" , bg="red",font="15")
#appointment not found error message
Appointment_NotFound2=tkinter.Label(EditAppframe4,text="Appointment not be found",bg="red",font="15")
#appointment time already taken error message
Space_taken2 = tkinter.Label(EditAppframe4, text="data and time taken", bg="red", font ="15")
#label to confirm save
Edit_success = tkinter.Label(EditAppframe4, text="edit successful",bg = "green",font= "15")
#csv is open and cannot make changes
Csv_open2=tkinter.Label(EditAppframe4,text="Csv is open", bg= "red",font="15")


#creating window for cancel app window
CancelApp=tkinter.Toplevel(EditApp)
CancelApp.title("Cancel your Appointment")
CancelApp.geometry("440x100")
CancelApp.configure(bg="grey")
CancelApp.withdraw()
#frames for cancel app window
CancelAppframe1=tkinter.Frame(CancelApp)
CancelAppframe1.configure(bg="grey")
CancelAppframe1.pack()
CancelAppframe2=tkinter.Frame(CancelApp)
CancelAppframe2.configure(bg="grey")
CancelAppframe2.pack()
#label to ask user wether they want to cancel
ConfirmCancel_Lbl = tkinter.Label(CancelAppframe1,text="Are you sure you want to cancel your appointment?",bg="lightgrey",fg="black",font="calibri 14")
ConfirmCancel_Lbl.pack()
#space between title and buttons
CancelApp_Space = tkinter.Label(CancelAppframe2,text="Nails By Katie - Admin Page",bg="grey",fg="grey",font="calibri 12 bold")
CancelApp_Space.pack()
#yes button
Cancel_Y_Bttn=tkinter.Button(CancelAppframe2,text=" Yes ",bg="lightgrey",fg="green",width = "10",font="calibri 12",command=EditApp_Window)
Cancel_Y_Bttn.pack(side=tkinter.LEFT)
Cancel_N_Bttn=tkinter.Button(CancelAppframe2,text=" No ",bg="lightgrey",fg="red",width = "10" ,font="calibri 12",command=EditApp_Window)
Cancel_N_Bttn.pack(side=tkinter.RIGHT)

