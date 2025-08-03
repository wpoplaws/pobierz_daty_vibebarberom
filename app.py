from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/next-slots')
def next_slots():
    # Przykładowe dane testowe - tu potem wstawimy dane z Altegio
    data = {
        "Jędras": "2025-08-05 12:00",
        "Kubson": "2025-08-05 13:30",
        "Igor": "2025-08-06 10:15"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()