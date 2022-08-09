from app import db
from sqlalchemy.dialects.postgresql import JSON
from geoalchemy2 import Geometry


class SubwayStation(db.Model):
    __tablename__ = 'subwaystation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    routes = db.Column(db.String(140), nullable=False)
    geom = db.Column(Geometry('POINT', srid=26918))

class Street(db.Model):
    __tablename__ = 'street'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    geom = db.Column(Geometry('MULTILINESTRING', srid=26918))

class CensusBlock(db.Model):
    __tablename__ = 'censusblock'

    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.String(255), unique=True, nullable=False)
    geom = db.Column(Geometry('MULTIPOLYGON', srid=26918))
    boroname = db.Column(db.String(140), nullable=False)
    popn_total = db.Column(db.Integer)
    popn_white = db.Column(db.Integer)
    popn_black = db.Column(db.Integer)
    popn_asian = db.Column(db.Integer)
