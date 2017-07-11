# Animal Shelter

### About the Animal Shelter Database:
Built as part of the [Udacity's Full Stack Nanodegree](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/079be127-2d22-4c62-91a8-aa031e760eb0) this is a database I created using python SQLAlchemy. The python file puppies.py is the model for this database. This code  creates a SQLite file called puppies.db. Then the file puppypopulator.py populates the database and queries are performed on the data in queries.py

### Getting Set Up:

#### System Requirements:
1. [Python3](https://www.python.org/)
2. [Vagrant](https://www.vagrantup.com/)
  * This is the software that configures the Virtual machine
3. [Virtual Box](https://www.virtualbox.org/)
  * This is the software that actually runs the virtual machine
  * Allows you to share files between the VM filesystem and your host computer
  * Install the platform package for your OS
  * Don't launch after installing, Vagrant handles this for you

#### Project Setup:
1. Install Python3 
2. Install Vagrant
3. Install Virtual Box
4. Download or clone this repository and place it in the vagrant directory

#### Launch the VM:
1. Inside the Vagrant directory downloaded from the full-stack-nanodegree-vm run this command in your terminal
   `vagrant up`
2. Log in to the VM 
   `vagrant ssh`
3. Change directory to the files and look around
   `cd /vagrant' 'ls' `
   
#### Set Up the Database:
1. Load the data in the local database
   `python puppies.py`
2. Populate the database
   `python puppypopulator.py `
  
#### Run the Queries:
1. From the vagrant direcotry inside the VM
   `python queries.py`

### About the Data:
There are two tables in the data:
* The Shelter table contains information about the shelters (name, id, address).
* The Puppy table contains the adoptable puppies (name, DOB, weight, id, shelter location, gender, picture).

### About the Queries:
1. Query all of the puppies and return the results in ascending alphabetical order
   ```
   session.query(Puppy.name, Puppy.gender).order_by(Puppy.name).all()
   ```
2. Query all of the puppies that are less than 6 months old organized by the youngest first
   ```
   session.query(Puppy.name, Puppy.dateOfBirth).filter(Puppy.dateOfBirth >= sixMonth).order_by(Puppy.dateOfBirth.desc())
   ``` 
3. Query all puppies by ascending weight
   ```
   session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight).all()
   ```
4. Query all puppies grouped by the shelter in which they are staying
   ```
   session.query(Puppy).join(Shelter).order_by(Puppy.shelter_id.asc(), Puppy.name)
   ```

### Exiting the VM
To exit type `control + D`
