CREATE SCHEMA IF NOT EXISTS my_collections AUTHORIZATION postgres;

CREATE TABLE IF NOT EXISTS my_collections.my_movies (
	id serial4 NOT NULL,
	autor varchar NOT NULL,
	descripcion varchar NOT NULL,
	fecha_estreno date NULL,
	CONSTRAINT my_movies_pk PRIMARY KEY (id)
);