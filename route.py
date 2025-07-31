from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# basic route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/items')
def resources():
    return render_template('items.html')

@app.route('/builds')
def builds():
    return render_template('builds.html')

@app.route('/keybinds')
def keybinds():
    return render_template('keybinds.html')

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)