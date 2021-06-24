from flask import Flask
from flask_restplus import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/ping/<string:url>')
class Ping(Resource):
    def put(self, url):
        response = requests.get(url)
        return response.text
        

if __name__ == '__main__':
    app.run(debug=True)