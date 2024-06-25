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

![alt text](<Img/DBeaver BD.PNG>)

También se adjunta la creación del esquema y la tabla en el archivo Creacion_BD_tabla.sql

Para generar el archivo requeriments.txt usamos el siguiente comando:
    
    pip freeze > requirements.txt

Finalmente, al intentar dockerizar la API, uso el siguiente comando:

    docker build -t fastapimovie .

Aparece el siguiente mensaje de error:

    #9 6.400   Preparing metadata (setup.py): started
    #9 6.975   Preparing metadata (setup.py): finished with status 'error'
    #9 7.007   error: subprocess-exited-with-error
    #9 7.007
    #9 7.007   × python setup.py egg_info did not run successfully.
    #9 7.007   │ exit code: 1
    #9 7.007   ╰─> [23 lines of output]
    #9 7.007       running egg_info
    #9 7.007       creating /tmp/pip-pip-egg-info-r1qrshgp/psycopg2.egg-info
    #9 7.007       writing /tmp/pip-pip-egg-info-r1qrshgp/psycopg2.egg-info/PKG-INFO
    #9 7.007       writing dependency_links to /tmp/pip-pip-egg-info-r1qrshgp/psycopg2.egg-info/dependency_links.txt      
    #9 7.007       writing top-level names to /tmp/pip-pip-egg-info-r1qrshgp/psycopg2.egg-info/top_level.txt
    #9 7.007       writing manifest file '/tmp/pip-pip-egg-info-r1qrshgp/psycopg2.egg-info/SOURCES.txt'
    #9 7.007
    #9 7.007       Error: pg_config executable not found.
    #9 7.007
    #9 7.007       pg_config is required to build psycopg2 from source.  Please add the directory
    #9 7.007       containing pg_config to the $PATH or specify the full executable path with the
    #9 7.007       option:
    #9 7.007
    #9 7.007           python setup.py build_ext --pg-config /path/to/pg_config build ...
    #9 7.007
    #9 7.007       or with the pg_config option in 'setup.cfg'.
    #9 7.007
    #9 7.007       If you prefer to avoid building psycopg2 from source, please install the PyPI
    #9 7.007       'psycopg2-binary' package instead.
    #9 7.007
    #9 7.007       For further information please check the 'doc/src/install.rst' file (also at
    #9 7.007       <https://www.psycopg.org/docs/install.html>).
    #9 7.007
    #9 7.007       [end of output]
    #9 7.007
    #9 7.007   note: This error originates from a subprocess, and is likely not a problem with pip.
    #9 7.010 error: metadata-generation-failed
    #9 7.010
    #9 7.010 × Encountered error while generating package metadata.
    #9 7.010 ╰─> See above for output.
    #9 7.010
    #9 7.010 note: This is an issue with the package mentioned above, not pip.
    #9 7.010 hint: See above for details.
    #9 7.190
    #9 7.190 [notice] A new release of pip is available: 23.0.1 -> 24.1
    #9 7.190 [notice] To update, run: pip install --upgrade pip


