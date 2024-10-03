from flask import Flask, send_file, jsonify
import random
import string
import socket
import time
import dns.resolver

app = Flask(__name__)

@app.route('/ad')
def ad():
    tracking_pixel_url = 'http://127.0.0.1:5001/tracking_pixel'
    return f'''
        <div style="border: 2px solid #ccc; padding: 10px; background-color: #f9f9f9;">
            <h2>Ad Content</h2>
            <p>This is an advertisement from Domain 2!</p>
            <img src="{tracking_pixel_url}" style="display:none;" alt="Tracking Pixel"/>
        </div>
    '''
@app.route('/tracking_pixel')
def tracking_pixel():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    hostname = f"{random_string}.example.com"  # Adjust this as needed

    try:
        # Use dnspython to perform a recursive DNS query
        resolver = dns.resolver.Resolver()
        answer = resolver.resolve(hostname, 'A')  # Query for an 'A' record
        ip_address = answer[0].address
        print(f"Resolved IP for {hostname}: {ip_address}")
    except dns.resolver.NoAnswer:
        print(f"No answer for {hostname}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain does not exist: {hostname}")
    except Exception as e:
        print(f"DNS Resolution Error for {hostname}: {e}")

    return send_file('1x1_pixel.png', mimetype='image/png')

# @app.route('/tracking_pixel')
# def tracking_pixel():
#     # Generate a random string for the hostname
#     random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
#     hostname = f"{random_string}.example.com"  # Change "example.com" to your domain
#
#     # Simulate a DNS request (this won't actually send a DNS request, just an example)
#     try:
#         print("before")
#         print(hostname)
#         ip_address = socket.gethostbyname(hostname)
#         print("after")
#         print(f"Resolved IP for {hostname}: {ip_address}")
#     except socket.error as e:
#         print(f"DNS Resolution Error for {hostname}: {e}")
#
#     # Return a 1x1 pixel image (you can use an actual image file if you want)
#     return send_file('1x1_pixel.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
