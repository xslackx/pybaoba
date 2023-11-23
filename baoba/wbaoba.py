from os.path import abspath
from flask import Flask, render_template
from utils import *

tmpl = abspath('web/templates')
statics = abspath('web/static')

app = Flask('baoba web', template_folder=tmpl, static_folder=statics)

# To improve better response to user browser
guestOs = osLike()
guestCmd = packMan(guestOs)
guestPacks = packIns(guestCmd)
guestFmt = packFmt(guestPacks, guestOs)

@app.route("/")
def web():
    return render_template('index.html', packages=guestFmt)
    
app.run(host="0.0.0.0")