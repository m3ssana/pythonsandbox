from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Open the JSON file and load its contents
    with open('example.json', 'r') as f:
        data = json.load(f)

    # Pass the JSON data to the HTML template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
