from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine('sqlite:///testDB.db', echo=True)

Base = declarative_base()


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Department [id="{self.id}", name="{self.name}"]'


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department")

    def __repr__(self):
        return f'Person [id="{self.id}", name="{self.name}"]'


Base.metadata.create_all(engine)

session = Session(engine)




# long: sqlite = 0-8 bytes, java = 8 bytes
