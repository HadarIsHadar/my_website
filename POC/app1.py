from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Main Application</title>
            <script>
                function sendAdRequest() {
                    fetch('/get_ad')
                        .then(response => response.text())
                        .then(data => {
                            document.getElementById('ad-container').innerHTML = data;
                        })
                        .catch(error => {
                            alert('Error: ' + error);
                        });
                }
            </script>
        </head>
        <body>
            <h1>Main Application</h1>
            <button onclick="sendAdRequest()">Get Ad</button>
            <div id="ad-container"></div>
        </body>
        </html>
    '''

@app.route('/get_ad')
def get_ad():
    try:
        # Replace with the actual URL of your second domain
        response = requests.get('http://127.0.0.1:5001/ad')
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
