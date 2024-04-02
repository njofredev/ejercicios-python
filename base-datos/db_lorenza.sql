-- LorenzaDB
CREATE TABLE Productos(
	id_producto INT PRIMARY KEY,
	nombre VARCHAR(50),
	descripcion VARCHAR(255),
	precio_costo INT,
	precio_venta INT,
	categoria VARCHAR(50),
	peso FLOAT,
	imagen BYTEA
);

CREATE TABLE Clientes(
	id_cliente INT PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	rut VARCHAR(50),
	direccion VARCHAR(100),
	telefono INT,
	correo VARCHAR(50)
);

CREATE TABLE Proveedores(
	id_proveedor INT PRIMARY KEY,
	nombre VARCHAR(50),
	rut VARCHAR(50)
);

CREATE TABLE Ventas(
	id_venta INT PRIMARY KEY,
	id_cliente INT,
	total INT,
	fecha_emision DATE,
	plazo_factura DATE,
	FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Detalle_ventas(
	id_detalle_venta INT PRIMARY KEY,
	id_venta INT,
	id_producto INT,
	cantidad INT,
	precio_unidad INT,
	descripcion VARCHAR(100),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Compras(
    id_compra INT PRIMARY KEY,
    id_proveedor INT,
    total INT,
    fecha_compra DATE,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

CREATE TABLE Detalle_compras(
    id_detalle_compra INT PRIMARY KEY,
    id_compra INT,
    cantidad INT,
    precio_compra INT,
    detalle VARCHAR(255),
    id_producto INT,
    FOREIGN KEY (id_compra) REFERENCES Compras(id_compra),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Inventario(
    id_inventario INT PRIMARY KEY,
    id_producto INT,
    stock_inicial INT,
    stock_final INT,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Detalle_inventario(
    id_detalle_inventario INT PRIMARY KEY,
    id_producto INT,
    id_venta INT,
    id_compra INT,
    fecha_vencimiento INT,
    cantidad INT,
    tipo_movimiento VARCHAR(50),
    lote INT,
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_compra) REFERENCES Compras(id_compra)
);