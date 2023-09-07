from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Favorite(db.Model):
    __tablename__ = 'favorite'
    favoriteID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    characterID = db.Column(db.Integer, db.ForeignKey('character.characterID'))

class Character(db.Model):
    __tablename__ = 'character'
    characterID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    episode = db.Column(db.String(40), nullable=True)
    favoriteID = db.relationship('Favorite')
    locationID = db.relationship('Location')
    statusID = db.relationship('Status')

    def serialize(self):
        return {
            "id": self.characterID,
            "name": self.name,
            "episode": self.episode
        }
    
class Status(db.Model):
    __tablename__ = 'status'
    statusID = db.Column(db.Integer, primary_key=True)
    characterID = db.Column(db.Integer, db.ForeignKey('character.characterID'))
    status = db.Column(db.String(15), nullable=True)

    def serialize(self):
        return {
            "id": self.statusID,
            "status": self.status
        }

class User(db.Model):
    __tablename__ = 'user'
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    favoriteID = db.relationship('Favorite')

    def serialize(self):
        return {
            "id": self.userID,
            "name": self.name,
            "mail": self.email
        }

class Location(db.Model):
    __tablename__ = 'location'
    locationID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    characterID = db.Column(db.Integer, db.ForeignKey('character.characterID'))

    def serialize(self):
        return {
            "id": self.LocationID,
            "name": self.name
            # do not serialize the password, its a security breach
        }
    # def __repr__(self):
    #     return '<User %r>' % self.username

