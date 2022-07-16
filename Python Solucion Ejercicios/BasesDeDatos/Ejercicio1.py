import sqlite3


conn = sqlite3.connect('database.db')

def createTable():
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Alumnos")
    cursor.execute('''CREATE TABLE Alumnos(id INT PRIMARY KEY NOT NULL, name TEXT, apellido TEXT)''')
    cursor.close()

def addData():
    cursor = conn.cursor()
    alumnos = [
        (1, 'Daniel', 'Villada'),
        (2, 'Santiago', 'Guerrero'),
        (3, 'Dairo', 'Cardona'),
        (4, 'Miguel', 'Correa'),
        (5, 'Veronica', 'Piedrahita'),
        (6, 'Samantha', 'Villada'),
        (7, 'Jhosep', 'Smith'),
        (8, 'Will', 'Rex'),
    ]
    cursor.executemany("INSERT INTO Alumnos VALUES(?,?,?)", alumnos)
    conn.commit()
    cursor.close()

def searchAlumno():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alumnos WHERE name = 'Samantha'")
    rows = cursor.fetchone()
    print(rows)
    cursor.close()

createTable()
addData()
searchAlumno()

endConn = conn.close()
