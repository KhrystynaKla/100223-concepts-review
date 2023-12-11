#!/usr/bin/env python3

from app import app
from models import db, Gift # models go here
from faker import Faker
from random import randint

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")
        Gift.query.delete()
        # write your seeds here!
        
        for _ in range(6):
            new_gift = Gift(name =faker.name(), price = randint(1,1000)/100.0)
            db.session.add(new_gift)
        db.session.commit()

        print("Seeding complete!")
