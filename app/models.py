# app/models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///./petsandpals.db")

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    pets = relationship("Pet", back_populates="owner")

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    owner = relationship("Owner", back_populates="pets")

class FeedingTraining(Base):
    __tablename__ = 'feeding'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class VetVisits(Base):
    __tablename__ = 'vet_visits'
    id = Column(Integer, primary_key=True)
    visit_date = Column(DateTime, nullable=False)
    vet_id = Column(Integer, ForeignKey('vets.id'))
    vet = relationship("Vets", back_populates="visits")

class Vets(Base):
    __tablename__ = 'vets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    visits = relationship("VetVisits", back_populates="vet")
