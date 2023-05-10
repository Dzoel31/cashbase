import mysql.connector
import os
from prettytable import from_db_cursor

# Prosedur untuk menjalankan xampp
def connectToDatabase():
    os.system("C:\\xampp\\xampp_start.exe")

# Prosedur untuk memberhentikan xampp
def closeConnection():
    os.system("C:\\xampp\\xampp_stop.exe")

# Prosedur untuk memilih database
def lobby(myCursor):
    os.system("cls")
    print("===SELAMAT DATANG DI PROGRAM DATABASE===")
    myCursor.execute("SHOW DATABASES")
    listDatabase = from_db_cursor(myCursor)

    print(listDatabase)

    choose = input("Pilih database : ")
    myCursor.execute(f"USE {choose}")

# Prosedur untuk berpindah database
def selectDatabase(myCursor):
    os.system("cls")
    myCursor.execute("SHOW DATABASES")
    listDatabase = from_db_cursor(myCursor)

    print(listDatabase)

    choose = input("Pilih database : ")
    myCursor.execute(f"USE {choose}")

# Prosedur untuk menampilkan database yang sedang digunakan
def useDatabase(myConnection):
    print("Database saat ini :", myConnection.database)

# Prosedur untuk menampilkan tabel
def showTable(myConnection, myCursor):
    os.system("cls")
    useDatabase(myConnection)
    myCursor.execute("SHOW TABLES")
    listTable = from_db_cursor(myCursor)

    print(listTable)

# Prosedur untuk menjalankan perintah select
def querySelect(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"SELECT * FROM {table}")
            tableData = from_db_cursor(myCursor)

            print(tableData)
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")

        repeat = input("\nIngin melanjutkan? [Y or Any key/N] : ").lower()

# Prosedur untuk melakukan insert ke dalam database
def queryInsert(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"DESC {table}")
            field = [f[0] for f in myCursor] # Mengambil nama kolom dalam tabel
            value = [] # Menampung value baru

            for i in range(len(field)):
                value.append(input(f"Masukkan {field[i]} : "))
            
            sqlInsertQuery = f"""INSERT INTO {table} VALUES {tuple(value)}"""

            myCursor.execute(sqlInsertQuery)
            
            # Untuk mengecek apakah query berhasil dijalankan atau tidak
            if myCursor.rowcount > 0:
                print(f"Query OK, {myCursor.rowcount} row inserted.")
            else:
                print("Query gagal dieksekusi")
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")

        repeat = input("\nIngin melanjutkan? [Y or Any key/N] : ").lower()

# Prosedur untuk melakukan proses update
def queryUpdate(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))
    
        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"DESC {table}")
            field = [f[0] for f in myCursor]

            myCursor.execute(f"SELECT * FROM {table}")
            tableData = from_db_cursor(myCursor)

            print(tableData)
            
            selectField = input("Pilih field yang akan diupdate : ")
            newValue = input("Masukkan data baru : ")
            selectData = input("Masukkan primary key (kolom pertama): ")

            sqlUpdateQuery = f"""UPDATE {table}
                                SET {selectField} = '{newValue}' 
                                WHERE {field[0]} = '{selectData}'"""
            
            myCursor.execute(sqlUpdateQuery)

            if myCursor.rowcount > 0:
                print(f"Query OK, {myCursor.rowcount} row updated.")
            else:
                print("Query gagal dieksekusi")
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")
        
        repeat = input("\nIngin melanjutkan? [Y or Any key/N] : ").lower()

# Prosedur untuk menjalankan perintah delete
def queryDelete(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")

            myCursor.execute(f"SELECT * FROM {table}")
            tableData = from_db_cursor(myCursor)

            print(tableData)
                
            selectFieldDelete = input("Pilih field yang akan didelete : ")
            dataDelete = input("Masukkan data yang ingin didelete : ")

            sqlDeleteQuery = f"""DELETE FROM {table}
                                WHERE {selectFieldDelete} = '{dataDelete}'""" 

            myCursor.execute(sqlDeleteQuery) 

            if myCursor.rowcount > 0:
                print(f"Query OK, {myCursor.rowcount} row deleted.")
            else:
                print("Query gagal dieksekusi")
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulangi!")

        repeat = input("\nIngin melanjutkan? [Y or Any key/N] : ").lower()           

# Main menu program untuk memilih dan mengeksekusi query yang dipilih
def mainMenu(myConnection, myCursor):
    try :
        while True:
            os.system("cls")
            useDatabase(myConnection)
            print("="*20)
            print("[1] Pilih database")
            print("[2] Query select")
            print("[3] Query insert")
            print("[4] Query update")
            print("[5] Query delete")
            print("[0] Exit")
            print("="*20)

            choose = int(input("Masukkan pilihan : "))
            if choose == 1:
                selectDatabase(myCursor)
            elif choose == 2:
                querySelect(myConnection, myCursor)
            elif choose == 3:
                queryInsert(myConnection, myCursor)
            elif choose == 4:
                queryUpdate(myConnection, myCursor)
            elif choose == 5:
                queryDelete(myConnection, myCursor)
            elif choose == 0:
                break
            else:
                input("Input tidak sesuai!\n Tekan enter untuk lanjut!")
    
    except Exception as error:
        print(f"Terjadi error : {error}")
        input("Enter untuk mengulang!")
        mainMenu(myConnection, myCursor)

# Main program untuk menyambungkan dengan database, menjalankan menu, dan mengakhiri koneksi dengan database
def main():
    connectToDatabase()
    print("Connected to database succesfully!")

    try:
        # Konfigurasi untuk koneksi
        myConnection = mysql.connector.connect(
            user="root",
            password="",
            autocommit = True,
        )

    except mysql.connector.Error as e:
        print(f"Terjadi error pada program : {e}")
    
    myCursor = myConnection.cursor()
    input("Press enter to continue")
    lobby(myCursor)
    mainMenu(myConnection, myCursor)
    closeConnection()
    print("Disconnected succesfully!")
    
main() # Run Program
