# This is a basic REST micro service example for python using the flask library
# Docs: http://flask.pocoo.org/docs/1.0/

from flask import Flask, jsonify, request
from example_data import customers

app = Flask(__name__)


# -----------------------------------------------------
# Basic 'customer' example for REST like resource paths
# -----------------------------------------------------

# Get a list of resources
@app.route('/customers', methods=['GET'])
def find_all_customers():
    return jsonify(customers.values())


# Get a single resource
@app.route('/customers/<customer_id>', methods=['GET'])
def find_single_customer(customer_id):
    if not customer_id in customers:
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


# Save a resource
@app.route('/customers', methods=['POST'])
def save_customer():
    customer_id = 'customer_{0}'.format(len(customers.keys()) + 1)
    customers[customer_id] = request.json
    customers[customer_id]['customer_id'] = customer_id

    return jsonify(customers[customer_id])


# -----------------------------------------------------
# Basic example for an asyn method call
# -----------------------------------------------------

@app.route('/do_your_magic', methods=['POST'])
def do_magic():
    data = request.json

    print data
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
        print 'Uuuups something broke'
        return 'Magic Error Message', 500
