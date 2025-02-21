import sqlite3

conn = sqlite3.connect('sql1.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
   id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   name  TEXT,
   email TEXT
);

CREATE TABLE Course (
   id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   title  TEXT
);

CREATE TABLE Member (
   user_id    INTEGER,
   course_id  INTEGER,
   role       INTEGER,
   PRIMARY KEY (user_id, course_id)
)
''')

cur.execute('''
       INSERT OR IGNORE INTO User (name, email) VALUES ('Jane','jane@stsugi.org');
''')
cur.execute(''' 
       INSERT OR IGNORE INTO User (name, email) VALUES ('Ed','ed@stsugi.org');
''')
cur.execute('''
       INSERT OR IGNORE INTO User (name, email) VALUES ('Sue','jane@stsugi.org');
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Course (title) VALUES ('Python');
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Course (title) VALUES ('SQL');
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Course (title) VALUES ('PHP');
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (1,1,1);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (2,1,0);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (3,1,0);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (1,2,0);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (2,2,1);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (2,3,1);
''')
cur.execute(''' 
       INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (3,3,0);
''')

cur.execute(''' 
       SELECT User.name, Member.role, Course.title
       FROM User JOIN Member JOIN Course
       ON Member.user_id = User.id AND Member.course_id = Course.id
       ORDER BY Course.title, Member.role DESC, User.name
''')
conn.commit()
