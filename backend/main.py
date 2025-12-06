from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from database.connection import init_database

load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)

    init_database(app)
    from database.models import User
    from database.models import Waitingline
    from database.models import Sessions

    from routes.status import status_bp
    app.register_blueprint(status_bp)

    from routes.auth.reset import reset_bp
    app.register_blueprint(reset_bp)

    from routes.auth.recover import recover_bp
    app.register_blueprint(recover_bp)

    from routes.auth.register import register_bp
    app.register_blueprint(register_bp)

    from routes.auth.singin import singin_bp
    app.register_blueprint(singin_bp)

    from routes.auth.me import me_route
    app.register_blueprint(me_route)

    from routes.waitingline import waitingline_bp
    app.register_blueprint(waitingline_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
