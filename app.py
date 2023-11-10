from flask import Flask, jsonify

message = ""
with open("C:\\Users\\jasra\\OneDrive\\Desktop\\mmdp_project\\output.txt","r") as file:
    message = file.read()
print(message)
file.close()
app = Flask(__name__)

@app.route('/api/output', methods=['GET'])
def get_output_data():
    data = {'message': message}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
