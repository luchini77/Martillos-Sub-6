import sqlite3


class CrearTablas:

    # CON EL CONSTRUCTOR SE CONECTA A LA BBDD, Y SE CREAN LAS DIFERENTES TABLAS
    def __init__(self):
        self.bd = sqlite3.connect('sub-6.db')
        self.cursor = self.bd.cursor()

        self.creando_tabla_martillo()
        self.creando_tabla_camara1()
        self.creando_tabla_camara2()

    # CREAR TABLA MARTILLO
    def creando_tabla_martillo(self):

        tablas = [
            """
                CREATE TABLE IF NOT EXISTS martillo(
                    ubicacion_martillo TEXT NOT NULL PRIMARY KEY UNIQUE,
                    numero_martillo TEXT,
                    firmware TEXT,
                    ip_martillo TEXT NOT NULL UNIQUE,
                    power_plc TEXT,
                    cpu TEXT
                );
            """
        ]
        try:
            for tabla in tablas:
                self.cursor.execute(tabla)
                print('Tabla Martillo creada correctamente')
        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

    # CREAR TABLA CAMARA 1

    def creando_tabla_camara1(self):

        tablas = [
            """
                CREATE TABLE IF NOT EXISTS camara1(
                    ip_camara1 TEXT NOT NULL PRIMARY KEY UNIQUE,
                    modelo_cam1 TEXT,
                    usuario1 TEXT,
                    pass1 TEXT,
                    u_mart1 TEXT,
                    FOREIGN KEY ('u_mart1') REFERENCES martillo('ubicacion_martillo')
                    );
            """
        ]
        try:
            for tabla in tablas:
                self.cursor.execute(tabla)
                print('Tabla Camara 1 creada correctamente')
        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)

    # CREAR TABLA CAMARA 2
    """def __init__(self):
        self.bd = sqlite3.connect('sub-6.db')
        self.cursor = self.bd.cursor()

        self.creando_tabla_camara2()"""

    def creando_tabla_camara2(self):

        tablas = [
            """
                CREATE TABLE IF NOT EXISTS camara2(
                    ip_camara2 TEXT NOT NULL PRIMARY KEY UNIQUE,
                    modelo_cam2 TEXT,
                    usuario2 TEXT,
                    pass2 TEXT,
                    u_mart2 TEXT,
                    FOREIGN KEY ('u_mart2') REFERENCES martillo('ubicacion_martillo')
                    );
            """
        ]
        try:
            for tabla in tablas:
                self.cursor.execute(tabla)
                print('Tabla Camara 2 creada correctamente')
        except sqlite3.OperationalError as error:
            print('Error al abrir:', error)



if __name__ == '__main__':
    CrearTablas()
