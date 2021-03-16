from fae.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def model_to_dict(row):
    if row is None:
        return None

    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)

    return d