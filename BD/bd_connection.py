import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'mi-contrasena',
    'host': 'localhost',
    'port': '5432',
}

class BDConnection():
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg2.connect(**db_params)
            print("Conectado a la BD...")
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.close()

    
    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT * FROM my_collections.my_movies
                        """)
            data = cur.fetchall()
            return data
        

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT * FROM my_collections.my_movies WHERE id = %s
                        """, (id,))
            data = cur.fetchone()
            return data

    def create(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO my_collections.my_movies (autor, descripcion, fecha_estreno) 
                VALUES (%(autor)s, %(descripcion)s, %(fecha_estreno)s)
            """, data)
        self.conn.commit()


    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                        DELETE FROM my_collections.my_movies WHERE id = %s
                        """, (id,))
            self.conn.commit()
    

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                        UPDATE my_collections.my_movies SET 
                        autor = %(autor)s, 
                        descripcion = %(descripcion)s,
                        fecha_estreno = %(fecha_estreno)s 
                        WHERE id = %(id)s
                        """, data)
            self.conn.commit()


    def __def__(self):
        self.conn.close()