class BookStore:
	instances = 0

	def __init__(self, title, author):
		self.title = title
		self.author = author
	
	def bookInfo(self):
		print'Title: ', self.title
		print'Author: ', self.author
		
			
b1 = BookStore("Python ", "AuthorPy")
b2 = BookStore("Java " , "AuthorJava")
b1.bookInfo()
b2.bookInfo()


