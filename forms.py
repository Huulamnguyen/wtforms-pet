# We can define many forms in form.py file and show it in an appropriate templates.
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


# Define pet form:
class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[
                          ('cat', 'cat'),  ('dog', 'dog'),  ('tiger', 'tiger'), ('por', 'porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Comments", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Comments", validators=[Optional()])
    available = BooleanField("Available")
