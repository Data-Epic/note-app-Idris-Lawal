# note-app-Idris-Lawal
A Smart Notes Manager was developed using Object Oriented Programming (OOP). This is a programme that creates a template for users to create, organize and manage different types of notes.

## Programming Language and IDE:
* Python
  - Pycharm
    
## Key OOP principles used:
- Encapsulation
- Inheritance
- Polymorphism

## Programming Steps:
1. Creating a Base Class
   A parent class named Note was created with attributes:
   * content: The note text
   * created_at: The Timestamp when the note was created
   and with a method:
   * display(): shows the details of the note
     
2. Extending the Base Class
   Two specialized classes were created to inherit from the Note class:
   * TextNote: A simple text-based note
   * ReminderNote: A reminder that includes additional reminder date and time.
  These child classes were created to have individual display methods that overrides the parent's method

3. Creating a NotesManager Class
   A class to manage different types of notes called NotesManager was created having the methods:
   * add_note(note_type, content, reminder_time=None) which adds a new note of the specified type
   * delete_note(note_id) that removes a note by its ID
   * show_notes() that diplays all notes
   * search_notes(keyword) that finds notes based on given keyword.