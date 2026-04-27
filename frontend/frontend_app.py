# The purpose of this project is to display the best maps
# for the special weapon Wave Breaker in the video game of
# Splatoon 3.
from flask import Flask, render_template, request
import requests

frontend_app = Flask(__name__)
backend_url = 'http://127.0.0.1:5001'

@frontend_app.route('/')
def home():  # put application's code here
    return render_template('base.html')

@frontend_app.route('/maplist')
def maplist():
    response = requests.get(backend_url + '/api')
    return render_template('waveMaps.html', wave_maps=response.json())

@frontend_app.route('/addMap', methods=['GET', 'POST'])
def addMap():
    if request.method == 'GET':
        return render_template('addMap.html')

    if request.method == 'POST':
        map_name = request.form.get('map_name')
        map_description = request.form.get('map_description')
        spu_amount = request.form.get('spu_amount')

        # Validating input a little bit, just sends you home if it fails.
        # spu_amount is capped at three because of how the amounts of gear
        # abilities are tracked in the Splatoon community, always an "X.X" format.
        if len(map_name) > 50 or len(map_description) > 250 or len(spu_amount) > 3:
            return render_template("base.html")

        waveMap = [{
            'map': map_name,
            'description': map_description,
            'spu': spu_amount
        }]
        response = requests.post(backend_url + '/api/new', json=waveMap)
        return f'<h1>Added map. <a href="http://127.0.0.1:5000/">Continue</a></h1>'

@frontend_app.route('/removeMap/<string:map_name>', methods=['POST'])
def del_map_by_id(map_name):
    response = requests.post(backend_url + '/api/remove', json=[map_name])
    return f'<h1>Map was removed. <a href="http://127.0.0.1:5000/">Continue</a></h1>'

if __name__ == '__main__':
    frontend_app.run(port=5000, debug=True)
