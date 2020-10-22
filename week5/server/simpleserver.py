#!flask/bin/python
from flask import Flask
app = Flask(__name__,
            static_url_path='',
            static_folder='../')

if __name__ == '__main__' :
    app.run(debug= True)