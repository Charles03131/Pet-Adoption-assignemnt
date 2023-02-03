"""adopt app"""

from flask import Flask,request,redirect,render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet,EditPet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretsecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route("/")
def show_pet_list():
    """show list of pets"""
    pets=Pet.query.all()
    return render_template("pet_list.html",pets=pets)


@app.route("/add", methods=["GET","POST"])
def add_pet():
    """show add pet form and processing of add pet form"""

    form=AddPet()

    if form.validate_on_submit():
        #need to add the security key
        
        new_pet=Pet(
        name=form.name.data,
        species=form.species.data,
        photo_url=form.photo_url.data,
        age=form.age.data,
        notes=form.notes.data,
        )

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("add_pet_form.html",form=form)

    


@app.route("/<int:pet_id>", methods=["GET","POST"])
def pet_details_and_edit(pet_id):
    """show pet details and process pet edit form"""
    pet=Pet.query.get_or_404(pet_id)
    form=EditPet(obj=pet)

    if form.validate_on_submit():
        #need to add the security key

        pet.photo_url=form.photo_url.data,
        pet.notes=form.notes.data,
        pet.available=form.available.data
    
        db.session.commit()

        flash("YAY you updated the info")
        return redirect("/")
    
    else:
        """show pet details/edit form"""
        flash("please try again")
        return render_template("pet_details_and_editform.html",form=form,pet=pet)
    
@app.route("/<int:pet_id>/delete", methods=["GET","POST"])
def delete_pet(pet_id):
    """delete pet"""
    pet=Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()

    return redirect("/")

  
#this last route to delete a pet was not required.It does not work yet.


