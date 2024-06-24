# API_Python_FastAPI
Repositorio para el trabajo del curso Despliegue Data API's con Python

Para inicializar la imagen y el contenedor de Postgres ejecutamos las siguientes líneas de comando

    docker pull postgres
    docker run --name mi-postgres -e POSTGRES_PASSWORD=mi-contrasena -p 5432:5432 -d postgres

Usando DBeaver, creo la base de datos my_collections y la tabla my_movies con la siguiente estructura:
    ID
    Autor
    Descripción
    Fecha_estreno

