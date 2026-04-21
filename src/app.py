#'/api/v1/details'
#'/api/v1/healthz'

from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        "time": datetime.date.today().strftime("%B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "ahora si me veo!",
        'deploy_on': 'kubernetes',
        'env': 'dev',
        'app_name': 'python-app-2'
    })


@app.route('/api/v1/healthz')

def healthz():
    return jsonify({"status": "up"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")