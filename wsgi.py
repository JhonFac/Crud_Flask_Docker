from flask import jsonify

from app import create_app

app = create_app()

if __name__ == "__main__":
    for rule in app.url_map.iter_rules():
        print(f"Ruta: {rule.rule}, Métodos: {','.join(rule.methods)}")
    app.run(host="0.0.0.0", port=80, debug=True)
