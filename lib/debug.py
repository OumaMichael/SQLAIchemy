from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import Base, Speciality

if __name__ == '__main__':

    engine = create_engine('sqlite:///lib/db/clinic_test.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()