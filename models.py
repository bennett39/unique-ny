from app import db
from sqlalchemy.dialects.postgresql import JSON


class SubwayLine(db.Model):
    __tablename__ = 'subwayline'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
