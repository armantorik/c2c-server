from flask import Flask

app = Flask(__name__)

def getHello():
    @app.route('/')
    def helloC2C():
       return 'Hello C2C!'

    app.run()