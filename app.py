from flask import Flask, request, jsonify, render_template, redirect, url_for
from bson import ObjectId
from database import insert_item, update_item, delete_item, get_items, JSONEncoder
from datetime import datetime

app = Flask(__name__)
app.json_encoder = JSONEncoder

@app.route('/')
def home():
    items = get_items()
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', items=items, current_date=current_date)

@app.route('/items', methods=['GET'])
def get_all_items():
    items = get_items()
    return jsonify(items)

@app.route('/add_item', methods=['POST'])
def add_item_form():
    name = request.form['name']
    description = request.form['description']
    date = request.form['date']
    item = {"name": name, "description": description, "date": date}
    insert_result = insert_item(item)
    item['_id'] = str(insert_result.inserted_id)
    return redirect(url_for('home'))

@app.route('/items', methods=['POST'])
def add_item_api():
    item = request.json
    insert_result = insert_item(item)
    item['_id'] = str(insert_result.inserted_id)
    return jsonify(item), 201

@app.route('/update_item', methods=['POST'])
def update_item_form():
    item_id = request.form['_id']
    name = request.form['name']
    description = request.form['description']
    date = request.form['date']
    query = {"_id": ObjectId(item_id)}
    new_values = {"name": name, "description": description, "date": date}
    update_item(query, new_values)
    return redirect(url_for('home'))

@app.route('/items', methods=['PUT'])
def update_item_route():
    query = request.json.get("query")
    new_values = request.json.get("new_values")
    update_item(query, new_values)
    return jsonify({"status": "updated"})

@app.route('/delete_item', methods=['POST'])
def delete_item_form():
    item_id = request.form['_id']
    query = {"_id": ObjectId(item_id)}
    delete_item(query)
    return redirect(url_for('home'))

@app.route('/items', methods=['DELETE'])
def delete_item_route():
    query = request.json
    delete_item(query)
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)
