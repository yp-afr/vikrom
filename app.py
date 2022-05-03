from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TjWnDSvc5$!A%D*G-KaNdRgUkXp2s5v8y/B?E(H+MbQeShVmYq3t6w9z$C&F)J@N'

    from views import views

    app.register_blueprint(views)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=82, debug=True)