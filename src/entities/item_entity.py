from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src.config.env_config import DB_TABLE_NAME

Base = declarative_base()

class Item(Base):
    __tablename__ = DB_TABLE_NAME

    IdTienda = Column(Integer, primary_key=True) #StoreNo
    IdTiempo = Column(Integer, primary_key=True) #CreationDate (esta en datetime)
    IdEncuesta = Column(String(120)) #Code
    NPS = Column(Integer)
    Limpieza = Column(Integer)
    InfoPrecioPromo = Column(Integer)
    TiempoEspera = Column(Integer)
    Amabilidad = Column(Integer)
    ProductosOfrecidos = Column(Integer)
    PromocionesOfrecidas = Column(Integer)
    ProductoDelMes = Column(String(50)) #en la tabla dice INT
    DNI = Column(String(50))
    Edad = Column(Integer)

