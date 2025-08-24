import csv
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load user data from the CSV file
def load_user_data():
    user_data = []
    with open('../data/user_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data.append(row)
    return user_data

# Simple logic for generating learning path recommendations
def recommend_path(user):
    current_state = user['current_state']
    learning_style = user['learning_style']

    # Example reinforcement learning-based recommendation logic
    if learning_style == 'visual':
        recommended_modules = ['Video Module 1', 'Video Module 2']
    elif learning_style == 'auditory':
        recommended_modules = ['Audio Module 1', 'Audio Module 2']
    elif current_state == 'advanced':
        recommended_modules = ['Advanced Module 1', 'Advanced Module 2']
    else:
        recommended_modules = ['Interactive Module 1', 'Interactive Module 2']
    
    return recommended_modules

@app.route('/api/recommend', methods=['POST'])
def recommend():
    user_data = load_user_data()
    user_id = request.json['user_id']
    
    # Find the user by ID
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    
    if user:
        recommendations = recommend_path(user)
        return jsonify(recommendations)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
