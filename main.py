from flask import Flask, render_template
import json

app = Flask(__name__)

def load_gift_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    gifts = load_gift_data()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
