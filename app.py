from flask import Flask, request
from google import genai
import os
import traceback

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Intentar leer como JSON o texto plano por respaldo
        data = request.get_json(silent=True)
        if data and 'prompt' in data:
            user_message = data['prompt']
        else:
            user_message = request.data.decode('utf-8')
            
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message
        )
        return response.text, 200
        
    except Exception as e:
        error_trace = traceback.format_exc()
        print("Error detallado:", error_trace)
        return f"Excepcion: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
