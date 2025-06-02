from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    json_path = os.path.join(app.root_path, 'data', 'inventory.json')
    with open(json_path) as f:
        inventory = json.load(f)
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)