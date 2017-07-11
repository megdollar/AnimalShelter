# 1. Query all of the puppies and return the results in ascending alphabetical order
# 2. Query all of the puppies that are less than 6 months old organized by the youngest first
# 3. Query all puppies by ascending weight
# 4. Query all puppies grouped by the shelter in which they are staying

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
import datetime


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

def alphabeticalPuppies(): 
	puppies = session.query(Puppy.name, Puppy.gender).order_by(Puppy.name).all()
	for puppy in puppies:
    		print "\n"
    		print ("Name: {:^5} |  Gender: {:^5}" .format(puppy[0], puppy[1]))

def youngestPuppies():
	sixMonth = datetime.date.today() - datetime.timedelta(6*365/12)
	puppies = session.query(Puppy.name, Puppy.dateOfBirth).filter(Puppy.dateOfBirth >= sixMonth).order_by(Puppy.dateOfBirth.desc())
	for puppy in puppies:
			print "\n"
			print ("Name: {:^5} |  DOB: {}" .format(puppy[0], puppy[1]))

def pupsByWeight():
	puppies = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight).all()
	for puppy in puppies:
			print "\n"
			print ("Name: {:^5} |  Weight: {}" .format(puppy[0], puppy[1]))

def pupsByShelter():
	puppies = session.query(Puppy).join(Shelter).order_by(Puppy.shelter_id.asc(), Puppy.name)
	for puppy in puppies:
			print "\n"
			print ("Name: {:^5} |  Shelter: {:^5}" .format(puppy.name, puppy.shelter.name))

alphabeticalPuppies()
youngestPuppies()
pupsByWeight()
pupsByShelter()