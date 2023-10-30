from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from Trial import StudentDatabase

db = StudentDatabase()

root = Tk()
root.title("Student Information System")

custom_font = Font(family="Arial", size=12, weight="bold")
back = "#FFFFFF"
front = "#82008B"
b1 = "#040A7D"

button_style = ttk.Style()
button_style.configure("TButton", font=custom_font, background="#F90707", foreground="white")

label_style = ttk.Style()
label_style.configure("TLabel", font=custom_font, foreground="white")

welcome_label = Label(root, text="Welcome to the Student Information System", font=("Arial", 20, "bold"), bg="#FF0000", fg="#FFFFFF")
welcome_label.pack(pady=8)
bg_color1 = "#040A7D"
bg_color2 = "#2393CB"

canvas = Canvas(root, width=200, height=300, bg=bg_color1, highlightthickness=0)
canvas.pack(fill="both", expand=True)

gradient = PhotoImage(width=1, height=1)
for x in range(400):
    r = int(x / 400 * (int(bg_color2[1:3], 16) - int(bg_color1[1:3], 16)) + int(bg_color1[1:3], 16))
    g = int(x / 400 * (int(bg_color2[3:5], 16) - int(bg_color1[3:5], 16)) + int(bg_color1[3:5], 16))
    b = int(x / 400 * (int(bg_color2[5:7], 16) - int(bg_color1[5:7], 16)) + int(bg_color1[5:7], 16))
    color = f"#{r:02X}{g:02X}{b:02X}"
    gradient.put(color, (x, 0))

canvas.create_image(0, 0, anchor="nw", image=gradient)

def open_register_window():
    register_window = Toplevel(root)
    register_window.title("Register")
    register_window.geometry("500x400")
    register_window.configure(bg=b1)

    roll_label = Label(register_window, text="Roll Number:", bg=back, fg=front, font=custom_font)
    roll_label.grid(row=0, column=0, padx=10, pady=5)

    first_name_label = Label(register_window, text="First Name", bg=back, fg=front, font=custom_font)
    first_name_label.grid(row=1, column=0, padx=10, pady=5)

    last_name_label = Label(register_window, text="Last Name:", bg=back, fg=front, font=custom_font)
    last_name_label.grid(row=2, column=0, padx=10, pady=5)

    age_label = Label(register_window, text="Age:", bg=back, fg=front, font=custom_font)
    age_label.grid(row=3, column=0, padx=10, pady=5)

    section_label = Label(register_window, text="Section:", bg=back, fg=front, font=custom_font)
    section_label.grid(row=4, column=0, padx=10, pady=5)

    Gender_label = Label(register_window, text="Gender", bg=back, fg=front, font=custom_font)
    Gender_label.grid(row=5, column=0, padx=100, pady=5, sticky="w")

    gender_var = StringVar()
    gender_var.set("Male")

    gender_frame = Frame(register_window, bg=back)
    gender_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    male_checkbox = Checkbutton(gender_frame, text="Male", variable=gender_var, onvalue="Male", offvalue="Male", bg=back, fg=front, font=custom_font)
    male_checkbox.pack(side="left")

    female_checkbox = Checkbutton(gender_frame, text="Female", variable=gender_var, onvalue="Female", offvalue="Female", bg=back, fg=front, font=custom_font)
    female_checkbox.pack(side="left")

    contact_label = Label(register_window, text="Contact Number:", bg=back, fg=front, font=custom_font)
    contact_label.grid(row=6, column=0, padx=10, pady=5)

    password_label = Label(register_window, text="Password:", bg=back, fg=front, font=custom_font)
    password_label.grid(row=7, column=0, padx=10, pady=5)

    roll_entry = Entry(register_window)
    roll_entry.grid(row=0, column=1, padx=10, pady=5)

    first_name_entry = Entry(register_window)
    first_name_entry.grid(row=1, column=1, padx=10, pady=5)

    last_name_entry = Entry(register_window)
    last_name_entry.grid(row=2, column=1, padx=10, pady=5)

    age_entry = Entry(register_window)
    age_entry.grid(row=3, column=1, padx=10, pady=5)

    section_entry = Entry(register_window)
    section_entry.grid(row=4, column=1, padx=10, pady=5)

    contact_entry = Entry(register_window)
    contact_entry.grid(row=6, column=1, padx=10, pady=5)

    password_entry = Entry(register_window, show="*")
    password_entry.grid(row=7, column=1, padx=10, pady=5)

    def register():
        RollNumber = roll_entry.get()
        FirstName = first_name_entry.get()
        LastName = last_name_entry.get()
        Age = age_entry.get()
        Section = section_entry.get()
        Gender = gender_var.get()
        ContactNumber = contact_entry.get()
        Password = password_entry.get()

        if RollNumber and FirstName and LastName and Age and Section and Gender and ContactNumber and Password:
            db.insert(RollNumber, FirstName, LastName, Age, Section, Gender, ContactNumber, Password)
            messagebox.showinfo("Register", "Registration Successful!")
        else:
            messagebox.showerror("Register", "Please fill in all fields.")

    register_button = Button(register_window, text="Register", command=register, bg="Red", fg="white", font=custom_font)
    register_button.grid(row=8, column=0, columnspan=2, pady=10)

def open_login_window():
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.configure(bg=b1)
    login_window.geometry("300x200")

    username_label = Label(login_window, text="Roll Number:", bg=back, fg=front, font=custom_font)
    username_label.grid(row=0, column=0, padx=10, pady=5)

    username_entry = Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = Label(login_window, text="Password:", bg=back, fg=front, font=custom_font)
    password_label.grid(row=1, column=0, padx=10, pady=5)

    password_entry = Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    def login():
        RollNumber = username_entry.get()
        Password = password_entry.get()
        if db.check_login(RollNumber, Password):
            student_info = db.fetch_student_info(RollNumber)
            show_student_info(student_info, login_window)
        else:
            messagebox.showerror("Login", "Invalid Roll Number or Password")

    login_button = Button(login_window, text="Login", command=login, bg=back, fg=front, font=custom_font)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

def show_student_info(student_info, login_window):
    if student_info:
        name = f"{student_info[1]} {student_info[2]}"
        login_window.destroy()
        welcome_window = Toplevel(root)
        welcome_window.title("Welcome")
        welcome_window.geometry("300x300")
        welcome_window.configure(bg=b1)
        welcome_label = Label(welcome_window, text=f"Hello, {name}!", bg="WHITE", fg="#0D00FF", font=custom_font)
        welcome_label.pack(padx=40, pady=20)
        view_data_button = Button(welcome_window, text="View My Data", command=lambda: view_student_data(student_info[0]), bg="Orange", fg="White", font=Font(weight="bold", family="arial"))
        view_data_button.pack()
        update_profile_button = Button(welcome_window, text="Update Profile", command=lambda: update_profile(student_info[0]), bg="green", fg="white", font=Font(weight="bold", family="arial"))
        update_profile_button.pack()
        delete_button = Button(welcome_window, text="Delete Student", command=lambda: delete_student(student_info[0], welcome_window), bg="red", fg="white", font=custom_font)
        delete_button.pack()
        logout_button = Button(welcome_window, text="Log Out", command=logout, bg="white", fg="#82008B", font=Font(weight="bold", family="arial"))
        logout_button.pack()
    else:
        messagebox.showerror("Login", "Invalid Roll Number or Password")

def view_student_data(RollNumber):
    student_info = db.fetch_student_info(RollNumber)
    if student_info:
        data_window = Toplevel(root)
        data_window.title("Student Data")
        data_window.configure(bg=b1)

        data_label = Label(data_window, text=f"Student Data for Roll Number: {RollNumber}", bg="#F0F0F0", fg="RED", font=custom_font)
        data_label.pack(padx=20, pady=10)

        data_text = f"Name: {student_info[1]} {student_info[2]}\n"
        data_text += f"Age: {student_info[3]}\n"
        data_text += f"Section: {student_info[4]}\n"
        data_text += f"Gender: {student_info[5]}\n"
        data_text += f"Contact Number: {student_info[6]}\n"

        data_info_label = Label(data_window, text=data_text, bg="#F0F0F0", fg="#040A7D", font=custom_font)
        data_info_label.pack(padx=20, pady=10)

def update_profile(RollNumber):
    student_info = db.fetch_student_info(RollNumber)
    if student_info:
        update_window = Toplevel(root)
        update_window.title("Update Profile")
        update_window.geometry("500x400")
        update_window.configure(bg=b1)

        roll_label = Label(update_window, text="Roll Number:", bg=back, fg=front, font=custom_font)
        roll_label.grid(row=0, column=0, padx=10, pady=5)
        roll_label.config(state='disabled')

        first_name_label = Label(update_window, text="First Name:", bg=back, fg=front, font=custom_font)
        first_name_label.grid(row=1, column=0, padx=10, pady=5)

        last_name_label = Label(update_window, text="Last Name:", bg=back, fg=front, font=custom_font)
        last_name_label.grid(row=2, column=0, padx=10, pady=5)

        age_label = Label(update_window, text="Age:", bg=back, fg=front, font=custom_font)
        age_label.grid(row=3, column=0, padx=10, pady=5)

        section_label = Label(update_window, text="Section:", bg=back, fg=front, font=custom_font)
        section_label.grid(row=4, column=0, padx=10, pady=5)

        Gender_label = Label(update_window, text="Gender", bg=back, fg=front, font=custom_font)
        Gender_label.grid(row=5, column=0, padx=100, pady=5, sticky="w")

        gender_var = StringVar(value=student_info[5])
        gender_var.set("Male")

        gender_frame = Frame(update_window, bg=back)
        gender_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        male_checkbox = Checkbutton(gender_frame, text="Male", variable=gender_var, onvalue="Male", offvalue="Male", bg=back, fg=front, font=custom_font)
        male_checkbox.pack(side="left")

        female_checkbox = Checkbutton(gender_frame, text="Female", variable=gender_var, onvalue="Female", offvalue="Female", bg=back, fg=front, font=custom_font)
        female_checkbox.pack(side="left")

        contact_label = Label(update_window, text="Contact Number:", bg=back, fg=front, font=custom_font)
        contact_label.grid(row=6, column=0, padx=10, pady=5)

        password_label = Label(update_window, text="New Password:", bg=back, fg=front, font=Font(family="Arial", size=12, weight="bold"))
        password_label.grid(row=7, column=0, padx=10, pady=5)

        roll_entry = Entry(update_window)
        roll_entry.grid(row=0, column=1, padx=10, pady=5)
        roll_entry.insert(0, student_info[0])
        roll_entry.config(state='disabled')

        first_name_entry = Entry(update_window)
        first_name_entry.grid(row=1, column=1, padx=10, pady=5)
        first_name_entry.insert(0, student_info[1])

        last_name_entry = Entry(update_window)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)
        last_name_entry.insert(0, student_info[2])

        age_entry = Entry(update_window)
        age_entry.grid(row=3, column=1, padx=10, pady=5)
        age_entry.insert(0, student_info[3])

        section_entry = Entry(update_window)
        section_entry.grid(row=4, column=1, padx=10, pady=5)
        section_entry.insert(0, student_info[4])

        contact_entry = Entry(update_window)
        contact_entry.grid(row=6, column=1, padx=10, pady=5)
        contact_entry.insert(0, student_info[6])

        password_entry = Entry(update_window, show="*")
        password_entry.grid(row=7, column=1, padx=10, pady=5)
        password_entry.insert(0, student_info[7])

        def update():
            RollNumber
            FirstName = first_name_entry.get()
            LastName = last_name_entry.get()
            Age = age_entry.get()
            Section = section_entry.get()
            Gender = gender_var.get()
            ContactNumber = contact_entry.get()
            Password = password_entry.get()

            if RollNumber and FirstName and LastName and Age and Section and Gender and ContactNumber and Password:
                db.update_student_info(RollNumber, FirstName, LastName, Age, Section, ContactNumber, Password)
                messagebox.showinfo("Update Profile", "Profile Updated Successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Update Profile", "Please fill in all fields, including the new password.")

        update_button = Button(update_window, text="Update", command=update, bg="#F90707", fg="white", font=custom_font)
        update_button.grid(row=8, column=0, columnspan=2, pady=10)

def delete_student(student_roll_number, welcome_window):
    result = messagebox.askyesno("Delete Student", "Are you sure you want to delete this profile?")
    if result:
        db.delete_student(student_roll_number)
        messagebox.showinfo("Delete Student", "Profile deleted successfully!")
        welcome_window.destroy()

def logout():
    root.destroy()

login_button = Button(root, text="Login", command=open_login_window, bg="white", fg="#82008B", font=custom_font)
login_button.pack(pady=40)
login_button.place(relx=0.5, rely=0.4, anchor="center")

register_button = Button(root, text="Register", command=open_register_window, bg="white", fg="#82008B", font=custom_font)
register_button.pack()
register_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
