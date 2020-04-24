from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

from get_personality import Personality

@app.route('/')
def list():
   con = sql.connect("../scraper/database/movie_actor_data.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * FROM actor_tb")
   rows = cur.fetchall()
   con.close()
   return render_template("list_actors.html",rows = rows)

@app.route('/actor/detail/<id>')
def actor_detail(id):
   con = sql.connect("../scraper/database/movie_actor_data.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   query = "SELECT * FROM actor_tb WHERE id = "+id
   cur.execute(query)
   row = cur.fetchall()[0]
   con.close()
   personality = Personality(row['actor_bio']).ibm_watson_data()
   if personality:
      return render_template("actor_detail.html",row = row, personality = personality.get('result_personality'))
   else:
      return render_template("actor_detail.html",row = row, personality = None)

if __name__ == '__main__':
   app.run(debug = True)