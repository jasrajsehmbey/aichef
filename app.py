from flask import Flask, jsonify,render_template, request

message = ""
with open("output.txt","r") as file:
    message = file.read()
print(message)
file.close()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/api/output', methods=['GET'])
def get_output_data():
    data = {'message': message}
    return jsonify(data)

@app.route('/', methods=['POST'])
def output():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path) #image 
    print(request.form['flavour']) #flavour 
    # store recipe in generated 
    generated  = message
    return render_template('index.html', recipe = generated)


if __name__ == '__main__':
    app.run(debug=True)
