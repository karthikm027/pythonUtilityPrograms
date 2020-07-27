#Python program to generate and store passwords of desired length
#The datatbase has to be created and the password has to be specified
# ----------------------------------------------------------------- 
# | purpose varchar(20)| username varchar(20)| passwrd varchar(50)|
#------------------------------------------------------------------
import mysql.connector
import secrets

pas= input("Enter the passwrd of your database\n")  #Your database password

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pas,
        database="password_manager"  #your database name
        )
except mysql.Error as e:
    flag=1
    msg = ('Failure in executing query. re-run the program')
    raise DatabaseError(msg) 


def generate_password(l):     #This function generates random characters of specified length 
    s=l//2
    return secrets.token_hex(s)

def add_to_db(purpose,un,generated_password):  #This function is used to add data to the mySQL db
    #mycursor= mydb.cursor()
    query= "INSERT INTO password(purpose,username,passwrd) VALUES(%s,%s,%s)"
    args= (purpose,un,generated_password)
    try:
        mycursor= mydb.cursor()
        mycursor.execute(query,args)
        mydb.commit()
        print("success")
    except Error as e:
        print(e)
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

def fetch():                        #This function displays all the entries of the table
    #mycursor= mydb.cursor()
    try:
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM password")
        result= mycursor.fetchall()
        for row in result:
            print("purpose : ",row[0])
            print("username: ",row[1])
            print("passwrd : ",row[2])
            print("-"*20)
    except Error as p:
        print(p)
    finally:
        if (mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

print("Enter your choice: ")
print("1--> To generate new password.")
print("2--> To access all the paswords.")
choice= int(input())

if choice==1:
    print("Enter the site for which you require password.")
    purpose= input()
    print("Enter the length you require.")
    length= int(input())
    generated_password= generate_password(length)
    print(generated_password)
    print("Enter your username for this site to store into db")
    un= input()
    add_to_db(purpose,un,generated_password)
elif choice==2:
    print("Password---->.")
    fetch()
else:
    print("Inavlid choice! re-run the program")
print("-----Thank you-----")







