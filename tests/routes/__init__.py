from app.routes.routes import set_routes


def test_set_routes():
    app = Flask(__name__)
    set_routes(app)
    client = app.test_client()
    response = client.get("/example")
    assert response.status_code == 200
