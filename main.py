import MySQLdb
from Classes.bcolors import bcolors


def insert_table():
    try:
        id = input("Input id : ")
        name = input("   Name  : ")
        value = str(id) + ", \"" + name + "\""
        statement = "insert into students(id,name) values(%s)" % value
        cursor.execute(statement)
        mydb.commit()
    except:
        pass


def show_records():
    print(bcolors.OKBLUE + "======Database records======" + bcolors.ENDC)
    cursor.execute("select * from students")
    data = cursor.fetchall()
    for i in data:
        print("  Id : ", i[0], end="")
        print("     Name : ", i[1])


def delete():
    global x
    x = int(
        input(
            "\n\t\t\t1. Delete Everything\n\t\t\t2. Delete a specific record\n\t\tInput : "))
    if x == 1:
        statement = "delete from students"
        cursor.execute(statement)
        mydb.commit()
        print(bcolors.FAIL + bcolors.BOLD + bcolors.UNDERLINE + "ALL RECORDS HAVE BEEN DELETED" + bcolors.ENDC)
    else:
        id = input("Input id : ")
        val = "select * from students where id=(%s)" % id
        cursor.execute(val)
        data = cursor.fetchone()
        statement = "delete from students where id=(%s)" % id
        cursor.execute(statement)
        mydb.commit()
        print("Data Deleted of id " + bcolors.WARNING + "{0}".format(
            data[0]) + bcolors.ENDC + " and name " + bcolors.FAIL + "{0}".format(data[1]) + bcolors.ENDC.format(data[0],
                                                                                                                data[
                                                                                                                    1]))


def connection():
    global mydb, cursor
    databaseselection = int(input("Select database : \n1. anish\n2. dit"))
    if databaseselection == 1:
        mydb = MySQLdb.connect("localhost", "anish", "toor@123", "anish")
        cursor = mydb.cursor()
        print(bcolors.WARNING + "Database Connected to anish" + bcolors.ENDC)
    if databaseselection == 2:
        mydb = MySQLdb.connect("localhost", "anish", "toor@123", "dit")
        cursor = mydb.cursor()
        print(bcolors.WARNING + "Database Connected to dit" + bcolors.ENDC)


if __name__ == "__main__":
    connection()
    running = True
    while running:
        x = int(
            input(
                "\t\t1. Insert into table\n\t\t2. Show database values\n\t\t3. Delete Records\n\t\t4. Exit\n\tInput : ")
        )
        if x == 1:
            insert_table()
        elif x == 2:
            show_records()
        elif x == 3:
            delete()
        else:
            print(bcolors.FAIL + bcolors.BOLD + "EXITING" + bcolors.ENDC)
            running = False
        print("\n\n\n")
