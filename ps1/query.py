history
%history
%%history
from sqlalchemy import create_engine; from sqlalchemy.orm import sessionmaker; from puppies import Base, Puppy, Shelter;
engine=create_engine('sqlite:///puppies.db');Base.metadata.bind=engine;DBSession=sessionmaker(bind=engine);session=DBSession();
session.query(Puppy).all()
session.query(Puppy).all()
foo = session.query(Puppy).all()
debug
foo = session.query(Puppy).all()
engine=create_engine('sqlite:///puppyshelter.db');Base.metadata.bind=engine;DBSession=sessionmaker(bind=engine);session=DBSession();
foo = session.query(Puppy).all()
foo
bar = foo[0]
bar
bar.id
foo = session.query(Puppy).all()
query = session.query(Puppy)
query.order_by?
query.order_by(name)
query.order_by('name')
query
query.all()
query.all()
[x.name for x in query.all()]
[x.name for x in query.order_by('name').all()]
[x.name for x in session.query(Puppy).all()]
[x.name for x in session.query(Puppy).all()]
[x.name for x in session.query(Puppy).order_by('name').all()]
' '.join([x.name for x in session.query(Puppy).order_by('name').all()])
' '.join([x.name for x in session.query(Puppy).distinct().order_by('name').all()])
query.order_by?
' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name).all()])
' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name.desc).all()])
' '.join([x.name for x in session.query(Puppy).distinct().order_by(Puppy.name.desc()).all()])
query.select_from?
query.select_from?
' '.join([x.name for x in session.query(Puppy.name).distinct().order_by(Puppy.name.desc()).all()])
' '.join([x.name for x in session.query(Puppy.name).distinct().order_by(Puppy.name.desc()).all()])
history
history -f query.py
