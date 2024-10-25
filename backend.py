from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV data
data_path = 'data.csv'  # Adjust the path to your data.csv file if needed

# Check if the file exists
if not os.path.exists(data_path):
    raise FileNotFoundError(f"The file {data_path} does not exist.")

# Read the CSV file into a DataFrame
data = pd.read_csv(data_path)

@app.route('/')
def home():
    return "Welcome to the Vehicle Telematics Chatbot API!"

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('query')

    # Here you can implement your logic to find the relevant response
    # For demonstration, we will just return a simple response based on the input
    if user_input.lower() in ['bye', 'exit']:
        response_text = "Goodbye! Have a nice day!"
    else:
        # You can implement your logic to match user_input with your data
        # For now, we'll just return the first row of the dataframe as an example
        response_text = "I received your question: " + user_input

    # Example of how to extract some relevant information from the DataFrame
    # This part should be customized based on your specific needs
    if user_input in data['SomeColumnName'].values:  # Replace 'SomeColumnName' with your actual column name
        response_text = "Here is the information from the data: " + data[data['SomeColumnName'] == user_input].to_string()

    return jsonify({'relevant_text': response_text})

if __name__ == '__main__':
    app.run(debug=True)
