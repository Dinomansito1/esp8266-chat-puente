from flask import Flask, request

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt', '')

    # Aquí puedes procesar el texto que mande el ESP8266
    # De momento, devolveremos un eco de prueba corto para el LCD
    respuesta = f"Hola! Dijiste: {prompt}"

    return respuesta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)