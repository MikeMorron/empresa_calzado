-- Crear la base de datos
CREATE DATABASE gestion_calzado;

-- Usar la base de datos
USE gestion_calzado;

-- Crear la tabla Usuarios
CREATE TABLE Usuario (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Rol ENUM('Cortador', 'Guarnecedor', 'Encargado de ensamblar'),
    Salario DECIMAL(10, 2),
    FechaContrato DATETIME
);

-- Crear la tabla Produccion
CREATE TABLE Produccion (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Cant_Product INT,
    Fecha DATETIME,
    Precio DECIMAL(10, 2)
);

-- Crear la tabla Etiqueta
CREATE TABLE Etiqueta (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NombreProd VARCHAR(50),
    Fecha DATETIME,
    Precio DECIMAL(10, 2)
);

-- Crear la tabla Producto
CREATE TABLE Producto (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NombreProducto VARCHAR(50),
    NumeroProducto INT
);

-- Crear la tabla Pagos
CREATE TABLE Pagos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FechaPaquete DATETIME,
    CantidadProductos INT,
    TotalPagar DECIMAL(10, 2),
    PeriodoPagos VARCHAR(10),
    Id_Usuario INT,
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(ID)
);
