class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)

    def display_father_name(self):
        print("The fathername is ", self.father_name)


class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)


child_obj=son("john", "N S","Shankar")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()
