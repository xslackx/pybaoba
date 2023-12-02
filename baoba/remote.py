from paramiko import AutoAddPolicy, SSHClient
from ipaddress import ip_address
from utils import osLike as os
from utils import packMan as pk
from utils import packIns as ins
from utils import packFmt as pfmt

class sshBaoba:
    def __init__(self, host) -> None:
        self.client = SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.tryconn =  False
        
        try:
            if ip_address(host):
                self.host = host
                self.tryconn = True
        except:
            return ("Invalid IP Address")
        
    def con(self):
        if self.tryconn:
            self.client.connect(self.host, username='root', password='ruan')
            self.response: list = self.client.exec_command("cat /etc/os-release")
            return self.response
        
    def fmt(self):
        self.os = os(ssh=True, fp=self.response[1].read().decode())
        self.cmd = pk(self.os)
        self.inst = ins(self.cmd, ssh=True)
        self.exec = self.client.exec_command(self.inst)
        self.rem = pfmt(pkgs=self.exec[1].read().decode(), id=self.os)
        
        return self.rem