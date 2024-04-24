from flask import Flask,jsonify,request


app = Flask(__name__)
dict = {"name":"Maveen","age":20,"marks":70}

@app.route('/modelApi/',methods=['GET'])
def index():
    cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age' ]
    query = {}
    for i in  cols:
         query[i] = request.args.get(i)
    if query:
        reponse = jsonify(query)
        return reponse

