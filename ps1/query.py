from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Puppy, Shelter
import datetime

def diff_month(recent_date, old_date):
    return (recent_date.year - old_date.year) * 12 +  \
            recent_date.month - old_date.month

def get_age_by_month(date):
    return diff_month(datetime.date.today(), date)

def print_string_tuples(string_tuples):
    """Pretty prints a list of string tuples.
    
    Assumes every tuple has same length.
    """
    field_lengths = [max([len(x) for x in items])
            for items in zip(*string_tuples)]
    num_fields = len(string_tuples[0])
    fmt = ' | '.join(['%%%ds'] * num_fields) % tuple(field_lengths)
    for string_tuple in string_tuples:
        print(fmt % string_tuple)

if __name__ == "__main__":

    # Boiler-plate stuff
    engine=create_engine('sqlite:///puppyshelter.db')
    Base.metadata.bind=engine
    DBSession=sessionmaker(bind=engine)
    session=DBSession()

    # Get puppy names in reverse alphabetical order
    puppies = session.query(Puppy).order_by(Puppy.name.desc()).all()
    print('Puppies in reverse alphabetical order:')
    print(', '.join([puppy.name for puppy in puppies]))

    # Get puppies less than six months old
    six_months_ago = datetime.date(2015, 12, 1)
    puppies = session.query(Puppy).filter(Puppy.dateOfBirth >=
            six_months_ago).order_by(Puppy.dateOfBirth).all()
    print('Puppies less than six months old:')
    string_tuples = [(puppy.name, str(puppy.dateOfBirth))
            for puppy in puppies]
    print_string_tuples([('Puppy name', 'Date of Birth')] + string_tuples)

    # Get puppies by ascending weight
    puppies = session.query(Puppy).order_by(Puppy.weight)
    string_tuples = [(puppy.name, '%.2f' % puppy.weight)
            for puppy in puppies]
    print('All puppies by ascending weight')
    print_string_tuples([('Puppy name', 'Weight')] + string_tuples)

    # Get puppies grouped by shelter
    puppies = session.query(Puppy).order_by(Puppy.shelter_id)
    string_tuples = [(puppy.name, puppy.shelter.name)
            for puppy in puppies]
    print("Puppies by shelter:")
    print_string_tuples([('Puppy name', 'Shelter name')] + string_tuples)

    #session.query(Puppy).all()
    #session.query(Puppy).all()
    #foo = session.query(Puppy).all()
    #debug
    #foo = session.query(Puppy).all()
    #foo = session.query(Puppy).all()
    #foo
    #bar = foo[0]
    #bar
    #bar.id
    #foo = session.query(Puppy).all()
    #query = session.query(Puppy)
    #query.order_by?
    #query.order_by(name)
    #query.order_by('name')
    #query
    #query.all()
    #query.all()
    #[x.name for x in query.all()]
    #[x.name for x in query.order_by('name').all()]
    #[x.name for x in session.query(Puppy).all()]
    #[x.name for x in session.query(Puppy).all()]
    #[x.name for x in session.query(Puppy).order_by('name').all()]
    #' '.join([x.name for x in session.query(Puppy).order_by('name').all()])
    #' '.join([x.name for x in session.query(Puppy).distinct().order_by('name').all()])
    #query.order_by?
    #' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name).all()])
    #' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name.desc).all()])
    #' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name.desc()).all()])
    #query.select_from?
    #query.select_from?
    #' '.join([x.name for x in session.query(Puppy.name).distinct().order_by(Puppy.name.desc()).all()])
    #' '.join([x.name for x in session.query(Puppy.name).distinct().order_by(Puppy.name.desc()).all()])
    #history
    #history -f query.py
