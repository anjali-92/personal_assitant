from application.app import app

# Import your models here
from application.models import Pomodoro, db

@app.route("/")
def home():
    return {"Status": "Success"}, 200

@app.route("/start_timer", methods=["POST"])
def start_timer():
    # creates a Python Object
    pomo_obj = Pomodoro()

    # adds to the db session
    db.session.add(pomo_obj)

    # Makes the entry in the DB
    # you can do multiple db.session.add before committing
    db.session.commit()

    return "timer started"

@app.route("/get_pomodoros", methods=["GEt"])
def get_pomodoros():
    pomodoros = Pomodoro.query.all()

    results = []
    for pomo in pomodoros:
        results.append({
            "id": pomo.id,
            "start_time": pomo.start_time,
        })
    
    return results
