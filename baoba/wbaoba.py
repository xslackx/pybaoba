from os.path import abspath
from flask import Flask, render_template
from utils import *

tmpl = abspath('templates')
statics = abspath('static')

app = Flask('baoba web', template_folder=tmpl, static_folder=statics)

# To improve better response to user browser
guestOs = osLike()
guestCmd = packMan(guestOs)
guestPacks = packIns(guestCmd)
guestFmt = packFmt(guestPacks, guestOs)

@app.route("/")
def web():
    return guestFmt
#    return render_template('index.html')
    
app.run()