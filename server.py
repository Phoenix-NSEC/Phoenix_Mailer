
from mail_sender import sendZohoMail
from csv_praser import csv_praser
import os
import json
import time
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

subject = 'BRAIN FREEZE | PHOENIX'
dataFile = './templates/response.html'


@app.route('/apiV1/upload', methods=['POST'])
def uploadData():
    # htmlFile = './templates/brain_freeze_welcome.html'
    htmlFile = './templates/brain_freeze_2nd_rnd.html'
    data = request.files['csv']
    jsonData = csv_praser(data.filename, data)
    total_count = len(json.loads(jsonData))
    count = 0
    for k, v in json.loads(jsonData).items():
        count = count + sendZohoMail(k, subject, v,htmlFile)
        time.sleep(10)
    sendZohoMail(json.dumps({'status': 'success', 'total_entry': total_count, 'sent_to': count}), 'mailing result','info@phoenixnsec.in',dataFile)
    return make_response(jsonify({'status': 'success', 'total_entry': total_count, 'sent_to': count}), 200)


if __name__ == "__main__":
    app.run()
