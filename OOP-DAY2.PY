class Instagram:
    def __init__(self,title, description,creator_name,location):    
        self.title = title
        self.description = description
        self.likes = 0
        self.creator_name = creator_name
        self.location = location
        self.comments = []
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def display_creator_name(self):
        print("The creator name is ",self.creator_name)
    def display_location(self):
        print("The location is ",self.location)
    def display_comment(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("The comments are ")
            for comment in self.comments:
                print("-",comment)
    def add_comments(self,comment):
        self.comments.append(comment)
    def delete_last_comment(self):
        temp_comment=self.comments.pop()
        print("The last comment is deleted ",temp_comment)


'''TASK'''

       
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


issued_book = IssuedBook(
    "Python Programming",
    "John Smith",
    "Uday",
    "04-02-2026"
)

issued_book.display_issued_book_details()
