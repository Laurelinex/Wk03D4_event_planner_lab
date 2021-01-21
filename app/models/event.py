class Event:

    def __init__(self, date, name, guests_num, room, description, recurring):
        self.date = date
        self.name = name
        self.guests_num = guests_num
        self.room = room
        self.description = description
        self.recurring = recurring