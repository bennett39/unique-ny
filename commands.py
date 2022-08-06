import sys
import csv
from models import CensusBlock, Street, SubwayStation

def process_option(option, db):
    options = {
        'stations': (
            'data/data-subwaystations.csv',
            SubwayStation,
        ),
        'streets': (
            'data/data-streets.csv',
            Street,
        ),
        'blocks': (
            'data/data-censusblocks.csv',
            CensusBlock,
        ),
    }
    selected = options.get(option)

    if not selected:
        return f'Choose a valid option: {[o for o in options]}'

    path, model = selected
    result = load_data(path, db, model)

    return f'Ran {option} with result: {result}'

def load_data(path, db, model):
    if db.session.query(model).first():
        return 'Data already exists for this model!'

    count = 0
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            attrs = {k: v for k, v in row.items() if k not in {'st_astext', 'blkid'}}
            obj = model(geom=row['st_astext'], **attrs)
            if 'blkid' in row:
                obj.block_id = row['blkid']

            db.session.add(obj)
            count += 1
        db.session.commit()

    return f'Updated {count} records'
