from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine('sqlite:///testDB.db', echo=True)

Base = declarative_base()


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department")


Base.metadata.create_all(engine)



Session = sessionmaker(engine)


with Session() as session:
    d = Department(name="Design")
    p1 = Person(name="Tom", department=d)
    p2 = Person(name="Jack", department=d)

    session.add(d)
    session.add(p1)
    session.add(p2)

    session.commit()

    session.query(Department).all()



# long: sqlite = 0-8 bytes, java = 8 bytes