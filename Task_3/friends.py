import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

TWITTER_URL_USER = 'https://api.twitter.com/1.1/users/search.json'
TWITTER_URL_FRIENDS = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_data(user, twitter_url):
    """
    :param twitter_url: str
    :param user: str
    :return:dict
    Return user or users (friends of user) object/list of objects in dict format
    """
    if len(user) < 1:
        return {}
    if twitter_url == TWITTER_URL_USER:
        url = twurl.augment(twitter_url,
                            {'q': user, 'include_entities': False})
    else:
        url = twurl.augment(twitter_url,
                            {'screen_name': user, 'count': '20', 'include_entities': False})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    return json.loads(data)


def position_data(username):
    """
    :param username: str
    :return: dict, tuple
    Return dict where keys are a location of friends;
    values are name and link to twitter profile image
    """
    user_obj = get_data(username, TWITTER_URL_USER)[0]
    user_loc = user_obj["location"]
    user_img = user_obj["profile_image_url"]
    user_screen_name = user_obj["screen_name"]
    friends_obj = get_data(user_screen_name, TWITTER_URL_FRIENDS)
    friends_loc = []
    friends_name_and_img = []
    for friend in friends_obj["users"]:
        friends_loc.append(friend["location"])
        friends_name_and_img.append((friend["name"], friend["profile_image_url"]))
    friends_data = dict(zip(friends_loc, friends_name_and_img))
    friends_data[user_loc] = (user_screen_name, user_img)
    return friends_data, user_loc

