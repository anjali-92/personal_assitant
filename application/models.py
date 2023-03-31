from application.app import app, db
from datetime import datetime


# class Pomodoro_Settings():
#    set_focused_hours = 

# class Pomodoro_Cycle():
#     

class Pomodoro(db.Model):
    ''' docstring '''
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    stop_time = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    # pomo_cycle_id =
    # task_id =

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # email = db.Column(db.String(80), unique=True, nullable=False)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120))

# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here



# create all tables and initialize app
with app.app_context():
    db.create_all()
