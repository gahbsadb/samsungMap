from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import folium

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    map_html = None
    if request.method == "POST":
        city = request.form["city"]
        geolocator = Nominatim(user_agent="city_locator")
        location = geolocator.geocode(city)
        if location:
            m = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
            folium.Marker([location.latitude, location.longitude], popup=city).add_to(m)
            map_html = m._repr_html_()
        else:
            map_html = "<p>City not found.</p>"
    return render_template("index.html", map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)
