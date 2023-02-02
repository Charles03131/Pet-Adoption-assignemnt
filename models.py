"""Models for adopt"""

from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
    
def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)


class Pet(db.Model):
    """adoptable pet"""
    __tablename__="pets"

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.Text,nullable=False)
    species=db.Column(db.Text,nullable=False)
    photo_url=db.Column(db.Text,nullable=False)
    age=db.Column(db.Text,nullable=True)
    notes=db.Column(db.Text,nullable=True)
    available=db.Column(db.Boolean,nullable=False,default=True)
