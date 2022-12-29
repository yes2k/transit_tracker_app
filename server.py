from flask import Flask
import requests
from xml.dom.minidom import parseString

app = Flask(__name__)

@app.route("/api/kitchener")
def getting_train_location():
    pass



