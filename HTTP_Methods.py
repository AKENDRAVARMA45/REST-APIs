from flask import Flask, request, jsonify

_name

app = Flask(

data = [
{"name": "abc", "enrollment_number": 12345, "age": 19},
{"name": "pqr", "enrollment_number": 67890, "age": 20}

if

# GET
@app.route('/user', methods=['GET' ])
def get_user():
return jsonify(data)

name ' main_':
app.run(debug=True)