from flask import Flask, render_template,url_for            #pip install Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world1():
  now = datetime.now()
  date = now.strftime("%d/%m/%Y")
  time = now.strftime("%H:%M:%S")
  return render_template("STATION.html", date=date, time=time)

@app.route('/num/<n>/<t>')
def hello_world3(n: str, t: str):
  st = [20, 30]
  s = int(t)*st[int(n)-1]
  return render_template("THANK.html", n=n, t=t, sm=s)

@app.route('/num/<n>')
def hello_world2(n: str):
   return render_template("TICKETS.html", n=n)

app.run()
