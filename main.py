from save_json import writeAJson
from database import Database
from model import BookModel

db = Database(database="Relatorio5", collection="Livros")
db.resetDatabase()
data = db.collection.find()

book = BookModel(db) #Inicializando CRUD Model

#CRUD

livro_id = book.create_book("Moby Dick", "Herman Melville") #Create Book

book1 = book.read_book_by_id(livro_id) #Read Book

book.update_book(livro_id, "Mobie Dick", "Herman Melville") #Update Book

book.delete_book(livro_id) #Delete Book


livro_id = book.create_book("1984", "George Orwell") #Create Book

book1 = book.read_book_by_id(livro_id) #Read Book

book.update_book(livro_id, "1984", "George Orwell") #Update Book

book.delete_book(livro_id) #Delete Book

