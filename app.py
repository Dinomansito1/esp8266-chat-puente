import os
from flask import Flask, request
from google import genai

app = Flask(__name__)

# Inicializa el cliente de Gemini (busca automáticamente la variable GEMINI_API_KEY en Render)
client = genai.Client()

@app.route('/chat', methods=['POST'])
def chat():
    # 1. Recibir los datos en JSON enviados por el ESP8266
    data = request.get_json()
    
    if not data or 'prompt' not in data:
        return "Error: No prompt", 400
    
    user_prompt = data['prompt']
    
    try:
        # 2. Consultar directamente al modelo Flash gratuito de Gemini
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
        )
        
        # Extraer el texto de la respuesta
        respuesta_ia = response.text
        
        # 3. Limpiar saltos de línea para que no rompan la pantalla LCD de 16x2
        respuesta_limpia = str(respuesta_ia).strip().replace('\n', ' ')

        # 4. Devolver estrictamente texto plano en crudo
        return respuesta_limpia, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
