import json

from app.data import CV_DATA


def register_commands(app):
    @app.cli.command("cv-info")
    def show_cv_info() -> None:
        """Displays the CV data in the console.."""
        print(json.dumps(CV_DATA))
