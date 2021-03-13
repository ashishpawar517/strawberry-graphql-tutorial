import typing 
import dataclasses
import strawberry

@strawberry.type
class Person:
    first_name : str
    last_name : str
    age :int

    @strawberry.field
    def full_name(self,info) -> str:
        return f"{self.first_name} {self.last_name}"



@strawberry.type
class Company:
    name : str
    space : str


PEOPLE_DB = {"1":Person(first_name ="Patrick", last_name = "S",age = 21 )}

def resolve_person(root,info) -> Person:
    return Person(first_name = 'ninu', last_name= 'kinu', age = 22)

def resolve_person_by_id(root,id:strawberry.ID) -> typing.Optional[Person]:
    return PEOPLE_DB.get(id)


@strawberry.type
class Query:
    person : Person = strawberry.field(resolver= resolve_person,description="this is always returning same person")

    person_by_id :typing.Optional[Person] = strawberry.field(resolver=resolve_person_by_id,description = "get from people db")

    @strawberry.field
    def company(self,info) -> Company:
        return Company(name ="BAC",space = "BCA")

# input
@strawberry.input
class PersonInput:
    first_name: str
    last_name : str
    age : int

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_person(self,info,input:PersonInput) -> Person:
        return Person(**dataclasses.asdict(input))



schema = strawberry.Schema (query = Query,mutation=Mutation)
