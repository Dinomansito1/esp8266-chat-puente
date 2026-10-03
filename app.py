from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    # Aquí llamas a tu lógica de ChatGPT / IA para obtener el texto plano de respuesta:
    respuesta_ia = "Hola, esta es la respuesta de prueba" # (Reemplaza esto por la respuesta real de tu IA)
    
    # DEVUELVE SOLO EL TEXTO PLANO (o un JSON limpio, pero texto plano es más fácil de leer en la LCD):
    return respuesta_ia, 200, {'Content-Type': 'text/plain; charset=utf-8'}
