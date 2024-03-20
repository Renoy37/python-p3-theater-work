from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(String())
    hired = Column(Boolean)
    role_id = Column(Integer(), ForeignKey("roles.id"))

    role = relationship("Role", back_populates="auditions")

    def __repr__(self):
        return f"<Audition(actor='{self.actor}', location='{self.location}', phone={self.phone}, hired={self.hired})>"


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship("Audition", back_populates="role")

    def __repr__(self):
        return f"<Role(character_name='{self.character_name}')>"
