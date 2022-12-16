from flask import Flask                 # from the flask module import the Flask class


app = Flask(__name__)                   # Create an instance of the Flask class into app (now an object)
                                        # Class is to object as blueprint is to house.

@app.get("/")                           # A decorator that allows us to map a route to a "view function"
def index():                            # Flask calls functons mapped to a route "view functions"
    out = {                             # Flask will automatically convert dictionaries to JSON for convenience.
        "first_name": "Letherius",
        "last_name": "Miller",
        "hobbies": "DIY stuff",
        "is_active": True
    }
    return out                          # If we wish to build a RESTful service, this is a good convention to follow
                                        # as JSON is the norm for the most RESTful services.