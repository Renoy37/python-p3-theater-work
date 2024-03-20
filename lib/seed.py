import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Audition, Role

if __name__ == "__main__":
    engine = create_engine('sqlite:///theatre.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    john_doe_role = session.query(Role).filter_by(
        character_name='John Doe').first()
    if not john_doe_role:
        john_doe_role = Role(character_name='John Doe')

    jane_smith_role = session.query(Role).filter_by(
        character_name='Jane Smith').first()
    if not jane_smith_role:
        jane_smith_role = Role(character_name='Jane Smith')

    audition1 = Audition(actor="John", location="Kampala",
                         phone="123456789", hired=False, role=john_doe_role)
    audition2 = Audition(actor="Jane", location="Kampala",
                         phone="987654321", hired=False, role=jane_smith_role)

    session.add_all([audition1, audition2])

    session.commit()

    # audition_instance = session.query(Audition).first()
    # if audition_instance:
    #     role_instance = audition_instance.role  
    #     if role_instance:  
    #         role_instance.call_back()  
    #         session.commit()  
    #     else:
    #         print("No associated role found for this audition.")
    # else:
    #     print("No audition found in the database.")

    session.close()
