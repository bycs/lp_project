from app import create_app


app = create_app()


def run_app():
    app.run()


if __name__ == "__main__":
    run_app()
