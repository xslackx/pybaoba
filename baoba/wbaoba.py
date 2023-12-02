from os.path import abspath
from flask import Flask, render_template, request
from baba import Baoba
from remote import sshBaoba
import ipaddress

tmpl = abspath('web/templates')
statics = abspath('web/static')
app = Flask('Baoba Web', template_folder=tmpl, static_folder=statics)


@app.route("/")
def web():
    data = Baoba()
    return render_template('index.html', packages=data.guestFmt)

@app.route('/ssh')
def ssh():
    args = request.args.get('h')
    if args and ipaddress.ip_address(args):
        access = sshBaoba(args)
        access.con()
        data = access.fmt()
        
        return render_template('index.html', packages=data)
    else:
        return "<h1>The ssh host is missing"



    
app.run(host="0.0.0.0")