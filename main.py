# Employee Registeration system using python and sqlite3
import sqlite3
import modules

# Run the code once and the comment out
def db_table_create():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
        #Create table
    c.execute('''CREATE TABLE payrolls
                #   (enum integer, ename text, age integer, dept text, basicPay real,
                # ta real,hra real,comm real,overtime real,grossPay real,ftax real,
                #  ptax real,cpa real,netPay real)
                ''')

# Printing the Main Menu
def main():
    while True:
        print("\n" * 30)
        print(" M A I N  M E N U ")
        print("---------------------------------")
        print(" ")
        print("1. Create Database and Table ")
        print("2. New Employee Registration ")
        print("3. List Records")
        print("4. Search Records")
        print("5. Delete Records")
        print("9. EXIT ")
        print(" ")
        print("If you running the app for the first time select option 1 then proceed with other options")
        choice = int(input(" Enter your menu option (1/2/3/4/5) Enter 9 to exit: "))
        if choice == 2:
            modules.add_employee()  # Adding Employees
        elif choice == 1:
            db_table_create()
        elif choice == 3:
            modules.list_records()  # Listing Records
        elif choice == 4:
            modules.search_rec()  # Searching Records
        elif choice == 5:
            modules.delete_rec()  # Deleting Records
        # Exiting the program
        elif choice == 9:
            break
        else:
            print("Sorry wrong choice try again")  # Prompt for wrong Input


if __name__ == "__main__":
    main()
