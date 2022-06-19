

CREATE TABLE usuarios(
    id serial PRIMARY KEY, 
    nombre varchar(100), 
    apellidos varchar(255),
    email varchar(255), 
    password varchar(255) not null, 
    fecha date not null, 
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
    id serial PRIMARY KEY, 
    usuario_id serial not null,
    titulo varchar(255) not null, 
    descripcion text, 
    fecha date not null, 
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)