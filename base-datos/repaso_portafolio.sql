CREATE TABLE Empleados (
	ID_empleado INT PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	salario INT
);

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(1, 'Matias', 'Cataldo', 1000000),
(2, 'Rodrigo', 'Jara', 5000000),
(3, 'Rodrigo', 'Diaz', 7000000),
(4, 'Camila', 'Herrera', 8500000),
(5, 'Claudia', 'Martinez', 9000000),
(6, 'Jannet', 'Prado', 5000000)

UPDATE Empleados SET salario = 480000 WHERE ID_empleado = 5;

DELETE FROM Empleados WHERE ID_empleado = 1;

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(7, 'Nicolas', 'Jofre', 480000),
(8, 'Florencia', 'Mellado', 180000)

CREATE SEQUENCE seq_empleados START WITH 9 INCREMENT BY 1;

INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(NEXTVAL('seq_empleados'), 'Sebastian', 'Lobos', 2500000);


INSERT INTO Empleados (ID_empleado, nombre, apellido, salario) VALUES
(NEXTVAL('seq_empleados'), 'Alberto', 'Robles', 1300000),
(NEXTVAL('seq_empleados'), 'Jorge', 'Rueger', 1500000),
(NEXTVAL('seq_empleados'), 'Catalina', 'Ruiz', 1500000),
(NEXTVAL('seq_empleados'), 'Ada', 'Ramirez', 1300000);

CREATE TABLE Departamento (
	ID_departamento INT PRIMARY KEY,
	nombre VARCHAR(50),
	ID_empleado INT,
	FOREIGN KEY (ID_empleado) REFERENCES Empleados(ID_empleado)
);


