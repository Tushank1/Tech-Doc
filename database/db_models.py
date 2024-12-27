from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Users Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)  
    mobile_no = Column(Integer, nullable=False) 
    
    # Relationships
    address = relationship("Address", back_populates="user", uselist=False)
    contact = relationship("Contact", back_populates="user", uselist=False)

# Address Table
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    street_address = Column(String, nullable=False)
    landmark = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pincode = Column(Integer, nullable=False)

    # Relationship
    user = relationship("User", back_populates="address")

# Contact Table
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)

    # Relationship
    user = relationship("User", back_populates="contact")
