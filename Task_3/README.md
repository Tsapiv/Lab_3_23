Twitter Friends Map
==========================
Aim of this project is to let user see on the map location some Twitter user and his/her friend.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Prerequisites
That're things you need to install to get started

    python -m pip install folium
    python -m pip install geopy
    python -m pip install bs4
    python -m pip install flask
### Installing

    $ git clone https://github.com/Tsapiv/Lab_3_23.git
### Running
This program is adapted to be run on `pythonanywhere` and currently it is running from server. You can check it out by this link: http://tsapivv.pythonanywhere.com/
So that everything worked correctly in a form field enter the name (or better screen name) of person you'd like to find. If you want 
to find somebody else, just click on the button `Let's find somebody else!`<br>
Or you may want to run this program locally. To do this you must run `app.py`. This project uses libs such as `folium` to draw the map, `geopy` to find locations, `bs4` to edit `html` file (to make 
a button for navigation between the pages) and flask to run it as web-application.
### Contributing
* Sometimes, there can occur some issues with `geopy` or `pythonanywhere`, just ignore it.
* Don't do more than 15 requests in a row, because Twitter API has a limitations
* If you see blue screen, just scroll back because you're obviously looking into the ocean. 
### Authors
* Tsapiv Volodymyr
