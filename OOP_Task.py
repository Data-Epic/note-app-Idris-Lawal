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