from flask import Flask

from app.routes.routes import set_routes

app = Flask(__name__)
set_routes(app)

if __name__ == "__main__":
    for rule in app.url_map.iter_rules():
        print(f"Ruta: {rule.rule}, Métodos: {','.join(rule.methods)}")
    app.run()
