# The purpose of this project is to display the best maps
# for the special weapon Wave Breaker in the video game of
# Splatoon 3.
from flask import Flask, render_template, request

app = Flask(__name__)

## In memory data structure
waveMaps = [
    {'Map':'Hagglefish Market', 'Description':
    'Incredibly good spots in mid, with decent utility both on offense and defense. Better on tower control since you can throw wave on the tower.',
     'SPU':1.1},
    {'Map':'Makomart',
     'Description':'The entire middle of the map is a wave breaker spot, but there are also good spots on the stacks for defense and offense.',
     'SPU':0.0},
    {'Map':'Flounder Heights',
     'Description':'You can\'t mess up throwing wave on this map, but try to aim for higher locations for better coverage.',
     'SPU':0.1},
    {'Map':'Um\'ami Ruins',
     'Description':'Very good spots if you know where to look for them. Nothing spectacular, but wave is good in all areas.',
     'SPU':1.1},
]

@app.route('/')
def home():  # put application's code here
    return render_template('base.html')

@app.route('/maplist')
def maplist():
    return render_template('waveMaps.html', wave_maps=waveMaps)

@app.route('/addMap', methods=['GET', 'POST'])
def addMap():
    if request.method == 'POST':
        map_name = request.form.get('map_name')
        map_description = request.form.get('map_description')
        spu_amount = request.form.get('spu_amount')

        # Validating input a little bit, just sends you home if it fails.
        # spu_amount is capped at three because of how the amounts of gear
        # abilities are tracked in the Splatoon community, always an "X.X" format.
        if len(map_name) > 50 or len(map_description) > 250 or len(spu_amount) > 3:
            return render_template("base.html")

        waveMap = {
            'Map': map_name,
            'Description': map_description,
            'SPU': spu_amount
        }
        waveMaps.append(waveMap)
        # Sends you to check out the maps after you add it!
        return render_template('waveMaps.html', wave_maps=waveMaps)
    return render_template('addMap.html')

@app.route('/removeMap/<string:map_name>', methods=['POST'])
def del_map_by_id(map_name):
    for eachMap in waveMaps:
        if eachMap['Map'] == map_name:
            waveMaps.remove(eachMap)
            return f'<h1>Map was removed. <a href="http://127.0.0.1:5000/">Continue</a></h1>'
        # makes you go home if not found
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
