from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Audition, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:/// theatre.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb
    ipdb.set_trace()

audition_instance = session.query(Audition).filter_by(id=1).first()

role_instance = audition_instance.role

if role_instance:
    role_instance.call_back()
    session.commit()
