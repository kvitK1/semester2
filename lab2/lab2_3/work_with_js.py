
import json
import re
from folium import Map, FeatureGroup, CircleMarker
from geopy.geocoders import Nominatim
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# def opening():
#     with open('/Users/kvitoslava/2semestr/lab2/lab2_3/file.json', 'r') as file:
#         data =json.load(file)
#     data = data['users']
#     people = {}
#     for element in data:
#         people[element['screen_name']] = element['location']
#     return people


# def find_coordinates(address):
#     geolocator = Nominatim(user_agent="locationfind")
#     location = geolocator.geocode(address)
#     return location


# def create_coord_people(data):
#     geolocator = Nominatim(user_agent="locationfind")
#     locations = []
#     for key, value in data.items():
#         location = geolocator.geocode(value)
#         if location is not None:
#             address = [key, location.latitude, location.longitude]
#             locations.append(address)
#     return locations



# def map_creating(data):
#     friends_map = Map(zoom_start=4)
#     fg = FeatureGroup(name='Map_with_friends')
#     for i in range(len(data)):
#         CircleMarker(location=[data[i][1], data[i][2]], radius=10, popup=f'<strong>{data[i][0]}</strong>', fill_color='red', color='orange').add_to(fg)
#     friends_map.add_child(fg)
#     friends_map.save('Twitter_map.html')
#     # friends_map._repr_html_()
# map_creating(create_coord_people(opening()))


# @app.route('/map')
# def show_map():
#     return render_template('Twitter_map.html')



@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('tte.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'




if __name__ == '__main__':
    app.run(debug=True)