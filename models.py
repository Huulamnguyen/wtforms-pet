from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Connect model and app.py file


def connect_db(app):
    db.app = app
    db.init_app(app)


# Default picture for pets
URL_PHOTO_DEFAULT = "https://dcassetcdn.com/design_img/832896/119820/119820_4885988_832896_image.jpg"


# MODELS GO BELOW!
class Pet(db.Model):
    """Pet model"""
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=URL_PHOTO_DEFAULT)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.id} {self.name} {self.species}>"
