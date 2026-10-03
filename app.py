from flask import Flask, request
# Importa aquí la librería de la IA que estés usando (ej. openai, google.generativeai, etc.)

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # 1. Obtener los datos JSON enviados por el ESP8266
    data = request.get_json()
    if not data or 'prompt' not in data:
        return "Error: No prompt provided", 400
    
    user_prompt = data['prompt']
    
    try:
        # 2. AQUÍ LLAMAS A TU IA (Ejemplo usando OpenAI o la que tengas configurada)
        # Asegúrate de pedirle respuestas cortas para que entren bien en la pantalla LCD.
        # system_prompt = "Responde de forma muy breve, en máximo 2 o 3 oraciones."
        
        # Ejemplo de respuesta simulada o real de tu IA:
        respuesta_ia = "Esta es la respuesta generada por la IA." 
        
        # Si usas la librería oficial de OpenAI o similar, sería algo así:
        # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_prompt}])
        # respuesta_ia = response.choices[0].message.content

        # 3. Limpiar saltos de línea extremos para que no rompan la LCD
        respuesta_limpia = respuesta_ia.strip().replace('\n', ' ')

        # 4. DEVOLVER ESTRICTAMENTE TEXTO PLANO (Cero HTML)
        return respuesta_limpia, 200, {'Content-Type': 'text/plain; charset=utf-8'}

    except Exception as e:
        return f"Error interno: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
