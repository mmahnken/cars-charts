"""Models and database functions for cars database."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# -------------------------------------------------------------------
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Provide useful output when printing."""

        return "<Brand {name} brand_id={b_id}>".format(name=self.name,
                                                       b_id=self.brand_id)


class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    model_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.String(5), db.ForeignKey('brands.brand_id'),
                         nullable=False)
    name = db.Column(db.String(50), nullable=False)

    brand = db.relationship("Brand", backref="models")

    def __repr__(self):
        """Provide useful output when printing."""

        return "<Model {yr} {name} model_id={m_id}>".format(yr=self.year,
                                                            name=self.name,
                                                            m_id=self.model_id)

# End part 1
# -------------------------------------------------------------------
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

def example_data():
    b1 = Brand(brand_id="meg", name="Megolet", headquarters="Oakland", founded=2017)
    b2 = Brand(brand_id="kath", name="Kathoyota", headquarters="SF", founded=3011)

    m1 = Model(year=2017, name="Codette", brand=b1)
    m2 = Model(year=3012, name="Kamry", brand=b2)
    db.session.add_all([b1, b2, m1, m2])
    db.session.commit()


def connect_to_db(app, db_uri='postgres:///cars'):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
