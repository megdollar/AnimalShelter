# help with mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

# use for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# create foreign key relationships, use for mapper
from sqlalchemy.orm import relationship

# use in configuration code at end of file
from sqlalchemy import create_engine

# make instance of declarative_base class, 
# lets SQL know the classes are SQLAlchemy 
# classes that correspond to tables in DB
Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)

class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))

#create instance of create_engine class 
#point to DB we use
engine = create_engine('sqlite:///puppyshelter.db')

#goes into DB and adds classes as new tables in DB
Base.metadata.create_all(engine)






