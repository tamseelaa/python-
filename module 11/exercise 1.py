class Publication:
    def __init__(self,type_of_publication,name_of_publication):
        self.name=name_of_publication
        self.type=type_of_publication

    def print_info(self):
        print(f"\n\npublication of the {self.type} : {self.name}")
class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__("Book",name)
        self.author=author
        self.page_count=page_count
    def print_info(self):
        super().print_info()
        print(f"{self.name}(author {self.author},{self.page_count} pages) \n\n")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__("Magazine",name)
        self.chief_editor=chief_editor
        self.name=name

    def print_info(self):
        super().print_info()
        print(f"{self.name}(chief_editor {self.chief_editor})")

book=Book("Compartment No. 6","Rosa Liksom",192)
book.print_info()
magazine=Magazine("Donald Duck","Aki Hyyppa")
magazine.print_info()