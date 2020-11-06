"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()


# Sample for pets table:
dog = Pet(name="Doggy", species="dog", photo_url="https://cdn.cdnparenting.com/articles/2018/05/352176329-H-1024x700.jpg",
          age=7, notes="Healthy and happy", available=True)
cat = Pet(name="Kitie", species="cat", photo_url="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1327&q=80",
          age=10, notes="Happy and adoptable", available=True)
tiger = Pet(name="Truman", species="tiger", photo_url="https://images.unsplash.com/photo-1517957754642-2870518e16f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=701&q=80",
            age=12, notes="Healthy and happy", available=True)

db.session.add_all([dog, cat, tiger])
db.session.commit()
