import mysql.connector


class gestordb:

    def __init__(self, host, usuario, clave, puerto):
        try:
            mydb = mysql.connector.connect(
                host=host, user=usuario, password=clave, port=puerto
            )
            cursor = mydb.cursor()
            cursor.execute("show databases")
            for db in cursor:
                print(db)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
