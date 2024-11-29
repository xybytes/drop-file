import pickle
import json
import sys
from flask import Flask, request, jsonify

# Carica il modello
model_path = "./model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Crea l'app Flask
app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    try:
        # Ottieni i dati dalla richiesta
        data = request.get_json()
        inputs = data.get("data", [])
        
        # Effettua il prediction
        predictions = model.predict(inputs)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)