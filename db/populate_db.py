from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db import Adjectives, Base, Positive

engine = create_engine('sqlite:///happiness.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

adjectives = ['kind', 'loving', 'funny', 'happy', 'affectionate', 'ambitious', 'considerate',
              'generous', 'inventive', 'persistent', 'resourceful', 'sympathetic', 'witty']
              
positive = ['dogs', 'cats', 'puppies', 'kittens', 'sloths', 'parrots', 'hampsters', 'ferrets']

for item in adjectives:
    session = DBSession()
    new_adjective = Adjectives(adjective=item)
    session.add(new_adjective)
    session.commit()

for item in positive:
    session = DBSession()
    new_positive = Positive(category=item)
    session.add(new_positive)
    session.commit()

    

