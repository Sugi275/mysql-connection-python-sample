import mysql.connector
import time
import datetime
import sys

# コネクションの作成
def getConnection(mysqlHost):
    connection = mysql.connector.connect(
        host=mysqlHost,
        port='3306',
        user='admin',
        password='yourpassword',
        database='yourdatabase',
        connection_timeout=10
    )

    return connection

def selectLoop(connection):
    cursor = connection.cursor()
    
    for i in range(1000):
        print("================" + str(i) + "回目のループ ==============")
        dt_now = datetime.datetime.now()
        print(dt_now)
        cursor.execute("SELECT * FROM sample;")
        rows = cursor.fetchall()
        print(rows[0])
        print("   ")
        time.sleep(1)


def main(mysqlHost):
    while True:
        try:
            connection = getConnection(mysqlHost)
            selectLoop(connection)
        except mysql.connector.errors.InterfaceError as e:
            dt_now = datetime.datetime.now()
            print(dt_now)
            print("InterfaceError")
            print(e)
            time.sleep(1)
        except mysql.connector.errors.OperationalError as e:
            dt_now = datetime.datetime.now()
            print(dt_now)
            print("OperationalError")
            print(e)
            time.sleep(1)
        except:
            print("General Error")
            raise

if __name__ == "__main__":
    print("Start!")
    args = sys.argv
    mysqlHost = args[1]
    main(mysqlHost)
    print("Finish!")