from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "adoptpetwtformsexercise"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


# DEFINE ROUTES BELOW
@app.route('/')
def home_page():
    """Show all pets"""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show form to add new pet and handle form to submit to database"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} added.")
        return redirect('/')
    else:
        return render_template('new.html', form=form)


@app.route('/<int:id>', methods=["GET"])
def pet_detail(id):
    """Show pet detail"""
    pet = Pet.query.get_or_404(id)
    return render_template("detail.html", pet=pet)


@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    """Show edit form and handle form to submit"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Your { pet.name } has been updated")
        return redirect('/')
    else:
        # Fail, represent for editing form
        return render_template("edit.html", form=form, pet=pet)
