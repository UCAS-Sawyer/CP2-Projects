from faker import Faker

fake = Faker()

# Generate a person description
person_description = fake.hobby()

print(person_description)
