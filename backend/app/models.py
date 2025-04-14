from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    genero = Column(String(10), nullable=False)
    altura = Column(Float, nullable=False)
    peso_inicial = Column(Float, nullable=False)
    lesiones = Column(String(100), nullable=False)
    objetivo = Column(String(100), nullable=False)
    rol = Column(String(10), nullable=False)

    entrenador_profile = relationship("Entrenador", back_populates="usuario")
    rutinas = relationship("Rutinas", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario {self.id} {self.nombre} {self.email}>"

class Entrenador(Base):
    __tablename__ = 'entrenador'

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    clientes_activos = Column(Integer, nullable=False)

    usuario = relationship("Usuarios", back_populates="entrenador_profile")
    rutinas = relationship("Rutinas", back_populates="entrenador")

    def __repr__(self):
        return f"<Entrenador {self.id} Clientes Activos: {self.clientes_activos}>"

class Rutinas(Base):
    __tablename__ = 'rutinas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    tipo_rutina = Column(String(100), nullable=False)
    series = Column(Integer, nullable=False)
    repeticiones = Column(Integer, nullable=False)
    categoria = Column(String(100), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    entrenador_id = Column(Integer, ForeignKey('entrenador.id'))

    usuario = relationship("Usuarios", back_populates="rutinas")
    entrenador = relationship("Entrenador", back_populates="rutinas")
    ejercicios = relationship("RutinaEjercicio", back_populates="rutina")

    def __repr__(self):
        return f"<Rutina {self.id} {self.nombre}>"

class Ejercicios(Base):
    __tablename__ = 'ejercicios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    dificultad = Column(String(100), nullable=False)

    rutinas = relationship("RutinaEjercicio", back_populates="ejercicio")

    def __repr__(self):
        return f"<Ejercicio {self.id} {self.nombre}>"

class RutinaEjercicio(Base):
    __tablename__ = 'rutina_ejercicio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rutina_id = Column(Integer, ForeignKey('rutinas.id'), nullable=False)
    ejercicio_id = Column(Integer, ForeignKey('ejercicios.id'), nullable=False)

    rutina = relationship("Rutinas", back_populates="ejercicios")
    ejercicio = relationship("Ejercicios", back_populates="rutinas")

    def __repr__(self):
        return f"<RutinaEjercicio {self.id} Rutina: {self.rutina_id} Ejercicio: {self.ejercicio_id}>"