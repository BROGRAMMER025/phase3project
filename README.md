## AUTHOR
Allan Murigi

# Pets and Pals Database Management System

This project is a simple database management system for tracking owners, pets, feeding training techniques, vet visits, and vets. It uses Python and SQLAlchemy to interact with an SQLite database.

## Installation

Make sure you have Python installed. Clone the repository and install the required dependencies:

## python
Copy code
engine = create_engine("sqlite:///./petsandpals.db")
Running the Application
To run the application, execute the following command:

bash
Copy code
python app/cli.py
This will start a command-line interface where you can list owners, pets, feeding training techniques, vet visits, and vets. You can also add new entries.

## Commands
Here are some commands available in the CLI:

list_owners: List all owners.
list_pets: List all pets.
list_feeding_training: List all feeding training techniques.
list_vet_visits: List all vet visits.
list_vets: List all vets.
add_owner: Add a new owner.
add_pet: Add a new pet.
add_feeding_training: Add a new feeding training technique.
add_vet_visit: Add a new vet visit.
add_vet: Add a new vet.

## Database Schema
Owners Table
id (Primary Key)
name (Not Null)
Pets Table
id (Primary Key)
name (Not Null)
owner_id (Foreign Key - References Owners.id)
Feeding Training Table
id (Primary Key)
name (Not Null)
Vet Visits Table
id (Primary Key)
visit_date (Not Null)
vet_id (Foreign Key - References Vets.id)
Vets Table
id (Primary Key)
name (Not Null)

## ERD (Text Representation)
Owners
------
Attributes:
- id (Primary Key)
- name

Relationships:
- One-to-Many with Pets (One owner can have many pets)

Pets
----
Attributes:
- id (Primary Key)
- name
- owner_id (Foreign Key - References Owners.id)

Relationships:
- Many-to-One with Owners (Many pets can belong to one owner)
- One-to-Many with VetVisits (One pet can have many vet visits)

FeedingTraining
---------------
Attributes:
- id (Primary Key)
- name

Relationships:
- No direct relationships in the provided code

VetVisits
---------
Attributes:
- id (Primary Key)
- visit_date
- vet_id (Foreign Key - References Vets.id)
- pet_id (Foreign Key - References Pets.id)

Relationships:
- Many-to-One with Pets (Many vet visits can belong to one pet)
- Many-to-One with Vets (Many vet visits can be performed by one vet)

Vets
----
Attributes:
- id (Primary Key)
- name

Relationships:
- One-to-Many with VetVisits (One vet can perform many vet visits)

## ERD

+---------------------+    +---------------------+    +---------------------+    +---------------------+    +---------------------+
|        Owners       |    |         Pets        |    |   FeedingTraining  |    |      VetVisits      |    |         Vets        |
+---------------------+    +---------------------+    +---------------------+    +---------------------+    +---------------------+
| id (PK)             |    | id (PK)             |    | id (PK)             |    | id (PK)             |    | id (PK)             |
| name                |    | name                |    | name                |    | visit_date          |    | name                |
| pets (FK)           |----| owner_id (FK)       |    +---------------------+----| vet_id (FK)         |    +---------------------+
+---------------------+    +---------------------+                            | pet_id (FK)         |
                                                                                +---------------------+
