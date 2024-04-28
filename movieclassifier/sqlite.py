import sqlite3
import os

if os.path.exists('reviews.sqlite'):
    os.remove('reviews.sqlite')

conn =sqlite3.connect('reviews.sqlite')
c=conn.cursor()
c.execute('CREATE TABLE review_db'\
          ' (review TEXT, sentiment INTEGER, date TEXT)')

example1='i love it'
c.execute("INSERT INTO review_db"\
          " (review, sentiment,date) VALUES"\
            " (?,?,DATETIME('now'))", (example1,1))

example2="i don't like it"
c.execute("INSERT INTO review_db"\
          " (review, sentiment,date) VALUES"\
            " (?,?,DATETIME('now'))", (example2,0))
conn.commit()
conn.close()

conn =sqlite3.connect('reviews.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM review_db")
results=c.fetchall()
conn.close
print(results)