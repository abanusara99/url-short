from app import app
from flask import render_template, request, redirect
import shortuuid

url_mapping = {}

@app.route('/')
def index():
    return render_template('urlpage.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('urlpage.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('urlpage.html', error="URL not found!")

def generate_short_url():
    return shortuuid.uuid()[:8]
