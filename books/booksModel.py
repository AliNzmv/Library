from msilib.schema import Error
import sqlite3

#from soupsieve import select

database=sqlite3.Connection("../books/booksDB.db",check_same_thread=False)
cursor=database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books_table(isbn TEXT PRIMARY KEY, title TEXT,author TEXT, price INTEGER, pages INTEGER) ")
database.commit()

#=====================================================class for exceptions=================================
class Error(Exception):
    #base for exceptions
    pass
class valueLenghError(Error):
    #exception for lengh 
    pass
class valueMinError(Error):
    #Exception for minimum of a value
    pass
#-------------------------------------------book class----------------------------------------------------------------
class book:
    def __init__(self,isbn,title,author,price,pages):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
        cursor.execute("INSERT INTO books_table VALUES(?,?,?,?,?)",(isbn,title,author,price,pages))
        database.commit()


#---------------------------------------------find books------------------------------------------------------------
    @classmethod
    def find_book(cls,isbn):
        select_books=list(cursor.execute("SELECT * FROM books_table WHERE isbn=?",(isbn,)))
        try:
            if len(select_books)==0 :
                raise valueLenghError()
            else:
                return list(select_books)
        except valueLenghError:
            #error code -1
            record=-1
            return record

#--------------------------------------------list books------------------------------------------------------------------
    @classmethod
    def list_books(cls):
        books=list(cursor.execute("SELECT * FROM books_table"))
        return books


#--------------------------------------------------add books------------------------------------------------------------
    @classmethod
    def add_book(cls,isbn,title,author,price,pages):
        try:
            nbook=book(isbn,title,author,price,pages)
        except sqlite3.IntegrityError:
            #error code 2
            result=2
            return result
        except valueLenghError:
            result=1
            return result
        except valueMinError:
            result=3
            return result


#--------------------------------------------------delete book--------------------------------------------------
    @classmethod
    def delete_book(cls,isbn):
        del_book=cursor.execute("DELETE FROM books_table WHERE isbn=?",(isbn,))
        try:
            if del_book.rowcount==0 :
                raise Exception()
            database.commit()
        except :
            #error code -1
            return -1


#------------------------------------------------update book--------------------------------------------------------
    @classmethod
    def update_book(cls,isbn,title,author,price,pages):
        cursor.execute("Update books_table SET title=? WHERE isbn=?"(title,isbn))
        cursor.execute("Update books_table SET author=? WHERE isbn=?"(author,isbn))
        cursor.execute("Update books_table SET price=? WHERE isbn=?"(price,isbn))
        cursor.execute("Update books_table SET pages=? WHERE isbn=?"(pages,isbn))


        database.commit()





#---------------------------------------------------getter & setter for isbn------------------------------------------
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self,isbn2):
        if len(isbn2)!=8:
            raise valueLenghError()
        else:
            self._isbn=isbn2



#----------------------------------------------setter & getter for price----------------------
    @property
    def price(self):
        return self.p
    @price.setter
    def price(self,value):
        if value<0:
            raise valueMinError()
        else:
            self.p=value



    
#================================================================================================
