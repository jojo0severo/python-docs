from pydantic import BaseModel, EmailStr, Field, constr


class Dog(BaseModel):
    name: constr(max_length=8)
    age = Field(default=1)
    email: EmailStr = Field(..., alias="email_address")
    owner: str | None = None


dog = Dog(name="Fido", age=2, email_address="fido@dog.com", owner="Bob")
print(dog)
print()

# invalid_name = Dog(name="Fido123456789", age=2, email_address="fido@dog.com", owner="Bob")
# print(invalid_name)
# print()

# invalid_email = Dog(name="Fido", age=2, email_address="fido@dog", owner="Bob")
# print(invalid_email)
# print()

# invalid_owner = Dog(name="Fido", age=2, email_address="fido@dog.com", owner=123)
# print(invalid_owner)
# print()
