class Instagram:
    def __init__(self,title, description):  
        self.title = title
        self.description = description
        self.likes = 0
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


reel1=Instagram("dancing","dancing with friends")
# 0
reel1.disliked() #0
reel1.liked() #1




reel2=Instagram("finance minister conference","finance minister conference with friends")
reel1.liked() #2
# 0
reel2.liked() #1
reel1.disliked() #1
reel1.display_likes()
reel2.display_likes()


print(id(reel1))
print(id(reel2))


'''TASK'''



class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []  
    
    def display_title(self):
        print("Title of the reel:", self.title)

    def display_description(self):
        print("Description of the reel:", self.description)

    def display_creator(self):
        print("Creator name:", self.creator_name)

    def display_location(self):
        print("Location:", self.location)

    def display_likes(self):
        print("Likes on the reel:", self.likes)

    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

    
    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)


reel1 = Instagram(
    "Dancing",
    "Dancing with friends",
    "Uday",
    "Bangalore"
)

reel2 = Instagram(
    "Finance Minister Conference",
    "Conference with officials",
    "Ravi",
    "Delhi"
)

reel1.liked()
reel1.liked()
reel1.add_comment("Nice dance!")
reel1.add_comment("Amazing energy")

reel2.liked()
reel2.add_comment("Very informative")

reel1.display_likes()
reel1.display_comments()

reel2.display_likes()
reel2.display_comments()

print("Reel1 ID:", id(reel1))
print("Reel2 ID:", id(reel2))

