from . import db, ma


class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50)) 
    password = db.Column(db.String(50)) 
    photo = db.Column(db.String(50)) 


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'photo')

