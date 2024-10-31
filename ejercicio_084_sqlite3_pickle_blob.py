import sqlite3
import pickle

# 1. Abrir la conexión (se abre con un nombre de fichero)
# 10. Cerrar la conexión
class Pelicula:
    def __init__(self, id, titulo, duracion):
        self.id = id
        self.titulo = titulo
        self.duracion = duracion

    def __str__(self):
        return f'ID:{self.id}. Título:{self.titulo}. Duración:{self.duracion}'
    
    def __repr__(self) -> str:
        return self.__str__()

class DBManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = sqlite3.connect(file_name)
        self.__create_model()

    def __create_model(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS peliculas 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       pelicula BLOB NOT NULL)""")
        cursor.close()

        #CRUD(C)-CREATE
    
    #CRUD(C)-CREATE
    def insert_movie(self, movie):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO peliculas (pelicula) VALUES (?)",(movie,))
        self.connection.commit()
        cursor.close()  

    #CRUD(R)-READ
    def get_movie(self, id):
        cursor = self.connection.cursor()
        registro = cursor.execute("SELECT * FROM peliculas WHERE id=?",
                                  (id,)).fetchone()
        pelicula = pickle.loads(registro[1])
        cursor.close()
        return pelicula
    
    #CRUD(R)-READ
    def get_movies(self):
        cursor = self.connection.cursor()
        registros = cursor.execute("SELECT * FROM peliculas").fetchall()
        peliculas = []
        for registro in registros:
            peliculas.append(pickle.loads(registro[1]))
        cursor.close()
        return peliculas
    
    def __del__(self):
        self.connection.close()
     

DB_NAME = "movies_binary.db"

db_manager = DBManager(DB_NAME)
#pelicula = Pelicula(id=0, titulo='Memorias de África', duracion=95)
#db_manager.insert_movie(pickle.dumps(pelicula))
#pelicula = db_manager.get_movie(1)
#print(pelicula)
peliculas = db_manager.get_movies()
for pelicula in peliculas:
    print(pelicula)
