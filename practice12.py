class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def pay(self):
        return self._salary

    def __str__(self):
        return self.name + " " + str(self.pay())


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):
        return self._salary + self.bonus


class Intern(Employee):
    def __init__(self, name, hours):
        super().__init__(name, 0)
        self.hours = hours

    def pay(self):
        return self.hours * 200


class Company:
    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def show_all(self):
        for person in self.people:
            print(person)

    def total_payroll(self):
        total = 0
        for person in self.people:
            total = total + person.pay()
        return total


company = Company()

company.add(Employee("Asha", 30000))
company.add(Manager("Rohit", 50000, 8000))
company.add(Intern("Kabir", 80))

company.show_all()

print("Total Payroll:", company.total_payroll())