# This file contains all the functions required by the main file
######################
import sqlite3


# Adding a new employee to organization database - option 2
def add_employee():
    print("Enter the details of employee")
    print("-----------------------------")
    v_employee_number = int(input(" Enter employee Number: "))
    v_employee_name = input(" Enter employee Name: ")
    v_employee_age = int(input(" Enter employee age: "))
    v_employee_designation = input(" Enter Department (Enter any one of these(Sales,Mkt,Mgmt,Admin): ")
    v_employee_basic_pay = float(input(" Enter employee Basic Pay: "))
    v_travelling_allowance = float(input(" Enter Travelling Allowance: "))
    v_house_rent_allowance = float(input(" Enter House Rent Allowance: "))
    v_comm = float(input(" Enter COMM: "))
    v_overtime = float(input(" Enter Overtime: "))
    v_gross_pay = float(input(" Enter Gross Pay: "))
    v_ftax = float(input(" Enter FTAX: "))
    v_ptax = float(input(" Enter PTAX: "))
    v_cpa = float(input(" Enter CPA: "))
    v_net_pay = float(input(" Enter netPay: "))

    conn = sqlite3.connect('main.db')
    c = conn.cursor()

    # Insert a row of data
    c.execute('''INSERT INTO payrolls (enum,ename,age,dept,basicPay,ta,hra,comm,overtime,grossPay,ftax,ptax,cpa,netPay) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
              , (v_employee_number, v_employee_name, v_employee_age, v_employee_designation, v_employee_basic_pay,
                 v_travelling_allowance, v_house_rent_allowance, v_comm, v_overtime, v_gross_pay, v_ftax, v_ptax, v_cpa,
                 v_net_pay))
    # Save (commit) the changes
    conn.commit()
    print("Congratulations!! {0} , you are successfully added to Payroll register >>\n\n")
    input("Press enter to return back to Main Menu ")
    conn.close()
    return


# Listing Records to organization database - option 3
def list_records():
    try:
        conn = sqlite3.connect('main.db')
        c = conn.cursor()
        print("Connected to SQLite")

        c.execute("""SELECT * from payrolls""")  # all the records will be stored in c

        records = c.fetchall()  # to read records from c use fetchall function

        print("Total rows are: ", len(records))
        print("Printing each row")

        for col in records:
            print(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11],
                  col[12], col[13])

        c.close()
    except sqlite3.Error as error:
        print('Failed to read data from sqlite table', error)
    finally:
        if not conn:
            conn.close()
            print("The SQLite connection is closed")

        input("Press any key to go back to main menu ")


# Searching Records in organization database - option 4
def search_rec():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    print("Connected to SQLite")
    employee_no = int(input(' Enter the employee number to search '))

    c.execute("SELECT * from payrolls where enum=" + str(employee_no))  # all the records will be stored in c

    records = c.fetchall()  # to read records from c use fetchall function

    print("Total rows are: ", len(records))
    print("Printing each row")

    for col in records:
        print(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9])

    c.close()

    input('Press any key to go back to main menu ')


# Deleting Records from organization database - option 5
def delete_rec():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    print("Connected to SQLite")
    employee_no = int(input(' Enter the Employee number to delete '))

    c.execute("Delete from payrolls where enum=" + str(employee_no))  # The record will be deleted.
    # Save (commit) the changes
    conn.commit()
    conn.close()

    input('Press any key to go back to main menu')
