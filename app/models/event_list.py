from app.models.event import *
import datetime

event1 = Event(datetime.date(2021, 1, 21), "G23 Zoombar", 20, "Zoom", "Grab a drink and log your complaints", True)
event2 = Event(datetime.date(2021, 2, 4), "Digital Diversity Group", 50, "Eventbrite", "Codeclan will be exploring intersectionality with an exciting panel!", False)
events = [event1, event2]

def add_new_event(new_event):
    # if statement for true false recurring
    events.append(new_event)

def delete_event(event):
    event_to_delete = None
    for event in events:
        if event.name == event.name:
            event_to_delete = event
            break
    events.remove(event_to_delete)