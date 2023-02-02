from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, IntegerField,TextAreaField,BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional,AnyOf


class AddPet(FlaskForm):
    """form for adding pets"""
    name=StringField("Pet Name",validators=[InputRequired()])
    species=StringField("Species",validators=[AnyOf(values=['cat','dog','porcupine'],message="species must be cat,dog,or porcupine")])
    photo_url=StringField("Photo Url",validators=[Optional(),URL()])
    age=IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes=TextAreaField("Notes",validators=[Optional()])



class EditPet(FlaskForm):
    """form for editing pets"""
    
    
    photo_url=StringField("Photo Url",validators=[Optional(),URL()])
    notes=TextAreaField("Notes",validators=[Optional()])
    available=BooleanField("Available?")


