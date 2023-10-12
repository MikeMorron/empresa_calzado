from sqlalchemy import create_engine, Column, Integer, String, DateTime, DECIMAL, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(255))
    rol = Column(Enum('Cortador', 'Guarnecedor', 'Encargado de ensamblar'))
    salario = Column(DECIMAL(10, 2))
    fecha_contrato = Column(DateTime)
    
    produccion = relationship('Produccion', back_populates='usuario')
    paquetes = relationship('Paquete', back_populates='usuario')

class Produccion(Base):
    __tablename__ = 'Produccion'
    prod_id = Column(Integer, primary_key=True)
    cantidadprod = Column(Integer)
    fecha = Column(DateTime)
    precio = Column(Integer)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship('Usuario', back_populates='produccion')
    
class Etiqueta(Base):
    __tablename__ = 'Etiqueta'
    Id_etiqueta = Column(Integer, primary_key=True)
    articulo = Column(String(255))
    fecha = Column(DateTime)
    precio_art = Column(Integer)

class Articulo(Base):
    __tablename__ = 'Articulo'
    Id_art = Column(Integer, primary_key=True)
    nombre_art = Column(String(255))
    cantidad = Column(Integer)

class Paquete(Base):
    __tablename__ = 'Paquete'
    id_pago = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    cantidad = Column(Integer)
    periodo_pago = Column(Integer)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'))
    
    usuario = relationship('Usuario', back_populates='paquetes')
