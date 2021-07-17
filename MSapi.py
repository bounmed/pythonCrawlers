# -*- utf-8 -*-
from flask import Flask, request, jsonify
from MSSpider import *
app = Flask(__name__)

@app.route('/msscholar/<query>', methods=['POST'])
def msspider(query):
    result = query
    spider = MicroScholar()
    result = spider.run(query)
    return result

if __name__ == "__main__":
    app.run(debug=True, port=8000)
