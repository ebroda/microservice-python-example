# microservice-python-example
A small example of a REST like microservice written in python

The example is based on the flask library. 
Documentation can be found under: http://flask.pocoo.org/docs/1.0/

It implements the basic REST routes for an example customer resource.

    GET / : Welcome Message
    GET /customers : Retrieve all customers
    GET /customers/<customer_id> : Retrieve a single customer resource
    PUT /customers/<customer_id> : Update a single customer resource
    DELETE /customers/<customer_id> : Delete a single customer resource
    POST /customers : Create a new customer resource
    
    POST /do_your_magic: Barebone example for a simple service
    POST /calculate_price: (Simple) example for a possible price calculation

Additionally there is a endpoint called "do_your_magic" as an barebone example on how to implement a simple service.

# Dockerfile
The example can be easily deployed and tested using docker.
Just install docker and execute the following commands.

    $ docker build . -t python-microservice-example
    $ docker run --name python-microservice-example_1 -d -p 5000:5000 python-microservice-example

After the docker container is up and running you will be able to access the microservice via HTTP calls.
Go to your browser and enter: http://localhost:5000/customers
You should now see a list of example customer resources.

I recommend to use POSTMAN (https://www.getpostman.com/) to test the other methods, like POST, PUT and DELETE
You will find a postman_collection.json file next to the other sources, that you can import into POSTMAN.
