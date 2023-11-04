from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftablets = StringVar()
        self.bloodpressure = StringVar()
        self.PatientId = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        Labeltitle = Label(self.root, bd=10, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="green", bg="skyblue", font=("times new roman", 30, "bold"))
        Labeltitle.pack(side="top", fill="x")

        # ------------dataframe------------------
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=65, width=1280, height=300)

        DataframeLeft = LabelFrame(Dataframe, bd=5, padx=10, relief=RIDGE, font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=800, height=250)

        DataframeRight = LabelFrame(Dataframe, bd=5, padx=10, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=800, y=5, width=440, height=250)

        # --------------------buttons frame-----------------------------
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=370, width=1280, height=70)

        # ---------------------details frame-----------------------------
        detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        detailsframe.place(x=0, y=440, width=1280, height=200)

        # Patient Id
        lblPatientId = Label(DataframeLeft, font=("arial", 10, "bold"), text="Patient Id:")
        lblPatientId.grid(row=0, column=0, sticky=W, padx=2, pady=6)
        txtPatientId = Entry(DataframeLeft, font=("arial", 10, "bold"), textvariable=self.PatientId, width=20)
        txtPatientId.grid(row=0, column=1, padx=2, pady=6)

        # Patient Name
        lblPatientName = Label(DataframeLeft, font=("arial", 10, "bold"), text="Patient Name:")
        lblPatientName.grid(row=1, column=0, sticky=W, padx=2, pady=6)
        txtPatientName = Entry(DataframeLeft, font=("arial", 10, "bold"), textvariable=self.PatientName, width=20)
        txtPatientName.grid(row=1, column=1, padx=2, pady=6)

        # Date of Birth
        lblDateOfBirth = Label(DataframeLeft, font=("arial", 10, "bold"), text="Date Of Birth:")
        lblDateOfBirth.grid(row=2, column=0, sticky=W, padx=2, pady=6)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 10, "bold"), textvariable=self.DateOfBirth, width=20)
        txtDateOfBirth.grid(row=2, column=1, padx=2, pady=6)

        # Patient Address
        lblPatientAddress = Label(DataframeLeft, font=("arial", 10, "bold"), text="Patient Address:")
        lblPatientAddress.grid(row=3, column=0, sticky=W, padx=2, pady=6)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 10, "bold"), textvariable=self.PatientAddress, width=20)
        txtPatientAddress.grid(row=3, column=1, padx=2, pady=6)

        # Blood Pressure
        lblBloodPressure = Label(DataframeLeft, font=("arial", 10, "bold"), text="Blood Pressure:")
        lblBloodPressure.grid(row=4, column=0, sticky=W, padx=2, pady=6)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 10, "bold"), textvariable=self.bloodpressure, width=20)
        txtBloodPressure.grid(row=4, column=1, padx=2, pady=6)

        # Name of tablet
        lblNameTablet = Label(DataframeLeft, text="Name of tablet", font=("arial", 10, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=5, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("arial", 10, "bold"), width=20)
        comNametablet["values"] = ("Amifostine", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=5, column=1, padx=2, pady=6)

        # ---------------------------------dataframe right---------------------------
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=44, height=10.5, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ---------------------------------buttons------------------------------------
        btnPrescription = Button(Buttonframe,command=self.iPrescription, text='Prescription', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescriptionData, text='Prescription Data', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data, text='Update', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,command=self.idelete, text='Delete', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command=self.clear, text='Clear', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.iExit, text='Exit', bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=0, padx=2, pady=0)
        btnExit.grid(row=0, column=5)

        # -----------------------------------table------------------------------------
        # ----------------------------scroll bar-------------------------------------
        scroll_x = ttk.Scrollbar(detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(detailsframe, column=("PatientId", "pname", "dob", "address", "bloodpressure", "nameoftablets"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("PatientId", text="Patient ID")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")
        self.hospital_table.heading("bloodpressure", text="Blood Pressure")
        self.hospital_table.heading("nameoftablets", text="Name of Tablets")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("PatientId", width=50)
        self.hospital_table.column("pname", width=150)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=250)
        self.hospital_table.column("bloodpressure", width=100)
        self.hospital_table.column("nameoftablets", width=150)
        self.hospital_table.pack(fill="both", expand=1)
        self.fatch_data()
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

    # -------------------------------functionality description--------------------------
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.PatientName.get() == "":
            messagebox.showerror("Error", "Name of tablet and Patient Name are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
                my_cursor = conn.cursor()

                query = "INSERT INTO hospital (PatientId,patient_name, DOB, patientaddress, blood_pressure, name_of_tablet) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (self.PatientId.get(), self.PatientName.get(), self.DateOfBirth.get(), self.PatientAddress.get(), self.bloodpressure.get(), self.Nameoftablets.get())

                my_cursor.execute(query, values)
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")

            except mysql.connector.Error as err:
                print("MySQL Error: ", err)
                messagebox.showerror("Error", "An error occurred while inserting the record.")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def update_data(self):
        if self.Nameoftablets.get() == "" or self.PatientName.get() == "":
            messagebox.showerror("Error", "Name of tablet and Patient Name are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
                my_cursor = conn.cursor()

                query = "UPDATE hospital SET patient_name=%s, DOB=%s, patientaddress=%s, blood_pressure=%s, name_of_tablet=%s WHERE PatientId=%s"
                values = (self.PatientName.get(), self.DateOfBirth.get(), self.PatientAddress.get(), self.bloodpressure.get(), self.Nameoftablets.get(), self.PatientId.get())

                my_cursor.execute(query, values)
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been updated")

            except mysql.connector.Error as err:
                print("MySQL Error: ", err)
                messagebox.showerror("Error", "An error occurred while updating the record.")

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        self.PatientId.set(row[0])
        self.PatientName.set(row[1])
        self.DateOfBirth.set(row[2])
        self.PatientAddress.set(row[3])
        self.bloodpressure.set(row[4])
        self.Nameoftablets.set(row[5])
    


    def iPrescription(self):
        self.txtPrescription.insert(END, "Patient Id:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient address:\t\t\t" + self.PatientAddress.get() + "\n")
        self.txtPrescription.insert(END, "Blood pressure:\t\t\t" + self.bloodpressure.get() + "\n")
        self.txtPrescription.insert(END, "Name of tablet:\t\t\t" + self.Nameoftablets.get() + "\n")

    def idelete(self):
       conn = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
       my_cursor = conn.cursor()
    
       # Assuming "pname" is the field containing the patient's name
       query = "DELETE FROM hospital WHERE patient_name = %s"
       value = (self.PatientName.get(),)
    
       my_cursor.execute(query, value)
       conn.commit()
       conn.close()
    
       self.fatch_data()
       messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.PatientId.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.bloodpressure.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
       iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
       if iExit:
          root.destroy()
   
    

root = Tk()
my_gui = Hospital(root)
root.mainloop()
