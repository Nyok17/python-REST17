from flask import Flask, jsonify, request

app = Flask(__name__)

#Routes
@app.route('/')
def home():
    return 'Hello world'

@app.route('/items', methods=['GET'])
def get_items():
    items = ['Apples', 'Banana', 'Cherry', 'Orange']
    return jsonify(items)

@app.route('/add_items', methods=['POST'])
def add_items():
    data = request.get_json()
    new_item = data.get('item')
    return jsonify({'message': f"Item '{new_item}' added sucesfully!"})

if __name__=="__main__":
    app.run(debug=True)