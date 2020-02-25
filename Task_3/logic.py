import bs4
import friends
import geomarkers


def give_me_map(username):
    """
    :param username: str
    :return: ()
    Function take name of Twitter user and create html map
    with that person and some friends of that person on it
    """
    friends_loc, user_loc = friends.position_data(username)
    geomarkers.build_map(user_loc, friends_loc)


def add_button():
    """
    ()
    :return: ()
    Function adds button to html map and save it
    Button allows user to look for another Twitter's user
    """
    with open("/home/TsapivV/mysite/templates/map.html", encoding="utf-8") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, features="html.parser")
    new_button = soup.new_tag("button", type="button", onClick="window.location='/'")
    new_button["class"] = "btn btn-lg btn-block"
    new_button["style"] = "background-color: azure;\
                           font-size: 20px;\
                           font-weight: bold;\
                           border-color: aqua;\
                           border-width: 3px;\
                           color: #bd59d4;\
                           border-radius: 10px"
    new_button.append("Let's find somebody else!")
    soup.head.append(new_button)
    with open("/home/TsapivV/mysite/templates/map.html", "w", encoding="utf-8") as outf:
        outf.write(str(soup))
