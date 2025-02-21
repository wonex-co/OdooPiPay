# Sandbox URL https://sandbox.minepi.com/mobile-app-ui/app/the-insult-o-matic

from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_cors import CORS
import simplejson as json
import requests
import random
import variables

apikey = variables.apikey

header = {
    'Authorization' : "Key {}".format(apikey)
}

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Configure CORS
CORS(app, resources={r"/*": {"origins": ["https://app-cdn.minepi.com", "https://educontentpipay.azurewebsites.net"]}})

Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_content')
def get_content():
    with open('content.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    return random.choice(content)

@app.route('/validation-key.txt')
def get_key():
    with open('validation-key.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    return content[0]

@app.route('/back')
def back():
    return render_template('back.html')

@app.route('/payment/approve', methods=['POST'])
def approve():
    # Build the header for user authentication
    accessToken = request.form.get('accessToken')
    userheader = {
        'Authorization' : f"Bearer {accessToken}"
    }
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/approve"
    response = requests.post(approveurl, headers = header)
    userurl = "https://api.minepi.com/v2/me"
    userresponse = requests.get(userurl, headers = userheader)
    userjson = json.loads(userresponse.text)
    return(response.text)

@app.route('/payment/complete', methods=['POST'])
def complete():   
    # Build the header for user authentication
    accessToken = request.form.get('accessToken')
    userheader = {
        'Authorization' : f"Bearer {accessToken}"
    }
    paymentId = request.form.get('paymentId')
    txid = request.form.get('txid')
    userurl = "https://api.minepi.com/v2/me"
    userresponse = requests.get(userurl, headers = userheader)
    data = {'txid': txid}
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/complete"
    response = requests.post(approveurl, headers = header, data = data)
    return(response.text)

@app.route('/payment/cancel', methods=['POST'])
def cancel():    
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
    response = requests.post(approveurl, headers = header)
    return(response.text)

@app.route('/payment/error', methods=['POST'])
def error():    
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
    response = requests.post(approveurl, headers = header)
    return(response.text)

@app.route('/me', methods=['POST'])
def getme():
    userurl = "https://api.minepi.com/v2/me"
    response = requests.post(userurl, headers = header)
    return(response.text)

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/terms_of_service')
def terms_of_service():
    return render_template('terms_of_service.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
