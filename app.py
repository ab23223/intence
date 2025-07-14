from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import os, json
from datetime import datetime

app = Flask(__name__, static_folder='static')
ALBUMS_FILE = 'albums.json'
ALBUM_FOLDER = os.path.join('static', 'albums')
TEMPLATE_FILE = os.path.join('templates', 'album_template.html')

# -------------------------
# Combined Flask App
# -------------------------

@app.route('/')
def homepage():
    # Dynamically load all HTML files in albums folder
    album_files = sorted(
        [f for f in os.listdir(ALBUM_FOLDER) if f.endswith('.html')],
        reverse=True
    )
    return render_template('index.html', album_files=album_files)

@app.route('/albums/<path:filename>')
def serve_album(filename):
    return send_from_directory(ALBUM_FOLDER, filename)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/generate', methods=['POST'])
def generate_album():
    data = request.json
    name = data['album_name']
    desc = data['album_desc']
    urls = data['image_urls']
    date = datetime.now().strftime('%Y-%m-%d')

    with open(TEMPLATE_FILE) as f:
        html = f.read()

    image_list = ",\n".join(f'"{url}"' for url in urls)
    html = html.replace('{{title}}', name).replace('{{desc}}', desc).replace('{{images}}', image_list)

    filename = f"{name.replace(' ', '_')}_{date}.html"
    filepath = os.path.join(ALBUM_FOLDER, filename)

    os.makedirs(ALBUM_FOLDER, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(html)

    return jsonify({'success': True, 'preview_url': f'/albums/{filename}', 'filename': filename})

@app.route('/publish', methods=['POST'])
def publish_album():
    data = request.json
    with open(ALBUMS_FILE, 'r+') as f:
        albums = json.load(f)
        albums.insert(0, data)
        f.seek(0)
        json.dump(albums, f, indent=2)
        f.truncate()
    return jsonify({'success': True})

# -------------------------
# Additional Routes (converted from Bottle)
# -------------------------

@app.route('/category-sports')
def category_sports():
    return render_template('category-sports.html')

@app.route('/category-automotive')
def category_automotive():
    return render_template('category-automotive.html')

@app.route('/Training-15-05')
def training_1505():
    return render_template('Training-15-05.html')

@app.route('/Training-19-05')
def training_1905():
    return render_template('Training-19-05.html')

@app.route('/Choir-11-06')
def choir_1106():
    return render_template('Choir-11-06.html')

@app.route('/First-XV-14-06')
def first_xv_1406():
    return render_template('First-XV-14-06.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/googlec84cb0ca6911faab.html')
def google_verification():
    return render_template('googlec84cb0ca6911faab.html')

@app.route('/sitemap.xml')
def sitemap():
    return Response(render_template('sitemap.xml'), mimetype='application/xml')

# -------------------------
# Run Server
# -------------------------

if __name__ == '__main__':
    app.run(debug=True)
