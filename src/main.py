from flask import Flask, request, jsonify
from models import db, Character, Location, User, Favorite

app = Flask(__name__)

@app.route("/people")
def get_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))

    return jsonify({
        "status": "success",
        "data": characters
    }), 200


@app.route("/people/<int:character_id>")
def get_only_character(character_id):
    character = Character.query.get(character_id) #filter_by

    if character is not None:
        return jsonify({
            "status": "success",
            "data": character
        }), 200
    else: 
        return jsonify({
            "msg": "Character not found",
            "status": "Error"
        }), 404


@app.route("/planet")
def get_location():
    locations = Location.query.all()
    locations = list(map(lambda location: location.serialize(), locations))

    return jsonify({
        "status": "success",
        "data": locations
    }), 200


@app.route("/planet/<int.planets_id>")
def get_only_location(planets_id):
    location = Location.query.get(planets_id)

    if location is not None:
        return jsonify({
            "status": "success",
            "data": location
        }), 200
    else:
        return jsonify({
            "msg": "Location not found",
            "status": "Error"
        }), 404
    

@app.route("/users")
def get_user():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return ({
        "status": "success",
        "data": users
    }), 200


@app.route("/users/favorites/<int:user_id>")
def get_user_fav(user_id):
    user_fav = Favorite.query.filter_by(userID = user_id).all()
    return jsonify({
        "status": "success",
        "data": user_fav
    }), 200



@app.route("/favorite/planet/<int:planet_id>", methods = ["POST"])
def create_fav_planet(planet_id):
    planet_fav = Location.query.get(planet_id)
    data = request.get_json()


    db.session.add(planet_fav)
    db.session.commit()

    return jsonify({
        "msg": "Planet added to favorites",
        "status": "success"
    }), 200



@app.route("/favorite/people/<int:people_id>", methods = ["POST"])
def create_fav_character(people_id):
    character_fav = Character.query.get(people_id)
    data = request.get_json()


    db.session.add(character_fav)
    db.session.commit()

    return jsonify({
        "msg": "Character added to favorites",
        "status": "success"
    }), 200



@app.route("/favorite/planet/<int:planet_id>", methods = ["DELETE"])
def delete_fav_planet(planet_id):
    fav = Favorite.query.get(planet_id)
    if fav is not None:
        db.session.delete(planet_id)
        db.session.commit()
        return jsonify({
            "msg": "Planet has been delete in favorite",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "msg": "Planet not found in favorite",
            "status": "error"
        }), 404
    
    
@app.route("/favorite/people/<int:people_id>", methods = ["DELETE"])
def delete_fav_character(people_id):
    fav = Favorite.query.get(people_id)
    if fav is not None:
        db.session.delete(people_id)
        db.session.commit()
        return jsonify({
            "msg": "Character has been delete in favorite",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "msg": "Character not found in favorite",
            "status": "error"
        }), 404
