CREATE DATABASE my_db;

USE my_db;

CREATE TABLE Usuario (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    Rol ENUM('Cortador', 'Guarnecedor', 'ensamblador'),
    Salario DECIMAL(10, 2),
    FechaContrato DATETIME
);

CREATE TABLE Produccion (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Cant_Product INT,
    Fecha DATETIME,
    Precio DECIMAL(10, 2)
);

CREATE TABLE Etiqueta (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NombreProd VARCHAR(50),
    Fecha DATETIME,
    Precio DECIMAL(10, 2)
);

CREATE TABLE Producto (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NombreProducto VARCHAR(50),
    NumeroProducto INT
);

CREATE TABLE Pagos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FechaPaquete DATETIME,
    CantidadProductos INT,
    TotalPagar DECIMAL(10, 2),
    PeriodoPagos VARCHAR(10),
    Id_Usuario INT,
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(ID)
);
