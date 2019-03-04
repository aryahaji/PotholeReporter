class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    profiles = db.relationship('Profile', backref = 'user')

class PotHole(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    town = db.Column(db.String(), nullable = False)
    size = db.Column(db.Integer(), nullable = False)
    xcord = db.Column(db.Double(), nullable = False)
    ycord = db.Column(db.Double(), nullable = False)
    #image = *PICTURE*