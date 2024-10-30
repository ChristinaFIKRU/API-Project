from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (a dictionary as a simple database substitute)
items = {}

#Add
@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item_id = data['item_id']
    item_name = data['item_name']
    if item_id in items:
        return jsonify({'error': 'Item already exists'}), 400
    else:
        items[item_id] = {"item_id": item_id,"name": item_name}
        return jsonify({'message': 'Item added successfully'}), 201
#Delete

#Update

#Get
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error":"Item not found"}), 401
        
        
# Run the application
if __name__ == '__main__':
    app.run(port=8000, debug=True)
