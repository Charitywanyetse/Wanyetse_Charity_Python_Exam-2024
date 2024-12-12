
###  question 5 (i)


class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
Book = Book( "title", "author", "pages")        
print(Book.title)  
print(Book.author) 
print(Book.pages)   
        
        
###   question 5 (ii)

###  derived class

class EBook:
    def __init__(self,format):
        self.format = format
EBook = EBook("format")        
print(EBook.format)        


###  question 5 (iii)

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
                
Book = Book( title = "Bleesed Day", author = "Gorreti Golden")        
print(Book.title)      ### this prints the name of the author and the book title
print(Book.author) 



###  question 5 (iv)


###  A class is a code that represents and categories something
###  forexample a class can be used to deffrietiate between cohorts
###  forexample cohort 3 and 4

###  An object is the feature of a class forexample for a car as the class , 
###  the brand and the color are the objects of the class car
