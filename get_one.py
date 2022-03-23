from main import session, Department, Person

first_person = session.query(Person).get(1)
first_department = session.query(Department).get(1)

print(first_person)
print(first_department)
