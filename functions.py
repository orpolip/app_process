import psycopg2
import sys


def menu_handler():
    print(" 1 - First and last name of the mentors", "\n", "2 - Nickname of the mentors from Miskolc",
          "\n", "3 - Carol's full name and phone", "\n", "4 - Mysterious girl's full name and phone",
          "\n", "5 - Markus Schaffarzyk new applicant", "\n", "6 - Jemima Foreman' phone update", "\n",
          "7 - Delete Arsenio + 1", "\n", "0 - exit")
    user_input = input(str("Enter a number: "))
    if user_input == "1":
        return query1()
    elif user_input == "2":
        return query2()
    elif user_input == "3":
        return query3()
    elif user_input == "4":
        return query4()
    elif user_input == "5":
        return query5()
    elif user_input == "6":
        return query6()
    elif user_input == "7":
        return query7()
    elif user_input == "0":
        return SystemExit


def connect_route():
    conn = psycopg2.connect("dbname='galdonyi' user='galdonyi' host='localhost' password='orrpolip1'")
    conn.autocommit = True
    return conn


def query1():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query2():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query3():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT CONCAT(first_name,last_name),phone_number FROM applicants WHERE first_name='Carol';""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query4():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT CONCAT(first_name,last_name),phone_number 
    FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query5():
    cursor = connect_route().cursor()
    # cursor.execute("""INSERT INTO applicants (id,first_name, last_name, phone_number, email, application_code)
    # VALUES (11,'Markus','Schaffarzyk','003620/725-2666', 'djnovus@groovecoverage.com',54823);""")
    cursor.execute("""SELECT * FROM applicants WHERE application_code=54823;""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query6():
    cursor = connect_route().cursor()
    cursor.execute("""UPDATE applicants SET phone_number = '003670/223-7459' WHERE last_name='Foreman';""")
    cursor.execute("""SELECT phone_number FROM applicants WHERE CONCAT(first_name,last_name)='JemimaForeman';""")
    rows = cursor.fetchall()
    print("\n", rows, "\n")
    return menu_handler()


def query7():
    cursor = connect_route().cursor()
    cursor.execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""")
    return menu_handler()
