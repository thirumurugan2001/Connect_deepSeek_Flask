from flask import Flask, request, jsonify 
from flask_cors import CORS 
from  checker import * 
app = Flask(__name__)
CORS(app)

# This Route is used to the connect the Deepseek R1 Distill Llama-70b and implement the 3th tier.
@app.route('/deepseek', methods=['POST'])
def deepseek():
    try:
        data = request.get_json()
        response = deepSeekController(data)
        return {
            "data":response,
            "statusCode":200
        }
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400
        
# This is the main function in which the application runs.
if __name__ == "__main__":
    app.run(debug=True , port="8080",host="0.0.0.0")