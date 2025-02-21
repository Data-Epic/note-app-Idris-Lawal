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