from flask import Flask, jsonify, request
import google.generativeai as genai
import json
import os


app = Flask(__name__)
# Replace with your actual API key
genai.configure(api_key = os.getenv('API_KEY'))

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({"message": "Hello from Service B!"})

@app.route('/api/desc', methods=['POST'])
def getDescription():
    
    
    data = json.loads(request.json)
    print(data)

    desc = data.get('desc1')
    print(desc)
    
    #print(type(data))

    
    prompt = f"""
    
Give the one liner theme of following paragraph. The one liner should less than 25 charaters.
    
    Ensure the one liner is less than 25 characters. Give response in JSON. Key is desc and value is one liner.
    
    <p>{desc}</p>
    """

    #print(prompt)

    
    
    model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})
    response = model.generate_content([prompt])
    
    try:
        data = json.loads(response.text)
        print(data)
        
        # Ensure date is in correct format
        return jsonify(data), 200
    except json.JSONDecodeError:
        return {'error': 'Failed to parse expense data from image'}
    except KeyError:
        return {'error': 'Missing required fields in expense data'}
    except ValueError:
        return {'error': 'Invalid date or amount format'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)