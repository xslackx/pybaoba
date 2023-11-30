from os.path import abspath
from flask import Flask, render_template
from baba import Baoba

tmpl = abspath('web/templates')
statics = abspath('web/static')
app = Flask('Baoba Web', template_folder=tmpl, static_folder=statics)
data = Baoba()

@app.route("/")
def web():
    return render_template('index.html', packages=data.guestFmt)
    
app.run(host="0.0.0.0")