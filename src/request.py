import sqlite3
conn = sqlite3.connect('db/sessions.db')
c = conn.cursor()

c.execute("create table if not exists sessions (ID int, PROPERTIES text, STARTTIME text)")

session = "test"
starttime = "l"
c.execute("INSERT INTO sessions VALUES (NULL, ?, ?)", [session, starttime])

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()