# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Amount withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def display_balance(self):
#         print("Current balance:", self.balance)

# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, balance, interest_rate):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.balance += interest
#         print("Interest added:", interest)


# class CurrentAccount(BankAccount):
#     def __init__(self, account_holder, balance, overdraft_limit):
#         super().__init__(account_holder, balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw_with_overdraft(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             print("Amount withdrawn using overdraft:", amount)
#         else:
#             print("Overdraft limit exceeded")

# savings = SavingsAccount("Uday", 10000, 5)
# savings.deposit(2000)
# savings.add_interest()
# savings.withdraw(3000)
# savings.display_balance()

# print()

# current = CurrentAccount("Rahul", 5000, 3000)
# current.deposit(1000)
# current.withdraw_with_overdraft(7000)
# current.display_balance()


class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        self.display_person()
        print("Sport Name:", self.sport_name)


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        self.display_person()
        print("Student ID:", self.student_id)
        print("Sport Name:", self.sport_name)
        print("College Name:", self.college_name)

college_student = CollegeStudent(
    "Uday",
    "CS101",
    "Cricket",
    "VTU College"
)

college_student.display_college_student()
