# app/seed.py
from app.models import Owner, Pet, FeedingTraining 
from app import SessionLocal, init_db

def seed_data():
    init_db()

    # Add seed data as needed
    # Example:
    session = SessionLocal()
    owner1 = Owner(name="John Doe")
    pet1 = Pet(name="Fido", owner=owner1)
    technique1 = FeedingTraining(name="Raw Diet")

    session.add_all([owner1, pet1, technique1])
    session.commit()

if __name__ == "__main__":
    seed_data()
