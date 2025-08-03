from flask import Flask, jsonify
import os
from datetime import date

app = Flask(__name__)

# Przykładowa funkcja zwracająca najbliższy dostępny termin
def get_next_available_date(staff_id):
    return {
        "staff_id": staff_id,
        "next_available_date": date.today().isoformat()
    }

@app.route("/")
def index():
    return "<h1>Witaj! Serwis działa.</h1>"

@app.route("/next-available")
def next_available():
    barber_ids = {
        "Jedras": 2808131,
        "Kubson": 2808182,
        "Igor": 2850589
    }

    data = {
        name: get_next_available_date(staff_id)
        for name, staff_id in barber_ids.items()
    }

    return jsonify(data)

# ⬇️ KLUCZOWE!
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render ustawia PORT jako zmienną środowiskową
    app.run(host="0.0.0.0", port=port)
