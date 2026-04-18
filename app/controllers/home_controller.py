from flask import Blueprint, render_template

from app.models.developer import Developer


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    developer = Developer(
        name="Alex Carter",
        role="Full Stack Python Developer",
        location="Lima, Peru",
        about=(
            "Developer enfocado en aplicaciones web con Python, Flask y AWS. "
            "Disfruta construir productos mantenibles, claros y listos para escalar."
        ),
        skills=["Python", "Flask", "AWS", "SQLAlchemy", "Docker"],
        experience_years=5,
        email="alex.carter.dev@example.com",
        github="https://github.com/alexcarterdev",
    )
    return render_template("index.html", developer=developer)
