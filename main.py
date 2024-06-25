from fastapi import FastAPI, HTTPException, status
from BD.bd_connection import BDConnection
from models.movie_model import movieSchema

app = FastAPI()
conn = BDConnection()

@app.get("/selectTotal")
def consulta_total():
    try:
        rows = []
        for data in conn.read_all():
            dictmovies = {}
            dictmovies["id"] = data[0]
            dictmovies["autor"] = data[1]
            dictmovies["descripcion"] = data[2]
            dictmovies["fecha_estreno"] = data[3]
            rows.append(dictmovies)
    except:
        print("Error con la consulta GET - todas las películas")
    
    return rows


@app.get("/selectById/{id}")
def consulta_id(id:str):
    try:
        dictmovies = {}
        data = conn.read_one(id)
        dictmovies["id"] = data[0]
        dictmovies["autor"] = data[1]
        dictmovies["descripcion"] = data[2]
        dictmovies["fecha_estreno"] = data[3]
        return dictmovies
    except:
        print("Error con la consulta GET - solo 1 película")


@app.post("/create")
def insert(create_data:movieSchema):
    try:
        data = create_data.dict()
        #data.pop("id")
        #print(data)
        conn.create(data)
        return {"message": "Creado correctamente"}
    except Exception as err:
        print(err)
        print("Error al ejecutar el método POST")


@app.delete("/delete/{id}")
def delete(id:str):
    try:
        conn.delete(id)
    except Exception as err:
        print(err)
        print("Error al ejecutar el método DELETE")

    return {"message": "Registro ELIMINADO correctamente..."}


@app.put("/update/{id}")
def update(create_data:movieSchema, id:str):
    try:
        data = create_data.dict()
        data["id"] = id
        conn.update(data)
        return {"message": "Registro ACTUALIZADO correctamente..."}
    except Exception as err:
        print(err)
        print("Error al ejecutar el método PUT")
    
    