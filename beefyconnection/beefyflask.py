import os,re
from flask import *
from beefy_db import BeefyDatabase
app = Flask(__name__)

def globals():
    return { 'title' : 'Beefy Connection!',
             'logo'  : '/static/images/beefy.png'}

@app.route("/")
def form():
    return render_template('mainform.html',**globals())

@app.route("/bc-post",methods=['POST'])
def post():
    session['name'] = request.form.get('first-name') + request.form.get('last-name')
    #Needs some server side validation
    databaseConnector = BeefyDatabase("sqlite:///person.db")
    first_name_field = "" if (request.form.get("first-name") == None) else request.form.get("first-name")
    last_name_field =  "" if (request.form.get("last-name") == None) else request.form.get("last-name")
    phone_field = "" if (request.form.get("phone") == None) else request.form.get("phone")
    city_field = "" if (request.form.get("city") == None) else request.form.get("city")
    state_field = "" if (request.form.get("state") == None) else request.form.get("state")
    postal_field = "" if (request.form.get("postal") == None) else request.form.get("postal")
    irc_field = "" if (request.form.get("irc") == None) else request.form.get("irc")
    email_field = "" if (request.form.get("email") == None) else request.form.get("email")
    try:
        databaseConnector.add_person(first_name=first_name_field,
                                last_name=last_name_field,
                                phone=phone_field,
                                city=city_field,
                                state=state_field,
                                postal_code=postal_field,
                                irc=irc_field,
                                fb="",
                                twitter="",
                                interests="",
                                email=email_field,
                                fas="")
        return jsonify(status="Success")
    except Exception as e:
        return jsonify(**{ "status" : "Error",
                           "message" : str(e)})
@app.route("/bc-upload",methods=['POST'])
def upload():
    try:
        name = session['name']
        f = re.sub(r'data.*,','',request.form['photo'] +'==').decode('base64') 
        fn = open("%s/%s/%s" % (os.path.dirname(os.path.realpath(__file__)),"uploads",name + ".png"),'wb')
	fn.write(f)
	fn.close()
	return jsonify(status="Success")
    except Exception as e:
        return jsonify(**{ "status" : "Error",
                           "message" : str(e)})

@app.route("/bc-success")
def success():
    return render_template('thanks.html',**globals())

if __name__ == "__main__":
    app.secret_key = 'beefy-connect'
    app.debug = True
    app.run()
