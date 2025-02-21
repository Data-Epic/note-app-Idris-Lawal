from datetime import datetime
import pandas as pd

# Create Base Note class
class Note:
    default_date = datetime.today() #call class attribute setting today as a default date
    def __init__(self, content, created_at = default_date):
        self.content = content
        if isinstance(created_at, datetime):    #set date given to the standard date format
            self.created_at = created_at
        else:
            self.created_at = pd.to_datetime(created_at)

    def display(self):
        return (f"Note created at {self.created_at}:\n{self.content}")

mynote = Note("This is my note")
print(mynote.display())

# create Text Note inheriting from Note class with default date
class TextNote(Note):
    def __init__(self, content, created_at = Note.default_date):
        if isinstance(content, str):            # ensure content is text-based
            Note.__init__(self, content, created_at)
        else:
            raise ValueError("Content must be text-based!")
    def display(self):
        return(f"My TextNote created at {self.created_at}:\n{self.content}")

mytext = TextNote("I am happy", "2025-02-18")
print(mytext.display())
mytext1 = TextNote("Are you happy?")
print(mytext1.display())

class ReminderNote(Note):
    def __init__(self, content, reminder_date, reminder_time, created_at=Note.default_date):
        Note.__init__(self, content, created_at)
        if isinstance(reminder_date, datetime):
            self.reminder_date = reminder_date
        else:
            self.reminder_date = pd.to_datetime(reminder_date).date()
        self.reminder_time = reminder_time
    def display(self):
        return(f"My ReminderNote {self.created_at}:\n {self.content} on {self.reminder_date} by {self.reminder_time}")

myreminder = ReminderNote("Conference meeting", "2025-02-20", "4pm")
print(myreminder.display())

#created Notes Manager
class NotesManager:
    def __init__(self):
        self.notes = [] # list to store notes

    def add_note(self, note_type, content, reminder_time=None):
        self.note_type = note_type
        self.content = content
        self.reminder_time = reminder_time
        self.new_note = self.note_type + ":" + " " + self.content + " " + "-" + " " + str(self.reminder_time)
        self.notes.append(self.new_note)
        return "successfully added"

    def delete_note(self, note_id):
        self.note_id = note_id
        self.notes.pop(note_id-1)
        print(f"note {self.note_id} successfully deleted")

    def show_notes(self):
        print(self.notes)

    def search_notes(self, keyword):
        for note in self.notes:
            if keyword in note:
                print(note)
                break
        else:
            print("Note doesn't exist")

#test Note Manager
my_notes = NotesManager()
my_notes.add_note("text", "Review OOP concept")
my_notes.add_note("reminder", "Project deadline", "2025-03-10 10:00 AM")

my_notes.show_notes()
my_notes.search_notes("OOP")
my_notes.search_notes("Project")
my_notes.search_notes("Aim")
my_notes.delete_note(1)
my_notes.show_notes()