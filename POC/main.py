from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Hello World</title>
            <script>
                function sendDnsRequest() {
                    fetch('/resolve?hostname=example.com')
                        .then(response => response.json())
                        .then(data => {
                            alert('DNS Response: ' + data.ip);
                        })
                        .catch(error => {
                            alert('Error: ' + error);
                        });
                }
            </script>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <button onclick="sendDnsRequest()">Click Me!</button>
        </body>
        </html>
    '''

@app.route('/resolve')
def resolve_hostname():
    hostname = request.args.get('hostname', 'example.com')
    try:
        ip_address = socket.gethostbyname(hostname)
        return jsonify({'ip': ip_address})
    except socket.error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
