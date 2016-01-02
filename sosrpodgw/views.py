from flask import render_template
from sosrpodgw import app
from srapi import Programs, Podfiles, Podfile
from soco import SoCo


@app.route("/")
def index():
    return render_template("index.html", programs=Programs().get_all_programs_with_pod())

@app.route("/program/<id>/")
def program(id):
    return render_template("program.html", podfiles=Podfiles().get_all_podfiles(id))

@app.route("/podplay/<podid>")
def podplay(podid):
    zp = SoCo("192.168.0.54")
    podfile = Podfile().get_podfile(podid)
    zp.play_uri(podfile["url"])
    return "Spelar.."
    
    
