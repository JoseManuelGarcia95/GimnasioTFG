CREATE TABLE IF NO EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    genero VARCHAR(10) NOT NULL,
    altura FLOAT NOT NULL,
    peso_inicial FLOAT NOT NULL,
    lesiones VARCHAR(100) NOT NULL,
    objetivo VARCHAR(100) NOT NULL,
    rol VARCHAR(10) NOT NULL
);

CREATE TABLE IF NO EXISTS entrenador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clientes_activos INT NOT NULL,
    FOREIGN KEY (id) REFERENCES usuarios(id)
    FOREIGN KEY (Id) REFERENCES rutinas (id)
); 

CREATE TABLE IF NO EXISTS rutinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo_rutina VARCHAR(100) NOT NULL,
    series INT NOT NULL,
    repeticiones INT NOT NULL,
    categoria VARCHAR(100) NOT NULL,
);

CREATE TABLE IF NO EXISTS ejercicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    dificultad VARCHAR(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES rutinas(id)
);

CREATE TABLE IF NO EXISTS rutina_ejercicio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES rutinas(id),
    FOREIGN KEY (id) REFERENCES ejercicios(id)
);

INSERT INTO usuarios (nombre, apellidos, fecha_nacimiento, email, password, genero, altura, peso_inicial, lesiones, objetivo, rol)
VALUES ('admin', 'admin', '01/01/2000', 'admin@ejemplo.com', '123456', 'Masculino', 1.80, 80, 'Ninguna', 'Administrar', 'Administrador');

INSERT INTO usuarios (nombre, apellidos, fecha_nacimiento, email, password, genero, altura, peso_inicial, lesiones, objetivo, rol)
VALUES ('Carmen', 'Perez', '18/10/1998', 'carmen@ejemplo.com', '123456', 'Femenino', 1.60, 60, 'Ninguna', 'Perder peso', 'Cliente');

INSERT INTO usuarios (nombre, apellidos, fecha_nacimiento, email, password, genero, altura, peso_inicial, lesiones, objetivo, rol)
VALUES ('David', 'García', '15/03/1988', 'davidentrenador@ejemplo.com' '123456', 'Masculino', 1.80, 80, 'Ninguna', 'Hacer mejor la vida de los demás', 'Entrenador');
