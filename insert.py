from main import session, Department, Person

d = Department(name="Design")
p1 = Person(name="Tom", department=d)
p2 = Person(name="Jack", department=d)

session.add(d)
session.add(p1)
session.add(p2)

session.commit()

