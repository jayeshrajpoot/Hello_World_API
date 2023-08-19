from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static')

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for the hello world messages
@app.route('/hello', methods=['GET'])
def hello_world():
    # Get the language query parameter from the request
    language = request.args.get('language')

    # Define the hello world messages for different languages
    messages = {
        'English': 'Hello World',
        'French': 'Bonjour le Monde',
        'Hindi': 'Namastey Sansar'
    }

    # Check if the requested language is in the messages dictionary
    if language in messages:
        return jsonify({'message': messages[language]})
    else:
        # Return an error message if the language is not supported
        return jsonify({'error_message': 'The requested language is not supported'}), 400

# Run the app on all available network interfaces at port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
