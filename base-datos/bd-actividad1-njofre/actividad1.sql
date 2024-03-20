/*
Actividad n°1 - Lenguaje de consultas a una base de datos Postgresql
njofre

Dado el modelo de relaciones en la actividad, resolver:
1. Recuperar el nombre completo y la dirección de todos los empleados
que trabajan en el departamento de investigación.
2. Regresar todos los nombres de los empleados que tienen dos o más
cargas familiares.
3. Regresar una lista no repetida con todos los números de proyectos
que involucran un empleado de apellido 'Pérez', ya sea como trabajador
o gerente del departamento que controla ese proyecto.
4. Obtener el nombre de departamento y el número de empleados que ganan
más de $500.000.- pesos en ese departamento.
*/

-- Se crea la base de datos

CREATE TABLE Ubicacion_departamento (
    numero INT PRIMARY KEY,
    ubicacion VARCHAR(255),
);

CREATE TABLE Departamento (
    numero INT PRIMARY KEY,
    nombre VARCHAR(20),
    rut_gerente VARCHAR(10),
    ger_f_inic DATE,
    ubicacion INT,
    FOREIGN KEY (ubicacion) REFERENCES Ubicacion_departamento(numero)
);

CREATE TABLE Proyecto (
    numero INT PRIMARY KEY,
    nombre VARCHAR(20),
    ubicacion VARCHAR(255),
    depto_num INT,
    FOREIGN KEY (depto_num) REFERENCES Departamento(numero)
);

CREATE TABLE Empleado(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100),
    primer_apellido VARCHAR(25),
    segundo_apellido VARCHAR(25),
    fecha_nacimiento DATE,
    direccion VARCHAR(30),
    sexo CHAR(1),
    sueldo DECIMAL
);