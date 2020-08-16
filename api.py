import flask
from flask import Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello!!</h1><p>This site is a sample flask api. Healthcheck route is at /healthcheck</p>"

@app.route('/healthcheck', methods = ['GET'])
def api_healthcheck():
	js = "pass"
	resp = Response(js, status=200, mimetype='application/json')
	return resp

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)
