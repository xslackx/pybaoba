from os.path import abspath
from flask import Flask, render_template, request
from baba import Baoba
import ipaddress

tmpl = abspath('web/templates')
statics = abspath('web/static')
app = Flask('Baoba Web', template_folder=tmpl, static_folder=statics)
data = Baoba()

@app.route("/")
def web():
    return render_template('index.html', packages=data.guestFmt)

@app.route('/ssh')
def ssh():
    args = request.args.get('h')
    if args and ipaddress.ip_address(args):
        import paramiko
        from utils import osLike as os
        from utils import packMan as pk
        from utils import packIns as ins
        from utils import packFmt as fmt
        
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(args, username='root', password='ruan')
        _stdin, _stdout,_stderr = client.exec_command("cat /etc/os-release")
        
        remote_os = os(ssh=True, fp=_stdout.read().decode())
        remote_cmd = pk(remote_os)
        installed = ins(remote_cmd, ssh=True)
        _stdin, _stdout,_stderr = client.exec_command(installed)
        
        remote_fmt = fmt(pkgs=_stdout.read().decode(), id=remote_os)
        
        return render_template('index.html', packages=remote_fmt)
    else:
        return "<h1>The ssh host is missing"



    
app.run(host="0.0.0.0")