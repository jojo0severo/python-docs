from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name,
            self.fullname,
            self.password,
        )


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", backref=backref("addresses", order_by=id))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name="ed", fullname="Ed Jones", password="edspassword")
session.add(ed_user)
session.commit()

our_user = session.query(User).filter_by(name="ed").first()
print(our_user)
