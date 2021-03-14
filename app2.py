# creating a schema

# graphql schema is used to define the structure of the data that client
# can query
import typing
import strawberry 

@strawberry.type
class Book:
    title:str
    author:str

# creating a query books that will return list of zero or more
# books 


# strawberry can work with any times of data rest,db
# here we are creating a hardcoded data

def get_books():
    return [
        Book(
            title = "The Great SQL - GraphQL",
            author = "F. Agr author ",
        )
    ]

@strawberry.type
class Query:
    # books:typing.List(Book)
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)