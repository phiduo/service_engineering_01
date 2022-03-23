from main import session, Department, Person

all_persons = session.query(Person).all()
all_departments = session.query(Department).all()

print(all_persons)
print(all_departments)
