'''a module to use twitter api and create a web-site with map'''
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl
from folium import Map, FeatureGroup, CircleMarker
from geopy.geocoders import Nominatim
from flask import Flask, redirect, render_template, request, url_for, abort


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
app = Flask(__name__)


def json_create(name):
    '''
    A function to get the screen name and get the information from twitter.
    Return json.
    '''
    acct = name
    if len(acct) < 1:
        quit()
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js


def opening(data):
    '''
    A function to get the necessary data.
    Return a dictionary with screen name as key and location as value.
    '''
    data = data['users']
    people = {}
    for element in data:
        people[element['screen_name']] = element['location']
    return people


def find_coordinates(address):
    '''
    A function to find coordinates of locations.
    Return a list with latitude and longtitude.
    '''
    geolocator = Nominatim(user_agent="locationfind")
    location = geolocator.geocode(address)
    return location


def create_coord_people(data):
    '''
    A function to connect people and locations.
    Return list with screen_name, latitude, longtitude.
    '''
    geolocator = Nominatim(user_agent="locationfind")
    locations = []
    for key, value in data.items():
        location = geolocator.geocode(value)
        if location is not None:
            address = [key, location.latitude, location.longitude]
            locations.append(address)
    return locations


def map_creating(data):
    '''
    A function to create a map, using folium.
    Return a map in html.
    '''
    friends_map = Map(zoom_start=14)
    fg = FeatureGroup(name='Map_with_friends')
    for i in range(len(data)):
        CircleMarker(location=[data[i][1], data[i][2]], radius=10,
        popup=f'<strong>{data[i][0]}</strong>', fill_color='red', color='orange').add_to(fg)
    friends_map.add_child(fg)
    return friends_map._repr_html_()


@app.errorhandler(404)
def not_found(error):
    '''
    Error handler.
    '''
    return render_template('failure.html'), 404

@app.route('/')
def starter():
    '''
    The starter page.
    '''
    return render_template('base.html')

@app.route('/login', methods=['POST', "GET"])
def login():
    '''
    The page with send button.
    '''
    if request.method == 'POST':
        the_user = request.form['screen_name']
        return redirect(url_for('user', usr=the_user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    '''
    The page wiht map or error exception.
    '''
    try:
        return map_creating(create_coord_people(opening(json_create(usr))))
    except:
        abort(404)

@app.route('/choose', methods=['POST'])
def contact():
    '''
    Helper for starter page.
    '''
    if request.method =='POST':
        if request.form['button'] == 'YES':
            return redirect(url_for('login'))
        if request.form['button'] == 'NO':
            abort(404)

app.register_error_handler(404, not_found)

if __name__ == '__main__':
    app.run(debug=True)
