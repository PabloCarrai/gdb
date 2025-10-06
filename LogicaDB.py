import mysql.connector


class gestordb:

    def prueba_Conectividad(
        self, host="Localhost", usuario="root", clave="", puerto=3306
    ):
        try:
            mydb = mysql.connector.connect(
                host=host, user=usuario, password=clave, port=puerto
            )
            cursor = mydb.cursor()
            return "Prueba de conectividad a la db Exitosa"

        except mysql.connector.Error as err:
            print(f"Error: {err}")
