# This is a basic REST micro service example for python using the flask library
# Docs: http://flask.pocoo.org/docs/1.0/
import re

from flask import Flask, jsonify, request
from example_data import customers

app = Flask(__name__)


# -----------------------------------------------------
# Basic 'customer' example for REST like resource paths
# -----------------------------------------------------


@app.route('/', methods=['GET'])
def index():
    return 'DPNB Microservice Demonstrator'

# Get a list of resources
@app.route('/customers', methods=['GET'])
def find_all_customers():
    return jsonify(list(customers.values()))


# Get a single resource
@app.route('/customers/<customer_id>', methods=['GET'])
def find_single_customer(customer_id):
    if customer_id not in customers:
        return '', 404
    return jsonify(customers[customer_id])


# Update a resource
@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if customer_id in customers:

        for key in request.json:
            customers[customer_id][key] = request.json[key]

        return jsonify(customers[customer_id])
    else:
        return 'not found', 404


# Delete a resource
@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        return 'okay', 200
    else:
        return 'not found', 404


# Save a resource
def find_last_key(customers):
    last_key = 0
    for customer in customers:
        m = re.search(r'customer_(\d+)', customer)
        if int(m.group(1)) > last_key:
            last_key = int(m.group(1))

    return last_key


@app.route('/customers', methods=['POST'])
def save_customer():
    customer_id = 'customer_{0}'.format(find_last_key(customers) + 1)
    customers[customer_id] = request.json
    customers[customer_id]['customer_id'] = customer_id

    return jsonify(customers[customer_id])


# -----------------------------------------------------
# Basic example for an async method call
# -----------------------------------------------------

@app.route('/do_your_magic', methods=['POST'])
def do_magic():
    data = request.json

    print(data)
    # process the data

    response_object = {
        'list_of_magic_things': [
            {'id': 'magic_thing_1'},
            {'id': 'magic_thing_2'},
            {'id': 'magic_thing_3'},
        ]
    }

    success = True

    # return status code and response
    if success:
        return jsonify(response_object), 200
    else:
        print('Uuuups something broke')
        return 'Magic Error Message', 500
