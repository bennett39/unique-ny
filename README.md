# Unique New York

Explore demographics across neighborhoods & subway lines. PostGIS & GeoAlchemy w/ Flask

## Technologies

Flask, SQLAlchemy, Flask-Migrate (Alembic), Postgres, PostGIS, GeoAlchemy

## Get Started

1. Copy `.env.example` to `.env`
1. Run a local instance of Postgres (sorry I haven't done docker-compose yet)
1. Start a local environment & run `pip install -r requirements.txt`
1. Run the migrations with `flask db upgrade`
1. Start the development server with `flask --debug run --port 8080`
