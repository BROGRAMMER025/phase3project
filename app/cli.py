# app/cli.py
import click
from datetime import datetime
from models import Base, Owner, Pet, FeedingTraining, VetVisits, Vets, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def list_owners():
    owners = session.query(Owner).all()
    for owner in owners:
        click.echo(f"Owner ID: {owner.id}, Name: {owner.name}")

@cli.command()
def list_pets():
    pets = session.query(Pet).all()
    for pet in pets:
        click.echo(f"Pet ID: {pet.id}, Name: {pet.name}, Owner ID: {pet.owner_id}")

@cli.command()
def list_feeding_training():
    techniques = session.query(FeedingTraining).all()
    for technique in techniques:
        click.echo(f"Technique ID: {technique.id}, Name: {technique.name}")

@cli.command()
def list_vet_visits():
    visits = session.query(VetVisits).all()
    for visit in visits:
        click.echo(f"Visit ID: {visit.id}, Date: {visit.visit_date}, Vet ID: {visit.vet_id}")

@cli.command()
def list_vets():
    vets = session.query(Vets).all()
    for vet in vets:
        click.echo(f"Vet ID: {vet.id}, Name: {vet.name}")
        
@cli.command()
def list_vets():
    vets = session.query(Vets).all()
    for vet in vets:
        click.echo(f"Vet ID: {vet.id}, Name: {vet.name}")


@cli.command()
def add_owner():
    name = click.prompt("Enter owner's name")
    new_owner = Owner(name=name)
    session.add(new_owner)
    session.commit()
    click.echo("Owner added successfully!")

@cli.command()
def add_pet():
    name = click.prompt("Enter pet's name")
    owner_id = click.prompt("Enter owner's ID")
    new_pet = Pet(name=name, owner_id=owner_id)
    session.add(new_pet)
    session.commit()
    click.echo("Pet added successfully!")

@cli.command()
def add_feeding_training():
    name = click.prompt("Enter feeding training name")
    new_technique = FeedingTraining(name=name)
    session.add(new_technique)
    session.commit()
    click.echo("Feeding training added successfully!")

@cli.command()
def add_vet_visit():
    click.echo("Add Vet Visit")

    visit_date_str = click.prompt("Enter visit date (YYYY-MM-DD HH:MM:SS)")
    vet_id = click.prompt("Enter vet's ID", type=int)
    visit_date = datetime.strptime(visit_date_str, '%Y-%m-%d %H:%M:%S')
    vet_visit = VetVisits(visit_date=visit_date, vet_id=vet_id)
    session.add(vet_visit)
    session.commit()

    click.echo("Vet Visit added successfully!")

@cli.command()
def add_vet():
    name = click.prompt("Enter vet's name")
    new_vet = Vets(name=name)
    session.add(new_vet)
    session.commit()
    click.echo("Vet added successfully!")

def menu_options():
    while True:
        click.echo("1. List Owners")
        click.echo("2. List Pets")
        click.echo("3. List Feeding Training")
        click.echo("4. List Vet Visits")
        click.echo("5. List Vets")
        click.echo("6. Add Owner")
        click.echo("7. Add Pet")
        click.echo("8. Add Feeding Training")
        click.echo("9. Add Vet Visit")
        click.echo("10. Add Vet")
        click.echo("0. Exit")

        choice = click.prompt("Enter your choice")

        if choice == "0":
            break
        elif choice == "1":
            list_owners()
        elif choice == "2":
            list_pets()
        elif choice == "3":
            list_feeding_training()
        elif choice == "4":
            list_vet_visits()
        elif choice == "5":
            list_vets()
        elif choice == "6":
            add_owner()
        elif choice == "7":
            add_pet()
        elif choice == "8":
            add_feeding_training()
        elif choice == "9":
            add_vet_visit()
        elif choice == "10":
            add_vet()

if __name__ == "__main__":
    
    Base.metadata.create_all(bind=engine)
    menu_options()
