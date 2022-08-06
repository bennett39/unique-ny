# Unique New York

Explore demographics across neighborhoods & subway lines.

## Technologies

Flask, SQLAlchemy, Flask-Migrate (Alembic), Postgres, PostGIS, GeoAlchemy

## Get Started

1. Copy `.env.example` to `.env`
1. Run a local instance of Postgres (sorry I haven't done docker-compose yet)
1. Start a local environment & run `pip install -r requirements.txt`
1. Run the migrations with `flask db upgrade`
1. Start the development server with `flask --debug run --port 8080`
1. Check out http://localhost:8080/ to see if it's working

## Populate the database

There are better ways to load data into the database, but this is the quick-n-dirty version.

Once you've run the data load once, these routes will stop working with "Data already exists for this model!"

1. Visit http://localhost:8080/data/streets
1. Visit http://localhost:8080/data/blocks
1. Visit http://localhost:8080/data/stations
