from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    project_details = data.get('project_details')
    
    if not name or not email or not project_details:
        return jsonify({"error": "All fields are required"}), 400

    # Here you would save the data to a database or send it via email
    print(f"New project request from {name}: {project_details}")

    return jsonify({"message": "Request submitted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)