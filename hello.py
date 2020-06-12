#!/bin/python3
"""
flask http-server skeleton
"""
import sys
import netifaces as ni
from flask import Flask
from flask import jsonify
from flask import request

APP = Flask(__name__)

@APP.route('/somepath', methods=['GET', 'POST'])
def hello_world():
    """
    dummy request handler
    """
    try:
        val = request.get_json()
    except:
        return jsonify(results={'status':'fail'})
    print(val)
    return jsonify(results={'status': 'succ', 'input': val})

if __name__ == "__main__":
    IFNAME = sys.argv[1]
    PORT = int(sys.argv[2])
    IP = ni.ifaddresses(IFNAME)[ni.AF_INET][0]['addr']
    APP.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    APP.run(debug=True, host=IP, port=PORT)
