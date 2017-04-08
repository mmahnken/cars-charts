from flask import Flask, render_template, jsonify
from model import connect_to_db, Model, db
from sqlalchemy import func

app = Flask(__name__)

@app.route("/")
def show_homepage():
    """Show the homepage."""
    return render_template("index.html")

@app.route("/models/all")
def show_all_models():
    """Show the models."""
    all_models = Model.query.all()
    return render_template("all_models.html", models=all_models)

@app.route("/brands/all")
def show_all_brands():
    """Show the brands."""
    # all_brands = Brand.query.all()
    return render_template("all_brands.html")

@app.route("/models_by_year.json")
def get_line_chart_json():
    results = db.session.query(func.count(Model.model_id), Model.year).group_by(Model.year).order_by(Model.year).all()
    model_counts = [ int(count) for count, year in results ]
    model_years = [ result[1] for result in results ]
    return jsonify({"counts": model_counts, "years": model_years})
    # return jsonify(counts=model_counts, years=model_years) # Alternative syntax

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")