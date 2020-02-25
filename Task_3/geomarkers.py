import folium
import random
from geopy.geocoders import Nominatim


def find_location(location):
    """
    (str) -> tuple
    Return longitude and latitude оf the place where the films were shot
    >>> find_location("Lviv")
    (49.841952, 24.0315921)
    >>> find_location("London")
    (51.5073219, -0.1276474)
    """
    geolocation = Nominatim(user_agent="qwerty")
    geo_loc = geolocation.geocode(location)
    if geo_loc is None:
        return 0, 0
    return geo_loc.latitude, geo_loc.longitude


def normalizer(position):
    """
    :param position: tuple
    :return: tuple
    Return edited position in order to avoid collisions
    """
    x = random.uniform(-0.009, 0.009)
    y = random.uniform(-0.009, 0.009)
    return position[0]+x, position[1]+y


def build_map(user, position_dict):
    """
    (tuple, dict) -> ()
    Create a map where person and his/her top-10
    friend will be marked
    """
    user_loc = find_location(user)
    web_map = folium.Map(location=[user_loc[0], user_loc[1]],
                         zoom_start=7)
    fg_gang = folium.FeatureGroup(name="Gang")
    for position in position_dict:
        current_position = find_location(position)
        if current_position == (0, 0):
            continue
        icon = folium.features.CustomIcon(position_dict[position][1],
                                          icon_size=(50, 50))
        text = position_dict[position][0].strip('"')
        popup = folium.Popup(text, max_width=200)
        folium.Marker(
            location=normalizer(current_position),
            popup=popup,
            icon=icon
        ).add_to(fg_gang)
    web_map.add_child(fg_gang)
    web_map.add_child(folium.LayerControl())
    web_map.save("/home/TsapivV/mysite/templates/map.html")
