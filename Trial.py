
import sqlite3
class StudentDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("INFO.db")
        self.c = self.connection.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS DATA (
                Roll_no varchar(10) UNIQUE NOT NULL,
                Fname varchar(10) NOT NULL,
                Lname varchar(10) NOT NULL,
                Age int NOT NULL,
                Section Varchar(10) NOT NULL,
                Gender varchar(6) NOT NULL,
                Contact_No NUMBER(10) NOT NULL,
                Password varchar(10) NOT NULL)""")
            self.connection.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print("Table creation is unsuccessful\n", e)

    def insert(self, Roll_no, Fname, Lname, Age, Section, Gender, Contact_No, Password):
        try:
            self.c.execute(
            "INSERT INTO DATA (Roll_no, Fname, Lname, Age, Section, Gender, Contact_No, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (Roll_no, Fname, Lname, Age, Section, Gender, Contact_No, Password)
            )  
            self.connection.commit()
            print("Data inserted successfully")
        except sqlite3.Error as e:
            print("Data insertion is unsuccessful\n", e)


    def fetch_student_info(self, Roll_no):
        try:
            self.c.execute("SELECT * FROM DATA WHERE Roll_no = ?", (Roll_no,))
            student_info = self.c.fetchone()
            return student_info
        except sqlite3.Error as e:
            print("Fetching student info unsuccessful\n", e)

    def check_login(self, Roll_no, Password):
        try:
            self.c.execute("SELECT Roll_no, Password FROM DATA WHERE Roll_no = ? AND Password = ?", (Roll_no, Password))
            result = self.c.fetchone()
            if result:
                return True  # Authentication successful
            else:
                return False  # Authentication failed
        except sqlite3.Error as e:
            print("Fetching unsuccessful\n", e)
    def delete_student(self, Roll_no):
        try:
            self.c.execute("DELETE FROM DATA WHERE Roll_no = ?", (Roll_no,))
            self.connection.commit()
            print("Student deleted successfully")
        except sqlite3.Error as e:
            print("Deletion is unsuccessful\n", e)
    def update_student_info(self, Roll_no, Fname, Lname, Age, Section, Contact_No, Password):
        try:
            self.c.execute("""
                UPDATE DATA
                SET Fname=?, Lname=?, Age=?, Section=?, Contact_No=?, Password=?
                WHERE Roll_no=?
                """, (Fname, Lname, Age, Section, Contact_No, Password, Roll_no))
            self.connection.commit()
            print("Student information updated successfully")
        except sqlite3.Error as e:
            print("Update unsuccessful\n", e)


    def close(self):
        self.connection.close()
        

