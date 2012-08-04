from flask import Flask
from flask import request
from flask import json
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data', methods = ['POST'])
def api_message():

    #if request.headers['Content-Type'] == 'text/plain':
    #    return "Text Message: " + request.data
    print request
    if request.headers['Content-Type'] == 'application/json':
        print request.json
        if 'b64image' in request.json:
            img =  request.json['b64image']
            # example
            #str642 = 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGFBMVEX///8AAADdcDJ2dnbxxKrooHbFXSLiiFTBBJn/AAAAoUlEQVQI1+2P2wpCMQwEs7m0///HCgtFjwiGBUXItPRthq19iWEYBgCavvcGBJ0Aks6EpDMh6Uz0dCGBlblfMfOPA2tVXfQ090bgmsh07waYOHo3QDKP3g4QN7PtQmA5/R8GlrkYyGYg9AUW0gL9C/KCEALBN4A3AXz4hadEtXQm4nFFtvRgIyJOoho6Zd6zoi56o8IVRb2l8hBQ/wuGYRhuUkAKnGTDFncAAAAASUVORK5CYII='
            png_recovered = base64.decodestring(request.json['b64image'])
            #png_recovered = base64.decodestring(str642)
            f = open("temp.png", "w")
            f.write(png_recovered)
            f.close()
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "Hello"

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

if __name__ == '__main__':
    app.run(debug=True)
