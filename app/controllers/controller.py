from app import app
from app.models.event import Event
from flask import render_template, request
from app.models.event_list import events, add_new_event, delete_event

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/events')
def show_events():
    return render_template('events.html', title="Events List", events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_guests = request.form['event_guests']
    event_location = request.form['event_location']
    event_description = request.form['event_description']
    event_recurring = request.form['event_recurring']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('events.html', title="Events List", events=events)

@app.route('/events/delete/<event_name>', methods=[('POST')])
def delete_event():
    name = request.form['event_name']
    delete_event(event)
    return render_template('events.html', title="Events List", events=events)