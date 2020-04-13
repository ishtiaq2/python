class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return self.title + ' by ' + self.author

    def __len__(self):
        return self.pages

    def __del_(self):
        print('A Book object {} has been deleted'.format(self))


book = Book('Python rocks', 'Ishtiaq', 300)

print(book)
print(len(book))
del(book)
print(book)