
class Commentator:
    def __init__(self):
        self.comments = []

    def clear(self):
        self.comments.clear()

    def addComment(self, comment):
        self.comments.append(comment)

    def comment(self):
        for comment in self.comments:
            print(comment)
