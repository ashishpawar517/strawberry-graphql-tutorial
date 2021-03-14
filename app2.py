# creating a schema

# graphql schema is used to define the structure of the data that client
# can query
import typing
import strawberry 
import dataclasses

@strawberry.type
class Book:
    title:str
    author:str

# creating a query books that will return list of zero or more
# books 


# strawberry can work with any times of data rest,db
# here we are creating a hardcoded data


db = {
    "1":Book(title = 'JAVA PRO 8',author = "JVM Gosling"),
    "2":Book(title = 'PYTHON magic ',author = 'anaconda'),
    "3":Book(title = 'colorful java', author = 'gosling'),
}


def get_books():
    return list(db.values())

def get_book_by_id(root,n:strawberry.ID) -> typing.Optional[Book]:
    return db.get(n)

@strawberry.type
class Query:
    # books:typing.List(Book)
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    get_books_by_id : typing.Optional[Book] = strawberry.field(resolver = get_book_by_id)

@strawberry.input
class BookInput:
    title:str
    author:str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self,info,title:str,author:str) -> Book:
        last = int(list(db.keys())[-1])
        last += 1
        db[str(last)] = Book(title,author)
        return Book(title,author)

schema = strawberry.Schema(query=Query,mutation=Mutation)