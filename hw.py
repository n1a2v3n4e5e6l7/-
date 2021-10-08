from flask import Flask,jsonify, request

app = Flask(__name__)

list = [
    {
        'id': 1,
        'Name': u'Sakti',
        'Contact': u'9099941608', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Hiya',
        'Contact': u'9141074749', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': list[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    list.append(task)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : list
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)