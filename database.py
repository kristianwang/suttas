import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create the book table
conn.execute('''CREATE TABLE book
             (book_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             url TEXT NOT NULL,
             chapter_id INTEGER,
             FOREIGN KEY (chapter_id) REFERENCES chapter(chapter_id))''')

# Create the chapter table
conn.execute('''CREATE TABLE chapter
             (chapter_id INTEGER PRIMARY KEY,
             verse_id INTEGER,
             FOREIGN KEY (verse_id) REFERENCES verse(verse_id))''')

# Create the verse table
conn.execute('''CREATE TABLE verse
             (verse_id INTEGER PRIMARY KEY,
             verse_content TEXT NOT NULL)''')

# Commit the changes
conn.commit()





# Close the connection
conn.close()