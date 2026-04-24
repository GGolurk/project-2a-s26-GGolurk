# The purpose of this project is to display the best maps
# for the special weapon Wave Breaker in the video game of
# Splatoon 3.
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
